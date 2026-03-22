# UI/UX Skill Enhancement from Tidwell + StoryBrand — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Weave interaction design patterns from Tidwell "Designing Interfaces" and brand messaging from StoryBrand SB7 into existing website-skills.

**Architecture:** Three independent phases, each reading source text, creating a reference file, updating skills, then committing. Phases 1 and 2 draw from `tidwell-designing-interfaces.txt` (lines already known); Phase 3 from `storybrand.txt`.

**Tech Stack:** Markdown files only. No code. Read/Write/Edit tools only.

**Key line offsets in source files:**
- `tidwell-designing-interfaces.txt`: Ch1=563, Ch3=3200, Ch4=4608, Ch5=5351, Ch6=5977, Ch8=7421, Ch10=9462
- `storybrand.txt`: Ch4(Character)=962, Ch5(Problem)=1227, Ch6(Guide)=1601, Ch7(Plan)=1895, Ch8(CTA)=2103, Ch9(Failure)=2385, Ch10(Success)=2590, Ch11(Transform)=2870, Ch12(Website)=3121, Roadmap=3694

**500-line rule:** All SKILL.md files must stay under 500 lines. Check line count before and after edits.

---

## PHASE 1 — Tidwell Cognition + Visual → ux-psychology + design-system

### Task 1.1: Read Tidwell Ch1 (Cognition Patterns) and extract rules

**Files to read:**
- `tidwell-designing-interfaces.txt` lines 563–1500 (Ch1: Designing for People)

**Extract these patterns and their actionable design rules:**
- Safe Exploration (let users wander safely without losing progress)
- Instant Gratification (show progress immediately)
- Satisficing (users take first "good enough" option)
- Changes in Midstream (users change goals mid-task — keep state)
- Deferred Choices (let users skip optional decisions)
- Habituation (learned patterns become invisible)
- Microbreaks (users take attention breaks — design for re-entry)
- Spatial Memory (users remember where things are — keep navigation stable)
- Prospective Memory (users forget next steps — provide cues)
- Streamlined Repetition (repeated tasks need shortcuts)

### Task 1.2: Read Tidwell Ch4 (Layout) and extract rules

**Files to read:**
- `tidwell-designing-interfaces.txt` lines 4608–5350 (Ch4: Layout of Screen Elements)

**Extract these patterns:**
- Visual Framework (persistent header/nav/footer frame)
- Center Stage (dominant center content area with supporting panels)
- Grid of Equals (equal-weight items in a grid)
- Titled Sections (titled content blocks)
- Module Tabs (tabbed content within a page)
- Accordion (expandable sections to manage long pages)
- Responsive Enabling (show/hide content based on context)
- Progressive Disclosure (show detail only when needed)

### Task 1.3: Read Tidwell Ch5 (Visual Style) and extract rules

**Files to read:**
- `tidwell-designing-interfaces.txt` lines 5351–5976 (Ch5: Visual Style and Aesthetics)

**Extract these rules:**
- Preattentive variables (colour, size, shape, motion — what draws the eye first)
- Typography for readability (weight, contrast, leading, tracking)
- Colour psychology in UI (trust, urgency, neutral, brand)
- Flat vs skeuomorphic decision criteria
- When minimalism works vs when it frustrates

### Task 1.4: Read Tidwell Ch8 (Actions) and extract rules

**Files to read:**
- `tidwell-designing-interfaces.txt` lines 7421–8643 (Ch8: Doing Things — Actions and Commands)

**Extract these patterns:**
- Button Groups (visually grouping related actions)
- Prominent "Done" Button (make the obvious next step obvious)
- Preview (show result before committing)
- Spinners and Loading Indicators (when and how)
- Cancelability (allow users to stop long operations)
- Multilevel Undo (enable recovery from mistakes)
- Smart Menu Items (context-aware, disabled when not applicable)

### Task 1.5: Create reference file

**File to create:** `book-extractions/tidwell-cognition-visual-patterns.md`

