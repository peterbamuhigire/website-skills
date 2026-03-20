# Next Steps — March 2026

Immediate actions from the comprehensive review. Start at the top.

## This Week

### 1. Apply Quick Wins to Existing Skills

These take 30–60 minutes each and improve output quality immediately.

**seo/SKILL.md** — add these schema templates:
- FAQ schema (direct featured snippet play)
- HowTo schema
- LocalBusiness schema (full: address, hours, geo, telephone)
- BreadcrumbList schema
- Service schema

**page-builder/SKILL.md** — add:
- 4 alternative page opening structures (problem-first, data-first, story-first, question-first)
- Component naming rule: use client vocabulary, not generic names (HeroSection → ClientNameHero)
- Layout variation patterns: portfolio-led, video-hero, data-led, story-first

**design-system/SKILL.md** — add:
- 5-step mood board process
- Typography pairing rationale requirement
- 8px grid spacing methodology

**photo-manager/SKILL.md** — add:
- Art direction checklist (authentic vs staged, brand personality match)
- AI alt-text formula per image type (hero, product, team, decorative, infographic)

**website-builder/SKILL.md** — add:
- Quality gate checklist between each pipeline step
- Definition of done per skill output

### 2. Build `discovery-strategy` Skill

This is the most important missing skill. Without a discovery process:
- We cannot justify premium pricing
- We build without understanding what the client needs
- Projects go over scope or miss business goals

**What it covers:**
- Structured client intake questionnaire (30 questions across 6 dimensions)
- Business goals → website objectives mapping
- Competitor analysis: 3-5 sites, scored against 10 criteria
- Target audience research: 3 persona profiles
- Sitemap architecture: draft navigation before writing content
- Content strategy: which pages, what purpose, what CTA
- Project brief: 10-20 page deliverable the client signs off

**Deliverable:** `docs/discovery-brief.md` — the document all other skills read from

### 3. Build `wcag-accessibility` Skill

Legal and ranking requirement. No $50k site goes live without this.

**What it covers:**
- WCAG 2.2 AA requirements per component type
- Contrast ratio checking per design system token
- Focus state standards (visible, branded, not default browser outline)
- Screen reader testing checklist (VoiceOver + NVDA)
- ARIA roles per component type
- Keyboard navigation flow per page type
- Skip links implementation
- Form accessibility (label association, error announcement)
- Alt text rules (decorative vs informative vs functional)
- Audit report template (deliverable to client)

### 4. Build `performance-optimization` Skill

95+ Lighthouse is promised. This skill makes it achievable.

**What it covers:**
- LCP optimization: image priority, preload hints, hero image strategy
- CLS prevention: dimension reservation, font loading, layout shift detection
- INP optimization: JS deferral, event handler patterns
- Critical CSS extraction for Astro
- Resource hint strategy: preconnect, dns-prefetch, modulepreload
- Image strategy: WebP/AVIF generation, responsive srcset, lazy loading zones
- Font strategy: font-display swap, subsetting, self-hosting (already done, needs depth)
- Bundle analysis: Astro built-in tools, what to look for
- CDN configuration for static assets
- Lighthouse CI integration for automated checks

## Next 2 Weeks

### 5. Build `brand-style-guide` Skill

A brand style guide is a client deliverable. It justifies premium pricing alone.

**Deliverable format:** PDF-ready markdown → `docs/brand-style-guide.md`

**Sections:**
- Logo usage rules (clear space, minimum size, colour variants, don't-do examples)
- Colour palette card (hex, RGB, CMYK, Pantone, accessibility rating)
- Typography specimen sheet (headings, body, captions, code)
- Spacing and grid documentation
- Tone of voice: 3 principles, 10 example rewrites
- Photography style: mood words, 5 do / 5 don't examples
- Component library overview (buttons, cards, forms)

### 6. Build `design-audit` Skill

Runs before design-system. Produces the aesthetic direction that design-system implements.

**Process:**
1. Gather 10-15 reference sites (client-provided + Claude research)
2. Filter to 3-5 most aligned
3. Extract: colour families, type choices, spacing density, imagery style, animation language
4. Define: 5 design personality words
5. Validate against client brand values
6. Produce: design-direction.md (input to design-system)

### 7. Extend Schema Coverage

Add to `seo/SKILL.md` or create `schema-complete/SKILL.md`:
- All missing schema types (FAQ, HowTo, Service, LocalBusiness, Event, VideoObject, Review)
- Schema validation checklist
- Rich snippet testing process (Google Rich Results Test)
- Schema implementation per page type

## Month 2

### 8. Build `internal-linking` Skill
### 9. Build `content-cluster` Skill
### 10. Build `featured-snippets` Skill
### 11. Build `cro-audit` Skill
### 12. Build `competitive-intelligence` Skill

## Month 3

### 13. Build `post-launch-monitoring` Skill
### 14. Build `client-onboarding` Skill
### 15. Build `image-seo` Skill

---

## Tracking

Update this file as skills are built. Move completed items to a done section.

### Done (March 2026)
- [x] ecommerce/SKILL.md — upgraded with Larsson, Verma, Harris, Spencer frameworks
- [x] ecommerce-funnel/SKILL.md — created (RIC metrics, avatar, lifecycle)
- [x] ecommerce-checkout/SKILL.md — created (7C brand, East Africa payments)
- [x] ecommerce-analytics/SKILL.md — created (Phillips value chain, cohort, RFM)
- [x] agency-positioning/SKILL.md — created (Doctor-Pilot-Teacher, ROYA)
- [x] they-ask-you-answer/SKILL.md — created (Big 5, Selling 7, Assignment Selling)
- [x] agency-client-retention/SKILL.md — created (Rule of Five Ones, Land-Deliver-Retain)
- [x] monthly-report/SKILL.md — created (7-step interview, full report template)
- [x] Comprehensive review documented in docs/march-20-review/
