# Phase 11 and Phase 12 — Completion Report

**Date**: 2026-04-16
**Phases**: 11 (World-Class Operating Discipline) and 12 (African
Authority Engine), shipped concurrently.
**Source plans**:
- `docs/plans/website-agency-engine/phase-11-world-class-operating-discipline.md`
- `docs/plans/website-agency-engine/phase-12-african-authority-engine.md`

## Scope shipped (repository outputs)

### Phase 11 — Operating discipline

New skills:
- `observability/SKILL.md` + 5 references (alert-thresholds,
  rum-implementation, error-tracking, analytics-integration,
  runbook-template).
- `experimentation/SKILL.md` + 5 references (hypothesis-template,
  stat-significance-primer, ab-infrastructure,
  experiment-logbook-template, quarterly-review-template).
- `design-quality-score/SKILL.md` + 5 references (rubric,
  banned-patterns, scored-examples, score-calibration,
  report-template).

New scripts:
- `scripts/drift-check.sh` — documentation drift gate (CI step 11).
- `scripts/slop-scan.sh` — banned-pattern static scan.
- `scripts/design-quality-score.sh` — rubric aggregator (CI step 12).

New governance files:
- `glossary.md` — canonical-name authority.
- `docs/doc-style-guide.md` — writing standards.
- `docs/deprecation-policy.md` — rename and retirement rules.

New operator artefacts:
- `docs/onboarding-validation/2026/report.md` — four-persona ramp
  template.
- `certification/syllabus.md` — programme syllabus with four tracks.
- `certification/exam.md` — 60-question bank (Section A shared +
  B/C/D/E per track).
- `certification/cohort-2026-01.md` — first cohort record template.

Dashboard:
- `dashboards/quality-scorecard.md` — generated weekly (generation
  script is follow-up work; marker block documents schema).

Skill updates:
- `website-builder/references/maintenance-calendar.md` — quarterly
  drift audit, quarterly experimentation review, quarterly public-
  scorecard regeneration, annual certification recertification.
- `monthly-report/SKILL.md` — telemetry pre-flight, refuses to render
  without reachable sources.
- `deploy/SKILL.md` — launch decision record.
- `agency-positioning/SKILL.md` — premium-positioning proof assets.

Decision entry:
- `project-log/decisions/2026-04-16-phase-11-world-class-operating-discipline.md`

### Phase 12 — African authority engine

New skill:
- `africa-excellence/SKILL.md` + 6 references (low-bandwidth-patterns,
  mobile-money-ux, ussd-aware-design, african-language-pack,
  africa-trust-signals, cultural-patterns).

New public-facing files:
- `dashboards/public-scorecard.md` — quarterly public quality record.
- `docs/licensing-matrix.md` — per-path licensing.
- `docs/roadmap-public.md` — curated public roadmap.
- `LICENSE` — four-licence repository file (MIT + CC BY + CC BY-SA +
  CC BY-NC).

Skill updates:
- `they-ask-you-answer/SKILL.md` — continental publishing rhythm
  (quarterly cornerstone, benchmark releases, community contribution,
  conference presence, media relationships).
- `agency-positioning/SKILL.md` — proof assets section already
  referenced these artefacts from Phase 11; consistent.

Decision entry:
- `project-log/decisions/2026-04-16-phase-12-african-authority-engine.md`

## Operational outcomes not shipped (intentional)

These success criteria require real operators, clients, and publishing
and cannot be produced from within the repository. They are tracked on
the public roadmap:

- Multi-operator validation with at least three non-founder operators
  running complete projects.
- First certification cohort enrolled with at least five operators
  and at least one passed practical exam.
- Live telemetry scorecard generation against real client data.
- GrowthBook self-host provisioned and first experiment running.
- Three open-source benchmark sites published and indexed.
- Eight case studies with measurable outcomes published.
- Upstream open-source contribution merged.
- Conference talk or hosted workshop delivered.
- Public research note published.

## Verification

Drift-check (`scripts/drift-check.sh`) ran against the repository and
correctly flagged pre-existing drift (banned-term instances in
`sales-copywriting`, `visual-qa`, `they-ask-you-answer`, and
`sector-strategies/templates`; absolute-path links in `CLAUDE.md`,
`README.md`, and `docs/compatibility-report-2026-04-13.md`). None of
these were introduced by this phase; they are the gate doing its job
on legacy content. Follow-up: resolve the flagged instances as part
of the first quarterly documentation audit.

All new SKILL.md files are within the 500-line rule. All new scripts
are `set -euo pipefail`-compatible and have executable permissions.
Three new skills follow the canonical SKILL.md structure from
`docs/doc-style-guide.md`.

## Risks carried forward

- **Scorecard generation** (internal and public) depends on a job to
  be implemented against live telemetry; first deployment with the
  next retainer client.
- **Rubric two-operator calibration** requires the second operator to
  run the blind-scoring exercise in `scored-examples.md` (Example 4).
- **Drift-check pre-existing findings** should be cleaned up before
  the next merge to main to give the gate a clean baseline.

## Success criteria status

### Phase 11
- Multi-operator validation: **scaffolding in place**; operational
  outcome pending.
- Quality variance ≤ 5% across operators: **pending** first cohort.
- Drift-check runs in CI: **shipped**. Next monthly audit resolves
  pre-existing findings.
- Live telemetry on every shipped site: **contract shipped**;
  instrumentation pending per client.
- Monthly reports generated from live data: **skill updated to
  require it**; first live run pending.
- 30% of retainer clients with active experiment: **infrastructure
  shipped**; operational.
- First certification cohort enrolled: **syllabus/exam/cohort
  template shipped**; enrolment pending.
- Evaluation score Governance and Scalability ≥ 9.3: to be measured
  at next evaluation re-run.

### Phase 12
- Africa Excellence Layer codified: **shipped** (skill + 6
  references).
- Three open-source benchmark sites: **pending**; commitment on
  roadmap.
- Eight case studies: **pending**; commitment on roadmap.
- Public scorecard quarterly: **template shipped**; first
  regeneration pending.
- Two certification cohorts within 12 months: **pending**; programme
  ready.
- One upstream OSS contribution per year: **pending**; commitment
  on roadmap.
- One conference talk within 12 months: **pending**; commitment on
  roadmap.
- Twelve African client projects shipped: **pending**; operational.

## What this phase did not touch

- `accessibility-audit`, `visual-qa`, `security-gate` (Phase 10
  owns them; unchanged).
- `blog-writer`, `blog-idea-generator`, `sales-copywriting`,
  `brand-strategy`, `brand-storytelling`, `brand-style-guide`,
  `sectors/*` (domain craft, not operating discipline).
- `email-sender`, `form-ux-design`, `image-compression`, utility
  skills (unchanged).

## Next steps

1. File any drift-check findings as fixable PRs before the first
   operator-facing merge.
2. Implement the `scripts/generate-quality-scorecard.sh` generation
   job when the first retainer client instruments RUM.
3. Enrol cohort 2026-01.
4. Build the first Ugandan SME benchmark site in a separate repo
   under the CC BY-SA licence.
5. Run the first blind rubric calibration between two operators.

## Phase status

- Phase 10: shipped (2026-04-16).
- Phase 11: shipped (2026-04-16) — this report.
- Phase 12: shipped (2026-04-16) — this report.

The engine roadmap as written in `docs/plans/website-agency-engine/`
is now fully scaffolded. Operational outcomes continue per the public
roadmap.
