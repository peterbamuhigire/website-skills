# Website Skills

Claude Code skills for building beautiful, blazing-fast static websites from markdown content and photos.

This repository is designed to be used as a **Git submodule** at `.claude/skills/` in every client website project. All projects share the same skills, and updating this repo propagates improvements to every project.

---

## Architecture

```
website-skills/              ← this repo (submoduled into .claude/skills/)
├── README.md                Documentation (this file)
├── .gitignore
├── new-project.sh           Helper: scaffold a new client project (Linux/macOS)
├── new-project.ps1          Helper: scaffold a new client project (Windows)
├── prompts/                 Project-specific content generation prompts
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
│   ├── SKILL.md
│   └── references/          (website copywriting formulas)
├── photo-manager/           Catalogs photos, tracks dimensions, auto-detects logos, organizes assets
│   └── SKILL.md
├── seo/                     SEO configuration, meta tags, JSON-LD schema, sitemap
│   ├── SKILL.md
│   └── docs-seo-template.md
├── blog-writer/             SEO-ready bilingual blog articles with format templates and quality gates
│   ├── SKILL.md
│   └── references/          (9 writing craft, voice standards, content strategy, and format guides)
├── deploy/                  Builds, verifies, generates deployment configuration
│   └── SKILL.md
├── blog-idea-generator/     Adaptive 20-method ideation → 15-25 blog ideas with 200-word summaries
│   ├── SKILL.md
│   └── references/          (ideation frameworks, content formats)
├── policy-pages/            Privacy Policies & Terms of Use (legal, trust, compliance)
│   ├── SKILL.md
│   └── references/
├── seo-audit/               Post-build SEO audit (14 categories, scored report)
│   ├── SKILL.md
│   └── references/          (audit checklist, keyword research, local SEO, measurement)
├── email-sender/            PHP + PHPMailer self-hosted contact form handler
│   └── SKILL.md
├── image-compression/       Build-time image compression via Sharp (photo-manager pipeline)
│   └── SKILL.md
├── color-selection/         Color palette design from brand colors using color theory
│   ├── SKILL.md
│   ├── references/          (8 detailed color theory and application guides)
│   └── scripts/
├── sales-copywriting/       Persuasion and conversion copywriting (hybrid cross-cutting + on-demand)
│   ├── SKILL.md
│   └── references/          (5 reference guides: headlines, bullets, resistance, PASTOR/4Ps, closing)
├── east-african-english/    English-only language standard (legacy — see language-standards)
│   └── SKILL.md
├── skill-writing/           Guide for creating and updating skills (utility)
│   └── SKILL.md
├── skill-safety-audit/      Scans skills for unsafe or malicious instructions (utility)
│   └── SKILL.md
└── update-claude-documentation/  Updates project documentation systematically (utility)
    └── SKILL.md
```

## Skills

### i18n (Multi-Language Infrastructure) — NEW

Establishes complete multi-language support from the start. Every website automatically supports 3 languages: English (en), French (fr), and Kiswahili (sw). Implements path-based URLs (`/en/`, `/fr/`, `/sw/`), generates hreflang tags for SEO, creates language-specific sitemaps, handles text expansion (French ~30% longer, Kiswahili ~20% longer), and orchestrates per-language content builds. The root domain (`/`) is served by a lightweight Astro redirect page that detects browser language and sends visitors to the best language version, with default-language fallback when detection does not match. Includes flag-based language switcher (🇬🇧 🇫🇷 🇪🇦) visible on all pages.

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

**Sectors:** Tour & Travel, Corporate & Consulting, Personal & Portfolio, Education, Healthcare, E-commerce, Professional Services, Hobbyist Creator, Nonprofit/Charity/NGO, App Landing Pages

**Features:** Dark/light mode, logo detection, WCAG branding colors, 10+ industry components, conversion frameworks (AIDA, PAS, FAB)

**Produces:** `docs/sector-brief.md`, branding color configuration, dark mode setup

### website-builder (Orchestrator)

The entry point. When Claude is told to "build this website", this skill reads `docs/i18n-config.md` to detect enabled languages, then reads language-specific content from `docs/{lang}/`, scans photos in `photo-bank/`, and coordinates the other skills in order: design-system → photo-manager → page-builder → seo → deploy. Automatically builds all enabled language versions.

**Trigger phrases:** "Build this website", "Create a site", "Rebuild the site"

### design-system (Visual Foundation)

Establishes the complete visual identity before any pages are built. Reads `docs/style-brief.md` to determine mood, industry, and color preferences. Selects distinctive fonts from Fontsource (never Inter/Roboto/Arial), generates a full color palette, defines component patterns, and commits to a specific aesthetic direction.

**Produces:** `tailwind.config.mjs`, `src/styles/global.css`, `design-tokens.md`

### photo-manager (Image Pipeline)

