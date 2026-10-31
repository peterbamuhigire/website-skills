# Baseline scorecard (frozen)

Measured 2026-10-31 on `kaizen/2026-10-pass2` at commit `c41cfcb`, before any change in this cycle. Scores are an independent judgement from inspected files and fresh runs **(synthesis)**; they are not a carry-forward of the 29 October final. This file is not edited after its commit.

| Dimension | Baseline /100 | 29 Oct final | Named evidence and one-line deficiency |
|---|---:|---:|---|
| Doctrine | 70 | 70 | Router, contracts, release and hand-off rules exist and the validators pass. Deficiency: the router itself carries four machine-specific paths (`AGENTS.md` lines 61, 74, 371, 561). |
| Taxonomy and routing | 48 | 50 | Lexical smoke 37/40 rank-1 (92.5%), 40/40 top-three, 22/22 owned negatives. Deficiency: a plain "build a five-page site through release" prompt ranks `deploy` first and `website-builder` outside the top five; a copy-review prompt ranks `launch-campaigns` first; 30 of 62 skills have no positive fixture. |
| Skill depth | 62 | 65 | Orchestration, release and rollback workflows have inputs, stop conditions and recovery. Deficiency: the static-catalogue route has no page pattern, and the only manual mobile-money pattern assumes a backend (`mobile-money-ux.md` lines 64 to 79). |
| Applied proof | 25 | 25 | One single-page prototype under `examples/`; eight small fixture folders; no maintained multi-page deliverable with a gate record and release decision. Deficiency: every complete site produced so far lives outside the repository and is discarded. |
| Standards currency | 52 | 60 | JSON registers: 35 claims, none past review (earliest 2026-12-12). Deficiency: `docs/standards-register.md` has six rows past their `Next review` date and no validator reads that table; the vendored-detector source comparison is `NOT_ASSESSED` by default. |
| Output readiness | 58 | 65 | Task 1: eight offline gates pass on the finished site; four browser or tool gates `NOT_ASSESSED`; security.txt gate fails correctly on the placeholder domain. Deficiency: the security gate's audit step fails open (WSK2-D1) so a release verdict from it cannot yet be trusted when the audit does not run. |
| Accessibility and inclusion | 50 | 55 | Axe gate works when a browser and locked tools exist (29 October). Deficiency: `lang` and zoom-blocking viewport are caught only by that browser gate; the language pack claims ten first-class languages with two native-copy skills. Assistive-technology and native-language review remain `NOT_ASSESSED`. |
| Production and handoff | 65 | 65 | `rollback.sh` local validation runs: missing authority exits 3, mismatched target exits 3, authorised validation exits 0. Deficiency: no rollback rehearsal, staging, post-deploy smoke or hand-over pack. |
| Hygiene | 72 | 80 | Registry, contracts, size, drift, ingestion and slop-pack validators pass; 619 relative Markdown links, none broken. Deficiency: 26 machine-specific paths in active content (one dangling), 41 in history documents and client prompts; no validator for either. |
| Safety and integrity | 55 | 65 | Secrets scan, SRI and slop scan catch seeded defects; examples keep payment and contact disabled. Deficiency: the critical fail-open in `security-gate.sh` (lines 40 to 43); the Lighthouse CI dependency tree still reports high-severity records; legal review of privacy wording is `NOT_ASSESSED`. |

Raw baseline = **55.7/100** (sum 557 across ten dimensions). Portfolio Standard score = `min(raw, 65)` = **55.7/100**. The cap does not bind. The 29 October final was 60.0; the lower figure here is not a regression. It comes from a fresh observation that found a critical gate defect, routing misses, path hygiene and expired review rows that the previous pass did not measure. The improvement plan still targets 95.

**Blockers regardless of score:** the security gate fail-open (WSK2-D1) is a release-integrity failure. Dependency-audit, legal-review, staging-header and deployment evidence remain open from 29 October.

## Measured inputs

