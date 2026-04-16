# Gap Analysis

## Main System Gaps

### 1. Enforcement Still Lags Behind Guidance

This is now the primary limiter.

The repository has stronger artifacts, better stage gates, and much better operations than
it had before, but too many standards are still enforced socially rather than mechanically.

Examples:

- Lighthouse targets are stated, but not enforced by a hard gate
- QA and rollback standards exist, but are not yet wired into an automated CI pipeline
- accessibility standards are present in multiple places, but there is no dedicated accessibility gate
- strategy and trust requirements are documented, but downstream validation is still light

### 2. Visual QA Is Still Missing

The repo has excellent design thinking, but still lacks a first-class rendered-output review loop.

What is still missing:

- screenshot comparison or screenshot review guidance as an operational gate
- hierarchy and overflow checks on real pages
- a structured method to catch "technically correct, visually weak" output

This matters because premium design quality is judged on the page, not in the reference notes.

### 3. Performance Is Better Framed Than Enforced

Performance discipline is stronger than before, especially after Phase 6, but it is not yet
machine-enforced across the system.

Missing or still weak:

- one canonical performance-gate command
- route-level performance budget enforcement
- CI failure on performance regression
- bundle, image, and JS budget tracking

### 4. Accessibility Is Still Not A First-Class System Skill

Accessibility is respected in the repo, but it still behaves more like a distributed expectation
than a dedicated operating layer.

What remains missing:

- a dedicated accessibility-audit or accessibility-gate skill
- stronger keyboard/focus verification rules in the main launch flow
- more explicit accessibility pass/fail output tied to stage gates

### 5. CI And Automation Are Still Partial

The repository now has:

- QA matrices
- pre-launch checklists
- rollback runbooks
- a Playwright starter

That is real progress. But the engine still lacks a canonical automated CI path at the repository level.

Remaining gap:

- the standards exist, but the repo does not yet guarantee they run automatically and consistently

### 6. Governance Exists, But Has Not Yet Been Proven At Team Scale

Phase 9 added the right governance structures:

- role-based training map
- governance policy
- quality metrics dashboard definition
- maintenance calendar
- agency operations handbook index

This closes the documentation gap.

What remains unproven:

- whether a second or third operator can run the system cleanly in practice
- whether the governance rhythm will actually be maintained
- whether repository reviews will consistently remove drift instead of only documenting it

### 7. Legacy Documentation Drift Is Reduced, But Not Eliminated

The highest-visibility repo-level drift has now been cleaned up, especially in the top-level
documentation. The remaining gap is narrower and now sits mostly in older legacy references
and long-tail supporting docs rather than in the primary entry points.

What still remains:

- some older reference files still carry dated framing
- a few supporting docs still overlap in scope or terminology
- some capabilities are better documented than they are mechanically enforced

This is no longer a top-level coherence problem, but it still warrants periodic cleanup.

## What Has Been Closed Since The Earlier Evaluation

These were real weaknesses before and are materially better now:

- intake and qualification are now structured
- strategy is now a first-class artifact rather than an implied activity
- launch and rollback are now documented system behavior
- post-launch review exists as an operating standard
- governance and onboarding are now explicit
- the repo is less founder-dependent than before

## Bottom-Line Limiters

The main blockers preventing a true world-class score today are:

- insufficient hard validation
- missing visual QA
- incomplete accessibility enforcement
- incomplete CI integration
- limited proof that the governance model works under multi-operator conditions

---

## Addendum — Post-Phase 12 (2026-04-16)

Phases 10, 11, and 12 shipped on 2026-04-16. Every gap named above is now
addressed at the repository-infrastructure layer. The table below maps each
historical gap to its closure, and then lists the residual gaps that remain
genuinely open.

### Closed gaps

