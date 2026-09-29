#!/usr/bin/env node
// Validates the website data pack quality/slop-rules.website.json against the
// vendored chwezi-slop detector (M10-11-T03).
//
// The detector's own `--validate-registry` checks the registry against the design
// engine's fixtures and doctrine files, which are not vendored, and it does not
// validate `--extra-rules` packs. This script does the pack-side checks here:
//   1. the vendored registry is structurally valid (fixture and doctrine-file
//      checks excluded, exactly as the detector does at run time);
//   2. the pack loads (schema, data-only check kinds, ids unique against the registry);
//   3. every pack rule's doctrine_ref resolves to a heading in this engine;
//   4. every pack rule reports at least one finding on its flag fixture and none
//      on its pass fixture;
//   5. every line marked "flag" in a flag fixture is reported by some pack rule,
//      so each former hard-coded slop-scan pattern keeps a fixture line.
// Usage: node scripts/validate-slop-pack.mjs [--pack <json>] [--json]
// Exit codes: 0 valid; 1 invalid; 5 vendored detector unavailable (NOT_ASSESSED).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DETECTOR = process.env.CHWEZI_SLOP_DETECTOR
  ? path.resolve(process.env.CHWEZI_SLOP_DETECTOR)
  : path.join(ROOT, 'scripts', 'vendor', 'chwezi-slop', 'tools', 'slop-detector');

const args = process.argv.slice(2);
const packArg = args.includes('--pack') ? args[args.indexOf('--pack') + 1] : 'quality/slop-rules.website.json';
const asJson = args.includes('--json');
const PACK = path.resolve(ROOT, packArg);

async function main() {
  let registryMod, detectorMod;
  try {
    registryMod = await import(pathToFileURL(path.join(DETECTOR, 'lib', 'registry.mjs')).href);
    detectorMod = await import(pathToFileURL(path.join(DETECTOR, 'lib', 'detector.mjs')).href);
  } catch (e) {
    console.log(`NOT_ASSESSED: vendored detector unavailable at ${DETECTOR} (${e.message})`);
    return 5;
  }
  const { loadRegistry, validateRegistry, loadPack, anchorsOf, ENGINE_ROOT } = registryMod;
  const { runDetector } = detectorMod;
  const errors = [];
  const checked = [];

  const registry = loadRegistry();
  const structural = validateRegistry(registry, { root: ENGINE_ROOT }).filter((e) => !/fixture missing|doctrine_ref|doctrine marker/.test(e));
  errors.push(...structural.map((e) => `registry: ${e}`));

  let rules = [];
  try {
    rules = loadPack(PACK, registry.rules.map((r) => r.id));
  } catch (e) {
    errors.push(e.message);
  }

  const docCache = new Map();
  const flagHits = new Map();
  for (const rule of rules) {
    const [docPath, anchor] = rule.doctrine_ref.split('#');
    const abs = path.join(ROOT, docPath);
    if (!fs.existsSync(abs)) errors.push(`${rule.id}: doctrine_ref file missing ${docPath}`);
    else {
      if (!docCache.has(abs)) docCache.set(abs, anchorsOf(fs.readFileSync(abs, 'utf8')));
      if (!docCache.get(abs).anchors.has(anchor)) errors.push(`${rule.id}: doctrine_ref anchor #${anchor} not found in ${docPath}`);
    }
    for (const kind of ['flag', 'pass']) {
      const fixture = path.join(ROOT, rule.fixtures[kind]);
      if (!fs.existsSync(fixture)) { errors.push(`${rule.id}: ${kind} fixture missing ${rule.fixtures[kind]}`); continue; }
      const { report, exitCode } = await runDetector({ paths: [fixture], rule: [rule.id], tier: 'deep', noWaivers: true, extraRules: [PACK], failOn: 'warning', cwd: ROOT });
      if (exitCode === 1) { errors.push(`${rule.id}: detector error on ${rule.fixtures[kind]}: ${report.errors.join('; ')}`); continue; }
      const found = report.findings.filter((f) => f.rule === rule.id);
      if (kind === 'flag') {
        if (!found.length) errors.push(`${rule.id}: no finding on flag fixture ${rule.fixtures.flag}`);
        if (!flagHits.has(fixture)) flagHits.set(fixture, new Set());
        for (const f of found) flagHits.get(fixture).add(f.line);
      } else if (found.length) {
        errors.push(`${rule.id}: ${found.length} finding(s) on pass fixture ${rule.fixtures.pass} (line ${found.map((f) => f.line).join(', ')})`);
      }
    }
    checked.push(rule.id);
  }

  for (const [fixture, hits] of flagHits) {
    const lines = fs.readFileSync(fixture, 'utf8').split(/\r?\n/);
    lines.forEach((text, i) => {
      if (/(<!--|\/\*)\s*flag\s*(-->|\*\/)/.test(text) && !hits.has(i + 1)) {
        errors.push(`${path.relative(ROOT, fixture).split(path.sep).join('/')}:${i + 1}: marked "flag" but no pack rule reports it`);
      }
    });
  }

  const out = { pack: path.relative(ROOT, PACK).split(path.sep).join('/'), detector: path.relative(ROOT, DETECTOR).split(path.sep).join('/'), rules: checked.length, errors };
  if (asJson) console.log(JSON.stringify(out, null, 2));
  else {
    for (const e of errors) console.log(`FAIL ${e}`);
    console.log(`${errors.length ? 'FAIL' : 'PASS'}: ${checked.length} pack rules checked against ${registry.rules.length} registry rules`);
  }
  return errors.length ? 1 : 0;
}

main().then((code) => { process.exitCode = code; }, (e) => { console.error(`validate-slop-pack: ${e.stack || e.message}`); process.exitCode = 1; });
