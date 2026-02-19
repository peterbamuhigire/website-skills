# Website Skills

Claude Code skills for building beautiful, blazing-fast static websites from markdown content and photos.

This repository is designed to be used as a **Git submodule** at `.claude/skills/` in every client website project. All projects share the same skills, and updating this repo propagates improvements to every project.

---

## Architecture

```
website-skills/              ← this repo (submoduled into .claude/skills/)
├── README.md                Documentation (this file)
├── .gitignore
├── new-project.sh           Helper: scaffold a new client project
├── update-skills.sh         Helper: pull latest skills into a project
├── i18n/                    Multi-language infrastructure (3 languages: en, fr, sw)
│   ├── SKILL.md
│   └── docs-i18n-config-template.md
├── language-standards/      Language & tone standards — 3 languages: British English, Francophone French, East African Kiswahili
│   └── SKILL.md
├── brand-alignment/         Ensures site reflects client brand and speaks to ideal customer
│   └── SKILL.md
├── design-reference/        Analyses reference URLs and generates a design guide
│   └── SKILL.md
├── sector-strategies/       Industry-specific website design (9 sectors + app landing pages) with authentic patterns
│   ├── SKILL.md
│   ├── DARK-MODE-IMPLEMENTATION.md
│   ├── templates/
│   │   ├── branding-colors-template.md
│   │   ├── tour-travel/
│   │   ├── corporate-consulting/
│   │   ├── personal-portfolio/
│   │   ├── education/
│   │   ├── healthcare/
│   │   ├── ecommerce/
│   │   ├── professional-services/
│   │   ├── hobbyist-creator/
│   │   ├── nonprofit/
│   │   └── app-landing-pages/      (For app developers — 3 comprehensive guides)
│   └── README.md
├── website-builder/         Master orchestrator — coordinates all other skills
│   └── SKILL.md
├── design-system/           Fonts, colors, visual identity, animation strategy
│   └── SKILL.md
├── page-builder/            Transforms markdown content into Astro pages
│   └── SKILL.md
├── photo-manager/           Catalogs photos, tracks dimensions, auto-detects logos, organizes assets
│   └── SKILL.md
├── seo/                     SEO configuration, meta tags, JSON-LD schema, sitemap
│   ├── SKILL.md
│   └── docs-seo-template.md
├── deploy/                  Builds, verifies, generates deployment configuration
│   └── SKILL.md
├── policy-pages/            Privacy Policies & Terms of Use (legal, trust, compliance)
│   ├── SKILL.md
│   └── references/
├── color-selection/         Color palette design from brand colors using color theory
│   ├── SKILL.md
│   ├── references/          (8 detailed color theory and application guides)
│   └── scripts/
├── skill-writing/           Guide for creating and updating skills (utility)
│   └── SKILL.md
├── skill-safety-audit/      Scans skills for unsafe or malicious instructions (utility)
│   └── SKILL.md
└── update-claude-documentation/  Updates project documentation systematically (utility)
    └── SKILL.md
```

## Skills

### i18n (Multi-Language Infrastructure) — NEW

Establishes complete multi-language support from the start. Every website automatically supports 3 languages: English (en), French (fr), and Kiswahili (sw). Implements path-based URLs (`/en/`, `/fr/`, `/sw/`), generates hreflang tags for SEO, creates language-specific sitemaps, handles text expansion (French ~30% longer, Kiswahili ~20% longer), and orchestrates per-language content builds. Root domain redirects to configured default language. Includes flag-based language switcher (🇬🇧 🇫🇷 🇪🇦) visible on all pages.

**Content Structure:** `docs/{lang}/` with complete independent content per language

**Produces:** `docs/i18n-config.md`, language detection utilities, multi-language sitemaps, hreflang tags

**Applies to:** Content organization, URL routing, sitemap generation, SEO metadata

**Trigger phrases:** "Build a multi-language website", "I need French and Kiswahili support", "Support multiple languages"

### language-standards (Language & Tone Standards)

The foundational writing standard applied to all generated content in all 3 languages. **English:** Authentic East African English as used in Uganda, Kenya, and Tanzania — formal, clear, respectful, British-influenced, professionally courteous. Covers spelling (British), tone (warm but professional), vocabulary (measured, never exaggerated), sentence style, CTAs, country-specific nuances. **French:** Formal francophone African standard (no Québécois variants) with guidance on tu/vous usage and regional vocabulary. **Kiswahili:** Standard East African Kiswahili with formal register, harmony and humility-focused communication, proper noun class agreement. This skill runs alongside every other skill.