| Measure | Baseline | Method and limit |
|---|---|---|
| Validators | All registered validators pass or are `NOT_ASSESSED`; table in `00-scope-and-evidence.md` | Exact commands and exit codes recorded there |
| Routing precision@1 | 37/40 = 92.5% (floor 92%) | Lexical proxy, not live routing |
| Routing precision@3 | 40/40 = 100% | Same |
| Owned negatives | 22 pass, 0 fail, 0 not assessed | Same |
| Fixture coverage | 32 of 62 skills with any positive; **2 of 62** with three positives and two owned negatives (`deploy`, `ecommerce`); 14 skills with any negative; 30 with no positive | Counted from `tests/routing/fixtures.json` |
| Worked-example depth | 1 example directory (single page, synthetic prototype); 0 multi-page maintained deliverables; 0 release records with a gate table | `find examples fixtures` |
| Test suite | 153 cases pass under a pytest stand-in plus `unittest`; real pytest `NOT_ASSESSED` | pytest not installed |
| Broken relative Markdown links | 0 of 619 across 604 tracked Markdown files; 0 escape the checkout | Fenced code skipped; scratch script |
| Machine-specific absolute paths | 67 hits: 26 in active content (18 in skill files), 41 in history documents and client prompts (`prompts/` 28, `docs/` history 12, one session report) | `git grep` for `wamp64`, `/home/<user>/`, `/Users/<name>/` |
| Dangling cross-engine references | 0 dangling skill names among 12 distinct `chwezi-design-engine:<name>` forms (four non-skill tokens are prose or deliberate negatives in `tests/test_design_routes.py`); 1 dangling design-engine file path | Compared with the sibling's 103 `SKILL.md` names and tree |
| Expired source records | 0 overdue claims in the three JSON registers; 6 overdue rows in `docs/standards-register.md` | Claim-level `review_date` against 2026-10-31 |
| Vendored detector | Manifest passes (20 files, source commit `3fe84a6dc22d954483e1afce06c3e9b53fc2f5ca`); source comparison `NOT_ASSESSED` | Sibling name mismatch |
| Package size | 1,015 full and 814 package-oriented entries; limit 5,000 each; zero symlinks | `validate-checkout-size.py` |

Active-content path hits (file:line), for the record: `AGENTS.md`:61, 74, 371, 561; `rules/common/core.md`:10; `MEMORY.md`:8; `docs/standards-register.md`:4; `docs/source-registers/search-ai-currentness-2026-09-05.json`:205; and in skills `build/design-system/references/` (behaviour-and-visual-pattern-rules 180, data-tables-charts-and-svg-rules 5, design-system-governance-and-designops 5, grid-colour-gradient-and-surface-craft-rules 5, ui-composition-colour-and-icon-rules 5), `build/page-builder/references/` (form-layout-flow-and-validation-rules 7, navigation-mobile-and-form-pattern-rules 186), `content-copy/french-native-copy/references/meaning-first-institutional-copy.md`:88, `content-copy/language-standards/references/english-collocations-and-lexical-precision-2026-09-02.md`:3, `meta/skill-writing/SKILL.md`:13, `orchestration/hospitality-website-product/SKILL.md`:162, `orchestration/premium-ui-ux-design/references/` (ai-feature-discovery-and-risk-framing 5, ai-interface-trust-and-control-spec 5), `orchestration/website-experience-mapping/references/innovation-sprint-dvfs-reframe-and-assumption-testing.md`:5, `quality-gates/accessibility-audit/references/` (cognitive-affordance-and-memory-review 190, question-mark-and-scan-audit 80), `quality-gates/cross-page-design-consistency-audit/SKILL.md`:202, `quality-gates/kaizen-engine-and-product-improvement/SKILL.md`:110.

## Limits of this baseline

Live-model routing, field Core Web Vitals, assistive-technology testing, native-language review, legal review, staging headers and deployment are `NOT_ASSESSED`. Browser-based gates could not run on this host (no browser, no locked QA tools in the checkout).
