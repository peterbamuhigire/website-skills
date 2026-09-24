---
title: Intrinsic Layout and CSS Grid Patterns
description: Intrinsically responsive layout primitives, advanced CSS Grid patterns, container queries, modular scale, logical properties and composition over inheritance. Makes layouts responsive without media queries.
---

# Intrinsic Layout and CSS Grid Patterns

Parent skill: [design-system](../SKILL.md). Read when building or reviewing layout CSS, choosing between grid, flex and container queries, or setting up spacing and type scales.

Intrinsic design means layouts respond to their content and container, not to arbitrary viewport breakpoints. Set constraints (minimum item width, maximum measure, spacing ratio) and let the browser calculate. Media queries become manual overrides, not the primary mechanism. `layout-primitive-selection-and-overlay-icon-patterns.md` covers the selection procedure, Box, Imposter and Icon.

---

## 1. Compose small primitives

Do not style components as monoliths (`.dialog`, `.card`, `.hero`). Compose primitives that each do one job.

| Primitive | Job | CSS pattern |
|---|---|---|
| Stack | Vertical spacing | `* + * { margin-block-start }` |
| Box | Even padding | `padding` on all sides |
| Center | Centre with a maximum width | `max-inline-size` + `margin-inline: auto` |
| Cluster | Wrapping horizontal group | `display: flex; flex-wrap: wrap; gap` |
| Sidebar | Two columns that collapse | `flex-wrap: wrap` + `flex-grow` |
| Switcher | Row to column at a threshold | `flex-wrap` + `calc()` threshold |
| Cover | Vertically centred hero | `min-block-size` + flex column |
| Grid | Auto-filling grid | `repeat(auto-fit, minmax())` |
| Frame | Fixed aspect ratio | `aspect-ratio` |
| Reel | Horizontal scroll strip | `overflow-x: auto` + no-wrap flex |
| Container | Query context | `container-type: inline-size` |

A dialog is a Stack inside a Box inside an Imposter (positioned overlay).

## 2. Set up the scale and measure

Define a few irreducible values and derive the rest from them.

```css
:root {
  --measure: 60ch;   /* maximum line width */
  --ratio: 1.5;      /* modular scale ratio */
  --s0: 1rem;
  --s1: calc(var(--s0) * var(--ratio));
  --s2: calc(var(--s1) * var(--ratio));
  --s3: calc(var(--s2) * var(--ratio));
  --s4: calc(var(--s3) * var(--ratio));
  --s5: calc(var(--s4) * var(--ratio));
  --s-1: calc(var(--s0) / var(--ratio));
  --s-2: calc(var(--s-1) / var(--ratio));
}
```

Every spacing value derives from one ratio; changing `--ratio` recalibrates the whole design.

Choose the ratio by feel (test in the browser):

| Ratio | Name | Feel |
|---|---|---|
| 1.2 | Minor third | Tight, compact; dashboards |
| 1.25 | Major third | Balanced; most sites |
| 1.333 | Perfect fourth | Generous; editorial |
| 1.5 | Perfect fifth | Bold; landing pages |
| 1.618 | Golden ratio | Classical; luxury |

Derive type from the same scale so spacing and typography harmonise:

```css
:root {
  --ratio: 1.25;
  --s0: 1rem;
  --s1: calc(var(--s0) * var(--ratio));
  --s2: calc(var(--s1) * var(--ratio));
  --s3: calc(var(--s2) * var(--ratio));
  --font-small: calc(var(--s0) / var(--ratio));
  --font-base: var(--s0);
  --font-h4: var(--s1);
  --font-h3: var(--s2);
  --font-h2: var(--s3);
  --font-h1: calc(var(--s3) * var(--ratio));
}
```

Limit measure to roughly 60 to 75 characters, in `ch` not `px`, so text width scales with the font:

```css
p, h1, h2, h3, h4, h5, h6, li, figcaption, blockquote, dt, dd {
  max-inline-size: var(--measure, 60ch);
}
```

## 3. Use logical properties everywhere

They behave correctly in every writing mode and text direction. Multilingual sites (English, French, Swahili) may not need right-to-left today, but logical properties cost nothing and protect later work.

| Physical | Logical |
|---|---|
| `width` / `height` | `inline-size` / `block-size` |
| `max-width` / `min-height` | `max-inline-size` / `min-block-size` |
| `margin-top` / `margin-bottom` | `margin-block-start` / `margin-block-end` |
| `margin-left` / `margin-right` | `margin-inline-start` / `margin-inline-end` |
| `padding-left` / `padding-right` | `padding-inline-start` / `padding-inline-end` |
| `text-align: left` | `text-align: start` |
| `border-left` | `border-inline-start` |

