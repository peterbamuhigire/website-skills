# Experiment log

All changes were made after baseline commit `1f5db90`. The temporary practitioner sites, installed packages, browser reports and gate outputs remain outside the checkout. No production deployment or customer transaction occurred.

| ID / commit | Change and experiment | Result |
|---|---|---|
| WSK-01 / `e510d6b` | Added an explicit `browser.newContext()` → `context.newPage()` lifecycle in `scripts/a11y-page-context.mjs`; added tests for normal return and thrown scanner errors. | Node test: 2/2 pass. Exact locked gate (`@playwright/test` 1.64.1 and `@axe-core/playwright` 4.10.2) scans all five clean service routes with no serious/critical findings. The deliberate defect page returns critical and serious violations and fails as expected. A first run accidentally used the engine's default route list against the fixture; it was discarded, then repeated with the fixture's explicit routes file. |
| WSK-02 / `e85a746`, follow-up `ebce413` | Replaced regex-only SRI matching with `HTMLParser`-based classification of script and stylesheet assets. Canonical links and non-executable link relations are not assets. External script/style assets require a correctly sized SHA-256/384/512 digest and `crossorigin`. | Five parser tests pass. Clean service pages pass the SRI gate despite absolute canonical links. Defect page fails for its external script without valid SRI and `crossorigin`. The `security-gate.sh` still stops earlier at `npm audit`; its high advisory gate is not masked. |
| WSK-03 / `4351295` | Added bounded ecommerce guidance for static catalogues with seller-mediated enquiry/manual settlement; added three positive and a second owned-negative fixture and a fixture-coverage floor test. | Ecommerce coverage test passes with at least three positive and two owned-negative fixtures. Routing smoke: 37/40 rank-1 (92.5%), 40/40 top-three, 22/22 owned negatives, lint zero; the configured 92% rank-1 floor passes. The prior rank-1 ratio was 35/37 (94.6%), so the router did not improve on that metric. It is a lexical proxy, not live model evidence. |
| WSK-04 / `8cfb82f` | Rechecked and scoped SAI-018 against the official Google Search generative AI guide; refreshed its access/review dates and next review. | `validate-search-doctrine.py` and the targeted SAI-018 test pass. Claim wording is limited to Google Search. |
| WSK-05 / `1940e21`, `b6e5cdb` | Refreshed the overdue Anthropic model currentness entry and added official OpenAI catalogue, changelog, and Codex availability sources. | Current evidence supports retaining model-agnostic website skills and the active `gpt-6-luna` / high assignment. No paid model comparison was run; account entitlement, quality, cost, and latency comparison remain NOT_ASSESSED. |
| WSK-06 / `53dddac` | Added sibling lookup for the canonical `design-system-skills` repository name while retaining compatibility with the old `chwezi-design-engine` directory name. | Registry now reports eight routed design skills present by default on this checkout. Isolated regression tests cover both available and missing sibling cases. |
| WSK-07 / `dbc8b69` | Raised the drift walker's Markdown entry bound from 600 to 650 after the full suite found the eight new evidence/index pages took the checkout to 603 files; the existing 16 MiB byte bound is unchanged. | Focused drift regression passes; full suite passes with 138 tests; final drift check reports 603 Markdown files. |

## Practitioner tasks

### Service website

The disposable site has five pages and synthetic content. HTML performance lint passes on all five. Route-weight checks pass each route at 50.1 KB total, including 48.6 KB of local fonts; no JavaScript or third-party script bytes are reported by that gate. The fixed axe gate scans all five pages successfully. No real contact destination or service identity was supplied, so this remains a prototype.

Lighthouse CI ran three times per route (15 runs total) under the fixture's configured low-end mobile stress profile. All five route assertions fail the configured 2,000 ms maximum LCP. Across these retained results the reported values span 2,109.2901–2,418.24945 ms; FCP also fails its 1,500 ms assertion. The networking/render-blocking audit warnings are recorded but no threshold was changed. This is local lab evidence; field Core Web Vitals are NOT_ASSESSED.

### Static catalogue

The fixture presents synthetic catalogue content with disabled enquiry/payment controls and explicit missing inputs. New skill instructions require seller-approved destination and response owner before enabling enquiry, and verified provider, merchant, price, currency, stock, fulfilment, refund, reconciliation and access-control inputs before proposing manual settlement. This is guidance and a static artifact, not a live payment flow or validated commercial operation.

### Deliberately defective page

The accessibility gate detects one critical and two serious findings on the bad fixture and exits nonzero. Slop scan blocks three findings. HTML lint reports two errors: image dimensions absent and `document.write`. Metadata audit reports a four-character description plus missing canonical, social title, and image metadata. These are expected fixture failures, not defects in a real client website.

## Marketplace readiness

After implementation, Codex and Claude marketplace install/load/details checks both exit successfully for the local `chwezi-website` / `website` marketplace. The native runner used Podman containers with `--network none`, read-only checkout mounts and no model calls; checkout was clean at the time. This proves local manifest discovery and native install/load only. No public directory validation, publication, account-specific listing, or user configuration write was performed.