Structure:
```
---
source: Designing Interfaces 3rd Ed (Tidwell, Brewer, Valencia — O'Reilly 2020)
chapters: Ch1 Cognition Patterns, Ch4 Layout, Ch5 Visual Style, Ch8 Actions
purpose: Reference for ux-psychology and design-system skills
---

# Tidwell: Cognition, Visual, and Action Patterns

## Cognition Patterns (Ch1)
[all extracted patterns with What/When/Why/How]

## Layout Patterns (Ch4)
[all extracted patterns]

## Visual Style Rules (Ch5)
[all extracted rules]

## Action Patterns (Ch8)
[all extracted patterns]
```

### Task 1.6: Update ux-psychology/SKILL.md

**File to modify:** `ux-psychology/SKILL.md`

**Add after the existing Section 6 (Affordances):**

```markdown
## 8. TIDWELL COGNITION PATTERNS (Designing Interfaces, 3rd Ed)

Design for how people actually behave — not how we wish they'd behave.

### Safe Exploration
Users explore more if they know they can undo mistakes.
- Every destructive action must be reversible or require confirmation
- Auto-save drafts so exploration never means data loss
- "Test mode" or preview screens reduce fear of commitment

### Instant Gratification
Users want to see results immediately.
- Load the most important content first; defer supplementary content
- Show skeleton screens so progress is visible from the first frame
- Never make users wait on a blank screen for more than 200ms

### Satisficing
Users take the first option that's good enough, not the best option.
- Put the most likely choice first in every list, dropdown, or menu
- Design defaults as the answer most users would choose anyway
- Do not bury the correct choice below less likely options

### Changes in Midstream
Users frequently change their minds mid-task.
- Preserve form state across page refreshes and navigation
- Multi-step flows must allow backwards navigation without data loss
- Session persistence: returning after 30 minutes should restore state

### Deferred Choices
Users skip decisions they are not ready to make.
- Make optional fields genuinely skippable (no required flag, no blocking)
- "Fill this in later" mechanisms for onboarding flows
- Provide smart defaults so skipped fields don't create broken states

### Habituation
Repeated interactions become automatic and invisible.
- Consistent placement of navigation, actions, and labels is essential — move them and users feel disoriented
- Tooltips and help text are read once; after that, layout must self-explain
- Change warnings are critical: "We've updated our navigation" prevents confusion

### Spatial Memory
Users remember where on the screen things live.
- Never move navigation items between pages
- Pin primary actions to consistent screen locations (bottom-right for desktop CTA; top-right for mobile icon)
- If layout must change (responsive), animate the transition so users can follow elements

### Prospective Memory
Users forget what they were going to do.
- Use breadcrumbs, progress steps, and section titles to remind users where they are
- After a page load, scroll position and context must make the task obvious
- Email / notification reminders for deferred actions reduce abandonment

### Microbreaks
Users take short attention breaks; they must be able to re-enter context quickly.
- Page titles and section headings must convey full context without reading body text
- Re-entering a multi-step flow mid-way must show completed steps clearly
- "Where was I?" is a question your UI should answer at a glance

See full pattern details: `book-extractions/tidwell-cognition-visual-patterns.md`
```

Check line count after: must be under 500 lines.

### Task 1.7: Update design-system/SKILL.md

**File to modify:** `design-system/SKILL.md`

**Add after the existing Section 8 (Component Patterns):**

