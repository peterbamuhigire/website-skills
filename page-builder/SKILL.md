---
name: page-builder
description: Transforms markdown content from docs/{lang}/ into beautiful Astro pages and components. Supports multi-language builds (en, fr, sw). Creates dynamic [lang] routes, language-aware content loading, and language switcher component. Use after design-system and photo-manager have run.
---

# Page Builder Skill

Transform markdown content into stunning, production-grade Astro pages.

## Universal Guidelines Reference

Before building pages, review **Universal Design Guidelines** for:
- Visual hierarchy and cognitive load reduction
- Scannable content formatting (headings, lists, short paragraphs)
- Clear CTAs (calls-to-action) and value propositions
- Content strategy and information architecture
- Keyboard navigation and screen reader compatibility
- Mobile-first responsive design approach

This skill applies these universal content and UX principles to Astro implementation.

## Before Building ANY Page

**Read these files first:**
1. `design-tokens.md` — the design system decisions (fonts, colors, patterns)
2. `src/assets/images/_catalog.json` — available photos and their dimensions
3. `docs/{lang}/pages.md` — page structure and navigation for THIS language
4. The specific `docs/{lang}/*.md` file for the page content
5. **Universal Design Guidelines** — for content strategy and UX principles
6. **Language Standards** — tone, grammar, and style for THIS language (from language-standards skill)

**Multi-Language Note:** You are building pages for ONE language at a time. The website-builder will call you once per enabled language. Read content from `docs/{lang}/` (e.g., `docs/en/`, `docs/fr/`, `docs/sw/`), not the root `docs/` directory.

## Build Order

### First Time Only (All Languages)
1. `src/utils/i18n.ts` — language validation and utilities (shared, not language-specific)
2. `src/components/LanguageSwitcher.astro` — language switcher (shared)
3. `src/layouts/BaseLayout.astro` — language-aware HTML shell (shared, accepts lang prop)
4. `src/components/Header.astro` — language-aware navigation (shared, includes LanguageSwitcher)
5. `src/components/Footer.astro` — language-aware footer (shared)
6. Reusable components (Hero, ServiceCard, TeamMember, etc.) — shared across languages

### Per Language
7. Dynamic pages from `src/pages/[lang]/*.astro` — generate once per enabled language
8. Load language-specific content from `docs/{lang}/`
9. Pass lang prop through all components

**Note:** Components are shared across all languages. Content differs per language.

## BaseLayout.astro

Must include language prop and hreflang tags (NEW for i18n):

```astro
---
import '../styles/global.css';
import type { Language } from '../utils/i18n';
import { languages, getHrefLangPath } from '../utils/i18n';

interface Props {
  lang: Language;  // NEW: language code (en, fr, sw)
  title: string;
  description?: string;
  ogImage?: string;
}

const { lang, title, description = '', ogImage = '/og-image.png' } = Astro.props;
const siteTitle = 'Company Name'; // from docs/{lang}/company-profile.md
const currentPath = new URL(Astro.request.url).pathname.replace(/^\/[a-z]{2}/, '') || '/';

// Language label for Open Graph
const langToLocale = (l: Language) => {
  const locales = { en: 'en_GB', fr: 'fr_FR', sw: 'sw_KE' };
  return locales[l];
};
---

<!DOCTYPE html>
<html lang={lang}>  {/* NEW: dynamic lang attribute */}
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content={description} />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content={ogImage} />
  <meta property="og:locale" content={langToLocale(lang)} />  {/* NEW: language variant */}
  <title>{title} | {siteTitle}</title>

  {/* NEW: Hreflang tags for all language versions */}
  {languages.map(langCode => (
    <link
      rel="alternate"
      hreflang={langCode}
      href={`https://example.com${getHrefLangPath(langCode, currentPath)}`}
    />
  ))}
  <link
    rel="alternate"
    hreflang="x-default"
    href={`https://example.com/en${currentPath}`}
  />

  <!-- Structured Data -->
  <script type="application/ld+json" set:html={JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": siteTitle,
    // ... from docs/{lang}/company-profile.md
  })} />
</head>
<body class="font-body text-neutral-900 bg-surface antialiased">
  <Header lang={lang} />  {/* NEW: pass lang to Header */}
  <main>
    <slot />
  </main>
  <Footer lang={lang} />  {/* NEW: pass lang to Footer */}

  <!-- Scroll animation observer -->
  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
  </script>

  <!-- Alpine.js for interactive components -->
  <script>
    import Alpine from 'alpinejs';
    window.Alpine = Alpine;
    Alpine.start();
  </script>
