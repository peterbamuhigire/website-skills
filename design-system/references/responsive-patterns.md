---
title: Responsive Design Patterns
description: Mobile-first responsive architecture — fluid typography, spacing tokens, grid breakpoint recipes, Tailwind class patterns, and responsive component transforms for all three breakpoints (375px, 768px, 1280px+).
sources: Adham Dannaway "Practical UI" (2022) + Adrian Kuleszo "How to Design Better UI Components 3.0" (2024) + Lisandra Maioli "Fixing Bad UX Designs" (2018) + Will Grant "101 UX Principles" (2018)
---

# Responsive Design Patterns

Mobile-first means **designing for 375px first**, then enhancing upward. Every CSS rule starts at mobile and adds complexity at wider breakpoints — never the reverse.

---

## BREAKPOINT ARCHITECTURE

| Token | Tailwind | Width | Target | CSS |
|-------|----------|-------|--------|-----|
| `sm` | `sm:` | 640px | Large phones landscape | `@media (min-width: 640px)` |
| `md` | `md:` | 768px | Tablets portrait | `@media (min-width: 768px)` |
| `lg` | `lg:` | 1024px | Tablets landscape / small laptops | `@media (min-width: 1024px)` |
| `xl` | `xl:` | 1280px | Desktops | `@media (min-width: 1280px)` |
| `2xl` | `2xl:` | 1536px | Large desktops | `@media (min-width: 1536px)` |

**Primary design targets** (match project checklist):
- **375px** — base (single column, 16px body, 44×44px touch targets)
- **768px** — tablet (2-column grids, expanded navigation)
- **1280px** — desktop (max-w-7xl container, full navigation, 3–4 column grids)

**Container strategy:**
```html
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
```
- Mobile: 16px side padding (`px-4`)
- Tablet: 24px side padding (`sm:px-6`)
- Desktop: 32px side padding (`lg:px-8`)

---

## FLUID TYPOGRAPHY

Never hard-code font sizes per breakpoint. Use CSS `clamp()` for smooth scaling between minimum and maximum sizes.

**Formula:** `clamp(min, preferred, max)`
- `min` = smallest acceptable size (mobile)
- `preferred` = viewport-relative value (usually `vw`-based)
- `max` = largest size (desktop)

### Type Scale (Mobile → Desktop)

| Element | Mobile | Desktop | Fluid CSS | Tailwind |
|---------|--------|---------|-----------|----------|
| H1 (hero) | 32px | 64px | `clamp(2rem, 5vw, 4rem)` | `text-3xl sm:text-4xl lg:text-5xl xl:text-6xl` |
| H2 (section) | 24px | 40px | `clamp(1.5rem, 3.5vw, 2.5rem)` | `text-2xl sm:text-3xl lg:text-4xl` |
| H3 (subsection) | 20px | 28px | `clamp(1.25rem, 2.5vw, 1.75rem)` | `text-xl sm:text-2xl` |
| H4 | 18px | 22px | `clamp(1.125rem, 2vw, 1.375rem)` | `text-lg sm:text-xl` |
| Body | 16px | 18px | `clamp(1rem, 1.2vw, 1.125rem)` | `text-base lg:text-lg` |
| Small / caption | 14px | 14px | `0.875rem` (fixed) | `text-sm` |
| Button / CTA | 16px | 18px | `clamp(1rem, 1.2vw, 1.125rem)` | `text-base lg:text-lg` |

**Rules (Dannaway):**
- Body text: minimum **16px** — never below; use **18px** for audiences 45+
- Line height: **1.5–1.75** for body text; **decrease as font size increases** (H1 at 1.1–1.2, H2 at 1.2–1.3)
- Line length: **50–75 characters** max → use `max-w-prose` (65ch) for body text columns
- Left-align body text always — centred text is harder to scan beyond 3 lines
- Decrease letter-spacing for large headings (tight tracking improves cohesion at scale)

**Implementation in `global.css`:**
```css
:root {
  --text-h1: clamp(2rem, 5vw, 4rem);
  --text-h2: clamp(1.5rem, 3.5vw, 2.5rem);
  --text-h3: clamp(1.25rem, 2.5vw, 1.75rem);
  --text-body: clamp(1rem, 1.2vw, 1.125rem);
}
h1 { font-size: var(--text-h1); line-height: 1.15; }
h2 { font-size: var(--text-h2); line-height: 1.25; }
h3 { font-size: var(--text-h3); line-height: 1.3; }
body { font-size: var(--text-body); line-height: 1.65; }
```

