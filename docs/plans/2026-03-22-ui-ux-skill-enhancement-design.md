# Design: UI/UX Skill Enhancement from Tidwell + StoryBrand

**Date:** 2026-03-22
**Books:** Designing Interfaces 3rd Ed (Tidwell, Brewer, Valencia) + Building a StoryBrand (Donald Miller)
**Approach:** Option A — Reference files + targeted rule additions woven into existing skills

---

## Scope

### Tidwell "Designing Interfaces" → UI/UX skills

| Chapter | Content | Target Skill |
|---------|---------|-------------|
| Ch1: Cognition Patterns | Safe Exploration, Instant Gratification, Satisficing, Habituation, Spatial Memory, Prospective Memory, Microbreaks | `ux-psychology` |
| Ch3: Navigation | Clear Entry Points, Modal Panel, Fat Menus, Escape Hatch, Breadcrumbs, Progress Indicator, Animated Transition | `page-builder` |
| Ch4: Layout | Visual Framework, Center Stage, Grid of Equals, Titled Sections, Module Tabs, Accordion | `design-system` |
| Ch5: Visual Style | Typography preattentive attributes, colour psychology, skeuomorphic vs. flat decision | `design-system` |
| Ch6: Mobile | Vertical Stack, Generous Borders, Bottom Navigation, Filmstrip, Touch Tools | `page-builder` |
| Ch8: Actions | Button Groups, Preview, Loading Indicators, Cancelability, Undo | `design-system` |
| Ch10: Forms | Forgiving Format, Input Hints, Autocompletion, Good Defaults, Error Messages | `form-ux-design` |

### StoryBrand → Brand/Content skills

| Content | Target Skill |
|---------|-------------|
| SB7 Framework (7-part) | `brand-storytelling` |
| BrandScript template | `brand-strategy` |
| Website messaging hierarchy | `sales-copywriting` |
| Clarity / noise principles | `content-writing` |

---

## Architecture

- **Reference files:** Detailed pattern libraries saved to `book-extractions/` and skill `references/` directories
- **Skill updates:** 20-40 lines of actionable rules added to each target skill, referencing the detailed files
- **500-line rule:** Skills already near limit get rules replacing weaker existing content

---

## Phases + Commits

1. **Phase 1** — Tidwell Ch1/Ch4/Ch5/Ch8 → `ux-psychology` + `design-system` + reference file
2. **Phase 2** — Tidwell Ch3/Ch6/Ch10 → `page-builder` + `form-ux-design` + reference file
3. **Phase 3** — StoryBrand SB7 → `brand-storytelling` + `brand-strategy` + `sales-copywriting` + reference file

Commit after each phase with `feat:` prefix.
