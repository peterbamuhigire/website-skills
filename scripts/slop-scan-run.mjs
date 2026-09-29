#!/usr/bin/env node
// slop-scan-run.mjs: the Node half of scripts/slop-scan.sh (M10-11-T02, T13).
//
// Runs the chwezi-slop detector (vendored copy by default) over a built dist
// directory with the website data pack, writes the canonical JSON report and
// renders the Markdown report from it. It never re-implements a detector rule.
//
// Usage: node scripts/slop-scan-run.mjs <dist-dir> <reports-dir>
// Environment:
//   CHWEZI_SLOP_DETECTOR  a chwezi-design-engine checkout, its tools/slop-detector
//                         directory, or a cli.mjs path (skips the vendored hash check)
//   SLOP_RULES_PACK       data pack (default: <engine>/quality/slop-rules.website.json)
//   STRATEGY_BRIEF        strategy-brief artefact (default: ./project-artifacts/strategy-brief.json);
//                         pages that declare visitor_mode are scanned with --mode
// Exit codes: 0 clean; 1 blocking findings (block or warning); 5 NOT_ASSESSED
// (detector missing or tampered, pack invalid, operational failure).
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ENGINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const VENDOR = path.join(ENGINE, 'scripts', 'vendor', 'chwezi-slop');
const MODES = ['persuade', 'operate', 'read', 'experience'];

const [distArg, reportsArg] = process.argv.slice(2);
const DIST = path.resolve(distArg || 'dist');
const REPORTS = path.resolve(reportsArg || 'reports/design-quality');
const JSON_OUT = path.join(REPORTS, 'slop.json');
const MD_OUT = path.join(REPORTS, 'slop-scan.md');
const PACK = path.resolve(process.env.SLOP_RULES_PACK || path.join(ENGINE, 'quality', 'slop-rules.website.json'));
const posix = (p) => p.split(path.sep).join('/');
const display = (p) => { const rel = path.relative(process.cwd(), p); return rel && !rel.startsWith('..') && !path.isAbsolute(rel) ? posix(rel) : posix(p); };

function notAssessed(reason, extra = {}) {
  const report = {
    tool: 'chwezi-slop', wrapper: 'website-skills scripts/slop-scan.sh', status: 'NOT_ASSESSED', reason,
    findings: [], not_assessed: [{ rule: '*', reason }], waived: [], errors: [reason], exit_code: 5, ...extra,
  };
  fs.mkdirSync(REPORTS, { recursive: true });
  fs.writeFileSync(JSON_OUT, JSON.stringify(report, null, 2) + '\n');
  fs.writeFileSync(MD_OUT, renderMarkdown(report));
  console.error(`slop-scan: NOT_ASSESSED: ${reason}`);
  return 5;
}

