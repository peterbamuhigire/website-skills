# UX Discovery and Wireframe Procedure

Parent skill: [premium-ui-ux-design](../SKILL.md). Read when you run the UX discovery meeting for a website, turn its answers into a journey, an information architecture and a sitemap, and produce wireframes that are tested before any visual design starts.

Commercial intake questions and the strategy brief template live in `orchestration/website-builder/references/` (`intake-questionnaire-template.md`, `website-strategy-brief-template.md`). Journey-mapping methods are in `orchestration/website-experience-mapping/`. Persona rules are in `orchestration/website-experience-mapping/references/persona-discipline-and-motivation-rules.md`. This file covers the UX designer's side of the same stage.

---

## 1. Build in order: the five planes

Use Jesse James Garrett's five planes of user experience as the build order. Decide each layer substantially before working on the one above it. Changing a lower layer after the upper ones are built is the most expensive kind of rework.

| Order | Plane | Decisions | Website artefact |
|---|---|---|---|
| 1 | Strategy | Visitor needs and business goals | Discovery notes, measurable objective |
| 2 | Scope | Features, content and functions to include | Content and feature list |
| 3 | Structure | Information architecture and interaction flow | Sitemap, user flows |
| 4 | Skeleton | Placement of navigation, content and controls | Wireframes |
| 5 | Surface | Visual design, imagery, motion, sound | Visual design and design system |

Gate: do not open visual design (plane 5) until planes 1 to 4 are signed off.

---

## 2. The discovery meeting: five questions in order

End the meeting with all five answered in writing.

### 2.1 Business goal
Ask:
- Why has the client come to us now?
- What result do they want?
- What problem are they trying to solve?
- What must be true at the end of the project for it to count as a success?
- Why does this project exist at all?

Clients know their problem but rarely state their objective precisely. Like a dentist whose patient asks for an extraction, listen to the request and then decide the treatment. Examples of real goals: receive enquiry calls, collect email sign-ups, take bookings, sell tickets.

### 2.2 Visitor goal
The business goal is usually rational (make a sale). The visitor's goal is usually emotional (feel competent, impress someone, avoid embarrassment, try something new). Record both. They overlap but are never identical, and the visitor's goal should shape tone and design decisions throughout.

### 2.3 Audience and personas
- **Audience data** (quantitative): from analytics, where the site already exists. Capture age and gender split, device and screen mix, new versus returning visitors, traffic sources (social traffic tends to browse lightly; newsletter and direct traffic tends to be more engaged), common paths and time of day. Visitors at unusual hours may read less and rely more on images and buttons.
- **Personas** (qualitative): build them using the persona rules file. Minimum fields for a website persona: age range, education, work background, technical confidence, why they arrived, how much the information matters and what happens if they fail to find it, where else they could get it, time and context of access, devices, other apps and sites they use, and daily time online.

### 2.4 Competition
A competitor is anything that meets the same need, not only an identical business. A scooter hire service competes with buses, bicycles, taxis and walking. Doing nothing is always a competitor.

Review each significant competitor from three angles:
- **Communication:** tone, what they take for granted, which qualities they stress and why.
- **Audience:** is it the same as ours? How does their buyer differ (for example long, multi-person buying cycles versus quick decisions by small teams)?
- **Business model:** one-off or subscription, price level, and whether our client's position above or below it helps or hurts.

Use `build/design-reference/references/competitor-analysis-worksheet.md` for the detailed record.

### 2.5 Measurable objective
Every discovery meeting ends with one written, measurable objective. Reject vague aims ("get rich", "lots of emails", "look cutting-edge", "make competitors jealous").

Acceptable forms:
- more customers or enquiries than in the previous comparable period;
- more email sign-ups than before;
- longer engaged time on key pages;
- fewer support requests or product returns;
- more positive unsolicited feedback.

UX work is judged on whether the agreed number moved, not on whether the client likes the colours.

---

## 3. The decision journey

### 3.1 Exploration and evaluation
Before buying, people move back and forth between two modes many times:
- **Exploration:** widening the set of options (asking friends, searching, reading).
- **Evaluation:** narrowing the set (comparing features and proof against their goal).

