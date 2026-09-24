#!/usr/bin/env node
// route-weight-budget.mjs — static per-route first-load weight budget check.
//
// Replaces the old perf-gate check that measured raw HTML bytes only. For each
// concrete route in performance-budgets.json it reads the built HTML from the
// dist directory, resolves the first-load assets the page references, and
// enforces every budget category:
//
//   html_kb_gzip         HTML document, gzip -9
//   css_kb_gzip          linked + inline CSS, gzip -9
//   js_kb_gzip           same-origin classic/module scripts + inline JS, gzip -9
//   font_kb_total        font files referenced by @font-face or font preloads (raw bytes)
//   above_fold_image_kb  first eager image (fetchpriority="high" wins), resolved candidate (raw bytes)
//   third_party_js_kb    external scripts; bytes are not fetched, so any non-allowlisted
//                        external script fails a zero budget and is reported as a count
//   total_weight_kb      html + css + js + fonts + all eager (non-lazy) images
//
// Text assets are gzip-compressed with zlib level 9 to approximate the transfer
// size. Images and fonts count raw bytes (already compressed formats). This is a
// deterministic build-time proxy; Lighthouse "total-byte-weight" is the lab
// cross-check. Background images set in CSS are not resolved (reported as a limit).
//
// Parametrised routes such as /blog/[slug]/ are gated through one representative built page
// per template (the budget's "representative" path, else the first matching built page in
// alphabetical order). A budgeted route that cannot be found in the build is NOT_ASSESSED and
// blocks (exit 4) unless the budget marks it "optional": true.
//
// A route total_weight_kb above the global total_weight_kb is an invalid budget (exit 3)
// unless the route carries an "exception_decision" path recording the decision entry.
//
// Usage:
//   node route-weight-budget.mjs --dist dist --budgets performance-budgets.json \
//        [--report reports/bundle/route-weight.json] [--allow .third-party-allowed]
//   node route-weight-budget.mjs --dist dist --budgets performance-budgets.json \
//        --emit-lhci-config reports/lighthouse/lighthouserc.generated.json \
//        --lhci-base lighthouserc.json [--port 4321]
//     (also writes the Lighthouse CI config: staticDistDir = --dist, one URL per resolved
//      route, and a per-route total-byte-weight assertion equal to the route budget)
// Exit codes: 0 pass, 2 budget exceeded, 3 usage/prerequisite/invalid budget, 4 a budgeted
// route was not assessed.

import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

function parseArgs(argv) {
  const args = { dist: 'dist', budgets: 'performance-budgets.json', report: null, allow: '.third-party-allowed' };
  for (let i = 2; i < argv.length; i += 1) {
    const key = argv[i];
    const value = argv[i + 1];
    if (!key.startsWith('--') || value === undefined) {
      throw new Error(`bad argument: ${key}`);
    }
    args[key.slice(2)] = value;
    i += 1;
  }
  return args;
}

const KB = 1024;
const gzipSize = (buf) => zlib.gzipSync(buf, { level: 9 }).length;
const TEXT_EXT = new Set(['.html', '.htm', '.css', '.js', '.mjs', '.svg', '.json', '.txt']);

function attr(tag, name) {
  const re = new RegExp(`\\s${name}\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s>]+))`, 'i');
  const m = tag.match(re);
  return m ? (m[1] ?? m[2] ?? m[3]) : null;
}

function isExternal(url) {
  return /^(?:https?:)?\/\//i.test(url);
}

function resolveLocal(distDir, pageFile, url) {
  const clean = url.split('#')[0].split('?')[0];
  if (!clean || clean.startsWith('data:')) return null;
  const decoded = decodeURIComponent(clean);
  const target = decoded.startsWith('/')
    ? path.join(distDir, decoded)
    : path.join(path.dirname(pageFile), decoded);
  return path.resolve(target);
}

