# Layout Primitive Selection, Box, Overlay and Icon Patterns

Parent skill: [design-system](../SKILL.md). Read when choosing which layout primitive to use for a component, when reviewing CSS for bespoke flex/grid code, stray `@media` queries or hard-coded widths, or when building padded panels, centred overlays and inline icons.

Companion file: `intrinsic-layout.md` holds the core primitives (Stack, Center, Cluster, Sidebar, Switcher, Cover, Grid, Frame, Reel), logical properties, the axiom/modular-scale setup and container queries. This file adds the selection procedure, the global assumptions, and the three primitives not implemented there: Box, Imposter (overlay) and Icon.

---

## 1. Operating principles

1. **Describe rules; let the browser solve.** The viewport, font size, zoom, language and content length are unknown. Set constraints (maximum measure, minimum item width, spacing ratio) instead of pixel positions and cascades of breakpoints.
2. **One concern per primitive.** Stack does vertical rhythm only; Box does padding, border and background only; Grid does columns only. Build components by nesting primitives, not by adding properties to one.
3. **Suggest sizes, do not prescribe them.** Prefer `max-inline-size`, `flex-basis`, `min()`, `clamp()` and `ch` units over fixed `width`.
4. **`gap` for siblings inside flex and grid.** Reserve the adjacent-sibling margin pattern (`> * + *`) for the Stack, where `margin-block-start: auto` must stay available to push an item to the end.
5. **Set spacing variables on children, not parents.** `.stack > * + * { margin-block-start: var(--space, var(--s1)); }` lets a nested stack of the same class use its own value.
6. **Handle exceptions through the cascade**, with a sibling class at equal specificity, never with `!important`.
7. **Logical properties only** for content layout (`margin-inline`, `inline-size`, `inset-block-start`).

## 2. Global assumptions every primitive relies on

```css
*, *::before, *::after { box-sizing: border-box; }
img, video, svg { max-inline-size: 100%; }
:root { --measure: 60ch; --border-thin: 1px; /* plus the modular scale from intrinsic-layout.md */ }
```

The Center is the single exception: it uses `content-box` so its padding sits outside the measure.

## 3. Choosing the primitive

| Need | Primitive |
|---|---|
| Vertical rhythm between siblings | Stack |
| Padded card, callout, panel, dialog body | Box |
| Readable column centred at the measure | Center |
| Wrapping row of tags, chips, buttons | Cluster |
| Two regions that stack when narrow | Sidebar |
| Equal columns that all turn vertical below a threshold | Switcher |
| Full-height hero with a vertically centred main element | Cover |
| Card grid that reflows without breakpoints | Grid |
| Media cropped to a fixed ratio | Frame |
| Horizontally scrolling strip | Reel |
| Dialog, popover, overlay caption, centred play button | Imposter |
| Icon beside text that scales with the text | Icon |

Procedure: sketch the component as a tree of these primitives (for example, pricing = Switcher of Box > Stack), set each primitive's variables from the modular scale, and write new CSS only for what no primitive covers.

Quick reflow recipes to remember:
- Grid without media queries: `grid-template-columns: repeat(auto-fit, minmax(min(20ch, 100%), 1fr));`
- Sidebar that stacks when the main area would drop below half: sidebar gets a `flex-basis`; main content gets `flex-grow: 999; min-inline-size: 50%`.
- Switcher threshold: `flex-basis: calc((var(--threshold) - 100%) * 999);`

## 4. Box

Purpose: the visible rectangle. Owns padding, border, background and text colour; nothing else.

```css
.box {
  padding: var(--s1);
  border: var(--border-thin) solid;
  outline: var(--border-thin) solid transparent; /* redrawn in forced-colours mode */
  outline-offset: calc(var(--border-thin) * -1);
  color: var(--box-fg, var(--color-text));
  background-color: var(--box-bg, var(--color-surface));
}
.box * { color: inherit; }
.box.invert { color: var(--box-bg, var(--color-surface)); background-color: var(--box-fg, var(--color-text)); }
```

Rules: pad all four sides equally or not at all (unequal padding means a different layout need); keep the transparent outline so edges survive high-contrast modes; separate children with a Stack, not with borders on each child.

## 5. Imposter (centred overlay)

Purpose: place an element centred over its positioned ancestor or the viewport, whatever its height.

```css
.imposter {
  position: var(--positioning, absolute);
  inset-block-start: 50%;
  inset-inline-start: 50%;
  transform: translate(-50%, -50%);
}
.imposter.contain {
  --margin: 0px; /* keep the unit so calc() stays valid */
  overflow: auto;
  max-inline-size: calc(100% - (var(--margin) * 2));
  max-block-size: calc(100% - (var(--margin) * 2));
}
```

Rules: the parent needs `position: relative` (or use `--positioning: fixed` for the viewport); add `.contain` so tall content scrolls instead of spilling; for real dialogs wrap a native `<dialog>` so focus, Escape and backdrop come built in; stop assistive technology reading the obscured page (`inert` or focus trapping).

## 6. Icon

Purpose: an inline SVG sized to the text beside it.

```css
.icon { inline-size: 0.75em; block-size: 0.75em; inline-size: 1cap; block-size: 1cap; }
.with-icon { display: inline-flex; align-items: baseline; }
.with-icon .icon { margin-inline-end: var(--space, 0.5em); }
```

Rules: `0.75em` approximates capital height, `1cap` matches it exactly where supported (use `1ex` beside lowercase text); set `width` and `height` attributes on the SVG so it cannot render huge if CSS fails; draw with `currentColor` so icons follow text colour and themes; without a wrapper, a plain space between icon and label gives a gap that flips correctly in right-to-left text; always provide an accessible name (visible text, `<title>`, or `aria-label` on the parent control) unless the icon is decorative and hidden.

## 7. Review checklist

- [ ] Each component decomposes into named primitives; no one-off layout CSS where a primitive fits.
- [ ] No `@media` query used where `min()`, `auto-fit`, Sidebar or Switcher logic would do.
- [ ] No fixed `width` on content containers; measure capped with `max-inline-size`.
- [ ] Logical properties throughout; `gap` for flex/grid siblings.
- [ ] Spacing variables set on children; exceptions handled by cascade, not `!important`.
- [ ] Global `border-box`; Center uses `content-box`.
- [ ] Boxes pad evenly and keep a transparent outline; overlays contained; icons sized in text units with accessible names.

---

## Sources

- Heydon Pickering and Andy Bell, *Every Layout* (every-layout.dev).
