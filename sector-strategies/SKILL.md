---
name: sector-strategies
description: Industry-specific website design strategies and templates. Use when building websites for different business sectors (tour & travel, corporate & consulting, personal & portfolio, education, healthcare, e-commerce, professional services, hobbyist creators) to ensure the site reflects sector-specific design psychology, trust cues, and visual identity. Choose your sector → customize template → get industry-authentic design that doesn't look AI-generated.
---

## Why Sector Strategy Matters

Generic websites scream "AI-generated." Industry-specific design psychology makes sites trustworthy and distinctive.

A tour company's website needs wanderlust and discovery cues (but each tour operator needs DIFFERENT colors and fonts). A school's website needs credibility and safety (but each school needs UNIQUE visual identity). A hospital's website needs trust and accessibility (but each hospital needs DIFFERENT design choices).

**Key principle: No two websites built with these skills should look the same.**

Same build pipeline. Same component structure. Different psychology. Different trust signals. Different components. Different content order. **DIFFERENT VISUAL IDENTITY.**

This skill provides templates for nine core sectors to ensure sector-appropriate design psychology. But customization is REQUIRED to prevent homogeneity:
- **Design tokens** (reference palettes — not prescriptive)
- **Sector-brief template** (customization questionnaire — REQUIRED to answer)
- **Component patterns** (patterns to follow, with YOUR styling)
- **Trust signals framework** (what matters in that sector)

## Universal Guidelines

All sector templates are built on **Universal Design Guidelines** which cover:
- Purpose-driven design and visual hierarchy
- User-centered design and UX fundamentals
- Color theory, typography, spacing standards
- Accessibility requirements (WCAG 2.1 AA)
- Mobile-first responsive design
- Trust and credibility signals
- Navigation best practices
- Conversion optimization
- SEO fundamentals

Sector strategies LAYER ON TOP OF these universal principles, adding industry-specific trust cues, content architecture, and design psychology.

## How This Integrates

Sector-strategies is **step 0.5** in the build pipeline:

```
0. design-reference (optional)
→ 0.5 sector-strategies (YOU CHOOSE SECTOR) ← NEW
→ 1. design-system (reads docs/sector-brief.md)
→ 2. photo-manager
→ 3. page-builder
→ 4. deploy
```

Once you choose a sector and customize your brief, `design-system` uses it to generate tailwind.config.mjs and design-tokens.md with your sector's visual identity baked in.

## Available Sectors

**CRITICAL: Each sector template below is a CUSTOMIZATION STARTING POINT, not a final design. Your site must differentiate within your sector through:**
- Unique color palette (not the reference palette)
- Distinctive font pairing (not the example fonts)
- Your specific market positioning (budget vs. luxury, established vs. startup, etc.)
- Your competitor differentiation strategy

Read each sector description, then customize your sector-brief.md to reflect YOUR unique brand.

---

### Tour & Travel

**Trust cues**: Wanderlust, authentic experiences, community, discovery
**Visual identity**: Warm earth tones + sunset gradients; serif (heritage) + playful display font
**Key components**: Destination cards, itinerary timelines, booking widgets, experiential imagery
**Content order**: Hero + adventure CTA → Popular destinations → Travel guides → Testimonials → Booking
**Distinctive traits**: Real photography, storytelling copy, "you could be there" language

### Corporate & Consulting

**Trust cues**: Leadership, expertise, client wins, market authority, thought leadership
**Visual identity**: Deep navy + slate gray + accent blue; professional sans-serif + serif accents
**Key components**: Hero with value prop, mega menu, leadership team, company stats, case studies, investor relations
**Content order**: Hero + demo CTA → Solutions grid → Case studies → Leadership team → Insights hub → Contact
**Distinctive traits**: Professional photography, credential visibility, testimonials/client logos, downloadable resources, demo booking flow

### Personal & Portfolio

**Trust cues**: Authenticity, personality, quality work, expertise, approachability
**Visual identity**: Personalized colors + distinctive fonts that reflect individual brand (NOT defaults)
**Key components**: Hero with personality, portfolio/projects grid, about section, skills/experience, blog (optional), contact CTA
**Content order**: Hero + primary CTA → Featured projects → About/story → Skills or experience → Contact
**Distinctive traits**: Personal photo/branding, curated project showcase, authentic storytelling, unique visual identity, blog (if applicable)

