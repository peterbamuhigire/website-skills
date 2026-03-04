---
name: blog-idea-generator
description: Generate a curated list of blog post ideas tailored to a specific business, audience, and goals. Uses a guided interview to gather context (or reads existing client docs), then produces 15-25 prioritised topic ideas with titles, angles, keywords, and suggested structures. Use when the user says "generate blog ideas", "what should I blog about", "blog topic ideas", "content ideas", "blog brainstorm", or wants to populate a topic-ideas.md file.
---

# Blog Idea Generator

Generate 15-25 targeted blog post ideas for any client website. Each idea includes a working title, unique angle, target keyword, buyer journey stage, suggested article structure, and estimated word count.

**Read `references/ideation-frameworks.md`** before generating ideas — it contains the complete toolkit of techniques used in the process below.

---

## Step 1: Gather Context

### If client docs exist (preferred)

Read these files to pre-fill context:

1. `docs/en/company-profile.md` — business description, services, expertise, location
2. `docs/en/services.md` — service offerings, target customers
3. `docs/en/pages.md` — existing website pages and content
4. `docs/sector-brief.md` — industry context (if present)
5. `blog-writer/references/topic-ideas.md` — existing topics (if present, avoid duplicates)
6. `src/pages/en/blog/` — existing articles (avoid overlap)

Extract from these files:
- What the business does (core services)
- Who they serve (target audience segments)
- Where they operate (geographic focus)
- What makes them different (competitive advantage)
- What expertise the author has (experience, credentials)

### Then ask the user these questions

Even after reading docs, confirm and fill gaps with the guided interview. Ask one question at a time using AskUserQuestion. Skip questions already answered by the docs.

**The 8 Essential Questions:**

1. **Target audience** — "Who is your ideal reader? Be as specific as possible (job title, company size, industry, location)."
2. **Pain points** — "What are the top 3 problems your customers face that your business solves?"
3. **Business goals** — "What should blog readers DO after reading? (Contact you, book a demo, download something, understand a concept?)"
4. **Competitor content** — "Name 2-3 competitor websites or blogs in your space. What topics do they cover?"
5. **Unique expertise** — "What do you know that most of your competitors don't? What's your unfair advantage?"
6. **Customer questions** — "What questions do customers ask most often before buying?"
7. **Content gaps** — "What topics have you wanted to write about but haven't yet?"
8. **Tone and voice** — "How should the blog sound? (Technical expert, friendly advisor, industry insider, thought leader?)"

If the user provides brief answers, that's fine — work with what you have. Don't over-question.

---

## Step 2: Generate Ideas Using the Five-Method System

Apply all five ideation methods from `references/ideation-frameworks.md` to produce a diverse set of ideas. Aim for 25-30 raw ideas, then filter to the best 15-25.

### Method 1: Expert Method (Category Drilldown)

Identify 4-6 content categories from the business's services and expertise. For each category, generate 3-5 specific blog post ideas by drilling into sub-topics.

### Method 2: Offer Method (Buyer Awareness Stages)

Map ideas to each stage of the buyer's awareness:
- **Unaware** — articles that surface a problem the reader doesn't know they have
- **Problem-aware** — articles that help the reader understand their problem better
- **Solution-aware** — articles that show approaches to solving the problem
- **Decision-ready** — articles that help the reader choose the right solution

Generate at least 2 ideas per stage.

### Method 3: Pain Point Mining

For each of the top 3 customer pain points, generate 2-3 article ideas using these angles:
- The mistake angle ("5 mistakes that cause [pain point]")
- The how-to angle ("How to fix [pain point] in [timeframe]")
- The case study angle ("How [type of business] solved [pain point]")

### Method 4: Spin Technique (Competitor Gap Analysis)

Based on the competitor info provided, identify:
- What topics competitors cover well (avoid these unless you have a better angle)
- What topics they miss entirely (opportunity)
- What consensus advice you can challenge with evidence (contrarian angle)

Generate 3-5 ideas from gaps and counter-angles.

### Method 5: Customer Question Mapping

Turn each frequently asked customer question into a blog post idea. The title should echo the question; the article should be the definitive answer.

---

## Step 3: Filter and Prioritise

### Quality Filters

Remove any idea that fails these tests:

| Filter | Test |
|--------|------|
| **25-topic test** | Could you write 25 variations? If not, the angle is too narrow. |
| **High-value goal** | Does this help the reader make/save money, reduce risk, save time, or gain advantage? |
| **Unique expertise** | Does this require knowledge that isn't commonly available? |
| **So-what test** | Would the target reader care enough to click? |
| **Longevity** | Will this still be relevant in 12 months? |