</body>
</html>
```

## Header Component

Must include (language-aware):
- Company logo/name (from docs/{lang}/company-profile.md)
- Navigation links (from docs/{lang}/pages.md nav_order) — language-specific
- Mobile hamburger menu (Alpine.js)
- **Language switcher** (NEW) — LanguageSwitcher component showing en/fr/sw options
- CTA button if specified
- Sticky/fixed positioning with backdrop blur
- Clean transition on scroll (background opacity change)

```astro
---
import type { Language } from '../utils/i18n';
import LanguageSwitcher from './LanguageSwitcher.astro';

interface Props {
  lang: Language;  // NEW: current language
}

const { lang } = Astro.props;
const currentPath = new URL(Astro.request.url).pathname.replace(/^\/[a-z]{2}/, '') || '/';
---

<!-- Mobile menu with Alpine.js -->
<header class="sticky top-0 z-50 bg-white/95 backdrop-blur-lg">
  <nav x-data="{ open: false }" class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
    {/* Logo */}
    <a href={`/${lang}/`}>Logo / Company Name</a>

    {/* Desktop nav */}
    <div class="hidden md:flex gap-8 items-center">
      <a href={`/${lang}/about`}>About</a>
      <a href={`/${lang}/services`}>Services</a>
      {/* More links from pages.md */}
    </div>

    {/* Language Switcher (NEW) */}
    <div class="hidden md:block">
      <LanguageSwitcher currentLang={lang} currentPath={currentPath} />
    </div>

    {/* Mobile toggle */}
    <button @click="open = !open" class="md:hidden">Menu</button>

    {/* Mobile menu */}
    <div x-show="open" x-transition class="absolute top-full left-0 right-0 bg-white md:hidden">
      <a href={`/${lang}/about`}>About</a>
      <a href={`/${lang}/services`}>Services</a>
      {/* Language Switcher in mobile menu */}
      <LanguageSwitcher currentLang={lang} currentPath={currentPath} />
    </div>
  </nav>
</header>
```

**LanguageSwitcher (NEW):** This component is automatically included. It shows language options (English, Français, Kiswahili) and navigates to the same page in the selected language. See i18n/SKILL.md for the component definition.

## Section Patterns

### Hero Sections
Every page gets a hero. Vary the style per page:

- **Homepage hero:** Full-viewport, dramatic. Background image or gradient, large display font headline, subtitle, CTA button. Consider split layout (text left, image right) or full-bleed image with overlay.
- **Inner page hero:** Shorter (40-50vh), page title prominent, optional breadcrumb, subtle background texture or color.

```astro
<!-- Homepage Hero Example -->
<section class="relative min-h-screen flex items-center">
  {heroImage && (
    <Image
      src={heroImage}
      alt="..."
      class="absolute inset-0 w-full h-full object-cover"
      widths={[640, 1024, 1920]}
      loading="eager"
    />
  )}
  <div class="absolute inset-0 bg-gradient-to-r from-primary-900/80 to-primary-900/40" />
  <div class="relative z-10 max-w-7xl mx-auto px-6">
    <h1 class="font-display text-5xl md:text-7xl text-white animate-on-scroll">
      {headline}
    </h1>
  </div>
</section>
```

### Content Sections
- Alternate background colors for visual rhythm (surface → surface-raised → surface)
- Generous padding: `py-20 md:py-28 lg:py-32` (scales across all languages)
- Max content width: `max-w-7xl mx-auto px-6`
- Use `animate-on-scroll` on section children with stagger classes

### Dynamic Routes (NEW for i18n)

All pages are generated under language paths:

```
src/pages/[lang]/
├── index.astro          → /en/, /fr/, /sw/
├── about.astro          → /en/about, /fr/about, /sw/about
├── services.astro       → /en/services, /fr/services, /sw/services
└── [slug].astro         → /en/{slug}, /fr/{slug}, /sw/{slug}
```

**Route Configuration Example:**
```astro
---
export async function getStaticPaths() {
  const languages = ['en', 'fr', 'sw'];
  return languages.map(lang => ({
    params: { lang },
  }));
}

const { lang } = Astro.params;
// Load content from docs/{lang}/company-profile.md
---
```

Content loaded from `docs/{lang}/`, not `docs/`.

### Services/Features Grid
```astro
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
  {services.map((service, i) => (
    <div class={`animate-on-scroll stagger-${i + 1}`}>
      <ServiceCard {...service} />
    </div>
  ))}
</div>
```

### Team Grid
```astro
<div class="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
  {members.map(member => (
    <TeamMember
      name={member.name}
      role={member.role}
      photo={member.photo}  <!-- from catalog -->
      bio={member.bio}
    />
  ))}
