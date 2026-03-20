# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This is a **Claude Code skills library** — a collection of SKILL.md files that teach Claude how to build static websites from markdown content and photos. It is not a standalone application. It is designed to be added as a **Git submodule** at `.claude/skills/` in every client website project. All client projects share the same skills; updating this repo propagates improvements everywhere.

## Repository Structure

### Website Build Skills

```
i18n/SKILL.md                  ← Multi-language infrastructure (en, fr, sw) → docs/i18n-config.md
language-standards/SKILL.md    ← Language & tone standards (3 languages: cross-cutting, always active)
content-writing/SKILL.md       ← Copywriting standards: headlines, ledes, readability, niche vocabulary (cross-cutting, always active)
brand-alignment/SKILL.md       ← Brand coherence quality gate (cross-cutting, always active)
design-reference/SKILL.md      ← Analyses reference URLs → docs/design-reference.md
sector-strategies/SKILL.md     ← Industry-specific design & trust signals → docs/sector-brief.md
website-builder/SKILL.md       ← Master orchestrator (entry point)
design-system/SKILL.md         ← Fonts, colours, visual identity, animations
photo-manager/SKILL.md         ← Photo cataloguing, dimensions, logo detection, asset organisation
page-builder/SKILL.md          ← Multi-language markdown content → Astro pages and components
seo/SKILL.md                   ← Multi-language SEO, hreflang, language-specific sitemaps
blog-writer/SKILL.md           ← Bilingual blog articles (EN + FR), East African English & West African French voice
deploy/SKILL.md                ← Build verification, language-aware Nginx config, sitemap pinging
```

### Utility Skills

```
seo-audit/SKILL.md                    ← Post-build SEO audit (14 categories, scored report, action items)
blog-idea-generator/SKILL.md          ← Guided interview → 15-25 targeted blog topic ideas with titles, angles, keywords
email-sender/SKILL.md                 ← PHP + PHPMailer contact form handler (self-hosted, 4-layer spam prevention)
image-compression/SKILL.md            ← Build-time image compression via Sharp (runs inside photo-manager pipeline)
policy-pages/SKILL.md                 ← Privacy Policies & Terms of Use design (legal + trust)
color-selection/SKILL.md              ← Color palette design using brand colors and color theory
sales-copywriting/SKILL.md            ← Persuasion and conversion copywriting (hybrid: cross-cutting headlines/CTAs + on-demand PASTOR/4P's for sales pages)
ecommerce/SKILL.md                    ← E-commerce UX, CLICK system, trust signals, product pages, cart abandonment, mobile commerce
ecommerce-funnel/SKILL.md             ← Customer avatar, traffic temperature, funnel architecture (front-end → upsell → RIC), email sequences, lifecycle management
ecommerce-checkout/SKILL.md           ← Brand foundation (7C framework), EVP vs UVP, checkout UX deep-dive, post-purchase sequence, DTC growth levers
ecommerce-analytics/SKILL.md         ← RFM analysis, cohort retention, attribution modelling, CLV calculation, funnel drop-off diagnosis, RASTA reporting
agency-positioning/SKILL.md           ← Premium agency positioning: Doctor-Pilot-Teacher, 9 positioning assets, solutions language, authentic storytelling, premium pricing justification
they-ask-you-answer/SKILL.md          ← Content-driven lead generation: Big 5 pillars, Selling 7 videos, Assignment Selling, CarMax Effect, content as sales enablement
agency-client-retention/SKILL.md      ← Client pricing and retention: Rule of Five Ones, Land-Deliver-Retain, monthly reports, Seed the Vision, deal structures
monthly-report/SKILL.md               ← AI-generated monthly client reports: 7-step data interview, plain-English commentary, QA checklist, PDF-ready markdown output
brand-strategy/SKILL.md               ← Brand strategy: CBBE pyramid (Keller), brand mantra, 12 archetypes, positioning statement, 22 Laws applied, brand brief deliverable (docs/brand-brief.md)
brand-storytelling/SKILL.md           ← Brand storytelling: Five-Act Arc (Quesenberry), Hero's Journey, Golden Circle, Creative Brief, Story Engine, 5 signature story types
brand-style-guide/SKILL.md            ← Client deliverable: logo rules, colour palette card, typography specimen, photography style, voice/tone guide, always/never table (docs/brand-style-guide.md)
skill-writing/SKILL.md                ← Guide for creating and updating SKILL.md files
skill-safety-audit/SKILL.md           ← Security audit gate for new/changed skills
update-claude-documentation/SKILL.md  ← Systematic documentation updater
east-african-english/SKILL.md         ← Legacy English-only standard (superseded by language-standards)
```

