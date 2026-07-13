---
name: cro-audit
description: Use when auditing an existing website or completed build for evidence-backed conversion barriers and test priorities; do not use to implement fixes or invent a growth strategy without an inspectable artefact.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Cro Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- A built or live site needs read-only diagnosis of motivation, relevance, clarity, anxiety, friction, distraction, forms, trust, CTA, or mobile journey issues.
- Observations and behavioural evidence must become a prioritised remediation and experiment backlog.

## Do not use when
- The user requests direct implementation; hand findings to the relevant build skill after separate authority.
- There is no target artefact or journey to inspect; request one instead of auditing from assumptions.
- The request is ongoing experiment operation rather than diagnosis; use `experimentation` after an evidence-backed backlog exists.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Inspectable site/build, target journeys, and device scope | URL, repository, or supplied captures | yes | Stop and request an artefact; do not audit an imagined site. |
| Conversion definition, audience, offer, and business constraints | Measurement/discovery brief | yes | Report usability observations only, not CRO priorities. |
| Analytics, research, experiment, support, and revenue evidence | Approved providers | conditional | Label findings heuristic and impact unmeasured. |

## Workflow
1. Define the audit scope and what success or risk means in context.
2. Inspect the target using the relevant checklist and preserved guidance.
3. For ecommerce, premium, or revenue-critical sites, classify each finding by
   motivation, relevance, clarity, anxiety, friction, or distraction before recommending
   the fix.
4. Summarize the highest-value findings with clear reasoning.
5. Separate blockers from hypotheses, set confidence, and prioritise by evidence, user harm, and business value.
6. Define remediation/test acceptance and unassessed checks without editing the target.
7. If analytics or rendering fails, preserve observations, remove unsupported impact claims, and return the exact recovery evidence needed.

## Quality standards
- Findings must be evidence-based and ordered by impact.
- Recommendations should be specific enough to implement.
- Measured, observed, inferred, and unassessed findings remain distinguishable.
- Blockers, remediation, and experiment hypotheses have separate acceptance paths.

## Anti-patterns
- Auditing an imagined journey. Fix: require an inspectable page, state, or capture.
- Giving checklist findings equal priority. Fix: rank by evidence, harm, confidence, and value.
- Claiming causation from a heuristic. Fix: label it and propose a test.
- Editing during read-only audit. Fix: separate diagnosis from remediation authority.
- Optimising deceptive or inaccessible behaviour. Fix: block harm before experiments.
- Do not provide generic checklist output with no prioritization.
- Do not hide high-severity issues in vague language.
- Do not imply certainty when evidence is missing.
- Do not edit the audited site during the audit; separate findings from remediation authority.
- Do not recommend deceptive urgency, hidden costs, forced consent, or fabricated proof.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| `docs/cro-audit-report.md` | Product/marketing/build owners | Every finding cites page/state/evidence, classification, severity, confidence, correction, owner, and validation method. |
| Test backlog | Experimentation owner | Each hypothesis names audience, change, primary metric, guardrail, duration/stop rule, and instrumentation dependency. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Audit observation register | URL/state/device, capture or data reference, finding, confidence | Distinguishes measured, observed, inferred, and unassessed claims. |

## Capability Contract
Default to read-only browsing, repository inspection, analytics queries, and screenshots within authorised scope. Never edit, publish, launch tests, change tracking, spend, or access personal data beyond the approved minimum unless remediation is explicitly authorised.

## Degraded Mode
If analytics, browser states, device rendering, authentication, or research evidence is unavailable, audit only accessible evidence, mark each blocked check unassessed, and withhold impact estimates. An untested state is not a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Clear behavioural/business evidence | Prioritise with measured confidence | Opinion-led roadmap |
| Heuristic issue without data | Label heuristic and propose validation | False impact certainty |
| Accessibility, deception, or broken journey blocks use | Escalate before experiments | Optimising harm or failure |
| No inspectable target | Stop and request evidence | Fabricated audit |

## Worked Example
On a mobile pricing page, cite the exact viewport and state where total cost appears only after CTA activation, connect it to measured exits only if valid analytics exist, propose an upfront-cost treatment, and define completion plus refund/contact guardrails. Without analytics, call it a heuristic finding.

## References
- Use `references/evidence-led-conversion-system.md` for premium CRO, ecommerce CRO,
  checkout audits, conversion backlog creation, or any audit where analytics and
  business impact matter.

<!-- dual-compat-end -->
