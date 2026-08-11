---
name: premium-ui-ux-design
description: Use when a premium website build needs build-coupled UX and visual-quality orchestration before design-system and page-builder; use the external design-system-skills engine for general visual doctrine.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Premium UI/UX Design
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Translate approved website strategy and experience evidence into a distinctive, implementable premium UX direction.

<!-- dual-compat-start -->
## Use When

- A lead-generation, ecommerce, high-ticket, or public-proof website needs a premium UX gate
- visual direction must be connected to implementation constraints.

## Do Not Use When

- Use for general visual doctrine, which belongs to `design-system-skills`, or for token implementation owned by `design-system`.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Approved strategy, experience map, content hierarchy, brand evidence, reference analysis, and technical constraints | Upstream website skills and external design doctrine | yes | Define an implementable experience direction | Stop when strategy or content hierarchy is absent |

## Workflow

1. Load the external design doctrine and validate upstream strategy
2. Choose hierarchy, interaction, typography direction, states, and responsive behaviour
3. Test distinctiveness, accessibility, multilingual growth, and low-bandwidth constraints
4. Stop on a banned default or unsupported pattern, repair the direction, then hand decisions to design-system and page-builder.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Premium UX direction and implementation brief | Design-system and page-builder | Names type rationale, hierarchy, components, states, breakpoints, motion limits, and quality risks |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Decision and review record | Design and release owners | Links each major visual choice to brand, behaviour, accessibility, or performance evidence |

<!-- dual-compat-end -->
## Capability Contract

Read, search, and visual inspection are required. Planning is read-only by default; editing design artefacts or code requires implementation authority. Asset licensing, external publication, spending, and production mutation require explicit authority.

## Degraded Mode

Without rendering, fonts, assets, or the external doctrine, return the narrowest qualified direction, mark visual checks `not assessed`, and do not certify premium quality.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Brand and content justify a distinctive display face | Specify it with performance fallback | Generic AI-default typography |
| Interaction adds no task value or harms 3G use | Remove or simplify it | Decorative friction |

## Quality Standards

- State the chosen typeface and reason before visual production; cover error, empty, loading, focus, and disabled states; meet accessibility and Africa performance constraints.

## Anti-Patterns

- Choosing Inter or a bare system stack as the primary face. Fix: select a brand-fit permitted face and document why.
- Using a purple gradient as premium shorthand. Fix: derive colour and contrast from brand evidence.
- Designing only the homepage. Fix: define shared patterns for every template family.
- Ignoring non-happy states. Fix: specify error, empty, loading, focus, and disabled behaviour.
- Certifying quality without renders. Fix: mark visual assessment `not assessed` and require visual QA.

## Worked Example

For a Kampala advisory firm, choose a licensed editorial serif supported by its authority positioning, pair it with a compact sans for mobile utility, and test both under the 3G font budget before handoff.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- A website must look premium enough to justify high-ticket pricing, trust, or serious commercial attention.
- Building lead-generation, ecommerce, product, portfolio, SaaS marketing, hospitality, education, healthcare, nonprofit, or enterprise websites.
- The site risks looking generic, templated, over-decorated, slow, hard to scan, or visually cheap.
- The website must make the owner's offer feel more valuable while also acting as proof of the developer's premium craft.

## Preserved Domain Inputs
- Website strategy brief, target audience, offer, brand position, content inventory, photos/assets, and conversion goal.
- Any current design system, screenshots, competitor benchmarks, and performance/accessibility constraints.

## Preserved Domain Workflow
1. Define the website's business job: trust, conversion, sales support, application, booking, donation, product education, or authority.
2. Pick the visual voice that fits the buyer and offer: operational, editorial, luxury minimal, consumer polished, institutional, or local-premium.
3. Load `premium-website-product` when the brief needs premium positioning, content, SEO, stack, or agency proof before styling begins.
4. Build hierarchy from the conversion path before styling sections.
5. Create the design system using the premium playbook: visual principles, color, type, spacing, imagery, motion, charts/tables, and production polish.
6. Apply the premium website gate before page production and again after visual QA.
7. Record evidence in the project scorecard and design-quality report.

## Preserved Domain Quality Guidance
- First viewport immediately communicates brand/category, offer, credibility, and primary action.
- Layout is responsive, fast, accessible, and visually coherent across primary templates.
- Imagery shows the real product, place, person, proof, interface, or outcome whenever available.
- Color, typography, spacing, and motion are tokenized and commercially appropriate.
- Forms, pricing, service pages, product pages, and contact flows reduce anxiety and make the next step obvious.
- Data, testimonials, case studies, stats, and comparisons are presented with accurate and readable visual hierarchy.
- Simplicity is treated as premium: navigation, forms, copy blocks, state changes, and mobile flows remove buyer effort without hiding necessary proof.
- Every primary template scores at least 8/10 on the premium UI/UX gate and design-quality-score rubric.

## Preserved Domain Anti-Patterns
- Landing pages that feel like generic AI output: vague gradients, blob backgrounds, decorative card piles, weak stock photos, and unsupported claims.
- Beautiful pages that do not explain the offer or move the user toward a business outcome.
- One-note color palettes, cramped mobile layouts, slow hero media, and inaccessible overlays.
- Using visual novelty where proof, clarity, and trust are required.

## Preserved Domain Outputs
- Premium website UX brief, visual direction, token plan, page-level quality notes, conversion path guidance, or gate report.

## Preserved Domain References
- `references/premium-website-ui-ux-playbook.md` - book-derived website design rules.
- `references/enterprise-website-ux-playbook.md` - enterprise website stakeholder, proof, navigation, trust, and Africa-calibrated UX rules.
- `references/mobile-dashboard-website-patterns.md` - mobile navigation, first-visit guidance, dashboard/proof presentation, and mobile quality checks.
- `references/premium-website-gate.md` - scoring and blocking defects.
- `../premium-website-product/references/premium-website-market-asset-gate.md` - website-as-premium-product, content, SEO, launch, stack, and agency proof gate.
- `references/source-register.md` - provenance disposition and rights gate; no active source path is asserted.

## World-class UX foundations (book-derived)

Required reading before kicking off a premium engagement:

- `references/levy-four-tenets.md` — Four-tenet framework (Business Strategy + Value Innovation + Validated User Research + Killer UX Design); Top-10 anti-patterns to reject in client briefs.
- `references/enterprise-five-outcomes.md` — Five mandatory outcomes (Useful / Easy / Efficient / Pleasing / Accessible) as a pre-launch gate. One No = no launch.
- `references/pm-collaboration-rules.md` — Fekeshazi 5+1 (5-10 min to explain, design as ongoing process, etc.) and the "don't hide important functions in menus" rule.

If a brief fails Levy's Top-10 check or omits any of the 5 outcomes, push back before scoping.
