---
name: hospitality-website-product
description: Use when designing or building a world-class website for a hotel, resort, lodge, inn, guest house, restaurant, bar, venue, catering, or food-service brand.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Hospitality Website Product
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Use with `premium-website-product`, `website-builder`, `premium-ui-ux-design`,
`seo`, `google-ai-search`, accessibility, performance and experimentation skills.
The site must sell a truthful experience and make the next action easy; it is
not a substitute for a PMS, booking engine, payment provider or property proof.

<!-- dual-compat-start -->
## Use When

- A website or digital experience is for a hotel, resort, lodge, inn, guest house, restaurant, venue, catering or food-service business.

## Do Not Use When

- The task is only application engineering, visual-system governance, or a live SEO diagnosis; route to the narrower companion skill.

## Required Inputs

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Format, audience, intent, routes, verified entity facts and conversion goal | Client brief/content/evidence | Yes | Stop content/schema decisions and request the facts. |
| Approved assets, policies, rates, availability, locales, integrations and device constraints | Client/authorised systems | Conditional | Build only the qualified surface and mark unavailable checks `NOT_ASSESSED`. |

## Workflow

1. Classify guest and staff jobs and map the conversion journey.
2. Gather and date entity facts, content, assets, policies and integration boundaries.
3. Design the information architecture, visual experience and critical states.
4. Implement truthful content, schema, metadata, performance, accessibility and measurement.
5. Render, test, review, hand over and record post-launch learning; stop on unsupported claims and recover by narrowing the build when evidence is incomplete.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Hospitality website product brief/build package | Owner, designer, developer, SEO/content and operations teams | Route map, facts, states, conversion, accessibility, performance, search, measurement and handoff are explicit. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Content/schema/metadata inventory, renders, test record and measurement plan | Release owner | Each route has an oracle, owner, source/date and visible unassessed checks. |

## Capability Contract

Read/search, design, content, implementation, rendering and testing may be
required. Publishing, production analytics changes, account access and booking
integration mutation require explicit authority.

## Degraded Mode

Without facts, assets, deployment URL, renderer, device or accessibility tools,
return a qualified route/content specification and list the blocked checks.

## Decision Rules

| Condition | Action | Risk avoided |
|---|---|---|
| Entity fact and page content are verified | Use narrow accurate metadata/schema | Misleading search signals |
| Booking or reservation integration is absent | Use a truthful enquiry/human fallback | Broken conversion promise |
| Render or accessibility evidence is unavailable | Mark release `NOT_ASSESSED` | Polished but unusable site |
| A layered or parallax "journey" effect is requested | Use it only on a story page, never on booking, rates or contact pages; animate transform and opacity only behind a reduced-motion guard; ship a static version with the same content and booking action; no auto-scroll or scroll-jacking; verify the page still passes the performance gate | Motion sickness, lost bookings and slow pages on mobile data |

## Quality Standards

Task-first, truthful, accessible, fast, responsive, search-aware, conversion-
ready, measurable and maintainable.
<!-- dual-compat-end -->

## Hospitality discovery and information architecture

Start with the guest/job-to-be-done and build a task-first route map:

- stay: rooms, rates, inclusions, policies, accessibility, availability and
  booking/ enquiry;
- dine: menus, meal periods, dietary/allergen information, reservations,
  takeaway/delivery and contact;
- meet/celebrate: spaces, capacities, layouts, packages, enquiry and proof;
- experience: location, transport, nearby attractions, activities and guides;
- trust: real photography, facilities, service standards, reviews with
  attribution/permission, FAQs, terms, privacy, contact and support;
- convert: phone, WhatsApp or form only when staffed; use an actual booking or
  reservation flow when the integration and inventory are real.

Design separate journeys for a room booker, restaurant diner, event organiser,
corporate buyer, local visitor and returning guest. Mobile, low-bandwidth,
keyboard, screen-reader and human fallback paths are part of the product.

## Search, answer, generative, AI and experience optimisation

Treat the user's five-layer model as a measurement framework, not a collection
of guarantees:

- **SEO:** intent clusters, unique page titles, crawlable routes, canonicals,
  internal links, accurate local/entity facts, image text, performance and
  truthful refreshes. Backlinks are earned through useful partnerships and
  citations; domain authority is not a deliverable promise.
- **AEO:** answer the real question near the relevant heading, use concise
  summaries when useful, and visible FAQs where guests ask the questions. Google
  no longer shows FAQ (since 7 May 2026) or HowTo rich results; add that markup
  only for a documented non-Google consumer. “40–60 words” is
  a copy experiment, not a universal featured-snippet rule.
- **GEO:** make pages easy to quote accurately: named entity, location, dates,
  facilities, policies, prices/availability only when current, source/proof,
  tables and clear FAQs. Measure referral and answer-surface visibility where
  data exists; never promise citation in ChatGPT, Perplexity, Gemini or any
  other system.
- **AIO:** do not promise inclusion in training data or long-term model recall.
  Optimise controllable surfaces: indexability, factual consistency, public
  first-party pages, legitimate third-party profiles, update ownership, and
  explicit crawler/privacy choices. Wikipedia, Wikidata, GitHub or forums are
  used only when appropriate and editorially legitimate; no synthetic mentions
  or reputation manipulation.
- **SXO:** align intent, page speed, mobile clarity, trust, accessibility,
  availability, policies, CTA, confirmation and post-click support. Test
  qualified bookings/enquiries, completion, error rate and guest quality, not
  clicks alone.

## Truthful hospitality schema and content

Use the narrowest accurate schema for the page and verify required properties.
Possible entities include a verified `Hotel`, `Restaurant`, `FoodEstablishment`,
`Event`, `LocalBusiness`, `Offer`, `FAQPage`, `Menu` or `BreadcrumbList` where
the content actually exists. Never invent ratings, amenities, prices, reviews,
opening times, awards, room counts, availability, distances or reservation
links. Record source, last verified date, owner and expiry for volatile facts.

## Conversion and trust gates

- Show rates, taxes/fees, deposit, cancellation, arrival, accessibility and
  contact expectations before commitment.
- Keep booking, restaurant reservation and event enquiry paths distinct unless
  the integration reconciles identity, capacity, payment and confirmation.
- Provide confirmation, failure recovery, human support and an audit trail for
  enquiries or transactions; do not collect raw card data in the site.
- Use real, consented media and reviews. Never generate fake guest experience,
  review, urgency or scarcity claims.

## Acceptance evidence

For each route capture: intent, verified facts, metadata/schema inventory,
rendered mobile/desktop/keyboard checks, performance evidence, accessibility
findings, conversion event definition, analytics/referral source, owner and
retest date. Search eligibility, ranking, AI citation and conversion lift are
`NOT_ASSESSED` until measured in the real property context.

## References

- `../premium-website-product/SKILL.md`
- `../website-builder/SKILL.md`
- `../../seo-search/seo/SKILL.md`
- `../../seo-search/google-ai-search/SKILL.md`
- `C:\wamp64\www\chwezi-dev-engine\docs\source-registers\hospitality-currentness-2026-09.json`

## Anti-patterns

- A beautiful hero with no room, dining, event or contact task path. Fix: make
  the primary job visible above the fold and throughout the journey.
- Schema or review stars without verified visible evidence. Fix: omit the property.
- “AI-ready” claims based on `llms.txt`, training-data inclusion or model memory.
  Fix: document only controllable crawl, content and measurement actions.
- One funnel for booking, table reservations and event enquiries. Fix: separate
  the states and confirmations unless a real contract joins them.
- Desktop-only, photo-heavy pages that fail on low bandwidth. Fix: test the
  cheapest realistic device and provide text, compression and human fallback.

## Worked example

For a lodge, create a room page that shows verified capacity, inclusions,
policies, location and a real enquiry/booking path; add concise FAQ content and
accurate entity markup; test keyboard/mobile/error states; then measure
qualified enquiries and response fulfilment rather than promising rankings.