function pickSrcsetCandidate(srcset) {
  // Mobile viewport 412 CSS px at DPR 1.75 needs roughly 721 device px.
  const TARGET = 721;
  const candidates = srcset.split(',').map((part) => part.trim()).filter(Boolean).map((part) => {
    const [url, descriptor = '1x'] = part.split(/\s+/);
    const w = descriptor.endsWith('w') ? parseInt(descriptor, 10) : null;
    const x = descriptor.endsWith('x') ? parseFloat(descriptor) : null;
    return { url, w, x };
  });
  if (!candidates.length) return null;
  const widths = candidates.filter((c) => c.w);
  if (widths.length) {
    widths.sort((a, b) => a.w - b.w);
    return (widths.find((c) => c.w >= TARGET) || widths[widths.length - 1]).url;
  }
  const dens = candidates.filter((c) => c.x);
  if (dens.length) {
    dens.sort((a, b) => a.x - b.x);
    return (dens.find((c) => c.x >= 1.75) || dens[dens.length - 1]).url;
  }
  return candidates[0].url;
}

function routeFile(distDir, route) {
  if (route.endsWith('.html')) return path.join(distDir, route);
  const trimmed = route.replace(/^\/+/, '');
  return path.join(distDir, trimmed, 'index.html');
}

function budgetFor(budgets, route) {
  const merged = { ...(budgets.global || {}), ...((budgets.routes || {})[route] || {}) };
  if (merged.image_above_fold_kb !== undefined && merged.above_fold_image_kb === undefined) {
    merged.above_fold_image_kb = merged.image_above_fold_kb;
  }
  const routeOverride = (budgets.routes || {})[route] || {};
  if (routeOverride.image_above_fold_kb !== undefined) merged.above_fold_image_kb = routeOverride.image_above_fold_kb;
  if (routeOverride.above_fold_image_kb !== undefined) merged.above_fold_image_kb = routeOverride.above_fold_image_kb;
  return merged;
}

