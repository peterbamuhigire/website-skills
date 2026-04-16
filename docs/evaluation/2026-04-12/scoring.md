# Scoring

## Scorecard

| Dimension | Score | Rating |
|---|---:|---|
| Coverage | 9/10 | Very strong |
| Instruction Quality | 8.5/10 | Strong |
| System Architecture | 8.6/10 | Strong and maturing |
| Strategy And Commercial System | 8.8/10 | Strong |
| Delivery And Launch Operations | 8.6/10 | Strong |
| Governance And Scalability | 8.4/10 | Strong but newly installed |
| Performance And Accessibility Enforcement | 7.3/10 | Improved but incomplete |
| Output Quality Potential | 8.4/10 | High ceiling, improved repeatability |

**Overall:** **8.5 / 10**

## Justification

### Coverage - 9/10

The repository now covers much more than website generation. It includes commercial logic,
discovery, strategy, content, design, SEO, launch operations, proof systems, reporting hooks,
and governance. The remaining coverage gaps are now concentrated in enforcement layers rather
than missing whole parts of the business.

### Instruction Quality - 8.5/10

The repo has many concrete, usable references that can drive real work. The best parts are no
longer isolated guidance files; they increasingly connect to artifacts, gates, and workflows.
The score is held back by remaining legacy duplication and some repo-level documentation drift.

### System Architecture - 8.6/10

Architecture is materially stronger than before. The artifact chain, stage gates, deployment
logic, and handbook-style cross-linking all improve coherence. The system is still not fully
machine-enforced, but it is now much more legible and governable.

### Strategy And Commercial System - 8.8/10

This is now one of the strongest areas. Qualification, discovery, positioning, trust design,
page-goal mapping, proof logic, and strategy handoff are all materially better than they were
in the earlier state of the repo. The strategy layer is now a real system.

### Delivery And Launch Operations - 8.6/10

Phase 6 changed this category significantly. The repository now has QA matrices, pre-launch
verification, deployment and rollback runbooks, observability baselines, post-launch review,
and a Playwright starter. The remaining gap is automation, not conceptual weakness.

### Governance And Scalability - 8.4/10

Phase 9 adds the right structures: role-based onboarding, governance policy, quality metrics,
maintenance cadence, and a handbook index. That is a major improvement. The score is slightly
held back because the model is newly documented and not yet proven through repeated team-scale use.

### Performance And Accessibility Enforcement - 7.3/10

This is still the weakest dimension relative to the repo's ambition. The standards exist and
the launch layer is stronger, but there is still no first-class accessibility gate, no full
performance gate, and no canonical CI enforcement path.

### Output Quality Potential - 8.4/10

The ceiling is now higher and the variance is lower than before. A strong operator can use this
repo to run a premium agency system with much more consistency. The final jump to elite status
depends on the remaining enforcement and visual QA layers.

---

## Addendum — Post-Phase 12 (2026-04-16)

Phases 10, 11, and 12 shipped on 2026-04-16. The table below supersedes the
2026-04-12 scores for current-state reading. The previous scores remain above
as historical record.

### Revised Scorecard

| Dimension | 2026-04-12 | 2026-04-16 | Rating | Driver of the change |
|---|---:|---:|---|---|
| Coverage | 9.0/10 | 9.5/10 | Very strong | africa-excellence + observability + experimentation + design-quality-score close the remaining named gaps |
| Instruction Quality | 8.5/10 | 9.0/10 | Strong | glossary, doc style guide, deprecation policy make the authoring contract explicit |
| System Architecture | 8.6/10 | 9.3/10 | Elite-adjacent | Phase 10 CI pipeline + Phase 11 drift-check + Phase 12 licensing and public surface close the coherence gap |
| Strategy And Commercial System | 8.8/10 | 9.0/10 | Strong | premium-positioning proof assets section makes the commercial claims defensible |
| Delivery And Launch Operations | 8.6/10 | 9.3/10 | Elite | canonical CI + deploy launch-decision record + observability contract close the automation gap |
| Governance And Scalability | 8.4/10 | 9.2/10 (infra) / 7.5/10 (demonstrated) | Infra ready, demo pending | certification, drift-check, calibration, quarterly cadence shipped; real multi-operator execution still pending |
| Performance And Accessibility Enforcement | 7.3/10 | 9.4/10 | Elite | perf-gate, a11y-gate, visual-qa, security-gate are now blocking CI steps calibrated for African 3G |
| Output Quality Potential | 8.4/10 | 9.3/10 | High | design-quality-score rubric + slop-scan + banned-patterns turn premium into a defensible score |

**Overall (infrastructure)**: **9.2 / 10**
**Overall (demonstrated)**: **8.2 / 10** — reduced by operational outcomes not yet executed.

### Why the two overall scores

The engine as a repository is elite. The engine as a running operation has not
yet been demonstrated at multi-operator scale with real clients. This split is
honest: the 9.2 is the floor the system holds; the 8.2 acknowledges that
"works in practice" is a separate claim that requires separate evidence.

A re-run of this evaluation framework after the first certified cohort ships
its first projects — and after three benchmark sites publish — would raise the
demonstrated score into the same range as the infrastructure score.

### Per-dimension commentary

**Coverage 9.5/10** — The only remaining named gaps (upstream OSS contribution
cadence, published research notes, second-cohort recertification loop) are
operational, not coverage.

**System Architecture 9.3/10** — The artefact chain runs from intake through
strategy, build, launch, governance, and authority. Licensing is explicit;
dead-link and drift detection is a CI gate. The remaining 0.7 is head-room for
the generation scripts that turn the scorecards from templates into live data.

**Delivery and Launch Operations 9.3/10** — Canonical CI with 15 blocking
steps, post-deploy smoke, rollback hook, launch decision record. The gap is
only the live wiring of the observability endpoints to a real client.

**Governance and Scalability (infra 9.2, demonstrated 7.5)** — The governance
structures are now measurable: drift-check is a blocking gate; the quarterly
cadence is in the maintenance calendar; the certification programme has a
publishable syllabus and a 60-question exam bank. The demonstrated score waits
for multi-operator validation.

**Performance and Accessibility Enforcement 9.4/10** — From 7.3 to 9.4 in the
same week. Lighthouse perf-gate with 3G profile, axe-core a11y-gate, Playwright
visual-qa, and security-gate are all blocking CI steps. Africa-realistic
thresholds are calibrated. The remaining 0.6 is a residual margin for
fine-tuning as real client traffic reveals edge cases.

**Output Quality Potential 9.3/10** — The design-quality rubric plus
slop-scan is the mechanism that keeps "premium" from drifting. Two-operator
calibration discipline is the next proof point to close the remaining gap.
