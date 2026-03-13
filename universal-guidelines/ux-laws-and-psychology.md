---
title: UX Laws & Psychology Reference
description: The psychological principles behind every design decision — apply these on every website build
source: Conrad Bohnke, "From Zero to UI/UX Hero" (2024) + Nielsen Norman Group research
---

# UX Laws & Psychology Reference

Apply these principles when making layout, navigation, CTA, and interaction decisions. They are not optional nice-to-knows — they are the science behind what makes websites work.

---

## The Core Laws (Quick Reference)

| Law | Core Principle | Apply It Like This |
|-----|---------------|--------------------|
| **Miller's Law** | Working memory holds ~7 items (±2) | Limit nav items, form fields, pricing tiers to ≤7 |
| **Jakob's Law** | Users expect your site to work like sites they already know | Follow familiar patterns — logo top-left, nav top, hamburger on mobile |
| **Hick's Law** | More choices = slower decisions = more abandonment | Cut options. Highlight the recommended one. Use progressive disclosure. |
| **Law of Proximity** | Close = related. Apart = distinct. | Group related nav items, form fields, and features together |
| **Fitts's Law** | Larger, closer targets = faster interaction | Make primary CTAs large. Keep them near where the finger already is. |
| **Weber's Law** | Change must be noticeable but not jarring | Change designs gradually — give users time to adapt |
| **Aesthetic-Usability Effect** | Beautiful = perceived as more usable and trustworthy | Invest in visual quality. A polished site is forgiven for minor UX issues. |
| **Endowed Progress Effect** | Head start = more completion | Pre-fill one form step. Start progress bars at 20%. Give a bonus first point. |
| **Von Restorff Effect** | Distinctive items are remembered. Blended items are not. | CTAs must look like nothing else on the page. One standout. Not five. |
| **Zeigarnik Effect** | Incomplete tasks are remembered | Use progress indicators, profile completion meters, partial reveals |
| **F-Pattern** | Users scan online content in an F-shape | Most important words go at the start of lines and paragraphs |
| **Inverted Pyramid** | Most critical info first, then detail, then background | Structure every page, section, and paragraph this way |

---

## Cognitive Load Theory (Sweller)

Three types of cognitive load exist in every design:

- **Intrinsic Load** — the inherent complexity of the content itself (you can't always reduce this)
- **Extraneous Load** — complexity caused by poor presentation (bad design increases this — your fault)
- **Germane Load** — productive mental effort that builds understanding (good design maximises this)

**Your job:** Reduce intrinsic and extraneous load. Increase germane load.

**How to reduce extraneous load:**
- Chunk information into small, digestible pieces (never more than 3–4 ideas per section)
- Signpost: make the next step obvious at every point in the page
- Group similar options together; use collapsible menus for non-essential options
- Use imagery to explain complex options (show, don't just tell)
- Stick to familiar patterns (see Jakob's Law)

**When content is complex, simplify the design proportionally.** Complex topics consume cognitive capacity, leaving less ability to process design elements. Fewer colours, fewer visual highlights, shorter paragraphs, more whitespace.

---

## Don Norman's Action Cycle

Every user interaction has 7 stages. Design must support all of them or the interaction fails.

**Execution Phase:**
1. Forming the Goal — what does the user want to achieve?
2. Forming the Intention — deciding on a course of action
3. Specifying an Action — working out the exact steps
4. Executing the Action — doing it

**Evaluation Phase:**
5. Perceiving the System State — looking for feedback
6. Interpreting the System State — understanding the feedback
7. Evaluating the Outcome — did it work?

**At every stage, ask:** Are you helping the user move forward, or creating a barrier?

The most common failure points: Step 3 (the button isn't clear) and Step 5–6 (no feedback after clicking).

---

## Flow Theory — The Engagement State

Flow = the state of total involvement where the user loses track of time and converts naturally.

> *"Flow is the space between boredom and anxiety."*

- Too easy → boredom → the user feels nothing and leaves
- Too hard → anxiety/frustration → the user gives up and leaves
- Sweet spot → deep engagement → conversion

**Designing for flow:**
1. **Clear goals**: every page, button, and form field has an obvious purpose
2. **Immediate feedback**: confirm every action (Added to Cart, Form Submitted, Message Sent)
3. **Balance challenge and skill**: use progressive disclosure for complex interfaces
4. **Minimise distractions**: no auto-playing media, no intrusive pop-ups, no competing CTAs
5. **Give users control**: interactive tools, preference settings, self-paced journeys
6. **Seamless transitions**: each step leads logically to the next — no dead ends

---

## The Aesthetic-Usability Effect

Users perceive aesthetically pleasing designs as more usable — even when both versions have identical functionality.

1. A beautiful design is believed to work better
2. Users tolerate minor usability issues when the design looks good
3. **Warning:** Beauty can mask serious broken UX. Don't let aesthetics hide dysfunction.
4. The goal is both: beautiful AND functional

**Practical implication:** Budget time for visual polish. A site that looks cheap or unfinished signals untrustworthiness before the user has read a word.

---

## Prospect-Refuge Theory (Digital Safety)

Humans prefer environments that offer both freedom to explore (prospect) and a sense of safety (refuge). This applies directly to website design.

**Prospect design elements** (freedom to explore):
- Clear, open layout with obvious navigation paths
- Logical page structure — users always know where they are
- Uncluttered design — room to move and discover

**Refuge design elements** (safety and control):
- Personal account pages, privacy settings, clear data security indicators
- Explicit privacy policy and contact information
- No dark patterns — no hidden charges, no forced subscriptions

**In e-commerce specifically:** Users need to feel confident about data security (refuge) while enjoying the browsing experience (prospect). Place security seals near payment fields, not buried in the footer.

---

## Persuasion Principles (Cialdini, Applied Ethically)

These principles guide users toward genuinely beneficial actions. They are not manipulation — they work because they match how humans naturally make decisions.

1. **Reciprocity** — give value first. Free tool, checklist, guide, insight. Users who receive value are more willing to act.
2. **Commitment & Consistency** — small commitments lead to larger ones. Get a micro-yes before the big ask. Pre-check one onboarding step.
3. **Social Proof** — testimonials, ratings, user counts, case studies. If others are doing it, new users follow. Distribute throughout the page, not just in one testimonials section.
4. **Scarcity** — limited availability creates urgency. "Only 2 left." Use honestly — false scarcity destroys trust when discovered.
5. **Authority** — certifications, expert endorsements, trust badges, media logos, industry affiliations. Place near conversion points, not buried in footer.

**Ethics rule:** Persuasion design guides users toward actions that genuinely benefit them. Any technique used to trick users into actions against their interests is manipulation, not persuasion.

---

## Mental Models

Users form beliefs about how a system works based on past experiences with similar systems. Violating a user's mental model causes frustration and abandonment.

**Rules:**
- Don't reinvent the wheel without a clear, justified reason
- Introduce new interaction patterns sparingly — test them with users first
- Study competitors to understand what users are already comfortable with
- When you must change a pattern, give users a transition period (see Weber's Law)

---

## The F-Pattern in Practice

Nielsen Norman Group research: users scan online pages in an F-pattern.
- They read the headline across (first horizontal bar)
- They glance at the first few lines beneath it (second horizontal bar)
- They scan down the left edge of the remaining content (the vertical stroke)
- Reading becomes progressively less thorough as they move down

**Users read only about 20% of text on a webpage.**

**Implication for every page:**
- Place the most important words at the start of each line and paragraph
- Key information must be in the first 2–3 words of every bullet point
- The left edge of your content is the most-scanned area
- Don't bury the point — lead with it

---

## The Inverted Pyramid Structure

Borrowed from journalism. Apply to every page, section, and paragraph:

```
Most critical information (headline, main benefit, answer to the question)
         ↓
Important details (how it works, who it's for, proof)
         ↓
Background context (company story, full explanation, supporting detail)
```

Even if users read only the first sentence, they get the core message.

---

## Law of Proximity — In Detail

Items placed close together are perceived as belonging together. Items placed apart are perceived as distinct.

**Applied to navigation:**
- Group all menu link items together
- Group the language switcher and primary CTA together (both action items) but separate from nav links
- Clear visual distinction between navigation sections and action-oriented elements

**Applied to forms:**
- Group the label with its field (not separated by large gaps)
- Group related fields (first name + last name) together
- Separate field groups with visible whitespace

**Applied to content sections:**
- Related text and its illustration must be close together
- Section heading must be closer to its section content than to the section above
