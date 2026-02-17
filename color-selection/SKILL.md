---
name: color-selection
description: Select optimal color palettes for websites using brand colors and color theory. Use when users need to define their website's color scheme, generate complementary palettes, ensure accessibility compliance, or refine existing colors for better visual impact and industry alignment.
---

# Color Selection for Websites

Transform brand colors into cohesive, psychologically-optimized website color palettes that look intentional, professional, and industry-authentic.

## When to Use This Skill

✅ User provides primary brand colors (hex, RGB, or description)
✅ Designing a new website color system
✅ Refining existing colors for better contrast or accessibility
✅ Need complementary accent colors for CTAs, alerts, or secondary elements
✅ Building color tokens for Tailwind config or design system
✅ Ensuring WCAG accessibility compliance (4.5:1 contrast ratio)

## Core Workflow

### 1. Assess Brand Colors

Ask for the user's brand colors. Accept:
- **Hex codes** (e.g., `#3B82F6`)
- **RGB values** (e.g., `rgb(59, 130, 246)`)
- **Color descriptions** (e.g., "deep ocean blue" → convert to hex)
- **Visual examples** (inspect color from uploaded image or screenshot)

Typically users provide 1-3 primary colors. If only one provided, generate complementary palette from it. If multiple provided, evaluate harmony.

### 2. Analyze Color Context

Determine:
- **Industry/sector** (healthcare, e-commerce, finance, creative, education, etc.)
- **Tone** (corporate/conservative, modern/tech, friendly/approachable, luxe/premium)
- **Target audience** (millennials, professionals, children, enterprise clients)
- **Existing brand associations** (does primary color already represent something in their industry?)

**Reference:** See `references/color-psychology.md` for industry-specific color guidance and psychological associations.

### 3. Generate Palette Using Color Theory

Select the most appropriate color scheme based on harmony principles:
- **Monochromatic** — variations of one color (cohesive, safe)
- **Analogous** — adjacent colors on wheel (harmonious, balanced)
- **Complementary** — opposite colors on wheel (high contrast, dynamic)
- **Split-Complementary** — primary + two neighbors of complement (balanced contrast)
- **Triadic** — three evenly-spaced colors (vibrant, playful)
- **Tetradic** — four colors in two complementary pairs (complex, rich)
- **Achromatic** — grays, blacks, whites (timeless, minimalist)

**Reference:** See `references/color-schemes.md` for detailed explanations, HSL adjustments, and scheme-specific guidance.

### 4. Apply 60-30-10 Rule

Distribute colors by visual weight:
- **60%** — Primary color (backgrounds, large surfaces)
- **30%** — Secondary color (supporting elements, sections)
- **10%** — Accent color (CTAs, highlights, alerts)

Example:
```css
--color-primary: #3B82F6;      /* 60% */
--color-secondary: #F3F4F6;    /* 30% */
--color-accent: #DC2626;       /* 10% */
```

### 5. Build Complete System

Generate 5-7 color tokens:
1. **Primary** — primary brand color
2. **Secondary** — supporting color
3. **Accent** — CTA and high-emphasis elements
4. **Success** — positive feedback (green-ish)
5. **Warning** — cautionary feedback (amber-ish)
6. **Error** — destructive/alert feedback (red-ish)
7. **Neutral** — text, borders, backgrounds (grays)

All must meet **WCAG AA standards** (4.5:1 contrast for text, 3:1 for UI components).

**Reference:** See `references/accessibility-contrast.md` for contrast ratio calculation and verification.

### 6. Verify Accessibility

Test each color pair that will be used together:
- **Text on background**: Must be 4.5:1 (normal) or 3:1 (large 18pt+)
- **UI components**: Must be 3:1 (borders, icons, outlines)

Use formula: `(lighter color luminance + 0.05) / (darker color luminance + 0.05)`

Flag any combinations failing WCAG AA. Suggest adjustments (lighten/darken) to achieve compliance.

### 7. Output as Configuration

Provide color tokens as:
- **Tailwind CSS variables** (for `tailwind.config.mjs`)
- **CSS custom properties** (for `global.css`)
- **Design tokens JSON** (for reference)

Example Tailwind:
```javascript
colors: {
  primary: '#3B82F6',
  secondary: '#F3F4F6',
  accent: '#DC2626',
  success: '#10B981',
  warning: '#F59E0B',
  error: '#EF4444',
  neutral: '#6B7280'
}
```

## Industry-Specific Guidance

Before finalizing palette, reference `references/industry-color-psychology.md` for sector-specific expectations:

- **Healthcare/Wellness** — trust blues, calming greens, avoid alarming reds
- **E-Commerce** — action-oriented reds/oranges, trust blues, warm accents
- **Finance/Corporate** — authoritative blues/grays, minimal accent, high contrast
- **Creative/Design** — bold, unexpected colors, high saturation
- **Education** — welcoming blues/greens, accessible contrast
- **Food/Hospitality** — appetite-stimulating warm tones, welcoming accents

## Common Mistakes to Avoid

❌ **Too many colors** — Use no more than 7 token colors; limit primary palette to 3
❌ **Insufficient contrast** — Always test; low contrast fails accessibility and looks cheap
❌ **Color psychology mismatch** — Red for healthcare trust, blue for energy drinks, etc.
❌ **Saturated text** — Never use pure saturated colors for body text; use neutral grays
❌ **Ignoring cultural context** — White = pure in West, mourning in Asia; red = luck in China, alert in US
❌ **No dark mode consideration** — Provide both light and dark palette variants
❌ **Trend-only selection** — Balance 2026 trends with timeless choices for primary colors

## Testing Your Palette

1. **Contrast check**: Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
2. **Accessibility test**: Run palette through [WCAG Color Contrast Checker](https://www.tpgi.com/color-contrast-checker/)
3. **Real application**: Apply to actual website mockup — does it feel right?
4. **Mobile preview**: Colors appear different on different screens; test on actual devices
5. **Colorblind simulation**: Use [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) to see how ~8% of users perceive colors

## Integration with Design System

Once color palette is finalized:
1. Add to `design-tokens.md` (in project)
2. Generate `tailwind.config.mjs` using Design System skill
3. Apply to `src/styles/global.css`
4. Preview on actual pages to verify harmony across all elements

## Reference Files

- `references/color-theory-fundamentals.md` — HSL model, color wheel, temperature, harmony principles
- `references/color-psychology.md` — Color associations, cultural context, emotional impact (80+ associations)
- `references/color-schemes.md` — 7 color schemes with formulas, HSL adjustments, when to use each
- `references/industry-color-psychology.md` — Sector-specific expectations and recommendations
- `references/accessibility-contrast.md` — WCAG standards, contrast calculations, verification tools
- `references/practical-application.md` — Applying palettes to web components, light/dark modes, common UI patterns
- `references/tools-resources.md` — Color picker tools, generators, accessibility checkers

---

**Next Step:** Share your brand colors (hex, RGB, or description) and I'll generate your complete color palette with accessibility verification.
