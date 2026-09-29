# Methodology and rubric

## Method

The audit followed `chwezi-dev-engine/skills/sdlc-meta/skill-engine-audit/SKILL.md`
with its references `scoring-rubric.md` (including "Engine Eval Readiness
(measured)"), `eval-readiness-worked-example.md`, `audit-dimensions.md` and
`report-structure.md`.

1. **Harness first.** The engine's validators and the CI-declared gates were run
   from the engine root with `PYTHONDONTWRITEBYTECODE=1` before any dimension was
   scored (commands and exit codes in `11-measured-evidence.md`).
2. **Scope.** Read `CLAUDE.md` (a bridge that imports `AGENTS.md`), `AGENTS.md`
   in full, `README.md`, `docs/skill-authoring-standard.md`,
   `templates/skill/SKILL.md`, the two 6 September audit files and the M10-14
   portfolio evidence (`eval-readiness.json`, `readiness/coverage.json`,
   `readiness/collision-scan.json`, `readiness/website-smoke.txt`).
3. **Inventory.** Globbed all 62 `skills/<category>/<skill>/SKILL.md` files and
   recorded line counts, reference counts, acknowledgement-line presence, legacy
   sections and generic triggers for every skill.
4. **Sample reading.** Read in full or in substantial part 13 `SKILL.md` files
   across 9 groups (website-builder, i18n, ecommerce, seo, accessibility-audit,
   deploy, swahili-native-copy, blog-writer, design-quality-score, skill-writing,
   hospitality-website-product, monthly-report, google-ai-search) and the
   description plus worked example of 8 more (page-builder,
   retail-commerce-operating-system, cro-audit, brand-strategy, observability,
   security-gate, east-african-english, agency-positioning): 21 skills, all 11
   groups. Supporting references read: `wcag-baseline.md`,
   `african-language-pack.md`, `scored-examples.md`,
   `ai-search-response-mode-planning.md`, `google-generative-ai-search-playbook.md`.
5. **Scoring** against the fixed rubric, then synthesis.

**Documented limitation: no parallel fleet.** The skill prescribes independent
parallel agents per concern. In this re-audit a single auditor worked through
each concern in turn (standards, existing skills, taxonomy, output types,
hardening, sources). Scores are therefore less independent than a fleet would
produce; the concerns were written up separately to limit cross-contamination.

## Rubric

Bands from `scoring-rubric.md`: 90–100 rivals the field's best; 75–89 excellent;
60–74 solid but visibly short; 40–59 competent with major gaps; below 40
skeletal. The bar is the top 0.1 % of premium website agencies and static-site
engineering practice. Strictness directive applied: default 45–65; any 70+
requires an "Extraordinary justification" paragraph. None was awarded.

Labels: **measured** (from a command result cited here), **judged** (auditor
reading, with named deficiencies) or **NOT_ASSESSED** (scores 0 where it feeds a
formula).

## Weighting

| Bucket | Weight | Inputs |
|---|---:|---|
| Output-type readiness & coverage | 30 % | Mean of output coverage (dim 6), accessibility (dim 7) and production/hand-off (dim 8) |
| Skill depth & worked examples | 25 % | Mean of skill depth (dim 3) and worked examples (dim 4) |
| Standards currency | 15 % | Dim 5 |
| Taxonomy & structure | 10 % | Dim 2 |
| Doctrine & philosophy | 10 % | Dim 1 |
| Hygiene | 10 % | Mean of redundancy (dim 9), discovery/routing (dim 10) and safety (dim 11) |

Folding accessibility and production into the output bucket is this audit's
stated choice; the rubric's suggested weighting names only the six buckets.

## Three published numbers

- **Raw**: routing judged at 62.
- **Measured-constrained**: routing replaced by Readiness 59.6 (AO-14 rule 3).
- **Published**: `min(measured-constrained, 65)`, because the portfolio craft
  standard's acceptance evidence does not exist for this engine.

## Standards currency basis

Standards currency is **judged from the engine's own currentness records (no
fresh external research)**. No web research was performed; no external fact in
this report is newly asserted.

## Other limitations

- Tier 3 behavioural runs: `NOT_ASSESSED` (zero-spend rule; 0 `grading.json`).
- Rendered, browser, assistive-technology and field Core Web Vitals outcomes:
  `NOT_ASSESSED` (the fixture benchmark itself reports
  `"field_core_web_vitals": "NOT ASSESSED"`).
- Skill fan-in (`skill_fanin.py`) was not run: `NOT_ASSESSED`.
- Lexical routing figures are a drift guard, not proof of live routing.
- Remote CI status was not re-queried; the M10-14 executor recorded the website
  workflow as success at HEAD.

## Auditor independence

The auditor did not execute any my-10-kaizen phase and made no change to the
engine other than writing this folder. No git state was changed (no commit,
checkout, stash or reset). No paid API or model-executed evaluation was used.
Prior scores were read for comparison only and not copied.
