---
name: page-builder
description: Transforms markdown content from docs/ into beautiful Astro pages and components. Use after design-system and photo-manager have run. Reads design-tokens.md and _catalog.json to ensure visual consistency and proper image usage.
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
3. `docs/pages.md` — page structure and navigation
4. The specific `docs/*.md` file for the page content
5. **Universal Design Guidelines** — for content strategy and UX principles

## Build Order

Always build in this order:
1. `src/layouts/BaseLayout.astro` — the HTML shell
2. `src/components/Header.astro` — navigation
3. `src/components/Footer.astro` — footer
4. Reusable components (Hero, ServiceCard, TeamMember, etc.)
5. Individual pages

## BaseLayout.astro

Must include:
```astro
---
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
  ogImage?: string;
}

const { title, description = '', ogImage = '/og-image.png' } = Astro.props;
const siteTitle = 'Company Name'; // from docs/company-profile.md
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content={description} />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content={ogImage} />
  <title>{title} | {siteTitle}</title>

  <!-- Structured Data -->
  <script type="application/ld+json" set:html={JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": siteTitle,
    // ... from company-profile.md
  })} />
</head>
<body class="font-body text-neutral-900 bg-surface antialiased">
  <Header />
  <main>
    <slot />
  </main>
  <Footer />

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

Must include:
- Company logo/name (from company-profile.md)
- Navigation links (from pages.md nav_order)
- Mobile hamburger menu (Alpine.js)
- CTA button if specified
- Sticky/fixed positioning with backdrop blur
- Clean transition on scroll (background opacity change)

```astro
<!-- Mobile menu with Alpine.js -->
<nav x-data="{ open: false }">
  <!-- Desktop nav -->
  <div class="hidden md:flex">...</div>
  
  <!-- Mobile toggle -->
  <button @click="open = !open" class="md:hidden">...</button>
  
  <!-- Mobile menu -->
  <div x-show="open" x-transition class="md:hidden">...</div>
</nav>
```

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
- Generous padding: `py-20 md:py-28 lg:py-32`
- Max content width: `max-w-7xl mx-auto px-6`
- Use `animate-on-scroll` on section children with stagger classes

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

## Responsive Design Checklist

For EVERY page, mentally verify:

- [ ] **375px (mobile):** Single column, readable text (min 16px), tappable buttons (min 44x44px), no horizontal scroll
- [ ] **768px (tablet):** 2-column grids where appropriate, comfortable spacing
- [ ] **1280px (desktop):** Full layout, max-w-7xl container, generous whitespace
- [ ] **Navigation:** Hamburger on mobile, full nav on desktop
- [ ] **Images:** Responsive srcsets, never wider than viewport
- [ ] **Typography:** Scales up on larger screens (text-4xl md:text-5xl lg:text-6xl)

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

## Content Parsing

When reading docs/*.md files:
- YAML frontmatter (between `---`) = structured data (use as props)
- `## Heading` = section breaks
- `**bold text**` after heading = field values (role, summary, etc.)
- List items = features, values, etc.
- Parse flexibly — the user's markdown won't be perfectly structured
