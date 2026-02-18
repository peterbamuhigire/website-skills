# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This is a **Claude Code skills library** — a collection of SKILL.md files that teach Claude how to build static websites from markdown content and photos. It is not a standalone application. It is designed to be added as a **Git submodule** at `.claude/skills/` in every client website project. All client projects share the same skills; updating this repo propagates improvements everywhere.

## Repository Structure

### Website Build Skills

```
i18n/SKILL.md                  ← Multi-language infrastructure (en, fr, sw) → docs/i18n-config.md
language-standards/SKILL.md    ← Language & tone standards (3 languages: cross-cutting, always active)
brand-alignment/SKILL.md       ← Brand coherence quality gate (cross-cutting, always active)
design-reference/SKILL.md      ← Analyses reference URLs → docs/design-reference.md
sector-strategies/SKILL.md     ← Industry-specific design & trust signals → docs/sector-brief.md
website-builder/SKILL.md       ← Master orchestrator (entry point)
design-system/SKILL.md         ← Fonts, colours, visual identity, animations
photo-manager/SKILL.md         ← Photo cataloguing, dimensions, logo detection, asset organisation
page-builder/SKILL.md          ← Multi-language markdown content → Astro pages and components
seo/SKILL.md                   ← Multi-language SEO, hreflang, language-specific sitemaps
deploy/SKILL.md                ← Build verification, language-aware Nginx config, sitemap pinging
```

### Utility Skills

```
policy-pages/SKILL.md                 ← Privacy Policies & Terms of Use design (legal + trust)
color-selection/SKILL.md              ← Color palette design using brand colors and color theory
skill-writing/SKILL.md                ← Guide for creating and updating SKILL.md files
skill-safety-audit/SKILL.md           ← Security audit gate for new/changed skills
update-claude-documentation/SKILL.md  ← Systematic documentation updater
```

Each SKILL.md uses YAML frontmatter (`name`, `description`) followed by markdown instructions that Claude reads when the skill is invoked.

## Skill Execution Order

Website build skills are sequential — each depends on outputs from the previous:

0. **i18n** (mandatory) → reads `docs/i18n-config.md`, detects enabled languages (en, fr, sw), orchestrates all subsequent steps per language
0.5. **design-reference** (optional) → produces `docs/design-reference.md` from up to 5 client-provided URLs
1. **sector-strategies** (optional) → produces `docs/sector-brief.md` with industry-specific design strategy; reads 7 available sectors for distinctive, authentic sites
2. **design-system** → produces `tailwind.config.mjs`, `src/styles/global.css`, `design-tokens.md` (shared across languages)
3. **photo-manager** → produces `src/assets/images/*/`, `src/assets/images/_catalog.json`, auto-detects best logo in `branding/` (shared across languages)
4. **page-builder** → produces `src/layouts/`, `src/components/`, `src/pages/[lang]/` (per-language content from `docs/{lang}/`)
5. **seo** → integrates multi-language SEO: hreflang tags, language-specific sitemaps, Open Graph locale tags
6. **deploy** → produces `dist/`, per-language directories, `deploy.sh`, language-aware `nginx.conf` with root redirect

The `website-builder` skill orchestrates this entire sequence. It reads `docs/i18n-config.md` first, then all language-specific content from `docs/{lang}/` and `photo-bank/` photos.

Three skills are cross-cutting — they apply throughout all steps rather than producing specific files:

- **i18n** — defines language infrastructure, URL routing, language-specific sitemaps
- **language-standards** — all generated text in each language must follow standards (English: British spelling, formal tone; French: formal francophone African; Kiswahili: East African standard)
- **brand-alignment** — every page must reflect the client's brand identity, speak to their ideal customer, and maintain consistent messaging, visual treatment, and CTAs across the entire site and all languages

Utility skills run independently of the build pipeline:

- **policy-pages** — use when creating Privacy Policies and Terms of Use pages; reads docs/company-profile.md for jurisdiction context
- **color-selection** — use when defining website color palettes; generates harmonious colors from brand colors using color theory (monochromatic, analogous, complementary, split-complementary, triadic, tetradic, semantic); validates WCAG accessibility compliance
- **skill-writing** — use when creating or updating any SKILL.md
- **skill-safety-audit** — mandatory audit before accepting any new or changed skill
- **update-claude-documentation** — use after significant changes to update README.md, CLAUDE.md, and related docs

## Generated Site Tech Stack

Sites built by these skills use: Astro (static site generator), Tailwind CSS v4, Alpine.js (interactivity), GSAP (scroll animations, optional), Fontsource (self-hosted fonts), Lucide (SVG icons).

## Hard Design Rules Enforced by Skills

- Zero unnecessary JS — Astro ships no JS by default; Alpine.js only for interactive elements
- Self-host everything — no external CDN requests for fonts, scripts, or analytics
- Every site must look different — distinctive fonts, bold colour palettes per industry; never Inter/Roboto/Arial, never generic SaaS templates
- **Multi-language from the start** — every website supports 3 languages (English, French, Kiswahili); content organized in `docs/{lang}/`; URL structure with language paths (`/en/`, `/fr/`, `/sw/`)
- Photos are dimension-aware and intelligently named — every image measured before placement via `_catalog.json` (never upscale); descriptive photo names (e.g., `Logo-Light-Mode.png`, `Gallery-Project-01.jpg`, `Slide-Feature-01.jpg`) enable automatic categorization and placement; images shared across all language versions
- Content comes only from `docs/{lang}/` markdown — Claude never fabricates company information; all languages complete before build
- **Text expansion awareness** — French content ~30% longer, Kiswahili ~20% longer than English; designs flex for all languages
- **Language standards enforced** — British English, formal francophone French, East African Kiswahili; in-country reviewers approve translations
- Mobile-first — designed for 375px, enhanced for 768px and 1280px+ (all languages)
- Performance budget — 95+ Lighthouse per language, under 500KB first load (images shared across languages)
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
