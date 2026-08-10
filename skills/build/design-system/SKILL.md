---
name: design-system
description: Use when converting an approved brand and style brief into website tokens, component rules, responsive behaviour, states, and motion; do not use to analyse reference sites or assemble production pages.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Design System
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- An approved style brief must become reusable typography, colour, spacing, grid, imagery, motion, and component-state rules.
- An existing interface has token drift, duplicated components, inconsistent states, or page-specific styling that needs consolidation.

## Do not use when
- The task is extracting lessons from reference websites; use `design-reference` first.
- The task is assembling approved components into production routes; use `page-builder`.
- Brand direction is undecided; stop at a decision brief rather than styling by default.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Brand/style brief and approved constraints | Discovery or `docs/style-brief.md` | yes | Stop visual selection; return the missing decisions. |
| Design-reference synthesis | `design-reference` | conditional | Proceed only from explicit brand inputs and label comparison unassessed. |
| Existing components and tokens | Repository | conditional | For a redesign, stop until the current system is inspectable. |
| Target browsers and accessibility level | Technical brief | yes | Use documented repository defaults or qualify the system. |

## Workflow

**Step 0 — Consult the design doctrine first (cross-cutting).** Before choosing fonts, colour,
spacing, imagery, or motion, consult the **`design-system-skills`** engine: resolve its location
on this device from your global engine-routing table (`~/.claude/CLAUDE.md`, or `AGENTS.md` for
Codex) — never assume an absolute path — then read `doctrine/design-doctrine.md` and
`doctrine/references/` (banned AI-slop fonts incl. Inter/Geist, type scale, colour system,
pairing, the ai-slop taxonomy). State your typeface and colour intent with a one-line reason in
`docs/style-brief.md` before implementing (doctrine non-negotiable #1). Never use a banned
AI-slop font as primary type.

2. Stop token selection when brand, licence, glyph, or accessibility constraints are unresolved.
3. Audit the existing interface first when a site or product already exists: identify duplicated components, token drift, inconsistent states, and bespoke one-off styling before inventing anything new.
3. For premium or revenue-critical sites, load `premium-ui-ux-design` before choosing color, type, spacing, imagery, or motion direction.
4. Choose the smallest set of references needed for the current job.
5. Define the system in layers: primitives, semantic tokens, then component-level tokens and rules.
6. Produce the implementation, configuration, or guidance this skill owns.
7. Validate tokens, contrast, states, responsive behaviour, glyph coverage, and reduced motion.
8. Recovery: if rendering or fonts fail, retain the last verified system, mark the affected checks unassessed, and return the exact retest step.

## Quality standards
- Tokens and components have one documented source of truth and implementable responsive/state rules.
- Typeface, colour, imagery, spacing, motion, and data-viz decisions carry brand and accessibility rationale.
- Trend-led treatments are enhancements over a semantic baseline and include measurable budgets, fallbacks, and a client/user-task rationale; novelty is not a design-system requirement.
- Measured contrast, glyph, state, and viewport results stay distinct from unassessed visual checks.
- Define section inset tokens and usage rules for every visual container level: page sections/bands, heroes, cards, CTA rows, controls/toolbars, and media groups. Every container must provide deliberate top, bottom, and side breathing room so content never sits on its own boundary; variant classes such as dark/warm/full-bleed must preserve base section spacing.
- The design system must act as a living product, not a one-time style dump: include usage rules, states, and a clear source of truth.
- Prefer reusable components and documented patterns over page-specific bespoke styling.
- Premium design systems must define visual voice, dominant/subordinate/accent color logic, typography roles, imagery rules, data/proof presentation, component states, and responsive production rules.

## Anti-patterns
- Choosing type without brand, licence, and glyph checks. Fix: verify all three first.
- Creating page-specific values. Fix: promote repeated meanings into semantic tokens.
- Specifying only default states. Fix: define focus, error, loading, empty, and disabled states.
- Claiming contrast from appearance. Fix: measure the rendered colour pair.
- Adding motion without reduced motion. Fix: supply a reduced variant or remove it.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not use banned AI-default typefaces or palette defaults as the primary visual voice; state a reason.
- Do not define components without applicable hover, focus, disabled, loading, error, and empty states.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Token and component specification | `page-builder` and developers | Primitive, semantic, and component tokens have one source of truth and no unexplained duplicates. |
| Updated style brief | Client and delivery team | Typeface, colour, imagery, motion, state, and responsive choices include rationale. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| System QA record | Token drift, contrast, state, responsive checks | Results name the method; unavailable checks are unassessed. |

## Capability Contract
Read-only audit is the default for review requests. Edit tokens, styles, or components only when implementation is requested. Never install fonts, buy licences, publish, or change brand assets without explicit authority.

## Degraded Mode
If fonts, render tools, browsers, or brand evidence are unavailable, produce a bounded token proposal and list every visual or licence check still required. Do not claim contrast, rendering, or responsive compliance without measurement.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Existing token is coherent and used | Preserve and document it | Gratuitous redesign |
| Duplicate values express one meaning | Consolidate under a semantic token | Token drift |
| Typeface lacks licence or required glyphs | Reject pending verification | Legal or i18n failure |
| Motion ignores reduced-motion needs | Remove it or provide a reduced variant | Accessibility failure |
| Advanced treatment has no static or low-capability equivalent | Complete the fallback contract before tokenising it | Fragile or exclusionary system |

## Worked Example
For a multilingual professional-services site, choose a licensed serif with verified Latin Extended glyphs for editorial headings, pair it with a restrained sans for UI, define fluid type tokens and focus/error states, then hand `page-builder` tested component rules rather than isolated mock-up values.

## References
- Use `references/math-for-web-design.md` when sizing, spacing, typography, grids, media ratios, color ramps, or motion timing should be derived from proportion, `clamp()`, `calc()`, `minmax()`, aspect-ratio, or rounding logic.
- Use sibling skill `premium-ui-ux-design` when perceived quality, beauty, conversion, or high-ticket trust is part of the job.
- Prioritize `references/ux-quality-checklist.md` when validating whether the system is coherent enough to ship.

<!-- dual-compat-end -->
## Notes
- Minimum system outputs for substantial work:
  1. token structure
  2. component inventory or change list
  3. states and accessibility expectations
  4. source-of-truth location for future contributors


## Dashboard and data-viz coverage

For projects that include dashboards (executive, operational, public-facing), additional rules apply. See `references/enterprise-data-viz-rules.md` — covers chart-type selection, pre-attentive visual attributes, and the no-3D / no-shadow rules. Premium-priced dashboards must comply.
