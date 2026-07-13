---
name: visual-qa
description: Use when reviewing rendered routes for screenshot drift, hierarchy, overflow, empty sections, responsive states, content artefacts, and visual regressions; use design-quality-score for the broader design rubric.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Visual QA
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Run a read-only rendered-output gate that distinguishes measured regressions from unassessed visual risk.

<!-- dual-compat-start -->
## Use When

- Routes can be rendered before release
- screenshot baselines changed
- responsive or multilingual content may overflow or create empty sections.

## Do Not Use When

- Use `design-quality-score` for the seven-category design score or accessibility-audit for WCAG conformance.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Test build, route and viewport matrix, approved baselines, dynamic-region rules, and content states | Build pipeline and project artefacts | yes | Define comparable renders | Stop when baselines are missing or intentionally changed without approval |

## Workflow

1. Confirm read-only scope and build identity
2. Render the route, locale, viewport, and state matrix
3. Inspect diffs plus hierarchy, overflow, emptiness, content artefacts, and AI-slop markers
4. Stop release on unexplained blocking drift, recover by authorised repair or approved baseline decision, then rerun the matrix.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Visual QA report and diff set | Designers, developers, and release owner | Every route/state is pass, fail, or not assessed with an image or assertion reference |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Screenshots, diff metrics, assertion logs, and baseline decision | Release owner | Evidence names build, browser, viewport, locale, and state |

<!-- dual-compat-end -->
## Capability Contract

Read, search, rendering, browser, and execution capabilities are required for full assessment. Default to read-only. Baseline updates, code edits, and production mutation require explicit authority.

## Degraded Mode

Without rendering, browsers, fonts, devices, or baselines, return the narrowest qualified static review and mark visual checks `not assessed`; do not approve the release.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Unexpected diff affects hierarchy, content, or interaction | Block and investigate | Normalised visual regression |
| Intentional change has approved evidence | Update baseline separately and rerun | Baseline laundering |

## Quality Standards

- Cover every route family, locale, agreed viewport, and meaningful state; baseline changes need a decision record rather than a blanket refresh.

## Anti-Patterns

- Refreshing all baselines after failures. Fix: approve intentional changes individually.
- Testing the homepage only. Fix: sample every template and locale family.
- Ignoring dynamic regions. Fix: stabilise or mask only documented regions.
- Editing during read-only QA. Fix: separate finding evidence from remediation.
- Calling missing fonts a pass. Fix: mark the render unassessed and restore the production font environment.

## Worked Example

A Kiswahili service title clips at 360 px while English passes. Attach both renders, fail that route/state, repair the component, and rerun both locales to catch regression.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- Every build of a client site, as a CI-time gate before deploy.
- Before shipping any new template or component.
- When reviewing a design change that affects layout, hierarchy, or rhythm.

## Preserved Domain Exclusions
- Evaluating whether a design system is correct at the token level — that is
  `design-system`.
- Reviewing copy quality alone — that is `content-writing` and
  `design-quality-score`.

## Core contract
Every primary template passes:
1. Screenshot diff under 0.1% pixel difference vs the approved baseline at
   three viewports (375, 768, 1280) and in every theme the project supports.
2. Heading hierarchy assertion: exactly one h1, no skipped levels.
3. Horizontal overflow assertion: no element produces horizontal scroll at 375px.
4. Empty-section warning: every `<section>` contains >= 60 words of body copy
   or an explicit `data-visual-qa="intentionally-sparse"` opt-out.
5. AI-slop scan: no banned palettes, banned easing curves, banned headline
   patterns, generic icon overuse, or low-information hero sections.
6. Structured review checklist in `references/review-checklist.md` completed
   and signed by the QA operator.

A failed diff requires explicit reviewer approval and a baseline update PR.

## Canonical Command

```bash
# From a client project root after resolving this engine as WEBSITE_SKILLS
bash "$WEBSITE_SKILLS/scripts/visual-qa.sh"
```

The command:
1. Starts a static preview on `:4321`.
2. Captures screenshots per template, per viewport, per theme.
3. Diffs against `tests/visual/baseline/`.
4. Runs the structural assertions (hierarchy, overflow, empty-section).
5. Runs `scripts/slop-scan.sh` against rendered HTML and CSS.
6. Writes `reports/visual/diff/` and `reports/visual/summary.md`.
7. Exits non-zero on any diff above threshold or structural failure.

## Preserved Domain Workflow
1. Build the site.
2. Run the canonical command.
3. For any diff above 0.1%:
   a. If the change is intentional, commit the new baseline with a one-line
      reason in the commit message (`visual-qa baseline update: hero image
      refresh for Mara campaign`).
   b. If the change is unintentional, fix the regression and re-run.
4. Complete the structured checklist once per template per launch.
5. File the signed checklist under `project-log/launches/<project>/visual-qa.md`.

## Preserved Domain Inputs
- A built static output at `./dist/`.
- The template list from `performance-budgets.json` (shared source).
- Baselines committed under `tests/visual/baseline/<template>/<viewport>.png`.

## Preserved Domain Quality Guidance
- Baselines are reviewed by a human; never auto-accepted.
- Diffs live in PR comments with before/after thumbnails.
- Hierarchy, overflow, and empty-section are absolute assertions; no
  thresholds.
- AI-slop is evaluated per the **`design-system-skills`** engine's
  `doctrine/references/ai-slop-taxonomy.md` and `ai-slop-banned-fonts.md`
  (resolve its path from your global engine-routing table), plus the additions
  in `references/slop-rules.md`.
- The structured checklist is a human review of the gate's findings, not a
  replacement.

## Preserved Domain Anti-Patterns
- Auto-accepting baseline updates in CI. Baselines are the acceptance contract.
- Shipping a page with an empty section because "it was just a spacer".
- Shipping hero headlines like "Welcome to <brand>" or "Your one-stop solution".
- Using gradient hero backgrounds from the banned palette.
- Adding a visual-qa opt-out on every section to pass the gate.
- Letting visual QA become a single-reviewer opinion. The rubric is the gate.

## Preserved Domain Outputs
- `tests/visual/baseline/<template>/<viewport>.png` — committed baselines.
- `reports/visual/diff/<template>/<viewport>.diff.png` — diff images when a
  diff exceeds threshold.
- `reports/visual/summary.md` — CI-friendly summary.
- A signed manual checklist per launch.
- A blocking CI status on any above-threshold diff or structural failure.

## Preserved Domain References
- `references/screenshot-diff-harness.md` — Playwright harness and thresholds.
- `references/baseline-management.md` — how baselines are captured, versioned,
  and updated.
- `references/hierarchy-overflow-checks.md` — the structural assertions.
- `references/slop-rules.md` — banned patterns (extension of the
  `design-system-skills` engine's `doctrine/references/ai-slop-taxonomy.md`;
  resolve its path via your global engine-routing table).
- `references/review-checklist.md` — the structured human review sheet.

## Notes
- This skill complements `design-quality-score`; that skill scores the
  rendered output on a rubric, while this skill gates pixel-level regressions.
- Baseline images are stored in Git LFS on large projects; see
  `baseline-management.md` for the threshold.
- Do not treat the visual gate as optional for non-visual-heavy projects; a
  text-heavy site regresses hierarchy and spacing just as often.