| 2026-04-12 gap | How it was closed |
|---|---|
| #1 Enforcement still lags behind guidance | Phase 10 wired perf-gate, a11y-gate, visual-qa, security-gate into the 15-step canonical CI at `templates/ci/website.yml`. Phase 11 added drift-check and design-quality-score. Every standard named in the repo now has a blocking CI counterpart. |
| #2 Visual QA is still missing | `visual-qa/` skill + `scripts/visual-qa.sh` (screenshot diff + structural assertions + AI-slop scan) ship in Phase 10. Phase 11's `design-quality-score/` rubric adds the absolute-quality layer. |
| #3 Performance is better framed than enforced | `scripts/perf-gate.sh` + `lighthouserc.json` + `performance-budgets.json`, calibrated for African 3G (1638 Kbps, 300 ms RTT, 350 KB budget). Blocking CI step 7. |
| #4 Accessibility is still not a first-class system skill | `accessibility-audit/` skill + `scripts/a11y-gate.sh` (axe-core + manual checklist + NVDA/VoiceOver smoke). Blocking CI step 8. |
| #5 CI and automation are still partial | `templates/ci/website.yml` 15 ordered blocking steps; `scripts/install-canonical-ci.sh` inherits it into client projects. Any client not running the canonical pipeline is not considered shipped on the engine. |
| #6 Governance exists but has not been proven at team scale | Infrastructure shipped: `certification/syllabus.md`, `certification/exam.md` (60-question bank across shared + 4 tracks), `docs/onboarding-validation/2026/report.md`. **Team-scale proof remains pending** — see residual gaps below. |
| #7 Legacy documentation drift reduced but not eliminated | `scripts/drift-check.sh` (blocking CI step 11) now fails the build on dead links, deprecated-entity references, dated framing, banned terms, 500-line overruns, duplicated guidance, and forbidden constructions. Quarterly audit added to maintenance calendar. Pre-existing drift instances are the first quarterly audit's workload. |

### Residual gaps

These are no longer repository-infrastructure gaps; they are operational.
Repository authorship cannot close them — running the engine closes them.

#### A. Multi-operator demonstration (operational)

The certification programme is ready to run; the first cohort is not yet
enrolled. Until at least three non-founder operators have shipped complete
projects end-to-end using only the published skills, the governance model
remains unproven in practice.

#### B. Live telemetry generation (operational)

`observability/SKILL.md` defines the RUM + error-tracking + analytics + alerts
contract. `dashboards/quality-scorecard.md` and `dashboards/public-scorecard.md`
define the generated-artefact contract. The generation script runs against the
first retainer client with instrumentation live — which has not happened yet.

#### C. Experimentation execution (operational)

`experimentation/SKILL.md` plus the hypothesis template, stat primer, A/B
infrastructure reference, logbook template, and quarterly review template are
shipped. Zero experiments have been decided yet. The Phase 11 target of 30% of
retainer clients running an active experiment needs retainer clients.

#### D. Public authority assets (operational)

Benchmark library, case-study corpus, upstream OSS contribution, conference
presence, and research note — all are commitments on
`docs/roadmap-public.md`. Repository infrastructure (licensing matrix, public
scorecard template, africa-excellence skill) is in place; the assets
themselves are built outside the repository.

#### E. Rubric inter-operator calibration (quick close)

The design-quality-score rubric and worked examples are shipped. Two-operator
blind-scoring of the Example 4 calibration exercise has not yet happened. This
is a single 60-minute exercise away from closing.

#### F. Pre-existing drift cleanup (quick close)

`drift-check.sh` surfaces pre-existing legacy drift: banned-term instances in
`sales-copywriting/references/`, absolute-path links in `CLAUDE.md` and
`README.md`, dated framing in `sector-strategies/templates/`. None were
introduced by Phase 11/12. The first quarterly documentation audit closes them.

### Revised bottom-line limiters

Not blockers to world-class *claim* — the infrastructure is world-class. The
residuals are blockers to world-class *demonstration*:

- first certification cohort shipping its first real projects
- first client running with live telemetry feeding the scorecard
- first benchmark site published and indexed under CC BY-SA

All three are measurable, timed, and tracked on the public roadmap.
