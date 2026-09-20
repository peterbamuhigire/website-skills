#!/usr/bin/env node
/**
 * quality-gate.js — PostToolUse hook on Edit|Write|MultiEdit.
 *
 * Wraps this engine's existing shell gate scripts
 * (`scripts/a11y-gate.sh`, `scripts/design-quality-score.sh`,
 * `scripts/check-security-headers.sh`) so they fire automatically after a
 * relevant frontend file is touched, instead of only running when a human
 * remembers to invoke them. It does NOT reimplement their logic — it
 * shells out to the real scripts and translates their exit code and
 * stdout/stderr into the Claude Code PostToolUse hook contract.
 *
 * Why this is advisory (exit 0, warn) by default rather than a hard block:
 * all three underlying scripts need a built `dist/` directory, spin up a
 * local preview server, and shell out to `npx` (axe-core / serve), so a
 * single run can take anywhere from under a second (no dist yet — the
 * scripts themselves fast-exit with codes 3/4/5, see below) to well over a
 * minute (dist exists, full axe crawl + header probe). Blocking every Edit
 * on that latency, especially mid-build before `dist/` exists, would make
 * the engine unusable. The `strict` profile exists for teams that want a
 * hard gate anyway.
 *
 * Profile control (matches the ECC-style minimal/standard/strict pattern
 * referenced in this engine's kaizen backlog, WEB-3):
 *   CHWEZI_QUALITY_GATE_PROFILE=minimal   — hook is a no-op (fast exit 0)
 *   CHWEZI_QUALITY_GATE_PROFILE=standard  — (default) run gates that apply,
 *                                            report failures as warnings,
 *                                            never block
 *   CHWEZI_QUALITY_GATE_PROFILE=strict    — same runs, but a real gate
 *                                            FAILURE (not a missing
 *                                            prerequisite) blocks (exit 2)
 *
 * Kill switch: CHWEZI_QUALITY_GATES=off disables entirely (fail open).
 * Per-run budget: CHWEZI_QUALITY_GATE_TIMEOUT_MS (default 60000) — applied
 * per underlying script via spawnSync's timeout option; a script that
 * times out is treated as a skip (prerequisite/environment issue), not a
 * failure, since the network/tooling environment is outside this hook's
 * control.
 *
 * Each wrapped script already fast-exits when its prerequisite (a built
 * `dist/`, jq, npx) is missing — see the exit-code contracts in the
 * scripts' own headers. Those codes are treated as SKIP here, never as
 * FAIL, so the common case during iterative development (no build yet)
 * costs a few fast subprocess spawns, not a stalled edit loop.
 */

'use strict';

const path = require('path');
const fs = require('fs');
const { spawnSync } = require('child_process');

const SCRIPTS_DIR = path.join(__dirname, '..', 'scripts');
const MAX_STDIN = 1024 * 1024;

// Each gate: which edited-file extensions make it relevant, which script
// implements it, and which of that script's own exit codes mean "could not
// run" (prerequisite missing) rather than "ran and found a problem".
const GATES = [
  {
    name: 'a11y-gate',
    script: 'a11y-gate.sh',
    extensions: /\.(html?|astro|jsx|tsx|vue|svelte)$/i,
    skipExitCodes: new Set([3, 4]), // 3=prereq missing, 4=no dist/
    args: [],
  },
  {
    name: 'design-quality-score',
    script: 'design-quality-score.sh',
    extensions: /\.(css|scss|html?|astro|jsx|tsx|vue|svelte)$/i,
    skipExitCodes: new Set([5]), // 5=no dist/ (slop-scan-missing is a WARN in-script, not here)
    args: [],
  },
  {
    name: 'check-security-headers',
    script: 'check-security-headers.sh',
    extensions: /\.(html?|astro|conf|toml)$/i,
    skipExitCodes: new Set([3]), // 3=prereq or dist missing
    args: [],
  },
];

function readStdin() {
  try {
    return fs.readFileSync(0, 'utf8');
  } catch (e) {
    return '';
  }
}