## 4. Implement the primitives

### Stack
Injects margin between siblings through the parent; nothing on the first or last child.

```css
.stack > * + * { margin-block-start: var(--s1, 1.5rem); }
```
Tailwind: `<div class="space-y-6">`. Nest stacks for rhythm: a large stack (`space-y-12`) for sections, a medium one (`space-y-6`) inside a section, a small one (`space-y-4`) for paragraphs.

Split stack, to push the last item to the bottom of a flex column:
```css
.stack-split > :last-child { margin-block-start: auto; }
```

### Center
```css
.center {
  box-sizing: content-box; /* padding is added outside the maximum width */
  max-inline-size: var(--measure);
  margin-inline: auto;
  padding-inline: var(--s1);
}
```
Tailwind: `<div class="mx-auto max-w-prose px-4">`. `content-box` keeps content width constant whatever the padding.

### Cluster
For navigation links, tag lists, button groups.
```css
.cluster { display: flex; flex-wrap: wrap; gap: var(--s1); justify-content: flex-start; align-items: center; }
```
Tailwind: `flex flex-wrap gap-4 items-center`.

### Sidebar
Collapses below the content when space runs out; no breakpoint.
```css
.with-sidebar { display: flex; flex-wrap: wrap; gap: var(--s1); }
.with-sidebar > :first-child { flex-basis: 20rem; flex-grow: 1; }   /* sidebar minimum width */
.with-sidebar > :last-child { flex-basis: 0; flex-grow: 999; min-inline-size: 50%; } /* wraps when sidebar would exceed half */
```

### Switcher
Row when the container is wide enough, column when items would fall below a threshold.
```css
.switcher { display: flex; flex-wrap: wrap; gap: var(--s1); }
.switcher > * { flex-grow: 1; flex-basis: calc((var(--measure) - 100%) * 999); }
```
Wider than `--measure`: the calculation is hugely negative, so the basis is effectively zero and items sit side by side. Narrower: it is hugely positive, so each item takes a full row.

### Cover
```css
.cover { display: flex; flex-direction: column; min-block-size: 100svh; padding: var(--s2); }
.cover > * { margin-block: var(--s1); }
.cover > :first-child:not(h1, h2) { margin-block-start: 0; }
.cover > :last-child:not(h1, h2) { margin-block-end: 0; }
.cover > h1, .cover > h2 { margin-block: auto; }
```
Use `100svh` rather than `100vh` on mobile.

### Frame
```css
.frame { aspect-ratio: 16 / 9; overflow: hidden; }
.frame > img, .frame > video { inline-size: 100%; block-size: 100%; object-fit: cover; }
```
Common ratios: 16/9 hero, 4/3 card image, 1/1 avatar, 3/2 landscape photograph.

### Reel
For galleries and card strips on mobile; use scroll-snap, not a JavaScript carousel.
```css
.reel { display: flex; gap: var(--s1); overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
.reel > * { flex: 0 0 auto; scroll-snap-align: start; }
```
Tailwind: `flex gap-4 overflow-x-auto snap-x snap-mandatory` with children `w-[85vw] shrink-0 snap-start sm:w-[45vw] lg:w-auto lg:shrink`. Keep a visible cue that more content exists, and keep controls keyboard reachable.

## 5. Build grids

