# Performance Gate — Reference

Parent skill: [deploy](../SKILL.md). Read when running, configuring, explaining
or triaging the canonical performance gate, or when a client asks what "fast
enough to ship" means on this engine.

The gate is the machine-enforced answer to "is this site fast enough to ship?"
It is a **lab** gate. It blocks deploy. It does not prove that real visitors
have a good experience; field data at the 75th percentile decides that after
launch (see [lab-to-field calibration](lab-to-field-calibration.md)).

> Lab gates block deploy; field p75 decides success.

## Canonical Command

```bash
# From a client project root after resolving this engine as WEBSITE_SKILLS
bash "$WEBSITE_SKILLS/scripts/perf-gate.sh"
```

The script:

1. Checks `DIST_DIR` (default `./dist`) exists and the budgets and Lighthouse
   base config are readable.
2. Runs the HTML performance lint, `scripts/html-perf-lint.mjs`. It fails on
   classic scripts in `<head>` without `defer`/`async`/`type="module"`, images
   and iframes without dimensions, `loading="lazy"` on the hero image, and
   `document.write`. The hero is the image marked `fetchpriority="high"` or
   `data-hero`; if none is marked, the image with the largest declared size
   (a small logo that happens to come first is never treated as the hero).
   Its result is enforced at step 6, after the other gates report.
3. Runs `scripts/route-weight-budget.mjs`, which resolves every budgeted route
   (a template such as `/blog/[slug]/` uses one representative built page),
   reads the built page, resolves the CSS, JS, fonts and eager images it
   references, and enforces every category in `performance-budgets.json` (see
   "Weight budgets" below). A budgeted route that is not built is
   `NOT_ASSESSED` and blocks release.
4. Writes `reports/lighthouse/lighthouserc.generated.json` from that same
   route list: `staticDistDir` is `DIST_DIR`, there is one URL per resolved
   route (templates included), and each route carries its own
   `total-byte-weight` assertion equal to its budget.
5. Runs Lighthouse CI (`@lhci/cli autorun`) with the generated config: three
   runs per URL, median used for assertions. Results go to
   `reports/lighthouse/` and `reports/bundle/route-weight.json`.
6. Exits non-zero on any failure (1 Lighthouse, 2 weight budget or unbuilt
   route, 5 HTML lint); the deploy job must depend on `perf-gate`.

## Lighthouse version and scoring (checked 2026-09-23)

| Fact | Value | Source |
|---|---|---|
| Latest Lighthouse release | 13.5.0 (2026-09-18); major 13 since 2025-10-10 | SRC-LH-RELEASES (currentness register CW-03) |
| Lighthouse bundled by `@lhci/cli` 0.15.1 | 12.6.1 | npm registry metadata, read 2026-09-23 |
| Performance score weights | TBT 30, LCP 25, CLS 25, FCP 10, Speed Index 10 | SRC-LH-CONFIG, default-config.js |
| INP in the score | weight 0; not measured in navigation mode | SRC-LH-CONFIG; CW-03 |
| Default mobile throttling | 150 ms RTT, 1.6 Mbps down, 750 Kbps up, 4x CPU | SRC-LH-THROTTLING (CW-04) |

Rules:

- Record the Lighthouse version, the throttling profile, the run count and the
  `benchmarkIndex` with every gate report. Audit names and weights change
  between versions.
- Lighthouse 13 replaced many legacy audits with "performance insights".
  `lighthouserc.json` asserts the insight audits (`image-delivery-insight`,
  `document-latency-insight`, `font-display-insight`, `viewport-insight`,
  `render-blocking-insight`, `lcp-discovery-insight`,
  `network-dependency-tree-insight`, `third-parties-insight`,
  `legacy-javascript-insight`, `duplicated-javascript-insight`) and switches the
  retired legacy ids off. On 2026-09-24 the configuration was checked with
  `lhci assert` against real reports from Lighthouse 12.6.1 and 13.5.0; both
  produced the same assertion set, with no `auditRan` failures.
- Never promise a client a Lighthouse score. Promise the engine's lab gates
  before launch and "good" Core Web Vitals at p75 of field data after launch,
  where field data exists.

## Thresholds That Block Deploy

