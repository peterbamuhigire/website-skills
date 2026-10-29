# Validation and currentness record

Access date for official sources in this record: 2026-10-29. Source URLs are official publisher or package-maintainer records unless marked otherwise. This is not a legal review or a claim that every security issue is resolved.

## Currentness sources

- Google Search Central's [generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) was opened and compared with SAI-018. The claim and register now explicitly apply to Google Search only. Search crawling, indexing, inclusion, and serving are not guaranteed by this claim.
- The official [Anthropic model system-card list](https://www.anthropic.com/system-cards) and [model deprecation table](https://docs.anthropic.com/en/docs/about-claude/model-deprecations) were checked. These list Sonnet 5.5, Opus 5.5, and Haiku 5.5 releases from September–October 2026. This is product catalogue evidence, not account entitlement.
- The official [OpenAI model catalogue](https://developers.openai.com/api/docs/models), [API changelog](https://developers.openai.com/api/docs/changelog), and [Codex availability help page](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) were checked. The catalogue lists GPT-6.1 Terra, GPT-6.1 Sol, GPT-6 Luna, and GPT-6 Astra; the changelog records Terra on 2026-10-26. Current Codex assignment is `gpt-6-luna` with high reasoning under machine policy. User-account entitlement was not checked, and no paid comparative model run was done. Website skills remain model-agnostic; no release-recency-only change was justified.
- Registry-currentness calls checked exact temporary lockfile packages with `npm view` and `npm audit` on 2026-10-29. The locked QA set uses `@lhci/cli` 0.15.1, `serve` 14.2.6, and Playwright Test 1.64.1; official package pages include [Lighthouse CI](https://www.npmjs.com/package/@lhci/cli), [serve](https://www.npmjs.com/package/serve), and [Playwright Test](https://www.npmjs.com/package/%40playwright/test). Registry package latest tags do not themselves prove a safe, compatible upgrade path.

## Security advisory applicability

The exact disposable QA lockfile audit reports **15 high-severity package vulnerability records and zero critical records**. These are package records in the QA tool dependency graph, not 15 unique advisories and not proof of exposure in a deployed site. They resolve to these seven direct GHSA records: [basic-ftp GHSA-c475-qrg2-pj4r](https://github.com/advisories/GHSA-c475-qrg2-pj4r), [compression GHSA-vc2v-76pw-4v95](https://github.com/advisories/GHSA-vc2v-76pw-4v95), [extract-zip GHSA-jmr9-qjv8-65gv](https://github.com/advisories/GHSA-jmr9-qjv8-65gv) and [GHSA-7pqw-9j4j-h8q3](https://github.com/advisories/GHSA-7pqw-9j4j-h8q3), [tmp GHSA-52f5-9888-hmc6](https://github.com/advisories/GHSA-52f5-9888-hmc6) and [GHSA-ph9p-34f9-6g65](https://github.com/advisories/GHSA-ph9p-34f9-6g65), and [zod GHSA-mrhx-c7xc-m3w5](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5). The first tmp advisory is Low; the second is High. Aggregate audit records inherit findings through dependencies and do not each correspond to a separate GHSA.

### High package-record map

| Audit package record | Locked QA version / dependency path | Advisory or fixed-version fact | Compatibility decision |
|---|---|---|---|
| `@lhci/cli` | 0.15.1 direct; depends on `@lhci/utils`, Lighthouse 12.6.1, Inquirer, `proxy-agent`, `tmp`, and `uuid` ([npm](https://www.npmjs.com/package/%40lhci/cli)) | Aggregate of its vulnerable dependency records; audit's suggested fix is breaking `@lhci/cli` 0.1.0. | Current registry latest remains 0.15.1; forced downgrade rejected. |
| `@lhci/utils` | 0.15.1; depends on Lighthouse 12.6.1 ([npm](https://www.npmjs.com/package/%40lhci/utils)) | Aggregate through the pinned Lighthouse/Puppeteer chain. | No independent fix is published in the locked parent range. |
| `@puppeteer/browsers` | 2.13.2 under Puppeteer Core 24.43.1 ([npm](https://www.npmjs.com/package/%40puppeteer%2fbrowsers)) | Carries `extract-zip` and proxy-chain records. `extract-zip` advisory pages list no patched version. | Current browsers 2.x tree still includes vulnerable extract-zip 2.0.1; upstream patch unavailable at the check date. |
| `basic-ftp` | 5.3.1 under `get-uri` 6.0.5, whose dependency range is `^5.0.2` ([npm `get-uri`](https://www.npmjs.com/package/get-uri)) | GHSA affects `basic-ftp` through 6.2.0 and lists 6.2.1 as fixed; registry reports 6.2.3 ([npm](https://www.npmjs.com/package/basic-ftp)). | Fixed major 6 is outside the declared major-5 range; current `get-uri` 8.0.1 still declares `basic-ftp` `^5.3.1`. No compatible fix verified. |
| `chromium-bidi` | 14.0.0 under Puppeteer Core 24.43.1; declares Zod `^3.24.1` ([npm](https://www.npmjs.com/package/chromium-bidi)) | Zod advisory affects `<4.6.6`; npm registry reports 4.6.7 ([GitHub advisory](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5), [npm](https://www.npmjs.com/package/zod)). | Zod 4 is outside the declared major-3 range. Newer Chromium BiDi package lines use Zod 4 but are not the version pinned by this Puppeteer/Lighthouse chain. |
| `compression` | 1.8.1 nested under `serve` 14.2.6, which declares an exact 1.8.1 dependency ([npm](https://www.npmjs.com/package/serve)) | GHSA affects `<1.8.2`; fixed/current version is 1.8.2 ([GitHub advisory](https://github.com/advisories/GHSA-vc2v-76pw-4v95), [npm](https://www.npmjs.com/package/compression)). | Proven consumer-local override to `serve.compression` 1.8.2. The nested package dedupes to the already installed 1.8.2, removes the compression record, and passes normal/failure fixtures; the overall audit still has 13 high records. |
| `extract-zip` | 2.0.1 under `@puppeteer/browsers` 2.13.2 ([npm](https://www.npmjs.com/package/extract-zip)) | Both extract-zip GHSAs affect `<=2.0.1` and list no patched version. The registry latest remains 2.0.1. | No upstream fixed release available; cannot safely pin a nonexistent patched version. |
| `get-uri` | 6.0.5 under `pac-proxy-agent` 7.2.0 ([npm](https://www.npmjs.com/package/get-uri)) | Aggregate record from vulnerable `basic-ftp`; `get-uri` 8.0.1 still uses the major-5 basic-ftp line. | Updating `get-uri` within the locked proxy-agent range does not remove the vulnerable major-5 FTP dependency. |
| `lighthouse` | 12.6.1 exact dependency of `@lhci/cli` 0.15.1 ([npm](https://www.npmjs.com/package/lighthouse)) | Lighthouse audit range extends through 13.3.0; registry latest is 13.6.0. | The exact 12.6.1 parent pin prevents a compatible update; overriding to Lighthouse 13 crosses the locked LHCI contract and was not treated as safe. |
| `pac-proxy-agent` | 7.2.0 under Proxy Agent 6.5.0 ([npm](https://www.npmjs.com/package/pac-proxy-agent)) | Aggregate record via `get-uri` → basic-ftp. | Current proxy-agent range already resolves latest 7.x; FTP dependency remains on basic-ftp major 5. |
| `proxy-agent` | 6.5.0 under LHCI and Puppeteer ([npm](https://www.npmjs.com/package/proxy-agent)) | Aggregate record via `pac-proxy-agent` → `get-uri` → basic-ftp. | Latest 6.x in the locked parent range does not remove the vulnerable downstream dependency. |
| `puppeteer-core` | 24.43.1 under Lighthouse 12.6.1 ([npm](https://www.npmjs.com/package/puppeteer-core)) | Aggregate records through `@puppeteer/browsers` / extract-zip and Chromium BiDi / Zod. | Lighthouse pins `^24.10.0`; moving to Puppeteer 25.x requires crossing to a newer Lighthouse line and was not tested as a supported LHCI combination. |
| `serve` | 14.2.6 direct; exact nested compression 1.8.1 ([npm](https://www.npmjs.com/package/serve)) | High audit record is the compression GHSA above. Audit's auto-fix downgrades to breaking serve 10.0.2. | Keep serve 14.2.6 and use only the tested scoped compression patch in a consuming project; no serve downgrade. |
| `tmp` | Root 0.1.0 from LHCI `^0.1.0`, plus nested version under External Editor 3.1.0 which declares `^0.0.33` ([npm `@lhci/cli`](https://www.npmjs.com/package/%40lhci/cli), [npm `external-editor`](https://www.npmjs.com/package/external-editor)) | High GHSA affects `<0.2.6`, fixed version 0.2.6; 0.2.7 is current ([GitHub](https://github.com/advisories/GHSA-ph9p-34f9-6g65), [npm](https://www.npmjs.com/package/tmp)). The other tmp GHSA is Low, fixed at 0.2.4. | Fixed 0.2.x line is outside both declared 0.1.x and 0.0.x ranges. |
| `zod` | 3.25.76 under Chromium BiDi 14.0.0 ([npm `chromium-bidi`](https://www.npmjs.com/package/chromium-bidi)) | High GHSA affects `<4.6.6`, fixed 4.6.6; current 4.6.7 ([GitHub](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5), [npm](https://www.npmjs.com/package/zod)). | Major 4 is out of Chromium BiDi 14's declared `^3.24.1` range; no safe override verified. |

The full per-package audit JSON and experiment locks were retained outside the engine checkout. The table distinguishes the 15 high package records from the seven direct advisory records and records why remaining safe fixed versions cannot be applied within the locked parent ranges.

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
| `validate-checkout-size.py` | PASS: 945 full / 810 package entries at the recorded implementation checkpoint, zero symlinks; immutable 5,000 caps for each measure | Ten size-gate unit tests include exact 5,000 acceptance and 5,001 rejection for both measures, lower-limit fixtures, manifest identity/path parity, unreadable walks, and symlink escape. Runs in engine quality CI. |
| `website_fixture_benchmark.py` | PASS: two-page fixture; 2,026 bytes against 350 KB ceiling | Built-in lab fixture; field CWV NOT_ASSESSED. |
| `validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | PASS: 62 active, one template, zero contract debt | Static contracts. |
| `routing-smoke-test.py --min-rank1 92 --lint-fixtures` | PASS: 37/40 rank-1; 40/40 top-three; 22/22 owned negatives; zero lint | Lexical proxy only. |
| `validate-search-doctrine.py` | PASS: 18 canonical files, currentness verified | Search claim register and required doctrine anchors. |
| Full pytest suite | PASS: 153 tests after the SRI acceptance and exact-boundary size-gate regressions | Temporary Python venv; no repo dependencies added. |
| `source_ingestion_guardrail.py` | PASS: zero findings | Checkout guardrail. |
| `check-vendored-detector.py --source ../design-system-skills` | PASS: 20-file manifest and source comparison | Explicit adjacent source checkout; source commit `3fe84a6dc22d954483e1afce06c3e9b53fc2f5ca`. |
| `validate-slop-pack.mjs` | PASS: 20 website rules checked against 49 registry rules | Pack schema and rule linkage. |
| `drift_check.py --root . --reports-dir ... --as-of 2026-10-29` | PASS: 603 Markdown files | Local cross-file drift validator after increasing its bounded file cap to 650; 16 MiB byte bound is unchanged. |
| Banned phrase test | PASS: 6/6 test cases | Includes expected positive and negative fixture outcomes. |
| A11y service fixture | PASS: five routes, no serious/critical issues | Exact locked browser and axe versions; lab-only. |
| A11y defect fixture | Expected FAIL: one critical and two serious | Intentional negative fixture. |
| SRI unit and service fixture | PASS: ten tests; clean static site passes | External asset parsing, digest length, canonical-origin bypass, protocol-relative URL, and explicit served-origin checks. |
| SRI defect fixture | Expected FAIL: missing/invalid integrity and crossorigin | Intentional negative fixture. |
| Performance gate | FAIL: all five routes exceed LCP budget | 15 local lab runs; thresholds unchanged; field CWV NOT_ASSESSED. |
| Security gate, baseline lock | FAIL: npm audit detects 15 high package records, zero critical | Exact QA dependency tree. |
| Security gate, tested compression override | FAIL: 13 high package records, zero critical; compression finding removed | Disposable consumer lock only; gate not suppressed. |
| Visual QA wrapper | NOT_ASSESSED; exits 4 because task project lacks `tests/visual` | Engine checkout has no executable structure/capture specs. |
| Codex native marketplace | PASS | Isolated network-disabled Podman install/load/details run. |
| Claude native marketplace | PASS | Isolated network-disabled Podman install/load/details run. |
| Deployment and post-deploy smoke | NOT_ASSESSED | No deployment target or authorization was part of the task. |

## Size

Before source edits the checkout count was 837 full entries and 795 package-oriented entries, with zero symlinks. At the implementation checkpoint after the fixes and before the final evidence set, the same counter reported 905 full entries and 803 package-oriented entries. The new executable gate also validates exact registry/plugin/marketplace identity and path parity, rejects escaping/broken symlinks and unreadable walks, and fails if either count exceeds the immutable 5,000 cap. Counts include `.git` only in the full checkout measurement; the package-oriented count prunes `.git`, `.cache`, `.venv`, `venv`, `node_modules`, and `__pycache__`.
