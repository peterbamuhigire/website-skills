# ============================================================
# new-project.ps1 — Scaffold a new static website project (Windows)
# ============================================================
# Usage:
#   1. Copy this file into your project root
#   2. cd into your project root (git must already be initialised)
#   3. .\new-project.ps1
#
# Prerequisites:
#   - Git must be initialised in the project directory (git init or git clone)
#
# This script:
#   1. Adds website-skills as a submodule at .claude/skills/
#   2. Creates multi-language directory structure (en, fr, sw)
#   3. Copies all content templates from the skills submodule
#   4. Creates i18n config, SEO template, and photo-bank structure
#   5. Creates the CLAUDE.md project intelligence file
#   6. Makes an initial commit
#
# Linux/macOS users: use new-project.sh instead
# ============================================================

$ErrorActionPreference = "Stop"

$SkillsRepo = "https://github.com/peterbamuhigire/website-skills.git"

# --- Check prerequisites ---
$gitVersion = git --version 2>$null
if (-not $gitVersion) {
    Write-Host "Error: git is not installed or not in PATH." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Setting up website-skills submodule" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# --- Add website-skills as submodule ---
Write-Host "[1/6] Adding website-skills submodule..." -ForegroundColor Yellow
git submodule add -q $SkillsRepo .claude/skills
Write-Host "      Submodule added at .claude/skills/"
Write-Host ""

# --- Create directory structure ---
Write-Host "[2/6] Creating directory structure..." -ForegroundColor Yellow

# Multi-language content directories
$contentDirs = @(
    "docs/en",
    "docs/fr",
    "docs/sw",
    "docs/references"
)

# Photo bank with categorised subdirectories
$photoDirs = @(
    "photo-bank/branding",
    "photo-bank/hero",
    "photo-bank/team",
    "photo-bank/services",
    "photo-bank/gallery",
    "photo-bank/about",
    "photo-bank/testimonials",
    "photo-bank/misc"
)

# Source directories
$srcDirs = @(
    "public",
    "src/assets/images",
    "src/components",
    "src/layouts",
    "src/pages",
    "src/styles",
    "src/utils"
)

$allDirs = $contentDirs + $photoDirs + $srcDirs
foreach ($dir in $allDirs) {
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
}

Write-Host "      Created docs/, photo-bank/, src/, public/"
Write-Host ""

# --- Create .gitignore ---
Write-Host "[3/6] Creating .gitignore..." -ForegroundColor Yellow
$gitignoreContent = @"
# Build output
node_modules/
dist/
.astro/

# Client confidential content — never commit
docs/
photo-bank/

# OS files
.DS_Store
Thumbs.db
Desktop.ini

# Environment
.env
.env.*
!.env.example

# Logs
*.log
npm-debug.log*

# Editor
.vscode/settings.json
.idea/
*.swp
*.swo
"@
Set-Content -Path ".gitignore" -Value $gitignoreContent -Encoding UTF8
Write-Host ""

# --- Copy content templates to docs/en/ (source language) ---
Write-Host "[4/6] Copying content templates to docs/en/..." -ForegroundColor Yellow
$skillsDir = ".claude/skills"

# Core templates (required)
Copy-Item "$skillsDir/templates/company-profile.md" "docs/en/"
Copy-Item "$skillsDir/templates/pages.md" "docs/en/"
Copy-Item "$skillsDir/templates/style-brief.md" "docs/en/"

# Recommended templates
Copy-Item "$skillsDir/templates/services.md" "docs/en/"
Copy-Item "$skillsDir/templates/team-profiles.md" "docs/en/"
Copy-Item "$skillsDir/templates/contact.md" "docs/en/"

# Optional templates
Copy-Item "$skillsDir/templates/testimonials.md" "docs/en/"
Copy-Item "$skillsDir/templates/portfolio.md" "docs/en/"
Copy-Item "$skillsDir/templates/faq.md" "docs/en/"
Copy-Item "$skillsDir/templates/about-story.md" "docs/en/"
Copy-Item "$skillsDir/templates/gallery.md" "docs/en/"

# i18n configuration (project-level, not per-language)
Copy-Item "$skillsDir/i18n/docs-i18n-config-template.md" "docs/i18n-config.md"

# SEO configuration (project-level)
Copy-Item "$skillsDir/seo/docs-seo-template.md" "docs/seo.md"

Write-Host "      Copied 11 content templates + i18n config + SEO config"
Write-Host ""

# --- Create placeholder files for French and Kiswahili ---
Write-Host "[5/6] Creating French and Kiswahili placeholders..." -ForegroundColor Yellow

$frReadme = @"
# Contenu en Francais

Ce repertoire contient le contenu en francais du site web.

## Comment proceder

1. Traduisez chaque fichier de ``docs/en/`` en francais
2. Conservez la meme structure YAML frontmatter
3. Utilisez le francais formel (francophone africain)
4. Faites relire par un locuteur natif francophone

## Fichiers requis

Copiez et traduisez ces fichiers depuis ``docs/en/`` :

- ``company-profile.md`` (requis)
- ``pages.md`` (requis)
- ``style-brief.md`` (requis)
- ``services.md`` (recommande)
- ``team-profiles.md`` (recommande)
- ``contact.md`` (recommande)
- ``testimonials.md`` (optionnel)
- ``portfolio.md`` (optionnel)
- ``faq.md`` (optionnel)
- ``about-story.md`` (optionnel)
- ``gallery.md`` (optionnel)

## Standard de langue

- Francais formel francophone africain
- Vouvoiement systematique (jamais "tu")
- Ton professionnel et respectueux
"@
Set-Content -Path "docs/fr/README.md" -Value $frReadme -Encoding UTF8

$swReadme = @"
# Maudhui kwa Kiswahili

Saraka hii ina maudhui ya tovuti kwa Kiswahili.

## Jinsi ya kuendelea

1. Tafsiri kila faili kutoka ``docs/en/`` kwa Kiswahili
2. Weka muundo sawa wa YAML frontmatter
3. Tumia Kiswahili sanifu cha Afrika Mashariki
4. Hakikisha msomaji wa lugha ya Kiswahili amekagua

## Faili zinazohitajika

Nakili na tafsiri faili hizi kutoka ``docs/en/``:

- ``company-profile.md`` (lazima)
- ``pages.md`` (lazima)
- ``style-brief.md`` (lazima)
- ``services.md`` (inapendekezwa)
- ``team-profiles.md`` (inapendekezwa)
- ``contact.md`` (inapendekezwa)
- ``testimonials.md`` (si lazima)
- ``portfolio.md`` (si lazima)
- ``faq.md`` (si lazima)
- ``about-story.md`` (si lazima)
- ``gallery.md`` (si lazima)

## Kiwango cha lugha

- Kiswahili sanifu cha Afrika Mashariki
- Lugha ya heshima na utaalamu
- Epuka lahaja za kikanda
"@
Set-Content -Path "docs/sw/README.md" -Value $swReadme -Encoding UTF8

Write-Host "      Created docs/fr/README.md and docs/sw/README.md"
Write-Host ""

# --- Create photo-bank README ---
Write-Host "      Creating photo-bank guide..." -ForegroundColor Yellow

$photoBankReadme = @"
# Photo Bank

Drop client photos here with descriptive names. Organise into subdirectories by category.

## Directory Structure

``````
photo-bank/
  branding/     <- Logos, brand marks, favicons (e.g., Logo-Light.png, Logo-Dark.png)
  hero/         <- Hero/banner images (wide, min 1600px width)
  team/         <- Team member headshots (square preferred, min 400x400)
  services/     <- Service/product images
  gallery/      <- Portfolio/gallery images
  about/        <- About page images (office, workspace, culture)
  testimonials/ <- Client photos/logos for testimonials
  misc/         <- Anything that doesn't fit above
``````

## Naming Convention

Use descriptive, hyphenated names. The photo-manager skill auto-categorises based on names.

| Prefix | Example | Use |
|--------|---------|-----|
| ``Logo-`` | ``Logo-Light-Mode.png`` | Company logos |
| ``Hero-`` | ``Hero-Office-Exterior.jpg`` | Hero/banner images |
| ``Team-`` | ``Team-John-Doe.jpg`` | Team member headshots |
| ``Service-`` | ``Service-Consulting.jpg`` | Service illustrations |
| ``Gallery-`` | ``Gallery-Project-01.jpg`` | Portfolio/gallery items |
| ``About-`` | ``About-Office-Interior.jpg`` | About page images |
| ``Client-`` | ``Client-Acme-Corp.jpg`` | Client logos/testimonials |
| ``Slide-`` | ``Slide-Feature-01.jpg`` | Carousel/slider images |

## Photo Requirements

- **Format:** JPG or PNG (WebP also accepted)
- **Hero images:** Minimum 1600px wide, landscape orientation
- **Team headshots:** Minimum 400x400px, square crop preferred
- **Logos:** PNG with transparent background, both light and dark versions
- **General:** No upscaling - Claude measures dimensions before placement
- **File size:** Keep originals under 2MB each; Astro compresses during build

## Important

- Photos are SHARED across all language versions (en, fr, sw)
- Claude Code copies photos from here to ``src/assets/images/`` - originals stay untouched
- Never rename photos after the first build without updating the catalog
"@
Set-Content -Path "photo-bank/README.md" -Value $photoBankReadme -Encoding UTF8

$brandingReadme = @"
# Branding Assets

Place logo files here:

- ``Logo-Light-Mode.png`` - Logo for light backgrounds (transparent PNG)
- ``Logo-Dark-Mode.png`` - Logo for dark backgrounds (transparent PNG)
- ``Logo-Icon.png`` - Square icon version (for favicon, mobile)
- ``Logo-Full-Color.png`` - Full-colour logo with background

The photo-manager skill auto-detects the best logo for each context.
"@
Set-Content -Path "photo-bank/branding/README.md" -Value $brandingReadme -Encoding UTF8

Write-Host ""

# --- Create CLAUDE.md ---
Write-Host "[6/6] Creating CLAUDE.md project intelligence file..." -ForegroundColor Yellow

$claudeMd = @"
# CLAUDE.md - Static Website Project

This is a multi-language static website project built with Astro, Tailwind CSS, and Alpine.js. You are building a production-grade, visually stunning website from markdown content and client photos.

## Project Philosophy

We build **beautiful, blazing-fast, zero-JavaScript static websites** for clients who don't need a CMS. Every site must be distinctive - never generic. We ship performance by default and replace WordPress bloat with clean static HTML that scores 95-100 on Lighthouse.

## Architecture

``````
docs/
  i18n-config.md   -> Language configuration (which languages are enabled)
  seo.md           -> SEO meta tags, structured data, sitemap config
  en/              -> English content (source language)
  fr/              -> French content (translated)
  sw/              -> Kiswahili content (translated)
photo-bank/
  branding/        -> Logos, brand marks
  hero/            -> Hero/banner images
  team/            -> Team headshots
  services/        -> Service images
  gallery/         -> Portfolio images
  about/           -> About page images
  testimonials/    -> Client photos
  misc/            -> Other images
.claude/skills/    -> Build instructions (git submodule) - you follow these
src/               -> Astro source code - you generate this
dist/              -> Built static site - Astro generates this
public/            -> Static assets (favicon, og-image, robots.txt)
``````

The workflow is always: **read content -> establish design -> process photos -> build pages -> verify build**.

## Multi-Language Support

This site supports 3 languages: English (en), French (fr), Kiswahili (sw).

- **Configuration:** ``docs/i18n-config.md`` controls which languages are enabled
- **Content:** Each language has its own directory under ``docs/{lang}/``
- **URL structure:** ``/{lang}/page`` (e.g., ``/en/about``, ``/fr/about``, ``/sw/about``)
- **Default:** Root ``/`` redirects to the default language
- **Photos:** Shared across all languages (in ``photo-bank/``)
- **Components:** Shared across all languages (accept ``lang`` prop)

### Language Standards
- **English:** British spelling (colour, organisation), formal East African professional tone
- **French:** Formal francophone African, vouvoiement (vous), professional and respectful
- **Kiswahili:** Standard East African, formal/respectful business register

### Text Expansion
- French: 20-40% longer than English
- Kiswahili: 10-30% longer than English
- All designs must accommodate longer text without breaking

## Skills

You have skills in ``.claude/skills/``. Read them before generating any code.

| Skill | When to use | Reads | Produces |
|-------|-------------|-------|----------|
| ``website-builder`` | Starting a build or full rebuild | All docs/, photo-bank/ | Orchestrates everything |
| ``i18n`` | Always (cross-cutting) | docs/i18n-config.md | Language infrastructure |
| ``design-reference`` | When client provides reference URLs | Client URLs | docs/design-reference.md |
| ``sector-strategies`` | Industry-specific design direction | docs/en/company-profile.md | docs/sector-brief.md |
| ``design-system`` | Before building any pages | docs/en/style-brief.md, company-profile.md | tailwind.config.mjs, global.css, design-tokens.md |
| ``photo-manager`` | Before building pages, after design | photo-bank/**/* | src/assets/images/ (flat), _catalog.json |
| ``page-builder`` | After design + photos are ready | docs/{lang}/*.md, design-tokens.md, _catalog.json | src/pages/{lang}/, components/, layouts/ |
| ``seo`` | After pages are built | docs/seo.md, all pages | hreflang tags, sitemaps, structured data |
| ``deploy`` | After all pages are built | src/, dist/ | deploy.sh, nginx.conf, verification report |

**Execution order matters:** website-builder -> i18n -> design-system -> photo-manager -> page-builder -> seo -> deploy.

## Critical Rules

### Content is truth
- ALL text content comes from ``docs/{lang}/*.md`` files. Never invent company names, services, team members, or any factual content.
- If a docs file has placeholder text like ``[Write 2-3 paragraphs...]``, keep it as a placeholder in the built site or use a generic "Coming soon" - never fabricate content.
- YAML frontmatter in docs files contains structured data (name, email, phone, etc.). Use these values exactly.

### Photos are dimension-aware
- NEVER place a photo without first measuring its dimensions (use ``identify`` from ImageMagick or Python PIL).
- NEVER use a small image in a large slot (no upscaling).
- Every photo used must be tracked in ``src/assets/images/_catalog.json``.
- Photos are copied from ``photo-bank/`` to ``src/assets/images/`` (single flat directory) — never moved or modified.
- If no suitable photo exists for a slot, use a CSS gradient/solid color placeholder and document it in the catalog's ``placeholders_needed`` array.
- NEVER reference external placeholder services (no unsplash, no placeholder.com, no picsum).

### Design must be distinctive
- Read ``docs/en/style-brief.md`` and commit to a BOLD aesthetic direction appropriate to the industry.
- NEVER use Inter, Roboto, Arial, or system fonts as primary typefaces.
- NEVER default to purple-gradient-on-white or generic SaaS card layouts.
- Use fonts from Fontsource (self-hosted, no external CDN requests).
- Every project should look different. Vary themes, fonts, layout approaches, and color palettes.

### Performance is non-negotiable
- Zero unnecessary JavaScript. Astro ships no JS by default - keep it that way.
- Alpine.js only for interactive elements (mobile menu, accordions, tabs, modals).
- Self-host everything: fonts, icons, scripts. No external CDN dependencies.
- Use Astro's ``<Image>`` component for all images (auto WebP/AVIF, responsive srcsets, lazy loading).
- Hero images use ``loading="eager"``. Everything else uses ``loading="lazy"``.
- Target: total page weight under 500KB on first load (excluding lazy-loaded images).

### Accessibility is required
- Proper heading hierarchy: one ``<h1>`` per page, sequential ``<h2>``-``<h6>``.
- Descriptive ``alt`` text on every image.
- ``aria-label`` on icon-only buttons and non-obvious interactive elements.
- Keyboard-navigable mobile menu.
- Color contrast: 4.5:1 for body text, 3:1 for large text.
- Focus-visible styles on all interactive elements.
- Include a skip-to-content link in BaseLayout.

### Mobile-first, always
- Design for 375px first, then enhance for 768px and 1280px+.
- Navigation: hamburger on mobile, full nav on desktop.
- Touch targets minimum 44x44px.
- No horizontal scroll at any viewport width.
- Typography scales: use responsive Tailwind classes (text-3xl md:text-4xl lg:text-5xl).

## Tech Stack

- **Astro** (latest) - static site generator, zero JS by default, component islands
- **Tailwind CSS v4** - utility-first styling with design tokens in config
- **Alpine.js** - lightweight interactivity (17KB, no build step)
- **GSAP** (optional) - scroll-triggered animations, parallax
- **Fontsource** - self-hosted Google Fonts alternatives
- **Lucide** or **Phosphor** - SVG icon sets

## Common Commands

``````bash
npm run dev          # Start dev server at localhost:4321
npm run build        # Build to dist/
npm run preview      # Preview production build
``````

## File Naming Conventions

### Photos in photo-bank/
- ``Logo-{variant}.png`` - brand logos (in branding/)
- ``Hero-{description}.jpg`` - hero/banner images (in hero/)
- ``Team-{name}.jpg`` - team member headshots (in team/)
- ``Service-{name}.jpg`` - service/product images (in services/)
- ``Gallery-{name}.jpg`` - portfolio/gallery images (in gallery/)
- ``About-{description}.jpg`` - about page images (in about/)
- ``Client-{name}.jpg`` - client logos or testimonial photos (in testimonials/)

### Components in src/components/
- PascalCase: ``Header.astro``, ``ServiceCard.astro``, ``TeamMember.astro``
- One component per file
- Props interface defined at the top of the component

### Pages in src/pages/
- Language-prefixed: ``src/pages/en/index.astro``, ``src/pages/fr/about.astro``
- Slugs must match ``docs/{lang}/pages.md`` definitions

## Photo Replacement Workflow

The user will replace placeholder photos after the initial build:

1. ``src/assets/images/_catalog.json`` tracks every image with its path, dimensions, and where it's used.
2. To replace: drop a new file at the same path with the same filename.
3. Run ``npm run build`` - Astro regenerates optimized versions.
4. The catalog's ``notes`` field describes what each photo should be.

Always include helpful ``notes`` like "Needs: wide office exterior shot, min 1600x900".

## Deployment Model

Sites deploy via git pull and build. No server-side runtime, no database, no CMS.

``````
Local:  edit -> build -> git push
Server: git pull -> npm run build -> nginx serves dist/
``````

## When Updating an Existing Site

If the site already exists (src/ is populated):
- Read the existing ``design-tokens.md`` to maintain visual consistency.
- Read the existing ``_catalog.json`` to know what photos are available.
- Only regenerate the files that need to change - don't rebuild everything.
- Preserve any manual customizations the user may have made to components.
- Run ``npm run build`` after changes to verify nothing is broken.

## Error Handling

- If ``docs/en/`` is empty or missing critical files, tell the user what's needed before proceeding.
- If ``photo-bank/`` is empty, build with CSS gradient placeholders and document all needed photos.
- If ``npm run build`` fails, read the error output, fix the issue, and try again.
- If a font package fails to install, fall back to another distinctive font - never fall back to system fonts.
- If a language directory (fr/, sw/) is empty, skip that language in the build.
"@
Set-Content -Path "CLAUDE.md" -Value $claudeMd -Encoding UTF8

Write-Host ""

# --- Initial commit ---
git add .
git commit -q -m "Add website-skills submodule and project scaffold

- website-skills submodule at .claude/skills/
- Multi-language structure (en, fr, sw)
- Content templates in docs/en/
- i18n config and SEO config
- Photo bank with categorised subdirectories
- CLAUDE.md project intelligence file"

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  Setup complete!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Directory structure:" -ForegroundColor Cyan
Write-Host "  .claude/skills/        <- Website build skills (submodule)"
Write-Host "  docs/"
Write-Host "    i18n-config.md       <- Language settings"
Write-Host "    seo.md               <- SEO configuration"
Write-Host "    en/                  <- English content (11 templates ready)"
Write-Host "    fr/                  <- French content (translate from en/)"
Write-Host "    sw/                  <- Kiswahili content (translate from en/)"
Write-Host "  photo-bank/"
Write-Host "    branding/            <- Logos and brand marks"
Write-Host "    hero/                <- Hero/banner images"
Write-Host "    team/                <- Team headshots"
Write-Host "    services/            <- Service images"
Write-Host "    gallery/             <- Portfolio images"
Write-Host "    about/               <- About page images"
Write-Host "    testimonials/        <- Client photos"
Write-Host "    misc/                <- Other images"
Write-Host "  src/                   <- Generated by Claude Code"
Write-Host "  public/                <- Static assets (favicon, etc.)"
Write-Host "  CLAUDE.md              <- Project intelligence for Claude"
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Drop client documents (PDF, DOCX, TXT) into docs/references/"
Write-Host "  2. Drop client photos into photo-bank/ subdirectories"
Write-Host "  3. Drop logos (PNG, transparent) into photo-bank/branding/"
Write-Host "  4. Open Claude Code: claude"
Write-Host "  5. Use the kickstart prompt: .claude/skills/prompts/new-project-kickstart.md"
Write-Host "     Fill in the [PROJECT CONFIGURATION] section, then paste the full prompt"
Write-Host ""
