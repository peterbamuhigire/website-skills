# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This is a **Claude Code skills library** — a collection of SKILL.md files that teach Claude how to build static websites from markdown content and photos. It is not a standalone application. It is designed to be added as a **Git submodule** at `.claude/skills/` in every client website project. All client projects share the same skills; updating this repo propagates improvements everywhere.

## Repository Structure

### Website Build Skills

```
east-african-english/SKILL.md  ← Language & tone standard (cross-cutting, always active)
brand-alignment/SKILL.md       ← Brand coherence quality gate (cross-cutting, always active)
design-reference/SKILL.md      ← Analyses reference URLs → docs/design-reference.md
sector-strategies/SKILL.md     ← Industry-specific design & trust signals → docs/sector-brief.md
website-builder/SKILL.md       ← Master orchestrator (entry point)
design-system/SKILL.md         ← Fonts, colours, visual identity, animations
photo-manager/SKILL.md         ← Photo cataloguing, dimensions, logo detection, asset organisation
page-builder/SKILL.md          ← Markdown content → Astro pages and components
seo/SKILL.md                   ← SEO configuration, meta tags, structured data, sitemap
deploy/SKILL.md                ← Build verification, deploy scripts, Nginx config
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

0. **design-reference** (optional) → produces `docs/design-reference.md` from up to 5 client-provided URLs
0.5. **sector-strategies** (optional) → produces `docs/sector-brief.md` with industry-specific design strategy; reads 7 available sectors for distinctive, authentic sites
1. **design-system** → produces `tailwind.config.mjs`, `src/styles/global.css`, `design-tokens.md`
2. **photo-manager** → produces `src/assets/images/*/`, `src/assets/images/_catalog.json`, auto-detects best logo in `branding/`
3. **page-builder** → produces `src/layouts/`, `src/components/`, `src/pages/`
4. **seo** → integrates SEO configuration, meta tags, JSON-LD schema, sitemap during deploy
5. **deploy** → produces `dist/`, `deploy.sh`, `nginx.conf`

The `website-builder` skill orchestrates this entire sequence. It reads all `docs/` content and `photo-bank/` photos before generating anything.

Two skills are cross-cutting — they apply throughout all steps rather than producing specific files:

- **east-african-english** — all generated text must use British spelling, formal/respectful tone, and measured professional vocabulary as used in Uganda, Kenya, and Tanzania
- **brand-alignment** — every page must reflect the client's brand identity, speak to their ideal customer, and maintain consistent messaging, visual treatment, and CTAs across the entire site

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
- Photos are dimension-aware and intelligently named — every image measured before placement via `_catalog.json` (never upscale); descriptive photo names (e.g., `Logo-Light-Mode.png`, `Gallery-Project-01.jpg`, `Slide-Feature-01.jpg`) enable automatic categorization and placement
- Content comes only from `docs/` markdown — Claude never fabricates company information
- Mobile-first — designed for 375px, enhanced for 768px and 1280px+
- Performance budget — 95+ Lighthouse, under 500KB first load
- Every website includes Privacy Policy and Terms of Use — legal protection + user trust

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
├── docs/                  ← Client content (markdown): company-profile.md, services.md, style-brief.md, pages.md, etc.
├── photo-bank/            ← Raw client photos (never modified, only copied from)
└── src/                   ← Generated by Claude Code using these skills
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
