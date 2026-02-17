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
├── east-african-english/    Language & tone standard — British spelling, formal, respectful
│   └── SKILL.md
├── brand-alignment/         Ensures site reflects client brand and speaks to ideal customer
│   └── SKILL.md
├── design-reference/        Analyses reference URLs and generates a design guide
│   └── SKILL.md
├── website-builder/         Master orchestrator — coordinates all other skills
│   └── SKILL.md
├── design-system/           Fonts, colors, visual identity, animation strategy
│   └── SKILL.md
├── page-builder/            Transforms markdown content into Astro pages
│   └── SKILL.md
├── photo-manager/           Catalogs photos, tracks dimensions, organizes assets
│   └── SKILL.md
├── deploy/                  Builds, verifies, generates deployment configuration
│   └── SKILL.md
├── skill-writing/           Guide for creating and updating skills (utility)
│   └── SKILL.md
├── skill-safety-audit/      Scans skills for unsafe or malicious instructions (utility)
│   └── SKILL.md
└── update-claude-documentation/  Updates project documentation systematically (utility)
    └── SKILL.md
```

## Skills

### east-african-english (Language & Tone Standard)

The foundational writing standard applied to all generated content. Enforces authentic East African English as used in Uganda, Kenya, and Tanzania — formal, clear, respectful, British-influenced, and professionally courteous. Covers spelling (British), tone (warm but professional), vocabulary (measured, never exaggerated), sentence style, CTAs, and country-specific nuances. This skill runs alongside every other skill.

**Applies to:** All visible website text, meta descriptions, alt text, form labels, error messages

### brand-alignment (Brand Quality Gate)

Ensures the website functions as a coherent brand experience, not just a collection of pages. Reads company profile and style brief to identify the ideal customer, brand position, and differentiator, then validates that every page — layout, messaging, navigation, imagery, CTAs — serves that audience consistently. Catches common pitfalls: generic messaging, visual inconsistency, buried CTAs, speaking to everyone instead of the right someone.

**Applies to:** Homepage clarity, messaging consistency, visual restraint, navigation flow, CTA alignment, content prioritisation

### design-reference (Reference Site Analyser)

Accepts up to 5 URLs of websites the client admires, visits each one, and extracts design patterns — layout, typography, colour, navigation, animation, imagery, and CTAs. Filters every finding through our tech stack (Astro + Tailwind + Alpine.js), performance budget, and accessibility standards. Produces `docs/design-reference.md`, a structured guide that feeds directly into the design-system and page-builder skills.

**Trigger phrases:** "I like these websites", "Here are some references", "Build something similar to these"

**Produces:** `docs/design-reference.md`

### website-builder (Orchestrator)

The entry point. When Claude is told to "build this website", this skill reads all content from `docs/`, scans photos in `photo-bank/`, then coordinates the other skills in order: design-system → photo-manager → page-builder → deploy.

**Trigger phrases:** "Build this website", "Create a site", "Rebuild the site"

### design-system (Visual Foundation)

Establishes the complete visual identity before any pages are built. Reads `docs/style-brief.md` to determine mood, industry, and color preferences. Selects distinctive fonts from Fontsource (never Inter/Roboto/Arial), generates a full color palette, defines component patterns, and commits to a specific aesthetic direction.

**Produces:** `tailwind.config.mjs`, `src/styles/global.css`, `design-tokens.md`

### photo-manager (Image Pipeline)

Scans `photo-bank/`, measures every photo's dimensions with ImageMagick or PIL, copies them to organized `src/assets/images/{category}/` folders, and generates `_catalog.json` — a master registry tracking dimensions, aspect ratios, usage, and replacement notes for every image.

**Produces:** `src/assets/images/*/`, `src/assets/images/_catalog.json`

### page-builder (Content → Pages)

Reads markdown content from `docs/`, the design tokens, and the photo catalog, then generates Astro pages and reusable components. Builds mobile-first with scroll animations, Alpine.js interactivity, proper SEO meta tags, and accessibility compliance.

**Produces:** `src/layouts/`, `src/components/`, `src/pages/`

### deploy (Build & Ship)

Runs `npm run build`, verifies output, checks for broken references, and generates `deploy.sh` and `nginx.conf` with aggressive caching headers. Outputs a pre-launch checklist.

**Produces:** `dist/`, `deploy.sh`, `nginx.conf`

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
east-african-english        ← active throughout (language & tone standard)
brand-alignment             ← active throughout (brand coherence quality gate)
design-reference            ← optional first step (if client provides reference URLs)
        ↓
  docs/design-reference.md
        ↓
website-builder
  ├── 1. design-system    → tailwind.config, global.css, design-tokens.md
  ├── 2. photo-manager    → src/assets/images/, _catalog.json
  ├── 3. page-builder     → src/pages/, src/components/, src/layouts/
  └── 4. deploy           → dist/, deploy.sh, nginx.conf

Utility skills (not part of the build pipeline):
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

## Design Principles

These skills enforce several hard rules:

1. **Zero unnecessary JavaScript.** Astro ships no JS by default. Alpine.js only for interactive elements.
2. **Self-host everything.** No external CDN requests for fonts, scripts, or analytics.
3. **Every site looks different.** Skills choose distinctive fonts, bold color palettes, and varied aesthetics per industry — never generic SaaS templates.
4. **Photos are dimension-aware.** Every image is measured before placement. No upscaling, no broken aspect ratios.
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

---

## License

Private. For internal use across website projects.