| Category | Threshold | Evidence class | Enforced by |
|---|---|---|---|
| Performance score | >= 95 | lab, stress profile | Lighthouse CI |
| Accessibility score | >= 95 | lab | Lighthouse CI (plus the a11y gate) |
| Best Practices score | >= 95 | lab | Lighthouse CI |
| SEO score | = 100 | lab | Lighthouse CI |
| LCP | <= 2.0 s (1.8 s on `/`) | lab, stress profile | Lighthouse CI |
| TBT (lab proxy for responsiveness) | <= 200 ms | lab | Lighthouse CI |
| CLS | <= 0.1 | lab and field | Lighthouse CI; RUM |
| INP | <= 200 ms at p75 | **field only** | RUM / CrUX via `observability` |
| HTML (gzip) | <= 30 KB | static build | route-weight-budget |
| JS (gzip, first load) | <= 80 KB (60 KB on `/`) | static build | route-weight-budget |
| CSS (gzip, first load) | <= 30 KB | static build | route-weight-budget |
| Fonts | <= 80 KB per page | static build | route-weight-budget |
| Above-fold image | <= 200 KB (150 KB on `/`) | static build | route-weight-budget |
| Total first-load weight | <= 350 KB (a route may only go lower, never higher, without a recorded exception) | static build + lab | route-weight-budget; Lighthouse `total-byte-weight` per route |
| Third-party runtime JS | 0, unless allowlisted with a reason | static build | route-weight-budget; `audit-third-party-js.sh` |

Core Web Vitals "good" thresholds for field data (web.dev, checked 2026-09-23;
register CW-01): LCP <= 2.5 s, INP <= 200 ms, CLS <= 0.1, each at the 75th
percentile per device class. INP replaced FID on 12 March 2024 (CW-02); remove
any FID threshold you find.

Why INP is not asserted in the lab: Lighthouse navigation runs contain no real
user interaction, so there is no INP value to assert. An assertion on
`interaction-to-next-paint` either never evaluates or fails spuriously. TBT is
the lab proxy. For key interactions (menu, filter, form submit) an optional
Lighthouse user-flow or timespan run can exercise real input; treat its result
as diagnostic, not as field proof.

## Network Profile

Blocking runs use the engine's low-end **stress profile**: WebPageTest "3G"
network values (1.6 Mbps down, 768 Kbps up, 300 ms RTT) with a 4x CPU slowdown
and Lighthouse's mobile screen emulation. It is harsher than Lighthouse's own
default mobile profile and much slower than measured median mobile in some
markets. It is not a median. See [Africa calibration](africa-calibration.md)
for the evidence and wording rules. For comparison with PageSpeed Insights lab
data, run the advisory `lighthouserc.default-mobile.json`.

## Weight budgets

`scripts/route-weight-budget.mjs` measures each concrete route in
`performance-budgets.json`:

| Measured | Method |
|---|---|
| HTML, CSS, JS | gzip level 9 of the built file (inline `<style>` and `<script>` included) |
| Fonts | raw bytes of the first `url()` in each `@font-face` and of font preloads |
| Above-fold image | the `fetchpriority="high"` image, else the first eager image; `srcset` candidate chosen for a 412 px viewport at DPR 1.75; `<picture>` uses its first `<source>` |
| Total | HTML + CSS + JS + fonts + all eager (non-lazy) images |
| Third-party scripts | counted; any non-allowlisted external script fails a zero budget; allowlisted script bytes are `NOT_ASSESSED` statically |

Known limits (reported in the JSON as `limits`): CSS background images and
external stylesheets or fonts are not measured statically; Lighthouse's
`total-byte-weight` and `third-parties-insight` cover them in the lab run. A
route listed in the budgets but not built is `NOT_ASSESSED` and blocks release
(exit 2 from `perf-gate.sh`), unless the budget marks it `"optional": true`
with a decision entry; if no budgeted route exists at all, the gate fails.

## Failure Triage

| Symptom | First place to look |
|---|---|
| LCP regression | Is the LCP element a real `<img>` in the initial HTML? Eager with `fetchpriority="high"`? Responsive candidate within budget? Render-blocking CSS or head scripts? TTFB and cold-connection cost (see below) |
| Weight overshoot | `reports/bundle/route-weight.json` per category; new dependencies; unsubsetted fonts; hero candidate too large |
| CLS regression | images or iframes without `width`/`height`; injected banners without reserved space; font swap without metric-matched fallback |
| TBT regression (and field INP) | hydration cost, heavy handlers, per-keystroke work, third-party scripts at first interaction; see [INP-safe interaction patterns](../../../build/page-builder/references/inp-safe-interaction-patterns.md) |
| SEO score dropped | missing meta, duplicate titles, `hreflang` gaps |
| Lighthouse fails with `auditRan` | the bundled Lighthouse version changed; map the retired audit to its insight and record a decision entry |