Three consequences:
1. The experience starts before the website, through word of mouth, forums, comparison tools and earlier contact with the brand. One site has limited short-term influence.
2. Visitors do not know every alternative. Be present where they already search (search engines, marketplaces, social platforms).
3. In evaluation, visitors want objective facts. Replace vague claims ("market leader") with verifiable specifics (a customer count, a named certification), and check any figure before stating it.

### 3.2 Journey matrix
Map the path from "need arises" to "action taken" as a grid.

| | Exploration | Evaluation | Decision | After decision | After the experience |
|---|---|---|---|---|---|
| Actions and where they happen | | | | | |
| Thoughts (what they say to themselves) | | | | | |
| Feelings | | | | | |
| Opportunities for us | | | | | |

- **After decision:** a small effort confirms the choice was right. Thank them, confirm what happens next, give a contact route for problems.
- **After the experience:** re-engage with something of value that keeps the brand present and prepares the next purchase.

Rule drawn from the journey: every element on every page either moves the visitor to the next step or is removed. When a visitor starts to find their own way instead of following the path, the business has lost them.

---

## 4. Information architecture: three questions

1. **How is the content organised?** Rank each piece of content by priority, reconcile what the client wants included with what visitors look for, and order it to follow the visitor's reasoning. A bookshop places new and featured titles at the entrance for browsers, then genres, then alphabetical order within each genre; websites work the same way.
2. **What is each item called?** Use the terms visitors expect, not internal jargon, for menu items, categories and tags. Present attributes in the order visitors ask about them (for a property: price, rooms, floor area, bathrooms, floor).
3. **Which navigation?** Which menu items matter to the visitor, where the menu sits, and whether free-text search is needed (and why or why not).

The answers produce the sitemap.

---

## 5. Sitemap

A sitemap shows each page as a block and each navigation route as an arrow. Build one for every project to:
- understand the true size and complexity of the job;
- make sure every section is known and controlled;
- estimate design and development effort;
- give the client a visual overview and confirm exactly which pages are in scope.

Use `orchestration/website-experience-mapping/references/map-to-sitemap-conversion.md` to derive pages from journey stages.

---

## 6. Wireframes

A wireframe is the skeleton of a page: where things go and in what priority. It is not the design.

**Rules**
- Leave out brand colours, photographs, typefaces and the logo. Judging appearance at this stage derails structural thinking.
- Draw only structural blocks: image placeholder, text block, columns, title, video.

**Three questions each wireframe must answer**
1. How does the visitor move within and between pages? What is clickable, what happens on click, and what changes on tablet and phone?
2. How is information grouped? How many columns; is there a main column; does a sidebar follow the scroll; how are results told apart from main content, titles from subtitles, and links from text?
3. In what priority is information shown? What is the main content; how important is the title; when should the call to action appear, and what must the visitor have read before clicking it?

**Three rules for better wireframes**
1. **Start from the journey.** Decide which mode the arriving visitor is in. Exploration pages widen options and inspire (featured items, categories, search). Evaluation pages give features, proof and reasons to proceed.
2. **Keep the business goal visible.** Show it as a clear action on every relevant page. Give each page one objective; competing objectives confuse. On phones be stricter still: one call to action per screen.
3. **Validate before presenting.** Show wireframes to colleagues and to representative visitors before the client sees them. Simulate navigation on paper or screen, ask people to think aloud, and record their difficulties. Run the trunk test in `build/page-builder/references/scan-first-page-and-goodwill-rules.md`.

**Getting started: study before drawing.** Review at least ten well-regarded sites in the same category. For each page ask: what am I looking for here, what am I thinking, and why is this element placed here? Page patterns for exploration sites, evaluation sites and acquisition pages are in `build/page-builder/references/component-design-rules.md` ("SITE PATTERN LIBRARY").

**Wireframe checklist**
- [ ] One objective per page.
- [ ] Visitor mode (exploration or evaluation) decided for each page.
- [ ] Call to action visible, with enough supporting content before it to justify the click.
- [ ] Every element moves the visitor forward.
- [ ] Trunk test passed.

---

## 7. Match the visitor's mental model

