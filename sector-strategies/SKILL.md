---
name: sector-strategies
description: Industry-specific website design strategies and templates. Use when building websites for different business sectors (tour & travel, corporate & consulting, education, healthcare, e-commerce, professional services, hobbyist creators) to ensure the site reflects sector-specific design psychology, trust cues, and visual identity. Choose your sector → customize template → get industry-authentic design that doesn't look AI-generated.
---

## Why Sector Strategy Matters

Generic websites scream "AI-generated." Industry-specific design psychology makes sites trustworthy and distinctive.

A tour company's website needs wanderlust and discovery cues (warm palettes, adventure typography, destination imagery). A school's website needs credibility and safety (clear hierarchy, professional fonts, enrollment clarity). A hospital's website needs trust and accessibility (calming colors, readable type, appointment CTAs).

Same CMS. Different psychology. Different trust signals. Different components. Different content order.

This skill provides templates for seven core sectors, each with:
- **Design tokens** (colors, typography, spacing optimized for that sector)
- **Component patterns** (buttons, cards, CTAs that convert in that industry)
- **Content architecture** (what users expect to see first)
- **Trust signals** (what makes that sector's sites credible)

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

## How to Use This Skill

### Step 1: Choose Your Sector

Read the sector descriptions above. Which best matches your client's business?

If multiple apply, choose the **primary customer intent**:
- Eco-tourism education? → Tourism (primary) with education trust signals
- Specialty clinic in hospital? → Healthcare (primary) with professional services polish
- Creator selling courses? → Hobbyist/Creator (primary) with professional services credibility

### Step 2: Customize Your Sector Brief

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

Open it and answer these core questions:
1. What are your **unique value propositions** compared to competitors?
2. What **trust signals** matter most to your ideal customer?
3. What **action** do you want visitors to take first? (book, enroll, purchase, contact, subscribe)
4. What **visual personality** matches your brand? (bold vs. subtle, modern vs. heritage, playful vs. serious)
5. What **competitor sites** should we reference? (design-reference skill will analyze these)

Save as `docs/sector-brief.md`. The design-system skill will read this.

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

Each `sector-strategies/templates/{sector}/` contains three files:

**sector-brief-template.md**
Customization questions for your client. Copy to `docs/sector-brief.md` and fill in answers.

**design-tokens.md**
Reference palette: colors, typography, spacing rules, component sizes. Not auto-applied; used by design-system skill to inform its output.

**component-patterns.md**
HTML/Tailwind examples for sector-specific UI: buttons, cards, CTAs, forms. Reference when building custom components.

## Common Questions

**Q: Can I mix sectors?**
A: No. Choose one primary sector and lean into it. Mixing dilutes trust signals.

**Q: My sector isn't listed. What do I do?**
A: Start with the closest sector template. Customize it. After delivery, document what worked and propose it as a new sector template.

**Q: When do I customize sector-brief.md?**
A: Before running design-system. It needs your sector-brief answers to generate correct design tokens.

**Q: Can I skip this skill?**
A: Technically yes, but then your design-system output will be generic. This skill prevents that.

## Next Steps

1. Choose your sector from the list above
2. Copy `sector-strategies/templates/{sector}/sector-brief-template.md` → `docs/sector-brief.md`
3. Answer all customization questions in your brief
4. Run the `design-system` skill
5. Proceed with photo-manager, page-builder, deploy