</div>
```

### Testimonials
Options: carousel (Alpine.js), grid, or single featured quote.
Use display font for the quote, smaller text for attribution.

### CTA Sections
Bold, contrasting background. Clear action. One button, one message.

### Contact
- Contact info (from docs/contact.md)
- Simple form (Astro can handle this with form actions or static)
- Embedded map (optional, use iframe)
- Social links

## Image Usage Rules

**ALWAYS use Astro's Image component:**
```astro
---
import { Image } from 'astro:assets';
import heroImg from '../assets/images/hero/hero-office.jpg';
---

<Image
  src={heroImg}
  alt="Descriptive alt text"
  widths={[640, 1024, 1920]}
  sizes="(max-width: 640px) 640px, (max-width: 1024px) 1024px, 1920px"
  loading="lazy"
  class="rounded-2xl object-cover"
/>
```

- Hero images: `loading="eager"` (above the fold)
- Everything else: `loading="lazy"`
- ALWAYS provide descriptive alt text
- ALWAYS use object-cover for background-style images
- Check _catalog.json for available images before using ANY image

## Multi-Language Text Expansion (NEW)

French and Kiswahili content will be longer than English. Design with flexibility:

| Language | Expansion | Design Impact |
|----------|-----------|---------------|
| English | 1.0x (baseline) | Base design |
| French | 1.2–1.4x | ~30% longer text |
| Kiswahili | 1.1–1.3x | ~20% longer text |

**Flex Design Principles:**
- Use `min-width` and `max-width`, never fixed widths
- Test all buttons, labels, and CTAs with longer text
- Navigation items must wrap gracefully on smaller screens
- Forms must accommodate longer labels without overlapping inputs
- Avoid text in images (impossible to translate)

**Testing Checklist for Multi-Language:**
- [ ] French button labels don't overflow
- [ ] Kiswahili form labels align properly
- [ ] Navigation items wrap at mobile breakpoints for all languages
- [ ] Hero headlines don't become illegible in French/Kiswahili

## Responsive Design Checklist

For EVERY page in EVERY language, mentally verify:

- [ ] **375px (mobile):** Single column, readable text (min 16px), tappable buttons (min 44x44px), no horizontal scroll, text wraps properly
- [ ] **768px (tablet):** 2-column grids where appropriate, comfortable spacing, French/Kiswahili text fits
- [ ] **1280px (desktop):** Full layout, max-w-7xl container, generous whitespace, buttons/labels flex for longer text
- [ ] **Navigation:** Hamburger on mobile, full nav on desktop, language switcher visible
- [ ] **Images:** Responsive srcsets, never wider than viewport
- [ ] **Typography:** Scales up on larger screens (text-4xl md:text-5xl lg:text-6xl), baseline text readable

## Accessibility Requirements

- Proper heading hierarchy (one h1 per page, sequential h2-h6)
- Alt text on all images
- aria-labels on icon-only buttons
- Focus-visible styles on interactive elements
- Sufficient color contrast (4.5:1 for body text, 3:1 for large text)
- Skip-to-content link in BaseLayout
- Keyboard navigable mobile menu

## Performance Rules

- NO external scripts (no Google Fonts, no analytics CDN, no external JS)
- Fonts self-hosted via Fontsource
- Images optimized via Astro (auto WebP/AVIF)
- Critical CSS inlined by Astro
- Minimal JavaScript — only Alpine.js for interactivity + scroll observer
- Lazy load all below-fold images

## Content Best Practices

### Scannable Content Formatting

Users scan, they don't read. Format all content for quick comprehension:

**Formatting Rules:**
- Descriptive headings (tell story in headlines)
- Bullet points for features/benefits (break up paragraphs)
- Short paragraphs (3-4 lines maximum)
- Bold key terms and phrases
- Images/visuals every 200-300 words
- Adequate whitespace between sections

**Content Structure:**
```
Headline (value prop)
↓
2-3 short paragraphs (context)
↓
Bullet points (benefits/features)
↓
Visual break (image/graphic)
↓
CTA or next section
```

### Clear Calls-to-Action

Tell users exactly what to do next.

**CTA Best Practices:**
- Use action language ("Get Started", "Download", "Subscribe")
- Make buttons visually distinct (highest contrast)
- Position after value prop and benefits
- Limit 1-2 primary CTAs per section
- Include secondary CTA for users not ready

## Content Parsing (Multi-Language)

When reading `docs/{lang}/*.md` files (NEW: language-specific):
- YAML frontmatter (between `---`) = structured data (use as props)
- `## Heading` = section breaks
- `**bold text**` after heading = field values (role, summary, etc.)
- List items = features, values, etc.
- Parse flexibly — the user's markdown won't be perfectly structured

**Important for Multi-Language:**
- Read content from `docs/{lang}/` for THIS language only
- Don't mix languages or read from root `docs/` directory
- Each language has complete independent content
- Apply language standards from language-standards skill to ensure proper tone
- Respect text expansion when designing layouts