function readAllowlist(file) {
  if (!file || !fs.existsSync(file)) return [];
  return fs.readFileSync(file, 'utf8').split(/\r?\n/)
    .map((line) => line.replace(/#.*/, '').trim().split(/\s+/)[0])
    .filter(Boolean);
}

function measureRoute(distDir, route, budget, allowlist) {
  const pageFile = routeFile(distDir, route);
  if (!fs.existsSync(pageFile)) {
    return { route, status: 'NOT_ASSESSED', reason: `built file not found: ${path.relative(distDir, pageFile)}` };
  }
  const html = fs.readFileSync(pageFile);
  const text = html.toString('utf8');
  const seen = new Set();
  const missing = [];
  const limits = [];
  const thirdPartyScripts = [];
  const totals = { html: gzipSize(html), css: 0, js: 0, font: 0, eagerImages: 0, aboveFoldImage: 0 };
  const cssTexts = [];

  const addFile = (url, kind) => {
    const file = resolveLocal(distDir, pageFile, url);
    if (!file) return 0;
    if (seen.has(file)) return 0;
    seen.add(file);
    if (!fs.existsSync(file) || !fs.statSync(file).isFile()) {
      missing.push(url);
      return 0;
    }
    const buf = fs.readFileSync(file);
    if (kind === 'css') cssTexts.push({ css: buf.toString('utf8'), file });
    return TEXT_EXT.has(path.extname(file).toLowerCase()) ? gzipSize(buf) : buf.length;
  };

  for (const tag of text.match(/<link\b[^>]*>/gi) || []) {
    const rel = (attr(tag, 'rel') || '').toLowerCase();
    const href = attr(tag, 'href');
    if (!href) continue;
    if (rel.split(/\s+/).includes('stylesheet')) {
      if (isExternal(href)) { limits.push(`external stylesheet not measured: ${href}`); continue; }
      totals.css += addFile(href, 'css');
    } else if (rel.includes('preload') && (attr(tag, 'as') || '').toLowerCase() === 'font') {
      if (isExternal(href)) { limits.push(`external font not measured: ${href}`); continue; }
      totals.font += addFile(href, 'font');
    } else if (rel.includes('modulepreload')) {
      if (!isExternal(href)) totals.js += addFile(href, 'js');
    }
  }

  for (const m of text.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)) {
    cssTexts.push({ css: m[1], file: pageFile });
  }

  for (const m of text.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    const tag = `<script${m[1]}>`;
    const src = attr(tag, 'src');
    const type = (attr(tag, 'type') || '').toLowerCase();
    if (src) {
      if (isExternal(src)) {
        let host = src;
        try { host = new URL(src.startsWith('//') ? `https:${src}` : src).origin; } catch { /* keep raw */ }
        const allowed = allowlist.some((origin) => src.startsWith(origin) || host === origin);
        thirdPartyScripts.push({ src, allowed });
      } else {
        totals.js += addFile(src, 'js');
      }
    } else if (!type || type === 'module' || type.includes('javascript')) {
      totals.js += m[2].trim() ? gzipSize(Buffer.from(m[2])) : 0;
    }
  }

  for (const { css, file } of cssTexts) {
    for (const block of css.match(/@font-face\s*{[^}]*}/gi) || []) {
      const urls = [...block.matchAll(/url\(\s*['"]?([^'")]+)['"]?\s*\)/gi)].map((u) => u[1]);
      // Browsers download the first supported format; count the first URL only.
      const first = urls.find((u) => !u.startsWith('data:'));
      if (!first) continue;
      if (isExternal(first)) { limits.push(`external font not measured: ${first}`); continue; }
      const resolved = first.startsWith('/') ? first : path.relative(path.dirname(pageFile), path.join(path.dirname(file), first)).split(path.sep).join('/');
      totals.font += addFile(resolved, 'font');
    }
    if (/background(?:-image)?\s*:[^;]*url\(/i.test(css)) {
      limits.push('CSS background images are not resolved by the static walker');
    }
  }

  // Images: picture/source first, then img. Lazy images are excluded from first load.
  const imageEvents = [];
  const pictureRanges = [];
  for (const m of text.matchAll(/<picture\b[\s\S]*?<\/picture>/gi)) {
    const block = m[0];
    const img = (block.match(/<img\b[^>]*>/i) || [''])[0];
    const source = (block.match(/<source\b[^>]*>/i) || [''])[0];
    const candidate = (source && attr(source, 'srcset')) ? pickSrcsetCandidate(attr(source, 'srcset'))
      : (attr(img, 'srcset') ? pickSrcsetCandidate(attr(img, 'srcset')) : attr(img, 'src'));
    imageEvents.push({ index: m.index, tag: img, url: candidate });
    pictureRanges.push([m.index, m.index + block.length]);
  }
  for (const m of text.matchAll(/<img\b[^>]*>/gi)) {
    if (pictureRanges.some(([a, b]) => m.index >= a && m.index < b)) continue;
    const tag = m[0];
    const url = attr(tag, 'srcset') ? pickSrcsetCandidate(attr(tag, 'srcset')) : attr(tag, 'src');
    imageEvents.push({ index: m.index, tag, url });
  }
  imageEvents.sort((a, b) => a.index - b.index);
  const eager = imageEvents.filter((e) => e.url && (attr(e.tag, 'loading') || '').toLowerCase() !== 'lazy');
  const hero = eager.find((e) => (attr(e.tag, 'fetchpriority') || '').toLowerCase() === 'high') || eager[0];
  for (const e of eager) {
    if (isExternal(e.url)) { limits.push(`external image not measured: ${e.url}`); continue; }
    const size = addFile(e.url, 'image');
    totals.eagerImages += size;
    if (e === hero) totals.aboveFoldImage = size;
  }

  const kb = (bytes) => Math.round((bytes / KB) * 10) / 10;
  const measured = {
    html_kb_gzip: kb(totals.html),
    css_kb_gzip: kb(totals.css),
    js_kb_gzip: kb(totals.js),
    font_kb_total: kb(totals.font),
    above_fold_image_kb: kb(totals.aboveFoldImage),
    eager_images_kb: kb(totals.eagerImages),
    total_weight_kb: kb(totals.html + totals.css + totals.js + totals.font + totals.eagerImages),
    third_party_scripts: thirdPartyScripts.length,
  };

  const failures = [];
  const check = (key) => {
    const limit = budget[key];
    if (typeof limit !== 'number') return;
    if (measured[key] > limit) failures.push(`${key} ${measured[key]} KB > budget ${limit} KB`);
  };
  ['html_kb_gzip', 'css_kb_gzip', 'js_kb_gzip', 'font_kb_total', 'above_fold_image_kb', 'total_weight_kb'].forEach(check);
  const unallowed = thirdPartyScripts.filter((s) => !s.allowed);
  if (typeof budget.third_party_js_kb === 'number' && budget.third_party_js_kb === 0 && unallowed.length) {
    failures.push(`third_party_js_kb budget is 0 but ${unallowed.length} non-allowlisted external script(s) found: ${unallowed.map((s) => s.src).join(', ')}`);
  }
  if (thirdPartyScripts.some((s) => s.allowed)) {
    limits.push('allowlisted third-party script bytes are NOT_ASSESSED statically; use Lighthouse third-parties-insight');
  }
  if (missing.length) failures.push(`referenced asset(s) missing from dist: ${missing.join(', ')}`);

  return {
    route,
    file: path.relative(distDir, pageFile).split(path.sep).join('/'),
    status: failures.length ? 'FAIL' : 'PASS',
    measured,
    budget,
    failures,
    limits: [...new Set(limits)],
  };
}


function walkIndexRoutes(distDir) {
  const found = [];
  const walk = (dir) => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (entry.name === 'index.html') {
        const rel = path.relative(distDir, path.dirname(full)).split(path.sep).join('/');
        found.push(rel ? `/${rel}/` : '/');
      }
    }
  };
  walk(distDir);
  return found.sort();
}

