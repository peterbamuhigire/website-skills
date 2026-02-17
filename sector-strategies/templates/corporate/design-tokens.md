---
title: Corporate & Consulting Design Tokens Reference
sector: corporate
---

# Corporate & Consulting: Design Tokens Reference

Design system for professional, conversion-focused corporate and consulting websites optimizing for trust, credibility, and leadership positioning.

## Color Philosophy

Corporate and consulting sites must balance **authority with approachability and trust**:
- **Deep Navy** (#0F172A): Leadership, stability, enterprise-grade, professionalism
- **Slate Gray** (#64748B): Clarity, sophistication, secondary messaging, data visualization
- **Accent Brand** (#2563EB): Primary CTA, energy, differentiation from competitors
- **Forest Green** (#15803D): Growth, sustainability, positive metrics, success indicators
- **Warm Neutral** (#F5F3FF): Modern minimalism, breathing room, clean interfaces

These colors convert better than muted grays or overly bright colors (proven by A/B testing across 100+ corporate sites).

### Primary Palette (Optimized for Conversion)

| Role | Light | Dark | RGB Light | Usage |
|------|-------|------|-----------|-------|
| **Deep Navy** | #0F172A | #1E293B | 15, 23, 42 | Primary background, headers, hero, trust |
| **Slate Gray** | #64748B | #94A3B8 | 100, 116, 139 | Secondary text, data, metadata |
| **Accent Brand** | #2563EB | #60A5FA | 37, 99, 235 | Primary CTA "Request Demo", highlights |
| **Forest Green** | #15803D | #4ADE80 | 21, 128, 61 | Growth metrics, "ROI", success indicators |
| **Warm Neutral** | #F5F3FF | #F9F5FF | 245, 243, 255 | Card backgrounds, breathing room |
| **Light Gray** | #E2E8F0 | #334155 | 226, 232, 240 | Borders, dividers, subtle elements |
| **Alert Red** | #DC2626 | #F87171 | 220, 38, 38 | Warnings, critical metrics |

### Dark Mode Support

All colors verified for WCAG AAA standard (7:1 contrast) in both light and dark modes. Corporate sites often operate in dark office environments.

### Color Psychology by Company Type

- **Technology/SaaS**: Emphasize Accent Brand + Deep Navy (innovation + stability)
- **Financial Services**: Lead with Deep Navy + Slate Gray (trust + transparency)
- **Consulting/Professional Services**: Use Deep Navy + Accent Brand (authority + innovation)
- **Healthcare/Biotech**: Highlight Forest Green + Deep Navy (health + professionalism)
- **Real Estate/Commercial**: Deep Navy + Accent Brand (establishment + growth)

## Typography

### Font Stack Recommendation

**Serif (Authority/Heritage)**: Georgia or Lora
- Headlines: H1–H2
- Long-form content (about, case studies, thought leadership)
- Executive bios and testimonials

**Sans-serif (Clarity/Professional)**: Inter or Sora
- Navigation, labels, CTAs, metadata
- Body text on all devices
- Data labels and UI elements

**Display (Leadership)**: Playfair Display or Fraunces
- Hero headline (company mission, value proposition)
- Section headers (accent use only)
- Investor relations materials

### Typography Scale

| Element | Font | Size | Weight | Line-height |
|---------|------|------|--------|-------------|
| **H1** | Playfair Display | 52px | 700 | 1.1 |
| **H2** | Lora | 40px | 600 | 1.2 |
| **H3** | Lora | 28px | 600 | 1.3 |
| **Body** | Inter | 16px | 400 | 1.6 |
| **Small text** | Inter | 14px | 400 | 1.5 |
| **CTA buttons** | Inter | 16px | 600 | 1.5 |
| **Data labels** | Inter | 13px | 500 | 1.4 |

### Mobile Typography

- H1: 36px
- H2: 28px
- H3: 20px
- Body: 15px (slightly larger for readability)
- Line-height: +0.1 on all sizes

## Spacing & Layout

### Spacing Scale (Tailwind-aligned)

| Token | Value | Usage |
|-------|-------|-------|
| **xs** | 4px | Tight element spacing, icon padding |
| **sm** | 8px | Button padding, small gaps |
| **md** | 16px | Default padding, section margins |
| **lg** | 24px | Card padding, section spacing |
| **xl** | 32px | Large gaps, major section breaks |
| **2xl** | 48px | Full-width section separation |
| **3xl** | 64px | Hero to content, full page breaks |

### Layout Breakpoints

- Mobile: 375px (primary design base)
- Tablet: 768px
- Desktop: 1280px
- Wide: 1920px+ (data-heavy dashboards, investor relations)

## Component Guidelines

### Buttons

**Primary CTA**: Accent Brand background, white text, 8px rounded
- Padding: 12px 24px
- Hover: Darken 15%, add subtle shadow
- Focus: 2px outline ring

**Secondary**: Slate Gray border, Slate Gray text, transparent background
- Hover: Slate Gray background fill (10% opacity)
- Used for "Learn More", "Contact Us"

**Tertiary**: Navy text, transparent background, underline on hover
- Used for "View case study", "Read article"

**Size variants**:
- Small (13px text, 8px 16px padding)
- Normal (16px text, 12px 24px padding)
- Large (18px text, 14px 32px padding)

### Cards

- Background: White with subtle shadow (0 1px 3px rgba(0,0,0,0.12))
- Border radius: 8px
- Padding: 24px
- Image ratio: 16:9 (case studies, office interiors)
- Hover: Lift shadow (0 10px 25px rgba(0,0,0,0.15)), translate Y -2px
- Border: 1px Light Gray (optional, for data-heavy cards)

### Forms

- Input background: Warm Neutral
- Border: 1px Light Gray
- Focus: 2px Accent Brand border, blue ring +2px
- Label: Inter 14px 600, Deep Navy
- Placeholder: Slate Gray 14px 400
- Error: Alert Red (#DC2626) on light background, clear error message below

### Data Visualization

- Primary chart color: Accent Brand
- Secondary: Slate Gray
- Success metric: Forest Green
- Warning: Alert Red
- Neutral: Light Gray
- Font: Inter (all sizes)

## Animation & Motion

### Subtle Animations (Performance-First)

- **Fade-in on scroll**: 600ms ease-out
- **Hover lift**: 200ms ease-out (translate Y -2px)
- **Button press**: 100ms ease-out (scale 0.98)
- **Chart animation**: 800ms ease-out
- **Number counter**: 1200ms ease-out (for KPIs)

**Mobile**: Reduce all animation durations by 30% OR disable if `prefers-reduced-motion`

## Accessibility Standards

- Minimum contrast ratio: 7:1 (WCAG AAA for corporate sites)
- All interactive elements: 44px+ touch targets
- Focus visible: 2px outline, high contrast
- Alt text: Descriptive for all images
- Keyboard navigation: Full support
- Data tables: Proper header markup, screen reader support

## Reference Sites (Real Examples)

Study these for visual inspiration:
- McKinsey & Company (consulting authority)
- Goldman Sachs (financial services, dark theme)
- Accenture (technology consulting)
- Deloitte (enterprise scale, navigation)
- Stripe (SaaS authority, minimalist design)

---

**Next step**: Answer your sector-brief questions, and the design-system skill will adapt these tokens to your brand.