```markdown
## Tidwell Layout + Visual Patterns

### Layout Architecture Patterns

**Visual Framework**
Every page needs a persistent visual frame: consistent header, footer, and (on desktop) sidebar. This frame orients users across all pages. The frame must never move — only the center stage content changes.
- Header: logo + primary nav + utility nav (search, account)
- Footer: sitemap links, legal, social — visually distinct from body
- Sidebar (if used): contextual nav, filters, related content
- Center stage: the primary content for that page only

**Center Stage**
The primary content area is the largest region and gets the most visual weight. Supporting elements (sidebar, breadcrumbs) must be visually subordinate.
- Center stage content gets more whitespace, larger type, higher contrast
- Never let a sidebar visually compete with center stage
- On mobile: sidebar collapses; center stage becomes full width

**Grid of Equals**
When displaying a collection of equal-weight items (features, services, team, testimonials), use a grid that treats each item identically.
- Same card dimensions, same image aspect ratio, same text hierarchy
- Visual inequality in a "grid of equals" implies ranking that isn't intended
- Break symmetry deliberately: a 2-1 ratio signals "this one is special"

**Titled Sections**
Every major content block needs a title. Untitled sections are visually and semantically invisible.
- Title → subtitle (optional) → content: always this hierarchy
- Titles must be scannable: "What we do" beats "A comprehensive suite of end-to-end solutions"
- Section titles anchor spatial memory — users remember content by section name

**Progressive Disclosure**
Show only what's needed for the current task. Reveal detail on demand.
- Tier 1: essential information (visible by default)
- Tier 2: supporting detail (revealed on expand, tab, or scroll)
- Tier 3: edge cases and advanced options (help overlay, separate page)
- Violating this forces all users to process information only power users need

**Accordion**
For long pages with multiple content sections: use accordion to collapse non-essential sections.
- First section should default-open (most important)
- One open section at a time (exclusive) unless content comparisons require multiple open
- Section headers must be clickable across their full width (44px min height)
- Never accordion primary navigation — only secondary/supplementary content

### Action Design Patterns

**Button Groups**
Actions that belong together must be visually grouped. Isolated buttons imply they are the only action.
- Primary action rightmost in a horizontal group (F-pattern reading ends right)
- Destructive action must be visually separated from primary — never adjacent
- Icon-only buttons in groups require tooltips on hover; standalone icon buttons need visible labels

**Prominent Done / Next Button**
Every screen must have an obvious "what do I do next" affordance.
- The primary action button must be the most visually prominent interactive element on the page
- Secondary action styled to ≤30% visual weight of primary
- If a screen has no primary action, it has no purpose — add one or remove the screen

**Preview Before Commit**
For any action that is hard to reverse, show a preview state first.
- Photo uploads: show thumbnail before final save
- Form submissions: show review screen before "Confirm"
- Bulk actions: show "You are about to delete 14 items" with item list before confirming

**Cancelability**
Any operation taking more than 2 seconds must be cancelable.
- Show a Cancel button adjacent to the progress indicator
- On cancel: restore prior state completely; do not leave partial data
- Confirm cancel if the operation was expensive to start: "Cancel this upload? You'll lose progress"

**Spinners and Loading Indicators**
- Under 300ms: no indicator needed
- 300ms–3s: spinner or progress bar
- Over 3s: progress bar with estimated time remaining + cancel option
- Never use a spinner for a full-page reload — use skeleton screens instead

See full action pattern details: `book-extractions/tidwell-cognition-visual-patterns.md`
```

Check line count after: must be under 500 lines. If over, trim by removing the "Liquid Glass" section detail (keep the rule; move detail to its reference file).

### Task 1.8: Commit Phase 1

```bash
cd C:/wamp64/www/website-skills
git add book-extractions/tidwell-cognition-visual-patterns.md
git add ux-psychology/SKILL.md
git add design-system/SKILL.md
git commit -m "feat: add Tidwell cognition, layout, visual, action patterns to ux-psychology + design-system"
```

---

## PHASE 2 — Tidwell Navigation + Mobile + Forms → page-builder + form-ux-design

### Task 2.1: Read Tidwell Ch3 (Navigation) and extract rules

**Files to read:**
- `tidwell-designing-interfaces.txt` lines 3200–4607 (Ch3: Getting Around)

**Extract these patterns with their design rules:**
- Clear Entry Points (defined starting points for content discovery)
- Menu Page (dedicated navigation/index pages)
- Modal Panel (overlays for focused tasks — when to use and when NOT to)
- Escape Hatch (always provide a way back to home/safety)
- Fat Menus (mega-menus for large site navigation)
- Breadcrumbs (location trail for deep hierarchies)
- Progress Indicator (step counters for multi-step flows)
- Animated Transition (motion that explains spatial relationships)
- Navigational models: Hub-and-Spoke, Fully Connected, Tree, Step-by-Step