### Intrinsically responsive grid
No media queries:
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
  gap: var(--s1);
}
```
`auto-fit` creates as many columns as fit; `minmax(250px, 1fr)` sets a floor and equal growth; `min(250px, 100%)` prevents overflow below 250px. Column count then follows the container. Tailwind: `grid grid-cols-[repeat(auto-fit,minmax(min(250px,100%),1fr))] gap-6`.

### Named areas for page layouts
```css
.page {
  display: grid;
  grid-template-areas: "header header" "sidebar main" "footer footer";
  grid-template-columns: 280px 1fr;
  grid-template-rows: auto 1fr auto;
  min-block-size: 100vh;
}
.header { grid-area: header; } .sidebar { grid-area: sidebar; }
.main { grid-area: main; } .footer { grid-area: footer; }
@media (max-width: 768px) {
  .page { grid-template-areas: "header" "main" "sidebar" "footer"; grid-template-columns: 1fr; }
}
```
Whole-page structure changes are a legitimate use of a media query.

### The `fr` unit
A fraction of the space left after fixed and content-sized tracks.
```css
grid-template-columns: 1fr 1fr 1fr;      /* three equal */
grid-template-columns: 280px 1fr;        /* fixed plus flexible */
grid-template-columns: auto 1fr;         /* content-sized plus remainder */
grid-template-columns: 1fr 1.618fr;      /* golden proportion */
```

### Alignment
```css
.grid { align-items: start; justify-items: stretch; align-content: start; justify-content: center; }
.featured { align-self: center; justify-self: end; }
```
`align-*` acts on the block axis, `justify-*` on the inline axis; the `*-items` and `*-self` forms align content within cells, `*-content` aligns the grid within its container.

### Subgrid
Lets nested grids inherit parent tracks, so card titles, descriptions and calls to action align across cards of unequal content length.
```css
.parent { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--s1); }
.child { display: grid; grid-column: span 3; grid-template-columns: subgrid; }
```
Check current browser support before relying on it and provide a sensible fallback.

## 6. Choose container queries or media queries

Container queries let a component respond to its parent's size.

```css
.container-context { container-type: inline-size; container-name: card; }
@container (min-width: 400px) { .card-content { display: grid; grid-template-columns: 200px 1fr; } }
@container card (min-width: 600px) { .card-content { grid-template-columns: 300px 1fr 200px; } }
```
Tailwind (needs the container-queries plugin or a version that includes it): parent `@container`, child `flex flex-col @md:flex-row @lg:grid @lg:grid-cols-3`.

| Situation | Use |
|---|---|
| Card layout that changes with where it is placed | Container query |
| Sidebar content adapting as the sidebar narrows | Container query |
| Design-system component used in several contexts | Container query |
| Navigation switching between mobile and desktop | Media query |
| Full-page structure changes | Media query |

Rule: if the component appears in containers of different widths at the same viewport size, use container queries; if it changes only with the viewport, use media queries.

## 7. Size type and units fluidly

Fluid root size with explicit bounds:
```css
:root { font-size: clamp(1rem, 0.875rem + 0.5vw, 1.375rem); }
```
The simpler `calc(1rem + 0.5vw)` also works; the `1rem` term keeps the size from dropping below the user's chosen default, and all `rem` values then scale together.

Never set font sizes in `px`: it ignores the size the user chose in browser settings and weakens zoom behaviour.

Unit rules:
- Font sizes: `rem`, `em`, `clamp()`.
- Spacing (margin, padding, gap): `rem` or scale custom properties.
- Text maximum width: `ch`.
- Media queries: `em`, so they scale with user font preferences.
- Borders, outlines, shadows: `px` is acceptable.

## 8. Anti-patterns

| Anti-pattern | Problem | Intrinsic alternative |
|---|---|---|
| Fixed widths (`width: 400px`) | Breaks off that width | `max-inline-size` + `flex-basis` |
| Fixed heights | Overflow, truncation | `min-block-size` or `aspect-ratio` |
| Breakpoint-only column changes | Ignores content | `repeat(auto-fit, minmax())` |
| `px` font sizes | Ignores user settings | `rem`, `em`, `clamp()` |
| Monolithic component styles | Duplicated layout code | Compose primitives |
| `float` for layout | Fragile, clearfix hacks | Flexbox or Grid |
| `!important` overrides | Specificity wars | Cascade and custom properties |
| Negative margins for spacing | Break at boundaries | `gap` |

## 9. Implementation checklist

- [ ] Modular scale (ratio and base) defined in `:root`.
- [ ] Measure applied to all text elements (`max-inline-size: 60ch`).
- [ ] Logical properties instead of physical ones.
- [ ] No `px` font sizes; `rem`, `em` or `clamp()` only.
- [ ] Fluid root font size via `clamp()` or `calc(1rem + 0.5vw)`.
- [ ] Grids use `repeat(auto-fit, minmax())`, no breakpoint needed.
- [ ] Stack used for vertical spacing, not per-element margins.
- [ ] Sidebar collapses without a media query.
- [ ] Container queries for components used in several contexts.
- [ ] `gap` everywhere, no margin hacks.
- [ ] Subgrid for cross-card alignment, with a fallback.
- [ ] Reel with scroll-snap for horizontal scrolling, not a JavaScript carousel.
- [ ] `100svh` instead of `100vh` for mobile viewport height.

## Sources

- Pickering, H. and Bell, A. (2019 onward) *Every Layout*, every-layout.dev. Informed the primitive set, composition approach, modular scale, measure and logical-property rules.
- Andrew, R. (2019) *Get Ready for CSS Grid Layout*, 2nd edn, A Book Apart. Informed the grid, `fr`, alignment, named-area and subgrid patterns.