Cold-connection arithmetic for the stress profile: DNS, the TCP handshake (one
round trip) and TLS 1.3 (one more) cost several hundred milliseconds at 300 ms
RTT before the first HTML byte. Every extra origin repeats part of that cost.
Keep critical resources on the first-party origin.

### LCP checklist

1. The LCP element is a real `<img>` in the initial HTML (not a CSS background,
   not injected by JS), so the browser's preload scanner can find it.
2. Never put `loading="lazy"` on the above-fold or LCP image.
3. Give it `fetchpriority="high"` (or a responsive preload) and explicit
   dimensions.
4. Serve a responsive candidate (`srcset` with `w` descriptors plus `sizes`) in
   a modern format within the above-fold budget.
5. No render-blocking third-party script in `<head>`; first-party scripts are
   `defer` or modules.
6. Critical CSS small or inlined within the CSS budget.
7. Web font preloaded (woff2, subset) with `font-display: swap` or `optional`
   and a metric-matched fallback.
8. TTFB: edge-cached HTML with revalidation (see
   [edge caching and delivery](edge-caching-and-delivery.md)).
9. Confirm with a filmstrip that the hero is visible in the first meaningful
   frame on the stress profile.

### CLS checklist

1. `width`/`height` (or CSS `aspect-ratio`) on every image, video and iframe.
2. Reserved space (min-height) for anything injected later: consent bars,
   embeds, async lists, lazy sections.
3. Skeletons that match final geometry.
4. Never insert content above what the user is reading.
5. Fixed dimensions for header, navigation and gallery containers.
6. Metric-matched font fallbacks (`size-adjust`, `ascent-override`; check
   current browser support before relying on them).
7. Animate only `transform` and `opacity`.

### Lighthouse run hygiene

1. Headless CI runs are canonical; DevTools-in-tab numbers are for local
   debugging only.
2. At least three runs; report the median.
3. Keep the profile fixed and named; record `benchmarkIndex` because "4x CPU"
   means different things on different runners.
4. Record the Lighthouse version with every report.

## Third-party cost

The default allowlist is empty. When a client insists on a third-party script,
follow [third-party cost measurement](third-party-cost-measurement.md): owner
and value, zero-JS alternative first (see
[third-party facades](../../../build/page-builder/references/third-party-facades.md)),
performance-tax A/B, slow-vendor (single point of failure) test, loading
strategy, allowlist line with owner and review date, and quarterly review.

```bash
bash "$WEBSITE_SKILLS/scripts/audit-third-party-js.sh" dist .third-party-allowed
```

## Font Performance

```bash
bash "$WEBSITE_SKILLS/scripts/check-font-performance.sh" dist
```

Enforces `font-display: swap` (or `optional`/`fallback`), font preloads, woff2
only, and total font weight under the budget.

## CI Integration

The canonical workflow at `templates/ci/website.yml` runs `perf-gate.sh` after
the build and before deploy. Node 18+ is required for the weight walker and
HTML lint. If any gate fails, deploy is skipped and the pull request is blocked.

## When Thresholds Change

Thresholds are part of the engine contract, not project-level tuning. Do not
relax them inside `lighthouserc.json` to hide a regression. If a page genuinely
needs a higher budget (a map-heavy page), add a route entry to
`performance-budgets.json` and a decision entry under `project-log/decisions/`.
When a score threshold conflicts with a measured field-CWV or UX improvement,
field evidence wins; log the waiver with owner and expiry.

## Related

- [Lab-to-field calibration](lab-to-field-calibration.md)
- [Third-party cost measurement](third-party-cost-measurement.md)
- [Edge caching and delivery](edge-caching-and-delivery.md)
- [Legacy-site performance audit](legacy-site-performance-audit.md)
- [AI-generated code performance review](../../../quality-gates/design-quality-score/references/ai-generated-code-performance-review.md)
- [RUM attribution and segmentation](../../../launch-ops/observability/references/rum-attribution-and-segmentation.md)
- `africa-excellence/references/low-bandwidth-patterns.md`
- Sources: Osmani, A. (2026) *Web Performance Engineering in the Age of AI*,
  O'Reilly Media (lab/field doctrine, budgets, third-party management, run
  hygiene); Grigorik, I. *High Performance Browser Networking*, O'Reilly
  (network cost model); Wagner, J. *Web Performance in Action*, Manning
  (budget enforcement). Volatile facts: `docs/source-registers/performance-currentness-2026-09-23.json`.
