---
name: retail-commerce-operating-system
description: Use when building or specifying a retail website, e-commerce site, omnichannel storefront, product catalogue, customer portal, or commerce frontend that must integrate product data, search/navigation, PDP content, cart/checkout, fulfilment, returns, loyalty/CRM, analytics, POS/inventory, and finance/control evidence.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Retail Commerce Operating System
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- A website or web app sells retail products, supports store pickup, exposes inventory, handles returns, captures loyalty/CRM events, or integrates with POS, inventory, ERP, WMS, payment, or fulfilment systems.
- The brief includes omnichannel, retail transformation, merchandising, product data, search/navigation, PDP, checkout, fulfilment, returns, loyalty, CRM, promotions, markdowns, vendor/private label, store locator, or retail dashboards.
- The project needs implementation-facing requirements for retail software rather than only conversion copy or a catalogue page.

## Do Not Use When

- The site is only a brochure for a retailer and has no product, commerce, account, order, fulfilment, returns, or analytics scope.
- The task is only checkout copy or a funnel strategy; use `ecommerce`, `ecommerce-checkout`, `ecommerce-funnel`, or `ecommerce-analytics` as the narrower skill.
- The project requires accounting treatment, tax, inventory valuation, or reconciliation promises without routing to the finance doctrine engine.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Business model, channels, categories, geography, store/warehouse/fulfilment model | Discovery/business artefacts | yes | Stop architecture decisions and return the missing operating choices. |
| Systems of record for product, price, inventory, order, customer, payment, loyalty, analytics, and finance | Technical/operations owners | yes | Produce an integration discovery map only. |
| Fulfilment, pickup, return, support, promotion, consent, and privacy rules | Policy owners | yes | Do not invent customer promises or eligibility logic. |
| Approved SRS and acceptance criteria | SRS engine or project | conditional | Produce capability requirements, not implementation commitments. |

## Workflow
1. Confirm the retail decision, scope boundary, owners, and source artefacts; stop if customer promises or systems of record are unknown.
2. Complete the Retail Build Diagnostic and mark every unknown rather than inferring it.
3. Select only the required scope modules and define source-of-truth, events, exceptions, and finance/control handoffs for each.
4. Decide whether the output is a discovery map, SRS input, implementation plan, or audit; keep audit work read-only unless remediation is authorised.
5. Validate catalogue, search, PDP, pricing, cart, fulfilment, returns, loyalty, store, and measurement dependencies end to end.
6. Recovery: on tool or integration failure, preserve evidence, repair the failed boundary, and rerun the narrowest safe test.

## Retail Build Diagnostic

Before design or implementation, answer:

1. What is the system of record for product, category, price, inventory, order, customer, and finance data?
2. Which channels must share the same customer promise: store, web, app, marketplace, social commerce, call centre?
3. What must the website show about availability, delivery, pickup, returns, warranty, total cost, and customer support?
4. Which product attributes drive search, filters, comparison, recommendations, and SEO?
5. Which promotions, coupons, loyalty rewards, bundles, markdowns, or price zones must the frontend respect?
6. Which events must feed analytics, CRM, advertising, fulfilment, inventory, accounting, and weekly review dashboards?
7. Which failure states matter: out of stock, payment failure, pickup unavailable, delivery delay, return rejected, stale price, stale inventory?
8. Which finance/control handoffs exist for refunds, discounts, markdowns, gift cards, loyalty, vendor funding, POS settlement, or stock movement?

## Scope Modules

| Module | Website/web-dev requirements |
|---|---|
| Product data and taxonomy | Required attributes, category tree, variant model, media rules, alt text, SEO fields, channel publication rules. |
| Search and navigation | Synonyms, filters, facets, sort options, zero-result recovery, relevance testing, product-card comparison fields. |
| Product detail page | Decision-quality media, specs, benefits, availability, delivery/pickup promise, return policy, reviews/proof, related products, event tracking. |
| Pricing and promotions | Price source, effective dates, price-zone logic, offer eligibility, coupon handling, bundle rules, markdown display, stack prevention. |
| Cart and checkout | Guest checkout, address validation, shipping/pickup selection, payment methods, error recovery, order preview, consent, performance budget. |
| Fulfilment | Available-to-promise, reservation, delivery/pickup slots, order-line status, substitution, partial fulfilment, customer notifications. |
| Returns | Return initiation, eligibility, reason capture, inspection status, exchange/refund, reverse logistics, support escalation. |
| Loyalty and CRM | Consent, enrollment, identity, tier/points/reward display, lifecycle events, suppression preferences, customer segments. |
| Store experience | Store locator, inventory by store, opening hours, service availability, click-and-collect instructions, local trust signals. |
| Analytics and WBR | Event taxonomy, dashboard metrics, source lineage, refresh cadence, experiment backlog, weekly action log. |

## Event Taxonomy Minimum

Track these events when the matching module exists:

- `product_viewed`, `product_media_used`, `product_attribute_selected`
- `search_submitted`, `search_zero_results`, `filter_applied`, `sort_changed`
- `category_viewed`, `product_list_clicked`, `recommendation_clicked`
- `cart_item_added`, `cart_item_removed`, `cart_quantity_changed`
- `checkout_started`, `checkout_step_completed`, `payment_failed`, `order_placed`
- `pickup_selected`, `delivery_selected`, `fulfilment_exception_seen`
- `return_started`, `return_reason_selected`, `refund_requested`
- `loyalty_enrolled`, `reward_viewed`, `reward_redeemed`
- `promotion_viewed`, `coupon_applied`, `coupon_rejected`

Each event must define payload, trigger, deduplication key, consent basis, destination systems, and reporting use.

## Acceptance Standards

