# Success Metrics - World-Class Agency Engine

This document defines the observable metrics that prove the 12-phase plan has actually
produced a world-class agency engine, rather than only documenting the intent of one.

These metrics are the acceptance contract for the plan as a whole. Update this file at
the end of every phase. If a metric cannot be measured, the phase is not complete.

## Top-Level Repository Score

The 2026-04-12 evaluation scored the system at **8.5/10**. The plan target is:

| Milestone | Target Score | Source |
|---|---:|---|
| End of Phase 10 | 9.0 / 10 | Re-run of `docs/evaluation/` framework after enforcement gates |
| End of Phase 11 | 9.3 / 10 | Re-run of `docs/evaluation/` framework after operating discipline |
| End of Phase 12 | 9.5 / 10 | Re-run plus first public benchmark + certification cohort enrolled |

A re-evaluation must be filed to `docs/evaluation/YYYY-MM-DD/` after each phase, using the
same scorecard structure as the 2026-04-12 evaluation.

## Dimension Targets

Every dimension in the evaluation scorecard must move to at least the values below.

| Dimension | Current | End-of-Phase-10 | End-of-Phase-11 | End-of-Phase-12 |
|---|---:|---:|---:|---:|
| Coverage | 9.0 | 9.2 | 9.4 | 9.5 |
| Instruction Quality | 8.5 | 8.8 | 9.2 | 9.4 |
| System Architecture | 8.6 | 9.0 | 9.3 | 9.5 |
| Strategy and Commercial System | 8.8 | 8.8 | 9.0 | 9.3 |
| Delivery and Launch Operations | 8.6 | 9.3 | 9.4 | 9.5 |
| Governance and Scalability | 8.4 | 8.6 | 9.3 | 9.5 |
| Performance and Accessibility Enforcement | 7.3 | 9.2 | 9.4 | 9.5 |
| Output Quality Potential | 8.4 | 9.0 | 9.3 | 9.5 |

## Phase 10 Metrics - Hard Enforcement and Visual QA Gates

**Performance gate**

- Lighthouse score is enforced at >= 95 for performance, >= 100 for SEO, >= 95 for best practices.
- One canonical command (`pnpm run perf-gate` or equivalent) runs the full performance check.
- JS budget is enforced: <= 80 KB gzip per route on first load.
- Image budget is enforced: <= 200 KB per above-the-fold image after compression.
- Performance regression on any tracked route fails CI.

**Accessibility gate**

- Every project ships with zero axe-core violations at "serious" or "critical" severity.
- Keyboard-only navigation passes the published checklist on every primary template.
- Focus order is verified on the homepage, pricing/services page, contact form, and one
  long-form page on every project.
- Screen reader smoke test (NVDA on Windows, VoiceOver on macOS/iOS) is documented per
  project before launch.

**Visual QA**

- Every project has baseline screenshots stored under `tests/visual/baseline/`.
- Screenshot diff runs on every PR; threshold is 0.1% pixel difference unless approved.
- Hierarchy and overflow checks run on every primary template at 375px, 768px, and 1280px.
- AI-slop scan on rendered output produces a pass/fail with documented heuristics.

**Canonical CI**

- One workflow file is the system standard (`.github/workflows/website.yml`).
- Every client project inherits or copies this workflow on day one.
- CI runs: install -> build -> unit -> e2e -> metadata audit -> Lighthouse -> axe -> visual diff -> security scan.
- Failed CI blocks deploy in the canonical pipeline.

**Security and compliance gate**

- Dependency audit runs in CI; any "high" or "critical" CVE blocks deploy.
- CSP headers are validated on staging before launch.
- SRI is enforced on any third-party asset that survived design review.
- A privacy-and-cookie baseline is verified per the operating compliance matrix
  (Uganda DPPA, Kenya DPA, GDPR, POPIA).

## Phase 11 Metrics - World-Class Operating Discipline

**Multi-operator proof**

- At least three operators other than the founder have run a complete project from
  intake to launch using only the published skills and references.
- Time to onboard a new strategist or builder to first solo project: <= 6 weeks.
- Quality variance across operators on the published scorecard: <= 5%.
- Certification programme has a defined curriculum, exam, and first cohort enrolled.

**Documentation coherence**

- Drift-detection script runs in CI and reports any term-inconsistency, dead link,
  or dated reference.
- Glossary is single source of truth and is enforced by the drift script.
- Every deprecated skill or reference is marked, dated, and scheduled for removal.
- No SKILL.md exceeds 500 lines without justification.

**Telemetry and observability**

- Every shipped site reports RUM (LCP, INP, CLS) to a centralised dashboard.
- Sentry or equivalent error tracking is wired on every shipped site.
- Monthly-report skill ingests live data from at least one analytics source per project.
- Quality scorecard updates from real data, not from operator narration.

**Experimentation and CRO**

- Hypothesis logbook is maintained per project under `project-log/experiments/`.
- A/B testing infrastructure (GrowthBook, Statsig, or equivalent) is documented and
  used on at least 30% of retainer clients.
- Statistical-significance primer is part of operator certification.
- Quarterly experimentation review produces a written learning report.

**Anti-slop and premium output**

- Every page passes the rendered-output design-quality rubric before sign-off.
- Anti-slop heuristics scan typography rhythm, contrast, spacing, and copy patterns.
- Premium-output review is a documented stage gate, not a personal opinion.

## Phase 12 Metrics - African Authority Engine

**Africa excellence**

- Every shipped site is tested on simulated 3G and 4G connections from a Nairobi or
  Lagos test endpoint.
- Mobile money integration patterns are documented for M-Pesa, MTN MoMo, Airtel Money,
  and at least one West African provider.
- Multilingual support is documented and proven for English, French, Kiswahili, and
  at least one of Luganda, Amharic, or Yoruba per client need.
- Country-specific trust signals are catalogued for at least six African markets.

**Continental authority**

- At least three open-source benchmark sites are public, indexed, and demonstrate the
  system's standards across different sectors.
- Case-study corpus is published with at least eight real client outcomes per the Phase 7 template.
- Public quality scorecard is updated quarterly and is visible on the agency site.
- The agency has presented at least once at an African design or developer conference
  (or hosted its own) within 12 months of Phase 12 completion.

**Operator certification network**

- Certification programme has a published syllabus, exam, and recertification cycle.
- First cohort has at least five enrolled operators.
- Certified operators can be hired into client projects with a documented quality
  contract.

**Knowledge commons**

- Skills, references, and benchmarks are open or partially open under a stated licence.
- A public changelog records every material change to the engine.
- The agency contributes back to at least one upstream open-source project (Astro,
  Tailwind, axe-core, or equivalent) that the engine depends on.

## Commercial Health Metrics (Cross-Phase)

These hold throughout Phases 10-12. If they regress, the plan is failing.

| Metric | Target | Why |
|---|---|---|
| Average project value | >= $12,000 | Premium positioning is the commercial frame |
| Gross margin per project | >= 60% | Below this, scaling is unprofitable |
| Refund or dispute rate | <= 2% | Quality gates should prevent disputes |
| Retainer attach rate | >= 40% of new projects | Phase 8 outcome must hold |
| Proposal win rate | >= 35% on qualified leads | Phase 1-2 qualification should not erode |
| Time from intake to launch | <= 10 weeks for Foundation tier | Discipline, not speed-for-speed's sake |

## How To Use This Document

- Update the dimension table after every phase re-evaluation.
- Capture missed metrics as incidents in `project-log/incidents/`.
- Treat unmeasured metrics as failures. If you cannot measure it, the system is not yet
  world-class on that dimension.
- The plan is complete only when every metric in this document is observable and at target.
