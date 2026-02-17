#!/bin/bash
set -e

# ============================================================
# new-project.sh — Scaffold a new static website project
# ============================================================
# Usage:
#   ./new-project.sh client-name
#   ./new-project.sh client-name git@github.com:yourorg/client-name.git
#
# This script:
#   1. Creates the project directory
#   2. Initializes git
#   3. Adds website-skills as a submodule at .claude/skills/
#   4. Copies the docs templates and photo-bank folder
#   5. Creates the CLAUDE.md project intelligence file
#   6. Makes an initial commit
# ============================================================

SKILLS_REPO="https://github.com/peterbamuhigire/website-skills.git"

# --- Validate input ---
if [ -z "$1" ]; then
  echo "Usage: ./new-project.sh <project-name> [remote-repo-url]"
  echo ""
  echo "Examples:"
  echo "  ./new-project.sh acme-corp"
  echo "  ./new-project.sh acme-corp git@github.com:yourorg/acme-corp.git"
  exit 1
fi

PROJECT_NAME="$1"
REMOTE_URL="$2"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# --- Check if directory already exists ---
if [ -d "$PROJECT_NAME" ]; then
  echo "Error: Directory '$PROJECT_NAME' already exists."
  exit 1
fi

echo "=== Creating project: $PROJECT_NAME ==="
echo ""

# --- Create project directory ---
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME"

# --- Initialize git ---
git init
echo ""

# --- Add website-skills as submodule ---
echo "Adding website-skills submodule..."
git submodule add "$SKILLS_REPO" .claude/skills
echo ""

# --- Create directory structure ---
mkdir -p docs
mkdir -p photo-bank
mkdir -p public
mkdir -p src/assets/images/hero
mkdir -p src/assets/images/team
mkdir -p src/assets/images/services
mkdir -p src/assets/images/gallery
mkdir -p src/assets/images/about
mkdir -p src/assets/images/testimonials
mkdir -p src/assets/images/misc

# --- Create .gitignore ---
cat > .gitignore << 'EOF'
node_modules/
dist/
.astro/
.DS_Store
*.log
.env
EOF

# --- Create docs templates ---
cat > docs/company-profile.md << 'DOCEOF'
---
name: "Company Name"
tagline: "Your compelling one-liner"
industry: "e.g., Legal, Healthcare, Real Estate, Construction"
founded: "2020"
location: "Kampala, Uganda"
email: "info@company.com"
phone: "+256 700 000000"
website: "https://company.com"
social:
  twitter: ""
  linkedin: ""
  facebook: ""
  instagram: ""
---

## About
[Write 2-3 paragraphs about the company — what they do, who they serve, what makes them different.]

## Mission
[One clear mission statement.]

## Vision
[One aspirational vision statement.]

## Values
- Excellence: [Description]
- Integrity: [Description]
- Innovation: [Description]
- Community: [Description]

