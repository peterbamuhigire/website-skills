# Local Search and Entity Presence Audit

Parent skill: [`../SKILL.md`](../SKILL.md)

Audit whether a real organisation or location is consistently, accurately, and
usefully represented for local discovery. Do not rely on universal voice-search
statistics, review-response deadlines, post quotas, or “near me” formulas.

## Scope

Record the business model, eligible locations or service areas, markets,
languages, customer tasks, business-profile owners, website routes, feeds,
directories, and conversion outcomes. Separate storefronts, offices, service
areas, franchises, practitioners, and online-only operations.

## Website evidence

- [ ] Name, address or service area, phone, hours, categories, products/services,
      and contact routes are verified and internally consistent.
- [ ] Each location page represents a genuine location or materially distinct
      local service, not a doorway-page variant.
- [ ] Local pages provide useful evidence such as access instructions, service
      scope, staff, facilities, local pricing or process, support, and limitations.
- [ ] Titles, headings, copy, links, canonical, hreflang, and metadata describe
      the location naturally without geographic stuffing.
- [ ] Maps, directions, forms, calls, bookings, and messages work accessibly on
      relevant mobile and desktop contexts.
- [ ] Location changes, temporary closures, and relocations have redirect,
      profile, schema, citation, and customer-notification plans.

## Business profiles and directories

- [ ] Google Business Profile, Bing Places, merchant/product surfaces, and
      relevant directories represent the same verified entity.
- [ ] Organisation ownership and least-privilege access are documented.
- [ ] Categories, hours, contacts, service areas, products, and media are current.
- [ ] Feature availability and eligibility are verified for the target market.
- [ ] Duplicate, practitioner, department, virtual-office, and closed listings
      have an intentional policy.
- [ ] Reviews are solicited and answered according to current platform policy,
      privacy, consent, capacity, and service-recovery needs—never fabricated,
      gated, or incentivised deceptively.

## Structured data

Use `LocalBusiness` or the narrowest valid subtype only when a genuine local
entity exists. Mark up facts visible on the page and supported by the project:
stable entity ID, name, URL, verified address or service area, contact, hours,
geo where accurate, and legitimate profile references. Omit unsupported ratings,
prices, areas, credentials, or locations.

Schema.org validity does not guarantee a Google feature. Validate vocabulary,
rendered fact parity, and current consumer eligibility separately.

## Local authority and corroboration

Assess legitimate sector associations, partners, public records, local media,
events, community work, and customer-approved case evidence for relevance and
source quality. Do not equate directory quantity with authority or create
inauthentic mentions.

## Search and AI measurement

- analyse local queries, pages, countries, devices, calls, directions, bookings,
  messages, and qualified outcomes using the property's own baseline;
- review Google generative AI impressions and Bing AI citation activity where
  available without calling them local ranking scores;
- test representative conversational prompts only as repeated observations,
  recording market, locale, platform, date, citations, factual support, and
  errors;
- distinguish visibility, representation accuracy, referral, task completion,
  and business outcome.

## Finding priorities

1. harmful wrong facts, impersonation, closure, or safety information;
2. ownership loss, duplicate entities, and conflicting locations;
3. broken booking/contact/accessibility or index controls;
4. page-profile-feed-schema inconsistency;
5. weak local usefulness or evidence;
6. measurement and maintenance gaps.

Every finding names evidence, owner, impact, confidence, correction, platform
dependency, acceptance check, and retest date. Missing account or live-profile
access is `NOT_ASSESSED`.

## Currentness

Verify all platform capabilities and policies against first-party sources on the
day of work. Use the shared claim register at
[`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json)
for search/AI rules; add a project register for local-platform and jurisdictional
facts.
