---
title: Glass and Translucency (Glassmorphism) — Disallowed as Decoration
scope: cross-cutting
tech-stack: Astro + Tailwind CSS v4 + Alpine.js
---

# Glass and Translucency (Glassmorphism)

**Status: no-ship as decoration.** Frosted or "liquid" glass surfaces (a
semi-transparent background over `backdrop-filter: blur()`, usually with a thin
light border and a soft shadow) are not used on client websites. This file
used to teach the technique; it was corrected on 2026-09-29 (M10-11) because
it contradicted the doctrine below. The earlier version is in git history.

## Why

- **Doctrine.** The design engine lists glassmorphism among the no-ship
  choices for websites (`chwezi-design-engine/doctrine/references/ai-slop-taxonomy.md`,
  K5 AS4 decorative attention) and names "glassmorphism as a default surface
  treatment" as a practice the literature teaches and the engine rejects.
  This engine's `visual-qa/references/slop-rules.md` §13 applies the same
  boundary.
- **Enforcement.** The `chwezi-slop` detector rule `glassmorphism` (block)
  fails `scripts/slop-scan.sh` when a backdrop blur sits over a translucent
  background, so client CI blocks it on `main`.
- **Legibility.** Text over a blurred, moving or photographic backdrop has no
  fixed contrast ratio; it passes on one image and fails on the next.
- **Cost on the target devices.** Backdrop blur is a per-frame compositing cost.
  On the low-end Android phones common in the engine's East African markets it
  slows scrolling and drains battery (see `deploy/references/performance-gate.md`
  for the network and device profile).
- **Convergence.** It is one of the surface treatments AI-generated sites
  default to, so it reads as a template rather than a brand decision.

## What to use instead

| Need | Use | Not |
|---|---|---|
| Text over a hero photograph | A solid panel from the token palette, or a dark scrim (a solid colour at fixed opacity, no blur) with contrast measured on the actual image, 4.5:1 for body text | A frosted card |
| A sticky navigation bar | Transparent over the hero, then a solid token surface once the page scrolls (a class toggled on scroll; no blur) | `backdrop-blur` on the bar |
| Separating a card from the page | A 1px border in a token neutral, or a lightness step between surface tokens | Translucency plus a glow border |
| Modal or dialog separation | The native `<dialog>` with a solid `::backdrop` colour at fixed opacity | A blurred page behind the dialog |
| Premium feel in tourism, hospitality or portfolio sites | Photography, typography and spacing chosen in the brief; the design engine's `sector-strategies` for the visual treatment | Glass as the "premium" signal |

## The only exception

Translucency is allowed only where it is functional rather than decorative,
for example a platform-native material the client's own app already uses and
the website must match. It then needs all of:

1. a reason recorded as a waiver in the form `<who>: <evidence>` (a human
   grants it; agents may not grant a waiver wider than a single value), listed
   in the release evidence;
2. body-text contrast of at least 4.5:1 measured against the busiest backdrop
   the element can sit on;
3. a solid fallback under `@media (prefers-reduced-transparency: reduce)` and
   `@media (prefers-contrast: more)`, and when `backdrop-filter` is
   unsupported;
4. no blur on anything larger than the element itself, and never on the page
   background.

The waiver format and the detector's inline waiver syntax are in
`quality-gates/visual-qa/references/slop-rules.md` (Waivers).

## Related

- `references/ai-slop-prevention.md` (glassmorphism overuse)
- `references/motion-design.md` (no decorative motion on surfaces)
- `quality-gates/visual-qa/references/slop-rules.md` §13 (visual no-ship boundary)
