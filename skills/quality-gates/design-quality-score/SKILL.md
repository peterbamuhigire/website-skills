---
name: design-quality-score
description: Use when scoring a rendered website against the engine's seven-category design-quality and anti-slop rubric; use visual-qa for screenshot regression and cross-page-design-consistency-audit for system drift.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Design Quality Score
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Assign a reproducible read-only design score and release advice without confusing absent visual evidence with quality.

<!-- dual-compat-start -->
## Use When

- A rendered site needs the canonical design score
- a PR or main release needs slop-scan evidence
- improvement priorities need category scores.

## Do Not Use When

- Use `visual-qa` for baseline diffs or the cross-page audit to diagnose two competing design systems.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Rendered route sample, scoring rubric, brand and design decisions, viewport matrix, and content states | Build and approved project artefacts | yes | Score against intended and canonical quality | Stop if representative renders or the rubric are unavailable |

## Workflow

1. Confirm read-only scope, build, sample, and rubric
2. Score each category with cited visual evidence and run the slop scan
3. Reconcile category totals and stop a blocking main release below the documented threshold
4. After authorised remediation, rerender and rescore the affected categories.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Design quality scorecard | Designers, developers, and release owner | Category evidence sums to the reported score and release advice follows the documented threshold |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Annotated renders, slop-scan output, category calculations, and unassessed list | Release owner | Another reviewer can reproduce every awarded or deducted point |

<!-- dual-compat-end -->
## Capability Contract

Read, search, rendering, and visual inspection are required. Default to read-only. Code, token, baseline, production, or publication changes require separate authority.

## Degraded Mode

Without representative renders, fonts, or rubric evidence, return the narrowest qualified partial score, mark affected categories `not assessed`, and do not certify the total.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Category evidence is unavailable | Leave it unassessed rather than awarding points | Inflated score |
| Main-branch score is below the blocking threshold | Block release and prioritise corrections | Shipping visible quality debt |

## Quality Standards

- Every point needs evidence; score route families and states, preserve authored exceptions, and apply the rubric arithmetic exactly.

## Anti-Patterns

- Scoring from source code alone. Fix: inspect rendered output.
- Awarding points for an unavailable route. Fix: mark that category unassessed.
- Letting one polished homepage represent the site. Fix: sample every template family.
- Changing the rubric mid-review. Fix: record any threshold change as a decision first.
- Replacing unusual authored choices with defaults. Fix: distinguish intentional design from defects.

## Worked Example

If the homepage is distinctive but three interior templates use generic utilities, score the sampled evidence rather than averaging from the homepage and route the cause to cross-page consistency.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- Before any site launches — each primary template is scored.
- Before promoting a visual baseline change to main.
- During visual QA when the operator suspects the output is drifting
  toward generic AI aesthetic.
- During certification practical exams — the score is part of the
  evidence.

## Preserved Domain Exclusions
- Scoring copy-only or data-only changes. The rubric measures rendered
  design, not isolated content.
- Scoring early design mocks before they become shipped templates; use
  `design-reference` and `design-system` at mock stage.

## Core contract

Every primary template is scored against the 7-category rubric before
launch. The minimum score to ship is **8/10 per category and 8/10
overall**. A category below 8 blocks deploy.

The scoring is:
1. **Defensible against the rubric**, not against taste. Every score
   cites the rubric clause that justifies it.
2. **Evidenced**. The operator files a per-template report with the
   score, the evidence (screenshots, specific class names, specific
   copy), and the rationale.
3. **Repeatable**. A second operator scoring the same template arrives
   within one point per category.

## Preserved Domain Workflow
1. Build the site and confirm Phase 10 gates (perf, a11y, visual-qa,
   security) have passed on the CI or locally.
2. For each primary template (home, services, service-detail, contact,
   blog-index, blog-post, and any client-specific templates), open the
   template on a desktop and on a 3G-throttled mobile profile.
3. Walk the rubric category-by-category. Use the worked examples in
   `references/scored-examples.md` as calibration.
4. Run the static checks via `scripts/slop-scan.sh` for banned
   headline patterns, banned colour combinations, and other mechanical
   flags. The script is not the score — it is the floor.
5. Run `scripts/design-quality-score.sh` which aggregates the operator
   scores from `reports/design-quality/<template>.md` and produces the
   overall pass/fail for the pipeline.
6. For premium, ecommerce, lead-generation, or high-ticket templates, run the
   sibling `premium-ui-ux-design` gate and attach the premium score table.
7. File the per-template reports. Total score goes in the scorecard.
8. If any category scores below 8, the template does not ship; remediate
   and re-score.

## Preserved Domain Inputs
- A built production-like render of the site (`dist/` or deployed
  preview).
- The design-system tokens for the client (colour, type, spacing) so
  the operator can verify adherence.
- The brand style guide for copy and photography expectations.
- At least one prior benchmark scored site at the same rubric (the
  Phase 12 benchmark library when available).

## Preserved Domain Quality Guidance
- Every scored report cites the rubric clause by number.
- A score is defensible in a 5-minute walkthrough with a second operator.
- The aggregate score appears in `dashboards/quality-scorecard.md` row
  for the project.
- A score below 8 with a decision entry saying "we'll fix later" is
  not permitted to ship. The decision entry is the fix, not the
  waiver.

## Preserved Domain Anti-Patterns
- Scoring against taste. "I don't like it" is not a category; the
  rubric is.
- Scoring only the home page. Every primary template must be scored.
- Scoring desktop only. 3G-throttled mobile is a first-class view.
- Letting `slop-scan.sh` pass substitute for the human walkthrough.
  The script catches common failures; the rubric catches design
  failures.
- Inflating scores to clear the gate. A second operator spot-check is
  the long-term audit.

## Preserved Domain Outputs
- `reports/design-quality/<template>.md` per primary template.
- An aggregate row in `dashboards/quality-scorecard.md`.
- A pass or fail exit code from `scripts/design-quality-score.sh`
  consumed by the canonical CI pipeline step 12.

## Preserved Domain References
- `references/rubric.md` — the 7-category rubric with sub-criteria.
- `references/scored-examples.md` — worked examples with scores and
  rationales.
- `references/banned-patterns.md` — the list of banned patterns the
  slop-scan enforces.
- `references/score-calibration.md` — how two operators calibrate
  scoring to stay within one point per category.
- `references/report-template.md` — the per-template report format.
- `../premium-ui-ux-design/SKILL.md` — premium website gate for perceived
  value, conversion clarity, visual polish, and production fit.

## Notes

- This skill composes with `visual-qa` (visual-qa detects regressions,
  design-quality-score measures absolute quality).
- The skill composes with `design-system` (the rubric assumes the
  tokens are correct; violating tokens is a separate drift issue).
- In the canonical CI, this skill runs advisory on PRs and blocking
  on main.
