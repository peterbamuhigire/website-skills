---
name: ecommerce-analytics
description: Use when defining or auditing ecommerce events, KPIs, funnels, cohorts, RFM, attribution, CLV, and dashboards; do not use for general store strategy or checkout-interface design.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Ecommerce Analytics
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- Ecommerce decisions need event instrumentation, KPI definitions, funnel/drop-off analysis, cohorts, RFM, CLV, attribution, or a decision-facing dashboard.
- Order/revenue evidence must be reconciled across analytics and commerce systems before optimisation claims are used.

## Do not use when
- The request is overall store/business-model strategy; use `ecommerce`.
- The request is checkout-interface or lifecycle-message design; use `ecommerce-checkout` or `ecommerce-funnel`.
- No decision, metric definition, schema, or data evidence exists; define them before reporting results.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Decisions, KPI definitions, targets, and reporting audience | Business/measurement brief | yes | Stop dashboard design and request decision ownership. |
| Event schema, data sources, identity, consent, and revenue rules | Analytics/commerce systems | yes | Produce a measurement gap map, not calculated metrics. |
| Extracts or connected data with date range and timezone | Data provider | conditional | Define formulas and QA tests only; do not invent results. |

## Workflow
1. Confirm the decisions, metric definitions, owners, date range, timezone, grain, consent, and source systems; stop on material ambiguity.
2. Map the funnel and event schema, including triggers, payloads, identity, deduplication, and destinations.
3. Validate data quality, reconcile revenue/orders, and record exclusions before calculating KPIs.
4. Choose cohort, RFM, CLV, attribution, or drop-off methods only when their assumptions fit the question.
5. Produce the plan, dashboard, or analysis with caveats and action thresholds.
6. If a source or reconciliation fails, preserve definitions and queries, withhold affected results, and return the owner/test needed for recovery.

## Quality standards
- Metrics expose formula, source, grain, timezone, owner, target, exclusions, and caveats.
- Event specifications cover identity, consent, deduplication, destinations, and QA.
- Revenue/order reporting reconciles to named commerce records or remains explicitly unassessed.

## Anti-patterns
- Reporting undefined conversion or revenue. Fix: state formula, source, grain, and exclusions.
- Counting thank-you views as orders. Fix: deduplicate against confirmed order identifiers.
- Mixing timezones or currencies. Fix: normalize and disclose transformation rules.
- Treating attribution as causation. Fix: label limitations and use experiments for causal claims.
- Hiding source disagreement. Fix: reconcile it or expose the variance and owner.
- Do not produce generic framework dumps with no decision made.
- Do not invent facts to complete the output.
- Do not ignore the actual audience, offer, or business constraints.
- Do not mix gross/net revenue, orders, users, sessions, or timezones without explicit definitions.
- Do not treat attribution as causal proof.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Measurement plan/event specification | Developers and analysts | Each event has trigger, payload, identity, consent, deduplication, destination, and QA rule. |
| KPI/dashboard specification or analysis | Operators and decision-makers | Every metric has formula, source, grain, cadence, owner, target, and caveat. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Data-quality and reconciliation record | Checks, expected/actual, exceptions | Unresolved discrepancies and unassessed sources remain visible. |

## Capability Contract
Default to read-only analysis. Query or export only authorised data and minimise personal data. Instrumentation edits, dashboard publication, advertising changes, and production writes require explicit authority.

## Degraded Mode
If data, identity resolution, consent evidence, or query capability is unavailable, deliver definitions, schemas, and validation queries only. Mark every uncomputed KPI and untested event unassessed.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| KPI drives a named decision | Include with owner and threshold | Vanity reporting |
| Event cannot be deduplicated | Fix identity/key before release | Inflated conversion |
| Sources disagree | Reconcile and expose variance | False precision |
| Attribution is observational | Label limitations and avoid causal language | Misallocated spend |

## Worked Example
Define `order_placed` from a confirmed order identifier rather than a thank-you page view, reconcile event revenue to the order system by day and currency, and report checkout completion with bot/internal traffic exclusions. If reconciliation is unavailable, mark revenue unassessed.

## References
- Use sibling reference `../ecommerce/references/premium-ecommerce-growth-system.md`
  when defining ecommerce funnel events, channel segmentation, abandoned-cart metrics,
  checkout completion, repeat purchase, or revenue optimization dashboards.

<!-- dual-compat-end -->
