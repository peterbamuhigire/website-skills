---
name: ecommerce
description: Use when defining the overall model, experience, trust, product-decision, and growth strategy for an online store; do not use for deep checkout, lifecycle, analytics, or omnichannel operating-system work.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Ecommerce
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- A new or existing online store needs its business model, product-decision experience, customer promise, trust proof, and growth handoffs defined together.
- Product/category experience or channel strategy needs a store-wide decision before narrower checkout, funnel, analytics, or retail-system work.

## Do not use when
- The issue is limited to checkout/payment recovery; use `ecommerce-checkout`.
- The issue is acquisition/lifecycle orchestration or KPI/event design; use `ecommerce-funnel` or `ecommerce-analytics`.
- Omnichannel systems, POS, inventory, fulfilment, or finance controls dominate; use `retail-commerce-operating-system`.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Business model, offer, customer, geography, and channel mix | Discovery/business brief | yes | Stop model selection and list the missing decisions. |
| Catalogue, pricing, fulfilment, returns, payments, and support reality | Operations/client evidence | yes | Produce only a qualified discovery checklist. |
| Current store and performance evidence | Repository, URL, or analytics | conditional | Do not claim optimisation impact or current defects. |

## Workflow
1. Read the current business context and the concrete task to solve.
2. Identify the business model and channel reality before recommending page or funnel patterns.
3. Treat the store as a traffic, product-decision, checkout, retention, and measurement
   system before recommending isolated page changes.
4. Use only the relevant detailed guidance and references for the request at hand.
5. Decide the customer promise, trust/proof, product-decision flow, and owned handoffs; stop if operations cannot support them.
6. Produce the strategy with sources, assumptions, exclusions, owners, and acceptance conditions.
7. Validate fit with checkout, funnel, analytics, fulfilment, policy, and implementation owners.
8. Recovery: if evidence fails, remove the unsupported tactic, preserve verified decisions, and rerun the missing validation step.

## Quality standards
- Outputs distinguish client facts, framework recommendations, assumptions, and validation needs.
- Recommendations must match the business model, traffic source, and fulfilment reality.

## Anti-patterns
- Choosing a channel before testing the model. Fix: decide from control, customer, economics, and operations.
- Copying marketplace tactics into an owned store. Fix: validate fit with audience and fulfilment.
- Using fabricated proof or urgency. Fix: publish only verified claims and real constraints.
- Treating a product page as the whole system. Fix: connect acquisition, decision, checkout, retention, and measurement.
- Promising uplift without a baseline. Fix: state a hypothesis and measurement plan.
- Do not produce generic framework dumps with no decision made.
- Do not import Amazon-specific tactics into a standalone ecommerce site without checking fit.
- Do not invent facts to complete the output.
- Do not ignore the actual audience, offer, or business constraints.
- Do not recommend scarcity, reviews, or guarantees without truthful evidence and policy support.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Ecommerce strategy and experience brief | Checkout, funnel, analytics, design, and build skills | States the model, customer decisions, trust proof, fulfilment promise, risks, and owned handoffs. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Assumption and source register | Claim, source, confidence, validation owner | Client facts and framework recommendations are distinguishable. |

## Capability Contract
Default to read-only analysis and planning. Edit store configuration, prices, catalogue, campaigns, or customer data only with explicit implementation authority; publishing, spending, payment changes, and destructive actions require separate approval.

## Degraded Mode
When store access, analytics, operations evidence, or network capability is unavailable, return a qualified model brief and mark affected checks not assessed. Do not claim revenue lift or readiness.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Owned store fits control and retention needs | Define owned-store experience and acquisition path | Channel/model mismatch |
| Omnichannel integrations dominate scope | Route to `retail-commerce-operating-system` | Under-specified operations |
| Checkout is the isolated problem | Route to `ecommerce-checkout` | Diluted diagnosis |
| Evidence cannot support a tactic | Qualify or reject it | Invented commercial certainty |

## Worked Example
For a local furniture retailer with delivery constraints, document an owned-store model, decision-quality product pages, delivery-zone disclosure, verified trust proof, and the handoffs to checkout and analytics. Do not transplant marketplace urgency patterns or promise conversion lift without baseline data.

## References
- Use `references/business-model-selection.md` when the task depends on marketplace vs owned-store tradeoffs, fulfilment posture, or retention model.
- Use `references/acquisition-and-retargeting.md` when traffic, retargeting, or remarketing paths materially affect the recommendation.
- Use `references/premium-ecommerce-growth-system.md` when designing, auditing, or
  improving ecommerce product pages, category pages, cart, checkout, retention, or
  revenue measurement for a premium client.
- Use sibling skill `../retail-commerce-operating-system/SKILL.md` when the site must integrate product data, inventory, POS, fulfilment, returns, loyalty/CRM, promotions, markdowns, store pickup, retail dashboards, or finance/control handoffs.

<!-- dual-compat-end -->
