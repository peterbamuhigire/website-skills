---
name: website-experience-mapping
description: Use when mapping journeys, moments of truth, mental models, service interactions, or ecosystem dependencies before premium page architecture; use page-builder after the behaviour and evidence map is approved.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Website Experience Mapping
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Translate outside-in customer behaviour into an actionable website experience map before page decisions harden.

<!-- dual-compat-start -->
## Use When

- A premium build must change behaviour
- multiple audiences or channels interact
- page requirements need evidence from the customer journey.

## Do Not Use When

- Use `page-builder` for approved screens or `service-blueprint-website-delivery` for the agency's backstage delivery operations.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Audience evidence, jobs, journey observations, service channels, business goals, and known constraints | Discovery, research, analytics, and client workshops | yes | Ground the map in observed behaviour | Stop and request research when critical stages rest only on assumptions |

## Workflow

1. Define actor, outcome, scope, evidence quality, and map type
2. Map stages, questions, emotions, channels, failures, and moments of truth
3. Connect each website intervention to behaviour and operational ownership
4. Stop on unsupported critical assumptions, recover through research or explicit hypothesis labelling, then hand approved requirements to page architecture.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Website experience map and intervention brief | Content, design-system, and page-builder | Each priority moment links evidence, user need, website response, owner, and success signal |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source register and assumption log | Product and delivery owners | Distinguishes observed evidence, inference, and untested hypothesis |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Planning is read-only by default. Workshop notes may be edited when authorised; contacting participants, recording sessions, publishing maps, or spending requires explicit authority.

## Degraded Mode

Without research, analytics, or workshop access, return the narrowest qualified hypothesis map, label every unsupported stage, and mark behavioural validation `not assessed`.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence shows a sequential goal | Use a journey map | Page list detached from behaviour |
| Frontstage and backstage failure interact | Hand off to service blueprint | Unowned operational failure |

## Quality Standards

- Map an explicit actor and outcome; separate evidence from assumptions; every intervention needs an owner and observable success signal.

## Anti-Patterns

- Drawing a journey from internal opinions. Fix: cite research or label a hypothesis.
- Mapping every possible audience together. Fix: choose one actor and goal per primary map.
- Turning the map into a page inventory. Fix: preserve behaviour, questions, and failure moments.
- Ignoring offline and support channels. Fix: map the ecosystem around the website.
- Proceeding with a critical unknown. Fix: stop for research or narrow the decision.

## Worked Example

Analytics shows mobile visitors abandon at fee questions. Map that moment, cite the event evidence, assign transparent pricing content, and give page-builder a measurable intervention rather than adding a generic FAQ.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- A premium website must align stakeholders, content, navigation, and conversion architecture to a real outside-in customer experience.
- The brief is broad ("redesign", "modernize", "reposition") and risks becoming inside-out brochureware.
- Multiple buyer types, channels, devices, or sectors must be reconciled into one coherent site.
- Discovery surfaced friction, drop-off, or misalignment that the sitemap alone cannot fix.
- The agency must defend page count, content depth, or scope decisions during proposal or design review.

## Preserved Domain Exclusions
- The work is a single landing page test where a hypothesis-led CRO experiment is faster.
- The team already has a validated, recent experience map and only needs implementation.
- The client cannot supply customer access or proxy research and refuses paid discovery.

## Preserved Domain Inputs
- Business goal, commercial KPI, and the behaviour the website must change.
- Available customer evidence: interviews, support tickets, sales calls, analytics, reviews, search terms.
- Stakeholder list across sales, support, operations, fulfilment, and leadership.
- Existing site structure, top entry pages, and known friction points.
- Constraints: locales, regulated content, accessibility, performance budget, CMS, integrations.

## Preserved Domain Workflow
1. Frame the mapping effort. Pick one map type per goal: customer journey map for a discrete buyer flow; experience map for a broad cross-channel reality; service blueprint when backstage operations must change; ecosystem map when multiple actors and platforms intersect; mental-model diagram when the site must match how users actually think about the task.
2. Investigate. Combine internal interviews, customer interviews, analytics, search data, and review mining. Capture verbatim language, decision moments, emotions, and unmet needs.
3. Illustrate. Lay out lanes for stages, actions, thoughts, emotions, touchpoints, opportunities, and metrics. Mark moments of truth, drop-off, and trust gaps.
4. Hold an alignment workshop. Walk stakeholders through the current state, surface disagreements, agree on the future-state experience, and capture concrete commitments.
5. Translate the future-state map into website architecture: sitemap, page goals, content priorities, primary CTAs, proof placement, form fields, analytics events, and measurement plan.
6. Hand off to `page-builder`, `seo`, `content-writing`, `form-ux-design`, and `service-blueprint-website-delivery` with explicit input artifacts.
7. Schedule a review window after launch to update the map with real behaviour and feed `experimentation`.

## Preserved Domain Quality Guidance
- Every page on the resulting sitemap maps to at least one customer stage, intent, and decision.
- Each "moment of truth" has a named page, content asset, proof element, and analytics event.
- Emotional low points are paired with explicit reassurance, evidence, or service-recovery copy on the page that addresses them.
- Backstage gaps that affect the website (slow quote, broken handoff, missing FAQ) are routed to `service-blueprint-website-delivery` rather than hidden in copy.
- The map names sources, sample sizes, and confidence so future stakeholders can challenge or update it.
- The future-state map states a measurable outcome per stage (lead quality, qualified call rate, time-to-value, retention).

## Preserved Domain Anti-Patterns
- Decorative journey maps with smiley faces and no decisions, evidence, or links to pages.
- Mapping the inside-out sales funnel and calling it a customer journey.
- Skipping employee experience and backstage operations, then blaming the website for poor conversion.
- Producing a map that nobody owns after the workshop.
- Using a single persona to justify a site that must serve multiple buyer types.

## Preserved Domain Outputs
- One labelled experience artefact (CJM, experience map, ecosystem map, or service blueprint) with sources and dates.
- Future-state map with measurable outcomes per stage.
- Sitemap and page-goal table derived from the map.
- Conversion and proof placement plan: where each piece of evidence must appear.
- Analytics event plan tied to the map's moments of truth.
- Backlog of backstage and operations fixes routed to `service-blueprint-website-delivery`.

## Preserved Domain References
- `references/mapping-method-selector.md` — choose the right map type for the brief.
- `references/discovery-interview-guide.md` — outside-in interview protocol and question bank.
- `references/map-to-sitemap-conversion.md` — turn a future-state map into pages, content, CTAs, and analytics.
- `references/alignment-workshop-runbook.md` — stakeholder workshop facilitation, decisions, and follow-up.