Scans `photo-bank/`, measures every photo's dimensions with ImageMagick or PIL, copies them into a **single flat** `src/assets/images/` directory, and generates `_catalog.json` — the source of truth for category, role, dimensions, aspect ratios, usage, and replacement notes. **Auto-detects the best logo** from files containing "logo" in the filename (scores by resolution, format, dimensions) and copies it to `src/assets/images/logo.png`. **Recognizes descriptive photo names** (e.g., `Logo-Light-Mode.png`, `Staff-Members.jpg`, `Government-License.jpg`) to automatically categorize and appropriately place photos through catalog metadata, not folder structure.

**Produces:** `src/assets/images/*`, `src/assets/images/logo.png`, `src/assets/images/_catalog.json`

### page-builder (Content → Pages)

Reads markdown content from `docs/{lang}/` for each enabled language, the design tokens, and the photo catalog, then generates Astro pages and reusable components. Creates dynamic `[lang]` routes for multi-language support. Builds mobile-first with scroll animations, Alpine.js interactivity, proper SEO meta tags, language-aware text expansion, and accessibility compliance. Includes LanguageSwitcher component.

**Produces:** `src/layouts/`, `src/components/`, `src/pages/[lang]/`, `src/utils/i18n.ts`

### seo (Search Engine Optimization — Multi-Language)

Implements a 4-layer SEO architecture: (1) **Technical SEO** — multi-language sitemap generation (sitemap-en.xml, sitemap-fr.xml, sitemap-sw.xml), hreflang tags pointing to all language versions, robots.txt, canonical URLs; (2) **On-Page SEO** — per-page, per-language meta tags (title 50-60 chars, description 150-160 chars) read from `docs/{lang}/seo.md`; (3) **Structured Data** — JSON-LD schema generation for Organization, WebSite, WebPage, BreadcrumbList, Service, Person, FAQPage with language variants; (4) **Off-Page** — post-launch manual checklist for Google Business Profile, directory submissions, review requests per language.

**Produces:** Hreflang tags in BaseLayout, language-specific meta tags, JSON-LD schemas in src/utils/schema.ts, language-specific sitemaps, sitemap-index.xml, `public/robots.txt`, `seo-audit.md` report

**Integrates during:** deploy step as pre-build configuration

### deploy (Build & Ship — Multi-Language)

Runs `npm run build`, verifies output for all language versions, checks for broken references, and generates `deploy.sh` and language-aware `nginx.conf` with aggressive caching headers and language-aware routing. The web server must serve the generated Astro root page at `/` so browser-language detection can run there. Outputs a comprehensive multi-language pre-launch checklist. Verifies hreflang tags, language-specific sitemaps, and per-language Lighthouse scores.

**Produces:** `dist/{en,fr,sw}/`, `deploy.sh`, `nginx.conf` (with root-page preservation at `/` and language routing)

### blog-writer (Content Marketing — Blog Articles)

Generates SEO-ready bilingual blog articles with featured images, in-article photography, and distinctive per-article design. Each article is a marketing asset — a demonstration of expertise that builds trust and attracts clients through organic search. Step 0 reads idea summaries from blog-idea-generator (audience, format, angle, SEO keywords); 7 format-specific structural templates (How-to, Case study, List, Opinion, Guide, Story, Comparison) guide article structure; quality gate verifies alignment before design. Reads company profile for author voice, scans photo-bank for article images, creates content in `docs/{lang}/blog/`, builds Astro blog pages with Article JSON-LD, and updates the blog index.

**Reference Files:** `human-voice-standards.md`, `writing-craft.md` (+ 7 format templates), `content-strategy.md` (+ calendar planning, seasonal mapping, cross-language planning), `reader-experience.md`, `storytelling.md`, `editorial-standards.md`, `article-design.md`, `ideation-and-research.md`, `topic-ideas.md`

**Produces:** Blog articles in `docs/{lang}/blog/`, Astro pages in `src/pages/{lang}/blog/`, Article JSON-LD, updated blog index

**Trigger phrases:** "Write a blog article", "Create a blog post", "Write about [topic]", "Add content to the blog"

### seo-audit (Post-Build SEO Audit)

Comprehensive SEO audit for static websites. Analyses 14 categories — technical SEO, on-page, content quality, structured data, pagespeed & performance, mobile usability, local SEO, internal linking, security & trust, accessibility, competitive positioning, voice search readiness, off-page signals, and SEO measurement. Produces a scored audit report with prioritised action items. Run after deploy or on demand.

**Reference Files:** `audit-checklist.md` (detailed per-check explanations), `keyword-research.md` (long-tail, voice search, intent mapping), `local-seo-guide.md` (Google Business Profile, citations, reviews), `seo-measurement-guide.md` (KPI framework, traffic/conversion benchmarks)

**Produces:** Scored audit report with category breakdowns and prioritised action plan