### Sector-Specific Skills

```
sectors/legal/SKILL.md                ← Law firm websites: client psychology, practice area matrix, ethics constraints, attorney profiles, legal local SEO, intake conversion
```

Each SKILL.md uses YAML frontmatter (`name`, `description`) followed by markdown instructions that Claude reads when the skill is invoked.

## Skill Execution Order

Website build skills are sequential — each depends on outputs from the previous:

0. **i18n** (mandatory) → reads `docs/i18n-config.md`, detects enabled languages (en, fr, sw), orchestrates all subsequent steps per language
0.5. **design-reference** (optional) → produces `docs/design-reference.md` from up to 5 client-provided URLs
0.6. **brand-strategy** (recommended) → produces `docs/brand-brief.md` (brand positioning, archetype, mantra, POPs/PODs); required input for brand-style-guide; feeds design-system, brand-alignment, page-builder
1. **sector-strategies** or **sectors/{sector}** (optional) → produces `docs/sector-brief.md`; use `sectors/legal` for law firms, others via sector-strategies
2. **design-system** → produces `tailwind.config.mjs`, `src/styles/global.css`, `design-tokens.md`; reads `docs/brand-brief.md` if available
3. **photo-manager** (includes **image-compression**) → compresses photos via Sharp, then produces `src/assets/images/` (flat directory, no subdirectories), `src/assets/images/_catalog.json`, auto-detects best logo (shared across languages)
4. **page-builder** → produces `src/layouts/`, `src/components/`, `src/pages/[lang]/` (per-language content from `docs/{lang}/`)
5. **seo** → integrates multi-language SEO: hreflang tags, language-specific sitemaps, Open Graph locale tags
5.5. **blog-writer** (optional) → produces SEO-ready bilingual blog articles in `docs/{lang}/blog/`, reads idea summaries from blog-idea-generator, Astro blog pages, Article JSON-LD, updates blog index
6. **deploy** → produces `dist/`, per-language directories, `deploy.sh`, language-aware `nginx.conf` with root redirect
7. **seo-audit** (optional, post-deploy) → audits 14 SEO categories, produces scored report with prioritised action items

The `website-builder` skill orchestrates this entire sequence. It reads `docs/i18n-config.md` first, then all language-specific content from `docs/{lang}/` and `photo-bank/` photos.

Four skills are cross-cutting — they apply throughout all steps rather than producing specific files:

- **i18n** — defines language infrastructure, URL routing, language-specific sitemaps
- **language-standards** — all generated text in each language must follow standards (English: British spelling, formal tone; French: formal francophone African; Kiswahili: East African standard)
- **content-writing** — copywriting standards for all website text: benefit-driven headlines, strong ledes, readability (Fog Index 8-10), niche vocabulary, scannable formatting, features-to-benefits translation, and page structure templates
- **brand-alignment** — every page must reflect the client's brand identity, speak to their ideal customer, and maintain consistent messaging, visual treatment, and CTAs across the entire site and all languages

Utility skills run independently of the build pipeline:

