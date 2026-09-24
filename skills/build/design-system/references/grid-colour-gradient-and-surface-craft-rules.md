# Grid, Colour, Gradient and Surface Craft Rules

Parent skill: [design-system](../SKILL.md). Read when setting the page grid, choosing type metrics, building a palette from a brand colour, specifying gradients, shadows, buttons, toggles or illustration rules for a website design system, or when a design "looks off" and the cause is craft rather than concept.

Related files: `legacy-guidance.md` (8pt spacing, two-layer shadows, button states, nested radius, line-height formula), `../../page-builder/references/component-design-rules.md` (navbars, hero, cards, icons, images), and the design engine's colour skills at `C:/wamp64/www/design-system-skills/skills/02-color-brand-and-visual-identity/color-selection/` for palette psychology and the full palette procedure.

---

## 1. Grid

### 1.1 Terms
- **Columns** — vertical content tracks.
- **Gutters** — gaps between columns (or rows).
- **Margins** — space outside the grid; generous margins give the page breathing room.
- **Module** — the cell where a column and row intersect; elements snap to modules.

### 1.2 Decision rules
1. Use 12 columns on desktop by default; 6 or 8 are acceptable alternatives. Avoid 7, 9 or 11 columns: they divide awkwardly into halves, thirds and quarters.
2. Prefer a **fluid** grid (columns flex, gutters and margins fixed) for responsive pages. Use a **fixed** grid only for content that must not reflow.
3. Keep all dimensions on the 8-point scale; use 4-point steps for text baselines.
4. Mobile: 16px side margins as the default (20–24px for airy brands); gutters of at least 16px, dropping to 8px only in deliberately dense layouts.
5. Desktop gutters sit in the 12–16px range for dense interfaces and wider for marketing pages; set the outer margin so the content column holds a comfortable measure rather than using a fixed number.
6. When aligning neighbouring text blocks, align them on the **baseline of the first line**, not on the top of the text box.

---

## 2. Type metrics beyond the basics

1. **Typeface selection order:** legibility (can similar letters be told apart?), then scalability (does it hold at small UI sizes and large display sizes?), then weight range (regular, bold and at least one intermediate plus italic). Never use script faces for body or UI text.
2. **Letter-spacing:** leave at zero for body text; well-made fonts are already spaced. Add slight tracking to runs of capitals, which are set tight by design. Excess tracking harms legibility.
3. **The rag:** keep the ragged right edge of left-aligned text even; break or rewrite lines that leave a deep notch or a single orphaned word.
4. **Type scale:** define a named set of text styles (about ten) with a purpose each, generated from a base size and ratio. Use no more than three sizes within one section.

---

## 3. Colour construction

### 3.1 Vocabulary to use in specifications
- **Hue** — the pure colour. **Tint** — hue plus white. **Shade** — hue plus black. **Saturation** — intensity.
- **Formats:** HEX/RGB (or OKLCH) for screens; CMYK for print; Pantone for controlled brand matching. Record all three in brand handover when print is in scope.

### 3.2 Harmony choice
| Scheme | Character | Typical use |
|---|---|---|
| Monochromatic (one hue, its tints and shades) | Calm, safe, premium | Minimal and professional sites |
| Analogous (neighbours on the wheel) | Harmonious | One dominant hue, two accents |
| Complementary (opposites) | Vivid, tense | Use the complement sparingly, e.g. for CTAs |
| Split-complementary | Contrast with less tension | Conversion-led product sites |
| Triadic | Bold, playful | Creative brands |
| Tetradic (two complementary pairs) | Striking, hard to balance | Editorial; needs strict dominance |

### 3.3 Five-step palette procedure
1. **Primary:** the recurring brand accent for buttons, key icons and headings. It need not come from a wheel formula.
2. **Secondary:** for secondary actions; either a harmony partner of the primary or a neutral grey family.
3. **Semantic colours:** blue = information, green = success, amber/yellow = warning, red = danger or error. Apply to alerts, notices and validation.
4. **Tints and shades:** build a scale for each colour for backgrounds, cards and overlays.
5. **Distribution:** apply roughly 60% dominant neutral, 30% secondary, 10% accent by visual weight.

Colours sampled from natural scenes tend to feel familiar and balanced; use them as a starting point when a brief has no brand colour.

### 3.4 Dark and contrast rules
- Use dark grey rather than pure black for text on white; avoid pure white text on pure black (the letters appear to glow).
- In dark mode, tints read more strongly than shades; step lighter to create emphasis.
- Check contrast numerically: at least 4.5:1 for normal text and 3:1 for large text (confirm against the current WCAG version in force for the project).
- Treat colour as a primary quality signal visitors judge quickly; do not quote specific "percentage of judgement" statistics without checking the source.

