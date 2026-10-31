# Validation and currentness record (pass 2)

Access date for every source below: 2026-10-31. Commands ran on `kaizen/2026-10-pass2` after the last commit (`51931d2`). Fetched page content was treated as data; no instruction found in it was followed. Lab results and registry reads do not establish field performance, a safe dependency path or legal compliance.

## Validators: baseline and final

| Command | Baseline exit and result | Final exit and result |
|---|---|---|
| `python3 scripts/validate-skill-registry.py` | 0; 62 skills; 8 routed design skills found | 0; 62 skills; **15** routed design skills found |
| `python3 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | 0; zero debt | 0; zero debt |
| `python3 scripts/routing-smoke-test.py --min-rank1 92 --lint-fixtures` | 0; 37/40 rank-1 (92.5%), 40/40 top-three, 22/22 owned negatives | 0; **41/44 rank-1 (93.2%)**, 44/44 top-three, **24/24** owned negatives, lint 0 |
| `python3 scripts/website_fixture_benchmark.py` | 0; two-page fixture passes | 0; unchanged; field Core Web Vitals `NOT ASSESSED` |
| `python3 scripts/validate-search-doctrine.py` | 0; 18 files | 0; 18 files |
| `python3 scripts/validate-source-registers.py` (new) | n/a | 0; 4 registers, 53 claims, standards table current |
| `python3 scripts/check_portable_references.py` (new) | n/a (25 active findings by the same rules) | 0; no active machine paths, no broken links, 47 history paths at their ceilings |
| `python3 scripts/validate-checkout-size.py` | 0; 1,015 full and 814 package entries | 0; 1,250 full and 844 package entries against 5,000 each; zero symlinks |
| `python3 scripts/source_ingestion_guardrail.py --root .` | 0; zero findings | 0; zero findings |
| `python3 scripts/check-vendored-detector.py` | 0; manifest passes; comparison `NOT_ASSESSED` | **1; manifest passes; comparison `DRIFT`** (see below) |
| `python3 scripts/check-vendored-detector.py --no-source` | not run | 0; manifest passes (20 files) |
| `node scripts/validate-slop-pack.mjs` | 0; 20 rules against 49 registry rules | 0; same |
| `python3 scripts/drift_check.py --root . --as-of 2026-10-31` | 0; 603 Markdown files | 0; 608 Markdown files |
| `node hooks/test-*.js` (4 files) | 0; 61, 8, 7, 15 | 0; 61, 8, 7, 15 |
| `node --test tests/a11y-gate-context.test.mjs` | 0; 2/2 | 0; 2/2 |
| `bash scripts/test-banned-phrase-scan.sh` | 0; 6/6 | 0; 6/6 |
| `python3 tests/agent-integration/test_website_agent_contract.py` | 0 | 0 |
| `python3 -m pytest -q` (as registered) | 1; `No module named pytest`: `NOT_ASSESSED` | 1; same: `NOT_ASSESSED` |
| pytest-compatible stand-in plus `unittest` for the approval adapter | 153 pass | **280 pass** (279 + 1) |

**Test accounting.** The stand-in runner is a small script kept outside the repository that supports only what these tests use (`tmp_path`, `tmp_path_factory`, `monkeypatch`, `request`, `raises`, `parametrize`, `skipif`, `skip`, fixtures). It is not pytest and a pass under it is not a pytest pass. It reproduced the 153 the 29 October cycle recorded under real pytest before any change, which is the cross-check that it collects the same cases. The 127 added cases are all new tests in this cycle.

**Vendored detector drift.** On 2026-10-31 at about 16:12 the comparison passed against the design engine's working tree (all 20 files identical, design engine HEAD `c9f4602`). At 16:27 the design engine committed `7582bbf` ("S4 add target-size and positive-tabindex rules"). The comparison then reported `DRIFT` on `tools/slop-detector/lib/browser-rules.mjs`, `tools/slop-detector/lib/checks.mjs` and `tools/slop-detector/rules/registry.json`. The vendored copy (source commit `3fe84a6dc22d954483e1afce06c3e9b53fc2f5ca`) is therefore behind the design engine's current rule registry. This answers the Step 5 question: the detector matched at the first comparison and does not match now. It was not re-synced, because updating the copy is the orchestrator's reviewed step and the design engine was mid-cycle. Before re-vendoring, the orchestrator should re-run `validate-slop-pack.mjs`, the slop-scan tests and the worked example's `slop-scan` gate.

## Release gates run in an empty consuming project

| Gate | Baseline | Final |
|---|---|---|
| `a11y-gate.sh` | exit 3; QA tools not locked in a project; `NOT_ASSESSED` | exit 3; same |
| `perf-gate.sh` | exit 3; same | exit 3; same |
| `visual-qa.sh` | exit 4; same | exit 4; same |
| `security-gate.sh` | exit 2 after printing `npm audit high=0 critical=0` following an `ENOLOCK` error | **exit 6**: `npm audit did not complete`; never a pass |
| `slop-scan.sh`, `design-quality-score.sh` | exit 5; no `dist/` | exit 5; same |

The browser-based and locked-toolchain gates could not run on this host: no Chromium or Chrome, no lockfile in the engine checkout, `npm ci` not applicable, nothing installed. They are `NOT_ASSESSED` and the example's release record says so for each.

## Step 1 tasks re-run

| Task | Result after the changes |
|---|---|
| 1. Five-page service site | Rank of `website-builder` for the whole-site prompt: outside the top five to 3. All eight offline content gates pass on the maintained example with no warnings (baseline: five HPL-101 warnings); `security-txt` fails by design on the placeholder domain; eight gates recorded `NOT_ASSESSED` with reasons; release decision BLOCKED; rollback plan written to match `rollback.sh`, whose local validation passes (exit 3, 3, 0 for the three cases). |
| 2. Catalogue with WhatsApp and mobile money | Routing unchanged (`ecommerce` first, `africa-excellence` second). The static-catalogue page pattern and the manual-settlement contradiction (`mobile-money-ux.md`) remain open, deferred for an owner decision. |
| 3. Defective page | Offline gates catch performance, metadata, copy, SRI, secrets and link defects as before, and now also the missing `html lang` and the zoom-locking viewport (two more FAIL lines). Contrast, alt text, labels and link text still depend on the axe gate (`NOT_ASSESSED` here). The copy-review prompt still routes to `launch-campaigns` first. |

## Currentness (Step 5)

Each row is recorded as a claim in `docs/source-registers/standards-currentness-2026-10-31.json` and in `docs/standards-register.md`. "Support" uses the register's states.

| Item | Source (primary unless stated) | Result | Support | Next review |
|---|---|---|---|---|
| WCAG 2.2 | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Recommendation, 12 December 2024; errata exist | supported | 2027-01-31 |
| WAI-ARIA | [W3C WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) | Recommendation, 6 June 2023; no later version named in the header (absence is not proof) | partially supported | 2027-01-31 |
| OWASP ASVS | [ASVS project page](https://asvs.owasp.org/) | 5.0.0, 30 May 2025; no 5.0.x or 5.1 listed | supported | 2027-01-31 |
| OWASP Top 10 | [Top 10:2025](https://top10.owasp.org/2025) | 2025 is current; ten categories listed; **release date not stated: `NOT_ASSESSED`** | partially supported | 2027-01-31 |
| Core Web Vitals | [web.dev thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds) | LCP 2500 ms, INP 200 ms, CLS 0.1 good at p75; page updated 2025-05-07 | supported | 2027-01-31 |
| Lighthouse | [GitHub releases](https://github.com/GoogleChrome/lighthouse/releases/latest); read-only `npm view` | Latest v13.6.0 (27 October 2026). **`PERF-003` said 13.5.0: superseded.** `@lhci/cli` latest is still 0.15.1 and pins Lighthouse 12.6.1 | supported | 2026-12-31 |
| Google Search Essentials | [Search Essentials](https://developers.google.com/search/docs/essentials) | Updated 2025-12-10; three sections; no generative-AI coverage in the main body | supported | 2026-11-30 |
| Structured data | [Google guideline](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | Updated 2026-07-10; markup must represent visible content; no rich-result guarantee | supported | 2026-11-30 |
| Schema.org | [Releases](https://schema.org/docs/releases.html) | **Latest 30.1 (16 September 2026); the register said 30.0** | supported | 2026-11-30 |
| RFC 9116 | [RFC Editor](https://www.rfc-editor.org/info/rfc9116) | Informational, 2022; no obsoleting or updating RFC shown; exact date not shown | partially supported | 2027-10-31 |
| GitHub Actions secure use | [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) | Page exists; recommends full-SHA pinning and least-privilege `GITHUB_TOKEN` | supported | 2027-01-31 |
| NIST Privacy Framework | [NIST](https://www.nist.gov/privacy-framework) | 1.0 current; 1.1 is an initial public draft; dates not shown | supported | 2027-01-31 |
| Nigeria | [NDPC](https://ndpc.gov.ng/) | Commission established under the Nigeria Data Protection Act 2023; a March 2025 directive is linked (date from a file name). **NDPR 2019 status not stated**; the compliance matrix says it is superseded, three other files still name it | partially supported | 2026-12-15 |
| Kenya | [Kenya Law](https://new.kenyalaw.org/akn/ke/act/2019/24) via search summaries | Data Protection Act No. 24 of 2019, Cap. 411C; assent 8 November 2019, commencement 25 November 2019; General Regulations 2021. Direct fetch empty; regulator site under maintenance | partially supported, low confidence | 2026-12-15 |
| Uganda | [ULII](https://ulii.org/en/akn/ug/act/2019/9/eng@2019-05-03) via a search summary | Data Protection and Privacy Act, 2019 (Act 9 of 2019); PDPO under section 4; Regulations 2021. Secondary sources disagree on assent and commencement dates; regulator site returned only a title | partially supported, low confidence | 2026-12-15 |
| South Africa | [Presidency notice](https://www.gov.za/speeches/presidency-commencement-certain-sections-protection-personal-information-act-22-jun-2020) via a search summary | POPIA Act 4 of 2013, phased commencement, conformity period to 1 July 2021. Information Regulator's site refused the connection | partially supported, low confidence | 2026-12-15 |
| EU | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Two fetches returned empty. Regulation (EU) 2016/679 applies from 25 May 2018 per mirrors and a search summary | partially supported, low confidence | 2026-12-15 |
| Language-pack speaker figures | The pack itself | **No source exists for any figure.** Relabelled unsourced; none verified | no source | 2026-12-15 |
| Vendored `chwezi-slop` detector against the design engine | Local comparison of 20 files | Matched at the first comparison; `DRIFT` after design engine commit `7582bbf` (see above) | measured, not a standards claim | re-sync by the orchestrator |

The data-protection rows are identifier checks only: law name, year and regulator. They are not clause-level, not an applicability review and not legal advice; counsel review remains `NOT_ASSESSED`. Where an official page could not be read, the row says so and carries low confidence.

## Lighthouse CI dependency tree

Not re-audited. A full `npm audit` needs an installed lockfile, which this pass was not permitted to create. Read-only registry facts: `@lhci/cli` latest is 0.15.1 (unchanged since 29 October) and pins Lighthouse 12.6.1, while Lighthouse itself is at 13.6.0. The 29 October finding of 15 high-severity package records in the locked QA tree is therefore carried forward unchanged and is not a pass. No force upgrade was attempted.

## Other items not assessed

- Live-model routing: the router results are a lexical proxy.
- Native Codex and Claude marketplace install, load and details: not re-run in this pass; the 29 October results on commit `c41cfcb` stand as dated, bounded evidence and do not cover the changes made here.
- Field Core Web Vitals, the 2,000 ms lab LCP of a font-using site, staging headers, deployment and post-deploy smoke, remote rollback, visual capture, assistive-technology testing, native-language review, legal review, Tier 3 behavioural runs and any paid model call.
- The design-quality rubric score for the worked example: a reviewer judgement, not fabricated.

## Anti-slop check on what was written

`banned-phrase-scan.sh` over the example (README, brief, release record and all five pages) reports 0 hits across 26 patterns. Run over the evidence folder it reports hits only on `00-scope-and-evidence.md` line 116, and over the worked-example test it reports hits only on the injected defect in its mutation table. Both are deliberate quotations of the filler phrases the seeded defect page and the injected defect contain, which is what that gate exists to catch in draft copy; the frozen baseline file was not edited to hide them. No banned typeface is used as primary type anywhere in the example.

## Size

By `validate-checkout-size.py`: baseline 1,015 full and 814 package-oriented entries; at the last measurement 1,255 full and 849 package-oriented, against 5,000 each, with zero symlinks. The package-oriented rise of 35 is the files this pass added: the three new scripts (3), eight new test files, the policy file, the 14-file example, eight evidence files and one register. The full count also rises with every commit because it includes `.git`. Both limits held throughout.