## History
[The company's story — founding, growth milestones, key achievements.]

## Key Numbers
- Clients served: 500+
- Years in business: 5
- Team size: 25
- Projects completed: 200+
DOCEOF

cat > docs/services.md << 'DOCEOF'
---
service_count: 4
---

## Service 1: [Service Name]
**summary:** [One-line summary for cards]
**description:** [Full paragraph describing this service]
**icon:** shield
**features:**
- Feature A
- Feature B
- Feature C

## Service 2: [Service Name]
**summary:** [One-line summary for cards]
**description:** [Full paragraph describing this service]
**icon:** building
**features:**
- Feature A
- Feature B
- Feature C

## Service 3: [Service Name]
**summary:** [One-line summary for cards]
**description:** [Full paragraph describing this service]
**icon:** users
**features:**
- Feature A
- Feature B
- Feature C

## Service 4: [Service Name]
**summary:** [One-line summary for cards]
**description:** [Full paragraph describing this service]
**icon:** chart-line
**features:**
- Feature A
- Feature B
- Feature C
DOCEOF

cat > docs/team.md << 'DOCEOF'
## John Doe
**role:** CEO & Founder
**photo:** team-john.jpg
**bio:** [Brief biography — 2-3 sentences about background and role.]
**linkedin:** https://linkedin.com/in/johndoe
**email:** john@company.com

## Jane Smith
**role:** Head of Operations
**photo:** team-jane.jpg
**bio:** [Brief biography — 2-3 sentences about background and role.]
**linkedin:** https://linkedin.com/in/janesmith
**email:** jane@company.com
DOCEOF

cat > docs/testimonials.md << 'DOCEOF'
## Testimonial 1
**name:** Client Name
**role:** Managing Director, XYZ Ltd
**photo:** client-name.jpg
**quote:** "[Client testimonial quote — 1-3 sentences about their experience.]"

## Testimonial 2
**name:** Client Name
**role:** CEO, ABC Holdings
**photo:** client-name.jpg
**quote:** "[Client testimonial quote — 1-3 sentences about their experience.]"

## Testimonial 3
**name:** Client Name
**role:** Operations Manager, DEF Corp
**photo:** client-name.jpg
**quote:** "[Client testimonial quote — 1-3 sentences about their experience.]"
DOCEOF

cat > docs/contact.md << 'DOCEOF'
---
address: "Plot 12, Kampala Road, Kampala, Uganda"
phone: "+256 700 000000"
email: "info@company.com"
hours: "Monday - Friday: 8:00 AM - 5:00 PM"
map_embed: ""
---

## Get in Touch
[Optional paragraph inviting visitors to reach out.]

## Office Location
[Description of where the office is, landmarks, parking info, etc.]
DOCEOF

cat > docs/faq.md << 'DOCEOF'
## What services do you offer?
[Answer here]

## How long have you been in business?
[Answer here]

## What areas do you serve?
[Answer here]

## How can I get a quote?
[Answer here]

## Do you offer support after project completion?
[Answer here]
DOCEOF

cat > docs/style-brief.md << 'DOCEOF'
---
# Design Direction
mood: "professional yet warm"
industry_feel: ""
primary_color: ""
secondary_color: ""
accent_color: ""
dark_mode: false
preferred_style: ""
references: ""
---

## Brand Notes
[Any existing brand guidelines — logo colors, fonts they already use, things to avoid.
Leave blank and Claude will make creative choices based on the industry.]

## Content Tone
[Professional, friendly, authoritative, casual, etc.]

## Special Requests
[Any specific design requests — e.g., "dark theme", "include a project gallery",
"hero should feature team photo, not stock imagery"]
DOCEOF

cat > docs/pages.md << 'DOCEOF'
---
pages:
  - slug: "/"
    title: "Home"
    sections: [hero, services-overview, about-snippet, testimonials, cta]
  - slug: "/about"
    title: "About Us"
    sections: [hero, story, mission-vision, team-preview, numbers]
  - slug: "/services"
    title: "Services"
    sections: [hero, service-list-detailed, process, cta]
  - slug: "/team"
    title: "Our Team"
    sections: [hero, team-grid]
  - slug: "/contact"
    title: "Contact"
    sections: [hero, contact-info, form]
nav_order: [Home, About, Services, Team, Contact]
cta_text: "Get in Touch"
cta_link: "/contact"
---

## Notes
[Add or remove pages as needed. Available section types:
hero, services-overview, service-list-detailed, about-snippet, story,
mission-vision, team-preview, team-grid, testimonials, numbers, cta,
contact-info, form, faq, gallery, process, culture]
DOCEOF

# --- Create photo-bank README ---
cat > photo-bank/README.md << 'DOCEOF'
# Photo Bank

Drop client photos here with descriptive names.

## Naming Convention
- `hero-*.jpg` — hero/banner images (wide, min 1600px)
- `team-*.jpg` — team member headshots (square preferred)
- `service-*.jpg` — service/product images
- `gallery-*.jpg` — portfolio/gallery images
- `about-*.jpg` — about page images
- `client-*.jpg` — client logos/photos for testimonials

Claude Code will catalog dimensions and organize these into the site.
DOCEOF

# --- Create CLAUDE.md ---
cat > CLAUDE.md << 'CLAUDEEOF'
# CLAUDE.md — Static Website Project

This is a static website project built with Astro, Tailwind CSS, and Alpine.js. You are building a production-grade, visually stunning website from markdown content and client photos.

## Project Philosophy

We build **beautiful, blazing-fast, zero-JavaScript static websites** for clients who don't need a CMS. Every site must be distinctive — never generic. We ship performance by default and replace WordPress bloat with clean static HTML that scores 95-100 on Lighthouse.

## Architecture

```
docs/                → Content (markdown, YAML frontmatter) — human writes this
photo-bank/          → Raw client photos — human dumps these here
.claude/skills/      → Build instructions (git submodule) — you follow these
src/                 → Astro source code — you generate this
dist/                → Built static site — Astro generates this
```

The workflow is always: **read content → establish design → process photos → build pages → verify build**.

## Skills

You have 5 skills in `.claude/skills/`. Read them before generating any code.

| Skill | When to use | Reads | Produces |
|-------|-------------|-------|----------|
| `website-builder` | Starting a build or full rebuild | All docs/, photo-bank/ | Orchestrates everything |
| `design-system` | Before building any pages | docs/style-brief.md, docs/company-profile.md | tailwind.config.mjs, global.css, design-tokens.md |
| `photo-manager` | Before building pages, after design | photo-bank/*.{jpg,png,webp} | src/assets/images/*/, _catalog.json |
| `page-builder` | After design + photos are ready | docs/*.md, design-tokens.md, _catalog.json | src/pages/, src/components/, src/layouts/ |
| `deploy` | After all pages are built | src/, dist/ | deploy.sh, nginx.conf, verification report |

**Execution order matters:** website-builder → design-system → photo-manager → page-builder → deploy.

## Critical Rules

### Content is truth
- ALL text content comes from `docs/*.md` files. Never invent company names, services, team members, or any factual content.
- If a docs file has placeholder text like `[Write 2-3 paragraphs...]`, keep it as a placeholder in the built site or use a generic "Coming soon" — never fabricate content.
- YAML frontmatter in docs files contains structured data (name, email, phone, etc.). Use these values exactly.

### Photos are dimension-aware
- NEVER place a photo without first measuring its dimensions (use `identify` from ImageMagick or Python PIL).
- NEVER use a small image in a large slot (no upscaling).
- Every photo used must be tracked in `src/assets/images/_catalog.json`.
- Photos are copied from `photo-bank/` to `src/assets/images/{category}/` — never moved or modified.
- If no suitable photo exists for a slot, use a CSS gradient/solid color placeholder and document it in the catalog's `placeholders_needed` array.
- NEVER reference external placeholder services (no unsplash, no placeholder.com, no picsum).

### Design must be distinctive
- Read `docs/style-brief.md` and commit to a BOLD aesthetic direction appropriate to the industry.
- NEVER use Inter, Roboto, Arial, or system fonts as primary typefaces.
- NEVER default to purple-gradient-on-white or generic SaaS card layouts.
- Use fonts from Fontsource (self-hosted, no external CDN requests).
- Every project should look different. Vary themes, fonts, layout approaches, and color palettes.

### Performance is non-negotiable
- Zero unnecessary JavaScript. Astro ships no JS by default — keep it that way.
- Alpine.js only for interactive elements (mobile menu, accordions, tabs, modals).
- Self-host everything: fonts, icons, scripts. No external CDN dependencies.
- Use Astro's `<Image>` component for all images (auto WebP/AVIF, responsive srcsets, lazy loading).
- Hero images use `loading="eager"`. Everything else uses `loading="lazy"`.
- Target: total page weight under 500KB on first load (excluding lazy-loaded images).

### Accessibility is required
- Proper heading hierarchy: one `<h1>` per page, sequential `<h2>`-`<h6>`.
- Descriptive `alt` text on every image.
- `aria-label` on icon-only buttons and non-obvious interactive elements.
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

- **Astro** (latest) — static site generator, zero JS by default, component islands
- **Tailwind CSS v4** — utility-first styling with design tokens in config
- **Alpine.js** — lightweight interactivity (17KB, no build step)
- **GSAP** (optional) — scroll-triggered animations, parallax
- **Fontsource** — self-hosted Google Fonts alternatives
- **Lucide** or **Phosphor** — SVG icon sets

## Common Commands

```bash
npm run dev          # Start dev server at localhost:4321
npm run build        # Build to dist/
npm run preview      # Preview production build
```

## File Naming Conventions

### Photos in photo-bank/
- `hero-{description}.jpg` — hero/banner images
- `team-{name}.jpg` — team member headshots
- `service-{name}.jpg` — service/product images
- `gallery-{name}.jpg` — portfolio/gallery images
- `about-{description}.jpg` — about page images
- `client-{name}.jpg` — client logos or testimonial photos

### Components in src/components/
- PascalCase: `Header.astro`, `ServiceCard.astro`, `TeamMember.astro`
- One component per file
- Props interface defined at the top of the component

### Pages in src/pages/
- kebab-case: `index.astro`, `about.astro`, `our-services.astro`
- Slugs must match `docs/pages.md` definitions

## Photo Replacement Workflow

The user will replace placeholder photos after the initial build:

1. `src/assets/images/_catalog.json` tracks every image with its path, dimensions, and where it's used.
2. To replace: drop a new file at the same path with the same filename.
3. Run `npm run build` — Astro regenerates optimized versions.
4. The catalog's `notes` field describes what each photo should be.

Always include helpful `notes` like "Needs: wide office exterior shot, min 1600x900".

## Deployment Model

Sites deploy via git pull and build. No server-side runtime, no database, no CMS.

```
Local:  edit → build → git push
Server: git pull → npm run build → nginx serves dist/
```

## When Updating an Existing Site

If the site already exists (src/ is populated):
- Read the existing `design-tokens.md` to maintain visual consistency.
- Read the existing `_catalog.json` to know what photos are available.
- Only regenerate the files that need to change — don't rebuild everything.
- Preserve any manual customizations the user may have made to components.
- Run `npm run build` after changes to verify nothing is broken.

## Error Handling

- If `docs/` is empty or missing critical files, tell the user what's needed before proceeding.
- If `photo-bank/` is empty, build with CSS gradient placeholders and document all needed photos.
- If `npm run build` fails, read the error output, fix the issue, and try again.
- If a font package fails to install, fall back to another distinctive font — never fall back to system fonts.
CLAUDEEOF

# --- Add remote if provided ---
if [ -n "$REMOTE_URL" ]; then
  git remote add origin "$REMOTE_URL"
  echo "Remote added: $REMOTE_URL"
fi

# --- Initial commit ---
git add .
git commit -m "Initial project setup with website-skills submodule"
echo ""

echo "=== Project '$PROJECT_NAME' created successfully ==="
echo ""
echo "Next steps:"
echo "  1. cd $PROJECT_NAME"
echo "  2. Edit all files in docs/ with client content"
echo "  3. Drop client photos into photo-bank/"
echo "  4. Open Claude Code: claude"
echo "  5. Tell Claude: \"Build this website following the website-builder skill\""
echo ""
if [ -n "$REMOTE_URL" ]; then
  echo "  6. git push -u origin main"
else
  echo "  To add a remote later:"
  echo "    git remote add origin git@github.com:yourorg/$PROJECT_NAME.git"
  echo "    git push -u origin main"
fi
echo ""
