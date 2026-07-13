---
name: ecommerce-funnel
description: Use when designing ecommerce acquisition, retargeting, lifecycle messaging, offers, upsells, retention, and repeat-purchase journeys; do not use for checkout mechanics or measurement architecture alone.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Ecommerce Funnel
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- Acquisition, retargeting, abandoned-cart, onboarding, repeat-purchase, win-back, upsell, or loyalty journeys need an owned lifecycle map.
- Segments, triggers, consent, offers, timing, suppression, experiments, and economics must be designed as one system.

## Do not use when
- The task is catalogue/store model strategy or checkout state design; use `ecommerce` or `ecommerce-checkout`.
- The task is event/KPI/dashboard architecture without lifecycle decisions; use `ecommerce-analytics`.
- Consent, suppression, economics, or fulfilment capacity is unknown; stop before activation.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Segments, buying cycle, products, margins, channels, and lifecycle objective | Business/commerce brief | yes | Stop offer sequencing and request economics and audience evidence. |
| Consent, contact rules, suppression, returns, and fulfilment limits | CRM/legal/operations | yes | Produce no send-ready campaign. |
| Baseline funnel and cohort evidence | Analytics | conditional | Frame journey as a hypothesis, not an optimisation result. |

## Workflow
1. Confirm segments, lifecycle objective, economics, consent, suppression, channels, fulfilment, and baseline; stop on unsafe activation gaps.
2. Map current journey and evidence-backed drop-offs before selecting offers or messages.
3. Decide triggers, timing, channel, content, offer, exits, frequency, and owner for each stage.
4. Define instrumentation, primary metrics, margin/service guardrails, and experiment stop conditions.
5. Review privacy, brand, stock, support, and operational capacity before handoff.
6. If activation evidence or systems fail, keep the plan in draft, suppress affected audiences, and return the recovery owner/test.

## Quality standards
- Each journey names segment, evidence, trigger, channel, timing, exit, suppression, owner, metric, and guardrail.
- Offers respect verified margin, stock, fulfilment, brand, consent, and support capacity.
- Optimisation claims distinguish measured incrementality from correlation and hypothesis.

## Anti-patterns
- Activating an inferred segment. Fix: validate segment evidence and eligibility first.
- Sending without consent or suppression. Fix: block activation until both are enforced.
- Discounting without margin or capacity checks. Fix: set economic and service guardrails.
- Measuring opens as business success. Fix: use incremental purchase and guardrail outcomes.
- Running journeys without exits. Fix: define conversion, recency, frequency, and unsubscribe exits.
- Do not produce generic framework dumps with no decision made.
- Do not invent facts to complete the output.
- Do not ignore the actual audience, offer, or business constraints.
- Do not send without consent or omit suppression, frequency, and unsubscribe controls.
- Do not use discounts that conflict with margin, stock, brand, or fulfilment limits.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Funnel/lifecycle map | Marketing, CRM, ecommerce, analytics | Names segment, trigger, message/offer, channel, timing, exit, suppression, metric, and owner at each stage. |
| Experiment backlog | Growth owner | Each item has hypothesis, audience, primary metric, guardrail, and stop condition. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Journey assumption register | Evidence, assumption, risk, validation step | Unsupported segment or lift claims are explicitly qualified. |

## Capability Contract
Planning and review are read-only by default. Creating or sending campaigns, changing audiences or offers, using customer data, publishing, or spending requires explicit authority and consent controls.

## Degraded Mode
When CRM access, analytics, consent evidence, or verified economics is unavailable, deliver a qualified lifecycle map and mark activation not assessed. Do not provide send-ready lists.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Segment has distinct need/evidence | Tailor journey and measurement | Generic blasting |
| Consent or suppression is uncertain | Block activation | Privacy harm |
| Offer erodes margin or service capacity | Redesign or reject it | Unprofitable growth |
| Baseline is missing | Run a measurement-first test | Unsupported lift claim |

## Worked Example
For replenishable skincare, separate first-time education from repeat-purchase timing, suppress recent purchasers from abandoned-cart messages, cap frequency, and measure incremental repeat purchase with margin and unsubscribe guardrails rather than reporting opens as success.

## References
- Use sibling reference `../ecommerce/references/premium-ecommerce-growth-system.md`
  when planning traffic-to-retargeting paths, lifecycle journeys, abandoned-cart
  recovery, repeat purchase, or ecommerce growth metrics.

<!-- dual-compat-end -->
