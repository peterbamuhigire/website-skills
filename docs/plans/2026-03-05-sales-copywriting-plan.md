# Sales Copywriting Skill — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a hybrid sales-copywriting skill with 5 reference files, enhance 3 existing references, and integrate into 3 existing skills — giving every website captivating, original, conversion-focused copy.

**Architecture:** Hybrid cross-cutting + on-demand skill. Core principles (headlines, CTAs, anti-resistance, proof) apply to all pages. Sales frameworks (PASTOR, 4 P's, guarantees) activate for landing/sales pages only. Level 2 persuasion: confident but professional.

**Tech Stack:** Markdown skill files (SKILL.md + references/*.md). No code changes.

**Design doc:** `docs/plans/2026-03-05-sales-copywriting-design.md`

---

### Task 1: Create `sales-copywriting/SKILL.md`

**Files:**
- Create: `sales-copywriting/SKILL.md`

**Step 1: Create the directory**

Run: `mkdir -p sales-copywriting/references`

**Step 2: Write the SKILL.md**

Create `sales-copywriting/SKILL.md` with this content (under 500 lines):

```markdown
---
name: sales-copywriting
description: Persuasion and conversion copywriting frameworks. Cross-cutting core (headlines, CTAs, anti-resistance, proof) applies to all pages. Sales frameworks (PASTOR, 4 P's, guarantees) activate for landing/sales/product pages. Level 2 persuasion — confident and professional, never pushy.
---

# Sales Copywriting

## When This Skill Applies

**Cross-cutting (always active during page-builder and blog-writer):**
- Writing any headline or subheadline
- Writing any CTA or button text
- Writing bullet points that need to persuade
- Structuring proof and credibility signals
- Handling objections in copy

**On-demand (activated for specific page types):**
- Landing pages and sales pages
- Product/service detail pages with conversion goals
- Pricing pages
- Lead generation pages
- Any page where the primary goal is conversion

## Reference Files

Read these references based on what you are building:

| Reference | Read When |
|-----------|-----------|
| `references/headline-mastery.md` | Writing ANY headline (all pages, all articles) |
| `references/fascination-bullets.md` | Writing bullet points that need to persuade or intrigue |
| `references/resistance-and-objections.md` | Writing any persuasive copy (all pages benefit) |
| `references/pastor-and-4ps.md` | Building landing pages, sales pages, or product pages |
| `references/closing-and-guarantees.md` | Writing CTAs, guarantees, offers, or pricing sections |

## Cross-Cutting Principles

These apply to EVERY page and article. They are non-negotiable.

### 1. The Headline Is the Ad for the Rest of the Page

The headline's only job is to make them read the next sentence. You have 2 seconds. Every headline must pass the 4 U's test (see `references/headline-mastery.md`):

- **Useful** — does it promise something the reader can use?
- **Unique** — is it said in a way they haven't heard before?
- **Urgent** — does it create a reason to read NOW?
- **Ultra-specific** — does it use concrete details, not vague claims?

Score each U from 1-4. A headline needs at least 3 scores of 3+ to publish.

### 2. Benefits Hide Features — The Transformation Frame

Never state a feature without wrapping it in its transformation:

| Wrong (Feature) | Right (Transformation) |
|-----------------|----------------------|
| "24/7 customer support" | "Get answers at 2am when your system goes down" |
| "Cloud-based platform" | "Access your data from any device, anywhere" |
| "ISO 27001 certified" | "Your data is protected by the same security banks use" |
| "10 years experience" | "We've solved this exact problem for 200+ companies like yours" |

The reader always asks "So what?" — answer it before they do.

### 3. Anti-Resistance Writing (Bill Bonner's Theory of Resistance)

**The core insight:** Prospects actively resist being sold. The moment they see where your argument is heading, they erect defences and dismiss it.

**What fails:**
- Blatantly logical approaches ("15 Reasons to Choose Us") — they jump ahead, figure it out, dismiss it
- Transparent sales efforts — they see through them
- Revealing the hook early — they avoid it
- Letting them know they're being sold — the instant they realise, they leave

**What works:**
- Approach from an unexpected angle — not the obvious pitch
- Keep them off balance — they can't predict your next point
- Lead with story or insight, not with product
- Let the conclusion feel like THEIR idea, not yours
- Use the "Golden Nuggets" technique: embed fascinating information that gives value while building credibility. When you tell someone something they didn't know, you give them something free — they feel gratitude and read on.

**Practical application for website pages:**
- Homepage hero: lead with the customer's problem or aspiration, not your product name
- Services page: lead with the outcome, not the service description
- About page: lead with the customer's journey, not your company history
- Blog posts: lead with an insight or story, not "In this article we will discuss..."

### 4. Proof Woven In, Not Bolted On

Proof should appear throughout copy, not in a separate "testimonials" section alone.

**7 Types of Proof (ordered by strength):**
1. Specific numbers and results ("reduced downtime by 73%")
2. Named case studies with details ("Kampala Medical Centre went from 4-hour waits to 20-minute check-ins")
3. Expert endorsements with credentials
4. Real testimonials with full name + role + company
5. Statistics from credible sources
6. Awards, certifications, and ratings
7. "As featured in" media mentions

**The Proof Integration Rule:** Every major claim on a page should have proof within 3 paragraphs. Don't make claims and prove them later — prove as you go.

### 5. The Three Things Prospects Never Do (At First)

1. They never READ — they scan. Write for scanners: strong subheads, short paragraphs, bullet points that tell the story alone.
2. They never BELIEVE — they doubt. Every claim needs proof nearby.
3. They never BUY — they resist. Remove friction, handle objections before they arise, make the next step obvious and low-risk.

Your copy must overcome all three, in sequence.

### 6. CTA Craft — Beyond "Click Here"

Every CTA must complete the sentence: "I want to ___."

| Weak | Strong |
|------|--------|
| "Submit" | "Send My Message" |
| "Learn More" | "See How It Works" |
| "Contact Us" | "Get Your Free Assessment" |
| "Sign Up" | "Start My Free Trial" |
| "Buy Now" | "Place My Order" |
| "Download" | "Get My Free Guide" |

**CTA placement rules:**
- After every major proof point or benefit section
- At least one CTA visible without scrolling
- At the bottom of every page
- Between testimonials (every 2-3)
- Never before you've given a reason to click

**5 Closing Approaches** (see `references/closing-and-guarantees.md` for full templates):
1. "You Will Certainly Arrive" — one year from now, you'll be somewhere. Where?
2. "Different Results" — want different results? Do something different. Now.
3. "Crossroads" — two roads. The familiar one, or the better one.
4. "Decision Time" — your destiny is shaped in moments of decision.
5. "Handholding" — you won't be alone. Here's exactly how we'll support you.

### 7. Sell What They WANT, Give What They Need

People buy on emotion, justify with logic. Your copy must:
1. **First:** Connect emotionally — paint the transformation, the aspiration, the relief
2. **Then:** Provide logical justification — data, specs, comparisons, credentials

The prospect needs to tell themselves (and others): "I made the right decision because..."

### 8. The Copy Thesis — One Sentence That Drives Everything

Before writing ANY page, complete this sentence:

> Any [TARGET AUDIENCE] can [SOLVE THEIR PROBLEM] by using [YOUR PRODUCT/SERVICE], because [HOW IT SOLVES THE PROBLEM].

This sentence never appears in the copy. It drives every word you write. If a sentence doesn't serve the Copy Thesis, cut it.

## Sales-Page-Specific Frameworks

**These activate ONLY for landing pages, sales pages, and product pages.** Do not apply the full PASTOR or 4 P's to an About page or blog post.

### PASTOR Framework (Ray Edwards)

For full details, see `references/pastor-and-4ps.md`. Summary:

| Letter | Element | What to Write |
|--------|---------|---------------|
| P | Person, Problem, Pain | Identify the specific person. Describe the problem in THEIR words. Articulate the pain it causes. |
| A | Amplify, Aspirations | What happens if they DON'T solve this? Put a cost on inaction. Then paint the aspiration. |
| S | Story, Solution, System | Tell the story of how this problem was solved. Real story, never fabricated. |
| T | Transformation, Testimony | Focus on the transformation (not deliverables). Provide real testimonials. |
| O | Offer | Describe exactly what you're offering. 80% transformation, 20% deliverables. |
| R | Response | Ask them to act. Tell them exactly what to do. Remind them why it matters. |

### 4 P's Framework (AWAI/Hollingshead)

| P | Element | What to Write |
|---|---------|---------------|
| Promise | Make a specific promise | Identify a fear or desire. Tell them what you'll do about it. |
| Picture | Paint the transformed life | Make them SEE themselves reaping the benefits. Use sensory language. |
| Proof | Prove it's true | While proving, keep reminding of the promise. Use the 7 proof types. |
| Push | Call to action with urgency | Make the specific offer. Create urgency. Be specific: not "soon" but "by Friday." |

### Value Anchoring

When presenting pricing or packages:
1. Itemise the value of each component separately
2. Show the total value (must be at least 10x the price)
3. Reveal the actual price as a contrast
4. Frame as investment, not cost: "Who wouldn't invest $X to get $Y?"

### Guarantee Writing

See `references/closing-and-guarantees.md` for the 10-part guarantee formula. Key rules:
- Give the guarantee a NAME (not just "money-back guarantee")
- Sell benefits WITHIN the guarantee copy
- Personalise it (your promise, not company policy)
- Longer guarantees = lower refund rates
- Show returns are easy (phone, email, address)

## Persuasion Ceiling

**Level 2 persuasion is the default.** This means:

**Always use:**
- Benefit-focused headlines
- Transformation framing
- Anti-resistance writing
- Proof integration
- Fascination bullets
- Named guarantees
- Value anchoring
- Strategic CTAs
- Story-led copy

**Use only when explicitly requested:**
- Countdown timers
- Strikethrough pricing
- Flying popovers
- "Only X left" scarcity (unless genuinely true)
- Multiple P.S. sections
- "5 Reasons to Buy NOW" boxes

**Never use:**
- Manipulative dark patterns
- False scarcity or urgency
- Guilt-based CTAs
- Fear-mongering beyond honest problem amplification
- Claims without proof

## Integration With Other Skills

- **page-builder:** Reads `references/headline-mastery.md` and `references/fascination-bullets.md` for all pages. Reads full skill for landing/sales pages.
- **blog-writer:** Reads `references/headline-mastery.md` for all headlines. Applies anti-resistance writing to persuasive articles.
- **brand-alignment:** Sales-copywriting techniques must align with brand voice. Level 2 persuasion is the ceiling unless the brand brief specifically requests otherwise.
- **language-standards:** All persuasion copy must follow language standards (British English, formal French, standard Kiswahili). Persuasion techniques adapt to cultural context.
- **human-voice-standards:** All copy must pass human voice checks. Fascination bullets and PASTOR copy are especially prone to AI patterns — apply the blacklist rigorously.
```

**Step 3: Verify line count**

Run: `wc -l sales-copywriting/SKILL.md`
Expected: Under 500 lines

**Step 4: Commit**

```bash
git add sales-copywriting/SKILL.md
git commit -m "Add sales-copywriting skill — hybrid cross-cutting + on-demand persuasion

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 2: Create `sales-copywriting/references/headline-mastery.md`

**Files:**
- Create: `sales-copywriting/references/headline-mastery.md`

**Step 1: Write the reference file**

This consolidates headline formulas from all 3 books plus existing techniques. Content:

```markdown
# Headline Mastery

Consolidated headline frameworks from Ray Edwards, Paul Hollingshead (AWAI), Angie Lee, and existing website-skills formulas. Use for ALL headlines — page headlines, section headlines, blog headlines, subheadlines.

## The 4 U's Scoring System (AWAI)

Score every headline 1-4 on each dimension. Publish only if 3+ dimensions score 3+.

| U | Score 1 (Weak) | Score 4 (Strong) |
|---|----------------|------------------|
| **Useful** | No clear benefit | Specific, actionable benefit |
| **Unique** | Generic, heard before | Fresh angle or phrasing |
| **Urgent** | No reason to read now | Compelling reason to read immediately |
| **Ultra-specific** | Vague claims | Concrete numbers, names, details |

## 10 Headline Templates

### 1. The "How-To" Headline (Ray Edwards)
Tie to a specific benefit, not just an action.

- Weak: "How to Write Blog Posts"
- Strong: "How to Write Blog Posts That Generate 3x More Enquiries"

### 2. The "Transactional" Headline (Ray Edwards)
Promise an exchange: give me X, I'll give you Y.

- "Give Me 30 Minutes and I'll Show You How to Cut Your Inventory Costs in Half"
- "Try These 3 Changes for One Week and Watch Your Customer Complaints Disappear"

### 3. The "Reason-Why" Headline (Ray Edwards)
Uses the power of "because" (Cialdini research: people comply more when given a reason).

- "7 Reasons Your POS System Is Costing You Money (And How to Fix Each One)"
- "Why Your Competitors' Websites Convert Better — And What They Know That You Don't"

### 4. The "Probing Question" Headline (Ray Edwards)
Evokes curiosity or taps a known problem. NEVER ask a question they can answer "No" to.

- "What Would You Do With an Extra 2 Hours Every Day?"
- "Are You Making These 5 Costly Mistakes With Your Business Accounts?"

### 5. The "If-Then" Headline (Ray Edwards)
Easy action → major benefit. Lowers the perceived effort.

- "If You Can Send an Email, You Can Manage Your Entire Inventory"
- "If You Can Count to 10, You Can Balance Your Books Every Month"

### 6. The Number Headline (Angie Lee)
Numbers trigger credibility — the brain associates them with measured data.

- "237 Businesses Switched to [Product] Last Quarter — Here's What They Found"
- "3 Changes That Reduced Our Client's Stock Losses by 41%"

Tip: Odd numbers outperform even numbers in headlines. Use specific numbers (237) not round ones (200).

### 7. The Benefit-Over-Feature Headline (Angie Lee)
Frame around the solution, never the product.

- Wrong: "Best New Cloud POS System"
- Right: "Process Sales in 3 Seconds — Even When the Internet Goes Down"

### 8. The Uncle B.E.N. Formula (Existing — Enhanced)
**B**enefit + **E**motion + **N**ovelty

- Benefit: What do they gain?
- Emotion: What do they feel?
- Novelty: What's new or different?

Example: "Sleep Through the Night Again — This New Approach Fixes What Medication Can't"

### 9. The Dramatised Benefit (Caples/AWAI)
Don't state the benefit flatly. Show the interaction of people. Let the reader feel the triumph.

- Flat: "Learn Piano So Well You'll Impress Your Friends"
- Dramatised: "They Laughed When I Sat Down at the Piano — But When I Started to Play!"
- Flat: "Our Software Is Easy to Use"
- Dramatised: "Her Accountant Couldn't Believe She'd Done the Books Herself"

### 10. The Pre-Head + Main Headline Combo (Angie Lee / Ray Edwards)
Short pre-headline (eyebrow) targets the exact audience. Main headline delivers the promise.

- Pre-head: "Attention, Restaurant Owners in Kampala"
- Headline: "How to Cut Food Waste by 30% Without Changing Your Menu"

Pre-head format: "Attention, [Target Group]!" — screens readers so the right people keep reading.

## Headline Process

1. **Write 20+ headlines before choosing one.** Even expert copywriters do this. Save rejected headlines for split testing.
2. **Test the Copy Thesis first:** Complete "Any [audience] can [solve problem] by using [product], because [how]" — then write headlines that express this thesis.
3. **Read it aloud.** If it sounds awkward spoken, rewrite.
4. **Check the 4 U's.** Score each dimension. If below threshold, strengthen the weakest U.
5. **Verify anti-AI.** Check against the human-voice blacklist. AI headlines tend toward: "Unlock the Power of...", "Discover the Secret to...", "Transform Your... Journey." Rewrite any that trigger.

## Subheadline Architecture

Subheadlines are the "bucket brigade" of your page. Readers scan ONLY headlines, subheads, bullet points, and images. Your subheads must tell the complete story by themselves.

**Test:** Read only the subheads on your page in sequence. Do they tell a compelling story? Would a scanner understand the value proposition? If not, rewrite them.

**Subhead types:**
- **Benefit subhead:** "Get Back 2 Hours Every Day"
- **Curiosity subhead:** "The One Thing Most POS Systems Get Wrong"
- **Proof subhead:** "How Kampala Medical Centre Cut Wait Times by 80%"
- **Transition subhead:** "But That's Only the Beginning"
- **Objection subhead:** "You're Probably Wondering About the Cost"

Mix types. Never use 3 of the same type in a row.

## Common Headline Mistakes

1. **Clever over clear** — if they don't understand it instantly, it fails
2. **Product-focused** — "Introducing Our New X" (no one cares about your product, they care about their problem)
3. **Too long** — online headlines: 8-12 words optimal; over 15 loses impact
4. **Answerable with "No"** — "Do You Want to Save Money?" → reader says "Not really" and scrolls on
5. **No benefit** — "Welcome to Our Website" (the most wasted headline in history)
6. **AI patterns** — "Unlock", "Discover", "Transform Your Journey", "In Today's Fast-Paced World"
7. **Trying to sell in the headline** — the headline sells ONLY the idea of reading the next line
```

**Step 2: Commit**

```bash
git add sales-copywriting/references/headline-mastery.md
git commit -m "Add headline mastery reference — 10 templates, 4 U's scoring, process

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 3: Create `sales-copywriting/references/fascination-bullets.md`

**Files:**
- Create: `sales-copywriting/references/fascination-bullets.md`

**Step 1: Write the reference file**

```markdown
# Fascination Bullets — 21 Templates

Bullet points are the most-read elements on any page after headlines. Readers scan them even when they skip body copy. Great bullets create curiosity, highlight benefits, and drive action.

Source: Ray Edwards' "How to Write Copy That Sells" — 21 bullet point templates.

## Two Master Categories

**Blind bullets:** Conceal the secret, arouse curiosity. The reader must take action (buy, click, sign up) to learn the answer. Use for sales pages and lead generation.

**Naked bullets:** Reveal information directly. Demonstrate expertise by giving away real value. Use for service pages, feature lists, and blog content.

## The 21 Templates

### 1. The "Wrong!" Bullet
Contradict a common assumption. Creates immediate curiosity.

- "Think you need a dedicated IT team to run enterprise software? Wrong."
- "More menu items means more revenue, right? Wrong — and here's why."

### 2. The "Themed Sequence" Bullet
Group bullets under an evocative theme.

- "The 5 Silent Profit Killers in Every Restaurant Kitchen"
- "3 Inventory Mistakes That Look Smart But Cost You Thousands"

### 3. The "Two-Step" Bullet
Main statement + parenthetical that's the real hook.

- "The one report you should run every Monday morning. (Skip it and you won't notice the problem until it's cost you a month's profit.)"
- "Why your best employee might be your biggest security risk. (This has nothing to do with trust.)"

### 4. The "Giveaway" Bullet
Give away genuinely useful information. Readers think: "If the free stuff is this good, what do I get when I pay?"

- "Set your reorder point at 1.5x your average weekly sales — this single number eliminates 80% of stockout emergencies."
- "Run your daily reconciliation at 3pm, not closing time — here's why the timing matters more than the process."

### 5. The "Reverse Hook" Bullet
Interesting fact + unexpected benefit.

- "73% of restaurant waste happens before food reaches the plate. (Here's a 10-minute daily check that catches it.)"
- "The average small business loses 4 hours per week to manual data entry. (One setting change eliminates most of it.)"

### 6. The "Naked Benefit" Bullet
Direct benefit claim. No concealment — just clear value.

- "Process a complete sale in under 3 seconds, even during peak hours"
- "See your exact profit margins by product, by day, updated in real time"

### 7. The "Transactional" Bullet
Give me [small thing] → get [big benefit].

- "Give us 15 minutes to set up, and you'll save 2 hours every day on stock counts"
- "Spend 5 minutes on the daily dashboard, and you'll spot problems before they cost you money"

### 8. The "If-Then" Bullet
Easy compliance → valuable benefit.

- "If you can use a smartphone, you can run your entire pharmacy inventory"
- "If your staff can tap a screen, they can process any sale — no training manual needed"

### 9. The "Truth About" Bullet
Works with controversial or misunderstood topics.

- "The truth about 'cloud security' — and why most small businesses have it backwards"
- "The truth about loyalty programmes — most cost more than they earn"

### 10. The "Single Most" Bullet
Provable superior benefit. Use only when you can back it up.

- "The single fastest way to close your books at month-end"
- "The one report that tells you more about your business health than any other"

### 11. The "How-To" Bullet
Most common type. Must be specific and dimensional — not vague.

- Vague: "How to manage inventory better"
- Dimensional: "How to keep your shelves full of what sells and stop tying up cash in what doesn't"

### 12. The "Number" Bullet
Specific count of techniques, ways, or reasons.

- "7 settings most new users miss — each one saves 10+ minutes per day"
- "4 reports your accountant wishes you'd send (and how to generate them in one click)"

### 13. The "Sneaky" Bullet
Implies a hidden truth the reader suspected. Confirms their instinct.

- "The real reason most POS vendors lock you into long contracts"
- "What your supplier isn't telling you about minimum order quantities"

### 14. The "Better Than" Bullet
Find something good and make it better.

- "Better than spreadsheets: real-time stock levels that update automatically"
- "Better than a cash register: a complete business management system that fits in your pocket"

### 15. The "Simple Fact" Bullet
Use when you can't use a blind bullet. Present the scenario plainly.

- "When your internet goes down, your POS keeps working — every transaction syncs when you're back online"
- "Every sale automatically updates your stock count, your accounting, and your sales reports"

### 16. The "What" Bullet
Easiest to write. States what the reader will learn or get.

- "What to check every morning before opening your shop"
- "What the top 10% of restaurants do differently with their table turnover"

### 17. The "What NEVER" Bullet
Negative form, plays on fear of mistakes.

- "What to never say to a customer who asks for a discount"
- "The one thing you should never do during a stock take (most businesses do it every time)"

### 18. The "Do You?" Bullet
Target a mistake the reader is probably making.

- "Do you reconcile your cash drawer AFTER your staff leave? Here's why that's backwards."
- "Do you price your menu items based on food cost alone? You're leaving 15-20% margin on the table."

### 19. The "Reason Why" Bullet
Hides the reason, creating curiosity.

- "The reason why you should run payroll on Thursday, not Friday"
- "Why your busiest day might be your least profitable — and how to check in 2 minutes"

### 20. The "Secrets Of" Bullet
Unusual solution or method. Use sparingly — overuse weakens it.

- "The stock rotation method used by Nairobi's top supermarkets — and why it works for shops of any size"
- "How the best pharmacies track expiry dates without any extra work"

### 21. The "Probing Question" Bullet
Ask a question you know the reader can't answer confidently.

- "Do you know which of your products has the highest margin? (Hint: it's probably not your best seller.)"
- "Can you tell, right now, how much cash you should have in the drawer? (Most business owners can't.)"

## Mixing Rules

- **Use a minimum of 3-5 different bullet types per page.** Monotonous bullets defeat their purpose.
- **Break bullets into groups of 5-7** with a paragraph or subhead between groups. Walls of bullets lose impact.
- **Lead each group with your strongest bullet.** Readers notice the first and last in a group.
- **Never end a bullet with a full stop/period.** Periods signal "stop reading." End with an open thought, a question, or let the last word carry weight.
- **Mix blind and naked bullets.** Give away some value (naked) to create trust, then use blind bullets to create curiosity.

## Process

1. Write 5 bullets using each of the 21 types = 105 bullets
2. Select the top third (35 bullets)
3. Organise by section/topic
4. Mix types within each group
5. Test: read bullets aloud — do they create curiosity or state clear value? If neither, cut.
```

**Step 2: Commit**

```bash
git add sales-copywriting/references/fascination-bullets.md
git commit -m "Add fascination bullets reference — 21 templates with examples and mixing rules

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 4: Create `sales-copywriting/references/resistance-and-objections.md`

**Files:**
- Create: `sales-copywriting/references/resistance-and-objections.md`

**Step 1: Write the reference file**

```markdown
# Resistance & Objection Handling in Copy

How to write persuasive copy that overcomes the reader's natural resistance without triggering their defences.

## Bill Bonner's Theory of Resistance (AWAI)

### The Core Insight

There is natural tension between buyer and seller. The buyer ACTIVELY TRIES TO RESIST at every point. If the prospect can see and anticipate the direction of your sales argument, he erects defences and dismisses it.

### What Doesn't Work

| Approach | Why It Fails |
|----------|-------------|
| "15 Reasons to Choose Us" | Reader jumps ahead, figures out the pitch, dismisses it |
| Transparent sales copy | Reader sees through it, feels manipulated |
| Revealing the hook early | Reader sees it coming and avoids it |
| Showing where the copy is going | Reader decides not to take the trip |
| Letting the reader know he's being sold | The instant he consciously realises, he's gone |

### What Works

**Approach from an unexpected angle.** Don't lead with the obvious pitch. Lead with a story, an insight, a surprising fact — something that gives value before it asks for anything.

**Keep them off balance.** When they predict your next point, go somewhere else. When they erect a defence, go around it.

**Make the conclusion feel like THEIR idea.** Present evidence and let them connect the dots. Don't say "Therefore you should buy our product." Say "Here's what happened when [company] tried this approach..." and let them draw the conclusion.

**Never let them see where you're going.** This doesn't mean being vague. It means being interesting. Each paragraph should be surprising, valuable, or emotionally resonant — so they keep reading for the content, not because they're following your sales pitch.

### Market-Level Resistance

The marketplace builds up resistance to copy over time, like bacteria to antibiotics. Approaches that worked last year may feel stale this year. This is why:
- Every website must look and sound different (your existing design rule)
- Copy must use the client's authentic voice, not template language
- Fresh angles matter more than proven formulas applied robotically

### Practical Application

**Homepage hero:** Don't start with "We are [Company], the leading provider of..." Start with the customer's world — their problem, their aspiration, their daily reality.

**Services page:** Don't list services with features. Start with the outcome, then reveal how you deliver it. The reader should be thinking "I want that result" before they realise you're selling a service.

**About page:** Don't start with "Founded in 2015..." Start with why you exist — the problem you saw that no one was solving properly.

**Blog posts:** Don't start with "In this article, we will explore..." Start with a story, a question, a surprising fact, a bold claim. The first paragraph should make them forget they're on a business blog.

## The 4 Things Buyers Fear More Than Losing Money (Ray Edwards)

When someone hesitates, it's rarely about the money. These are the real barriers:

### 1. Hassle
They hate bureaucratic red tape more than the monetary loss. If returning your product or cancelling your service involves forms, phone trees, or waiting periods, they won't buy in the first place.

**In copy:** "Cancel with one email. No forms, no phone calls, no waiting period."

### 2. Stress
They don't want pushy follow-ups, aggressive upsells, or spouse disapproval.

**In copy:** "No sales calls. No pressure. Just the information you need to decide."

### 3. Looking Foolish
They fear others will judge them for being gullible or making a bad choice.

**In copy:** "Join 200+ businesses in East Africa who made the same choice." (Social proof removes the fear of being the only one.)

### 4. Feeling Foolish
They fear being duped or taken advantage of — that the product won't deliver.

**In copy:** Strong guarantee + specific proof + transformation testimonials.

### The Secret

Prospects secretly WANT you to be right. They secretly want to buy. They secretly hope you have the solution. Your job is not to convince a hostile audience — it's to remove the barriers for people who already want to say yes.

## Preemptive Objection Handling

### The Principle

Never ignore objections. Silence confirms the reader's worst fears. Address objections BEFORE they arise, woven naturally into copy.

### Common Objections and Where to Handle Them

| Objection | Where in Copy | How to Handle |
|-----------|---------------|---------------|
| "Is it worth the money?" | Before pricing section | Value anchoring: show ROI, contrast with cost of NOT solving |
| "Is it too complicated?" | Features/how-it-works section | Show simplicity: "If your staff can use a phone, they can use this" |
| "Will it work for MY situation?" | Throughout, especially services | Specific case studies from similar businesses |
| "Can I trust this company?" | About page, proof sections | Named clients, years in business, team photos, specific numbers |
| "What if it doesn't work?" | Near the CTA | Strong guarantee with specific terms |
| "I need to think about it" | Before and after CTA | Urgency (honest), cost of delay, easy first step |
| "My current solution works fine" | Problem section | Quantify what "fine" is actually costing them |

### The "Yes, But" Technique

Acknowledge the objection, then reframe:

- "Yes, migrating systems takes effort. But our setup team handles 90% of the work — most clients are live within 48 hours."
- "Yes, it's an investment. But consider: how much does one stockout cost you? Most of our clients recoup the annual cost within their first month."

### Objection Handling for Service Businesses

For service pages, every service description should preemptively answer:
1. "What exactly will I get?" (specifics, not vague promises)
2. "How long will it take?" (timeline, milestones)
3. "What do I need to do?" (their responsibilities — keep them minimal)
4. "What if I'm not happy?" (guarantee or revision policy)
5. "Why you and not someone cheaper?" (USP — what's unique about your approach)

## The Three Fundamental Rules of Selling (AWAI)

### Rule 1: People don't like being sold
Buying implies control. Being sold implies losing it. Don't pressure — tempt. Don't force — offer. Your job is to help them solve a problem.

### Rule 2: People buy on emotion, not logic
Sell to the heart first. The Seven Emotional Triggers: Fear, Greed, Vanity, Lust, Pride, Envy, Laziness. Create verbal pictures that tease desires.

### Rule 3: After buying emotionally, people justify with logic
After the emotional hook, provide the rational backup: data, specs, statistics, credentials. This lets them tell themselves: "I made the right decision because..."

## Emotional Triggers and When to Use Them

| Trigger | When Appropriate | Example in Copy |
|---------|-----------------|-----------------|
| **Fear of loss** | Problem amplification | "Every month you delay costs you $X in [specific loss]" |
| **Aspiration** | Transformation sections | "Imagine closing your books in 10 minutes instead of 3 hours" |
| **Pride** | Results/proof sections | "Join the businesses that run the smartest operations in the region" |
| **Relief** | After problem section | "No more midnight stock counts. No more spreadsheet errors. No more guessing." |
| **Belonging** | Social proof sections | "200+ businesses trust [product] to run their daily operations" |
| **Curiosity** | Headlines, bullet points | Use fascination bullets — see `fascination-bullets.md` |
```

**Step 2: Commit**

```bash
git add sales-copywriting/references/resistance-and-objections.md
git commit -m "Add resistance and objections reference — Theory of Resistance, 4 buyer fears, preemptive handling

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 5: Create `sales-copywriting/references/pastor-and-4ps.md`

**Files:**
- Create: `sales-copywriting/references/pastor-and-4ps.md`

**Step 1: Write the reference file**

```markdown
# PASTOR & 4 P's — Sales Page Frameworks

Use these frameworks ONLY for landing pages, sales pages, and product pages where the primary goal is conversion. Do not apply the full framework to About pages, blog posts, or informational content.

## The PASTOR Framework (Ray Edwards)

### P — Person, Problem, Pain

**Goal:** Make the reader feel understood before you offer anything.

1. **Identify the specific person.** Not "business owners" but "restaurant owners in Kampala managing 10-30 staff."
2. **Describe the problem in THEIR words.** Use language from client interviews, support tickets, reviews. Not your words — theirs.
3. **Articulate the pain.** What does this problem actually feel like day-to-day? Late nights, stress, lost money, embarrassment?

Key principle (Jay Abraham): "The more accurately you can describe your reader's problem in terms they relate to, the more they instinctively feel that you must have an answer."

Key principle (Robert Collier): "Join the conversation that is already taking place in the reader's mind."

### A — Amplify and Aspirations

**Goal:** Make the cost of inaction concrete, then paint the alternative.

1. **Amplify the consequences.** What happens if they DON'T solve this? Be specific.
   - Put a monetary cost on it: "Every month you continue with manual stock counts, you're losing an average of X hours and Y items to shrinkage."
   - Show the trajectory: "This problem gets worse, not better, as you grow."

2. **Paint the aspiration.** After establishing the cost, paint what life looks like when this is solved.
   - "Imagine knowing exactly what's in stock, what's selling, and what to reorder — every morning, without lifting a finger."

### S — Story, Solution, System

**Goal:** Bridge from problem to solution through narrative.

1. **Tell the story** of how this problem was solved — for you, for a client, for someone the reader can relate to.
2. **The story must be real.** Never fabricate. There is always a story to tell — dig deeper.
3. **Introduce the solution** naturally as part of the story, not as a product pitch.
4. **If there's a system or process**, describe it simply — 3-5 steps maximum.

### T — Transformation and Testimony

**Goal:** Show what changes, not what you deliver.

1. **Focus on the transformation.** Don't sell "8 modules and 12 reports." Sell "complete visibility into your business in 5 minutes a day."
2. **Provide real testimonials.** Hierarchy of believability:
   - Video testimonial (strongest)
   - Photo + full name + company + role
   - Full name + company
   - Full name only
   - Initials only (weakest — avoid if possible)
3. **Testimonials must answer three questions:**
   - Has this person done it themselves?
   - Have they helped others do it?
   - Can they help ME specifically?

### O — Offer

**Goal:** Make the offer crystal clear and transformation-focused.

1. **80% transformation, 20% deliverables.** Lead with what they GET (outcomes), not what you GIVE (stuff).
2. **Make the offer stand alone.** If someone reads only the offer section, they should understand enough to make a decision.
3. **Tie every deliverable to a transformation:**
   - Not: "Inventory management module"
   - But: "Inventory management module — so you always know what to order, when to order it, and never run out of your best sellers"
4. **Use the prospect's voice:** "Yes, I want to [transformation]..."

### R — Response

**Goal:** Tell them exactly what to do and why it matters.

1. **Ask directly.** "Click the button below to start your free trial."
2. **Tell them what happens next.** "You'll create your account in 2 minutes, and our team will help you import your data within 24 hours."
3. **Remind them why.** "Remember: every day without [solution] is another day of [problem]."
4. **Use one of the 5 closing templates** from `closing-and-guarantees.md`.

---

## The 4 P's Framework (AWAI / Paul Hollingshead)

A simpler alternative to PASTOR. Use when PASTOR feels too heavy for the page.

### Promise
- Identify a fear or desire — what keeps the prospect up at night or what they daydream about.
- Tell them what you're going to do about it. Be specific.
- This is the opening. Do NOT start with features, company history, or price.

### Picture
- Make them SEE themselves living with the problem solved.
- Use sensory language: what they'll see, feel, hear.
- Put them in the middle of the transformation.

Example: "Picture this: it's 6pm on Friday. Instead of hunching over spreadsheets, you're at home. Your phone buzzes — it's your daily report. Sales up 12%. Stock levels healthy. No emergencies. You smile and put the phone down."

### Proof
- Prove what you say is true.
- While proving, KEEP REMINDING of the promise (this is the clever twist).
- Use the 7 proof types: specific numbers, named case studies, expert endorsements, testimonials, statistics, awards, media mentions.
- Bob Bly's USP test: (1) Direct or implied benefit, (2) Important enough to move people, (3) Unique — competition can't or doesn't offer it.

### Push
- Make the specific offer with a clear call to action.
- Use price anchoring: show higher value first, then reveal the lower price.
- Create urgency — be specific: not "soon" but "by Friday at 5pm."
- A vague push translates to "never."

---

## The 15 Building Blocks of a Sales Letter (Ray Edwards)

For comprehensive sales pages, these building blocks map to PASTOR:

### P blocks:
1. **Pre-head (Eyebrow)** — "Attention, [Target Group]!"
2. **Headline** — The ad for the rest of the page. 2 seconds to grab attention.
3. **Deck copy** — Bold text between headline and body. Reinforces headline, arouses curiosity.

### A + S blocks:
4. **Lead** — Opening that sets criteria: who this is for and what they gain. Classic "If you [situation], then [promise]" structure.
5. **Body** — Bulk of text, contains all remaining elements.
6. **Subheads** — The bucket brigade. Scanners read ONLY subheads.
7. **Rapport** — Relationship building. People buy from people who are like them, who they want to be like, or who like them.
8. **Bullet points** — Fascination bullets (see `fascination-bullets.md`).

### T blocks:
9. **Credibility** — "Who am I and why should you listen to me?"
10. **Testimonials** — Third-party verification (see hierarchy above).

### O blocks:
11. **Value justification** — Demonstrate value is at least 10x price.
12. **Risk reversal** — Named guarantee (see `closing-and-guarantees.md`).
13. **Bonuses** — Relevant, unexpected additions that enhance value. Must be as good as a paid product.

### R blocks:
14. **Call to action** — Ask directly. Tell them exactly what to do.
15. **P.S.** — Use 1-3 (never more). Restate your entire proposition in one sentence plus a link. Readers scroll to the bottom first.

---

## The O.P.E.N. Scale — Matching Copy to Awareness Level

| Level | Awareness | Copy Approach |
|-------|-----------|--------------|
| **O** — Oblivious | Don't know they have a problem | Lead with education, stories, surprising facts. Soft offer. Long copy needed. |
| **P** — Pondering | Beginning to feel the pain | Validate the feeling. Amplify consequences. Softer offer. |
| **E** — Engaged | Actively looking for a solution | Compare options. Prove superiority. Mid-strength offer. |
| **N** — Need | Urgent, will buy now | Direct offer. Clear CTA. Minimal persuasion needed. |

**How to determine the level:** Look at how the visitor arrives.
- Organic search for problem keywords → Pondering or Engaged
- Referral from a trusted source → Engaged or Need
- Direct visit / returning visitor → Engaged or Need
- Social media / blog discovery → Oblivious or Pondering

Match your copy intensity to their awareness. An Oblivious reader needs 3x more copy than a Need reader.

---

## Value Anchoring Technique

When presenting pricing or packages:

1. **Itemise value separately:**
   | Component | Value |
   |-----------|-------|
   | Core system | $X |
   | Setup and training | $Y |
   | Ongoing support | $Z |
   | **Total Value** | **$X+Y+Z** |

2. **Reveal actual price as contrast:** "Your investment: just $[Price]"

3. **Frame as investment, not cost:** "Who wouldn't invest $500 to get $5,000 back?"

4. **Use Angie Lee's pricing psychology:**
   - Avoid round numbers (too easy to glance over)
   - Numbers ending in 7 perform best, then 3, then 9
   - Never compete on price — compare on value

---

## 9 Offer Types (Ray Edwards)

| Type | Description | Best For |
|------|-------------|----------|
| **Hard** | This is what you get, this is the price, buy now | Need-level prospects |
| **Soft** | Try for 30 days, we'll bill you if you keep it | Risk-averse prospects |
| **Charter** | First-time pricing, never offered again | New product launches |
| **Limited Supply** | Specific number available | High-demand products/services |
| **Limited Time** | Deadline, then offer ends | Promotions (must be real) |
| **Application** | Apply for the privilege of buying | High-ticket services |
| **Payment Plan** | Instalments for higher-ticket | Higher price points |
| **One-Time (OTO)** | Upsell, never available again (must enforce) | Post-purchase |
| **Negative Option** | Auto-subscription | SaaS (over-communicate terms) |

Choose the offer type that matches the prospect's awareness level (O.P.E.N. scale above).
```

**Step 2: Commit**

```bash
git add sales-copywriting/references/pastor-and-4ps.md
git commit -m "Add PASTOR and 4 P's reference — sales page frameworks, building blocks, offer types

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 6: Create `sales-copywriting/references/closing-and-guarantees.md`

**Files:**
- Create: `sales-copywriting/references/closing-and-guarantees.md`

**Step 1: Write the reference file**

```markdown
# Closing Templates & Guarantee Formulas

How to close copy and remove risk. These techniques apply to sales pages, landing pages, and any page with a conversion goal.

## 5 Closing Templates (Ray Edwards)

Each uses **transitional copy** first: recap benefits, restate the big idea, remind of the guarantee. Then the closing metaphor.

### 1. The "You Will Certainly Arrive" Close

> One year from today, you will certainly arrive. The question is: where?
>
> If you continue doing what you've been doing, you'll continue getting what you've been getting. That may be fine. But if you want [transformation], you have the opportunity right now to make that happen.
>
> [CTA button]

**Best for:** Aspirational products/services where the transformation takes time.

### 2. The "Different Results" Close

> If you want different results, you need to do something different.
>
> You've seen the proof. You've heard from [number] people who've already made the change. The only question is whether you'll keep doing things the hard way, or try a better approach.
>
> Make a definitive decision right now.
>
> [CTA button]

**Best for:** Products replacing an outdated method or competitor.

### 3. The "Crossroads" Close

> You're standing at a crossroads.
>
> To the left is the road you've been travelling — the spreadsheets, the late nights, the guesswork. You know where it leads because you've been there.
>
> To the right is the road fewer businesses choose — but every one that does wonders why they waited so long.
>
> [CTA button]

**Best for:** Decisions with clear before/after contrast.

### 4. The "Decision Time" Close

> In your moments of decision, your future is shaped.
>
> You now have all the information you need. You've seen what [product/service] does. You've seen the results. The only thing left is your decision.
>
> What will you decide right now?
>
> [CTA button]

**Best for:** Confident brands with strong proof sections.

### 5. The "Handholding" Close

> You won't be alone.
>
> From the moment you [sign up / place your order], our team is with you. Here's exactly what happens:
>
> 1. [Specific first step — what happens immediately]
> 2. [Specific second step — within 24 hours]
> 3. [Specific third step — within first week]
>
> You'll have [specific support: dedicated contact, phone number, training sessions]. We've done this [number] times. We know exactly how to get you from where you are to where you want to be.
>
> [CTA button]

**Best for:** Complex products/services where the prospect fears the transition.

---

## The 10-Part Guarantee Formula (Ray Edwards)

A weak guarantee: "100% money-back guarantee."
A strong guarantee transforms risk reversal into another selling opportunity.

### The 10 Parts

1. **Start with the code language:** "100% unconditional money-back guarantee" — this is required safety language that prospects recognise and trust.

2. **Sell benefits WITHIN the guarantee:** Restate key benefits inside the guarantee copy itself. The guarantee is another chance to sell.

3. **Integrate your USP:** What makes your guarantee different from everyone else's? Weave it in.

4. **Personalise it:** Make it YOUR personal promise, not a corporate policy. "I personally guarantee..." not "Our company guarantees..."

5. **Give the longest guarantee possible:** Longer guarantees = lower refund rates. 30 days < 60 days < 1 year < lifetime. (Counter-intuitive but consistently proven.)

6. **Show returns are easy:** Display phone number, email address, physical address. Prove there's no red tape.

7. **Make it unconditional:** "No questions asked. No forms. No hassle."

8. **Emphasise refund speed:** "We process refunds within 24 hours" — not "within 30 business days."

9. **Add the amazement twist:** Go beyond money back — "Keep the bonuses as our gift" or "Double your money back if..."

10. **Give it a name:** Not "Our Guarantee" but something evocative:
    - "[Company]'s Love-It-or-Leave-It, Keep-Everything Guarantee"
    - "The Try-It-for-60-Days, Risk-Nothing Promise"
    - "Our Sleep-Easy, No-Questions, Full-Refund Guarantee"

### Example: Weak → Strong

**Weak:**
> "We offer a 30-day money-back guarantee. If you're not satisfied, contact us for a refund."

**Strong:**
> **The [Company] Try-It-Risk-Free Promise**
>
> I personally guarantee that [Product] will [key transformation — e.g., "give you complete visibility into your business operations within your first week"]. If it doesn't, I don't want your money.
>
> You have a full 60 days to put [Product] to work. That's 60 days of [benefit 1], [benefit 2], and [benefit 3] — completely risk-free.
>
> If at any point you feel it's not right for you, simply email us at [email] or call [phone]. No forms, no waiting, no questions. We'll process your refund within 24 hours. And you keep any bonuses or training materials as our gift for giving us a fair try.
>
> That's how confident I am that [Product] will change the way you run your business.
>
> — [Founder Name], Founder

### When to Use Each Part

- **Service businesses:** Parts 1-7 minimum. Services can't easily offer "keep the product" so emphasise the personal promise and ease of cancellation.
- **Software/SaaS:** All 10 parts. Free trial + money-back guarantee is the strongest combination.
- **One-time products:** All 10 parts including the amazement twist.

---

## Risk Reversal Beyond Guarantees

Guarantees are one form of risk reversal. Other techniques:

| Technique | Example |
|-----------|---------|
| **Free trial** | "Try it for 14 days. No credit card required." |
| **Pilot project** | "We'll do a pilot with 5 users before you commit." |
| **Pay for results** | "You only pay when you see [specific result]." |
| **Free consultation** | "Let's discuss your situation — 30 minutes, no obligation." |
| **Case study proof** | "See exactly how [similar company] got results first." |
| **Partial commitment** | "Start with just one location. Expand when you're ready." |

---

## Urgency — Honest Techniques Only

**Legitimate urgency:**
- Real capacity limits ("We onboard 5 new clients per month to ensure quality")
- Real price changes ("Pricing increases on [date] when we add [feature]")
- Seasonal relevance ("Set up before the holiday rush")
- Cost of delay ("Every week without [solution] costs you approximately $X")

**Never fabricate urgency.** Fake countdown timers, fake "only 3 left" claims, and artificial deadlines destroy credibility permanently. If you don't have legitimate urgency, use the cost-of-delay approach instead.
```

**Step 2: Commit**

```bash
git add sales-copywriting/references/closing-and-guarantees.md
git commit -m "Add closing templates and guarantee formulas reference — 5 closes, 10-part guarantee, risk reversal

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 7: Enhance `blog-writer/references/storytelling.md`

**Files:**
- Modify: `blog-writer/references/storytelling.md` (253 lines — append new sections after line 253)

**Step 1: Read current file**

Run: Read `blog-writer/references/storytelling.md` to confirm current ending.

**Step 2: Append new sections**

Add these sections at the end of the file:

```markdown

## Sales Storytelling vs Informational Storytelling

**Informational storytelling** (default for blog posts): The story illustrates a point. The reader learns something. The CTA is secondary.

**Sales storytelling** (for landing pages, product pages, conversion copy): The story IS the selling mechanism. Every detail moves the reader toward action.

When writing sales-oriented stories, use the frameworks below. For standard blog articles, the Five-Beat Structure (above) remains your primary tool.

## The Dominant Story Idea (Ray Edwards)

Borrowed from movie trailers. Your product has a story — find it and build your copy around it.

### Three Elements:

1. **The Dominant Story Idea (DSI)** — Sum up your product's story the way a movie trailer sums up a film. One sentence. This becomes your headline and lead.

2. **Sample Feelings** — Show scenes that help the reader feel the feelings they want from the product. These become your bullet points and deck copy.

3. **Proof It Works** — Testimonials, case studies, before/after. Distributed throughout.

### Finding Your DSI:
- Immerse yourself in the product and the client's world
- Read copy from OTHER industries and ask "How might this story apply to my client?"
- Ask: "If this product were a film, what film would it be?"
- Watch the news for current tie-ins

### Using Your DSI:
- Get it into the headline and lead
- Summarise Sample Feelings in bullet points
- Distribute proof throughout the body

## John Forde's Story Construction Process (AWAI)

### 1. Know Your Story
- Study everything about the subject
- Read everything available
- Close your eyes and tell yourself what the story is about
- Write the details different ways
- Pick the most effective approach

### 2. Prepare Your Story
- Ask what message you want to convey
- Identify the key moment that makes it compelling and relates to your promise

### 3. Identify the Arc
- Start by figuring out how the story ENDS
- List inspiring details and order them
- Start in the MIDDLE of the story (where the action is) — not the beginning

### 4. Construct the Story
- Make it tight: use only important details, cut ruthlessly
- Hint at the big benefit to come
- Tell it quickly — don't meander
- Stick to the truth
- Rely on specificity and juicy details
- When finished, tie it all together with your promise, then transition to the rest

## 6 Places to Find Stories (AWAI)

1. **Talk to the creator/founder** — there's almost always an interesting backstory
2. **Discover how the product was developed** — unusual origins, accidental discoveries, pivots
3. **Learn what goes into production** — exotic ingredients, new technology, careful processes
4. **Talk to the team** — customer service, product development, sales staff all have stories
5. **Mine testimonials deeply** — call the person, have them expand, record the conversation. Ask "How did you feel?" not just "What happened?"
6. **Current events and trends** — tie your story to something happening now

## Seth Godin's 9 Qualities of Great Stories

1. **True** — consistent and authentic (not necessarily factual, but always honest)
2. **Bold promise** — fun, safety, or a shortcut; must be exceptional or not worth telling
3. **Trusted** — earned credibility to tell the story
4. **Subtle** — fewer details spelled out = more powerful; let readers draw conclusions
5. **Happen fast** — first impressions are far more powerful than we credit
6. **Appeal to senses, not logic** — create feelings, not arguments
7. **Rarely aimed at everyone** — narrow audience spreads the story; water it down and it appeals to no one
8. **Don't contradict themselves** — consistency across all touchpoints
9. **Agree with the audience's worldview** — best stories don't teach anything new; they make the audience feel smart and right

## Jen Stevens' Authenticity Rules (AWAI)

### 1. Employ specific details
- Bad: "The business was successful, very successful."
- Good: "Within 18 months, they'd opened three locations across Kampala, employed 45 staff, and processed 2,000 orders per week."

### 2. Avoid filler words
Eliminate: fashionable, lovely, charming, upscale, colourful, beautiful, amazing, incredible. These are lazy descriptions that don't paint specific pictures. Replace with concrete detail.

### 3. Use strong verbs
Replace "to be" and "to have" with verbs that describe action or offer visual images.
- "swept through" instead of "was in"
- "tucked into" instead of "had"
- "launched" instead of "started"

### 4. Ferret out details others overlook
- What did you see, smell, hear, feel?
- Offer exact numbers
- When gathering testimonials, don't just ask "what happened" — ask "how did you feel?" and "in what ways did this change how you see things?"
- Draw out specific details: not "business improved" but "we hired two new staff and finally took a holiday for the first time in three years"

## 14 Storytelling Tips for Copywriters (John Forde, AWAI)

1. **Appear spontaneous** — study until the message is second nature, then write naturally
2. **Give hope** — for things to come
3. **Show passion** — necessity, not optional
4. **Overcome obstacles** — drama is about obstacles and how they're overcome
5. **Make it personal** — personal stories prove what logic can't
6. **Name the hero** — show your reader how they'll triumph
7. **Name a villain** — what keeps the prospect up at night? That's your villain
8. **Reward and tease** — reward with progress, tease with more to come
9. **Enlarge and enrich** — remind what's important, raise the bar
10. **Build a relationship** — between brand and customer, beneath the surface
11. **Commute facts to the subconscious** — embed facts painlessly through story
12. **Have a good twist** — unexpected angle that keeps them reading
13. **Make sense** — knowledgeable customers spot fakes immediately
14. **Leave them wanting more** — know the final emotion and write toward it
```

**Step 3: Commit**

```bash
git add blog-writer/references/storytelling.md
git commit -m "Enhance storytelling reference with DSI, Forde's construction, Godin's 9 qualities, Stevens' authenticity

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 8: Enhance `blog-writer/references/writing-craft.md`

**Files:**
- Modify: `blog-writer/references/writing-craft.md` (791 lines — append after line 791)

**Step 1: Read current file ending**

Run: Read `blog-writer/references/writing-craft.md` offset 780 to confirm current ending.

**Step 2: Append new sections**

Add after current content:

```markdown

## Advanced Research Methods

### Gene Schwartz's 4-Read Research Method

Before writing about any product or topic, read all available material 4 times:

1. **First read:** Get the general idea. Don't take notes. Just absorb.
2. **Second read:** Underline heavily. Aim for 40-50 pages of underlined material from a book-length source.
3. **Third read:** Type up your underlined material. This forces precision in vocabulary — you'll capture the exact words clients, experts, and users employ.
4. **Fourth read:** Structure emerges. Go over your typed notes and begin organising.

"Copywriting is research. It has something I call 'claim density.' It's packed with facts, with information, with ideas." — Gene Schwartz

**Adapted for blog writing:** When writing about a client's industry, read their website, marketing materials, competitor sites, and industry publications. Read them multiple times. The vocabulary, the concerns, the specific language — all of this becomes raw material for authentic copy.

### The Golden Nuggets Technique (Don Mahoney, AWAI)

Embed your writing with fascinating bits of information that stimulate the reader's imagination.

**How it works:**
- When you tell somebody something they didn't know, you give them something for free
- On a subconscious level, they feel gratitude
- They're more likely to keep reading and more likely to respond
- Simultaneously, you build credibility as someone who knows the subject deeply

**Examples:**
- Instead of "Coffee is popular in East Africa," write: "Ethiopia produces over 400,000 tonnes of coffee annually — and the best lots never leave the country."
- Instead of "Mobile payments are growing," write: "M-Pesa processes more transactions per month than Western Union does globally in a year."

**How to find Golden Nuggets:**
- Read industry reports and pull surprising statistics
- Interview subject matter experts and ask "What's something most people get wrong about this?"
- Look for historical context — how things used to work vs how they work now
- Find counter-intuitive facts that challenge assumptions

### The Prospect Visualisation Technique (AWAI)

Before writing for any audience:
1. Sum up the reader in a few lines (demographics, fears, desires)
2. Think of someone you personally know who fits this description
3. If possible, find a photo and keep it visible while writing
4. Think about how you'd talk to this specific person
5. What words would you use? What tone? How much evidence would they need?

This transforms "writing for an audience" into "writing for a person" — the single most effective way to produce authentic copy.

## Advanced Authenticity Techniques

### Writing With Passion (AWAI)

1. Study the subject and list all its good qualities
2. Get genuinely excited about it — find the angle that interests YOU
3. Start naturally "selling" the topic in casual conversation
4. Even temporary enthusiasm that fades after writing is effective in the draft
5. If you fail to write with passion, you'll put the reader to sleep

### Three Tricks to Eliminate "Adspeak" (Paul Hollingshead)

1. **Imagine the person you're writing to.** Picture them as a friend.
2. **Believe that what you're writing about will improve their life.** If you don't believe it, find the angle where it's true.
3. **Figure out what it would take to convince YOU.** Your skepticism mirrors theirs.

### Claude Hopkins' 3 Rules for Connecting With Readers

1. **Know who you're writing for.** Ask who benefits most. Ask who has purchased before.
2. **Speak in their language.** Don't preach, bully, or talk down. Don't be bigger, smarter, or more sophisticated. Write the way you'd talk to a friend.
3. **Take helping seriously.** Offer real solutions, not flimsy ones. Back everything with research, details, facts, numbers. No humour that steals credibility or breaks momentum.

### Ted Nicholas' Peak State Preparation

For writing sessions that require genuine energy and voice:
1. Get fully rested
2. Eat lightly before writing
3. Light exercise to get alert
4. Eliminate interruptions
5. Prime your mind with positive thoughts
6. Take a brisk 5-minute walk before writing

"When writing, imagine you are talking to a friend or loved one. Credibility, tone, and warmth come from the feelings you generate through the words you write." — Ted Nicholas
```

**Step 3: Commit**

```bash
git add blog-writer/references/writing-craft.md
git commit -m "Enhance writing craft with Schwartz research method, Golden Nuggets, authenticity techniques

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 9: Enhance `page-builder/references/website-copywriting.md`

**Files:**
- Modify: `page-builder/references/website-copywriting.md` (768 lines — append after line 768)

**Step 1: Read current file ending**

Run: Read `page-builder/references/website-copywriting.md` offset 755 to confirm current ending.

**Step 2: Append new sections**

Add after current content:

```markdown

## Cross-References to Sales Copywriting

For enhanced copywriting techniques, consult these references from the `sales-copywriting` skill:

| Technique | Reference | Use When |
|-----------|-----------|----------|
| Headline formulas (10 templates + 4 U's scoring) | `sales-copywriting/references/headline-mastery.md` | Writing ANY headline |
| Fascination bullets (21 templates) | `sales-copywriting/references/fascination-bullets.md` | Writing bullet points that need to persuade |
| Objection handling and anti-resistance | `sales-copywriting/references/resistance-and-objections.md` | Services pages, pricing, FAQ |
| PASTOR and 4 P's frameworks | `sales-copywriting/references/pastor-and-4ps.md` | Landing pages, sales pages |
| Closing templates and guarantees | `sales-copywriting/references/closing-and-guarantees.md` | CTAs, guarantee sections, pricing pages |

## Proof Integration Per Page Type

Proof should be woven throughout copy, not confined to a testimonials page.

| Page | Proof Type | Placement |
|------|-----------|-----------|
| **Homepage** | Hero: one bold claim with specific number. Below fold: 2-3 named client logos or results. | Within first 2 scrolls |
| **Services** | Per-service: one case study snippet or specific result. | Within each service description |
| **About** | Team credentials, years of experience, number of clients served. | Woven into narrative, not listed |
| **Contact** | "Join X businesses who..." or one short testimonial. | Above or beside the form |
| **Pricing** | ROI calculation or "pays for itself in X days." | Before or within pricing table |
| **FAQ** | Link objection answers to proof: "Here's what [client] experienced..." | Within relevant answers |

## Value Anchoring for Pricing Pages

When building pricing pages or sections:

1. **Lead with the transformation, not the price.** The reader should want the result before they see the cost.
2. **Itemise value components** to show total value exceeds price.
3. **Frame as investment:** "Your investment" not "The cost."
4. **Show ROI:** "Most clients recoup their investment within [timeframe]."
5. **Avoid round numbers** in pricing — numbers ending in 7 outperform, then 3, then 9.
6. **Never compete on price.** Compare on value, outcomes, and unique benefits.
```

**Step 3: Commit**

```bash
git add page-builder/references/website-copywriting.md
git commit -m "Enhance website copywriting with sales-copywriting cross-references, proof integration, value anchoring

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 10: Add integration references to existing skills

**Files:**
- Modify: `page-builder/SKILL.md` (690 lines)
- Modify: `blog-writer/SKILL.md` (897 lines)
- Modify: `brand-alignment/SKILL.md` (400 lines)

**Step 1: Read the reference file sections of each SKILL.md**

Read the top ~40 lines of each to find where reference files are listed.

**Step 2: Add to page-builder/SKILL.md**

Find the section near line 9 where references are listed. Add:

```
- `sales-copywriting/references/headline-mastery.md` — Read for ALL headlines (10 formulas + 4 U's scoring)
- `sales-copywriting/references/fascination-bullets.md` — Read when writing bullet points
- `sales-copywriting/SKILL.md` — Read FULL skill when building landing pages, sales pages, or product pages
```

**Step 3: Add to blog-writer/SKILL.md**

Find the section near line 12-21 where references are listed. Add:

```
- `sales-copywriting/references/headline-mastery.md` — Read for ALL blog headlines (10 formulas + 4 U's scoring)
- `sales-copywriting/references/resistance-and-objections.md` — Read for persuasive and opinion articles
```

**Step 4: Add to brand-alignment/SKILL.md**

Find the section near line 83 where skill relationships are described. Add a note:

```
- **sales-copywriting** — Persuasion techniques must align with brand voice. Level 2 persuasion (confident, professional) is the default ceiling. Hard-sell tactics (Level 3) require explicit client approval in the style brief.
```

**Step 5: Commit**

```bash
git add page-builder/SKILL.md blog-writer/SKILL.md brand-alignment/SKILL.md
git commit -m "Add sales-copywriting integration references to page-builder, blog-writer, brand-alignment

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 11: Update CLAUDE.md and README.md

**Files:**
- Modify: `CLAUDE.md`
- Modify: `README.md`

**Step 1: Read CLAUDE.md**

Read `CLAUDE.md` to find exact locations for:
- Utility Skills section (around lines 28-41)
- "All Skills" count if present

**Step 2: Add sales-copywriting to CLAUDE.md utility skills list**

After the `color-selection/SKILL.md` line, add:

```
sales-copywriting/SKILL.md             ← Persuasion and conversion copywriting (hybrid: cross-cutting headlines/CTAs + on-demand PASTOR/4P's for sales pages)
```

**Step 3: Read README.md**

Read `README.md` to find where skills are described. Add sales-copywriting in the appropriate section.

**Step 4: Commit**

```bash
git add CLAUDE.md README.md
git commit -m "Add sales-copywriting to project documentation

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 12: Update memory file

**Files:**
- Modify: `C:\Users\Peter\.claude\projects\C--wamp64-www-website-skills\memory\MEMORY.md`

**Step 1: Update the All Skills count and add sales-copywriting entry**

Update:
- Change "All Skills (22 total, as of 2026-03-04)" to "All Skills (23 total, as of 2026-03-05)"
- Add to Utility list: `sales-copywriting`
- Add a "Recently Added Skills" entry for sales-copywriting with date and description

**Step 2: No commit needed** (memory files are not in the repo)

---

## Task Summary

| Task | What | Files |
|------|------|-------|
| 1 | Create sales-copywriting SKILL.md | 1 new |
| 2 | Create headline-mastery.md reference | 1 new |
| 3 | Create fascination-bullets.md reference | 1 new |
| 4 | Create resistance-and-objections.md reference | 1 new |
| 5 | Create pastor-and-4ps.md reference | 1 new |
| 6 | Create closing-and-guarantees.md reference | 1 new |
| 7 | Enhance storytelling.md | 1 modified |
| 8 | Enhance writing-craft.md | 1 modified |
| 9 | Enhance website-copywriting.md | 1 modified |
| 10 | Add integration refs to 3 skills | 3 modified |
| 11 | Update CLAUDE.md + README.md | 2 modified |
| 12 | Update memory file | 1 modified |

**Total: 6 new files, 8 modified files, 12 commits.**
