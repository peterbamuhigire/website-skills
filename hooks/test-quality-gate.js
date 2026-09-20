#!/usr/bin/env node
/**
 * test-quality-gate.js — direct unit test for quality-gate.js.
 * Run: node hooks/test-quality-gate.js
 *
 * Covers the wrapper's own logic (matcher, profile, kill-switch, skip vs
 * fail classification) without depending on network access or a real
 * `dist/` build. Two kinds of cases:
 *   1. Process-level: spawn the real hook against real scripts with no
 *      dist/ present, and confirm it exits fast and does not block.
 *   2. In-process: exercise runGate()/getFilePaths()/profile() against a
 *      stub script directory so pass/skip/fail classification and the
 *      strict-profile block path are verified deterministically without
 *      needing axe-core, npx, or jq installed.
 */

'use strict';

const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

const HOOK = path.join(__dirname, 'quality-gate.js');
let failures = 0;
let total = 0;

function check(name, pass, extra) {
  total++;
  console.log(`${pass ? 'PASS' : 'FAIL'} — ${name}`);
  if (!pass && extra) console.log(`       ${extra}`);
  if (!pass) failures++;
}

function runProcess(payload, env = {}, cwd) {
  const result = spawnSync(process.execPath, [HOOK], {
    input: JSON.stringify(payload),
    encoding: 'utf8',
    cwd: cwd || process.cwd(),
    env: { ...process.env, ...env },
  });
  return { code: result.status, stderr: result.stderr || '', stdout: result.stdout || '' };
}

// ---------------------------------------------------------------------
// Process-level tests
// ---------------------------------------------------------------------

// A tmp dir with no dist/ — real scripts must fast-skip.
const tmpProject = fs.mkdtempSync(path.join(os.tmpdir(), 'chwezi-qg-test-'));

{
  const start = Date.now();
  const r = runProcess({ tool_input: { file_path: 'src/index.html' } }, {}, tmpProject);
  const elapsedMs = Date.now() - start;
  check('real run, no dist/, html file — exits 0 (never blocks on missing prerequisite)', r.code === 0, `exit=${r.code}`);
  check('real run, no dist/, html file — fast (<15s, no server spin-up)', elapsedMs < 15000, `took ${elapsedMs}ms`);
}

{
  const r = runProcess({ tool_input: { file_path: 'README.md' } }, {}, tmpProject);
  check('non-frontend file (.md) — no-op, exits 0', r.code === 0, `exit=${r.code}`);
}

{
  const r = runProcess({ tool_input: { file_path: 'src/index.html' } }, { CHWEZI_QUALITY_GATES: 'off' }, tmpProject);
  check('CHWEZI_QUALITY_GATES=off — no-op regardless of file type', r.code === 0, `exit=${r.code}`);
}

{
  const r = runProcess({ tool_input: { file_path: 'src/index.html' } }, { CHWEZI_QUALITY_GATE_PROFILE: 'minimal' }, tmpProject);
  check('profile=minimal — no-op', r.code === 0, `exit=${r.code}`);
}

{
  const r = runProcess('not json', {}, tmpProject);
  check('malformed stdin — fails open, exits 0', r.code === 0, `exit=${r.code}`);
}

fs.rmSync(tmpProject, { recursive: true, force: true });

// ---------------------------------------------------------------------
// In-process tests against the module's own functions, with stub scripts
// standing in for the slow real gates so pass/skip/fail/strict-block
// classification is verified without network access.
// ---------------------------------------------------------------------

const mod = require('./quality-gate.js');

check('getFilePaths — single file_path', (() => {
  const paths = mod.getFilePaths({ tool_input: { file_path: 'a.css' } });
  return paths.length === 1 && paths[0] === 'a.css';
})());

check('getFilePaths — edits array', (() => {
  const paths = mod.getFilePaths({ tool_input: { edits: [{ file_path: 'a.tsx' }, { file_path: 'b.html' }] } });
  return paths.length === 2 && paths.includes('a.tsx') && paths.includes('b.html');
})());

check('getFilePaths — neither shape present returns []', (() => {
  const paths = mod.getFilePaths({ tool_input: {} });
  return Array.isArray(paths) && paths.length === 0;
})());

check('profile() — defaults to standard', mod.profile() === 'standard');

{
  process.env.CHWEZI_QUALITY_GATE_PROFILE = 'strict';
  const ok = mod.profile() === 'strict';
  delete process.env.CHWEZI_QUALITY_GATE_PROFILE;
  check('profile() — honours strict', ok);
}

{
  process.env.CHWEZI_QUALITY_GATE_PROFILE = 'bogus';
  const ok = mod.profile() === 'standard';
  delete process.env.CHWEZI_QUALITY_GATE_PROFILE;
  check('profile() — falls back to standard on invalid value', ok);
}

// runGate() classification against stub scripts
const stubDir = fs.mkdtempSync(path.join(os.tmpdir(), 'chwezi-qg-stubs-'));
function writeStub(name, exitCode) {
  const p = path.join(stubDir, name);
  fs.writeFileSync(p, `#!/usr/bin/env bash\nexit ${exitCode}\n`);
  fs.chmodSync(p, 0o755);
  return p;
}

{
  // Simulate a passing gate by pointing runGate's script lookup at a stub.
  // runGate() resolves scripts relative to hooks/../scripts, so we test
  // the classification logic directly via spawnSync-equivalent behaviour
  // by constructing a fake gate object and calling runGate with SCRIPTS_DIR
  // monkey-patched via a temporary copy trick: write the stub INTO the
  // real scripts dir under a throwaway name, then restore.
  const realScriptsDir = path.join(__dirname, '..', 'scripts');
  const stubName = '__test-stub-quality-gate.sh';
  const stubPath = path.join(realScriptsDir, stubName);

  function withStub(exitCode, fn) {
    fs.writeFileSync(stubPath, `#!/usr/bin/env bash\nexit ${exitCode}\n`);
    fs.chmodSync(stubPath, 0o755);
    try {
      return fn();
    } finally {
      fs.rmSync(stubPath, { force: true });
    }
  }

  const passResult = withStub(0, () => mod.runGate({ name: 'stub', script: stubName, extensions: /.*/, skipExitCodes: new Set([3]), args: [] }));
  check('runGate — exit 0 classified as pass', passResult.status === 'pass', JSON.stringify(passResult));

  const skipResult = withStub(3, () => mod.runGate({ name: 'stub', script: stubName, extensions: /.*/, skipExitCodes: new Set([3]), args: [] }));
  check('runGate — declared skip-exit-code classified as skip', skipResult.status === 'skip', JSON.stringify(skipResult));

  const failResult = withStub(1, () => mod.runGate({ name: 'stub', script: stubName, extensions: /.*/, skipExitCodes: new Set([3]), args: [] }));
  check('runGate — undeclared non-zero exit classified as fail', failResult.status === 'fail', JSON.stringify(failResult));
}

fs.rmSync(stubDir, { recursive: true, force: true });

console.log(`\n${total - failures}/${total} passed`);
process.exit(failures > 0 ? 1 : 0);
