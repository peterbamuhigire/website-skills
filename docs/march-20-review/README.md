# March 2026 Comprehensive Review
## Goal: $50,000 Website Capability Assessment

**Date:** 2026-03-20
**Reviewed by:** 3 parallel audit agents (build pipeline, SEO/performance, gap analysis)
**Overall rating:** 3.5 / 5 — Capable at $5k–$15k. Significant gaps before $50k is honest.

---

## What This Review Covers

1. [Current State](#current-state) — what works and what score each skill earned
2. [Critical Gaps](#critical-gaps) — what is missing or weak for premium projects
3. [New Skills Required](#new-skills-required) — 14 skills that do not exist yet
4. [Prioritised Roadmap](#prioritised-roadmap) — what to build first for fastest ROI
5. [Anti-Slop Audit](#anti-slop-audit) — where AI-generated output is still detectable
6. [Quick Wins](#quick-wins) — improvements achievable in a single session

---

## Current State

### Build Pipeline Skills

| Skill | Rating | Strength | Weakness |
|-------|--------|----------|----------|
| website-builder | 3/5 | Orchestrates the pipeline | No quality gate between steps; no checklist for what "done" looks like |
| i18n | 4/5 | Solid 3-language infrastructure | No RTL support; no plural rules for Kiswahili |
| language-standards | 4/5 | Covers all 3 languages well | No tone calibration per page type (hero ≠ legal ≠ blog) |
| design-system | 3/5 | Good token structure | No mood board process; colour methodology is ad hoc; no type scale rationale |
| photo-manager | 4/5 | Dimension-aware, flat catalog | No AI alt-text generation; no art direction rules for hero/product/team |
| page-builder | 3/5 | Covers major page types | No component library; no animation choreography spec; templates lack real differentiators |
| seo | 3/5 | Core on-page covered | Schema only 40% complete; no featured snippet targeting; no content cluster architecture |
| blog-writer | 3.5/5 | 7 structural templates, strong formats | No internal linking strategy; no topic cluster map; no E-E-A-T signals beyond author bio |
| deploy | 4/5 | Language-aware Nginx, sitemap ping | No post-deploy monitoring setup; no uptime check; no CDN configuration |
| brand-alignment | 3/5 | Good checklist concept | No brand audit process; no deliverable (brand style guide); cross-skill enforcement weak |

### Utility Skills

| Skill | Rating | Strength | Weakness |
|-------|--------|----------|----------|
| sales-copywriting | 4/5 | PASTOR, 4 P's, strong frameworks | No landing page wireframe pairing; conversion rate prediction absent |
| blog-idea-generator | 3.5/5 | 20-method ideation, adaptive | No competitor gap analysis; no keyword demand signal |
| seo-audit | 3/5 | 14 categories | Scores are manual; no Core Web Vitals tooling; no structured action-item output format |
| color-selection | 3.5/5 | WCAG compliance checks | No perceptual contrast testing; no dark mode palette generation |
| email-sender | 4/5 | 4-layer spam protection | No transactional email templates; no drip sequence support |
| policy-pages | 3.5/5 | Jurisdiction-aware | Not kept current with GDPR/local law updates; no cookie consent integration |
| image-compression | 4.5/5 | Sharp-based, under 500KB | No WebP/AVIF generation; no responsive srcset generation |

### New Skills (This Session)

| Skill | Rating | Notes |
|-------|--------|-------|
| ecommerce | 4/5 | Strong post-upgrade; CLICK system solid |
| ecommerce-funnel | 4/5 | RIC metrics, avatar work good |
| ecommerce-checkout | 4/5 | 7C brand + East Africa payments |
| ecommerce-analytics | 4/5 | Phillips value chain, cohort analysis |
| agency-positioning | 4/5 | Doctor-Pilot-Teacher, authentic storytelling |
| they-ask-you-answer | 4.5/5 | Sheridan's framework fully extracted |
| agency-client-retention | 4/5 | Nelson's systems complete |
| monthly-report | 4/5 | 7-step interview, full template |

---

## Critical Gaps

These are the gaps that prevent this library from producing $50k websites. Ranked by impact.

### GAP 1: No Accessibility Skill (WCAG 2.2)
**Impact: CRITICAL**

A $50k website cannot have accessibility failures. WCAG 2.2 compliance is a legal requirement in many jurisdictions and a ranking signal for Google. Currently:
- No contrast ratio verification beyond color-selection
- No focus state standards
- No screen reader testing guidance
- No keyboard navigation requirements
- No skip-link implementation
- No ARIA role guidance per component type

Every page-builder output can have accessibility failures and the library has no way to catch them.

### GAP 2: No Performance Optimization Skill (Core Web Vitals)
**Impact: CRITICAL**

95+ Lighthouse is mentioned in CLAUDE.md but there is no skill that actually teaches Claude how to achieve it. Currently:
- No LCP optimization strategy (lazy loading, preload hints, image priority)
- No CLS prevention (dimension reservation, font loading strategy)
- No FID/INP optimization (JS deferral, input latency patterns)
- No critical CSS extraction
- No bundle analysis process
- No resource hint strategy (preconnect, dns-prefetch, preload)
- No CDN configuration guidance

Astro helps but Astro alone does not guarantee 95+.

### GAP 3: No Discovery & Strategy Skill
**Impact: CRITICAL**

$50k projects start with a discovery phase that justifies the price. Currently there is no skill for:
- Client intake process (structured questionnaire)
- Business goals → website objectives mapping
- Competitor analysis methodology
- Target audience research
- Sitemap architecture planning
- Content strategy before writing begins
- Project brief production (deliverable clients keep)

Without this, Claude starts building without understanding what the client actually needs.

### GAP 4: No Design Audit / Mood Board Skill
**Impact: HIGH**

design-system produces tokens but has no methodology for arriving at the right aesthetic. A $50k website requires:
- Mood board construction (reference gathering, visual direction)
- Industry aesthetic analysis (what competitors look like, what to differentiate from)
- Typography pairing rationale (not just "pick something nice")
- Colour psychology per industry
- Layout language definition (grid system, spacing rhythm)
- Visual hierarchy audit before build

Without a design audit process, designs emerge from guesswork.

### GAP 5: No CRO Audit Skill
**Impact: HIGH**

Conversion rate optimisation is what separates premium agencies from template shops. Missing:
- Heuristic evaluation checklist (10 Nielsen heuristics applied to web)
- Attention flow analysis (above fold, eye tracking patterns)
- CTA effectiveness scoring
- Trust signal audit
- Form UX audit
- Mobile usability scoring
- Hypothesis generation for A/B tests

### GAP 6: No Internal Linking Strategy
**Impact: HIGH**

seo skill covers on-page basics but has no internal linking architecture. For a $50k site:
- Topic cluster hub-and-spoke mapping
- Anchor text strategy (exact, partial, branded, generic ratios)
- PageRank sculpting (which pages to prioritise)
- Link from/to matrix for blog posts
- Orphan page detection
- Breadcrumb SEO strategy

Without this, blog content does not build authority for money pages.

### GAP 6: Schema Markup Gaps (40% Complete)
**Impact: HIGH**

Current schema: Product (ecommerce), Article (blog), basic Organization.
Missing:
- LocalBusiness with full address, hours, geo coordinates
- Service (for service business sites)
- FAQ (for FAQ sections — direct featured snippet play)
- HowTo (for instructional content)
- BreadcrumbList
- SiteLinks Searchbox
- Review/AggregateRating for non-product pages
- VideoObject for embedded videos
- Event schema

Each missing schema type is a lost rich snippet opportunity.

### GAP 7: No Brand Style Guide Deliverable Skill
**Impact: HIGH**

A $50k project delivers a brand style guide that the client owns. Currently design-system produces code files (tailwind.config.mjs) but no client-facing document. Missing:
- Logo usage rules
- Colour palette card (hex, RGB, CMYK, Pantone)
- Typography specimen sheet
- Spacing and grid documentation
- Tone of voice summary
- Do/Don't examples
- Brand asset export process

### GAP 8: No Competitive Intelligence Skill
**Impact: MEDIUM**

Every serious project needs to know what competitors look like. Missing:
- Competitor site audit checklist
- Content gap identification
- Keyword gap analysis methodology
- Design differentiation strategy
- Feature comparison matrix

### GAP 9: No Voice Search / Featured Snippet Skill
**Impact: MEDIUM**

Voice search is mentioned vaguely in seo skill but there is no actionable process:
- Question-intent keyword identification
- Answer box formatting (40-60 word paragraphs, definition format, numbered lists)
- People Also Ask targeting
- Conversational keyword variants
- Local voice search signals ("near me", opening hours)

### GAP 10: No Video SEO Skill
**Impact: MEDIUM**

Videos are mentioned (YouTube embeds only) but there is no skill for:
- YouTube channel optimisation
- Video schema (VideoObject)
- Thumbnail best practices
- Video sitemap
- Transcript SEO

### GAP 11: No Image SEO Skill (Beyond Compression)
**Impact: MEDIUM**

image-compression handles file size but has no SEO layer:
- Alt text formulas per image type (hero, product, team, decorative)
- File naming conventions for SEO
- Image sitemap generation
- Structured data for images
- Google Lens optimisation

### GAP 12: No Content Cluster / Pillar Page Architecture
**Impact: MEDIUM**

blog-idea-generator produces topics but has no cluster architecture:
- Pillar page structure (2000+ word hub)
- Cluster page requirements (600–1500 word spokes)
- Internal linking rules between pillar and clusters
- Topic authority building sequence
- Keyword mapping per cluster

### GAP 13: No Post-Launch Monitoring Setup Skill
**Impact: MEDIUM**

deploy skill launches the site but no skill sets up ongoing monitoring:
- Google Search Console verification
- Uptime monitoring (UptimeRobot or similar)
- Core Web Vitals ongoing tracking
- 404 error alerting
- Rank tracking setup
- Monthly performance baseline capture

### GAP 14: No Client Onboarding Skill
**Impact: MEDIUM**

agency-client-retention covers retention but there is no onboarding process:
- Client welcome sequence
- Project kick-off agenda
- Access collection checklist (hosting, domain, social, analytics)
- Expectations document
- Communication preferences capture
- Milestone sign-off process

---

## New Skills Required

These 14 skills do not exist and should be built in order of priority:

| Priority | Skill Name | Purpose | Estimated Impact |
|----------|------------|---------|-----------------|
| 1 | `wcag-accessibility` | WCAG 2.2 audit + remediation | CRITICAL — legal + ranking |
| 2 | `performance-optimization` | Core Web Vitals 95+ methodology | CRITICAL — ranking + UX |
| 3 | `discovery-strategy` | Client intake, competitor analysis, project brief | CRITICAL — justifies premium price |
| 4 | `design-audit` | Mood board, aesthetic direction, visual hierarchy | HIGH — design quality |
| 5 | `brand-style-guide` | Client-facing deliverable: logo, colour, type, voice | HIGH — agency deliverable |
| 6 | `cro-audit` | Heuristic evaluation, attention flow, CTA scoring | HIGH — conversion |
| 7 | `schema-complete` | Full schema library: FAQ, HowTo, Service, LocalBusiness, Event | HIGH — rich snippets |
| 8 | `internal-linking` | Topic cluster architecture, anchor text strategy | HIGH — SEO authority |
| 9 | `featured-snippets` | Answer box targeting, PAA strategy, voice search | MEDIUM — visibility |
| 10 | `competitive-intelligence` | Competitor audit, content/keyword gaps | MEDIUM — positioning |
| 11 | `image-seo` | Alt text, naming, image sitemap, Lens optimisation | MEDIUM — SEO completeness |
| 12 | `content-cluster` | Pillar + spoke architecture, topic authority building | MEDIUM — SEO authority |
| 13 | `post-launch-monitoring` | GSC setup, uptime, CWV tracking, rank tracking | MEDIUM — retention |
| 14 | `client-onboarding` | Welcome sequence, access collection, kick-off | MEDIUM — professionalism |

---

## Anti-Slop Audit

The anti-slop rules in `blog-writer/references/human-voice-standards.md` cover written content well. However, three areas still produce detectable AI output:

### 1. Generic Component Names
page-builder produces components named `HeroSection`, `ServiceCard`, `TestimonialSlider`. Every Astro template on the internet uses these names. Premium sites have named components that reflect the client's world.

**Fix:** page-builder should name components after the client's brand or sector vocabulary.

### 2. Stock Photo Culture
No skill currently enforces that photos look like the actual client. The catalog system works but has no guidance on:
- Authentic over staged
- Avoiding multi-ethnic stock photo clichés
- Matching photo style to brand personality
- Rejecting photos that look like Unsplash homepage

**Fix:** photo-manager needs art direction rules per site personality type.

### 3. Predictable Page Structure
Every site currently follows: Hero → Services → About → Testimonials → CTA → Footer. This is correct but predictable.

**Fix:** page-builder needs layout variation patterns (problem-solution, story-first, portfolio-led, data-led, video-hero) that break the template feeling.

---

## Quick Wins

These improvements can be made immediately without building new skills:

### In `seo/SKILL.md`
- Add FAQ schema template (20 lines, directly reusable)
- Add HowTo schema template
- Add LocalBusiness schema with all fields
- Add BreadcrumbList schema

### In `page-builder/SKILL.md`
- Add 4 alternative page opening structures (problem-first, data-first, story-first, question-first)
- Add component naming guidance (use client vocabulary, not generic)

### In `design-system/SKILL.md`
- Add 5-step mood board process (gather → filter → extract → define → validate)
- Add typography pairing rationale requirement
- Add spacing scale methodology (8px grid or 4px base)

### In `photo-manager/SKILL.md`
- Add art direction checklist (authentic vs staged, brand personality match)
- Add AI alt-text formula per image type

### In `brand-alignment/SKILL.md`
- Add cross-skill enforcement checkpoint (brand-alignment runs after each major skill)
- Add brand deviation flag process

### In `website-builder/SKILL.md`
- Add quality gate checklist between each step
- Add "definition of done" per skill output

---

## Prioritised Roadmap to $50k

### Phase 1: Foundation (Build Now — 1-2 weeks)
These gaps block $50k work entirely:

1. **`discovery-strategy`** — without this, we cannot justify premium pricing
2. **`wcag-accessibility`** — legal exposure without this
3. **`performance-optimization`** — 95+ Lighthouse is promised, needs a process
4. **Quick wins** — schema, page structure variety, mood board process

### Phase 2: Premium Deliverables (2-4 weeks)
These are what $50k clients expect to receive:

5. **`brand-style-guide`** — client keeps this; justifies the price alone
6. **`design-audit`** — mood board + aesthetic direction before any code
7. **`cro-audit`** — post-build conversion analysis

### Phase 3: SEO Authority (4-6 weeks)
These compound over time and are what agencies charge retainers for:

8. **`schema-complete`** — full rich snippet coverage
9. **`internal-linking`** — topic cluster authority building
10. **`content-cluster`** — pillar + spoke architecture
11. **`featured-snippets`** — voice search + answer box targeting

### Phase 4: Agency Systems (6-8 weeks)
These turn one-off projects into recurring revenue:

12. **`competitive-intelligence`** — better briefs, better positioning
13. **`post-launch-monitoring`** — GSC, uptime, rank tracking
14. **`client-onboarding`** — professional process justifies premium
15. **`image-seo`** — completes the SEO picture

---

## What $50k Actually Requires

A $50k website project (in African markets, typically USD 15k–30k; in European/US markets, USD 30k–50k+) requires:

1. **Discovery deliverable** — 10-20 page strategy document the client reviews and signs
2. **Brand style guide** — logo rules, colour system, typography, voice guide
3. **Competitive analysis** — 3-5 competitor teardowns with differentiation strategy
4. **Multi-language content** — EN + FR + SW fully written, not templated
5. **Accessibility compliance** — WCAG 2.2 AA audit report provided
6. **Performance guarantee** — 95+ Lighthouse across all pages documented
7. **Full schema coverage** — every applicable schema type implemented
8. **CRO analysis** — post-launch conversion review with recommendations
9. **Content cluster foundation** — 1 pillar page + 4-6 cluster articles at launch
10. **Monthly reporting** — ✅ (monthly-report skill built this session)

Of these 10 requirements, the current library satisfies 2.5 (multi-language content, monthly reporting, partial performance). The skills built today (ecommerce, agency-positioning, they-ask-you-answer, agency-client-retention) move toward 5/10.

The roadmap above closes the remaining 5 gaps.

---

## Summary Verdict

The library is strong for $5k–$15k websites. It has excellent bones: multi-language infrastructure, human voice standards, content writing depth, and now agency systems knowledge.

To reach $50k, three things must happen:

1. **Discovery must happen before build** — currently we jump straight to design-system
2. **Deliverables must exist beyond the website** — brand guide, strategy doc, accessibility report
3. **SEO must go deeper** — schema, clusters, internal linking, featured snippets

The new skills built today (they-ask-you-answer, agency-positioning, agency-client-retention) are exactly right for justifying and retaining $50k clients. What remains is the technical depth to deliver at that level.

See [next steps](NEXT-STEPS.md) for the immediate action plan.
