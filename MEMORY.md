# MEMORY.md - Key Learnings & Patterns

This file preserves important patterns and decisions across sessions to avoid re-learning and enable continuity.

## Session: Policy Pages & Photo Naming (2026-02-17)

### Policy Pages Skill (NEW)

**What:** Created comprehensive policy-pages skill for Privacy Policies and Terms of Use.

**Key Pattern:** Every website must have both documents. They serve dual purposes:
- **Legal protection** (legally binding agreements/disclosures)
- **User trust** (transparent communication showing respect for user data)

**File Structure:**
- `policy-pages/SKILL.md` (368 lines, under 500-line hard limit)
- `policy-pages/references/privacy-policy-detailed.md` (737 lines)
- `policy-pages/references/terms-of-use-detailed.md` (925 lines)

**Critical Elements:**
- Privacy Policy: 15 essential elements (jurisdiction-specific: GDPR, CCPA, COPPA, PIPEDA, LGPD, Privacy Act 1988, PECR)
- Terms of Use: 15+ essential elements (enforceability, liability limits, dispute resolution)
- Both must use plain language (avoid legal jargon)
- Both must be mobile-optimized and accessible (WCAG 2.1 AA)
- Version control: archive old versions, track changes

**Jurisdictions Covered:**
- GDPR (EU) - requires DPO contact, explicit consent, 72-hour breach notification
- CCPA (California) - requires opt-out, response within 45 days
- COPPA (US) - children under 13 require parental consent
- PIPEDA (Canada) - consent required, no use beyond stated purpose
- LGPD (Brazil) - transparency and accountability principles
- Privacy Act 1988 (Australia) - APPs compliance, anonymization requirements
- PDPA (Singapore/Thailand) - lawful basis, cross-border restrictions

### Photo Naming Conventions (CRITICAL for Automation)

**Pattern:** Descriptive photo filenames enable Claude to automatically identify purpose and appropriate placement.

**Recognition Patterns:**
- `Logo-*` (Light/Dark modes) → Header/footer branding, auto-selected
- `Headshot-*`, `CEO-*` → Team section leadership
- `Staff-*`, `Team-Members-*` → About page team intro
- `Hero-*`, `Banner-*` → Full-width page heroes
- `Testimonial-*`, `Quote-*` → Testimonials carousel
- `Certificate-*`, `License-*`, `Award-*` → Trust/credentials section
- `Gallery-*`, `Portfolio-*` → Multi-image photo galleries (auto-grouped)
- `Slide-*`, `Carousel-*` → Slideshow/carousel sections (rotating, auto-sorted by number)

**Naming Rules:**
1. Use hyphens (not underscores): `Logo-Light-Mode.png`
2. Capitalize key words: `CEO-Headshot.jpg`
3. Be specific: `Developer-Alice.jpg` not `team-photo.jpg`
4. Include variants: `Logo-Light-Mode.png` + `Logo-Dark-Mode.png`
5. One purpose per file: don't combine purposes
6. Describe role: filename tells Claude what the photo is for
7. Gallery collections: `Gallery-Project-01.jpg`, `Gallery-Project-02.jpg` (sorted by number)
8. Slideshow candidates: `Slide-Feature-01.jpg`, `Carousel-Testimonials-01.jpg` (grouped and rotated)

**Claude Behavior:**
- Reads filename → interprets purpose
- Categorizes automatically → `hero/`, `team/`, `services/`, `gallery/`, `testimonials/`, etc.
- Places intelligently → no "put this here" questions
- Updates catalog → `_catalog.json` records recognized purpose
- Handles ordering → photos named `01`, `02`, `03` auto-sort

### Photo Naming Impact on Photo-Manager

**File Structure Changes:**
- `hero/` - Full-width heroes and banners
- `team/` - Team member headshots
- `services/` - Service/product images
- `gallery/` - Multi-image galleries AND slideshows
- `about/` - About page images
- `testimonials/` - Client/testimonial photos
- `branding/` - Logos and brand assets
- `misc/` - Everything else

