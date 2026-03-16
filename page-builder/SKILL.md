---
name: page-builder
description: Transforms markdown content from docs/{lang}/ into beautiful Astro pages and components. Supports multi-language builds (en, fr, sw). Creates dynamic [lang] routes, language-aware content loading, and language switcher component. Use after design-system and photo-manager have run.
---

# Page Builder Skill

Transform markdown content into stunning, production-grade Astro pages.

## Copywriting Reference

Before writing ANY page copy, read **`references/website-copywriting.md`** for copy formulas and **`references/conversion-design-rules.md`** for layout, CTA, UX anti-pattern rules, 60-30-10 colour rule, SCAMPER differentiation, and dual decision-maker rule. Also read **`blog-writer/references/human-voice-standards.md`** for the AI vocabulary blacklist. All generated text must sound 100% human-written.

**`references/interaction-design-principles.md`** — ISO 9241-110 interaction principles applied to static websites. Use as a checklist when building every page: task suitability, self-descriptiveness, conformity with expectations, learnability, controllability, error robustness, user engagement.

**Persuasion & conversion references** (from `sales-copywriting` skill):
- `sales-copywriting/references/headline-mastery.md` — Read for ALL headlines (10 formulas + 4 U's scoring)
- `sales-copywriting/references/fascination-bullets.md` — Read when writing bullet points that need to persuade
- `sales-copywriting/SKILL.md` — Read FULL skill when building landing pages, sales pages, or product pages

## Universal Guidelines Reference

Before building pages, review these references:

**`universal-guidelines/UNIVERSAL-DESIGN-GUIDELINES.md`** — core standards for every page.

**`universal-guidelines/ux-laws-and-psychology.md`** — apply these on every page:
- **F-Pattern**: place the most important words at the start of every line and paragraph
- **Inverted Pyramid**: most critical information first, always
- **Hick's Law**: limit navigation items, pricing options, and form fields to ≤7
- **Von Restorff**: one primary CTA must look like nothing else on the page
- **Endowed Progress**: show progress bars pre-loaded at 20%; pre-check one onboarding step
- **Law of Proximity**: group related elements; separate unrelated ones by visible space
- **Jakob's Law**: use familiar patterns — never reinvent navigation without reason

**`references/conversion-design-rules.md`** — layout and UX anti-patterns to avoid on every page, plus button anatomy (all 6 states), Flow Theory checklist, and Endowed Progress applications.

This skill applies these universal content and UX principles to Astro implementation.

## Before Building ANY Page

**Read these files first:**
1. `design-tokens.md` — the design system decisions (fonts, colors, patterns)
2. `src/assets/images/_catalog.json` — available photos and their dimensions
3. `docs/{lang}/pages.md` — page structure and navigation for THIS language
4. The specific `docs/{lang}/*.md` file for the page content
5. **Universal Design Guidelines** — for content strategy and UX principles
6. **Language Standards** — tone, grammar, and style for THIS language (from language-standards skill)
7. **Voice DNA** — if the client has existing writing (blog posts, LinkedIn, proposals), build a voice profile before writing any copy (see `blog-writer/references/human-voice-standards.md` — Voice DNA Extraction)

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

## Hard UX Rules (from conversion research)

### No Carousels or Sliders (MANDATORY)

Never use auto-rotating carousels, sliders, or any self-moving content on any page. This includes:
- Homepage header carousels
- Testimonial carousels
- Client logo carousels
- Blog post carousels

**Why:** Carousels rotate faster than visitors can read. Visitors ignore them (banner blindness) or find them annoying. Multiple studies show carousels reduce clicks and conversions. Use static content or tabbed content instead.

**Exception:** A manually controlled image gallery (user clicks arrows) is acceptable for portfolios or product photos.

### No Dropdown Navigation Menus (MANDATORY)

Never use dropdown menus in the main navigation. They:
- Are annoying and hard to use (especially on mobile)
- Cause visitors to skip top-level pages
- Make it harder to find information

**Alternatives:**
- 3-5 services? List them as top-level navigation items
- Many services? Create a dedicated Services overview page with links to each
- About sub-pages (team, story, values)? Combine into one About page

**Exception:** Mobile hamburger menu is fine (it's a toggle, not a hover dropdown). Mega menus are acceptable for e-commerce sites with many product categories.

### Homepage Section Ordering

Homepage sections follow the inverted pyramid — most important information first:

1. **What you do / for whom** — tagline, value proposition (+ photo for solopreneurs, CTA for e-commerce)
2. **Unique selling point** — if not clear from #1, explain why you're different
3. **Credibility** — testimonials, client logos, trust signals, statistics
4. **Overview of offers** — services/products with CTAs to dive deeper
5. **More credibility** — case studies, awards, certifications that support #4
6. **Featured content** — lead magnet, blog posts, or specific offer
7. **Final CTA** — last nudge before footer

**The homepage must NOT simply mirror the navigation.** Don't repeat "About | Services | Blog | Contact" as sections with thin descriptions. Add context, solve problems, build trust.

### CTA Placement Rule

Never place a CTA button before you've given the visitor enough context to want to click it. A CTA asking people to "Contact Us" before explaining what you do is wasted. Place CTAs AFTER:
- Explaining the benefit
- Addressing likely objections
- Providing evidence (testimonial, statistic, case study)

**Homepage exception:** Multiple CTAs are expected on homepages (see ordering above), but each CTA should follow its relevant context section.

### False Bottom Avoidance

A "false bottom" is an area that looks like the end of the page when content continues below. Avoid:
- Full-width coloured sections followed by another full-width section of the same colour
- Large amounts of whitespace between sections
- CTA sections that feel like a natural ending when there's more content below

**Fix:** Ensure visual continuity — alternate section backgrounds, add subtle separators, or use a design element that signals "more below."

### Testimonials in Context (MANDATORY)

Never create a standalone "Testimonials" page. Instead, place testimonials where they support specific claims:
- Homepage: below the value proposition to reinforce trust
- Service pages: next to the service the testimonial references
- About page: reinforcing team credibility
- Contact page: reducing hesitation before reaching out

Each testimonial should reinforce the claim made in the section above it. A testimonial about fast support belongs near the "support" section, not lumped with unrelated quotes.

### Contact Form Simplicity

Contact forms must be as short as possible:
- **Required fields only:** Name, Email, Message (3 fields maximum for initial contact)
- Phone number: optional, with explanation of why you're asking
- No "Subject" dropdown — set it automatically based on page context
- Placeholder text must look different from filled text (grey italic vs black regular)
- Submit button: visually prominent, clear label ("Send Message" not "Submit")
- Never ask for company size, budget, or detailed project info in an initial contact form

---

## Section Patterns

### Hero Sections
Every page gets a hero. Vary the style per page:

- **Homepage hero:** Full-viewport, dramatic. Background image or gradient, large display font headline, subtitle, CTA button. Consider split layout (text left, image right) or full-bleed image with overlay.
- **Inner page hero:** Shorter (40-50vh), page title prominent, optional breadcrumb, background image with overlay.

**MANDATORY:** Every Hero component MUST include a `bgImage` prop with a relevant photograph and an appropriate gradient overlay (e.g. `bg-gradient-to-r from-primary-900/80 to-primary-900/40`). Plain-colour heroes without a background image are not permitted. Select a contextually appropriate photo from `src/assets/images/` for each page.

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

**Always exactly 3 testimonials** in a `grid grid-cols-1 md:grid-cols-3` layout.

**Convention — no real customers exist yet, so generate realistic fictional ones:**
- Use realistic East African names (Ugandan, Kenyan, Tanzanian)
- Use real Ugandan/East African town names for location
- **Never include business names** — only: name, location, industry type
- Each testimonial covers a different industry, sector or service the product serves
- Quotes should reference specific product features relevant to that industry

**TestimonialCard props:** `quote`, `name`, `location`, `type` (no `business` prop).

```astro
<TestimonialCard
  quote="The specific feature changed how I run my business..."
  name="Nakato Grace"
  location="Mbale, Uganda"
  type="Retail"
/>
```

### Screenshots / Product Previews (Lightbox Required)

Screenshots and product images MUST be clickable with a fullscreen lightbox so users can view them at real size. Thumbnails alone don't communicate enough detail.

**Implementation pattern:**

1. **Lightbox component** (`src/components/Lightbox.astro`) — included once per page via BaseLayout. Uses Alpine.js `x-on:open-lightbox.window` to listen for custom events. Renders a fullscreen overlay with close button (X), Escape key, click-outside-to-close, caption bar, and `cursor-zoom-out`.

2. **BaseLayout** includes `<Lightbox />` just before the Alpine.js script tag. This makes the lightbox available on every page automatically.

3. **Screenshot thumbnails** use the `.screenshot-trigger` CSS class and dispatch Alpine events:

```astro
<div
  x-data
  @click="$dispatch('open-lightbox', { src: '/screenshots/FILENAME.jpg', alt: 'Description' })"
  class="rounded-lg overflow-hidden shadow-hero screenshot-trigger"
>
  <img src="/screenshots/FILENAME.jpg" alt="Description" class="w-full h-auto" loading="lazy" />
  <span class="expand-hint">
    <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" />
    </svg>
    Click to enlarge
  </span>
</div>
```

4. **CSS** (in `global.css`) for `.screenshot-trigger`: `cursor: zoom-in`, hover scale, gradient overlay, and `.expand-hint` label that fades in on hover.

5. **French label:** Use "Cliquez pour agrandir" instead of "Click to enlarge". Mobile screenshots: use "Enlarge" / "Agrandir".

**Rules:**
- NEVER show screenshots as static thumbnails — always make them clickable
- Every screenshot container needs `x-data` and `@click="$dispatch('open-lightbox', ...)"`
- The lightbox is zero-dependency (Alpine.js only, no external library)
- Mobile screenshots also get the lightbox treatment

### CTA Sections
Bold, contrasting background. Clear action. One button, one message.

### Contact
- Contact info (from docs/contact.md)
- Simple form (Astro can handle this with form actions or static)
- Embedded map (optional, use iframe)
- Social links

## Nested Border Radius Rule (MANDATORY)

Never round inner elements the same as their parent container. Apply the formula: **outer radius = inner radius + padding**. When a card uses `rounded-2xl` (16px) with `p-4` (16px padding), inner images/buttons/elements must use a smaller radius like `rounded-lg` (8px) or `rounded-xl` (12px). Matching radii on parent and child creates bulgy, uneven corners. Always subtract the gap/padding from the parent radius.

## Image Usage Rules

**ALWAYS use Astro's Image component:**
```astro
---
import { Image } from 'astro:assets';
import heroImg from '../assets/images/hero-office.jpg';
---

<Image
  src={heroImg}
  alt="Descriptive alt text"
  widths={[640, 1024, 1920]}
  sizes="(max-width: 640px) 640px, (max-width: 1024px) 1024px, 1920px"
  loading="lazy"
  class="rounded-xl object-cover"  {/* inner radius < parent card radius */}
/>
```

- Hero images: `loading="eager"` (above the fold)
- Everything else: `loading="lazy"`
- ALWAYS provide descriptive alt text
- ALWAYS use object-cover for background-style images
- Check _catalog.json for available images before using ANY image
- **Image cards MUST NEVER have white space.** Always add `img { display: block; }` in the base layer of global.css. Every image inside a card must use `w-full h-full object-cover` (or `object-contain` for product shots only). The image container must have `overflow-hidden` and a height constraint (`h-full`, `aspect-[ratio]`, or explicit height). Never leave an image at its default inline display — this causes a baseline gap that produces ugly white space at the bottom of cards.

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
- **Element-vs-background contrast check (MANDATORY):** Before using ANY colour class on a button, badge, text, or element, verify that the colour token actually exists in the theme (`global.css` `@theme` block) AND that it contrasts against its parent section background. For example, `bg-amber` does not exist if the theme only defines `bg-amber-500`; an undefined class renders no background, making the element invisible. Always cross-reference the exact token names in `@theme`. On dark backgrounds (navy, sea-800, sea-900), use `bg-highlight` (amber) or `bg-white`; on light backgrounds, use `bg-primary`, `bg-sea-800`, or `bg-navy`.
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

**Always apply the content-writing skill** when creating any page text. That skill defines the full copywriting standard — headlines, ledes, readability, niche vocabulary, scannable formatting, and persuasive structure.

### Copywriting Standards (Mandatory)

All visible text must follow `references/website-copywriting.md` and `blog-writer/references/human-voice-standards.md`:

- **Headlines sell, body explains** — write all headlines first. If headings alone don't tell the story, fix them before writing body text.
- **The Specificity Ladder** — climb from vague to specific. "We help businesses" → "We help East African SMEs" → "We build inventory systems for manufacturers with 50-200 staff"
- **Client language mining** — read every `docs/{lang}/` file and extract the client's own words. The site should sound like the business owner talking.
- **Zero AI vocabulary** — never use: delve, tapestry, landscape (metaphor), leverage, navigate (metaphor), foster, realm, harness, synergy, embark, beacon, robust, vibrant, pivotal, paramount, testament, bolster. See full blacklist in `blog-writer/references/human-voice-standards.md`.
- **Outcome over feature** — "Get paid faster" not "Invoicing module". Apply the "So What?" filter to every sentence.
- **Mirror technique on homepage** — reflect the visitor's reality before talking about the business.

### Scannable Content Formatting

### Quick Reference (from content-writing skill)

- **Headlines**: Benefit-driven, specific, written AFTER content. Five times more people read the headline than the body.
- **Lede**: First 10 words hook the reader. Opening paragraph max 11 words. No throat-clearing.
- **Readability**: Target Fog Index 8-10. Short sentences (avg 15-20 words), short paragraphs (3-4 lines max), vary lengths.
- **Subheads**: Every 2-3 paragraphs. Readers should understand the page by scanning subheads alone.
- **Benefits over features**: Always translate features into reader benefits. Bullet points for features/benefits.
- **Niche vocabulary**: Use topic-specific expert terms naturally — signals authority to readers and search engines.
- **Visuals**: Images every 200-300 words. Captions on all images (read 2x more than body copy).
- **Takeaways**: End blog posts and long pages with 3-5 bulleted key points.
- Bold key terms and phrases. Adequate whitespace between sections.

### Clear Calls-to-Action

Tell users exactly what to do next. See `references/website-copywriting.md` for page-specific CTA formulas.

- Use specific action language ("Discuss Your Project" not "Contact Us", "See How It Works" not "Learn More")
- Make buttons visually distinct (highest contrast)
- Position after value prop and benefits
- Limit 1-2 primary CTAs per section
- CTA wording must be consistent across the site
- Never use manipulative language ("Don't miss out!", "Act now!", "Last chance!")

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
