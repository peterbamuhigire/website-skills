---
name: kaizen-engine-and-product-improvement
description: Use when auditing or improving the website engine or any website, landing page, ecommerce experience, dashboard, portal, or visual web product it produces.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Kaizen Engine and Product Improvement
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Auditing this engine or a website/product after discovery, build, launch, or user feedback.
- Converting CRO, accessibility, visual QA, performance, SEO, content, or maintenance findings into tested improvements.

## Do Not Use When

- The task is only a single security or visual gate.
- A current platform, legal, accessibility, or market claim lacks Digital Research verification.

## Required Inputs

| Artefact | Source/provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Website/product scope, audience/page goals, content/design/build artefacts, analytics or user evidence, current score, and constraints | Project and engine | yes | Set audit scope and improvement target | Stop or mark unassessed |

## Workflow

1. Read the local adoption plan and portfolio standard; resolve the design-system engine for visual work.
2. Inventory strategy, page/build, UX, content, SEO, commerce, quality, security, launch, and maintenance routes.
3. Score every applicable dimension and product type. Publish `min(raw score, 65)` and record blockers.
4. Audit value proposition, information architecture, content, accessibility, responsive behaviour, visual consistency, performance, security, SEO/GEO, conversion ethics, analytics, deployment, and maintenance.
5. Write a 95/100 plan with exact file, owner, experiment, metric, acceptance evidence, and rollback.
6. Run one reversible test or content/design improvement; check with visual, accessibility, security, performance, and conversion gates.
7. Standardise successful learning in the owning skill/reference/fixture, retest and rescore the affected output, and set the next review.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Capped audit and 95/100 improvement plan | Delivery and release owner | Evidence gaps, blockers, owners, experiments, acceptance proof, and re-audit date are explicit |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Route inventory, score calculations, rendered evidence, gate results, experiment log, and before/after review | Release owner | Another reviewer can reproduce the score and verify the named improvement |

<!-- dual-compat-end -->

## Capability Contract

Read, search, rendering, visual inspection, and relevant project gates are required for a full audit. Default to read-only; remediation, content, design, code, baseline, or production changes require separate authority.

## Degraded Mode

If representative renders, analytics, user evidence, fonts, source registers, or gate tools are unavailable, return a qualified partial score, mark affected checks `not assessed`, and do not certify readiness.

## Decision Rules

| Finding | Action | Failure avoided |
|---|---|---|
| Output evidence is unavailable | Mark unassessed and block the affected claim | Inflated score |
| A change improves one metric but harms accessibility, trust, security, or another guardrail | Reject, roll back, or escalate | Local optimisation |
| A change passes gates and improves the target measure | Standardise it and schedule re-audit | Lessons lost in chat |

## Quality Standards

Do not infer conversion improvement without measurement. Do not use dated platform facts without verification. Keep content/structure in this engine and visual-system decisions in design-system-skills. Make user controls, trust, privacy, accessibility, and fallback paths explicit for AI features.

Apply Kaizen at two levels: first audit this skills engine's routes, references,
validators, handoffs, and visual-reference handling; then audit the individual site
or visual web product. Both initial analyses publish `min(raw_score, 65)` before a
95/100 improvement cycle. Inspiration books and captures may inform hypotheses,
but only differentiated, rights-safe, accessible, performant, measured changes
may be standardised.

## Mandatory 65-to-95 gate

The first review is an initial analysis: calculate raw findings, publish only
`min(raw_score, 65)`, and keep missing renders, analytics, and accessibility or
security evidence visible as blockers. Freeze that baseline before improving.
Target 95/100 one reversible change at a time, naming the root cause, exact owning
skill or artefact, owner, measure, visual/accessibility/performance guardrails,
stop/rollback rule, acceptance evidence, standardisation decision, and re-audit date.

## Anti-Patterns

- Copying a trendy layout without page-goal evidence. Fix: test the user task.
- Calling a site premium without rendered proof. Fix: run visual and accessibility QA.
- Adding AI for novelty. Fix: prove the user problem and safe fallback first.
- Optimising clicks while hiding uncertainty or consent. Fix: apply ethical persuasion and trust gates.
- Closing a ticket without a re-test. Fix: retain before/after evidence.

## Worked Example

If a landing-page experiment raises form starts but increases abandonment or removes accessible error feedback, keep the result as a failed experiment, restore the safe baseline, record the evidence, and test a narrower change before standardising.

## Mandatory Digital Research currentness gate

Every Kaizen cycle must begin with `digital-research-skills` source evaluation
and source verification. Record scope, dates, freshness class, support status,
uncertainty, and review date for current web standards, accessibility, browser,
platform, security, SEO, and lifecycle claims; quarantine unsupported claims as
`NOT_ASSESSED`. Apply the [portfolio Kaizen currentness gate](../../../../digital-research-skills/docs/continuous-improvement/kaizen-currentness-gate.md).

## References

- [Local adoption plan](../../../docs/continuous-improvement/kaizen-adoption-2026-08.md)
- Portfolio standard: resolve `digital-research-skills` from the global routing table, then read `docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md`.
- [Book-driven positioning, story, and proof](../../brand/brand-strategy/references/book-driven-positioning-story-and-proof.md) - strategy, narrative, proof, experiments, and currentness.
- [Book-driven Kaizen Wave 3](references/book-driven-kaizen-wave-3-2026-09-02.md) - task-first dashboards, retrieval/SEO evidence, experimentation, image QA, accessibility, and protocol currency.
- `skills/orchestration/website-builder/`
- `skills/quality-gates/design-quality-score/`