**Logo Auto-Detection Algorithm:**
Scores logos by: file size (resolution), format (PNG RGBA > PNG RGB > others), aspect ratio (wide for headers, square for favicons), presence of transparency.

**Catalog Entry Enrichment:**
Each photo now includes `recognized_purpose` field based on filename pattern recognition.

## Established Patterns (Confirmed)

### Anti-Homogeneity Principle
**Confirmed across 8+ sectors:** No two websites should look identical. Sector templates are REFERENCE ONLY. Mandatory customization via sector-brief questionnaire enforces differentiation through unique colors, fonts, visual identity.

### Universal Design Guidelines
**Confirmed:** Single source of truth (UNIVERSAL-DESIGN-GUIDELINES.md) prevents duplication across sector skills. All skills reference it rather than duplicating content.

### Plain Language in Legal Documents
**Critical:** Both Privacy Policies and Terms of Use must use plain language (avoid jargon). Before/after examples show the transformation (dense legal → clear communication).

### Version Control for Long Documents
**Pattern:** Archive old versions with timestamps (v1.0, v2.0, v2.1) so users can see what changed. Include changelog in document.

## Anti-Patterns (To Avoid)

❌ Generic photo names (`IMG_001.jpg`, `photo1.png`) - forces Claude to ask for clarification
❌ Combining multiple purposes in one photo filename - splits photos instead
❌ Not including light/dark mode variants - limits theming options
❌ Dense legal language in policies - reduces trust and comprehension
❌ No version control on policy documents - users don't see change history
❌ Forgetting to update README.md when adding new skills
❌ Skills exceeding 500-line hard limit - use reference files for detailed content

## Critical Files & References

**Key Documentation:**
- `/README.md` - Main skills inventory with execution order
- `/CLAUDE.md` - AI guidance for working with skills
- `/universal-guidelines/UNIVERSAL-DESIGN-GUIDELINES.md` - 40 design principles
- `/sector-strategies/` - 8 industry-specific templates
- `/policy-pages/` - Privacy Policies + Terms of Use

**Common File Paths:**
- Skills always at `/{skill-name}/SKILL.md`
- Reference files at `/{skill-name}/references/{topic}.md`
- Asset templates at `/{skill-name}/templates/`
- Generated client files at `docs/`, `photo-bank/`, `src/`

## Maintenance Checklist

**After Adding New Skill:**
1. ✅ Create SKILL.md (under 500 lines)
2. ✅ Create reference files if detailed content needed
3. ✅ Add to CLAUDE.md (Utility or Build skills section)
4. ✅ Update README.md skills list + execution order
5. ✅ Run skill-safety-audit on the new skill
6. ✅ Test with a real client project
7. ✅ Update MEMORY.md with patterns
8. ✅ Commit all changes

**Photo Manager Workflow:**
1. Read photo filenames
2. Recognize patterns (Gallery, Slide, Logo, Headshot, etc.)
3. Categorize into appropriate folder
4. Update _catalog.json with recognized purpose
5. Auto-select best logo if multiple logo files exist

### Color Selection Skill (NEW)

**What:** Comprehensive skill for generating harmonious color palettes from brand colors using color theory.

**Key Pattern:** Color selection is design-driven, not random. Every palette should:
- Use color theory (7 fundamental schemes)
- Account for psychology (emotional responses vary by color and industry)
- Validate accessibility (4.5:1 contrast for text, 3:1 for UI)
- Consider industry context (healthcare ≠ e-commerce ≠ creative agencies)
- Support both light and dark modes

**File Structure:**
- `color-selection/SKILL.md` (282 lines, under 500-line hard limit)
- 7 reference guides (~2,500 lines total):
  * `color-theory-fundamentals.md` (370 lines) - HSL model, color wheel, harmony
  * `color-psychology.md` (380 lines) - Individual colors + psychology + cultural context
  * `color-schemes.md` (435 lines) - All 7 schemes with generation formulas
  * `industry-color-psychology.md` (391 lines) - 10+ industry-specific guidance
  * `accessibility-contrast.md` (334 lines) - WCAG standards + testing
  * `practical-application.md` (420 lines) - Real-world CSS components
  * `tools-resources.md` (346 lines) - 15+ tools + workflows