### Education

**Trust cues**: Credibility, structure, student success, enrollment
**Visual identity**: Clean sans-serif + readable serif; primary colors + professional gray
**Key components**: Course catalog, staff directory, event calendar, application CTAs
**Content order**: Hero + enrollment CTA → Academics grid → Faculty profiles → Events → Apply
**Distinctive traits**: Clear hierarchy, accreditation badges, student testimonials, enrollment clarity

### Healthcare

**Trust cues**: Expert credentials, patient safety, accessibility, appointment availability
**Visual identity**: Calming blue-green + trust neutrals; accessible sans-serif with generous spacing
**Key components**: Specialty finder, doctor profiles, appointment button, insurance badges, hours
**Content order**: Hero + appointment CTA → Specialties → Doctors → Hours/Insurance/Accessibility → Contact
**Distinctive traits**: Accessibility-first, credential visibility, frictionless appointment booking

### E-commerce

**Trust cues**: Product quality, customer reviews, fast checkout, secure payment
**Visual identity**: Bold accent + trust neutrals; clean sans-serif for product names
**Key components**: Product cards with reviews, quantity selectors, checkout CTA, trust badges (secure, returns)
**Content order**: Hero + shop CTA → Featured products → Customer reviews → Policy clarity → Checkout
**Distinctive traits**: Social proof (reviews), urgency signals (in-stock), transparent pricing and returns

### Professional Services

**Trust cues**: Expertise, credentials, client wins, established track record
**Visual identity**: Sophisticated palette (navy/charcoal + one accent); premium spacing
**Key components**: Service cards, team profiles, client logos, case study cards, contact CTA
**Content order**: Hero + service menu → Services grid → Team bios → Case studies → Testimonials → Contact
**Distinctive traits**: Portfolio/case studies, expert bios, premium photography, credential visibility

### Hobbyist/Creator

**Trust cues**: Authenticity, personal brand, niche expertise, behind-the-scenes, community
**Visual identity**: Bold personality-driven fonts; high-saturation accent + authentic substrate
**Key components**: Portfolio grid, process/behind-scenes, subscribe CTA, community signals
**Content order**: Hero + personality → Best work → Process/behind-scenes → Community/subscribe → Contact
**Distinctive traits**: Personal voice, authentic storytelling, niche focus, less corporate, more human

### App Landing Pages

**💡 For app developers building their own landing pages**

**Trust cues**: Conversion-focused design, social proof, clear value proposition, urgency/scarcity
**Visual identity**: Varies by app type (see design-tokens.md for 5 category-specific palettes)
**Key components**: Hero with sticky CTA, benefit cards, demo video/screenshots, testimonials, FAQ, app store badges
**Content order**: Hero + CTA → Key benefits → How it works → Social proof → FAQ → Download CTA
**Distinctive traits**: Mobile-first design (80% traffic), conversion optimization focus, clear problem-solution narrative

