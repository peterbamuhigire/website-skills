---
name: premium-website-product
description: Use when defining or qualifying a revenue-critical website as a premium commercial product, including proof, scope, investment logic, no-bid thresholds, and delivery promises; use website-builder after approval.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Premium Website Product
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Set the commercial and quality product boundary before a premium website enters delivery.

<!-- dual-compat-start -->
## Use When

- An agency must qualify a premium engagement
- scope and proof must justify price
- a brief may require paid discovery, reduced scope, or no-bid.

## Do Not Use When

- Use `website-builder` after scope approval, or `premium-ui-ux-design` for the build-coupled visual experience gate.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Business goals, buyer evidence, proof assets, budget range, constraints, and decision authority | Client discovery and agency records | yes | Test product viability | Stop or prescribe paid discovery when goals, authority, or evidence are insufficient |

## Workflow

1. Assess business outcome, audience, proof, constraints, and decision authority
2. Choose full premium, smaller premium, paid discovery, or no-bid
3. Define promises, exclusions, evidence, measurement, and acceptance
4. Stop on unsupported claims or unfinanceable scope, recover by narrowing or discovery, then hand approved scope to delivery.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Premium website product brief | Proposal and website-builder | Names outcome, audience, scope, proof, exclusions, investment logic, measures, and acceptance |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Qualification and scope decision record | Commercial owner | Links each promise to proof or labels it an assumption requiring discovery |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Planning is read-only by default. Editing the commercial brief requires authorisation; pricing commitments, spending, contracting, and publication require explicit commercial authority.

## Degraded Mode

If buyer evidence, proof, or budget authority is unavailable, return the narrowest qualified discovery or no-bid recommendation and mark viability checks `not assessed`.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Outcome, proof, authority, and viable investment align | Offer full premium scope | Overpromised delivery |
| Valuable goal but evidence is incomplete | Sell paid discovery | Unpriced uncertainty |
| Budget cannot support credible minimum scope | No-bid or smaller premium scope | Low-quality delivery |

## Quality Standards

- Every promise must have evidence, an owner, a measure, and an acceptance condition; premium language cannot compensate for weak proof.

## Anti-Patterns

- Calling every brochure site premium. Fix: tie scope to a material business outcome.
- Quoting before decision authority is known. Fix: complete qualification first.
- Inventing projected results. Fix: use verified proof or label an assumption for discovery.
- Discounting until an unsafe scope fits. Fix: reduce scope or no-bid.
- Handing vague promises to delivery. Fix: define exclusions and acceptance evidence.

## Worked Example

A client wants multilingual ecommerce on a brochure budget with no catalogue data. Recommend paid discovery or a smaller premium catalogue phase; do not promise full commerce delivery.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- Building, proposing, pricing, auditing, or positioning a website that must justify premium fees.
- The website must serve as a marketing, SEO, conversion, trust, sales-enablement, recruitment, investor, or partner-facing asset.
- The output must make the website owner look more credible while also strengthening the developer's premium reputation.
- The client or project risks treating the website as a cheap brochure, template skin, or decoration exercise.

## Preserved Domain Exclusions
- The task is a narrow implementation fix with no design, content, SEO, conversion, or positioning implication.
- The user explicitly wants commodity work and accepts that it is outside the premium website engine.

## Preserved Domain Inputs
- Business model, target buyer, offer, geography, languages, proof assets, existing analytics, and conversion goal.
- Brand assets, photos, content inventory, search topics, competitors, and technical constraints.
- Commercial context: project tier, budget, expected business outcome, launch date, and maintenance plan.

## Preserved Domain Workflow
1. Define the website's commercial job: qualified leads, sales, bookings, subscriptions, investor confidence, recruitment, authority, support reduction, or partner trust.
2. Package the website as a product: named outcome, included strategy, UX, content, SEO, analytics, QA, training, and post-launch improvement window.
3. Design the content system before page styling: search intent, buyer questions, proof burden, page goal, CTA ladder, internal links, schema, and follow-up path.
4. Apply the premium website market-asset gate to strategy, content, UI/UX, SEO, stack, launch, handover, and agency proof.
5. Route downstream: `agency-positioning` for offer/pricing, `premium-ui-ux-design` for visual/product feel, `premium-commercial-writing` for premium copy quality across pages/articles/documents/offers, `content-writing` and `sales-copywriting` for narrower copy tasks, `seo` for search/GEO, `page-builder` for implementation, and `deploy` for hard gates.
6. Reject or re-scope work that cannot support premium quality, measurable value, or credible proof.

## Preserved Domain Quality Guidance
- The first viewport states the brand/category, commercial promise, proof signal, and next action.
- Every money page has search intent, buyer objection, proof asset, CTA, schema requirement, and analytics event.
- Copy is specific enough to sell the owner's business and polished enough to advertise the developer's quality.
- The stack choice is explained in buyer language: speed, ownership, security, maintainability, SEO, integration, and cost over time.
- Premium is visible in service quality: discovery, strategy, copy, design system, QA, accessibility, performance, security, analytics, training, and improvement cadence.
- The website contains a discreet but credible developer proof trail where appropriate: footer credit, case-study eligibility, performance report, or standards page, subject to client agreement.

## Preserved Domain Anti-Patterns
- Treating content as placeholder text after design is finished.
- Selling SEO as metadata only instead of content architecture, technical crawlability, authority, and measurement.
- Using luxury visuals while the content, forms, performance, or mobile UX feel ordinary.
- Building pages that impress designers but do not help the owner win customers, investors, partners, or staff.
- Accepting low-fit, sub-premium work that would dilute the agency's published standard.

## Preserved Domain Outputs
- Premium website product brief.
- Website-as-marketing-asset strategy.
- Content, SEO, conversion, and proof requirements.
- Stack philosophy and technical approach notes.
- Premium delivery, handover, and post-launch improvement plan.
- Gate report with blockers and required fixes.

## Preserved Domain References
- `references/premium-website-market-asset-gate.md` - actionable checklist for premium website strategy, content, SEO, UX, stack, delivery, and agency proof.
- `../website-builder/references/premium-website-engine-playbook.md` - orchestration, acquisition, conversion, measurement, and asset-value system.
- `../agency-positioning/references/premium-website-offer-playbook.md` - agency offer ladder, fee floors, scope, and premium positioning.
- `../premium-ui-ux-design/references/premium-website-ui-ux-playbook.md` - premium visual and UX execution.
- `../premium-commercial-writing/SKILL.md` - use when the website's copy, blogs, SEO/GEO content, sales documents, or offer pages must justify premium fees.