### Task 2.2: Read Tidwell Ch6 (Mobile) and extract rules

**Files to read:**
- `tidwell-designing-interfaces.txt` lines 5977–6628 (Ch6: Mobile Interfaces)

**Extract these patterns:**
- Vertical Stack (single-column mobile layout)
- Filmstrip (horizontal swipe navigation)
- Touch Tools (contextual toolbars that appear on selection)
- Bottom Navigation (primary nav at bottom of screen)
- Collections and Cards (mobile-optimized card patterns)
- Generous Borders (minimum 44px touch targets + breathing room)
- Loading or Progress Indicators (mobile-specific loading patterns)
- How to approach a mobile design (the 5-step process)

### Task 2.3: Read Tidwell Ch10 (Forms) and extract rules

**Files to read:**
- `tidwell-designing-interfaces.txt` lines 9462–10523 (Ch10: Getting Input from Users)

**Extract these patterns:**
- Forgiving Format (accept multiple input formats, normalise on save)
- Structured Format (when rigid format is acceptable — phone, date)
- Fill-in-the-Blanks (sentence-style forms for simple data entry)
- Input Hints (examples shown in context, above field)
- Input Prompt (placeholder as a last resort only)
- Autocompletion (when and how to implement)
- Good Defaults + Smart Prefills (reduce cognitive load)
- Error Messages (inline, specific, actionable)

### Task 2.4: Create reference file

**File to create:** `book-extractions/tidwell-navigation-mobile-forms.md`

Structure:
```
---
source: Designing Interfaces 3rd Ed (Tidwell, Brewer, Valencia — O'Reilly 2020)
chapters: Ch3 Navigation, Ch6 Mobile, Ch10 Forms
purpose: Reference for page-builder and form-ux-design skills
---

# Tidwell: Navigation, Mobile, and Form Patterns

## Navigation Patterns (Ch3)
[all extracted patterns with What/When/Why/How]

## Mobile Patterns (Ch6)
[all extracted patterns]

## Form Patterns (Ch10)
[all extracted patterns]
```

### Task 2.5: Update page-builder/SKILL.md

**File to modify:** `page-builder/SKILL.md`

First read the file to find the best insertion point and check current line count.

**Add a new section "Navigation and Mobile Patterns (Tidwell)" with rules from Ch3 and Ch6:**

Key rules to weave in:
- **Clear Entry Points:** The homepage and every landing page must have 1-3 clearly visible entry points that match the 3 most common visitor intents. Never bury entry points below the fold.
- **Escape Hatch:** Every page must have an easy path back to the homepage. Lost users abandon — give them a lifeboat.
- **Navigational model:** Choose hub-and-spoke (homepage as hub) for content sites; step-by-step for checkout/onboarding flows; never fully-connected (every page links to every other page) — it overwhelms.
- **Fat Menus:** For sites with 15+ pages: use a mega-menu with categorised columns, not a flat dropdown. Flat dropdowns fail when categories are mixed.
- **Breadcrumbs:** Required on any page more than 2 levels deep. Format: Home > Category > Page. Current page is not a link.
- **Animated Transition:** Motion must explain spatial relationships. Slide left = go forward; slide right = go back; fade = modal/layer; never animate for decoration.
- **Mobile Vertical Stack:** All mobile layouts default to single-column vertical stack. No side-by-side columns at 375px.
- **Bottom Navigation:** 4-5 items maximum for mobile primary nav. Labels under icons always. Active state must be visually unambiguous.
- **Generous Borders:** All tappable elements minimum 44px height AND 44px width with 8px spacing between adjacent targets. No exceptions.
- **Filmstrip:** Horizontal scrollable rows for browsing collections (services, portfolio, team) — partial next item visible to signal scrollability.

### Task 2.6: Update form-ux-design/SKILL.md

**File to modify:** `form-ux-design/SKILL.md`

The file is exactly 500 lines — check exact line count first. If at the limit, we must add content via concise additions or replacing weaker sections.

