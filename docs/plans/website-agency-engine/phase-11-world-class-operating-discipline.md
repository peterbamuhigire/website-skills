# Phase 11 - World-Class Operating Discipline

## Objective

Prove that the engine works under multi-operator load, eliminate the documentation drift
the evaluation flagged as a residual risk, wire live telemetry into the quality scorecard
that Phase 9 only defined, install a structured experimentation programme, and add the
rendered-output quality scoring that prevents premium claims from drifting into AI slop.

This phase converts Phase 9's governance from "documented" to "demonstrated."

## Why This Phase Matters

The 2026-04-12 evaluation is explicit that Phase 9 added "the right governance structures"
but flags two unproven properties:

- whether a second or third operator can actually run the system cleanly
- whether the governance rhythm will be maintained instead of decaying

It also notes that monthly-report and the Phase 9 quality dashboard are not yet connected
to live data, that there is no structured experimentation layer, and that legacy
documentation drift continues in long-tail references.

Without this phase the engine remains founder-dependent in practice, even if the
documentation looks scalable. Premium agencies fail here more often than they fail at
craft. Most agencies can deliver one excellent site; few deliver excellent variance
across ten sites by three operators with measurable client outcomes.

## Core Outcomes

- a multi-operator validation programme that produces measured ramp-time, quality variance,
  and friction logs across at least four operator personas
- a published certification curriculum, exam, and first cohort
- a drift-eradication system that runs in CI and reports inconsistencies, dead links,
  dated terminology, and outdated references
- a live telemetry loop that feeds RUM, error tracking, and analytics data into the
  monthly-report skill and the quality scorecard
- a structured experimentation and CRO programme with a hypothesis logbook, A/B
  infrastructure documentation, statistical-significance literacy, and a quarterly
  learning cycle
- a rendered-output design-quality scoring rubric and anti-slop scan that runs on every
  shipped site

## Workstreams

### 1. Multi-Operator Validation and Certification

Run the system through real operators and measure where it actually breaks.

Required scope:

- four operator personas defined: strategist, designer/builder, SEO and content operator,
  QA and launch operator
- timed onboarding programme: each operator follows the published role track and runs
  one assigned project from intake to launch
- friction log captured at every stage gate; recorded under
  `docs/onboarding-validation/<operator>/friction-log.md`
- quality variance measured against the Phase 10 gates and the design-quality rubric
  (workstream 5 below)
- ramp-time targets:
  - strategist: first solo discovery in <= 2 weeks
  - builder: first solo build in <= 4 weeks
  - SEO operator: first solo SEO production cycle in <= 3 weeks
  - QA operator: first solo launch in <= 4 weeks
- certification programme: published syllabus, written exam, practical exam (a real
  test project), and a recertification cycle of 12 months
- first cohort enrolled with at least five operators

Output: `docs/onboarding-validation/2026/report.md` with measured outcomes per persona,
plus `certification/syllabus.md`, `certification/exam.md`, and `certification/cohort-2026-01.md`.

### 2. Documentation Coherence and Drift Eradication

Convert documentation maintenance from a periodic chore into a CI-enforced property.

Required scope:

- a top-level `glossary.md` that locks the canonical names for every concept, skill,
  artifact, deliverable, gate, and stage
- a `drift-check.sh` script that runs in CI and fails on:
  - dead internal links
  - references to renamed or deprecated skills
  - terminology that contradicts the glossary
  - dated framing (e.g. "as of 2024", "the next quarter") in references
  - SKILL.md files exceeding 500 lines without justification comment
  - duplicated guidance across reference files
- deprecation policy at `docs/deprecation-policy.md`: every deprecated skill or reference
  must be marked, dated, and have a removal date
- documentation style guide at `docs/doc-style-guide.md` covering tone, structure,
  reference vs SKILL split, link conventions, and the 500-line rule
- quarterly documentation audit added to the maintenance calendar with a written audit
  report filed to `project-log/decisions/`

Output: every drift-check failure produces a fixable PR; no quarterly audit reports
"no findings" without evidence of having actually scanned.

### 3. Live Telemetry and Observability Loop