---

## 4. Gradients

1. Choose the type by shape: **linear** for rectangles and panels; **radial** for round shapes or a spotlight effect; **conic (angular)** for rotational effects.
2. Keep transitions gentle; hard jumps between stops look cheap.
3. Use no more than three colours in small shapes and keep stop spacing symmetrical.
4. Put the lightest colour at the top of vertical linear gradients, as if lit from above.
5. The safest gradient runs between a colour and its own tints and shades.
6. Two complementary colours meet in a muddy grey midpoint. Fix it by adding a bridging hue between them or by interpolating in a perceptual space (OKLCH).
7. A "morph" gradient layers a radial gradient over a linear one for organic depth; use once per page at most and check text contrast over every part of it.

---

## 5. Surfaces and depth

- Three depth states: **none** (flat on the surface), **drop shadow** (raised), **inner shadow** (recessed; suits text inputs).
- Vary shadow size with element size and elevation; avoid a single identical shadow on everything.
- In dark mode never use white or light glows as shadows; darken the element's own colour instead.
- See `legacy-guidance.md` §7 for the two-layer core-plus-cast shadow recipe and light direction.

---

## 6. Buttons and touch spacing

1. **Base button:** label at least 16px; about 12px vertical padding; width roughly twice the height as a starting proportion; derive XS–XL sizes by scaling these together.
2. **Tap targets:** at least 44 × 44px on touch screens (platform guides quote smaller minimums; use the larger figure); keep 8–10px clear space between adjacent targets.
3. **Shape:** moderately rounded corners keep attention on the label; keep radius, type and shadow identical across primary, secondary and tertiary buttons, changing only fill and border.
4. **Placement:** forward actions right, back actions left; place buttons where the page's scan path (F- or Z-pattern) ends. To slow a destructive choice, reverse the usual emphasis so the safe option is primary.
5. **States:** design default, hover, pressed, focus, loading and disabled (see `legacy-guidance.md` §8).

### Toggles
Use a toggle only for an immediate on/off setting. Show state through position and colour plus an external text label; never print "ON"/"OFF" inside the track.

---

## 7. Illustration rules

1. Use illustration when the subject need not be shown literally; use photography when users must see the real product, place or person.
2. Never shrink a detailed illustration into a small slot; commission or derive a simplified version for small sizes.
3. Keep one character set, one palette (drawn from the design tokens) and one drawing style across the site.
4. Highest-value placements: hero (sets mood and message), onboarding or "how it works" steps, empty states (show what to do next) and error pages (friendly explanation plus a way forward).

### Icon additions
Complementing the icon rules in `component-design-rules.md`: limit each icon to three or four colours; use duotone icons at medium sizes; keep gradient, glass and 3D icons for large hero or feature moments and use them sparingly, as repeated rich icons tire the eye.

---

## 8. Style-era vocabulary (for briefs and critiques)

Use these labels precisely when discussing direction; each carries known risks.

| Style | Signature | Risk to check |
|---|---|---|
| Flat | 2D shapes, no depth, bold colour | Weak affordance on controls |
| Material-style elevation | Shadow-based layers, cards | Generic look if unmodified |
| Neumorphism | Soft inset/outset shadows, low contrast | Fails contrast; avoid for controls |
| Glassmorphism | Frosted translucent panels over vivid backgrounds | Contrast and performance; limit to one element |
| Neubrutalism | Thick black borders, hard contrast, irregular grids | Must be deliberate and brand-fit |
| Bauhaus-inspired | Geometric sans, primary colours, strict grid | Can feel cold without warmth elsewhere |

---

## 9. Craft checklist

- [ ] Grid column count divides cleanly; fluid grid; mobile margins and gutters at least 16px.
- [ ] Adjacent text blocks align on first baselines.
- [ ] Typeface passes legibility, scalability and weight-range checks; no script body text.
- [ ] Tracking only on capitals; even rag; no more than three sizes per section.
- [ ] Palette built in five steps; semantic colours defined; 60-30-10 by weight.
- [ ] No pure black text on white or white-on-black body text; contrast measured.
- [ ] Gradients gentle, max three stops, lightest on top, no grey midpoint.
- [ ] Shadows scaled to elevation; no light shadows in dark mode.
- [ ] Buttons sized from one formula; tap targets and gaps meet minimums; toggles labelled outside.
- [ ] Illustrations consistent and simplified for small sizes.

---

## Sources

- Elisa Paduraru (2024) *Roots of UI/UX Design: Learn to Develop Intuitive Web Experiences*, Creative Tim.
- Ran Segall et al., Flux Academy, *The Complete Guide for Choosing Colors* (harmony and 60-30-10 framing; full procedure lives in the design engine's `color-selection/references/flux-process.md`).
