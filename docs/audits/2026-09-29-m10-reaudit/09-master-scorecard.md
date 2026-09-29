# Master scorecard

## Dimensions (the 11 in `audit-dimensions.md`)

| # | Dimension | Label | Score | Evidence |
|---:|---|---|---:|---|
| 1 | Doctrine & philosophy | judged | 62 | Premium-by-default, evidence-or-`NOT_ASSESSED`, currentness gate and book-source rule are clear and inherited by every sampled skill. Deducted: 559-line `AGENTS.md` mixing routing with phase history; contestable new-tab internal-link rule in `blog-writer`; router lists design-engine skills as local; proposal-skills embedding contradicts the portfolio routing table |
| 2 | Taxonomy & structure | judged | 55 | 11 groups; agency-ops grab-bag (14); two 2-skill groups; no intake, landing-page or catalogue-lite owner (see 02) |
| 3 | Skill depth & rigour | judged | 57 | Zero contract debt (measured, `validate-skill-contracts.py`); deep references in core skills; 15 skills with preserved sections, 10 generic triggers, 4 with no references |
| 4 | Worked examples & applied proof | judged | 40 | 62/62 worked-example sections but all scenarios of 1–3 sentences; `examples/` holds one prototype; scored examples are descriptive; Tier 3 `NOT_ASSESSED` adds nothing |
| 5 | Standards currency | judged (engine's own currentness records; no fresh external research) | 58 | Dated search and performance registers; FAQ rich-result retirement; INP from field only; WCAG 2.2 AA baseline. Deducted: no currentness register for accessibility or tooling; unsourced language-pack figures; Uganda/Tanzania/Rwanda network data partly `NOT_ASSESSED` by the engine itself |
| 6 | Coverage / output-type readiness | judged | 55 | Mean of eight output types, 54.75 (see 05) |
| 7 | Accessibility / inclusivity | judged | 56 | WCAG 2.2 AA gate with manual keyboard and screen-reader scripts; axe limits stated. Deducted: no rendered a11y evidence; RTL shallow; ten-language claim without copy routes; new-tab rule |
| 8 | Production / hand-off / render fidelity | judged | 58 | 15-step CI, approval-gated rollback, fixture benchmark PASS (measured), locked QA tooling. Deducted: lab fixture only; field CWV `NOT_ASSESSED`; no hand-over pack template |
| 9 | Redundancy & hygiene | judged | 50 | 32 legacy-guidance files; 15 preserved-section skills; root clutter (`SESSION_2026-02-17_SUMMARY.md`, `SESSION_2026-05-05_REPORT.md`, `ENGINE-AUDIT-JULY-2026-MASTER.md`, `static-website-starter.zip`, `MEMORY.md`); cross-engine near-duplicates (below 0.75, undeclared) such as `blog-writer` 0.72 with business-plan, `french-native-copy` 0.70 and `swahili-native-copy` 0.67 with social-media, `update-claude-documentation` 0.68 with proposal |
| 10 | Discovery & routing | **measured** | **59.6** | Engine Eval Readiness (see 11). Judged value for the raw number: 62 |
| 11 | Safety & integrity | judged | 64 | Capability and authority contracts in every sampled skill; 4 hook self-tests pass; source-ingestion guardrail 0 findings; vendored detector hash check PASS; locked QA tooling. Deducted: local safety-audit skill duplicates the dev gate; no per-skill safety verdict register sampled |

## Groups

seo-search 61 · content-copy 60 · quality-gates 60 · launch-ops 59 ·
orchestration 57 · build 56 · brand 54 · ux-conversion 53 · agency-ops 52 ·
commerce 50 · meta 48 (mean 55.5; detail in 03).

## Output types

Marketing/company website 60 · Blog 58 · Client intake brief 57 ·
Deployment/hand-over pack 56 · Landing page 55 · Performance and SEO audit
reports 55 · Multilingual/African-language 52 · E-commerce-lite/catalogue 45
(mean 54.75; detail in 05).

## Bucket arithmetic

| Bucket | Weight | Inputs | Bucket score |
|---|---:|---|---:|
| Output readiness | 0.30 | mean(55, 56, 58) | 56.333 |
| Depth & worked examples | 0.25 | mean(57, 40) | 48.500 |
| Standards currency | 0.15 | 58 | 58.000 |
| Taxonomy | 0.10 | 55 | 55.000 |
| Doctrine | 0.10 | 62 | 62.000 |
| Hygiene (raw) | 0.10 | mean(50, 62, 64) | 58.667 |
| Hygiene (measured) | 0.10 | mean(50, 59.6, 64) | 57.867 |

## The three overall numbers

- **Raw** = 0.30 × 56.333 + 0.25 × 48.5 + 0.15 × 58 + 0.10 × 55 + 0.10 × 62 + 0.10 × 58.667
  = 16.900 + 12.125 + 8.700 + 5.500 + 6.200 + 5.867 = **55.29 → 55.3**
- **Measured-constrained** = 16.900 + 12.125 + 8.700 + 5.500 + 6.200 + 5.787 = **55.21 → 55.2**
- **Published** = `min(55.2, 65)` = **55.2** (craft-standard acceptance evidence absent; cap not binding)

**Engine Eval Readiness: 59.6** (reported beside the overall, not folded away).

No score of 70 or above was awarded, so no extraordinary-justification paragraph
is required.

## Comparison with the prior audit

| Item | 6 Sep 2026 | 29 Sep 2026 |
|---|---|---|
| Overall | `NOT ASSESSED` (cap 65) | 55.2 published |
| Active skills / contracts | 60 | 62, zero debt |
| Routing fixtures | 31 | 37 positives + 21 owned negatives, p@1 94.6 % |
| Tests | 38 passed | 131 passed |
| Slop gate | not present | slop-scan over vendored detector, tested |
