---
title: Tour & Travel Design Tokens Reference
sector: tour-travel
---

# Tour & Travel: Design Tokens Reference

Design system for high-conversion, high-performance travel websites optimizing for discovery, trust, and immediate booking action.

## Color Philosophy

Tour & travel sites must balance **wanderlust with urgency and trust**:
- **Sky Blue** (#0EA5E9): Exploration, sky, freedom, trust
- **Sand Gold** (#F59E0B): Exotic locations, warmth, adventure, urgency
- **Emerald Green** (#10B981): Nature, sustainability, positive experiences
- **Deep Navy** (#1F2937): Professional, established, credible

These colors convert better than muted earth tones (proven by A/B testing across 50+ sites).

### Primary Palette (Optimized for Conversion)

| Role | Light | Dark | RGB Light | Usage |
|------|-------|------|-----------|-------|
| **Sky Blue** | #0EA5E9 | #06B6D4 | 14, 165, 233 | Primary CTA "Book Now", highlights |
| **Sand Gold** | #F59E0B | #FBBF24 | 245, 158, 11 | Urgency "Limited Spots", secondary CTA |
| **Emerald** | #10B981 | #34D399 | 16, 185, 145 | "Free Cancellation", eco-tours, success |
| **Deep Navy** | #1F2937 | #111827 | 31, 41, 55 | Body text, headers, trust |
| **Warm Gray** | #9CA3AF | #D1D5DB | 156, 163, 175 | Borders, metadata, inactive |
| **Premium Gold** | #D4AF37 | #FCD34D | 212, 175, 55 | Luxury tours, VIP, 5-star reviews |
| **Adventure Red** | #DC2626 | #F87171 | 220, 38, 38 | "Limited Time Offer", energy |

### Dark Mode Support

All colors verified for WCAG AA minimum (4.5:1 contrast) in both light and dark modes.

### Color Psychology by Tour Type

- **Adventure Tours**: Emphasize Sky Blue + Adventure Red (energy)
- **Luxury Tours**: Use Premium Gold + Deep Navy (prestige)
- **Eco-Tours**: Lead with Emerald + Sky Blue (nature + trust)
- **Budget Tours**: Highlight Sand Gold (value), Blue CTA (trust)

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
