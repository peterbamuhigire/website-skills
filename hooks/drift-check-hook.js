#!/usr/bin/env node
/**
 * drift-check-hook.js — Stop hook wrapping `scripts/drift-check.sh`.
 *
 * `drift-check.sh` (-> `drift_check.py`) is a bounded, deterministic check
 * over THIS ENGINE'S OWN tracked Markdown (SKILL.md files, glossary.md,
 * docs/doc-style-guide.md, etc. — see drift_check.py's SCOPE_EXCLUDED_PARTS
 * and REQUIRED_FILES). It is not a per-edited-file check and it is not a
 * check of whatever client project the engine has been installed into, so
 * it is wired to the Stop event (fires once per agent response, matching
 * ECC's "console.log audit: Stop hook checks all modified files after each
 * response" pattern) rather than to PostToolUse on every edit — running a
 * repo-wide Markdown scan after every single Edit would be wasted work
 * when a session touches the same doc many times in a row.
 *
 * It only does real work when invoked from within a checkout of this
 * engine (or with SKILLS_DIR pointed at one) — drift_check.py requires
 * `git` to enumerate tracked files and requires the engine's own
 * `glossary.md` / `docs/doc-style-guide.md` / `docs/deprecation-policy.md`
 * to exist (REQUIRED_FILES). When those aren't present — e.g. this hook
 * fires inside an installed client project rather than the engine repo
 * itself — the script exits fast with code 8 (prerequisite/runner error),
 * which this wrapper treats as SKIP, not FAIL.
 *
 * Profile control mirrors quality-gate.js:
 *   CHWEZI_QUALITY_GATE_PROFILE=minimal   — no-op
 *   CHWEZI_QUALITY_GATE_PROFILE=standard  — (default) run, warn, never block
 *   CHWEZI_QUALITY_GATE_PROFILE=strict    — run; a real drift finding
 *                                            (exit 1-7, 9) blocks (exit 2)
 * Kill switch: CHWEZI_QUALITY_GATES=off
 * Budget: CHWEZI_QUALITY_GATE_TIMEOUT_MS (default 60000)
 */

'use strict';

const path = require('path');
const fs = require('fs');
const { spawnSync } = require('child_process');

const SCRIPT_PATH = path.join(__dirname, '..', 'scripts', 'drift-check.sh');
const SKIP_EXIT_CODES = new Set([8]); // prerequisite or runner error

function profile() {
  const p = (process.env.CHWEZI_QUALITY_GATE_PROFILE || 'standard').toLowerCase();
  return ['minimal', 'standard', 'strict'].includes(p) ? p : 'standard';
}

function timeoutMs() {
  const t = Number(process.env.CHWEZI_QUALITY_GATE_TIMEOUT_MS);
  return Number.isFinite(t) && t > 0 ? t : 60000;
}

function runDriftCheck(cwd) {
  if (!fs.existsSync(SCRIPT_PATH)) {
    return { status: 'skip', reason: 'drift-check.sh not found' };
  }
  const result = spawnSync('bash', [SCRIPT_PATH], {
    cwd: cwd || process.cwd(),
    encoding: 'utf8',
    timeout: timeoutMs(),
    env: process.env,
  });

  if (result.error) {
    return { status: 'skip', reason: String(result.error.message || result.error) };
  }
  if (result.status === 0) {
    return { status: 'pass' };
  }
  if (SKIP_EXIT_CODES.has(result.status)) {
    return { status: 'skip', reason: `exit ${result.status} (prerequisite not met — not an engine checkout, or git/python3 unavailable)` };
  }
  return {
    status: 'fail',
    reason: `exit ${result.status}`,
    detail: (result.stdout || result.stderr || '').trim().split('\n').slice(-15).join('\n'),
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

  // drift-check-hook is stdin-agnostic (Stop payload carries no file info
  // we need), but Claude Code still sends a JSON payload on stdin for
  // Stop hooks — drain it defensively so the pipe never backs up, without
  // requiring it to parse.
  try {
    fs.readFileSync(0, 'utf8');
  } catch (e) {
    /* no stdin, or already drained — fine either way */
  }

  const result = runDriftCheck(process.env.SKILLS_DIR || path.join(__dirname, '..'));

  if (result.status === 'pass') {
    if (process.env.CHWEZI_QUALITY_GATE_VERBOSE) console.error('[drift-check] PASS — no blocking drift in engine docs.');
    process.exit(0);
  }
  if (result.status === 'skip') {
    if (process.env.CHWEZI_QUALITY_GATE_VERBOSE) console.error(`[drift-check] SKIP (${result.reason})`);
    process.exit(0);
  }

  console.error(`[drift-check] FAIL (${result.reason})`);
  if (result.detail) console.error(result.detail);

  if (currentProfile === 'strict') {
    console.error(
      '\n[drift-check] BLOCKED (strict profile) — engine documentation drift detected. ' +
      'Run `bash scripts/drift-check.sh` for the full report, or set ' +
      'CHWEZI_QUALITY_GATE_PROFILE=standard to make this advisory.'
    );
    process.exit(2);
  }
  process.exit(0);
}

if (require.main === module) {
  main();
}

module.exports = { runDriftCheck, profile, timeoutMs, main };