**Special note:** Unlike client sectors, app landing pages emphasize conversion frameworks (AIDA, PAS, FAB, Hero's Journey) and include comprehensive A/B testing strategies.

## How to Use This Skill

### Step 1: Choose Your Sector

Read the sector descriptions above. Which best matches your client's business?

If multiple apply, choose the **primary customer intent**:
- Eco-tourism education? → Tourism (primary) with education trust signals
- Specialty clinic in hospital? → Healthcare (primary) with professional services polish
- Creator selling courses? → Hobbyist/Creator (primary) with professional services credibility

### Step 2: Customize Your Sector Brief (REQUIRED — Do Not Skip)

**CRITICAL: This step determines whether your site looks generic or distinctive.**

Copy the sector template into your client project:

```
your-client-project/
├── docs/
│   ├── company-profile.md    (client provides)
│   ├── services.md           (client provides)
│   ├── style-brief.md        (client provides)
│   └── sector-brief.md       ← COPY TEMPLATE HERE & CUSTOMIZE
```

Template location: `sector-strategies/templates/{sector}/sector-brief-template.md`

**Answer EVERY question thoroughly:**
1. **What is your ONE unique difference** compared to competitors?
2. **Define YOUR brand colors** (not the sector reference palette)
3. **Choose YOUR fonts** (not the example fonts — use Fontsource for distinctive options)
4. **What is your visual style?** (photography approach, vibe, distinctive traits)
5. **How do you build trust?** (rank trust elements by importance)
6. **What is your ideal customer's pain point?** (this shapes emotional design)

**Do NOT:**
- Use the reference colors directly
- Use example fonts without customizing
- Skip the differentiation questions
- Default to the sector template — customize it for YOUR brand

Save as `docs/sector-brief.md`. The design-system skill will read this brief and generate YOUR unique visual identity.

### Step 3: Run design-system

The design-system skill now has three inputs:
1. `docs/sector-brief.md` (from this skill)
2. `docs/style-brief.md` (from client)
3. `sector-strategies/templates/{sector}/design-tokens.md` (reference palette)

It generates:
- `tailwind.config.mjs` (sector-optimized colors, typography, spacing)
- `design-tokens.md` (your sector's visual language)
- `src/styles/global.css` (animations, utilities, reset for sector)

### Step 4: Continue Pipeline

photo-manager → page-builder → deploy

---

## What's in the Templates

Each `sector-strategies/templates/{sector}/` contains files to guide customization:

**sector-brief-template.md** ⭐ CRITICAL
Customization questionnaire for your client. Copy to `docs/sector-brief.md` and fill in EVERY answer.
- This questionnaire drives differentiation
- Your answers shape the design-system output
- Skipping this results in generic design
- REQUIRED: Answer all sections fully

**design-tokens.md** (REFERENCE ONLY)
Reference palette showing ONE example of how this sector could be designed.
- Example colors (NOT to be used as-is)
- Example typography (NOT to be used as-is)
- Color psychology (to inform YOUR choices)
- DO NOT use these directly — customize them via your sector-brief
- Anti-homogeneity principle: Every site needs different colors/fonts

**component-patterns.md**
HTML/Tailwind examples for sector-specific UI patterns: buttons, cards, CTAs, forms.
- Use these as pattern inspiration
- Style them with YOUR brand colors/fonts
- Do not copy directly — adapt to your visual identity

## Common Questions

**Q: Will all sites in the same sector look the same?**
A: NO — if you customize your sector-brief properly. Each site will have unique colors, fonts, and visual identity. The sector framework ensures trust signals are appropriate to the industry. Customization ensures differentiation.
- Bad: Use tour-travel template defaults → all travel sites look similar
- Good: Answer your sector-brief with unique colors/fonts → distinctive travel site

**Q: Can I skip the sector-brief customization?**
A: NO. This results in generic design. The sector-brief is REQUIRED to drive differentiation.

**Q: Can I mix sectors?**
A: No. Choose one primary sector and lean into it. Mixing dilutes trust signals. If your business is hybrid (e.g., eco-tourism education), choose the PRIMARY sector and customize the sector-brief to address secondary aspects.

**Q: My sector isn't listed. What do I do?**
A: Start with the closest sector template. Customize the sector-brief fully. After delivery, document what worked and propose it as a new sector template for the library.

**Q: When do I customize sector-brief.md?**
A: Before running design-system. The design-system skill reads your sector-brief to generate YOUR unique visual identity.

**Q: How do I ensure my site doesn't look like another site?**
A:
1. Complete your sector-brief with genuine differentiation answers
2. Choose unique colors (not the reference palette)
3. Choose distinctive fonts from Fontsource
4. Have design-reference analyze your competitors (so you know what to avoid)
5. Let design-system generate unique output based on your inputs

## Next Steps

1. Choose your sector from the list above
2. Copy `sector-strategies/templates/{sector}/sector-brief-template.md` → `docs/sector-brief.md`
3. Answer all customization questions in your brief
4. Run the `design-system` skill
5. Proceed with photo-manager, page-builder, deploy