function templateRegex(template) {
  const parts = template.split(/\[[^\]]*\]/).map((part) => part.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
  return new RegExp(`^${parts.join('[^/]+')}$`);
}

function discoverRoutes(distDir, budgets) {
  const built = walkIndexRoutes(distDir);
  const entries = [];
  const names = Object.keys(budgets.routes || {});
  if (!names.includes('/')) names.unshift('/');
  for (const template of names) {
    const cfg = (budgets.routes || {})[template] || {};
    const optional = cfg.optional === true;
    if (!template.includes('[')) {
      entries.push({ template, route: template, budget: budgetFor(budgets, template), optional, resolved: true });
      continue;
    }
    const explicit = cfg.representative;
    const candidates = built.filter((r) => templateRegex(template).test(r));
    const chosen = explicit ? (built.includes(explicit) ? explicit : null) : candidates[0];
    entries.push({ template, route: chosen || template, budget: budgetFor(budgets, template), optional,
      resolved: Boolean(chosen), representative_of: template });
  }
  return entries;
}

function validateBudgets(budgets) {
  const problems = [];
  const globalTotal = (budgets.global || {}).total_weight_kb;
  for (const [route, cfg] of Object.entries(budgets.routes || {})) {
    if (typeof cfg.total_weight_kb === 'number' && typeof globalTotal === 'number'
        && cfg.total_weight_kb > globalTotal && !cfg.exception_decision) {
      problems.push(`${route}: total_weight_kb ${cfg.total_weight_kb} exceeds the global ${globalTotal}; add "exception_decision" with the decision entry path or lower it`);
    }
  }
  return problems;
}

function emitLhciConfig(entries, budgets, args, distDir) {
  const base = JSON.parse(fs.readFileSync(args['lhci-base'], 'utf8'));
  const port = args.port || '4321';
  const ci = base.ci;
  const resolved = entries.filter((e) => e.resolved);
  ci.collect.staticDistDir = distDir;
  ci.collect.url = resolved.map((e) => `http://localhost:${port}${e.route}`);
  const baseAssert = ci.assert || {};
  const shared = { ...(baseAssert.assertions || {}) };
  delete shared['total-byte-weight'];
  const globalTotal = (budgets.global || {}).total_weight_kb;
  const matrix = [{ matchingUrlPattern: '.*', preset: baseAssert.preset, assertions: shared }];
  for (const e of resolved) {
    const limitKb = typeof e.budget.total_weight_kb === 'number' ? e.budget.total_weight_kb : globalTotal;
    if (typeof limitKb !== 'number') continue;
    const literal = `http://localhost:${port}${e.route}`.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    matrix.push({ matchingUrlPattern: `^${literal}$`,
      assertions: { 'total-byte-weight': ['error', { maxNumericValue: Math.round(limitKb * 1024) }] } });
  }
  ci.assert = { assertMatrix: matrix };
  fs.mkdirSync(path.dirname(path.resolve(args['emit-lhci-config'])), { recursive: true });
  fs.writeFileSync(args['emit-lhci-config'], `${JSON.stringify(base, null, 2)}\n`);
}

