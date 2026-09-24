#!/usr/bin/env node
// html-perf-lint.mjs — static HTML performance lint for built sites.
//
// Fails (exit 1) on patterns that reliably harm LCP, CLS or responsiveness:
//   HPL-001  classic <script src> in <head> without defer, async or type="module"
//   HPL-002  <img> or <iframe> without both width and height attributes
//            (an inline style with aspect-ratio also satisfies the rule)
//   HPL-003  loading="lazy" on the hero image
//   HPL-004  document.write in an inline script
// Warns (exit 0) on:
//   HPL-101  the hero image has no fetchpriority="high" and no data-hero marker
//   HPL-102  inline style sets a background-image on an element before the first <img>
//            (a CSS-background hero is invisible to the preload scanner)
//
// Hero detection (not "the first <img>", which is often a logo): every image marked
// fetchpriority="high" or data-hero is a hero. If none is marked, the hero is the image with
// the largest declared width x height (first in document order on a tie). Images without
// numeric dimensions cannot be ranked (they already fail HPL-002).
//
// Usage: node html-perf-lint.mjs <dist-dir> [--report reports/bundle/html-perf-lint.json]
// Exit codes: 0 pass (warnings allowed), 1 findings, 3 usage error.

import fs from 'node:fs';
import path from 'node:path';

function attr(tag, name) {
  const re = new RegExp(`\\s${name}(?:\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s>]+)))?(?=[\\s/>])`, 'i');
  const m = tag.match(re);
  if (!m) return null;
  return m[1] ?? m[2] ?? m[3] ?? '';
}

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, out);
    else if (/\.html?$/i.test(entry.name)) out.push(full);
  }
  return out;
}

function lintFile(file, root) {
  const html = fs.readFileSync(file, 'utf8');
  const rel = path.relative(root, file).split(path.sep).join('/');
  const findings = [];
  const add = (code, severity, message) => findings.push({ file: rel, code, severity, message });

  const headMatch = html.match(/<head\b[\s\S]*?<\/head>/i);
  const head = headMatch ? headMatch[0] : '';
  for (const m of head.matchAll(/<script\b([^>]*)>/gi)) {
    const tag = `<script${m[1]}>`;
    const src = attr(tag, 'src');
    const type = (attr(tag, 'type') || '').toLowerCase();
    if (!src) continue;
    if (type === 'module' || attr(tag, 'defer') !== null || attr(tag, 'async') !== null) continue;
    if (type && !type.includes('javascript')) continue;
    add('HPL-001', 'error', `render-blocking script in <head>: ${src} (add defer or async, or use type="module")`);
  }

  const images = [...html.matchAll(/<img\b[^>]*>/gi)];
  const marked = (tag) => (attr(tag, 'fetchpriority') || '').toLowerCase() === 'high' || attr(tag, 'data-hero') !== null;
  const area = (tag) => {
    const w = parseInt(attr(tag, 'width') || '', 10);
    const h = parseInt(attr(tag, 'height') || '', 10);
    return Number.isFinite(w) && Number.isFinite(h) ? w * h : 0;
  };
  let heroes = images.filter((m) => marked(m[0]));
  const hasMarker = heroes.length > 0;
  if (!hasMarker && images.length) {
    let best = null;
    for (const m of images) {
      if (area(m[0]) > (best ? area(best[0]) : 0)) best = m;
    }
    if (best) heroes = [best];
  }
  images.forEach((m) => {
    const tag = m[0];
    const label = attr(tag, 'src') || attr(tag, 'srcset') || '(no src)';
    const style = (attr(tag, 'style') || '').toLowerCase();
    if ((attr(tag, 'width') === null || attr(tag, 'height') === null) && !style.includes('aspect-ratio')) {
      add('HPL-002', 'error', `image without width and height: ${label}`);
    }
  });
  for (const m of heroes) {
    const tag = m[0];
    const label = attr(tag, 'src') || attr(tag, 'srcset') || '(no src)';
    if ((attr(tag, 'loading') || '').toLowerCase() === 'lazy') {
      add('HPL-003', 'error', `loading="lazy" on the hero image: ${label}`);
    }
    if (!hasMarker) {
      add('HPL-101', 'warn', `hero image (largest declared size) has no fetchpriority="high" or data-hero; confirm it is the LCP element and mark it: ${label}`);
    }
  }
  for (const m of html.matchAll(/<iframe\b[^>]*>/gi)) {
    const tag = m[0];
    const style = (attr(tag, 'style') || '').toLowerCase();
    if ((attr(tag, 'width') === null || attr(tag, 'height') === null) && !style.includes('aspect-ratio')) {
      add('HPL-002', 'error', `iframe without width and height: ${attr(tag, 'src') || '(no src)'}`);
    }
  }

  for (const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    if (/document\.write(?:ln)?\s*\(/.test(m[2])) add('HPL-004', 'error', 'document.write in inline script');
  }

  const firstImg = images.length ? images[0].index : html.length;
  const beforeHero = html.slice(0, firstImg);
  if (/style\s*=\s*["'][^"']*background(?:-image)?\s*:[^"']*url\(/i.test(beforeHero)) {
    add('HPL-102', 'warn', 'inline background-image before the first <img>; a CSS-background hero is not discoverable early');
  }
  return findings;
}

function main() {
  const args = process.argv.slice(2);
  const dist = args[0];
  const reportIndex = args.indexOf('--report');
  const report = reportIndex >= 0 ? args[reportIndex + 1] : null;
  if (!dist || !fs.existsSync(dist) || !fs.statSync(dist).isDirectory()) {
    console.error('html-perf-lint: usage: node html-perf-lint.mjs <dist-dir> [--report file]');
    return 3;
  }
  const files = walk(dist);
  const findings = files.flatMap((file) => lintFile(file, dist));
  const errors = findings.filter((f) => f.severity === 'error');
  for (const f of findings) {
    const line = `html-perf-lint: ${f.severity.toUpperCase()} ${f.code} ${f.file}: ${f.message}`;
    if (f.severity === 'error') console.error(line); else console.log(line);
  }
  const summary = { tool: 'html-perf-lint', files: files.length, errors: errors.length,
    warnings: findings.length - errors.length, status: errors.length ? 'FAIL' : 'PASS', findings };
  if (report) {
    fs.mkdirSync(path.dirname(path.resolve(report)), { recursive: true });
    fs.writeFileSync(report, `${JSON.stringify(summary, null, 2)}\n`);
  }
  console.log(`html-perf-lint: ${summary.status} (${files.length} HTML files, ${errors.length} errors, ${summary.warnings} warnings)`);
  return errors.length ? 1 : 0;
}

process.exitCode = main();