- **Implementation model:** the interface mirrors how the system works internally. Logical to the builder, awkward for the visitor.
- **Mental model:** how the visitor thinks the task works, usually simpler and more intuitive.
- **Represented model:** what is actually built. The closer it sits to the mental model, the easier the site feels.

Examples of closing the gap:
- Offer date choices the way people plan ("today", "this weekend", "this month") alongside the full calendar.
- Accept equivalent terms visitors treat as the same (a city name or its airport code; a town or its district).
- Pre-select the options most visitors choose, provided they serve the visitor (see the defaults rules in `build/page-builder/references/navigation-mobile-and-form-pattern-rules.md`).
- Split a complex task into a step-by-step wizard when that follows how people think the task through, even if the system does not need the steps.

Ask of every screen: how would this visitor think about this?

---

## 8. Keep research ahead of design

**Do not design on instinct.** "Meeting user needs" is vague enough to excuse guesswork. Base decisions on discovery, personas, journeys and observed behaviour.

**A recurring failure.** A UX specialist is brought in a quarter of the way through a project and asked for screen designs. There is no task analysis, no contextual research and no usage scenarios, only requirement lists. Scenarios are reverse-engineered from the requirements, and the first time real users see the system is at delivery. They reject it ("That is not how we work"), and the project either goes back for costly rework or ships something nobody uses.

Rule: start iterating with real users early, before requirements and scope are frozen. Late iteration is not a substitute.

**Three lenses for every design review.** Check each concept from three angles:
- **Environment:** how the site fits the visitor's wider context, habits and social setting over time.
- **Interaction:** how the visitor operates it; the displays, controls and actions where person and site meet.
- **Emotion:** how it feels, what it says socially, and whether it gives pleasure in use.

**Earn trust.** Do what the site promises, do not over-promise, and never trade the visitor's interest for a business target. Make actions reversible wherever possible; undo is among the most reassuring controls a visitor can have.

---

## 9. Testing cadence and method choice

**Test early, test often, test cheaply.** Arguments about what visitors like waste time; watching visitors reveals what works. A small round of sessions with a few representative people, repeated regularly (for example monthly), finds most serious problems. Rough testing beats no testing.

Test at every stage: before design (on the current site and on competitors), on sketches, on wireframes, on prototypes and on live pages.

**Behaviour, not opinion.** Focus groups reveal attitudes and expectations; usability tests reveal behaviour. Do not use a focus group to answer a usability question.

**Toolbox**

| Tool | Purpose |
|---|---|
| Personas | Keep real visitor goals in view |
| Journey maps | Show what visitors do, think and feel end to end |
| Flowcharts | Map every path, decision and error route exactly |
| Wireframes | Fix structure at low to medium fidelity |
| Prototypes | Test concepts early (low fidelity) and refine them later (high fidelity) |

**Method selector**

| Method | Answers | Notes |
|---|---|---|
| Field study | Visitor goals, context and mental models | Exploratory; small sample |
| Usability test | Where a specific flow causes friction | A handful of participants per round; repeat after fixes |
| Rapid iterative testing | Fix-and-retest as you go | Change the design between participants |
| Think-aloud | How people perceive and interpret the screen | Often combined with usability tests |
| Heuristic evaluation | Early expert review without users | Several reviewers; never a replacement for users |
| Survey | Attitudes and demographics at scale | Weak on behaviour |
| Focus group | Needs, frustrations, expectations | Hard to run well; not for usability questions |
| Analytics | What people do and where they drop off | Never says why; pair with observation |

Detailed protocols are in `orchestration/website-experience-mapping/references/validation-research-method-playbook.md`.

---

## Sources

- Panzarella, L. (2022) *UI & UX Web Design Simply Explained*. Part 1 (UX design).
- Branson, S. (2020) *UX / UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*. Chapters on design perspectives, process and credibility.
- Hodent, C. (2022) *What UX Is Really About: Introducing a Mindset for Great Experiences*. CRC Press. Sections on the five planes, the UX toolbox and research methods.
- Krug, S. (2014) *Don't Make Me Think, Revisited*, 3rd edn. New Riders. Chapter on usability testing.