- `scripts/palette_generator.py` - CLI utility for palette generation

**7 Color Schemes Available:**
1. Monochromatic - One hue, varied saturation/lightness (60-30-10 distribution)
2. Analogous - Adjacent colors on wheel (harmonious, natural)
3. Complementary - Opposite colors on wheel (high contrast, dynamic)
4. Split-Complementary - Primary + complement neighbors (balanced contrast)
5. Triadic - 3 evenly-spaced colors (vibrant, balanced)
6. Tetradic - 4 colors in two pairs (complex, rich)
7. Achromatic - Grays, blacks, whites (timeless, sophisticated)

**Color Psychology Critical Insights:**
- Red: energy, urgency, appetite (avoid in healthcare/meditation)
- Blue: trust, calm, professionalism (most overused in tech)
- Green: growth, health, harmony (versatile across industries)
- Purple: creativity, luxury, imagination (trending 2024-2026)
- Orange: enthusiasm, warmth, playfulness (friendly, energetic)
- Yellow: optimism, happiness (hard to read - avoid for text)
- Saturation matters: 100% = bold/energetic, 50% = professional, <30% = sophisticated
- Lightness distribution: Dark (serious), Medium (readable), Light (gentle)

**Industry-Specific Guidance:**
- Healthcare: Blues, greens, whites (avoid reds, dark colors)
- Finance/Banking: Navy, grays, whites (very conservative)
- E-Commerce: Warm colors for appetite, bold CTAs (complementary schemes)
- Tech/SaaS: Blue (overused) → differentiate with purple, emerald, burnt orange
- Creative/Design: Bold, unexpected combinations (must demonstrate creativity)
- Professional Services: Navy + accent (trustworthy + modern)
- Education: Welcoming blues/greens (accessible for diverse learners)
- Food/Hospitality: Warm reds, oranges, browns (appetite-stimulating)
- Nonprofit: Mission-aligned colors (environmental = green, health = blue)
- Personal Branding: Reflect personality (memorable, authentic)

**Accessibility Requirements:**
- Text on background: 4.5:1 contrast (AA), 7:1 (AAA)
- Large text (18pt+): 3:1 contrast (AA), 4.5:1 (AAA)
- UI components: 3:1 contrast against adjacent colors
- Test with colorblind simulators (Coblis) - ~8% users affected
- Never use color alone to convey meaning (add text/icon/pattern)

**60-30-10 Rule (Essential for Balance):**
- 60% Primary color (backgrounds, large surfaces, brand identity)
- 30% Secondary color (supporting elements, section backgrounds)
- 10% Accent color (CTAs, highlights, alerts, focus points)
This distribution feels natural; violations cause visual discomfort.

**Dark Mode Strategy:**
- Adjust lightness inversely: light mode `hsl(240, 100%, 50%)` → dark mode `hsl(240, 100%, 65%)`
- Same hue, opposite lightness
- CSS custom properties enable automatic switching with `@media (prefers-color-scheme: dark)`

**Palette Generator Script Usage:**
```bash
python palette_generator.py 3B82F6 semantic      # Generate complete palette
python palette_generator.py DC2626 triadic       # Generate triadic scheme
python palette_generator.py 10B981 monochromatic # Generate monochromatic
```

**Output Formats:**
- CSS custom properties (for global.css)
- Tailwind config format (for tailwind.config.mjs)
- JSON for tools/systems
- Design tokens for Figma

### App Landing Pages Sector (NEW)

**What:** New sector template for building high-converting app landing pages for your own app projects.

**Files Created:**
1. `sector-strategies/templates/app-landing-pages/design-tokens.md` (414 lines)
   - Color strategies by app type (5 categories with palettes)
   - Typography system (mobile-first, responsive scaling)
   - Component patterns (hero, cards, testimonials, CTAs, buttons)
   - Layout patterns (mobile/tablet/desktop)
   - Spacing system (8px grid)
   - Visual hierarchy and hierarchy principles
   - Motion/animations with performance consideration
   - Responsive breakpoints
   - Dark mode color mapping
   - Accessibility checklist
   - Performance targets (< 3 seconds load, LCP < 2.5s)