---

## RESPONSIVE SPACING SYSTEM

Use the **8pt grid** (Kuleszo) as base unit. Spacing tokens scale with breakpoints.

### Spacing Scale

| Token | Mobile (base) | Tablet (`md:`) | Desktop (`lg:`) | Use for |
|-------|---------------|----------------|-----------------|---------|
| `xs` | 4px | 4px | 4px | Inline icon gaps, tiny separators |
| `sm` | 8px | 8px | 8px | Field-to-label, tight groups |
| `md` | 16px | 16px | 16px | Intra-component padding |
| `lg` | 24px | 32px | 32px | Card padding, group spacing |
| `xl` | 32px | 48px | 48px | Between sections (minor) |
| `2xl` | 48px | 64px | 80px | Between major sections |
| `3xl` | 64px | 80px | 120px | Hero padding, page-level spacing |

**Tailwind pattern:**
```html
<!-- Section spacing scales up at breakpoints -->
<section class="py-12 md:py-16 lg:py-24">
  <div class="space-y-6 md:space-y-8 lg:space-y-10">
```

**Dannaway's proximity rule:** Space elements based on how closely related they are.
- Related items (label + field): **8px**
- Siblings (list items): **16px**
- Groups (card sections): **24–32px**
- Sections: **48–80px**
- Unrelated content: **80–120px**

The **further apart** two elements are, the **less related** they appear. Group related items tightly; separate unrelated items generously.

---

## RESPONSIVE GRID PATTERNS

### Column Collapse Rules

| Breakpoint | Columns | Tailwind Grid | Use for |
|------------|---------|---------------|---------|
| 375px (base) | 1 | `grid-cols-1` | Everything stacks vertically |
| 640px (`sm:`) | 2 | `sm:grid-cols-2` | Cards, features, team members |
| 768px (`md:`) | 2–3 | `md:grid-cols-2` or `md:grid-cols-3` | Services, portfolio |
| 1024px (`lg:`) | 3 | `lg:grid-cols-3` | Full grid layouts |
| 1280px (`xl:`) | 3–4 | `xl:grid-cols-4` | Dense grids (gallery, products) |

**Standard grid recipes:**
```html
<!-- Services / Features grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">

<!-- Team / Testimonials grid -->
<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">

<!-- Gallery / Portfolio grid -->
<div class="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">

<!-- Two-column layout (content + sidebar) -->
<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
  <div class="lg:col-span-2"><!-- Main content --></div>
  <aside><!-- Sidebar --></aside>
</div>
```

**12-column grid (Kuleszo):**
- Desktop (1440px frame): 12 columns, 100px margins, 20px gutters → 1240px working area
- Tablet (768px): 8 columns, 32px margins, 16px gutters
- Mobile (375px): 4 columns, 16px margins, 8px gutters
- Always align major layout blocks to the column grid

---

## RESPONSIVE COMPONENT TRANSFORMS

### Navigation
```
Mobile (375px):        Tablet (768px):         Desktop (1280px):
┌──────────────┐      ┌───────────────────┐   ┌──────────────────────────┐
│ Logo    ☰    │      │ Logo    ☰         │   │ Logo  Nav Nav Nav  [CTA] │
└──────────────┘      └───────────────────┘   └──────────────────────────┘
```
- **Mobile/Tablet:** Logo left, hamburger right → off-canvas menu slides from right
- **Desktop (`lg:`):** Full horizontal nav with primary CTA as button
- Tailwind: `hidden lg:flex` for desktop nav; `lg:hidden` for hamburger

### Cards
```
Mobile:                 Tablet:                Desktop:
┌──────────┐           ┌─────┐ ┌─────┐       ┌───┐ ┌───┐ ┌───┐
│  Image   │           │     │ │     │       │   │ │   │ │   │
│  Title   │           │     │ │     │       │   │ │   │ │   │
│  Text    │           └─────┘ └─────┘       └───┘ └───┘ └───┘
│  [CTA]   │
└──────────┘
```
- Mobile: full-width, vertical stack
- Tablet: 2-column grid
- Desktop: 3-column grid
- Card padding: `p-4 md:p-6` (16px → 24px)

