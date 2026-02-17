---
title: Tour & Travel Design Tokens Reference
sector: tour-travel
---

# Tour & Travel: Design Tokens Reference

This file provides sector-standard design tokens for tour & travel websites. Use as reference when customizing your `sector-brief.md`. The design-system skill will adapt these to your specific brand.

## Color Philosophy

Tour & travel sites succeed when they evoke **wanderlust and discovery**. Colors should feel:
- Warm and inviting (earth, sunset, stone tones)
- Energizing but not jarring (avoid neon or high-contrast)
- Trustworthy (paired with neutral grounding)

### Primary Palette (Sector Standard)

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Warm Terracotta** | #C97655 | 201, 118, 85 | Primary brand, headers, emphasis |
| **Deep Forest** | #2D5A4F | 45, 90, 79 | Secondary brand, CTAs, trust |
| **Sunset Gold** | #E8B84A | 232, 184, 74 | Accent, highlights, hover states |
| **Cream/Offwhite** | #FAF7F1 | 250, 247, 241 | Background, card backgrounds |
| **Charcoal** | #2C2C2C | 44, 44, 44 | Text, headers |
| **Stone Gray** | #8B8680 | 139, 134, 128 | Secondary text, borders |

### Color Usage Rules

- **Headers**: Charcoal on Cream (high contrast)
- **Body text**: Charcoal on Cream or Stone Gray on Cream
- **CTAs (buttons)**: White text on Deep Forest or Terracotta
- **Hover states**: Shift hue +1, opacity +10%
- **Disabled**: Gray 50%, reduced opacity

### Secondary Palettes (Choose One)

**Warm/Luxe** (for high-end eco-lodges, luxury safaris)
- Burnt sienna, rose gold, deep bronze, warm taupe

**Cool/Adventure** (for younger, active travelers)
- Teal, dusty blue, sage green, cream

**Earthy/Authentic** (for cultural and backpacker tours)
- Rust, olive green, natural linen, charcoal

## Typography

### Font Stack Recommendation

**Serif (Heritage/Trust)**: Lora or Merriweather
- Headlines: H1–H3
- Long-form content (about, blog, testimonials)

**Sans-serif (Clarity/Efficiency)**: Poppins or Sora
- Navigation, labels, CTAs, short copy
- Body text on mobile

**Display (Adventure/Discovery)**: Playfair Display or Fraunces
- Hero headline (one word or short phrase)
- Accent headers

### Typography Scale

| Element | Font | Size | Weight | Line-height |
|---------|------|------|--------|-------------|
| **H1** | Playfair Display | 48px | 700 | 1.2 |
| **H2** | Lora | 36px | 600 | 1.3 |
| **H3** | Lora | 24px | 600 | 1.4 |
| **Body** | Poppins | 16px | 400 | 1.6 |
| **Small text** | Poppins | 14px | 400 | 1.5 |
| **CTA buttons** | Poppins | 16px | 600 | 1.5 |

### Mobile Typography

- H1: 32px
- H2: 24px
- Body: 15px (slightly larger for readability)
- Line-height: +0.1 on all sizes

## Spacing & Layout

### Spacing Scale (Tailwind-aligned)

| Token | Value | Usage |
|-------|-------|-------|
| **xs** | 4px | Icon spacing, tight spacing |
| **sm** | 8px | Padding in buttons, small gaps |
| **md** | 16px | Default padding, small margins |
| **lg** | 24px | Section padding, card spacing |
| **xl** | 32px | Large gaps, section margins |
| **2xl** | 48px | Major section breaks |
| **3xl** | 64px | Full-width section separation |

### Layout Breakpoints

- Mobile: 375px (primary design base)
- Tablet: 768px
- Desktop: 1280px+

## Component Guidelines

### Buttons

**Primary CTA**: Deep Forest background, white text, 12px rounded
- Padding: 12px 24px
- Hover: Darken 10%, add shadow

**Secondary**: Terracotta outline, Terracotta text, transparent background
- Hover: Light Terracotta background fill

**Size variants**:
- Small (12px text, 8px 16px padding)
- Normal (16px text, 12px 24px padding)
- Large (18px text, 14px 32px padding)

### Cards

- Background: White with light shadow (0 2px 8px rgba(0,0,0,0.08))
- Border radius: 8px
- Padding: 24px
- Image ratio: 16:9 (destination photos), 1:1 (experiences/people)
- Hover: Lift shadow (0 8px 16px rgba(0,0,0,0.12)), scale +2%

### Forms

- Input background: Cream
- Border: 1px Stone Gray
- Focus: 2px Deep Forest border, blue ring +2px
- Label: Poppins 14px, Charcoal
- Error: Red #D32F2F on light background

## Animation & Motion

### Subtle Animations (Performance-First)

- **Fade-in on scroll**: 600ms ease-out
- **Hover lift**: 200ms ease-out (translate Y -4px)
- **Button press**: 100ms ease-out (scale 0.98)
- **Image reveal**: 800ms ease-out

**Mobile**: Reduce all animation durations by 30% OR disable if `prefers-reduced-motion`

## Accessibility Standards

- Minimum contrast ratio: 4.5:1 (WCAG AA)
- All interactive elements: 44px+ touch targets
- Focus visible: 2px outline, high contrast
- Alt text: Descriptive for all images
- Keyboard navigation: Full support

## Reference Sites (Real Examples)

Study these for visual inspiration:
- Wilderness Safaris (luxe eco-safari)
- Trafalgar Tours (mature travelers, structured)
- Intrepid Travel (adventure, younger demographic)
- Natural Habitat Adventures (conservation-focused)
- Perenn (design-forward, boutique)

---

**Next step**: Answer your sector-brief questions, and the design-system skill will adapt these tokens to your brand.