function getFilePaths(input) {
  const toolInput = input && (input.tool_input || input.toolInput || input.input) || {};
  if (toolInput.file_path) return [String(toolInput.file_path)];
  if (Array.isArray(toolInput.edits)) {
    return toolInput.edits.map((e) => String((e && e.file_path) || '')).filter(Boolean);
  }
  return [];
}

function profile() {
  const p = (process.env.CHWEZI_QUALITY_GATE_PROFILE || 'standard').toLowerCase();
  return ['minimal', 'standard', 'strict'].includes(p) ? p : 'standard';
}

function timeoutMs() {
  const t = Number(process.env.CHWEZI_QUALITY_GATE_TIMEOUT_MS);
  return Number.isFinite(t) && t > 0 ? t : 60000;
}

function runGate(gate) {
  const scriptPath = path.join(SCRIPTS_DIR, gate.script);
  if (!fs.existsSync(scriptPath)) {
    return { name: gate.name, status: 'skip', reason: `${gate.script} not found` };
  }
  const result = spawnSync('bash', [scriptPath, ...gate.args], {
    cwd: process.cwd(),
    encoding: 'utf8',
    timeout: timeoutMs(),
    env: process.env,
  });

  if (result.error) {
    // bash unavailable, spawn failed, or timeout (result.error.code === 'ETIMEDOUT')
    return { name: gate.name, status: 'skip', reason: String(result.error.message || result.error) };
  }
  if (result.status === 0) {
    return { name: gate.name, status: 'pass' };
  }
  if (gate.skipExitCodes.has(result.status)) {
    return { name: gate.name, status: 'skip', reason: `exit ${result.status} (prerequisite not met)` };
  }
  return {
    name: gate.name,
    status: 'fail',
    reason: `exit ${result.status}`,
    detail: (result.stderr || result.stdout || '').trim().split('\n').slice(-10).join('\n'),
  };
}

function main() {
  if (['off', '0', 'false', 'disabled', 'disable'].includes((process.env.CHWEZI_QUALITY_GATES || '').toLowerCase())) {
    process.exit(0);
  }

  const currentProfile = profile();
  if (currentProfile === 'minimal') {
    process.exit(0);
  }

  const raw = readStdin();
  let payload;
  try {
    payload = JSON.parse(raw);
  } catch (e) {
    process.exit(0); // fail open on unparseable payload
  }

  const filePaths = getFilePaths(payload);
  if (filePaths.length === 0) process.exit(0);

  const applicable = new Map(); // gate name -> gate
  for (const fp of filePaths) {
    for (const gate of GATES) {
      if (gate.extensions.test(fp)) applicable.set(gate.name, gate);
    }
  }
  if (applicable.size === 0) process.exit(0);

  const results = [...applicable.values()].map(runGate);
  const failed = results.filter((r) => r.status === 'fail');
  const skipped = results.filter((r) => r.status === 'skip');
  const passed = results.filter((r) => r.status === 'pass');

  const lines = ['[quality-gate] frontend file edited — ran: ' + results.map((r) => r.name).join(', ')];
  for (const r of passed) lines.push(`  PASS ${r.name}`);
  for (const r of skipped) lines.push(`  SKIP ${r.name} (${r.reason})`);
  for (const r of failed) {
    lines.push(`  FAIL ${r.name} (${r.reason})`);
    if (r.detail) lines.push(r.detail.split('\n').map((l) => `    ${l}`).join('\n'));
  }

  if (failed.length === 0) {
    if (skipped.length > 0 || process.env.CHWEZI_QUALITY_GATE_VERBOSE) {
      console.error(lines.join('\n'));
    }
    process.exit(0);
  }

  console.error(lines.join('\n'));
  if (currentProfile === 'strict') {
    console.error(
      `\n[quality-gate] BLOCKED (strict profile) — ${failed.length} gate(s) failed on a real run ` +
      `(not a missing prerequisite). Fix the reported issue(s), or set ` +
      `CHWEZI_QUALITY_GATE_PROFILE=standard to make this advisory, or CHWEZI_QUALITY_GATES=off to disable.`
    );
    process.exit(2);
  }
  process.exit(0); // standard profile: advisory only
}

if (require.main === module) {
  main();
}

module.exports = { GATES, runGate, getFilePaths, profile, timeoutMs, main };