function main() {
  let args;
  try {
    args = parseArgs(process.argv);
  } catch (err) {
    console.error(`route-weight-budget: ${err.message}`);
    return 3;
  }
  const distDir = path.resolve(args.dist);
  if (!fs.existsSync(distDir)) {
    console.error(`route-weight-budget: dist directory not found: ${distDir}`);
    return 3;
  }
  let budgets;
  try {
    budgets = JSON.parse(fs.readFileSync(args.budgets, 'utf8'));
  } catch (err) {
    console.error(`route-weight-budget: cannot read budgets: ${err.message}`);
    return 3;
  }
  const allowlist = readAllowlist(args.allow);
  const problems = validateBudgets(budgets);
  if (problems.length) {
    for (const problem of problems) console.error(`route-weight-budget: invalid budget: ${problem}`);
    return 3;
  }
  const entries = discoverRoutes(distDir, budgets);
  const results = entries.map((e) => {
    if (!e.resolved) {
      return { route: e.template, status: 'NOT_ASSESSED', optional: e.optional,
        reason: `no built page matches ${e.template}${e.optional ? ' (optional)' : ''}` };
    }
    const r = measureRoute(distDir, e.route, e.budget, allowlist);
    r.optional = e.optional;
    if (e.representative_of) r.representative_of = e.representative_of;
    return r;
  });
  if (args['emit-lhci-config']) {
    if (!args['lhci-base']) {
      console.error('route-weight-budget: --emit-lhci-config needs --lhci-base');
      return 3;
    }
    emitLhciConfig(entries, budgets, args, distDir);
  }
  const assessed = results.filter((r) => r.status !== 'NOT_ASSESSED');
  const failed = results.filter((r) => r.status === 'FAIL');
  const summary = {
    tool: 'route-weight-budget',
    evidence_type: 'static build analysis (gzip -9 proxy for text, raw bytes for images/fonts); not a browser measurement',
    dist: distDir,
    status: !assessed.length ? 'NOT_ASSESSED' : (failed.length ? 'FAIL' : (results.some((r) => r.status === 'NOT_ASSESSED' && !r.optional) ? 'NOT_ASSESSED' : 'PASS')),
    routes: results,
  };
  if (args.report) {
    fs.mkdirSync(path.dirname(path.resolve(args.report)), { recursive: true });
    fs.writeFileSync(args.report, `${JSON.stringify(summary, null, 2)}\n`);
  }
  for (const r of results) {
    if (r.status === 'NOT_ASSESSED') {
      console.log(`route-weight-budget: ${r.route} NOT_ASSESSED (${r.reason})`);
      continue;
    }
    const m = r.measured;
    console.log(`route-weight-budget: ${r.route} ${r.status} total=${m.total_weight_kb}KB html=${m.html_kb_gzip} css=${m.css_kb_gzip} js=${m.js_kb_gzip} fonts=${m.font_kb_total} hero=${m.above_fold_image_kb} 3p-scripts=${m.third_party_scripts}`);
    for (const f of r.failures) console.error(`  FAIL ${f}`);
    for (const l of r.limits) console.log(`  LIMIT ${l}`);
  }
  const blocked = results.filter((r) => r.status === 'NOT_ASSESSED' && !r.optional);
  if (!assessed.length) {
    console.error('route-weight-budget: no budgeted route was found in the build; nothing assessed');
    return 4;
  }
  if (failed.length) return 2;
  if (blocked.length) {
    console.error(`route-weight-budget: NOT_ASSESSED blocks release for: ${blocked.map((r) => r.route).join(', ')} (mark a route "optional": true in the budgets, with a decision entry, if the site has no such page)`);
    return 4;
  }
  return 0;
}

process.exitCode = main();
