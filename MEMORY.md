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

---

**Last Updated:** 2026-02-17
**Skills Added:** policy-pages
**Enhancements:** Photo naming conventions, gallery/slideshow recognition
