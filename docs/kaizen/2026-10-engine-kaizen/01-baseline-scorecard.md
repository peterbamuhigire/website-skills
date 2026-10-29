# Baseline scorecard

Assessment date: 2026-10-29. This is an independent pre-change score from inspected files and fresh baseline runs. It is **(synthesis)**, not a carry-forward of the September audit's published rating.

| Dimension | Baseline /100 | Evidence and observed gap |
|---|---:|---|
| Doctrine | 70 | Router, contracts, safety, release and handoff instructions exist. Relevant currentness records include an overdue search claim and an overdue model review. Generic privacy reference content was not legally validated. |
| Taxonomy and routing | 45 | Lexical smoke: 35/37 rank-1, 37/37 top-three, 21/21 owned negatives. Static catalogue enquiry/manual settlement has no clearly scoped route in the existing ecommerce skills. Live-model routing is NOT_ASSESSED. |
| Skill depth | 60 | Website-builder provides an end-to-end route, sequence and stop conditions. Catalogue inquiry, seller-owned contact and manual payment boundaries are underspecified. |
| Applied proof | 25 | Built-in benchmark covers two pages and local structural checks. September re-audit reported no full worked deliverable type and only short examples. This cycle's complete sites are temporary fixtures, not maintained examples. |
| Standards currency | 55 | Search currentness validation fails on overdue SAI-018. The model-currentness record is overdue. Privacy legal text and jurisdictional applicability are NOT_ASSESSED. |
| Output readiness | 55 | Five-page synthetic site and release list exist outside the repository. The configured accessibility runner fails before scanning; lab LCP exceeds its configured budget; npm audit blocks security; visual capture cannot run without missing specs. |
| Accessibility and inclusion | 45 | Temporary patched runner scans the five-page site, but the repository runner fails on context creation. Assistive technology and native-language quality are NOT_ASSESSED. |
| Production and handoff | 65 | Gates, release state and rollback guidance exist. No staging host, deployed headers, deployment, rollback rehearsal or post-deploy proof were available. |
| Hygiene | 70 | Registry and contract validators pass. Search-currentness validator fails. Baseline checkout count is 837 full / 795 package-oriented, zero symlinks; both below the 5,000 hard limit. |
| Safety and integrity | 65 | Disposable data is synthetic and payment/contact actions are disabled. Dependency audit finds 15 high-severity vulnerability records and zero critical; legal review, edge headers and production controls remain open. |

Raw baseline = **55.5/100** (sum 555 across ten dimensions). Portfolio Standard score = **min(raw, 65) = 55.5/100**. The owner-specific initial cap is reported separately: **min(raw, 45) = 45/100**. The 65 cap does not bind. These caps do not convert release blockers into passes.

## Measured inputs and limitations

| Measure | Baseline observation | Evidence and limitation |
|---|---|---|
| Registry and contracts | 62 active skills, one template, zero contract debt | `validate-skill-registry.py`; `validate-skill-contracts.py --baseline quality/skill-contract-baseline.json`. Design route was initially reported unavailable by default; explicit comparison with the actual adjacent `design-system-skills` checkout later passed. |
| Built-in fixture | PASS; two-page benchmark, 2,026 raw fixture bytes against a 350 KB configured ceiling | `website_fixture_benchmark.py`; lab-only; field CWV NOT_ASSESSED. |
| Routing | 35/37 rank-1 (94.6%), 37/37 top-three, 21/21 owned negatives | `routing-smoke-test.py --min-rank1 92 --lint-fixtures`; lexical proxy, not live model. |
| Fixture depth | September audit records 30/62 skills with any positive and 1/62 with at least three positive plus two owned negative fixtures | `docs/audits/2026-09-29-m10-reaudit/00-executive-summary.md`; not a fresh model-routing result. |
| Full test suite | 130 passed, 1 failed | Temporary Python venv; sole failure is overdue SAI-018 currentness check. |
| Source currentness | `validate-search-doctrine.py` fails on SAI-018, review date 2026-10-03. Model record MODEL-001 review date 2026-10-15 is overdue. | Source registers `search-ai-currentness-2026-09-05.json` and `performance-currentness-2026-09-25.json`; official sources were rechecked for this cycle. |
| Accessibility | Exact configured gate fails on all five service pages with `Please use browser.newContext()`; a disposable runner using explicit context scans all five | Reproduced with locked axe 4.10.2. Clean pages had zero serious/critical findings in patched temporary runner. Defect page was not yet assessed by repository runner. |
| Performance | 15 Lighthouse runs fail the configured maximum LCP 2,000 ms; observed route range about 2,404–2,416 ms | Synthetic local mobile lab profile, not field CWV. FCP also exceeds 1,500 ms. |
| Security | `npm audit` reports 15 high package-vulnerability records and zero critical; gate exits before other subchecks. Preview header check fails eight configured edge headers. | Disposable lockfile/project; staging/edge behavior NOT_ASSESSED. Advisories are linked in `04-validation-record.md`; record count is not a count of unique advisories. |
| SRI and visual | SRI gate falsely treats absolute canonical URLs as external assets. Visual QA wrapper cannot find required capture/structure specs. | Clean fixture, exact disposable gate. Visual capture remains NOT_ASSESSED. |
| Defect fixture | Slop scan blocks three findings; HTML perf catches missing image dimensions and `document.write`; metadata check catches short description and missing canonical/social fields | Deliberately bad synthetic page. These are fixture findings, not real-site findings. Axe was blocked by runner failure. |
| Source comparison | Vendored manifest passes; explicit design source comparison passes against adjacent `design-system-skills` checkout | `check-vendored-detector.py --source ../design-system-skills`; source commit recorded in experiment log. Default sibling-name mismatch remains a portability gap. |
| Native marketplaces | Codex and Claude marketplace install/load/details commands pass offline in disposable Podman containers | No network, no model call, read-only engine mount, host config unchanged. This establishes local native install/load only. |
| Link/path scan | Portfolio-wide broken or machine-specific link audit NOT_ASSESSED | No complete baseline link scanner was run before edits. |

## Practitioner tasks

The five-page service website, small product catalogue, and deliberate defect page were created in disposable fixture directories. Fictional business facts are marked synthetic, while owner contact, payment provider, seller destination, and operational facts remain absent. No outbound enquiry, payment, deployment, or public submission occurred. The existing ecommerce route lacks explicit steps for a static catalogue with seller-mediated enquiry and manual settlement **(inference)** from the route text and prep-task trace.
