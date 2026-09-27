#!/usr/bin/env node
// Automated WCAG rule scan for each non-parameterized route in performance-budgets.json.
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { AxeBuilder } from '@axe-core/playwright';
import { chromium } from '@playwright/test';

const baseUrl = process.env.A11Y_BASE_URL;
const routesPath = process.env.ROUTES_FILE;
const reportDir = process.env.REPORTS_DIR;
if (!baseUrl || !routesPath || !reportDir) {
  console.error('a11y-gate: A11Y_BASE_URL, ROUTES_FILE, and REPORTS_DIR are required.');
  process.exit(3);
}

const routes = Object.keys(JSON.parse(fs.readFileSync(routesPath, 'utf8')).routes ?? {})
  .filter((route) => !route.includes('['));
if (routes.length === 0) {
  console.error(`a11y-gate: no concrete routes found in ${routesPath}`);
  process.exit(3);
}

fs.mkdirSync(reportDir, { recursive: true });
const summaryPath = path.join(reportDir, 'summary.md');
const rows = [];
let failed = false;
let browser;

const countImpact = (violations, impact) => violations.filter((violation) => violation.impact === impact).length;
const reportSlug = (route) => `root${route}`.replace(/[/?&#]/g, '_').replace(/_+$/g, '') || 'root';

try {
  browser = await chromium.launch({ headless: true });
  for (const route of routes) {
    const url = new URL(route, baseUrl).toString();
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    let results;
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 45_000 });
      results = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'])
        .analyze();
    } catch (error) {
      failed = true;
      results = { url, error: String(error?.stack ?? error), violations: [] };
    } finally {
      await page.close();
    }

    fs.writeFileSync(path.join(reportDir, `${reportSlug(route)}.json`), `${JSON.stringify([results], null, 2)}\n`);
    const violations = results.violations ?? [];
    const critical = countImpact(violations, 'critical');
    const serious = countImpact(violations, 'serious');
    const moderate = countImpact(violations, 'moderate');
    const minor = countImpact(violations, 'minor');
    rows.push(`| ${url} | ${critical} | ${serious} | ${moderate} | ${minor} |`);
    if (critical > 0 || serious > 0 || results.error) failed = true;
    console.log(`a11y-gate: ${route}: critical=${critical}, serious=${serious}, moderate=${moderate}, minor=${minor}${results.error ? ' (scan error)' : ''}`);
  }
} catch (error) {
  console.error(`a11y-gate: browser launch or route scan failed: ${String(error?.stack ?? error)}`);
  failed = true;
} finally {
  await browser?.close();
}

const generatedAt = new Date().toISOString();
fs.writeFileSync(summaryPath, [
  '# Accessibility Gate Summary',
  '',
  `Run: ${generatedAt}`,
  `Routes: ${routes.length}`,
  '',
  '| Route | Critical | Serious | Moderate | Minor |',
  '|---|---:|---:|---:|---:|',
  ...rows,
  '',
].join('\n'));

if (failed) {
  console.error(`a11y-gate: FAIL — scan errors or serious/critical violations present. See ${summaryPath}`);
  process.exit(1);
}
console.log(`a11y-gate: PASS — no serious or critical violations. Summary: ${summaryPath}`);
