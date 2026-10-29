# Validation and currentness record

Access date for official sources in this record: 2026-10-29. Source URLs are official publisher or package-maintainer records unless marked otherwise. This is not a legal review or a claim that every security issue is resolved.

## Currentness sources

- Google Search Central's [generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) was opened and compared with SAI-018. The claim and register now explicitly apply to Google Search only. Search crawling, indexing, inclusion, and serving are not guaranteed by this claim.
- The official [Anthropic model system-card list](https://www.anthropic.com/system-cards) and [model deprecation table](https://docs.anthropic.com/en/docs/about-claude/model-deprecations) were checked. These list Sonnet 5.5, Opus 5.5, and Haiku 5.5 releases from September–October 2026. This is product catalogue evidence, not account entitlement.
- The official [OpenAI model catalogue](https://developers.openai.com/api/docs/models), [API changelog](https://developers.openai.com/api/docs/changelog), and [Codex availability help page](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) were checked. The catalogue lists GPT-6.1 Terra, GPT-6.1 Sol, GPT-6 Luna, and GPT-6 Astra; the changelog records Terra on 2026-10-26. Current Codex assignment is `gpt-6-luna` with high reasoning under machine policy. User-account entitlement was not checked, and no paid comparative model run was done. Website skills remain model-agnostic; no release-recency-only change was justified.
- Registry-currentness calls checked exact temporary lockfile packages with `npm view` and `npm audit` on 2026-10-29. The locked QA set uses `@lhci/cli` 0.15.1, `serve` 14.2.6, and Playwright Test 1.64.1; official package pages include [Lighthouse CI](https://www.npmjs.com/package/@lhci/cli), [serve](https://www.npmjs.com/package/serve), and [Playwright Test](https://www.npmjs.com/package/%40playwright/test). Registry package latest tags do not themselves prove a safe, compatible upgrade path.

## Security advisory applicability

The exact disposable QA lockfile audit reports **15 high-severity package vulnerability records and zero critical records**. These are records in the QA tool dependency graph, not 15 unique advisories and not proof of exposure in a deployed site. The direct advisory links found in that graph are [basic-ftp GHSA-c475-qrg2-pj4r](https://github.com/advisories/GHSA-c475-qrg2-pj4r), [compression GHSA-vc2v-76pw-4v95](https://github.com/advisories/GHSA-vc2v-76pw-4v95), [extract-zip GHSA-jmr9-qjv8-65gv](https://github.com/advisories/GHSA-jmr9-qjv8-65gv) and [GHSA-7pqw-9j4j-h8q3](https://github.com/advisories/GHSA-7pqw-9j4j-h8q3), [tmp GHSA-52f5-9888-hmc6](https://github.com/advisories/GHSA-52f5-9888-hmc6) and [GHSA-ph9p-34f9-6g65](https://github.com/advisories/GHSA-ph9p-34f9-6g65), and [zod GHSA-mrhx-c7xc-m3w5](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5). Severity and affected-version ranges differ by advisory; consult each record before remediation.

`npm audit fix` proposed a breaking update to the locked Lighthouse CI tool range; no compatible full remediation was established in this cycle. The release security gate remains blocked. No force upgrade or blanket security-clear claim was made. Local preview also fails the configured edge-header check; staging/production headers are NOT_ASSESSED.

## Relevant web standards and legal scope

- The official [web.dev Core Web Vitals thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds) describe field thresholds at the 75th percentile. Those are not interchangeable with this engine's 2,000 ms synthetic Lighthouse stress assertion. This cycle does not report field CWV.
- Google Search sources are authoritative only for Google Search. They do not establish behaviour of OpenAI, Bing, or other answer products. No universal AI visibility outcome is claimed.
- Privacy and policy content mentions multiple jurisdictions. Current official identifiers alone do not prove clause-level compliance or applicability to a particular site. Counsel review and processing-specific fact gathering remain NOT_ASSESSED.
- African language-speaker population claims are not required for the catalogue change and no source was found during preparation; none was added.

## Gate record

| Gate | Result after changes | Evidence scope |
|---|---|---|
| `validate-skill-registry.py` | PASS: 62 skills; eight routed design skills found | Default sibling discovery plus registry schema. |
| `website_fixture_benchmark.py` | PASS: two-page fixture; 2,026 bytes against 350 KB ceiling | Built-in lab fixture; field CWV NOT_ASSESSED. |
| `validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | PASS: 62 active, one template, zero contract debt | Static contracts. |
| `routing-smoke-test.py --min-rank1 92 --lint-fixtures` | PASS: 37/40 rank-1; 40/40 top-three; 22/22 owned negatives; zero lint | Lexical proxy only. |
| `validate-search-doctrine.py` | PASS: 18 canonical files, currentness verified | Search claim register and required doctrine anchors. |
| Full pytest suite | PASS: 137 tests | Temporary Python venv; no repo dependencies added. |
| `source_ingestion_guardrail.py` | PASS: zero findings | Checkout guardrail. |
| `check-vendored-detector.py --source ../design-system-skills` | PASS: 20-file manifest and source comparison | Explicit adjacent source checkout; source commit `3fe84a6dc22d954483e1afce06c3e9b53fc2f5ca`. |
| `validate-slop-pack.mjs` | PASS: 20 website rules checked against 49 registry rules | Pack schema and rule linkage. |
| `drift_check.py --root . --reports-dir ... --as-of 2026-10-29` | PASS: 598 Markdown files | Local cross-file drift validator. |
| Banned phrase test | PASS: 6/6 test cases | Includes expected positive and negative fixture outcomes. |
| A11y service fixture | PASS: five routes, no serious/critical issues | Exact locked browser and axe versions; lab-only. |
| A11y defect fixture | Expected FAIL: one critical and two serious | Intentional negative fixture. |
| SRI unit and service fixture | PASS: five tests; clean static site passes | External asset parsing and valid digest length checks. |
| SRI defect fixture | Expected FAIL: missing/invalid integrity and crossorigin | Intentional negative fixture. |
| Performance gate | FAIL: all five routes exceed LCP budget | 15 local lab runs; thresholds unchanged; field CWV NOT_ASSESSED. |
| Security gate | FAIL: npm audit detects high vulnerability records | Edge-header and production security remain open. |
| Visual QA wrapper | NOT_ASSESSED; exits 4 because task project lacks `tests/visual` | Engine checkout has no executable structure/capture specs. |
| Codex native marketplace | PASS | Isolated network-disabled Podman install/load/details run. |
| Claude native marketplace | PASS | Isolated network-disabled Podman install/load/details run. |
| Deployment and post-deploy smoke | NOT_ASSESSED | No deployment target or authorization was part of the task. |

## Size

Before source edits the checkout count was 837 full entries and 795 package-oriented entries, with zero symlinks. At the implementation checkpoint after seven source changes, the same counter reports 905 full entries and 803 package-oriented entries, with zero symlinks. Both remain well below the hard **5,000** entry cap. Counts include `.git` only in the full checkout measurement; the package-oriented count prunes `.git`, `.cache`, `.venv`, `venv`, `node_modules`, and `__pycache__`.