**Trigger phrases:** "Audit my SEO", "How is my SEO?", "Check SEO", "Run an SEO audit"

### policy-pages (Legal — Privacy & Terms)

Privacy Policies and Terms of Use — legally compliant, accessible, jurisdiction-specific (GDPR, CCPA, COPPA, PIPEDA, LGPD, Privacy Act 1988, PECR). Plain language, mobile-optimised.

**Produces:** Privacy Policy page, Terms of Use page (customised to client's jurisdiction)

### color-selection (Color Palette Design)

Transforms brand colors into harmonious website color palettes using 7 color theory schemes (monochromatic, analogous, complementary, split-complementary, triadic, tetradic, achromatic). Validates WCAG accessibility (4.5:1 text, 3:1 UI), generates semantic palette with feedback colors.

**Reference Files:** 7 guides (color theory, psychology, schemes, industry, accessibility, application, tools)

**Scripts:** `palette_generator.py` — generates any scheme from hex color

**Produces:** Color palette with semantic tokens, CSS variables, Tailwind config, WCAG compliance report

### blog-idea-generator (Blog Ideation Engine)

Generates 15-25 targeted blog post ideas with 200-word hybrid summaries (narrative brief + structured specs). Reads all client docs, assesses available information across 6 dimensions, then adaptively selects 5-7 methods from a 20-method library. Guided interview fills gaps. Each idea includes audience, buyer stage, format, angle, key points, CTA goal, SEO keywords, and tier classification. Output feeds directly into blog-writer Step 0.

**Reference Files:** `ideation-frameworks.md` (20-method library with selection logic), `content-formats.md` (20 formats with structural templates)

**Produces:** `blog-writer/references/topic-ideas.md`

**Trigger phrases:** "Generate blog ideas", "What should I blog about?", "Blog topic ideas", "Content ideas"

### sales-copywriting (Persuasion & Conversion Copywriting)

Hybrid skill: cross-cutting core principles (headline craft, CTA formulas, anti-resistance writing, proof integration) apply to all pages built by page-builder and blog-writer. Sales-specific frameworks (PASTOR, 4 P's, fascination bullets, named guarantees, value anchoring) activate for landing pages, sales pages, and product pages. Level 2 persuasion (confident, professional) is the default ceiling.

**Reference Files:** 5 guides (headline mastery, 21 fascination bullet templates, resistance & objection handling, PASTOR & 4 P's frameworks, closing templates & guarantee formulas)

**Sources:** Ray Edwards, Paul Hollingshead (AWAI), Angie T. Lee

### skill-writing (Utility — Skill Creation Guide)

Guide for creating effective skills. Covers skill anatomy (YAML frontmatter, body, bundled resources), progressive disclosure design, the 500-line hard limit, and a six-step creation process. Use when creating or updating any SKILL.md in this repo.

### skill-safety-audit (Utility — Security Gate)

Scans new or updated skills for unsafe instructions — unknown installers, credential harvesting, unauthorized network actions, shadow dependencies, and hidden commands in bundled resources. Every new or changed skill must be audited before acceptance.

### email-sender (Utility — Contact Form Handler)

Secure email sending from static websites using PHP + PHPMailer on Apache/WAMP. Self-hosted contact form handler with 4-layer spam prevention (honeypot, timing, content scan, rate limiting), stateless CSRF, beautiful branded HTML emails, and bilingual support. No external services required — no reCAPTCHA, no third-party APIs.

**Requires:** Apache with PHP 8.x, domain SMTP credentials, SPF/DKIM/DMARC records

**Produces:** PHP contact form handler, Alpine.js form component, branded HTML email templates

### image-compression (Utility — Build-Time Compression)

Build-time image compression for static websites. Compresses photos from `photo-bank/` to under 500KB while retaining quality before copying to `src/assets/images/`. Uses Sharp (Node.js) as primary tool. Runs as part of the photo-manager pipeline (Step 2.5: between scanning and cataloguing). Astro then generates optimised WebP/AVIF variants from these already-compressed sources.

**Produces:** Compressed images ready for photo-manager cataloguing

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
  ├── 2. photo-manager      → compress via image-compression, then src/assets/images/, _catalog.json (shared)
  ├── 3. page-builder       → src/pages/[lang]/, src/components/, src/layouts/ (per-language)
  ├── 4. seo (integrates)   → hreflang tags, multi-lang sitemaps, locale meta tags
  ├── 5. blog-writer        → (optional) bilingual blog articles, Article JSON-LD, blog index
  ├── 6. deploy             → dist/{en,fr,sw}/, deploy.sh, nginx.conf (multi-language)
  └── 7. seo-audit          → (optional, post-deploy) 14-category scored audit report

Utility skills (not part of the build pipeline):
  policy-pages               ← use when creating Privacy Policy and Terms of Use pages (per-language)
  color-selection            ← use when defining color palettes (shared across languages)
  sales-copywriting          ← cross-cutting headlines/CTAs + on-demand PASTOR/4P's for sales pages
  email-sender               ← use when adding contact forms (self-hosted PHP + PHPMailer)
  image-compression          ← runs inside photo-manager pipeline (Sharp, under 500KB)
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

Use the included setup script to scaffold a complete client project with multi-language support:

**Linux / macOS:**
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

**Windows (PowerShell):**
```powershell
# Clone this repo
git clone https://github.com/peterbamuhigire/website-skills.git
cd website-skills

# Scaffold a new project
.\new-project.ps1 -ProjectName "acme-corp"

# Or with a remote already set up:
.\new-project.ps1 -ProjectName "acme-corp" -RemoteUrl "git@github.com:yourorg/acme-corp.git"
```

This creates a ready-to-go project with:
- Website-skills submodule at `.claude/skills/`
- Multi-language content directories (`docs/en/`, `docs/fr/`, `docs/sw/`)
- All 11 content templates copied into `docs/en/`
- i18n configuration and SEO template
- Photo bank with categorised subdirectories (branding, hero, team, services, gallery, about, testimonials, misc)
- CLAUDE.md project intelligence file
- Initial git commit

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
for project in clients/*/; do
  (cd "$project" && git submodule update --remote .claude/skills \
    && git add .claude/skills && git commit -m "Update website skills" && git push) 2>/dev/null
done
```

---

## Project Structure (Client Side)

Use `new-project.sh` (Linux/macOS) or `new-project.ps1` (Windows) to create this structure automatically.

```
client-project/
├── CLAUDE.md                  # Project intelligence for Claude Code
├── .claude/skills/            # ← THIS REPO (submodule)
├── docs/                      # Client content (markdown)
│   ├── i18n-config.md         # Language configuration (en, fr, sw)
│   ├── en/                    # English: company-profile.md, pages.md, style-brief.md (required) + optional files
│   ├── fr/                    # French content (translated from en/)
│   └── sw/                    # Kiswahili content (translated from en/)
├── photo-bank/                # Raw client photos: branding/, hero/, team/, services/, gallery/, about/, testimonials/, misc/
├── public/                    # Static assets (favicon, og-image)
└── src/                       # Generated by Claude Code (assets, components, layouts, pages, styles, utils)
```

---

## Photo Naming Convention

Use **descriptive, purpose-specific filenames** (not `IMG_001.jpg`). Claude auto-identifies photos by name pattern:

| Name Pattern | Automatic Placement |
|-------------|---------------------|
| `*Logo*` | Header, footer, favicon |
| `*Headshot*` | Team section grid |
| `*Hero*`, `*banner*` | Page hero sections |
| `*Testimonial*` | Testimonials section |
| `*Staff*`, `*Team*` | Team page introduction |
| `*Certificate*`, `*License*`, `*Award*` | Trust/credibility section |
| `*Gallery*`, `*portfolio*` | Photo gallery pages |
| `*Slide*`, `*carousel*` | Manual gallery / lightbox sequence assets |

**Best practices:** Use hyphens (`Logo-Dark-Mode.png`), capitalise key words, be specific (`Developer-Alice.jpg` not `team-photo.jpg`), include mode variants (`Logo-Light-Mode.png`, `Logo-Dark-Mode.png`). Photo Manager scans, catalogs, and Page Builder places automatically — no manual placement needed.

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
| 2026-02-17 | all | Initial release — 5 core skills, 3 utility skills, sector-strategies (7 sectors), policy-pages, SEO 4-layer architecture |
| 2026-02-22 | new-project | Setup scripts (`.sh` + `.ps1`) with i18n dirs, templates, photo-bank categories |
| 2026-03-01 | blog-writer, seo-audit | Bilingual blog skill; SEO audit (11 categories); human voice standards (60+ AI words banned) |
| 2026-03-02 | seo-audit | Enhanced from 11→14 categories (voice search, off-page, measurement); new seo-measurement-guide.md; major expansions to all reference files |
| 2026-03-02 | seo, page-builder, blog-writer, brand-alignment | Premium content: copywriting formulas (H.O.B.O., PAPA, Uncle B.E.N.), R.E.S.U.L.T.S. framework, StoryBrand, SEO content writing rules |
| 2026-03-05 | sales-copywriting | New hybrid skill: 5 reference files, PASTOR/4P's, fascination bullets, guarantees, anti-resistance; enhanced storytelling.md, writing-craft.md, website-copywriting.md |
| 2026-03-05 | blog-idea-generator, blog-writer | Adaptive 20-method ideation, 200-word summaries, 20 content formats; blog-writer Step 0, 7 format templates, quality gate, calendar/seasonal/cross-language planning |

---

## License

Private. For internal use across website projects.