### Tier Classification

Sort surviving ideas into three tiers:

| Tier | Purpose | Characteristics |
|------|---------|-----------------|
| **Tier 1: SEO drivers** | Attract organic traffic | Long-tail keywords, search intent match, evergreen |
| **Tier 2: Authority builders** | Establish expertise | Industry analysis, original frameworks, deep guides |
| **Tier 3: Thought leadership** | Build brand and trust | Opinion pieces, contrarian takes, predictions, stories |

Aim for: 6-8 Tier 1, 5-7 Tier 2, 4-5 Tier 3.

---

## Step 4: Format and Present Ideas

### Present to the User

Show the ideas in a table, grouped by tier:

```
## Tier 1: SEO Drivers (attract organic traffic)

| # | Working Title | Angle | Target Keyword | Journey Stage | Structure | Words |
|---|---------------|-------|----------------|---------------|-----------|-------|
| 1 | "How to Choose an ERP System for Your Retail Business" | Buyer's guide with decision framework | "erp system retail" | Solution-aware | What/Why/How | 2,000 |
```

For each idea, include:
- **Working title** — practical + creative (see headline patterns in `references/ideation-frameworks.md`)
- **Angle** — what makes this article different (1 sentence)
- **Target keyword** — primary long-tail keyword
- **Journey stage** — Unaware / Problem-aware / Solution-aware / Decision-ready
- **Structure** — which content organisation pattern (Problem/Solution, How-to, List, Q&A, etc.)
- **Words** — estimated word count (1,500-2,500 for standard, 2,500+ for pillar content)

### Ask the user for feedback

After presenting, ask:
- Which ideas excite you most?
- Any ideas to remove or modify?
- Any topics you expected but don't see?

Refine based on feedback.

---

## Step 5: Save Output

Save the final approved list to `blog-writer/references/topic-ideas.md` using this format:

```markdown
# Blog Topic Ideas — [Client Name]

Generated: YYYY-MM-DD
Target audience: [summary]
Content categories: [list]

## Tier 1: SEO Drivers

### 1. [Title]
- **Category:** [category]
- **Keywords:** [primary], [secondary]
- **Angle:** [1-2 sentences]
- **Journey stage:** [stage]
- **Structure:** [pattern] | **Words:** [count]
- **Section outline:**
  1. [h2 heading idea]
  2. [h2 heading idea]
  3. [h2 heading idea]
  4. [h2 heading idea]
  5. [h2 heading idea]

## Tier 2: Authority Builders
...

## Tier 3: Thought Leadership
...

## Content Calendar Suggestion

| Month | Article 1 (Tier) | Article 2 (Tier) |
|-------|-------------------|-------------------|
| Month 1 | [title] (T1) | [title] (T2) |
...
```

If the file already exists, merge new ideas — don't overwrite existing topics that haven't been written yet. Mark previously written topics as `[PUBLISHED]`.

---

## Headline Patterns Quick Reference

Use these patterns when crafting working titles (more in `references/ideation-frameworks.md`):

| Pattern | Template |
|---------|----------|
| Rule-based | "The N Rules of [Topic] Every [Audience] Should Know" |
| Mistake-based | "N [Topic] Mistakes That Cost [Audience] [Consequence]" |
| Contrarian | "Are You [Doing Thing] by Following Everyone's [Advice]?" |
| How-to | "How to [Achieve Goal] in [Timeframe/Context]" |
| Direct promise | "[Specific Outcome] for [Specific Audience]" |
| Question | "What Happens When [Scenario]?" |
| Myth-busting | "N Things the Experts Don't Tell You About [Topic]" |
| Guide | "The [Audience]'s Guide to [Topic]" |
| Lazy | "The Lazy [Audience]'s Guide to [Topic]" |
| Tools | "N Time-Saving [Tools/Services] for [Audience] in [Niche]" |

---

## Quality Checklist

Before finalising the idea list:

- [ ] At least 15 ideas across all 3 tiers
- [ ] No duplicate angles (each idea is distinct)
- [ ] At least 2 ideas per buyer awareness stage
- [ ] Ideas span at least 3 content categories
- [ ] Every title contains a target keyword or keyword-adjacent phrase
- [ ] No overlap with existing published articles
- [ ] Mix of article structures (not all lists, not all how-tos)
- [ ] At least 3 ideas that showcase the author's unique expertise
- [ ] At least 2 ideas based on real customer questions
- [ ] Content calendar covers at least 6 months at 2 articles/month