A retail commerce build is not complete until:

- Product publication blocks incomplete SKU, category, price, media, fulfilment, return, and accessibility fields.
- Search and navigation have test queries, zero-result recovery, and attribute governance.
- PDPs answer availability, delivery/pickup, returns, warranty/support, proof, total cost, and next action.
- Cart and checkout preserve price/inventory validation immediately before payment or order placement.
- Fulfilment and returns workflows expose customer status and operational exception paths.
- Promotions and coupons respect effective dates, eligibility, and offer-stack rules.
- Analytics events cover discovery, PDP, cart, checkout, fulfilment, returns, loyalty, and campaign performance.
- Dashboards expose stale-data warnings and source lineage for financial or operational KPIs.
- Performance, accessibility, privacy, and security gates pass under the repository's canonical CI pipeline.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Retail capability and integration specification | SRS, architecture, build, and operations teams | Every in-scope module names owner, source, contract, event, exception, customer state, and acceptance test. |
| Retail readiness/audit record | Project owner | Findings cite inspected evidence, severity, owner, and verification step. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| System-of-record and event lineage register | Entity/event, source, destination, consent/control, test | Covers every in-scope customer promise and control handoff. |
| Scenario test matrix | Scenario, expected/actual, owner, status | Includes stale price/inventory, payment failure, partial fulfilment, pickup failure, and return rejection where applicable. |

## Capability Contract
Discovery, specification, and audit default to read-only. Editing integrations, catalogue, inventory, price, promotions, orders, customer data, loyalty, payments, or finance records requires explicit authority. Publishing, production mutation, refunds, destructive actions, spending, and compliance/certification claims require separate approval and evidence.

## Degraded Mode
When systems, test accounts, network, data, devices, or policy evidence are unavailable, return the capability map and unassessed-boundary register. Never convert an inaccessible integration, control, or customer journey into a pass or promise live readiness.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| One system owns an entity | Record it and define downstream freshness/error behaviour | Conflicting truth |
| Customer promise lacks operational owner | Stop that feature commitment | Undeliverable promise |
| Scope includes accounting/tax/valuation | Route doctrine and SRS inputs before commitment | Unsupported finance claim |
| Inventory or price can become stale | Define timestamp, revalidation, and recovery | Oversell or wrong price |
| Narrow checkout/funnel/analytics task | Route to the sibling skill | Over-scoped operating-system work |

## Quality Standards
- Customer-facing availability, price, fulfilment, return, and loyalty states trace to named systems and owners.
- Every integration covers timeout, stale data, duplicates, partial success, retry, and support escalation where relevant.
- Event payloads define consent, deduplication, destination, and reporting use.
- Financial, tax, reconciliation, and compliance statements remain doctrine-owned and evidence-backed.
- Unknown and untested boundaries remain visible at release.

## Anti-Patterns
- Treating the website as the product-data master. Fix: name and integrate the actual system of record.
- Displaying stock without freshness or reservation behaviour. Fix: timestamp, revalidate, and define failure recovery.
- Promising pickup or delivery without capacity and exception ownership. Fix: bind the promise to operational rules and escalation.
- Designing only the happy path. Fix: test stale price, payment failure, partial fulfilment, rejected return, and delayed refund states.
- Claiming finance, tax, or audit readiness from frontend events. Fix: route to the finance doctrine and reconcile evidence.
- Activating loyalty or marketing events without consent and suppression rules. Fix: document lawful basis, preferences, and destinations.

## Worked Example
A click-and-collect build maps product data to PIM, store stock to inventory, reservation to OMS, payment to the gateway, and refund evidence to finance. It revalidates price and stock before order placement, exposes pickup failure recovery, emits deduplicated events, and leaves tax treatment to the finance doctrine.

## Finance and Control Route

If the web build touches refunds, discounts, markdowns, loyalty liabilities, gift cards, vendor-funded offers, inventory valuation, POS settlement, or management reporting, route to:

- SRS engine retail domain pack for software requirements.
- Finance doctrine engine `retail-and-pos-accounting-pack`.
- `ecommerce-analytics` for event/dashboard design.

Do not promise accounting, tax, reconciliation, or audit outcomes from this website skill alone.

## Companion Skills

- `skills/commerce/ecommerce/SKILL.md` for general e-commerce strategy.
- `skills/commerce/ecommerce-checkout/SKILL.md` for checkout and post-purchase detail.
- `skills/commerce/ecommerce-funnel/SKILL.md` for acquisition, lifecycle, and retention.
- `skills/commerce/ecommerce-analytics/SKILL.md` for measurement and dashboards.
- `skills/orchestration/premium-website-product/SKILL.md` for premium business-asset framing.
- `skills/launch-ops/observability/SKILL.md` for live telemetry.
- `skills/launch-ops/experimentation/SKILL.md` for tests and optimisation cadence.

## Evidence Basis

This skill is based on the internal digital-research-engine project `umbrex-retail-playbooks-engine-enhancement`, extracted on 2026-06-25 from public Umbrex retail playbook pages. Use it as a retail website completeness taxonomy, not as proof of client facts, market statistics, or accounting/legal treatment.

## References
- [`../ecommerce/SKILL.md`](../ecommerce/SKILL.md) for general store strategy and business-model framing.
- [`../ecommerce-checkout/SKILL.md`](../ecommerce-checkout/SKILL.md) for checkout and post-purchase detail.
- [`../ecommerce-funnel/SKILL.md`](../ecommerce-funnel/SKILL.md) for acquisition and lifecycle journeys.
- [`../ecommerce-analytics/SKILL.md`](../ecommerce-analytics/SKILL.md) for events, KPIs, reconciliation, and dashboards.
<!-- dual-compat-end -->
