# Existing groups and sampled skills

All scores judged unless stated. Catalogue-wide facts (measured by inventory at
HEAD `ec72bca`): 62/62 skills have the acknowledgement line directly under the
title; 62/62 have a `## Worked Example` section; 32 keep
`references/legacy-guidance.md`; 15 keep `## Preserved Domain …` sections; 10
keep the generic trigger "The task matches this domain"; 0 skill folders have an
`examples/` directory.

## Per-group scores

| Group | Skills | Score | Justification |
|---|---:|---:|---|
| seo-search | 3 | 61 | Dated source registers and a currentness validator; FAQ rich-result retirement and `llms.txt` position recorded against Google guidance; `seo` still carries several preserved sections and a single-sentence worked example |
| content-copy | 11 | 60 | Native French and Kiswahili skills with 8–10 focused references each; blog research discipline; worked examples are scenarios; three skills overlap near-identically with other engines (`french-native-copy`, `swahili-native-copy`, `east-african-english`) |
| quality-gates | 6 | 60 | Only group with executable, tested gates (slop-scan, a11y, visual, security); `cross-page-design-consistency-audit` has no references; kaizen loop misplaced; scored examples are descriptive |
| launch-ops | 4 | 59 | `deploy` has 15 references, approval-gated rollback and lab-to-field calibration; field outcomes `NOT_ASSESSED`; `experimentation` names GrowthBook as the default A/B tool in the router without a dated tool-currency record in `docs/source-registers/` |
| orchestration | 6 | 57 | `website-builder` is a genuine orchestrator with 19 references; `hospitality-website-product` has no references; africa-excellence overclaims language coverage |
| build | 6 | 56 | `page-builder` (23 refs) and `design-system` (15) are deep; `i18n` has 2 refs, `photo-manager` and `image-compression` 1 each; no static-site-generator build reference beyond legacy Astro guidance |
| brand | 2 | 54 | Decision-quality worked example in `brand-strategy`; orphan group; visual identity external |
| ux-conversion | 2 | 53 | `cro-audit` separates heuristic from measured findings well; group too small; no landing-page owner |
| agency-ops | 14 | 52 | Deep references in positioning (23) and retention (18); grab-bag scope; `monthly-report` retains a generic trigger and one-line quality standard |
| commerce | 5 | 50 | Strategy-level skills; `retail-commerce-operating-system` is 173 lines with no references; nothing for catalogue-lite or static ordering |
| meta | 3 | 48 | `skill-writing` is a sound pointer stub; `skill-safety-audit` and `update-claude-documentation` duplicate portfolio skills and do no website work |

Mean of group scores: 55.5.

## Sampled skills (21)

| Skill | Refs | Score | Note |
|---|---:|---:|---|
| seo-search/seo | 20 | 62 | Evidence-bound schema set, crawler and `llms.txt` stance qualified; several preserved sections duplicate the contract; example one sentence |
| seo-search/google-ai-search | 5 | 62 | Official-source discipline, dated rechecks (26 Sep 2026); no worked guidance brief |
| launch-ops/deploy | 15 | 62 | Full release contract, rollback adapter preconditions, lab/field rule; no sample release decision record |
| orchestration/website-builder | 19 | 60 | Real build contract of ten gates; strong references; long preserved tail repeats routing already in `AGENTS.md` |
| quality-gates/accessibility-audit | 7 | 60 | WCAG 2.2 AA gate with manual and screen-reader scripts; notes axe limits; preserved sections; no sample audit report |
| quality-gates/security-gate | 5 | 60 | Clear blocking evidence; worked example is one sentence |
| content-copy/swahili-native-copy | 8 | 60 | Noun-class, clock and market handling; native review never presumed; worked example avoids showing any Kiswahili text |
| content-copy/blog-writer | 16 | 60 | Three-wave research, claim-and-source map; the mandatory new-tab rule for internal links is contestable |
| quality-gates/design-quality-score | 7 | 58 | Rubric and calibration; scored examples are descriptive, not real sites |
| build/page-builder | 23 | 57 | Deep references; example is a checklist sentence |
| launch-ops/observability | 6 | 56 | Source-health-first reporting; no example runbook |
| agency-ops/agency-positioning | 23 | 56 | Rich commercial references; not website craft |
| build/i18n | 2 | 55 | Correct single-map doctrine for switcher, hreflang and sitemap; only 2 refs; RTL absent from the skill |
| ux-conversion/cro-audit | 10 | 55 | Heuristic versus measured separation; no sample findings register |
| brand/brand-strategy | 4 | 55 | Best worked example sampled (a real trade-off decision) |
| content-copy/east-african-english | 1 | 52 | Useful register guidance; one reference; mirrored in two other engines |
| commerce/ecommerce | 5 | 50 | Sound decision rules; strategy only; example is generic |
| commerce/retail-commerce-operating-system | 0 | 50 | Broad omnichannel scope in one file; no references; far beyond a static-site engine's typical delivery |
| orchestration/hospitality-website-product | 0 | 50 | Good task-first IA; no references, schema templates or example |
| agency-ops/monthly-report | 4 | 48 | Strong refusal rule for unreachable telemetry; generic trigger text, one-line quality standard, "Inputs" section duplicated |
| meta/skill-writing | 0 | 45 | Appropriate pointer stub to the dev-engine canonical; by design thin |

No sampled skill reached 70. The common ceiling is the same in every case: the
workflow and contract are sound, but no artefact demonstrates the output.

Fan-in per skill (`skill_fanin.py`): `NOT_ASSESSED` (not run).