**Applies to:** All visible website text in all languages, meta descriptions, alt text, form labels, error messages, CTAs

### brand-alignment (Brand Quality Gate)

Ensures the website functions as a coherent brand experience, not just a collection of pages. Reads company profile and style brief to identify the ideal customer, brand position, and differentiator, then validates that every page — layout, messaging, navigation, imagery, CTAs — serves that audience consistently. Catches common pitfalls: generic messaging, visual inconsistency, buried CTAs, speaking to everyone instead of the right someone.

**Applies to:** Homepage clarity, messaging consistency, visual restraint, navigation flow, CTA alignment, content prioritisation

### design-reference (Reference Site Analyser)

Accepts up to 5 URLs of websites the client admires, visits each one, and extracts design patterns — layout, typography, colour, navigation, animation, imagery, and CTAs. Filters every finding through our tech stack (Astro + Tailwind + Alpine.js), performance budget, and accessibility standards. Produces `docs/design-reference.md`, a structured guide that feeds directly into the design-system and page-builder skills.

**Trigger phrases:** "I like these websites", "Here are some references", "Build something similar to these"

**Produces:** `docs/design-reference.md`

### sector-strategies (Industry-Specific Design Framework)

Guides users to choose a sector (9+ available: tour & travel, corporate & consulting, personal & portfolio, education, healthcare, e-commerce, professional services, hobbyist creator, nonprofit/charity, PLUS app landing pages for developers), then applies proven design patterns, psychology, and trust signals unique to that industry. Each sector includes customization templates, dark/light mode design tokens, component patterns based on exemplary reference sites, and brand color guidance. **App landing pages sector is optimized for conversion frameworks, A/B testing, and mobile-first design** — for app developers building their own landing pages.

**Sectors:** Tour & Travel, Corporate & Consulting, Personal & Portfolio, Education, Healthcare, E-commerce, Professional Services, Hobbyist Creator, Nonprofit/Charity/NGO, **App Landing Pages** (new)

