---
name: website-builder
description: Master orchestrator for building static websites from markdown content and photos. Use when the user says "build a website", "create a site", or references docs/ content. Reads content from docs/, photos from photo-bank/, and generates a complete Astro website.
---

# Website Builder — Master Orchestrator

You are building a beautiful, blazing-fast static website using Astro + Tailwind CSS + Alpine.js.

## Before You Start

**ALWAYS read these files first, in this order:**

1. `docs/pages.md` — what pages to build and their structure
2. `docs/style-brief.md` — design direction and brand info
3. `docs/company-profile.md` — company details
4. ALL other files in `docs/` — services, team, testimonials, etc.
5. Scan `photo-bank/` — what photos are available

Do NOT generate any code until you have read ALL content files.

## Orchestration Steps

### Step 1: Scaffold (if needed)
If no `package.json` exists:
```bash
npm create astro@latest . -- --template minimal --no-git --no-install
npx astro add tailwind -y
npm install alpinejs
npm install gsap
```
Install any Fontsource fonts chosen by the design system.

### Step 2: Design System
Follow `.claude/skills/design-system/SKILL.md` to establish:
- Font selections (self-hosted via Fontsource)
- Color palette in tailwind.config.mjs
- Global styles in src/styles/global.css
- Animation utilities
- Component design patterns

### Step 3: Photo Management
Follow `.claude/skills/photo-manager/SKILL.md` to:
- Catalog all photos in photo-bank/
- Copy to src/assets/images/ with proper organization
- Generate _catalog.json with dimensions and usage tracking

### Step 4: Build Pages
Follow `.claude/skills/page-builder/SKILL.md` for each page:
- Create the BaseLayout.astro first
- Create reusable components (Header, Footer, Hero, etc.)
- Build each page from docs/ content
- Wire up navigation

### Step 5: Verify
- Run `npm run build` and fix any errors
- Check that all pages exist in dist/
- Verify no broken image references
- Create deploy.sh script

## Critical Rules

1. **Ship ZERO unnecessary JavaScript.** Astro handles this by default — don't add client-side frameworks unless absolutely needed.
2. **Every image must go through the photo pipeline.** Never hardcode image paths. Always reference from the catalog and use Astro's `<Image>` component.
3. **Mobile-first design.** Every page must look great at 375px width. Test mentally at 375px, 768px, 1280px.
4. **Semantic HTML.** Use proper heading hierarchy, landmark elements, aria-labels.
5. **Performance budget:** Total page weight under 500KB on first load (excluding lazy images).
6. **Design must be DISTINCTIVE.** No generic SaaS templates. Read the style brief and commit to a bold direction.
7. **Self-host everything.** No Google Fonts CDN, no external analytics scripts, no CDN dependencies.

## Output Summary

After building, provide:
- List of pages created
- Design direction chosen
- Photos used (and which are placeholders)
- Any content gaps found in docs/
- How to run locally: `npm run dev`
- How to replace placeholder photos (reference _catalog.json)