function resolveDetector() {
  const override = process.env.CHWEZI_SLOP_DETECTOR;
  if (override) {
    const p = path.resolve(override);
    for (const c of [p, path.join(p, 'cli.mjs'), path.join(p, 'tools', 'slop-detector', 'cli.mjs')]) {
      if (c.endsWith('.mjs') && fs.existsSync(c)) return { cli: c, source: `CHWEZI_SLOP_DETECTOR (${posix(c)}); vendored hash check skipped` };
    }
    return { error: `CHWEZI_SLOP_DETECTOR does not point at a chwezi-slop cli.mjs: ${override}` };
  }
  const manifestPath = path.join(VENDOR, 'VENDOR.json');
  let manifest;
  try { manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8')); } catch (e) { return { error: `vendored detector manifest unreadable (${e.message})` }; }
  for (const [rel, want] of Object.entries(manifest.files || {})) {
    const file = path.join(VENDOR, rel);
    if (!fs.existsSync(file)) return { error: `vendored detector file missing: ${rel}` };
    const text = fs.readFileSync(file).toString('latin1').replace(/\r\n/g, '\n');
    const got = crypto.createHash('sha256').update(Buffer.from(text, 'latin1')).digest('hex');
    if (got !== want) return { error: `vendored detector file tampered (hash mismatch): ${rel}` };
  }
  return { cli: path.join(VENDOR, 'tools', 'slop-detector', 'cli.mjs'), source: `vendored copy of chwezi-design-engine@${manifest.source_commit}; hash check PASS` };
}

function routeToFile(route) {
  let r = String(route || '').split(/[?#]/)[0].replace(/^\/+/, '');
  if (r === '' || r.endsWith('/')) r += 'index.html';
  else if (!path.extname(r)) r += '/index.html';
  return path.join(DIST, r);
}

function pageModes() {
  const briefPath = path.resolve(process.env.STRATEGY_BRIEF || path.join('project-artifacts', 'strategy-brief.json'));
  if (!fs.existsSync(briefPath)) return { groups: new Map(), note: 'no strategy brief found; all pages scanned without --mode' };
  let brief;
  try { brief = JSON.parse(fs.readFileSync(briefPath, 'utf8')); } catch (e) { return { error: `strategy brief unreadable: ${e.message}` }; }
  const groups = new Map();
  for (const page of brief.pages || []) {
    if (!page.visitor_mode) continue;
    if (!MODES.includes(page.visitor_mode)) return { error: `strategy brief page ${page.route}: visitor_mode must be one of ${MODES.join(', ')}` };
    const file = routeToFile(page.route);
    if (!fs.existsSync(file)) continue;
    if (!groups.has(page.visitor_mode)) groups.set(page.visitor_mode, []);
    groups.get(page.visitor_mode).push(file);
  }
  return { groups, note: `visitor modes from ${display(briefPath)}` };
}

function listFiles(dir) {
  const out = [];
  for (const name of fs.readdirSync(dir).sort()) {
    const p = path.join(dir, name);
    if (fs.statSync(p).isDirectory()) out.push(...listFiles(p));
    else out.push(p);
  }
  return out;
}

function runCli(cli, targets, mode) {
  const args = [cli, '--json', '--tier', 'deep', '--fail-on', 'warning', '--extra-rules', PACK];
  if (mode) args.push('--mode', mode);
  args.push(...targets);
  // cwd = dist, so finding paths read as dist-relative (index.html:12).
  const res = spawnSync(process.execPath, args, { cwd: DIST, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
  let report = null;
  try { report = JSON.parse(res.stdout); } catch { /* handled below */ }
  return { status: res.status, report, stderr: res.stderr };
}

function renderMarkdown(r) {
  const lines = ['# Slop-Scan Report', '', `Scanned: ${display(DIST)}`, `Generated: ${r.generated || new Date().toISOString()}`,
    `Detector: ${r.detector_source || 'unavailable'}`, `Canonical report: ${display(JSON_OUT)}`, ''];
  if (r.status === 'NOT_ASSESSED') {
    lines.push('## Status', '', `**NOT_ASSESSED** (exit 5): ${r.reason}`, '', 'This is not a pass. Fix the prerequisite and re-run.', '');
    return lines.join('\n');
  }
  const failing = r.findings.filter((f) => f.severity !== 'advisory');
  const advisory = r.findings.filter((f) => f.severity === 'advisory');
  lines.push('## Blocking findings (block and warning)', '');
  if (!failing.length) lines.push('- none');
  for (const f of failing) lines.push(`- ${f.file}:${f.line ?? '-'} ${f.severity} \`${f.rule}\` [${f.as_overlay}]: ${f.message}`);
  lines.push('', '## Advisory findings (reported, never blocking)', '');
  if (!advisory.length) lines.push('- none');
  for (const f of advisory) lines.push(`- ${f.file}:${f.line ?? '-'} \`${f.rule}\`: ${f.message}`);
  lines.push('', '## Waived', '');
  if (!r.waived.length) lines.push('- none');
  for (const w of r.waived) lines.push(`- ${w.file}:${w.line ?? '-'} \`${w.rule}\`: ${w.waiver.reason}`);
  lines.push('', '## Not assessed', '');
  if (!r.not_assessed.length) lines.push('- none');
  for (const n of r.not_assessed) lines.push(`- \`${n.rule}\`: ${n.reason}`);
  lines.push('', '## Summary', '', `- Files scanned: ${r.scanned_files}`, `- Findings: block ${r.summary.by_severity.block}, warning ${r.summary.by_severity.warning}, advisory ${r.summary.by_severity.advisory}`,
    `- Waived: ${r.summary.waived}`, '', r.exit_code === 2 ? '**Status**: FAIL (exit 1)' : '**Status**: PASS (exit 0)', '');
  return lines.join('\n');
}

function merge(parts) {
  const base = { ...parts[0].report };
  base.findings = []; base.not_assessed = []; base.waived = []; base.errors = []; base.scanned_files = 0;
  const na = new Map();
  for (const { report, mode, files } of parts) {
    base.findings.push(...report.findings);
    base.waived.push(...report.waived);
    base.errors.push(...report.errors);
    base.scanned_files += report.scanned_files || 0;
    for (const n of report.not_assessed) if (!na.has(n.rule)) na.set(n.rule, n);
    (base.runs ||= []).push({ mode: mode || null, targets: files.map((f) => posix(path.relative(DIST, f)) || '.') });
  }
  base.not_assessed = [...na.values()];
  const bySev = { block: 0, warning: 0, advisory: 0 };
  const byRule = {};
  for (const f of base.findings) { bySev[f.severity]++; byRule[f.rule] = (byRule[f.rule] || 0) + 1; }
  base.summary = { findings: base.findings.length, waived: base.waived.length, not_assessed: base.not_assessed.length, by_severity: bySev, by_rule: byRule };
  base.exit_code = base.errors.length ? 1 : (bySev.block + bySev.warning) ? 2 : 0;
  return base;
}

function main() {
  if (!fs.existsSync(DIST) || !fs.statSync(DIST).isDirectory()) return notAssessed(`dist directory not found at ${DIST}`);
  if (!fs.existsSync(PACK)) return notAssessed(`website data pack missing at ${PACK}`);
  const det = resolveDetector();
  if (det.error) return notAssessed(det.error);
  const modes = pageModes();
  if (modes.error) return notAssessed(modes.error, { detector_source: det.source });

  const moded = new Set([...modes.groups.values()].flat());
  const rest = moded.size ? listFiles(DIST).filter((f) => !moded.has(f)) : [DIST];
  const plan = [];
  if (rest.length) plan.push({ mode: null, files: rest });
  for (const [mode, files] of [...modes.groups.entries()].sort()) plan.push({ mode, files });

  const parts = [];
  for (const step of plan) {
    const res = runCli(det.cli, step.files, step.mode);
    if (!res.report) return notAssessed(`detector produced no JSON report (exit ${res.status}): ${(res.stderr || '').trim().slice(0, 400)}`, { detector_source: det.source });
    if (res.status === 1 || (res.report.errors && res.report.errors.length)) {
      return notAssessed(`detector operational failure: ${(res.report.errors || []).join('; ') || (res.stderr || '').trim().slice(0, 400)}`, { detector_source: det.source });
    }
    parts.push({ report: res.report, mode: step.mode, files: step.files });
  }
  const report = parts.length === 1 && !parts[0].mode ? parts[0].report : merge(parts);
  report.detector_source = det.source;
  report.visitor_modes = modes.note;
  fs.mkdirSync(REPORTS, { recursive: true });
  fs.writeFileSync(JSON_OUT, JSON.stringify(report, null, 2) + '\n');
  fs.writeFileSync(MD_OUT, renderMarkdown(report));
  const s = report.summary.by_severity;
  console.log(`slop-scan: block ${s.block}, warning ${s.warning}, advisory ${s.advisory}; report ${display(JSON_OUT)}`);
  return report.exit_code === 2 ? 1 : 0;
}

process.exitCode = main();