**Features:** Full dark/light mode support, automatic logo detection and selection, branding color documentation with WCAG accessibility compliance, 10+ pre-designed industry-specific components, 800+ line education implementation guide, comprehensive nonprofit dark mode support, **app landing page conversion frameworks (AIDA, PAS, FAB, Hero's Journey), complete A/B testing strategy, performance optimization guide**

**Trigger phrases:** "I want this to look like a school website", "This is a tour company", "Make it nonprofit-friendly", "Dark mode support", "Professional services firm", **"Build an app landing page", "I need a landing page for my app"**

**Produces:** `docs/sector-brief.md`, branding color configuration, dark mode setup

### website-builder (Orchestrator)

The entry point. When Claude is told to "build this website", this skill reads `docs/i18n-config.md` to detect enabled languages, then reads language-specific content from `docs/{lang}/`, scans photos in `photo-bank/`, and coordinates the other skills in order: design-system → photo-manager → page-builder → seo → deploy. Automatically builds all enabled language versions.

**Trigger phrases:** "Build this website", "Create a site", "Rebuild the site"

### design-system (Visual Foundation)

Establishes the complete visual identity before any pages are built. Reads `docs/style-brief.md` to determine mood, industry, and color preferences. Selects distinctive fonts from Fontsource (never Inter/Roboto/Arial), generates a full color palette, defines component patterns, and commits to a specific aesthetic direction.

**Produces:** `tailwind.config.mjs`, `src/styles/global.css`, `design-tokens.md`

### photo-manager (Image Pipeline)

Scans `photo-bank/`, measures every photo's dimensions with ImageMagick or PIL, copies them to organized `src/assets/images/{category}/` folders, and generates `_catalog.json` — a master registry tracking dimensions, aspect ratios, usage, and replacement notes for every image. **Auto-detects the best logo** from files containing "logo" in the filename (scores by resolution, format, dimensions) and copies it to `src/assets/images/branding/logo.png`. **Recognizes descriptive photo names** (e.g., `Logo-Light-Mode.png`, `Staff-Members.jpg`, `Government-License.jpg`) to automatically categorize and appropriately place photos throughout the site.

**Produces:** `src/assets/images/*/`, `src/assets/images/branding/logo.png`, `src/assets/images/_catalog.json`

### page-builder (Content → Pages)

Reads markdown content from `docs/{lang}/` for each enabled language, the design tokens, and the photo catalog, then generates Astro pages and reusable components. Creates dynamic `[lang]` routes for multi-language support. Builds mobile-first with scroll animations, Alpine.js interactivity, proper SEO meta tags, language-aware text expansion, and accessibility compliance. Includes LanguageSwitcher component.

**Produces:** `src/layouts/`, `src/components/`, `src/pages/[lang]/`, `src/utils/i18n.ts`

### seo (Search Engine Optimization — Multi-Language)

Implements a 4-layer SEO architecture: (1) **Technical SEO** — multi-language sitemap generation (sitemap-en.xml, sitemap-fr.xml, sitemap-sw.xml), hreflang tags pointing to all language versions, robots.txt, canonical URLs; (2) **On-Page SEO** — per-page, per-language meta tags (title 50-60 chars, description 150-160 chars) read from `docs/{lang}/seo.md`; (3) **Structured Data** — JSON-LD schema generation for Organization, WebSite, WebPage, BreadcrumbList, Service, Person, FAQPage with language variants; (4) **Off-Page** — post-launch manual checklist for Google Business Profile, directory submissions, review requests per language.

**Produces:** Hreflang tags in BaseLayout, language-specific meta tags, JSON-LD schemas in src/utils/schema.ts, language-specific sitemaps, sitemap-index.xml, `public/robots.txt`, `seo-audit.md` report

**Integrates during:** deploy step as pre-build configuration

### deploy (Build & Ship — Multi-Language)

Runs `npm run build`, verifies output for all language versions, checks for broken references, and generates `deploy.sh` and language-aware `nginx.conf` with aggressive caching headers and root domain redirect. Outputs a comprehensive multi-language pre-launch checklist. Verifies hreflang tags, language-specific sitemaps, and per-language Lighthouse scores.

**Produces:** `dist/{en,fr,sw}/`, `deploy.sh`, `nginx.conf` (with root redirect and language routing)

### policy-pages (Legal — Privacy & Terms)

Designs Privacy Policies and Terms of Use that are legally compliant, user-friendly, accessible, and build trust. Covers 15 essential elements for each document with jurisdiction-specific requirements (GDPR, CCPA, COPPA, PIPEDA, LGPD, Privacy Act 1988, PECR). Emphasizes plain language, visual hierarchy, mobile optimization, and version control. Every website must have both documents.

**Reference Files:** `privacy-policy-detailed.md` (737 lines), `terms-of-use-detailed.md` (925 lines)

**Jurisdictions Covered:** EU (GDPR), US (CCPA/COPRA, COPPA), Canada (PIPEDA), Brazil (LGPD), Australia (Privacy Act), Asia-Pacific (PDPA)

**Produces:** Privacy Policy page, Terms of Use page (customized to client's jurisdiction and business model)

### color-selection (Color Palette Design)

Transforms brand colors into harmonious, psychologically-optimized website color palettes using color theory principles. Takes user's primary brand color(s), applies the 7 fundamental color schemes (monochromatic, analogous, complementary, split-complementary, triadic, tetradic, achromatic), validates WCAG accessibility compliance (4.5:1 contrast for text, 3:1 for UI components), and generates complete semantic palette with feedback colors (success, warning, error, info).

**Reference Files:** `color-theory-fundamentals.md`, `color-psychology.md`, `color-schemes.md`, `industry-color-psychology.md`, `accessibility-contrast.md`, `practical-application.md`, `tools-resources.md`

**Scripts:** `palette_generator.py` — generates any color scheme from hex color; supports monochromatic, analogous, complementary, split-complementary, triadic, tetradic, tints/shades, and semantic palettes

**Features:** Full color theory coverage (HSL model, temperature, psychology), industry-specific guidance (healthcare, finance, e-commerce, tech, education, F&B, professional services, creative, nonprofits), colorblind accessibility checking, dark mode palette generation, real-world component examples, accessibility audit checklist, tools directory with 15+ online resources

**Produces:** Complete color palette with semantic tokens, CSS variables, Tailwind config format, WCAG compliance report, industry-specific recommendations

**Trigger phrases:** "Design a color palette", "Generate colors from my brand color", "What colors should we use?", "Help with color scheme"

### skill-writing (Utility — Skill Creation Guide)

Guide for creating effective skills. Covers skill anatomy (YAML frontmatter, body, bundled resources), progressive disclosure design, the 500-line hard limit, and a six-step creation process. Use when creating or updating any SKILL.md in this repo.

### skill-safety-audit (Utility — Security Gate)

Scans new or updated skills for unsafe instructions — unknown installers, credential harvesting, unauthorized network actions, shadow dependencies, and hidden commands in bundled resources. Every new or changed skill must be audited before acceptance.

### update-claude-documentation (Utility — Documentation Updater)

Systematically updates project documentation (README.md, CLAUDE.md, and related files) after significant changes. Ensures consistency across all docs, maps changes to affected files, and enforces the 500-line hard limit on all markdown files.

---

## Execution Order

Skills must run in this order — each depends on outputs from the previous:

```
i18n                        ← mandatory first step (detects enabled languages: en, fr, sw)
language-standards          ← active throughout (multi-language tone & style guide)
brand-alignment             ← active throughout (brand coherence quality gate)
design-reference            ← optional first step (if client provides reference URLs)
sector-strategies           ← optional step 0.5 (if starting from sector template)
        ↓
  docs/i18n-config.md (detected)
  docs/{lang}/design-reference.md or docs/sector-brief.md
        ↓
website-builder
  ├── 1. design-system      → tailwind.config, global.css, design-tokens.md (shared)
  ├── 2. photo-manager      → src/assets/images/, branding/logo.png, _catalog.json (shared)
  ├── 3. page-builder       → src/pages/[lang]/, src/components/, src/layouts/ (per-language)
  ├── 4. seo (integrates)   → hreflang tags, multi-lang sitemaps, locale meta tags
  └── 5. deploy             → dist/{en,fr,sw}/, deploy.sh, nginx.conf (multi-language)

Utility skills (not part of the build pipeline):
  policy-pages               ← use when creating Privacy Policy and Terms of Use pages (per-language)
  color-selection            ← use when defining color palettes (shared across languages)
  skill-writing              ← use when creating/updating any SKILL.md
  skill-safety-audit         ← mandatory audit before accepting new/changed skills
  update-claude-documentation← use after significant changes to update all docs
```

---

## Tech Stack

These skills generate websites using:

| Technology | Role |
|-----------|------|
| [Astro](https://astro.build) | Static site generator (zero JS by default) |
| [Tailwind CSS v4](https://tailwindcss.com) | Utility-first styling |
| [Alpine.js](https://alpinejs.dev) | Lightweight interactivity (17KB) |
| [GSAP](https://gsap.com) | Scroll-triggered animations (optional) |
| [Fontsource](https://fontsource.org) | Self-hosted fonts |
| [Lucide](https://lucide.dev) | SVG icons |

---

## Usage as Submodule

### Creating a new project (recommended)

Use the included `new-project.sh` script to scaffold a complete client project:

```bash
# Clone this repo (or keep it somewhere convenient)
git clone https://github.com/peterbamuhigire/website-skills.git
cd website-skills

# Scaffold a new project
chmod +x new-project.sh
./new-project.sh acme-corp

# Or with a remote already set up:
./new-project.sh acme-corp git@github.com:yourorg/acme-corp.git
```

This creates a ready-to-go project with the submodule wired up, all docs templates, photo-bank, CLAUDE.md, and an initial commit.

### Adding to an existing project manually

```bash
cd existing-project
git submodule add https://github.com/peterbamuhigire/website-skills.git .claude/skills
git add .
git commit -m "Add website-skills submodule"
```

### Cloning a project that has the submodule

```bash
# Option A: Clone with submodules in one step
git clone --recurse-submodules https://github.com/yourorg/client-project.git

# Option B: If you already cloned without submodules
cd client-project
git submodule init
git submodule update
```

### Updating skills in a project

Use the included `update-skills.sh` script:

```bash
# Copy it into your project (one-time)
cp /path/to/website-skills/update-skills.sh ./update-skills.sh

# Run it
chmod +x update-skills.sh
./update-skills.sh
```

Or manually:

```bash
cd client-project
git submodule update --remote .claude/skills
git add .claude/skills
git commit -m "Update website skills to latest"
git push
```

### Updating ALL client projects at once

```bash
# If all your projects are in a clients/ folder:
for project in clients/*/; do
  echo "=== Updating $project ==="
  (cd "$project" && git submodule update --remote .claude/skills \
    && git add .claude/skills \
    && git commit -m "Update website skills" \
    && git push) || echo "  Skipped (no changes or error)"
done
```

---

## Project Structure (Client Side)

Every client project that uses these skills should have this structure:

```
client-project/
├── CLAUDE.md                  # Project intelligence for Claude Code
├── .gitmodules                # Auto-generated, references this repo
├── .claude/
│   └── skills/                # ← THIS REPO (submodule)
│       ├── east-african-english/
│       ├── brand-alignment/
│       ├── design-reference/
│       ├── website-builder/
│       ├── design-system/
│       ├── page-builder/
│       ├── photo-manager/
│       ├── deploy/
│       ├── skill-writing/
│       ├── skill-safety-audit/
│       └── update-claude-documentation/
├── docs/                      # Client content (markdown)
│   ├── company-profile.md
│   ├── services.md
│   ├── team.md
│   ├── testimonials.md
│   ├── contact.md
│   ├── faq.md
│   ├── style-brief.md
│   └── pages.md
├── photo-bank/                # Raw client photos
└── src/                       # Generated by Claude Code
```

Use `new-project.sh` to create a new project with this structure, or set it up manually.

---

## Photo Naming Convention

To help Claude automatically identify and use photos appropriately, encourage clients to use **descriptive, purpose-specific filenames** instead of generic names like `IMG_001.jpg` or `photo1.png`.

### Good Photo Names (Descriptive)

Claude can immediately understand purpose and placement:

```
Branding/
├── Logo-Light-Mode.png
├── Logo-Dark-Mode.png
├── Favicon.svg
└── Brand-Icon.png

Team/
├── Staff-Members.jpg (group photo)
├── CEO-Headshot.jpg
├── Developer-Alice.jpg
├── Designer-Bob.jpg
└── Manager-Carol.jpg

Content/
├── Hero-Office-Team.jpg
├── Product-Feature-Screenshot.png
├── Testimonial-Client-John.jpg
└── Case-Study-Results-Dashboard.png

Certifications/
├── Government-License.jpg
├── ISO-Certification.png
└── Industry-Award-Badge.jpg

Gallery & Slideshows/
├── Gallery-Project-01.jpg
├── Gallery-Project-02.jpg
├── Portfolio-Website-Redesign.jpg
├── Slide-Product-Demo-01.jpg
├── Slide-Product-Demo-02.jpg
└── Carousel-Client-Testimonials.jpg

Social & Culture/
├── Team-Retreat-Event.jpg
├── Office-Culture-Photo.jpg
└── Product-Launch-Celebration.jpg
```

### What Claude Recognizes

Descriptive names enable Claude to:

| Name Pattern | Claude Identifies | Automatic Usage |
|-------------|------------------|-----------------|
| `*Logo*`, `*logo*` | Company branding | Header, footer, favicon |
| `*Headshot*`, `*headshot*` | Team member photos | Team section grid |
| `*Hero*`, `*banner*` | Full-width hero images | Page hero sections |
| `*Testimonial*`, `*quote*` | Client/user quotes | Testimonials section |
| `*Staff*`, `*Team*`, `*Members*` | Group photos | Team page introduction |
| `*Certificate*`, `*License*`, `*Award*` | Credentials | Trust/credibility section |
| `*Feature*`, `*Screenshot*` | Product features | Features grid |
| `*Culture*`, `*Event*`, `*Retreat*` | Behind-the-scenes | About section, culture |
| `*Case-Study*`, `*Before-After*` | Results/proof | Case studies section |
| `*Gallery*`, `*portfolio*` | Photo gallery collection | Photo gallery pages (multiple images) |
| `*Slide*`, `*carousel*` | Slideshow candidates | Slideshow/carousel sections |

### Photo Naming Best Practices

1. **Use hyphens, not underscores** — `Logo-Dark-Mode.png` not `Logo_dark_mode.png`
2. **Capitalize key words** — `CEO-Headshot.jpg` not `ceo-headshot.jpg`
3. **Specific > Generic** — `Developer-Alice.jpg` not `team-photo.jpg`
4. **Include mode/variant** — `Logo-Light-Mode.png`, `Logo-Dark-Mode.png` (allows automatic selection)
5. **Describe purpose** — `Hero-Product-Launch.jpg` not `IMG_001.jpg`
6. **One purpose per file** — Don't combine: `Logo-And-Favicon.png` → split to `Logo.png` and `Favicon.svg`

### How Claude Uses These Names

1. **Photo Manager** scans `photo-bank/` and reads all filenames
2. **Catalogs** each photo with its recognized purpose
3. **Page Builder** reads the catalog and places photos intelligently:
   - Logo files → header/footer
   - Headshots → team section
   - Hero images → page heroes
   - Testimonial photos → testimonials section
4. **No manual placement needed** — Claude understands intent from naming alone

---

## Design Principles

These skills enforce several hard rules:

1. **Zero unnecessary JavaScript.** Astro ships no JS by default. Alpine.js only for interactive elements.
2. **Self-host everything.** No external CDN requests for fonts, scripts, or analytics.
3. **Every site looks different.** Skills choose distinctive fonts, bold color palettes, and varied aesthetics per industry — never generic SaaS templates.
4. **Photos are dimension-aware and intelligently named.** Every image is measured before placement. No upscaling, no broken aspect ratios. Users encourage descriptive photo names (e.g., `Logo-Light-Mode.png`, `Staff-Members.jpg`, `Testimonial-Alice.jpg`, `Hero-Product-Image.jpg`) so Claude can automatically identify photo purpose and appropriate placement without asking.
5. **Content is truth.** All text comes from `docs/` markdown. Claude never fabricates company information.
6. **Mobile-first, always.** Designed for 375px, enhanced for 768px and 1280px+.
7. **Accessibility is required.** Proper heading hierarchy, alt text, ARIA labels, color contrast, keyboard navigation.
8. **Performance by default.** Target 95+ Lighthouse across all categories, under 500KB first load.

---

## Contributing / Improving Skills

When you find a pattern that works well (or doesn't), update the relevant SKILL.md:

1. Make changes in this repo
2. Run **skill-safety-audit** on any new or modified skill
3. Test with a real client project
4. Run **update-claude-documentation** to update README.md and CLAUDE.md
5. Push to main
6. Update submodules in active projects

When creating a new skill, follow the **skill-writing** guide for structure, frontmatter, and the 500-line hard limit.

Skill files use YAML frontmatter for metadata (name, description) and markdown for instructions. Claude Code reads the full file when the skill is invoked.

---

## Changelog

Track significant skill improvements here.

| Date | Skill | Change |
|------|-------|--------|
| 2026-02-17 | all | Initial release — 5 skills for Astro + Tailwind static sites |
| 2026-02-17 | east-african-english | Added language & tone standard for Uganda, Kenya, Tanzania |
| 2026-02-17 | brand-alignment | Added brand coherence quality gate for client websites |
| 2026-02-17 | design-reference | Added reference URL analyser — generates design guide from client-liked sites |
| 2026-02-17 | skill-writing | Added skill creation guide (utility) |
| 2026-02-17 | skill-safety-audit | Added security audit gate for new/changed skills (utility) |
| 2026-02-17 | update-claude-documentation | Added documentation updater (utility) |
| 2026-02-17 | sector-strategies | Added 7-sector industry-specific design framework (tour, education, healthcare, ecommerce, professional-services, hobbyist-creator, nonprofit) with full dark/light mode support, logo detection, branding colors, and 100+ component patterns |
| 2026-02-17 | photo-manager | Enhanced with automatic logo detection algorithm (scores by resolution, format, dimensions) and dedicated branding directory |
| 2026-02-17 | seo | Added comprehensive 4-layer SEO architecture (technical, on-page, structured data, off-page) with JSON-LD schema generation and audit reporting |
| 2026-02-17 | policy-pages | Added comprehensive Privacy Policy and Terms of Use skill (legally compliant, user-friendly, accessible); covers GDPR, CCPA, COPPA, PIPEDA, LGPD, Privacy Act 1988, PECR with jurisdiction-specific requirements and plain language principles |
| 2026-02-17 | photo-manager | Enhanced with photo naming convention recognition (descriptive filenames for auto-categorization); supports Gallery/Portfolio and Slide/Carousel patterns for automatic multi-image gallery and slideshow creation |
| 2026-02-17 | all | Added photo naming guidelines encouraging descriptive filenames (Logo-Light-Mode.png, Staff-Members.jpg, Gallery-Project-01.jpg, Slide-Feature-01.jpg) for automatic identification and placement without manual clarification |

---

## License

Private. For internal use across website projects.