### Hero Section
```
Mobile:                          Desktop:
┌────────────────────┐          ┌──────────────────────────────┐
│     [Image]        │          │  Headline        [Image]     │
│  Headline          │          │  Subtitle                    │
│  Subtitle          │          │  [CTA]  [Ghost]              │
│     [CTA]          │          └──────────────────────────────┘
└────────────────────┘
```
- Mobile: image on top, text stacked below, CTA full-width
- Desktop: side-by-side with text left, image right (or reverse)
- Tailwind: `flex flex-col lg:flex-row lg:items-center`

### Forms
- Labels: **above field** at all breakpoints (never side-by-side on mobile)
- At `md:` and above: optional left-aligned labels with `grid-cols-[200px_1fr]` for short forms
- Submit button: **full-width on mobile** (`w-full md:w-auto`)
- Form max-width: `max-w-lg` (512px) to prevent fields from stretching too wide

---

## RESPONSIVE IMAGES

**Never upscale** — use `_catalog.json` dimensions as maximum.

### srcset Pattern (Astro)
```astro
<Image
  src={import('../assets/images/hero.jpg')}
  widths={[400, 800, 1200]}
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
  alt="Descriptive alt text"
  class="w-full h-auto object-cover"
  loading="lazy"
/>
```

**Rules:**
- Hero images: `loading="eager"` (above fold); everything else: `loading="lazy"`
- Aspect ratios: maintain consistent ratios within grids (16:9 for heroes, 4:3 for cards, 1:1 for avatars)
- Full-bleed images on mobile, constrained on desktop: `w-full lg:rounded-xl lg:max-w-4xl`
- Background images: use `object-cover` + explicit `aspect-ratio` to prevent CLS

---

## SAFE AREAS & VIEWPORT

### Viewport Meta Tag (MANDATORY)
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
- **NEVER** set `maximum-scale=1` or `user-scalable=no` — this disables pinch-to-zoom and is an accessibility violation (Grant, Ch 65)
- Exception: only for fullscreen web apps where zoom breaks functionality

### Safe Areas (Modern Devices)
```css
/* Handle notch + home indicator on iOS */
body {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}
```
- Bottom-fixed CTAs must respect `env(safe-area-inset-bottom)` to avoid overlap with home indicator
- Sticky headers: account for `env(safe-area-inset-top)` on notched devices

### Orientation Handling
- **Never lock orientation** — let users rotate freely
- Test all layouts in both portrait and landscape
- Landscape mobile: content area narrows vertically → ensure CTAs remain visible without scrolling
- Use `min-height: 100svh` (small viewport height) instead of `100vh` to handle mobile browser chrome

---

## MOBILE-FIRST CSS ORDERING

Write CSS in this order — mobile defaults first, then layer on enhancements:

```css
/* 1. Mobile base (no media query) */
.card { padding: 1rem; }

/* 2. Tablet enhancement */
@media (min-width: 768px) {
  .card { padding: 1.5rem; }
}

/* 3. Desktop enhancement */
@media (min-width: 1280px) {
  .card { padding: 2rem; }
}
```

**Tailwind equivalent** (already mobile-first by default):
```html
<div class="p-4 md:p-6 xl:p-8">
```

---

## RESPONSIVE TESTING CHECKLIST

Before shipping any page, verify at all three primary breakpoints (375px, 768px, 1280px):

- [ ] **Typography readable** — no text smaller than 16px body, headings scale proportionally
- [ ] **Touch targets 44×44px minimum** on mobile — buttons, links, form fields
- [ ] **No horizontal scroll** at any breakpoint
- [ ] **Images don't overflow** container — all images use `max-w-full h-auto`
- [ ] **Grid columns collapse correctly** — 3-col → 2-col → 1-col
- [ ] **Navigation transitions** — hamburger on mobile, full nav on desktop
- [ ] **Forms usable** — labels visible, fields full-width on mobile, appropriate keyboard
- [ ] **CTAs visible** without scrolling at each breakpoint
- [ ] **No false bottoms** — next section always partially visible
- [ ] **Text expansion** — French (+30%) and Kiswahili (+20%) don't break layouts
- [ ] **Safe areas** — no content hidden behind notch or home indicator
- [ ] **Landscape tested** — layouts work when phone is rotated
- [ ] **`prefers-reduced-motion`** — animations disabled when user prefers
- [ ] **Print stylesheet** — page prints cleanly (hide nav, expand columns)
