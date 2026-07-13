---
name: ecommerce-checkout
description: Use when specifying or auditing cart, checkout, payment recovery, order confirmation, and post-purchase experience; do not use for overall ecommerce strategy, acquisition lifecycle, or KPI architecture.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Ecommerce Checkout
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- Cart-to-order completion needs flow, form, validation, total-cost, payment, recovery, confirmation, or post-purchase specification.
- An existing checkout needs a safe evidence-based audit across guest/account paths, devices, payment outcomes, and error states.

## Do not use when
- The request is general store strategy; use `ecommerce`.
- The request is acquisition/lifecycle messaging or measurement architecture; use `ecommerce-funnel` or `ecommerce-analytics`.
- No inspectable flow or approved policy rules exist; request them before detailed checkout commitments.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Checkout routes/states, basket rules, payment methods, geography, and devices | Store/repository brief | yes | Stop detailed recommendations and request the flow. |
| Shipping, tax, discount, returns, privacy, and support rules | Operations/legal owners | yes | Do not invent policy or total-cost behaviour. |
| Error evidence and funnel data | Analytics/support/testing | conditional | Give heuristic findings only and label impact unmeasured. |

## Workflow
1. Confirm the basket, identity, address, delivery, tax, discount, payment, consent, confirmation, and support rules; stop on policy conflicts.
2. Map guest/account paths and every applicable loading, validation, price/stock change, payment, retry, and confirmation state.
3. Inspect or test the flow with safe test data across agreed devices and payment methods.
4. Classify issues by evidence, harm, friction, confidence, and implementation dependency.
5. Specify corrections and scenario acceptance tests without changing production.
6. If a transaction or test environment fails, stop attempts, preserve identifiers/evidence, avoid duplicate submission, and escalate to the named owner.

## Quality standards
- The specification covers guest/account, device, validation, totals, price/stock changes, payment outcomes, retry, and confirmation.
- Recommendations cite an inspected state or are labelled heuristic, with no fabricated impact estimate.
- Consent, total cost, recovery, support, and accessibility remain visible throughout the flow.

## Anti-patterns
- Testing with real payment credentials. Fix: use an authorised sandbox and test instruments.
- Hiding total cost until submission. Fix: disclose and reconfirm every material change.
- Retrying uncertain payments blindly. Fix: use idempotency and a recoverable pending state.
- Designing only successful payment. Fix: cover decline, timeout, duplicate, and lost-confirmation states.
- Claiming impact from heuristics. Fix: label confidence and define measurement.
- Do not produce generic framework dumps with no decision made.
- Do not invent facts to complete the output.
- Do not ignore the actual audience, offer, or business constraints.
- Do not force account creation where guest checkout is feasible and approved.
- Do not hide total cost, preselect consent, or use deceptive urgency.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Checkout flow/state specification | Design and engineering | Covers guest/account paths, totals, validation, payment outcomes, recovery, confirmation, and support escalation. |
| Prioritised checkout findings | Product owner | Every finding cites a state/evidence item and a testable correction. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Checkout scenario matrix | Device, path, expected/actual, severity | Includes payment failure, timeout, duplicate submission, stock/price change, and confirmation loss. |

## Capability Contract
Audit checkout read-only by default and use test environments/test credentials only. Production transactions, refunds, payment-provider changes, customer contact, publishing, and spend require explicit authority.

## Degraded Mode
When a safe test environment, payment method, device coverage, or analytics is unavailable, inspect accessible states and mark blocked scenarios not assessed. Never place a real order.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Required data can be deferred | Move it after purchase or omit it | Form abandonment |
| Payment outcome is uncertain | Preserve basket/idempotency and show recovery | Duplicate or lost orders |
| Total changes before payment | Reconfirm clearly before submission | Surprise charges |
| Finding lacks behavioural data | Mark heuristic and propose a test | False impact claims |

## Worked Example
Test a mobile guest checkout where delivery cost appears after address entry, payment times out, and the buyer retries. Require stable basket totals, idempotent submission, a clear pending state, and a recoverable confirmation path without creating duplicate orders.

## References
- Use sibling reference `../ecommerce/references/premium-ecommerce-growth-system.md`
  when checkout recommendations must connect to product-page clarity, cart trust,
  abandoned-cart recovery, retention, or ecommerce measurement.

<!-- dual-compat-end -->