Connect the quality dashboard Phase 9 defined to actual data.

Required scope:

- a new top-level `observability/SKILL.md` skill that bundles the operating standards
  for telemetry on every shipped site
- RUM (Real User Monitoring) implementation pattern that ships LCP, INP, CLS, and
  navigation type to a centralised dashboard; one provider standardised
  (web-vitals.js feeding to a self-hosted endpoint or a chosen service)
- error tracking pattern: Sentry or equivalent on every shipped site with project-scoped
  alerting
- analytics integration pattern: GA4 or Plausible per project, with the event taxonomy
  from `seo/references/analytics-event-map.md` as the contract
- monthly-report wiring: the `monthly-report` skill must ingest live data from at least
  one analytics source per project; refuses to render a report if the data source is
  unreachable
- quality scorecard automation: the Phase 9 scorecard becomes a generated artifact under
  `dashboards/quality-scorecard.md`, regenerated weekly from real project data
- alert thresholds defined in `observability/references/alert-thresholds.md`:
  - LCP regression > 200ms triggers an alert
  - INP regression > 50ms triggers an alert
  - error rate > 1% over 24 hours triggers an alert
  - CLS regression > 0.05 triggers an alert

Output: every shipped project has live telemetry visible to the agency and to the client.

### 4. Experimentation and CRO Operations

Add the missing scientific feedback loop.

Required scope:

- a new top-level `experimentation/SKILL.md` skill
- hypothesis template at `experimentation/references/hypothesis-template.md` covering:
  - audience and segment
  - current behaviour and baseline metric
  - hypothesis statement (we believe X because Y, measured by Z)
  - success metric and minimum detectable effect
  - guardrail metrics
  - decision rule
- A/B infrastructure documentation: GrowthBook is the recommended default for cost,
  open-source posture, and African-bandwidth friendliness, with Statsig and PostHog as
  documented alternatives
- statistical-significance primer at `experimentation/references/stat-significance-primer.md`
  covering p-values, confidence intervals, sample size estimation, sequential testing,
  and the dangers of peeking
- experimentation logbook: every retainer client maintains
  `project-log/experiments/<test-name>.md` with the full hypothesis, design, results,
  and decision
- post-launch experimentation cadence: every retainer client runs at least one test
  per quarter
- quarterly experimentation review: a written learning report consolidates results
  across all clients and feeds back into the strategy and conversion skills

Output: at least 30% of retainer clients have an active experiment running within
6 months of phase start.

### 5. Anti-Slop and Premium Output Validation

Install rendered-output design-quality scoring that prevents premium claims from
drifting into generic AI-aesthetic output.

Required scope:

- a new top-level `design-quality-score/SKILL.md` skill
- a published rendered-output design-quality rubric covering:
  - typographic rhythm (vertical baseline, modular scale adherence, consistent leading)
  - colour discipline (palette adherence, contrast in real context, banned palettes)
  - spacing consistency (8pt or 4pt grid adherence on real pages)
  - hierarchy strength (squint test pass, content priority visible)
  - copy quality (no banned AI words, no generic headlines, no template phrases)
  - trust-signal placement (proof above the fold, named clients, real testimonials)
  - section originality (no template-feeling sections, no generic three-column features)