- **blog-idea-generator** — use before blog-writer to generate 15-25 targeted blog topic ideas with 200-word hybrid summaries; reads website content, assesses 6 information dimensions, adaptively selects 5-7 methods from a 20-method library; outputs to `blog-writer/references/topic-ideas.md`
- **policy-pages** — use when creating Privacy Policies and Terms of Use pages; reads docs/company-profile.md for jurisdiction context
- **color-selection** — use when defining website color palettes; generates harmonious colors from brand colors using color theory (monochromatic, analogous, complementary, split-complementary, triadic, tetradic, semantic); validates WCAG accessibility compliance
- **sales-copywriting** — hybrid persuasion skill: cross-cutting core (headlines, CTAs, anti-resistance, proof integration) applies to all pages; sales frameworks (PASTOR, 4 P's, guarantees, fascination bullets) activate for landing/sales pages; Level 2 persuasion default
- **skill-writing** — use when creating or updating any SKILL.md
- **skill-safety-audit** — mandatory audit before accepting any new or changed skill
- **seo-audit** — use after deploy to audit SEO across 14 categories (including voice search readiness, off-page signals, SEO measurement); produces scored report with prioritised action items
- **email-sender** — use when adding contact forms; self-hosted PHP + PHPMailer with 4-layer spam prevention, no external services
- **image-compression** — runs inside photo-manager pipeline; compresses photos to under 500KB via Sharp before cataloguing
- **update-claude-documentation** — use after significant changes to update README.md, CLAUDE.md, and related docs
- **brand-strategy** — use before design-system on any project; structured client discovery → brand brief deliverable (docs/brand-brief.md); covers CBBE pyramid, brand mantra, 12 archetypes, 22 Laws, Frequency-Consistency-Anchoring
- **brand-storytelling** — use when writing About pages, case studies, or any narrative-driven content; Five-Act Dramatic Arc, Hero's Journey (customer = hero, brand = mentor), Creative Brief, Golden Circle order, 5 signature story types
- **brand-style-guide** — use after brand-strategy and design-system; produces docs/brand-style-guide.md — a client-facing PDF-ready deliverable covering logo rules, colour palette, typography, photography, voice/tone, always/never rules
- **sectors/legal** — use instead of sector-strategies for any law firm client; covers client psychology, 8 practice area types, ethics/bar advertising constraints, attorney profiles, legal local SEO, intake conversion

## Required Claude Code Plugins

These plugins MUST be installed before any website development work. They are force multipliers — use them proactively wherever they can improve output quality, not just when explicitly invoked.

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
/plugin marketplace add anthropics/claude-code
/plugin install frontend-design@claude-code-plugins
```

**Prerequisites:** Node.js and the `claude` CLI (`npm install -g @anthropic-ai/claude-code`) with a Pro/Max subscription. Restart Claude Code after installing plugins.

**Superpowers plugin:** Use throughout the entire build pipeline — design decisions, code generation, debugging, quality checks, and any task where it offers enhanced capabilities. If superpowers provides a better way to accomplish something, prefer it over the default approach.

**Frontend Design plugin:** Use for all design system work, component styling, layout decisions, colour selection, typography, responsive design, and visual QA. Lean on it during design-system, page-builder, and any skill that produces visual output.

Install at the start of every new client project. These commands are idempotent (safe to re-run).

## Generated Site Tech Stack

Sites built by these skills use: Astro (static site generator), Tailwind CSS v4, Alpine.js (interactivity), GSAP (scroll animations, optional), Fontsource (self-hosted fonts), Lucide (SVG icons).

## Hard Design Rules Enforced by Skills

- Zero unnecessary JS — Astro ships no JS by default; Alpine.js only for interactive elements
- Self-host everything — no external CDN requests for fonts, scripts, or analytics
- Every site must look different — distinctive fonts, bold colour palettes per industry; never Inter/Roboto/Arial, never generic SaaS templates
- **Multi-language from the start** — every website supports 3 languages (English, French, Kiswahili); content organized in `docs/{lang}/`; URL structure with language paths (`/en/`, `/fr/`, `/sw/`)
- Photos are dimension-aware and intelligently named — every image measured before placement via `_catalog.json` (never upscale); all photos copied to a single flat `src/assets/images/` directory (no subdirectories) for easy replacement; descriptive filenames enable automatic categorization via catalog metadata; images shared across all language versions
- Content comes only from `docs/{lang}/` markdown — Claude never fabricates company information; all languages complete before build
- **Text expansion awareness** — French content ~30% longer, Kiswahili ~20% longer than English; designs flex for all languages
- **Language standards enforced** — British English, formal francophone French, East African Kiswahili; in-country reviewers approve translations
- **Content writing standards enforced** — benefit-driven headlines, strong ledes (no throat-clearing), Fog Index 8-10 readability, niche vocabulary for authority, scannable subheads every 2-3 paragraphs, features always translated to benefits
- **Human voice mandatory** — all content must pass as 100% human-written; 60+ AI vocabulary words banned (see `blog-writer/references/human-voice-standards.md`), sentence burstiness required, client language mining enforced; page-builder uses copywriting formulas from `page-builder/references/website-copywriting.md`
- Mobile-first — designed for 375px, enhanced for 768px and 1280px+ (all languages)
- Performance budget — 95+ Lighthouse per language, under 500KB first load (images shared across languages)
- **Videos hosted on YouTube only** — never upload video files to repos or servers; clients upload to their YouTube channel and provide URLs in docs; embed via `youtube-nocookie.com` iframe with `loading="lazy"`
- Every website includes Privacy Policy and Terms of Use in all enabled languages — legal protection + user trust

## Client Content Templates

The `templates/` directory contains markdown templates that clients copy into their `docs/` folder and fill in. These provide all the content the skills need to build a website.

**Core (required):** `company-profile.md`, `pages.md`, `style-brief.md`
**Recommended:** `services.md`, `team-profiles.md`, `contact.md`
**Optional:** `testimonials.md`, `portfolio.md`, `faq.md`, `about-story.md`, `gallery.md`

Additional templates live in skill directories: `seo/docs-seo-template.md`, `sector-strategies/templates/branding-colors-template.md`, `sector-strategies/templates/{sector}/sector-brief-template.md`.

If a client skips an optional template, skills use available information from core files to generate content — or omit that section entirely. The only truly required file is `company-profile.md`.

See `templates/README.md` for the full guide.

## Client Project Structure (Where Skills Are Consumed)

```
client-project/
├── .claude/skills/        ← THIS REPO (submodule)
├── docs/                  ← Language configuration and shared content
│   ├── i18n-config.md     ← Language configuration (en, fr, sw settings)
│   ├── en/                ← English content
│   │   ├── company-profile.md
│   │   ├── services.md
│   │   ├── pages.md
│   │   └── ... (all content)
│   ├── fr/                ← French content (translated)
│   │   ├── company-profile.md
│   │   ├── services.md
│   │   ├── pages.md
│   │   └── ... (all content)
│   └── sw/                ← Kiswahili content (translated)
│       ├── company-profile.md
│       ├── services.md
│       ├── pages.md
│       └── ... (all content)
├── photo-bank/            ← Raw client photos (never modified, only copied from, shared across all languages)
└── src/                   ← Generated by Claude Code using these skills
    ├── assets/
    │   └── images/        ← All photos in ONE flat directory + _catalog.json
    ├── pages/
    │   └── [lang]/        ← Dynamic routes per language (/en/, /fr/, /sw/)
    ├── components/        ← Shared across all languages
    ├── layouts/           ← Shared across all languages (accepts lang prop)
    └── utils/
        └── i18n.ts        ← Language utilities
```

## Working on Skills

When editing SKILL.md files in this repo:

1. Follow the **skill-writing** guide for structure, frontmatter, and the 500-line hard limit
2. Run **skill-safety-audit** on any new or modified skill before accepting it
3. Test changes against a real client project before pushing
4. Maintain the YAML frontmatter format (`name`, `description` — no other fields)
5. Respect the execution order — do not add dependencies that break the chain
6. Run **update-claude-documentation** to update README.md, CLAUDE.md, and changelog
7. After pushing, client projects update via `git submodule update --remote .claude/skills`