**Patterns to add from Tidwell Ch10 (that aren't already covered):**

- **Forgiving Format:** Accept phone numbers with or without spaces, dashes, and country code — normalise on save. Accept dates in multiple formats; detect and normalise. Never reject valid data because of formatting. Show the normalised result after save so users trust it was accepted.
- **Fill-in-the-Blanks:** For very short, simple forms (1-3 fields) consider sentence-style layout: "I am [name] and I want [service] for [budget]." Reduces cognitive distance between question and answer.
- **Autocompletion:** Show suggestions after 2 characters typed; max 8 suggestions; keyboard navigable; dismiss on Escape; never block the field with the list. For addresses: use browser autocomplete (`autocomplete="address-line1"`) before building custom.
- **Good Defaults:** Every field that can have a sensible default should have one. Pre-select the most likely country/region. Pre-fill returning user's known data. "Likely the same as above" patterns for billing = delivery address.
- **Smart Prefills:** If the user is logged in, pre-fill name, email, and phone. Show the pre-filled value greyed with "Edit" affordance rather than an empty field. Removes friction; reduces errors.

### Task 2.7: Commit Phase 2

```bash
cd C:/wamp64/www/website-skills
git add book-extractions/tidwell-navigation-mobile-forms.md
git add page-builder/SKILL.md
git add form-ux-design/SKILL.md
git commit -m "feat: add Tidwell navigation, mobile, form patterns to page-builder + form-ux-design"
```

---

## PHASE 3 — StoryBrand SB7 → brand-storytelling + sales-copywriting + brand-strategy

### Task 3.1: Read StoryBrand Ch4–Ch11 (the full SB7 Framework)

**Files to read:**
- `storybrand.txt` lines 962–3120 (Ch4: Character through Ch11: Transformation)

**Extract the 7 elements of the SB7 framework:**

**SB7 Element 1 — A Character (the Hero)**
- The customer is ALWAYS the hero, not the brand
- Define what the hero WANTS (a single desire, not a list)
- The desire must connect to survival: physical, relational, financial, or self-actualisation
- Avoid positioning the brand as the hero — this repositions the customer as a spectator

**SB7 Element 2 — Has a Problem**
Three levels:
- External problem: the tangible surface problem ("my lawn needs mowing")
- Internal problem: the emotional frustration ("I'm embarrassed by my yard")
- Philosophical problem: the injustice ("a hardworking person deserves a nice home")
- Great marketing names all three; internal problem is most persuasive

**SB7 Element 3 — And Meets a Guide**
The brand is the GUIDE, not the hero. The guide has two things:
- Empathy: "We understand how you feel"
- Authority: proven competence (stats, testimonials, logos, awards)
- Never lead with authority alone — empathy must come first

**SB7 Element 4 — Who Gives Them a Plan**
A plan reduces risk for the customer. Two types:
- Process plan: the steps to do business with you ("1. Call us. 2. Get a quote. 3. Relax.")
- Agreement plan: the values/commitments you stand by ("We never surprise you with hidden fees")
- 3-4 steps maximum; more feels complex and risky

**SB7 Element 5 — And Calls Them to Action**
Two types of CTA:
- Direct CTA: "Buy now" / "Book a call" — transactional, high intent
- Transitional CTA: "Download the guide" / "Watch the demo" — nurtures low-intent visitors
- Every page needs at least one direct CTA and one transitional CTA
- CTAs must be specific: "Get a free quote" not "Learn more"

**SB7 Element 6 — That Helps Them Avoid Failure**
Show the cost of NOT acting. Three stakes types:
- Loss of money / time / opportunity
- Loss of status, respect, or belonging
- Existential threat to goals or identity
- Stakes must be genuine — manufactured urgency destroys trust

**SB7 Element 7 — And Ends in Success**
Show what their life looks like AFTER. Three success types:
- Winning status or respect
- Achieving a goal or transformation
- Emotional resolution (peace of mind, confidence, connection)
- The "after" picture must be vivid and specific; vague aspirations don't convert

**Transformation (Ch11)**
The deepest level: what kind of person does the customer become after engaging your brand?
- Identity transformation is the most powerful motivator
- "You will be the kind of person who..." > any feature or benefit

### Task 3.2: Read StoryBrand Ch12 (Website Implementation) and extract rules

**Files to read:**
- `storybrand.txt` lines 3121–3693 (Ch12: Building a Better Website)

**Extract the website messaging hierarchy:**
1. Header: what you offer + why it makes their life better + how to get it (one sentence each)
2. The stakes: what they risk by not acting (just below the fold)
3. The guide position: empathy statement + authority proof
4. The plan: 3-step process
5. Features/benefits box: positioned AFTER the plan, not before
6. Video if available: "Explain your plan in under 2 minutes"
7. Price: not hidden; integrate logically in flow
8. Junk drawer footer: everything else

### Task 3.3: Read StoryBrand Marketing Roadmap

**Files to read:**
- `storybrand.txt` lines 3694–4500 (The StoryBrand Marketing Roadmap)

**Extract the one-liner formula:**
- We help [ideal customer] avoid [external/internal failure] by [plan summary] so they can [success vision]
- Test: can any team member say this in one breath?

### Task 3.4: Create reference file

**File to create:** `book-extractions/storybrand-sb7-framework.md`

Structure:
```
---
source: Building a StoryBrand (Donald Miller — HarperCollins 2017)
purpose: Reference for brand-storytelling, brand-strategy, and sales-copywriting skills
---

# StoryBrand: The SB7 Framework

## The Core Principle
[extracted content]

## The 7 Elements
[each element with rules and examples]

## BrandScript Template
[fillable template]

## Website Messaging Hierarchy (Ch12)
[8-section structure]

## The One-Liner Formula
[formula + example]
```

### Task 3.5: Update brand-storytelling/SKILL.md

**File to modify:** `brand-storytelling/SKILL.md`

First read to find current line count and insertion point.

**Add a new section "THE SB7 FRAMEWORK (Donald Miller)"** after existing frameworks.

Key rules to add:
- The customer-as-hero principle (most important rule)
- Brand-as-guide positioning with empathy first
- Three levels of problem (external/internal/philosophical)
- The plan as a risk-reducer
- Direct CTA vs transitional CTA taxonomy
- Failure stakes — how to name them without fearmongering
- Success resolution — the "after" picture
- Identity transformation as the deepest motivator
- How SB7 maps to website sections (from Ch12)

### Task 3.6: Update sales-copywriting/SKILL.md

**File to modify:** `sales-copywriting/SKILL.md`

First read to find current line count and insertion point.

**Weave in from StoryBrand:**
- The one-liner formula (We help X avoid Y by Z so they can W)
- Homepage header formula from Ch12
- Stakes copy: how to write the "what happens if you don't act" section
- Guide authority copy: format for testimonials/social proof that positions brand as guide
- CTA copy: direct vs transitional with specific examples

### Task 3.7: Update brand-strategy/SKILL.md

**File to modify:** `brand-strategy/SKILL.md`

**Add a brief BrandScript section** (the SB7 brand canvas) as an output deliverable alongside the brand brief.

BrandScript = one-page document with 7 fields:
1. Hero: [character + desire]
2. Problem: [external / internal / philosophical]
3. Guide: [empathy statement + authority proof]
4. Plan: [3-4 steps]
5. CTA: [direct CTA + transitional CTA]
6. Failure: [what's at stake]
7. Success: [what the after looks like]
8. One-liner: [the 1-sentence company description]

The BrandScript becomes the messaging brief for page-builder and sales-copywriting.

### Task 3.8: Commit Phase 3

```bash
cd C:/wamp64/www/website-skills
git add book-extractions/storybrand-sb7-framework.md
git add brand-storytelling/SKILL.md
git add sales-copywriting/SKILL.md
git add brand-strategy/SKILL.md
git commit -m "feat: add StoryBrand SB7 framework to brand-storytelling, sales-copywriting, brand-strategy"
```

---

## Post-implementation: Clean up temp files

```bash
cd C:/wamp64/www/website-skills
rm tidwell-designing-interfaces.txt
rm storybrand.txt
```

These temp files were created for extraction only — do NOT commit them.