- a `slop-scan.sh` script that runs against rendered HTML and CSS and reports:
  - banned colour combinations (per `design-system/references/ai-slop-prevention.md`)
  - banned easing curves
  - banned headline patterns (e.g. "Welcome to", "We are passionate about", "Your
    one-stop solution")
  - generic icon overuse
  - hero sections with fewer than 8 words of distinct value
- design-quality scoring is a pre-launch gate: the QA operator must score each primary
  template against the rubric and file the score in `project-log/decisions/`
- a worked-example library at `design-quality-score/references/scored-examples.md`
  showing real rendered outputs with their scores and rationales

Output: every shipped project has a recorded design-quality score and no project ships
with a rubric score below 8/10.

### 6. Cross-Cutting Discipline Integrations

Tie the new operating layers back to the rest of the engine.

Required scope:

- update `website-builder/SKILL.md` to make the design-quality score and live telemetry
  part of the build contract
- update `monthly-report/SKILL.md` to require live telemetry sources and refuse to
  render without them
- update `agency-positioning/SKILL.md` to reference the certification programme as part
  of premium positioning
- update `deploy/SKILL.md` to require the experimentation infrastructure decision at
  launch time, even when the answer is "no experiments yet"
- update the maintenance calendar in Phase 9 to include the quarterly drift audit, the
  quarterly experimentation review, and the annual certification recertification cycle

Output: no skill that the operator touches is unaware of the new operating discipline.

## Repository Outputs Required

- `docs/onboarding-validation/2026/report.md` with measured per-persona ramp times
- `certification/syllabus.md`, `certification/exam.md`, `certification/cohort-2026-01.md`
- `glossary.md` and `docs/deprecation-policy.md`
- `scripts/drift-check.sh` and integration into the canonical CI workflow
- `docs/doc-style-guide.md`
- `observability/SKILL.md` and supporting references
- `experimentation/SKILL.md` and supporting references
- `design-quality-score/SKILL.md` and supporting references
- `dashboards/quality-scorecard.md` regenerated automatically
- updates to `website-builder`, `monthly-report`, `agency-positioning`, and `deploy` skills
- a new entry in `project-log/decisions/` per workstream

## Success Criteria

- At least three operators other than the founder have run a complete project from
  intake to launch using only the published skills.
- Quality variance across operators on the published scorecard is <= 5%.
- Drift-check runs in CI; the next monthly run after this phase completes finds zero
  high-severity drift findings.
- Every shipped site has live telemetry visible to the agency and the client.
- Monthly reports are generated from live data; no operator-narrated metrics remain in
  the report template.
- At least 30% of retainer clients have an active experiment running with a documented
  hypothesis and decision rule.
- The first certification cohort is enrolled, has a published syllabus, and has at
  least one operator who has passed the practical exam.
- A re-run of the `docs/evaluation/` framework moves Governance and Scalability from
  8.4 to >= 9.3.

## Risks to Avoid

- Running multi-operator validation with only the founder's friends. Use real new
  hires or contractors so the friction is honest.
- Letting drift-check become a formality. The gate is only useful if it actually fails
  the build.
- Standing up telemetry without alerting. Data nobody looks at is decoration.
- Running experiments without documented hypotheses. Everything becomes opinion.
- Letting design-quality scoring become subjective. The rubric is the gate; the score
  must be defensible against the rubric, not against taste.
- Treating certification as ceremonial. The exam must be hard enough to fail.

## Reading Material To Buy And Provide At This Stage

- *The E-Myth Revisited* by Michael E. Gerber: systemising service work beyond the
  founder. Required pre-reading for the multi-operator validation workstream.
- *High Output Management* by Andrew S. Grove: training, supervision, and leverage at
  the level the certification programme requires.
- *Multipliers* by Liz Wiseman: how to design a system in which more operators raise
  rather than dilute quality.
- *An Elegant Puzzle* by Will Larson: organisational architecture and quality variance
  at small-team scale.
- *Trustworthy Online Controlled Experiments* by Ron Kohavi, Diane Tang, and Ya Xu:
  the canonical reference for the experimentation workstream.
- *You Should Test That* by Chris Goward: practical CRO programme design for agencies.
- *Lean Analytics* by Alistair Croll and Benjamin Yoskovitz: choosing the right
  metric per stage and avoiding vanity dashboards.
- *Observability Engineering* by Charity Majors, Liz Fong-Jones, and George Miranda:
  the engineering view of telemetry that the observability skill should be grounded in.
- *Site Reliability Engineering* edited by Betsy Beyer et al.: alerting philosophy
  and the discipline of measurable operations.
- *Docs for Developers* by Jared Bhatti et al.: the reference for the documentation
  style guide and the drift-eradication workstream.
- *Every Page Is Page One* by Mark Baker: the philosophy of self-contained, drift-
  resistant reference writing.
- *Refactoring UI* by Adam Wathan and Steve Schoger and *Practical Typography* by
  Matthew Butterick: the rubric authors for the design-quality scoring workstream.
