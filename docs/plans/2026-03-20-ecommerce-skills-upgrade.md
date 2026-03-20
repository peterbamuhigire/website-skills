# Ecommerce Skills Upgrade Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Upgrade the existing `ecommerce/SKILL.md` with cross-cutting principles from 8 books, then build three new companion skills: `ecommerce-funnel/`, `ecommerce-checkout/`, and `ecommerce-analytics/`.

**Architecture:** Hybrid approach — existing skill gets cross-cutting upgrades (brand vs product, conversion trinity, social commerce layer, Larsson's 12 principles); new companion skills each own a distinct domain with reference files for deep content. All skills stay under the 500-line hard limit.

**Sources:** Judah Phillips (analytics), Digital Growth Books (idea to success), Alex Harris (small biz online), Sarka Zapletalova (customer behaviour), Francisco Martinez-Lopez (digital marketing advances), Tanner Larsson (ecommerce evolved), Stephan Spencer (social ecommerce), Neil Verma (checkout/brand).

---

## Task 1: Upgrade `ecommerce/SKILL.md`

**Files:**
- Modify: `ecommerce/SKILL.md` (currently 233 lines → target ~380 lines)

**Step 1: Read the current file**

```bash
# Confirm current line count before editing
wc -l ecommerce/SKILL.md
```

**Step 2: Add Larsson's 12 Core Principles section after the existing intro**

Insert after line 8 (after "Design and build e-commerce..." sentence), before "## The CLICK System":

```markdown
## The 12 Core Principles (Larsson)

These principles define whether an ecommerce business succeeds before any design decisions are made. Audit every client project against these:

1. **Your business is not unique** — execution wins, not novelty. Stop searching for a secret and start executing better than competitors.
2. **Your business IS marketing** — product without marketing is invisible. Marketing is the growth engine, not an afterthought.
3. **Brand-centric, not product-centric** — products change, brands endure. Build the brand first; it lowers CAC and raises LTV permanently.
4. **Control the order process** — own the checkout, the data, and the customer relationship. Never fully depend on third-party marketplaces.
5. **Never compete on price** — price competition destroys margins. Compete on differentiation, expertise, experience, or community.
6. **Niche down** — 20% of the market holds 80% of the revenue. A focused niche beats a generic store every time.
7. **There is no free traffic** — organic, social, and referral traffic all require time or money investment. Budget accordingly.
8. **Spending is required** — successful ecommerce requires CAC (customer acquisition cost) investment. Refusing to spend is refusing to grow.
9. **Mobile-first is mandatory** — design for 375px first, enhance upward. Mobile is the primary purchase platform.
10. **Highest CAC budget wins** — in any category, the business that can profitably spend the most to acquire a customer wins market share.
11. **Multi-channel distribution** — no single channel owns the customer. Own + shared + paid channels working together.
12. **Three growth levers only** — increase number of customers, increase average order value, increase repeat purchases. Every tactic maps to one of these.
```

**Step 3: Add Brand vs Product Distinction section**

Append before `## Trust Signals`:

```markdown
## Brand vs. Product (Verma)

**A product is functional. A brand is emotional.**

| Product | Brand |
|---------|-------|
| What it does | How it makes you feel |
| Can be copied | Hard to replicate |
| Competes on price | Commands premium |
| Replaced by better products | Outlives individual products |

**Two value propositions to define for every client:**
- **UVP (Unique Value Proposition)** — functional: "What does it do better?" Used on product pages.
- **EVP (Emotional Value Proposition)** — psychological: "How does it make the customer feel? Who does it help them become?" Used in brand storytelling, hero sections, and checkout.

EVP is what reduces price sensitivity. A customer who connects emotionally with a brand does not shop for a cheaper alternative.
```

**Step 4: Add Conversion Trinity section (Harris)**

Append after the Brand vs Product section:

```markdown
## Conversion Trinity (Harris)

Humans navigate websites like animals following a scent trail — they follow information scent. If the trail goes cold, they leave.

**Three forces that kill or create conversions:**

1. **Information scent** — every page element must signal "you're getting closer to what you want." Headlines, images, CTAs, and navigation must form a coherent trail from ad → landing page → product → checkout.
2. **Persuasion architecture** — structure copy and layout to move visitors through: Awareness → Interest → Desire → Action. Each stage needs different content (facts for awareness, benefits for interest, proof for desire, urgency for action).
3. **Value proposition clarity** — answer four questions on every key page within 5 seconds:
   - What do you offer?
   - For whom?
   - Why is it better than alternatives?
   - Why should I believe you?

**Harris's MOS (Marketing Optimization System):**
- Phase 1: Strategic Evaluation — understand customer psychology and competitive landscape before building anything
- Phase 2: Five-Step Process — Discover → Hypothesise → Execute → Review → Scale
- Phase 3: Growth Plan — implement winners, kill losers, never stop testing
```

**Step 5: Add Social Commerce Layer (Spencer)**

Append after Conversion Trinity:

```markdown
## Social Commerce Layer (Spencer)

Social channels are not separate from the website — they feed it.

**Three-tier social network strategy:**
- **Tier 1** (broad reach): Facebook, Instagram, LinkedIn — product showcasing, paid ads, retargeting
- **Tier 2** (specialized): YouTube, Pinterest — tutorials, inspiration, discovery
- **Tier 3** (niche): Reddit, Quora — community participation, trust-building, long-tail traffic

**Key integration rules:**
- Install the Meta Pixel on every page — enables retargeting cart abandoners and building lookalike audiences
- UGC (user-generated content) on product pages outperforms studio photography for trust — build systems to collect and display it
- Community-first approach: participate in niche communities before promoting to them
- White-hat only: authentic engagement, value-first content. Fake reviews, bot engagement, and manufactured social proof destroy trust permanently.
- ROI formula: (conversion rate × average order value × customer lifetime multiplier) must exceed cost per click before scaling any channel
```

**Step 6: Verify line count is under 500**

```bash
wc -l ecommerce/SKILL.md
```

Expected: under 500 lines.

**Step 7: Commit**

```bash
git add ecommerce/SKILL.md
git commit -m "feat(ecommerce): add Larsson 12 principles, brand/product distinction, conversion trinity, social commerce layer"
```

---

## Task 2: Create `ecommerce-funnel/SKILL.md`

**Files:**
- Create: `ecommerce-funnel/SKILL.md`
- Create: `ecommerce-funnel/references/funnel-architecture.md`
- Create: `ecommerce-funnel/references/email-sequences.md`

**Step 1: Create the skill directory and SKILL.md**

```markdown
---
name: ecommerce-funnel
description: Ecommerce funnel strategy and customer lifecycle management. Use when building the customer journey beyond the product catalog — from cold stranger to loyal repeat buyer. Covers customer avatar creation, traffic temperature segmentation, funnel architecture (front-end → upsell → recurring), email campaign types, customer lifecycle stages, and the three growth levers. Companion to the ecommerce skill.
---

# Ecommerce Funnel Skill

Build the hidden 2/3 of ecommerce success: the customer journey, funnel architecture, and retention systems that turn one-time buyers into long-term revenue.

## The Iceberg Effect (Larsson)

Visible ecommerce (the site, the catalog, the traffic) is 1/3 of what drives success. Hidden below the surface:
- Customer psychology and avatar depth
- Funnel architecture (separate from the storefront)
- Retention mechanics and lifecycle management
- Data infrastructure and testing culture
- Team alignment on brand and positioning

Build the hidden layers before spending on traffic.

## Step 1: Customer Avatar Framework

Before building any funnel, define the customer avatar. Funnels built for "everyone" convert no one.

**Demographics (minimum):**
- Age range, gender, location
- Income bracket and spending patterns
- Job/role and daily schedule constraints

**7 Emotional Questions:**
1. What do they lie awake worrying about at night?
2. What do they deeply desire but feel embarrassed to admit?
3. What do they resent in their current situation?
4. What do they fear most about making the wrong purchase decision?
5. What does success look like to them 90 days after buying?
6. Who do they aspire to become?
7. What language do they use to describe their problem (exact words, not marketing speak)?

**10 Behavioural Questions:**
1. Where do they spend time online?
2. What content do they consume (YouTube channels, blogs, podcasts)?
3. What do they buy repeatedly in this category?
4. What have they tried before that didn't work?
5. What objections do they have before buying?
6. How do they research purchases? (reviews, experts, friends, specs)
7. What triggers the decision to buy now vs. later?
8. How price-sensitive are they?
9. What competing products have they considered?
10. How did they first hear about this category?

Use the avatar's exact language in headlines, product descriptions, and email subject lines.

## Step 2: Traffic Temperature

Not all visitors are equal. Messaging must match the visitor's relationship with the brand.

| Temperature | Who They Are | What They Need | What to Show |
|-------------|--------------|----------------|--------------|
| **Cold** | No brand awareness | Reason to trust | Value-first content, brand story, proof of credibility |
| **Warm** | Aware, considering | Reason to choose you | Differentiation, comparison, reviews, guarantees |
| **Hot** | Past buyers, cart abandoners | Reason to return | Personalised offers, loyalty rewards, win-back campaigns |

**Traffic sources by temperature:**
- Cold: social ads to new audiences, SEO, influencer reach
- Warm: retargeting (pixel-based), email list (leads not yet bought), lookalike audiences
- Hot: post-purchase email sequences, SMS, loyalty programme, retargeting past buyers

Never send cold-traffic messaging to hot-traffic audiences. They already know you — skip the introduction.

## Step 3: Funnel Architecture

The funnel runs parallel to the main storefront. It is a focused, sequential conversion path.

```
[Traffic Entry] → [Front-End Offer] → [Order Bump] → [Upsell] → [Downsell] → [RIC Offer]
```

**Front-End Offer:**
- Low-price, high-perceived-value product (tripwire or loss leader)
- Goal: convert a stranger into a buyer. Even a small purchase changes psychology.
- Must deliver genuine value — this is the trust-builder.

**Order Bump:**
- Shown on the checkout page, before payment is submitted
- Complementary product: "Add [X] to your order for just [price]" with a checkbox
- Should feel like an obvious upgrade, not a hard sell
- Target: 20-35% of buyers take the order bump

**Upsell (OTO — One Time Offer):**
- Shown immediately after purchase confirmation, before the thank-you page
- Higher-value version, bundle, or logical next product
- "Since you just bought X, you can add Y at a special price — this offer expires when you leave this page"
- Target: 15-25% uptake

**Downsell:**
- Shown if upsell is declined
- Smaller version of the upsell at a lower price, or a payment plan option
- "Not ready for the full bundle? Get just [core component] for [lower price]"

**Recurring Income Core (RIC):**
- Subscription, membership, or replenishment offer
- Highest lifetime value mechanism in ecommerce
- Can be front-loaded (subscribe to get the deal) or back-loaded (offered after initial purchase)

## Step 4: Three Customer Tiers

Not all buyers are equal. Identify and treat each tier differently.

| Tier | Who They Are | Strategy |
|------|--------------|----------|
| **Repeat Buyers** | Bought 2+ times | Loyalty programme, early access, VIP offers |
| **Continuity** | Active subscribers | Retention emails, usage tips, community access |
| **Whales** | 10x+ average order value | Personal outreach, bespoke bundles, premium service |

Whales are rare (2-5% of customers) but can represent 20-40% of revenue. Identify them early via purchase data and treat them accordingly.

## Step 5: Customer Lifecycle Management

Every customer moves through stages. Each stage needs different messaging.

```
New → Active → At-Risk → Lapsed
```

**New (0-30 days post-purchase):**
- Indoctrination email sequence (see references/email-sequences.md)
- Welcome to the brand, set expectations, deliver value immediately
- Introduce community, content, or loyalty programme
- Invite first review

**Active (regular purchasers):**
- Bucket promotions (seasonal, event-driven)
- Cross-sell and upsell based on purchase history
- Basket analysis: identify products frequently bought together and recommend proactively

**At-Risk (purchase frequency dropping):**
- Trigger: no purchase in [category-average interval × 1.5]
- Re-engagement offer: exclusive deal, new product launch, personal note
- Survey: "We miss you — what can we do better?"

**Lapsed (inactive beyond threshold):**
- Win-back campaign: compelling offer with time limit
- If no response after 3 win-back attempts: move to suppression list (do not spam)

## Step 6: RIC Metrics — Measuring Subscription Health

If the funnel includes a recurring offer, track these three metrics monthly:

| Metric | Formula | Target |
|--------|---------|--------|
| **Churn Rate (CR)** | Cancellations ÷ Active subscribers | Under 5%/month |
| **Customer Count Retention (CCR)** | Active subscribers this month vs. last | Growing or stable |
| **ASRC** | Total subscription revenue ÷ Active subscribers | Trending up |

Churn above 10%/month means the product or delivery experience has a fundamental problem. Fix before scaling.

## Integration

- **ecommerce** — base skill for product page UX, trust signals, cart, mobile
- **ecommerce-checkout** — brand foundation and checkout UX that feeds into the funnel
- **ecommerce-analytics** — measures funnel performance, cohort retention, CLV
- **sales-copywriting** — PASTOR and 4P's frameworks for funnel page copy
- **email-sender** — technical implementation of PHP + PHPMailer for transactional emails
```

**Step 2: Create `ecommerce-funnel/references/funnel-architecture.md`**

```markdown
# Funnel Architecture Reference

## Funnel Page Sequence

```
Landing Page → Checkout Page → Order Bump (on checkout) → Purchase Confirmation
    ↓                                                              ↓
Lead Magnet                                                  Upsell Page
(cold traffic)                                                     ↓
                                                           Upsell Accepted?
                                                          Yes → Thank You Page
                                                          No  → Downsell Page
                                                                     ↓
                                                              Thank You Page
```

## Offer Types by Funnel Position

### Front-End Offers
- **Tripwire** — irresistible low-price offer ($7-27) designed to convert strangers into buyers
- **Loss Leader** — sell at cost or slight loss; recoup on back-end offers
- **Free + Shipping** — zero product cost, pay only postage; high conversion, lower margins

### Order Bumps (Checkout Page)
- Must be complementary, not competitive with the main product
- Best performers: protective cases for electronics, ingredient refills, extended warranties, digital guides complementing physical products
- Copy formula: "Add [product] to your order — [one-sentence benefit]. Normally [price], today just [discounted price]."

### Upsells (Post-Purchase)
- **Bigger/Better** — premium version of what they just bought
- **More of the Same** — bulk purchase at a discount
- **Complementary Product** — logical next purchase
- **Bundle** — curated set at a discount vs. buying individually

### Downsells (After Upsell Decline)
- Stripped-down version of upsell
- Payment plan (same total, spread over 3-6 months)
- Single item from a bundle at individual price

### Recurring Income Core (RIC)
- **Replenishment Subscription** — consumables reordered automatically (coffee, supplements, skincare)
- **Curated Box** — monthly selection of products in a niche
- **Membership** — access to community, content, or exclusive pricing
- **Service Retainer** — ongoing support, coaching, or maintenance

## Funnel Copy Framework

Each funnel page follows this structure:

1. **Headline** — Calls out the customer avatar and the desire/problem
2. **Subheadline** — Clarifies the specific offer and primary benefit
3. **Social proof** — Reviews, case studies, or testimonials above the fold
4. **Offer presentation** — What they get, what it's worth, what they pay
5. **Proof stack** — More reviews, before/after, credentials, press
6. **Guarantee** — Remove risk. 30-day money back is minimum.
7. **CTA** — One clear action. No navigation. No exit links.
8. **Objection handling** — FAQ below the CTA

## Basket Analysis for Cross-Sell

Products frequently bought together can be identified via order history. For each top product, identify:
- What product is bought in the same order? → Bundle these.
- What product is bought 30-60 days later? → Trigger email/offer at day 25.
- What product is never bought together? → Do not cross-sell these.

## Promotion Calendar Framework

Plan promotions quarterly. Categories:

| Type | Examples | Frequency |
|------|----------|-----------|
| Holiday/Seasonal | Christmas, Eid, Diwali, Easter | 4-6/year |
| Commercial | Black Friday, Cyber Monday, Mother's Day | 6-8/year |
| Brand | Brand anniversary, product launch, milestone | 2-4/year |
| Niche | Category-specific awareness days | 2-4/year |
| Cause/Charity | Charitable tie-in, community event | 1-2/year |

Never discount without a reason. Reasons justify price cuts without training customers to wait for sales.
```

**Step 3: Create `ecommerce-funnel/references/email-sequences.md`**

```markdown
# Email Sequence Reference

## The Four Campaign Types (Larsson)

### 1. Indoctrination Sequence (Welcome)
**Trigger:** First purchase or opt-in
**Goal:** Transform a new buyer into a brand believer before they have time to experience buyer's remorse.

| Email | Timing | Content |
|-------|--------|---------|
| 1 | Immediately | Order confirmation + what to expect next |
| 2 | Day 1 | Brand origin story — why this exists, who founded it, what it stands for |
| 3 | Day 3 | Your product's backstory — why this specific product, what makes it different |
| 4 | Day 5 | Community introduction — join the group, follow social, meet other customers |
| 5 | Day 7 | First cross-sell — "customers who bought X also love Y" with social proof |
| 6 | Day 14 | Review request — "has your order arrived? We'd love your feedback" |

**Tone:** Warm, personal, story-driven. Not promotional. Not corporate.

### 2. Core Offer Campaign
**Trigger:** Promotional calendar, new product launch, restocking
**Goal:** Drive purchases from existing list.

Structure:
- Email 1: Tease/announcement (what's coming, why it matters)
- Email 2: Full offer reveal (product, price, benefit, proof)
- Email 3: Urgency/scarcity (deadline, limited stock, or bonus expiring)
- Email 4: Last chance (sent morning of deadline)

Subject line formulas:
- "The [product] you've been waiting for is here"
- "[Number] reasons [product] works when [alternative] doesn't"
- "Last chance: [offer] closes tonight"

### 3. Bucket Promotions
**Trigger:** Seasonal or event-based dates from promotion calendar
**Goal:** Drive revenue spikes around natural buying moments.

Rules:
- Tie the promotion to the reason (Christmas sale, not just "20% off")
- Segment by purchase history (don't promote baby products to customers who bought power tools)
- Exclude recent buyers from "urgency" campaigns — they already converted

### 4. Win-Back Campaign
**Trigger:** Customer has not purchased in [average purchase interval × 2]
**Goal:** Reactivate lapsed customers before they forget the brand entirely.

| Email | Timing | Content |
|-------|--------|---------|
| 1 | At trigger | "We miss you" — acknowledge absence, restate brand value |
| 2 | +7 days | Incentive offer — discount, free gift, or exclusive bundle |
| 3 | +14 days | Final chance — "This is our last message. Here's our best offer." |

After Email 3 with no response: move to suppression list. Do not continue emailing — it damages deliverability and brand perception.

## Subject Line Psychology

**Open-rate drivers:**
- Curiosity gap: "The one thing we never tell new customers..."
- Specificity: "27 customers returned this product. Here's why."
- Self-interest: "Your order is being held"
- Social proof: "12,847 people bought this last month"
- Urgency: "Closes at midnight" (only use when true)

**Avoid:**
- All caps subject lines
- Excessive punctuation (!!!, ???)
- Spam trigger words: "free", "guarantee", "winner", "cash"
- Vague subjects: "Newsletter #47" or "Check this out"

## Segmentation Rules

Always segment before sending:

| Segment | Filter | Send What |
|---------|--------|-----------|
| Never bought | On list, 0 purchases | Lead nurture + entry offer |
| Bought once | 1 purchase, >30 days ago | Cross-sell + review request |
| Active buyers | 2+ purchases, recent | Loyalty offer + new products |
| At-risk | Purchased before, silent 60+ days | Win-back sequence |
| Lapsed | Silent 120+ days | Final win-back or suppress |

Never send the same email to all segments. Segmented campaigns average 760% more revenue than broadcast campaigns.
```

**Step 4: Verify all files created and line counts**

```bash
wc -l ecommerce-funnel/SKILL.md
wc -l ecommerce-funnel/references/funnel-architecture.md
wc -l ecommerce-funnel/references/email-sequences.md
```

Expected: SKILL.md under 500 lines. Reference files have no hard limit.

**Step 5: Commit**

```bash
git add ecommerce-funnel/
git commit -m "feat: add ecommerce-funnel skill with funnel architecture and email sequence references"
```

---

## Task 3: Create `ecommerce-checkout/SKILL.md`

**Files:**
- Create: `ecommerce-checkout/SKILL.md`
- Create: `ecommerce-checkout/references/checkout-ux.md`
- Create: `ecommerce-checkout/references/brand-building.md`

**Step 1: Create `ecommerce-checkout/SKILL.md`**

```markdown
---
name: ecommerce-checkout
description: Ecommerce brand building and checkout experience optimisation. Use when establishing the brand foundation before site build, designing the checkout flow, or planning the post-purchase experience. Covers Verma's 7C brand framework, EVP vs UVP, checkout UX deep-dive, customer journey mapping, and DTC growth levers. Companion to the ecommerce skill.
---

# Ecommerce Checkout & Brand Skill

Most ecommerce failures are brand failures in disguise. Clients spend on traffic without a brand foundation, then wonder why CAC is high and repeat purchase rates are low. Build the brand first. Then optimise the checkout.

## The 7C Brand Framework (Verma)

Before designing any page, define these seven brand foundations. They inform every design decision, every word of copy, and every channel choice.

### 1. Core — Why You Exist
- Brand purpose: what problem does this business solve at a deeper level than "selling products"?
- Brand values: 3-5 non-negotiable principles that guide every decision
- Brand essence: one phrase that captures the spirit (not a tagline — an internal compass)

**Questions to ask the client:**
- Why did you start this? What frustrated you about what existed?
- What would you refuse to do even if it made you money?
- What do you want customers to feel, not just think?

### 2. Customer — Who You Serve
- Not demographics: psychographics, aspirations, and identity
- Help them become who they want to be — not just solve a problem
- The customer avatar's exact language must appear in all copy

**Key insight:** Customers don't buy products. They buy a better version of themselves.

### 3. Community — Your 1,000 True Fans
- 1,000 true fans (Kelly) — a business needs only 1,000 people who love it deeply, not millions who are indifferent
- Community creates defensibility: competitors can copy products, not communities
- Community touchpoints: Facebook group, Discord, loyalty programme, annual event, ambassador programme

### 4. Competition — Your Unique Point of View (Sole™)
- Not just "we're better" — a specific, defensible point of view on the category
- What do you believe that others in your category do not?
- Example: "Most protein supplements are engineered for bodybuilders. We believe everyday people deserve the same nutrition without the bro-culture."
- Your Sole™ is the foundation for all differentiation messaging

### 5. Creatives — Brand Identity Execution
- Name, logo, colour palette, typography, packaging — all must express the Core values
- Premium positioning = restraint (white space, mono palette, serif or geometric type)
- Value positioning = energy (contrast, bold type, product-forward imagery)
- Never choose fonts or colours in isolation — they must reinforce the brand's emotional positioning

### 6. Content — Brand Storytelling
- Four content types (in rotation):
  1. Brand stories: origin, values, team, behind-the-scenes
  2. Educational: how-tos, buying guides, industry insights, tutorials
  3. Social proof: customer stories, before/afters, case studies, UGC
  4. Promotional: product launches, limited offers, seasonal campaigns
- Story structure: customer as hero, brand as guide (not the other way around)

### 7. Channel — Where You Show Up
- Owned: email list, website, SMS — highest control, highest ROI
- Shared: social media, marketplaces, communities — reach, but platform-dependent
- Paid: ads — fast reach, requires margin to sustain
- Build owned channels first. Social platforms change algorithms; email lists are yours forever.

---

## EVP vs. UVP

Every product page needs both. Every checkout page needs the EVP reinforced.

**UVP (Unique Value Proposition) — functional**
- "What does it do better than alternatives?"
- Lives on: product pages, comparison sections, specs, feature lists
- Example: "Ships in 24 hours. 90-day returns. Free exchange."

**EVP (Emotional Value Proposition) — identity**
- "How does it make the customer feel? Who does it help them become?"
- Lives on: hero sections, brand story, checkout confirmation, packaging
- Example: "The kit that makes professional results feel personal."

EVP is what removes price sensitivity. Customers who connect emotionally do not comparison-shop.

**How to find the EVP:**
1. Ask: "What is the customer's life like 90 days after they buy?"
2. Ask: "What will they tell their friends?" (exact words)
3. Ask: "What do they feel in the moment they use this product?"

---

## Checkout UX Deep-Dive

The checkout is where revenue is won or lost. Every friction point costs money.

### Form Design Rules
- **Fields shown:** name, email, phone, shipping address, payment — nothing else
- **Never ask:** date of birth, gender, "how did you hear about us" (save for post-purchase survey)
- **Autofill:** enable browser autofill on all fields (`autocomplete` attributes)
- **Inline validation:** show errors as the user types, not on submit
- **Label position:** labels above fields (not placeholder text — placeholder disappears on focus)
- **Mobile keyboards:** use `type="email"`, `type="tel"`, `type="number"` for correct keyboard

### Trust Hierarchy at Checkout
Place trust signals exactly where anxiety peaks:

| Anxiety Point | Signal to Show |
|---------------|----------------|
| Before entering card details | SSL badge, payment logos, padlock icon |
| After entering address | "Your information is encrypted and never shared" |
| Before clicking Pay | Order summary with full total (no surprise costs) |
| After clicking Pay | Loading indicator + "Processing securely..." |

### Payment Method Priority (East Africa)
Order payment options by regional prevalence:
1. M-Pesa / MTN Mobile Money (highest adoption)
2. Visa / Mastercard debit cards
3. PayPal (diaspora customers)
4. Bank transfer (B2B clients)
5. Cash on delivery (where operationally possible)

Never offer only credit cards in markets where debit and mobile money dominate.

### Step Count and Progress
- Maximum 3 steps: Cart → Details → Payment
- Show a progress indicator at top (Step 1 of 3)
- Allow back navigation without losing entered data
- Single-page checkout preferred where technically feasible

### Order Summary Persistence
- Visible at all times during checkout (right column on desktop, collapsible accordion on mobile)
- Must show: each item, quantity, individual price, subtotal, delivery cost, total
- Edit cart link without losing checkout progress

---

## Customer Journey Mapping (7-Day Arc)

Understanding when decisions happen shapes where to invest in trust-building.

| Day | Stage | Customer Activity | Your Response |
|-----|-------|-------------------|---------------|
| 1 | **Problem Awareness** | Realises they have a need | Content marketing, SEO |
| 2 | **Solution Awareness** | Discovers category/solutions exist | Ads, influencer content |
| 3 | **Brand Discovery** | Finds your store | Landing page, brand story |
| 4-5 | **Consideration** | Compares options, reads reviews | Product pages, reviews, guarantees |
| 6 | **Purchase Decision** | Ready to buy | Checkout UX, trust signals, payment options |
| 7 | **Post-Purchase** | Evaluates decision | Confirmation email, shipping update, onboarding |

Most stores over-invest in Day 6 (checkout) and under-invest in Days 1-5 (awareness and consideration). Reduce drop-off by building trust early — not just at checkout.

---

## Post-Purchase Sequence

The 72 hours after purchase are the most important for LTV.

### Thank-You Page (immediately after payment)
Must include:
1. Order confirmation with reference number
2. Expected delivery date (be specific — not "5-7 business days")
3. Review invite: "You'll receive an email to review your purchase. Your feedback helps other customers."
4. Cross-sell: one complementary product (not a full catalog)
5. Social invite: "Join [X] customers in our community: [link]"

Do not show:
- Popup upsell that feels manipulative
- Excessive new offers before order is even delivered
- Social sharing buttons for the order itself (privacy)

### Transactional Emails (automated)
| Email | Timing | Content |
|-------|--------|---------|
| Order confirmation | Immediately | Order details, reference, expected delivery |
| Shipping confirmation | When dispatched | Tracking link, delivery date |
| Delivery confirmation | On arrival (if carrier API available) | "Your order arrived!" + review request |
| Review request | Day 7 post-delivery | Simple 1-click star rating + optional written review |

---

## DTC Growth Levers

Every checkout optimisation maps to one of three levers:

| Lever | Checkout Application |
|-------|---------------------|
| **More customers** | Reduce friction → more complete checkouts. Improve trust → more first-time buyers. |
| **Higher AOV** | Order bump on checkout page. Free shipping threshold. Bundle suggestions in cart. |
| **Higher LTV** | RIC offer post-purchase. Community invite. Indoctrination email sequence. |

Optimise for all three simultaneously. A checkout that converts once but never retains is a leaky bucket.

## Integration

- **ecommerce** — base UX, CLICK system, trust signals, product pages
- **ecommerce-funnel** — post-checkout sequences, upsells, customer lifecycle
- **ecommerce-analytics** — measures checkout conversion rate, drop-off by step, AOV trends
- **design-system** — brand identity execution (colours, type, visual hierarchy)
- **sales-copywriting** — EVP copy, headline formulas, CTA wording
- **i18n** — multi-language checkout, locale-specific payment methods, currency display
```

**Step 2: Create `ecommerce-checkout/references/checkout-ux.md`**

```markdown
# Checkout UX Reference

## Checkout Page Anatomy (Desktop)

```
┌─────────────────────────────────┬──────────────────────────┐
│ ← Back to cart  [Logo]  [SSL]   │                          │
├─────────────────────────────────│    ORDER SUMMARY         │
│ STEP 1 of 3: CONTACT INFO       │    ─────────────────     │
│                                 │    Product A    $29.00   │
│ [Email address          ]       │    Product B    $15.00   │
│ [Phone number           ]       │    ─────────────────     │
│                                 │    Subtotal     $44.00   │
│ SHIPPING ADDRESS                │    Delivery      $5.00   │
│ [First name] [Last name ]       │    ─────────────────     │
│ [Street address         ]       │    TOTAL        $49.00   │
│ [City      ] [Postcode  ]       │                          │
│ [Country dropdown       ]       │    ✓ SSL Secured         │
│                                 │    ✓ 30-day returns      │
│ [Continue to payment →  ]       │    ✓ Free exchange       │
└─────────────────────────────────┴──────────────────────────┘
```

## Checkout Page Anatomy (Mobile)

```
┌─────────────────────────┐
│ ← [Logo]          [SSL] │
│ ─────────────────────── │
│ ▼ Order Summary (tap)   │
│   TOTAL: $49.00         │
│ ─────────────────────── │
│ Step 1 of 3 ●○○         │
│                         │
│ CONTACT INFO            │
│ [Email               ]  │
│ [Phone               ]  │
│                         │
│ SHIPPING                │
│ [First name          ]  │
│ [Last name           ]  │
│ [Street address      ]  │
│ [City      ][Post    ]  │
│ [Country   ▼         ]  │
│                         │
│ [Continue to Payment →] │
│ (Full-width, 48px tall) │
└─────────────────────────┘
```

## Field Autocomplete Attributes

```html
<input type="text"    autocomplete="given-name"    name="first_name">
<input type="text"    autocomplete="family-name"   name="last_name">
<input type="email"   autocomplete="email"         name="email">
<input type="tel"     autocomplete="tel"           name="phone">
<input type="text"    autocomplete="street-address" name="address">
<input type="text"    autocomplete="address-level2" name="city">
<input type="text"    autocomplete="postal-code"   name="postcode">
<select               autocomplete="country"       name="country">
<input type="text"    autocomplete="cc-name"       name="card_name">
<input type="text"    autocomplete="cc-number"     name="card_number">
<input type="text"    autocomplete="cc-exp"        name="card_expiry">
<input type="text"    autocomplete="cc-csc"        name="card_cvv">
```

## Order Bump Component (Checkout)

```html
<!-- Place inside checkout form, above payment section -->
<div class="order-bump">
  <label>
    <input type="checkbox" name="order_bump" value="1">
    <div class="bump-content">
      <img src="bump-product.jpg" alt="Bump Product">
      <div>
        <strong>Add [Product Name] to your order</strong>
        <p>[One sentence: what it does + key benefit]</p>
        <span class="bump-price">Just $[price] — normally $[full price]</span>
      </div>
    </div>
  </label>
</div>
```

## Trust Badge Placement Rules

| Location | Badges to Show |
|----------|---------------|
| Below payment form headline | SSL padlock + "256-bit encryption" |
| Below payment method icons | Visa, Mastercard, M-Pesa, PayPal logos |
| Below CTA button | Money-back guarantee + returns policy snippet |
| Footer of checkout | Physical address + customer service contact |

## Error State Patterns

**Inline validation (real-time):**
```
[Email address        ] ← turns red border + shows message below
  ✗ Please enter a valid email address

[Email address        ] ← turns green border when valid
  ✓
```

**Submission error (if payment fails):**
- Show error at TOP of form (scroll to it)
- Keep all fields filled — never clear the form on error
- Specific message: "Your card was declined. Please check the card number and try again." (not "An error occurred")
- Offer alternative payment method if card fails twice

## Payment Step (Step 3)

```
PAYMENT METHOD
○ M-Pesa          [Logo]
○ Card            [Visa/MC logos]
○ PayPal          [Logo]
○ Bank Transfer

─── If M-Pesa selected: ───────────────────────────
[Phone number for M-Pesa push]
You will receive an M-Pesa prompt on your phone.
Enter your PIN to complete payment.

─── If Card selected: ──────────────────────────────
[Card number          ] [MM/YY] [CVV]
[Name on card         ]
□ Save card for future purchases

[🔒 Pay $49.00 securely →]

By completing your purchase you agree to our
[Terms of Service] and [Privacy Policy]
```
```

**Step 3: Create `ecommerce-checkout/references/brand-building.md`**

```markdown
# Brand Building Reference — 7C Workbook

Use these questions during client onboarding. Answers inform all copy, design, and channel decisions.

## 1. Core — Brand Foundation

**Purpose:**
- Why does this business exist beyond making money?
- What would the world lose if this business disappeared?

**Values (choose 3-5):**
- Authenticity / Transparency / Quality / Accessibility / Community / Innovation / Sustainability / Craftsmanship / Speed / Trust / Expertise / Fun

**Essence:**
- If the brand were a person, describe them in 5 words.
- What do you refuse to do even if it's profitable?

**Output:** One-paragraph brand essence statement used internally (not a tagline).

## 2. Customer — Avatar Deep Dive

See `ecommerce-funnel/SKILL.md` for the full avatar framework (7 emotional + 10 behavioural questions).

**Additional brand-level questions:**
- What does your ideal customer believe about themselves?
- What do they believe about people who DON'T buy your type of product?
- What transformation do they want: practical (save time/money/effort) or identity (become someone different)?

## 3. Community — 1,000 True Fans Plan

- What shared interest or identity unites your best customers?
- Where do they already gather online (subreddit, Facebook group, WhatsApp communities)?
- What would make someone proud to be associated with this brand publicly?

**Community touchpoints to build over time:**
- Private Facebook group or Discord server
- Ambassador programme (% commission for referrals)
- Annual virtual or in-person event
- Behind-the-scenes access for long-term customers

## 4. Competition — Finding the Sole™

**Category audit:**
- List 5 direct competitors. What do they all have in common (visually, in messaging, in values)?
- What does your brand believe that most competitors do not?
- What would you be willing to say publicly that others in your category avoid saying?

**Sole™ Statement Formula:**
"Most [category] brands believe [common belief]. We believe [different belief]. That's why we [proof point]."

Example: "Most skincare brands believe you need 10 products for great skin. We believe great skin needs great ingredients, not great marketing. That's why every product has 5 ingredients or fewer."

## 5. Creatives — Visual Identity Decisions

**Positioning check:**
- Premium (high price, aspirational): restraint, white space, serif or geometric type, monochrome or limited palette
- Mid-market (value + quality): clean layout, friendly typography, 2-3 colour palette
- Value (accessible, high volume): energy, contrast, bold headlines, product-forward imagery

**Font selection (reference design-system skill):**
- Never use Inter, Roboto, Arial, or system fonts for a distinctive brand
- Serif fonts signal heritage, authority, quality (editorial, legal, luxury)
- Sans-serif signals modernity, accessibility, technology
- Display/custom fonts signal creativity, distinctiveness, personality

**Colour psychology:**
- Reference color-selection skill for full palette design
- Checkout pages: use brand colours sparingly; neutral whites/greys dominate to reduce distraction

## 6. Content — Brand Story Templates

**Origin Story (400-600 words):**
Structure: Problem the founder faced → Failed existing solutions → Lightbulb moment → Building the solution → Proof it works → Invitation

**Product Story (200-300 words per product):**
Structure: Why this product exists → Who it's for → What makes it different → Proof → CTA

**Customer Story (testimonial template):**
Structure: Who they were before → What they tried → Why they chose this → What changed → What they'd say to someone like themselves before buying

## 7. Channel — Priority Build Order

Build in this order. Never skip to paid before owned is established.

| Priority | Channel | Why |
|----------|---------|-----|
| 1 | Email list | Owned, highest ROI, not algorithm-dependent |
| 2 | Website/blog | Owned, SEO compound interest, trust-builder |
| 3 | Social (1 platform) | Start on the platform where your avatar spends most time |
| 4 | Community | Build belonging before scaling reach |
| 5 | Paid ads | Scale only when CAC < CLV is proven with organic |

**Channel selection by product type:**

| Product | Primary Channel | Secondary |
|---------|----------------|-----------|
| Physical goods | Instagram / TikTok | Pinterest, Facebook |
| Digital goods | YouTube / blog | Twitter/X, email |
| B2B services | LinkedIn | Email, case studies |
| Local services | Google Business Profile | Facebook, WhatsApp |
| Subscription | Email | Community, referral |
```

**Step 4: Verify files and line counts**

```bash
wc -l ecommerce-checkout/SKILL.md
wc -l ecommerce-checkout/references/checkout-ux.md
wc -l ecommerce-checkout/references/brand-building.md
```

Expected: SKILL.md under 500 lines.

**Step 5: Commit**

```bash
git add ecommerce-checkout/
git commit -m "feat: add ecommerce-checkout skill with brand building and checkout UX references"
```

---

## Task 4: Create `ecommerce-analytics/SKILL.md`

**Files:**
- Create: `ecommerce-analytics/SKILL.md`
- Create: `ecommerce-analytics/references/kpi-framework.md`
- Create: `ecommerce-analytics/references/analytics-setup.md`

**Step 1: Create `ecommerce-analytics/SKILL.md`**

```markdown
---
name: ecommerce-analytics
description: Ecommerce analytics, measurement, and data-driven optimisation. Use when setting up analytics tracking, building KPI dashboards, analysing customer behaviour, or measuring funnel performance. Covers Phillips' value chain approach, RFM analysis, cohort retention, attribution modelling, CLV calculation, and conversion funnel drop-off diagnosis. Companion to the ecommerce and ecommerce-funnel skills.
---

# Ecommerce Analytics Skill

What you don't measure, you can't improve. Analytics is not a reporting exercise — it is the operating system of a profitable ecommerce business.

## The Analytics Value Chain (Phillips)

Seven sequential steps from data collection to business impact:

```
1. Identify Demand → 2. Plan Analytics → 3. Activate Environment → 4. Prepare Data
      ↓                                                                    ↓
7. Communicate Impact ← 6. Socialise Insights ← 5. Analyse & Optimise ← ┘
```

**Step 1 — Identify Demand:** What business questions need answers? Start with questions, not data.
**Step 2 — Plan Analytics:** Which metrics answer those questions? What tracking is required?
**Step 3 — Activate Environment:** Implement tracking (GA4, pixel, heatmaps, email platform).
**Step 4 — Prepare Data:** Ensure data quality, remove bots, de-duplicate, validate.
**Step 5 — Analyse & Optimise:** Find patterns, form hypotheses, test interventions.
**Step 6 — Socialise Insights:** Share findings with client in plain language, not raw data.
**Step 7 — Communicate Economic Impact:** Convert analytics findings into revenue impact (£/$ terms).

Never build a dashboard before completing Steps 1-2. Most ecommerce analytics fails because tracking is built first and questions are asked second.

## Core Metrics Framework

### The Three Growth Levers — Measured

Every ecommerce metric maps to one of three levers:

| Lever | Key Metrics |
|-------|-------------|
| More customers | Conversion rate, CAC, new visitor count, channel acquisition mix |
| Higher AOV | Average order value, units per transaction, attachment rate |
| Higher LTV | Repeat purchase rate, CLV, churn (subscriptions), referral rate |

Track one metric per lever as the North Star. Don't optimise all three simultaneously in early stage.

### Conversion Funnel Metrics

Track drop-off at each stage:

```
Sessions → Product Page Views → Add to Cart → Checkout Started → Purchase
  100%  →       45-60%       →    8-15%    →      5-10%       →   2-4%
```

Industry baselines above are approximations. Establish your own baseline first, then optimise by identifying the worst drop-off point.

**Diagnosis by drop-off location:**
- Sessions → Product page (high bounce): landing page mismatch, slow load, unclear offer
- Product page → Add to cart (low): weak product copy, missing reviews, price anchoring issue
- Add to cart → Checkout started (high abandonment): delivery cost shock, forced account creation
- Checkout started → Purchase (drop): form friction, payment failure, trust deficit

### Revenue Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Conversion Rate** | Orders ÷ Sessions × 100 | 2-4% (industry avg) |
| **AOV** | Revenue ÷ Orders | Category-dependent |
| **Revenue per Visitor** | Revenue ÷ Sessions | CAC must be below this |
| **CLV** | AOV × Purchase Frequency × Customer Lifespan | Must exceed CAC × 3 |
| **CAC** | Total acquisition spend ÷ New customers | Must be < CLV |
| **ROAS** | Revenue ÷ Ad spend | Minimum 3x to be profitable |

---

## RFM Analysis — Customer Segmentation

RFM segments customers by purchase behaviour. It is the foundation of all retention marketing.

**Three dimensions:**
- **Recency (R):** How recently did they buy? (Days since last purchase)
- **Frequency (F):** How often do they buy? (Number of orders)
- **Monetary (M):** How much do they spend? (Total lifetime spend)

**Scoring:** Score each customer 1-5 on each dimension (5 = best). Combine into segments:

| Segment | R | F | M | Strategy |
|---------|---|---|---|----------|
| Champions | 5 | 5 | 5 | Reward, make brand ambassadors |
| Loyal Customers | 4-5 | 4-5 | 3-5 | Upsell, ask for referrals |
| Potential Loyalists | 3-4 | 1-2 | 2-3 | Nurture with relevant offers |
| At-Risk | 2 | 3-4 | 3-4 | Win-back campaign |
| Lost | 1 | 1-2 | 1-2 | Aggressive win-back or suppress |

**How to calculate RFM:**
1. Export customer order history (order date, customer ID, order value)
2. Calculate days since last order (Recency)
3. Count total orders per customer (Frequency)
4. Sum total spend per customer (Monetary)
5. Score 1-5 within each dimension (quintile ranking)
6. Combine scores: RFM = R score + F score + M score (max 15)

Run RFM quarterly. Customers who move down tiers need immediate attention.

---

## Cohort Analysis — Retention Over Time

Cohort analysis tracks groups of customers acquired in the same period to reveal retention decay.

**Structure:**
- Row = acquisition cohort (e.g., "All customers acquired in January")
- Column = time period (Month 1, Month 2, Month 3...)
- Cell = % of cohort still purchasing in that period

**Example cohort table:**

| Cohort | M1 | M2 | M3 | M6 | M12 |
|--------|----|----|----|----|-----|
| Jan | 100% | 35% | 22% | 15% | 11% |
| Feb | 100% | 38% | 25% | 17% | — |
| Mar | 100% | 41% | 28% | — | — |

**Reading the table:**
- If M2 retention is improving cohort-over-cohort: product/onboarding is getting better
- If M6 retention is flat: customers buy once, then stop — address with win-back and lifecycle emails
- If a specific cohort underperforms: that acquisition channel may attract low-quality buyers

**Retention benchmark by category:**
- Fashion: 20-30% annual retention (highly competitive)
- Consumables (supplements, coffee): 40-60% (replenishment drives retention)
- Electronics: 15-20% (long repurchase cycles)
- Subscription boxes: measure monthly, target >90% month-over-month

---

## Attribution Modelling

Attribution assigns revenue credit to the marketing touchpoints that led to a sale. No single model is "correct" — use multiple to understand different truths.

| Model | How it works | Best for |
|-------|-------------|----------|
| **Last-click** | 100% credit to the final touchpoint before purchase | Understanding what closes sales |
| **First-click** | 100% credit to the first touchpoint | Understanding what generates awareness |
| **Linear** | Equal credit across all touchpoints | Understanding the full journey |
| **Time-decay** | More credit to recent touchpoints | Understanding what accelerates decisions |
| **Data-driven** | ML-based credit allocation | Mature businesses with high data volume |

**Practical guidance:**
- For budget decisions: use first-click to value awareness channels fairly
- For optimisation: use last-click to identify what converts
- For full picture: compare first vs. last-click. Big differences = customer journey has multiple distinct stages.

**Attribution window:**
- Fashion/impulse: 1-7 day window
- Considered purchases (electronics, furniture): 30-90 day window
- B2B services: 90-180 day window

---

## CLV Calculation

Customer Lifetime Value is the maximum you can afford to spend acquiring a customer.

**Simple CLV formula:**
```
CLV = AOV × Purchase Frequency (annual) × Customer Lifespan (years)
```

**Example:**
- AOV = $50
- Purchase frequency = 4x/year
- Average customer stays 2 years
- CLV = $50 × 4 × 2 = $400

**Gross margin adjustment:**
```
CLV (gross) = CLV × Gross Margin %
```
If gross margin is 40%: CLV (gross) = $400 × 0.40 = $160

**Maximum CAC rule:** CAC should not exceed 1/3 of gross CLV. In this example: CAC ≤ $53.

**How to improve CLV:**
1. Increase AOV: bundles, upsells, free shipping thresholds
2. Increase frequency: replenishment reminders, subscription offers, new product launches
3. Increase lifespan: community, loyalty programme, consistent brand experience

---

## A/B Testing Framework

Test one variable at a time. Measure statistical significance before declaring a winner.

**Testing priority (by revenue impact):**
1. Checkout CTA button (text, colour, size)
2. Product page headline
3. Product price display (charm pricing, anchoring)
4. Email subject lines
5. Ad creative
6. Product image (lifestyle vs. product-only)
7. Delivery cost display position

**Test structure:**
- Control (A): current version
- Variant (B): single changed element
- Traffic split: 50/50 for equal-sized groups
- Duration: minimum 2 weeks, minimum 100 conversions per variant
- Significance threshold: 95% confidence before declaring winner

**Do not test:**
- Multiple variables simultaneously (confounds results)
- During unusual periods (holidays, PR spikes)
- With sample sizes below 100 conversions per variant

---

## RASTA Reporting Model (Phillips)

Structure client dashboards and reports using RASTA:

- **R — Relevant:** Only include metrics that drive decisions. No vanity metrics.
- **A — Accurate:** Data quality verified before reporting. No bots, no test orders.
- **S — Simple:** One chart per insight. No data walls.
- **T — Timely:** Reports delivered when decisions are made, not on arbitrary schedules.
- **A — Actionable:** Every metric must have a "so what" — what action does this trigger?

**Monthly report structure:**
1. Executive summary (3 bullet points: what's up, what's down, what we're doing about it)
2. Revenue overview (total, vs. last month, vs. last year)
3. Three lever metrics (acquisition, AOV, retention)
4. Funnel drop-off (where are we losing customers?)
5. Top and bottom performing products
6. Recommended actions (prioritised by revenue impact)

## Integration

- **ecommerce** — tracks conversion rate, trust signal effectiveness, cart abandonment rate
- **ecommerce-funnel** — measures funnel conversion at each stage, email open/click rates, CLV by segment
- **ecommerce-checkout** — tracks checkout step drop-off, payment method success rates, form error rates
- **seo-audit** — organic search metrics, landing page performance, keyword-driven conversion rates
- **blog-writer** — measures content-to-conversion path (blog → product → purchase)
```

**Step 2: Create `ecommerce-analytics/references/kpi-framework.md`**

```markdown
# KPI Framework Reference

## The Ecommerce KPI Tree

```
REVENUE
├── Transactions
│   ├── Sessions (traffic volume)
│   ├── Conversion Rate (sessions → purchases)
│   └── Return Rate (gross revenue adjustment)
├── Average Order Value
│   ├── Units per Transaction
│   ├── Average Unit Price
│   └── Attachment Rate (add-ons / accessories)
└── Repeat Purchase Rate
    ├── Purchase Frequency (orders per customer per year)
    └── Customer Retention Rate (% active past 12 months)

CUSTOMER ECONOMICS
├── CAC (Customer Acquisition Cost)
│   ├── Paid CAC (ad spend ÷ new paid customers)
│   └── Blended CAC (total marketing spend ÷ all new customers)
├── CLV (Customer Lifetime Value)
│   ├── Gross CLV (revenue × lifespan)
│   └── Net CLV (gross CLV - CAC - COGS - service costs)
└── LTV:CAC Ratio (target: 3:1 minimum)
```

## KPI Benchmarks by Business Stage

| Metric | Early Stage (0-12mo) | Growth (1-3yr) | Mature (3yr+) |
|--------|---------------------|----------------|---------------|
| Conversion Rate | 1-2% | 2-4% | 3-5%+ |
| AOV | Establish baseline | Improve 10%/yr | Stable + upsell |
| Repeat Purchase Rate | 15-20% | 25-35% | 35-50% |
| CLV:CAC | 1.5:1 | 3:1 | 5:1+ |
| Email Open Rate | 20-25% | 25-35% | 35%+ |
| Cart Abandonment | 70-75% | 65-70% | 60-65% |

## Channel Performance KPIs

| Channel | Primary KPI | Secondary KPI |
|---------|------------|---------------|
| Organic Search | Organic revenue | Keyword ranking movement |
| Paid Search | ROAS | CPC, Quality Score |
| Email | Revenue per email sent | Open rate, Click rate |
| Social Organic | Engagement rate | Profile visits → sessions |
| Social Paid | ROAS, CPM | CTR, Frequency |
| Referral/Affiliate | Revenue, Commission rate | New customer % |

## Dashboard Template — Monthly

### Section 1: Revenue Health
- Total revenue (MTD vs. prior month vs. prior year)
- Orders (count)
- AOV
- Revenue per visitor

### Section 2: Acquisition
- Sessions by channel (organic, paid, email, social, direct)
- New vs. returning visitor ratio
- CAC by channel
- Conversion rate by traffic source

### Section 3: Customer Quality
- New customers acquired
- Repeat purchase rate (last 90 days)
- Average purchase frequency
- CLV trend (rolling 12-month cohorts)

### Section 4: Operational
- Cart abandonment rate
- Top 10 products by revenue
- Bottom 10 products by returns rate
- Out-of-stock incidents (if applicable)

### Section 5: Actions
- 3 things we're doing this month based on data
- 1 hypothesis we're testing
- 1 metric we're most concerned about
```

**Step 3: Create `ecommerce-analytics/references/analytics-setup.md`**

```markdown
# Analytics Setup Reference

## Tracking Stack

Minimum viable analytics stack for an ecommerce site:

| Tool | Purpose | Cost |
|------|---------|------|
| Google Analytics 4 | Sessions, conversions, funnel, acquisition | Free |
| Google Search Console | Organic keywords, impressions, CTR | Free |
| Meta Pixel | Facebook/Instagram retargeting, conversion tracking | Free |
| Hotjar or Microsoft Clarity | Heatmaps, session recordings, form analytics | Free tier available |
| Email platform (Mailchimp/Klaviyo) | Email analytics, segmentation, automation | Paid |

## GA4 Ecommerce Events to Implement

```javascript
// View product page
gtag('event', 'view_item', {
  currency: 'USD',
  value: 29.99,
  items: [{
    item_id: 'SKU123',
    item_name: 'Product Name',
    item_category: 'Category',
    price: 29.99,
    quantity: 1
  }]
});

// Add to cart
gtag('event', 'add_to_cart', {
  currency: 'USD',
  value: 29.99,
  items: [{ item_id: 'SKU123', item_name: 'Product Name', price: 29.99, quantity: 1 }]
});

// Begin checkout
gtag('event', 'begin_checkout', {
  currency: 'USD',
  value: 29.99,
  items: [{ item_id: 'SKU123', item_name: 'Product Name', price: 29.99, quantity: 1 }]
});

// Purchase
gtag('event', 'purchase', {
  transaction_id: 'ORDER-001',
  currency: 'USD',
  value: 34.99, // includes shipping
  shipping: 5.00,
  tax: 0,
  items: [{ item_id: 'SKU123', item_name: 'Product Name', price: 29.99, quantity: 1 }]
});
```

## Funnel Report Setup in GA4

1. Go to Explore → Funnel Exploration
2. Define steps:
   - Step 1: `view_item` (product page viewed)
   - Step 2: `add_to_cart`
   - Step 3: `begin_checkout`
   - Step 4: `purchase`
3. Set date range to rolling 30 days
4. Add segment: New Users vs. Returning Users
5. Screenshot and add to monthly report

## Heatmap Priorities

Run heatmaps on these pages first (highest ROI):
1. Homepage (above fold — what do visitors click before scrolling?)
2. Product page (do they click Add to Cart? Do they read reviews?)
3. Checkout step 1 (where do they hesitate or exit?)
4. Cart page (what causes them to leave without proceeding?)

## Conversion Rate Calculation

```
CR = (Transactions ÷ Sessions) × 100

Example: 3,000 sessions, 75 purchases
CR = (75 ÷ 3,000) × 100 = 2.5%
```

Segment CR by:
- Traffic source (organic CR vs. paid CR vs. email CR)
- Device (mobile CR vs. desktop CR — mobile is typically 40-60% lower)
- New vs. returning visitor
- Geography (if shipping internationally)

## CLV Calculation Worksheet

```
Step 1: Export all orders from the past 24 months
Step 2: Group by customer ID
Step 3: Calculate per customer:
  - First order date
  - Last order date
  - Total orders
  - Total spend

Step 4: Calculate averages:
  AOV = Total revenue ÷ Total orders
  Avg Purchase Frequency = Total orders ÷ Unique customers
  Avg Customer Lifespan = Average months between first and last order ÷ 12

Step 5: CLV = AOV × Purchase Frequency × Lifespan
Step 6: CLV (gross margin adjusted) = CLV × Gross Margin %
Step 7: Max CAC = CLV (gross) ÷ 3
```

## RFM Scoring — Spreadsheet Method

1. Export: customer_id, order_date, order_value for all orders
2. Calculate in spreadsheet:
   ```
   Recency = TODAY() - MAX(order_date) per customer [lower = better]
   Frequency = COUNT(orders) per customer [higher = better]
   Monetary = SUM(order_value) per customer [higher = better]
   ```
3. Use PERCENTRANK to score each dimension 1-5 (5 = best)
4. Combine: RFM_score = R + F + M (max 15)
5. Segment: 13-15 = Champions, 10-12 = Loyal, 7-9 = Potential, 4-6 = At-Risk, 3 = Lost
```

**Step 4: Verify line counts**

```bash
wc -l ecommerce-analytics/SKILL.md
wc -l ecommerce-analytics/references/kpi-framework.md
wc -l ecommerce-analytics/references/analytics-setup.md
```

**Step 5: Commit**

```bash
git add ecommerce-analytics/
git commit -m "feat: add ecommerce-analytics skill with KPI framework and analytics setup references"
```

---

## Task 5: Update CLAUDE.md and docs/plans/INDEX.md

**Files:**
- Modify: `CLAUDE.md` — add three new skills to the utility skills list and update skill count
- Modify: `docs/plans/INDEX.md` — add this plan to the index

**Step 1: Update CLAUDE.md skill listings**

In the "Utility Skills" section, add after the ecommerce entry (or in the appropriate place):

```markdown
- **ecommerce-funnel** — customer avatar, traffic temperature, funnel architecture, email sequences, lifecycle management; companion to ecommerce
- **ecommerce-checkout** — brand foundation (7C framework), EVP vs UVP, checkout UX deep-dive, post-purchase sequence, DTC growth levers; companion to ecommerce
- **ecommerce-analytics** — RFM analysis, cohort retention, attribution modelling, CLV calculation, funnel drop-off diagnosis; companion to ecommerce
```

**Step 2: Update skill count in CLAUDE.md** (currently says "23 total")

Change to: "26 total"

**Step 3: Update docs/plans/INDEX.md**

Add entry:
```markdown
| 2026-03-20-ecommerce-skills-upgrade.md | Completed | Upgrade ecommerce skill + add funnel/checkout/analytics companions from 8 books |
```

**Step 4: Commit**

```bash
git add CLAUDE.md docs/plans/INDEX.md docs/plans/2026-03-20-ecommerce-skills-upgrade.md
git commit -m "docs: update CLAUDE.md with new ecommerce skills, add plan to index"
```

---

## Task 6: Run skill-safety-audit on all new skills

Per CLAUDE.md requirements: run skill-safety-audit on any new or modified skill before accepting it.

**Step 1:** Invoke the `skill-safety-audit` skill on:
- `ecommerce/SKILL.md` (modified)
- `ecommerce-funnel/SKILL.md`
- `ecommerce-checkout/SKILL.md`
- `ecommerce-analytics/SKILL.md`

**Step 2:** Address any flagged issues before considering the work complete.
