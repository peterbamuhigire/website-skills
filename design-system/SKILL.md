---
name: design-system
description: Establishes the visual foundation for a website — fonts, colors, spacing, animations, and aesthetic direction. Use before building any pages. Reads docs/style-brief.md for brand direction.
---

# Design System Skill

Establish a cohesive, distinctive visual identity for the website before any pages are built.

## Input

Read `docs/style-brief.md` for:
- Industry and brand mood
- Specific color preferences (or let you choose)
- Preferred style direction
- Reference websites they admire

Also read `docs/company-profile.md` for industry context.

## Design Process

### 1. Choose Aesthetic Direction

Based on the industry and brief, commit to ONE bold direction:

| Industry | Good Directions |
|----------|----------------|
| Legal / Finance | Editorial, Luxury, Art Deco, Swiss/Grid |
| Healthcare | Organic, Warm Minimal, Soft Geometric |
| Tech / SaaS | Neo-Brutalist, Bold Geometric, Futuristic |
| Creative Agency | Maximalist, Experimental, Avant-Garde |
| Real Estate | Luxury, Editorial, Warm Modern |
| Education | Playful, Friendly, Colorful Minimal |
| Restaurant / Food | Organic, Warm, Textured, Artisanal |
| Construction | Industrial, Bold, Utilitarian |
| NGO / Non-profit | Warm, Human, Earthy, Hopeful |

**NEVER default to:** purple gradient on white, generic SaaS card layout, Inter + gray + rounded corners.

### 2. Typography

Choose fonts from **Fontsource** (npm packages, self-hosted):

- **Display/Heading font:** Something with CHARACTER. Examples: Clash Display, Cabinet Grotesk, Satoshi, General Sans, Instrument Serif, Playfair Display, DM Serif Display, Sora, Plus Jakarta Sans, Outfit, Manrope
- **Body font:** Highly readable, pairs well. Examples: DM Sans, Nunito Sans, Source Sans 3, Libre Franklin, Atkinson Hyperlegible

Install via: `npm install @fontsource-variable/{font-name}` or `npm install @fontsource/{font-name}`

Import in `src/styles/global.css`:
```css
@import '@fontsource-variable/clash-display';
@import '@fontsource/dm-sans/400.css';
@import '@fontsource/dm-sans/500.css';
@import '@fontsource/dm-sans/700.css';
```

**Rules:**
- NEVER use Inter, Roboto, Arial, system-ui as primary fonts
- NEVER use the same font pair across different projects
- Heading font should feel distinctive; body font should be invisible (easy to read)
- Limit to 2 font families max

### 3. Color Palette

Define in `tailwind.config.mjs`:

```javascript
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '...',
          100: '...',
          // ... full scale 50-950
          DEFAULT: '...',  // 600 or 700 usually
        },
        secondary: { /* ... */ },
        accent: { /* ... */ },
        neutral: { /* ... */ },
        surface: {
          DEFAULT: '...',  // page background
          raised: '...',   // cards, elevated elements
          sunken: '...',   // recessed areas
        }
      },
      fontFamily: {
        display: ['Clash Display Variable', 'sans-serif'],
        body: ['DM Sans', 'sans-serif'],
      },
    }
  }
}
```

**Color rules:**
- Dominant color with sharp accent outperforms evenly-distributed palettes
- Dark backgrounds + light text can feel more premium than white backgrounds
- Use surface colors for depth (not just white and gray)
- Accent color should be used SPARINGLY — for CTAs and key highlights only
- Generate full color scales (50-950) for flexibility

### 4. Global Styles

Create `src/styles/global.css`:

```css
@import 'tailwindcss';

/* Font imports */
@import '@fontsource-variable/...';

/* CSS Custom Properties for non-Tailwind use */
:root {
  --transition-smooth: cubic-bezier(0.4, 0, 0.2, 1);
  --transition-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Selection color matching brand */
::selection {
  background-color: var(--color-primary-200);
  color: var(--color-primary-900);
}

/* Scroll-triggered animation utilities */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s var(--transition-smooth),
              transform 0.6s var(--transition-smooth);
}

.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger delays for groups */
.stagger-1 { transition-delay: 0.1s; }
.stagger-2 { transition-delay: 0.2s; }
.stagger-3 { transition-delay: 0.3s; }
.stagger-4 { transition-delay: 0.4s; }
.stagger-5 { transition-delay: 0.5s; }
```

### 5. Animation Strategy

Use a lightweight Intersection Observer script (add to BaseLayout):

```javascript
// Scroll animation observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
```

For more complex animations (parallax, text reveals), use GSAP:
```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);
```

Only import GSAP where actually needed (Astro island architecture handles this).

### 6. Component Patterns

Document these design decisions for the page-builder to follow:

**Buttons:**
- Primary: solid background, rounded-lg or rounded-full, generous padding
- Secondary: outline or ghost style
- Hover: scale(1.02) + shadow elevation or color shift
- Transition: all 0.2s ease

**Cards:**
- Consistent border-radius (match button radius)
- Subtle shadow or border — not both
- Hover: lift effect (translateY(-4px) + shadow increase)

**Sections:**
- Generous vertical padding (py-20 to py-32)
- Max-width container with comfortable side padding
- Alternating background tones for visual rhythm
- Section headings: display font, large, with a subtle accent element (line, dot, gradient text)

**Images:**
- rounded-lg or rounded-2xl consistently
- object-cover for all background/hero images
- Subtle hover zoom on interactive images

## Universal Guidelines

Before starting design decisions, review **Universal Design Guidelines** for:
- Color theory and accessibility requirements
- Typography scales and readability standards
- Spacing systems and visual hierarchy
- Accessibility standards (WCAG 2.1 AA)
- Mobile-first responsive design approach
- Trust and credibility signals

This skill applies those universal principles to your specific sector/brand.

## Output

Create these files:
1. `tailwind.config.mjs` — with full theme configuration
2. `src/styles/global.css` — with font imports, base styles, animation utilities
3. `design-tokens.md` — a reference document summarizing all design decisions for other skills to read

The `design-tokens.md` should include:
- Aesthetic direction chosen and why
- Font pairing with installation commands
- Color palette with hex values
- Component patterns (buttons, cards, sections)
- Animation approach
- Spacing rhythm
- Do's and Don'ts specific to this project
