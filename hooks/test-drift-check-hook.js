#!/usr/bin/env node
/**
 * test-drift-check-hook.js — direct unit test for drift-check-hook.js.
 * Run: node hooks/test-drift-check-hook.js
 */

'use strict';

const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

const HOOK = path.join(__dirname, 'drift-check-hook.js');
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

// Real run against the actual engine checkout: drift-check.sh should
// either PASS (exit 0 from the hook) or, if it finds real drift, still
// exit 0 in standard (default) profile — never block on a Stop hook by
// default.
{
  const start = Date.now();
  const r = runProcess({}, {}, path.join(__dirname, '..'));
  const elapsedMs = Date.now() - start;
  check('real run against engine checkout, standard profile — never blocks', r.code === 0, `exit=${r.code}, stderr=${r.stderr.slice(0, 300)}`);
  check('real run against engine checkout — completes within budget (<60s)', elapsedMs < 60000, `took ${elapsedMs}ms`);
}

// Run from a directory that is NOT an engine checkout (no git, no
// glossary.md) — the underlying script must fast-skip (exit 8), and the
// hook must translate that to a non-blocking no-op.
{
  const emptyDir = fs.mkdtempSync(path.join(os.tmpdir(), 'chwezi-drift-test-'));
  const r = runProcess({}, { SKILLS_DIR: emptyDir }, emptyDir);
  check('non-engine directory — skip classified as non-blocking pass-through', r.code === 0, `exit=${r.code}`);
  fs.rmSync(emptyDir, { recursive: true, force: true });
}

{
  const r = runProcess({}, { CHWEZI_QUALITY_GATES: 'off' }, path.join(__dirname, '..'));
  check('CHWEZI_QUALITY_GATES=off — no-op', r.code === 0, `exit=${r.code}`);
}

{
  const r = runProcess({}, { CHWEZI_QUALITY_GATE_PROFILE: 'minimal' }, path.join(__dirname, '..'));
  check('profile=minimal — no-op', r.code === 0, `exit=${r.code}`);
}

// In-process: strict profile blocks on a real fail classification.
// We can't cheaply force drift_check.py to fail without corrupting real
// engine docs, so this is tested against runDriftCheck's classification
// directly using a stub script substituted at the well-known path,
// mirroring the quality-gate test's approach.
{
  const mod = require('./drift-check-hook.js');
  const realScriptPath = path.join(__dirname, '..', 'scripts', 'drift-check.sh');
  const backupPath = realScriptPath + '.bak-test';
  fs.copyFileSync(realScriptPath, backupPath);
  try {
    fs.writeFileSync(realScriptPath, '#!/usr/bin/env bash\necho "simulated drift finding"\nexit 3\n');
    const result = mod.runDriftCheck(path.join(__dirname, '..'));
    check('runDriftCheck — non-8 non-zero exit classified as fail', result.status === 'fail', JSON.stringify(result));

    fs.writeFileSync(realScriptPath, '#!/usr/bin/env bash\nexit 8\n');
    const skipResult = mod.runDriftCheck(path.join(__dirname, '..'));
    check('runDriftCheck — exit 8 classified as skip', skipResult.status === 'skip', JSON.stringify(skipResult));

    fs.writeFileSync(realScriptPath, '#!/usr/bin/env bash\nexit 0\n');
    const passResult = mod.runDriftCheck(path.join(__dirname, '..'));
    check('runDriftCheck — exit 0 classified as pass', passResult.status === 'pass', JSON.stringify(passResult));
  } finally {
    fs.copyFileSync(backupPath, realScriptPath);
    fs.rmSync(backupPath, { force: true });
  }
}

console.log(`\n${total - failures}/${total} passed`);
process.exit(failures > 0 ? 1 : 0);