2. `sector-strategies/templates/app-landing-pages/implementation-guide.md` (550+ lines)
   - Phase 1: Strategy & Content (goal definition, problem-solution, benefits, audience, headline, subheadline)
   - Phase 2: Visual Planning (framework selection, asset planning, color/font choice)
   - Phase 3: Build Page Structure (sections checklist, copy writing, asset gathering)
   - Phase 4: Design Mockups (wireframes, high-fidelity mockups, feedback)
   - Phase 5: Build the Page (development setup, semantic HTML, responsive CSS, interactivity)
   - Phase 6: Optimize & Launch (performance optimization, tracking setup, accessibility audit)
   - Phase 7: Optimize & Iterate (weekly analysis, A/B testing roadmap, quarterly refresh)
   - Complete templates and checklists for each phase

3. `sector-strategies/templates/app-landing-pages/conversion-strategies.md` (500+ lines)
   - Core concepts (why app landing pages matter, 10 essential components)
   - 5 proven conversion frameworks:
     * AIDA (Attention → Interest → Desire → Action)
     * PAS (Problem → Agitation → Solution)
     * FAB (Features → Advantages → Benefits)
     * Hero's Journey (narrative structure)
     * Mobile-First Conversion Path (thumb-driven scrolling)
   - Copy formulas (headline formula, feature vs. benefit, microcopy)
   - Visual design (60-30-10 rule, visual hierarchy, color psychology)
   - Social proof strategies (types, testimonials, trust badges, placement)
   - CTA optimization (anatomy, copywriting, testing variables)
   - Performance optimization (speed impact, Core Web Vitals, image optimization)
   - A/B testing strategy (what to test, testing process, statistical significance)
   - Analytics & measurement (key metrics, tracking setup, heatmaps)
   - 10 common mistakes to avoid

**Key Insight:** App landing pages are NOT generic websites—they're conversion-optimized experiences designed specifically to drive app installs or sign-ups.

**Differentiation from Other Sectors:**
- Focus on CONVERSION (not brand/trust alone)
- Heavy emphasis on A/B testing and iteration
- Mobile-first mandatory (80% of traffic is mobile)
- Complete analytics implementation required
- 5 proven frameworks specific to app discovery
- Includes CTA psychology and optimization

**5 App Type Palettes Provided:**
1. **Productivity** — Blue + Green (professionalism + action)
2. **Health/Wellness** — Green + Coral (wellness + energy)
3. **Entertainment** — Magenta + Gold (fun + premium)
4. **Finance** — Navy + Green (trust + growth)
5. **Social** — Purple + Coral (modern + connection)

**Conversion Frameworks Covered:**
- AIDA: Best for awareness-focused campaigns
- PAS: Best for pain-point focused solutions
- FAB: Best for tech-forward audiences
- Hero's Journey: Best for transformation apps
- Mobile-First Path: Best for all apps (80%+ mobile traffic)

**CTA Testing Variables:**
Copy, color, size, position, button style, icon — each systematically tested

**A/B Testing Roadmap:**
Week 1: Headlines | Week 2: CTA color | Week 3: Hero visual | Week 4: Social proof | Week 5: Benefit order | Week 6: Implement winners

**Key Metrics to Track:**
CTR, Conversion Rate, Bounce Rate, Time on Page, Scroll Depth, Exit Rate

**Performance Targets:**
- Page load < 3 seconds
- LCP < 2.5s (Largest Contentful Paint)
- CLS < 0.1 (Cumulative Layout Shift)
- Images < 100KB each
- Total page < 500KB

**Why This Sector Exists:**
Unlike client sectors (which need multiple pages, navigation, content systems), app landing pages have a SINGLE goal: drive conversions (downloads, sign-ups). This sector provides templates specifically designed for this constraint.

---

**Last Updated:** 2026-02-17
**Skills Added:** policy-pages, color-selection
**Sectors Added:** app-landing-pages
**Enhancements:** Photo naming conventions, gallery/slideshow recognition, comprehensive color theory framework, app landing page conversion optimization
