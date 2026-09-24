# Navigation, Mobile and Form Pattern Rules

Parent skill: [page-builder](../SKILL.md). Read when you build site navigation, the home page, mobile layouts, or any form that stands between a visitor and their goal.

This file is the full pattern reference behind the short "Tidwell Navigation and Mobile Rules" list in `legacy-guidance.md`. Implementation detail for menus lives in `advanced-navigation.md`; touch sizing and keyboard attributes live in `touch-interactions.md`; form error states live in `ui-states.md`.

---

## 1. Navigation

### 1.1 Persistent navigation (every page except focused forms and checkout)

| Element | Rule |
|---|---|
| Site identity (logo) | Top-left, highest in the visual hierarchy, links to the home page. It is also the universal escape hatch. |
| Sections | The primary navigation; mirrors the top level of the information architecture. |
| Utilities | At most four or five in the header (sign in, basket, contact, language); the rest go to the footer. Visually quieter than sections. |
| Search | A plain input with a button labelled "Search". Do not use alternative labels such as "Find" or "Go". |

### 1.2 Page-level wayfinding
- Give every page a prominent name that matches the link the visitor clicked, word for word.
- Highlight the current section and subsection in the navigation. Make the "you are here" marker stronger than feels necessary; a marker that looks loud in the design file is usually just visible on the live page.
- Use breadcrumbs on any site more than two levels deep: Home > Category > Subcategory > Current page. Every item except the last is a link; set the last item in bold and do not link it. Place breadcrumbs at the top of the content.
- Design navigation for every level. Third- and fourth-level pages receive as many visits as top-level pages and must not be left without navigation.
- Use a progress indicator, not breadcrumbs, for linear sequences: "Step 2 of 4: Delivery details", with completed steps clickable for backward movement.

### 1.3 Clear entry points
- Give first-time visitors two to four task-oriented "front doors" on landing pages.
- Label entry points in the words visitors search for, not internal department names.
- Weight entry points visually by importance; keep global and utility navigation smaller than the entry points.

### 1.4 Escape hatches
- Every constrained context (wizard, modal, reduced-navigation landing page, 404, error page) needs a visible route back to a known safe place.
- The 404 and error pages must carry a prominent link to the home page and, where available, search.
- Modal exits: an "X" close control top-right, a click on the backdrop, the Escape key, and an explicit Cancel or Close button. After a successful action, return the visitor to where they were before the modal opened.

### 1.5 Keep distances short
- Prefer a flat structure: more items at the top level, fewer levels of depth.
- Promote high-frequency tasks into global navigation regardless of where they sit in the hierarchy.
- For each page, check whether the most common goal is reachable in two clicks or fewer.
- Put signage at every decision point; no dead ends.
- Remember that click count matters less than certainty. A visitor will happily take several obvious clicks; one ambiguous click costs more. Use this as the tie-breaker when depth and clarity conflict.

### 1.6 Sitemap footer
- Use the two-part pattern: a task-oriented header answers "what can I do now?"; a full sitemap footer answers "what else is here?".
- Include main content categories, about and contact, support, legal pages (privacy, terms) and social links.
- Give the footer a background clearly distinct from the page body.
- Prefer a sitemap footer to hover-dependent fly-out menus for accessibility.

---

## 2. Home page

### 2.1 The three questions
Within a glance, the home page must answer:
1. What is this?
2. What can I do here?
3. Why here rather than somewhere else?

### 2.2 Tagline rules
- Describe what the business does and how it differs; a tagline is not a motto.
- Keep it short, roughly six to eight words.
- Place it next to the site identity.

### 2.3 Starting options
Make three ways in visible without scrolling: search, browse (the main sections or entry points), and a sample of the best content or offer.

The home page is the fixed reference point of the site. It must be one click away from every page.

---

## 3. Mobile

### 3.1 Vertical stack
- Order all content in a single column. Use side-by-side placement only for very short controls whose labels will never be translated or enlarged.
- Put useful content in the first screenful. Do not stack logo, promotion strip and navigation tabs above the content (the "layer cake" fault); remove decorative layers instead.
- Place form labels above inputs to save width.
- Thumbnail-plus-text rows are acceptable; check that they degrade cleanly at 320 px wide.

### 3.2 Touch targets and spacing
- Follow the minimum target sizes in `touch-interactions.md` and leave space between targets.
- Make the whole row of a radio button or checkbox tappable, including its label.
- Assume visitors tap while moving; pad generously, because repeated mis-taps erode trust.

### 3.3 Navigation placement
- Keep the top of the screen for content. Place global navigation at the bottom of the page or in a compact bottom bar.
- Keep a mobile bottom navigation to four to six items.

### 3.4 Touch tools for immersive content
- For video, galleries and full-screen media, hide controls until the visitor taps.
- Show controls as a translucent overlay and hide them again after a few seconds of inactivity.
- Controls inside the overlay still meet the minimum touch-target size.

### 3.5 Strip to essentials
- Design for three mobile intents: "I need this fact now", "I have two minutes to spare", and "Where is this near me?".
- Remove sidebars, pull quotes, secondary promotions, share rows, related-content panels and newsletter pop-ups from the mobile view.
- Treat every extra tap as a risk to completion; remove taps where possible.
- Avoid typing: use taps, prefills, autocomplete and location where the visitor consents.
- Put frequent and urgent features close at hand; everything else may sit a few taps away provided the path is obvious.

### 3.6 Affordance without hover
- Mobile has no hover state; every clickable element must look clickable at rest.
- Flat styling removes cues; signal interactivity through position, formatting, colour and shape together.

### 3.7 Loading on mobile
- Show partial content as it arrives; use skeleton placeholders where content is pending.
- Show progress where the content will appear, not only as a global spinner.
- Serve images sized for the device; never ship desktop images to phones.
- Measure load time on a mid-range device and connection before launch; do not quote abandonment percentages without current evidence.

### 3.8 Mobile hygiene
1. Never disable zoom.
2. Make deep links land on the linked content, not on the home page.
3. If a separate mobile experience exists, always provide a path to the full site.

---

## 4. Forms

### 4.1 Form length
- Treat every field as a cost the visitor pays. Ask: is this needed for the transaction, or only for our database?
- Derive what can be derived. If a postcode yields the town, do not ask for both. If the email address is the username, do not ask for a separate username.
- Remove optional fields entirely when completion matters more than data completeness.

### 4.2 Forgiving format
The system, not the visitor, does the reformatting.

| Field | Accept | Then |
|---|---|---|
| Card number | Spaces, hyphens or no separators | Strip separators; detect the card scheme from the leading digits; never ask the visitor to choose the card type |
| Phone | International format, local format, spaces or hyphens | Detect or default the country code; store in one canonical format |
| Date | Several common orders and written month names | Parse, then echo back in the site's standard format for confirmation |
| Postcode | With or without the internal space, any letter case | Normalise to the canonical format |

Where the input is ambiguous (for example 07/08), echo the interpretation back in words ("7 August") so the visitor can correct it.

### 4.3 Input hints
- Place a short example or format note beside or below the field, visible before the field receives focus; never on hover only.
- Keep hints to one or two short sentences, slightly smaller than the label but readable.
- Leave the field itself empty. Placeholder text is easily mistaken for a filled field and skipped; if a placeholder is used, it is an example only and never the label.
- Localise examples (for instance, a phone example in the local national format).

### 4.4 Good defaults and prefills
- Prefill what the system already knows: signed-in name, email, saved address ("Use the same address as last time?").
- Prefill region or town from a known postcode where reliable.
- Choose defaults that serve the visitor, not the business (for example the plan that fits the stated need, not the most expensive).
- Remember that prefilled fields make a form feel shorter than its field count.

### 4.5 Autocompletion
- Suggest matching valid options as the visitor types (search, towns, product names).
- Match anywhere in the string, not only at the start; highlight the matched characters.
- Show at most five to seven suggestions.
- Support arrow keys and Enter; always allow free text that is not in the list.

### 4.6 Actionable validation
- One message states which field, what is wrong, and how to fix it: "[Field] [problem]: [fix, with example]".
- After a failed submission, keep every entered value; highlight only the invalid fields.
- Move focus to the first invalid field.
- Never clear the form after a failed submission.

### 4.7 Gatekeeper forms
Any form standing between the visitor and their goal (sign-up, checkout, enquiry, booking):
- Present it in centre stage with minimal navigation, or in a focused modal panel.
- Remove site navigation, sidebars, promotional banners and testimonial carousels.
- Keep the logo (trust and escape), a clear form title, a progress indicator for multi-step forms, a privacy reassurance, and a telephone or alternative contact route.

---

## 5. Sign-off checklist

- [ ] Logo top-left and linked home on every page; utilities limited; search labelled "Search".
- [ ] Every page name matches the link that leads to it; current location highlighted.
- [ ] Breadcrumbs on deep pages; step indicators on linear flows.
- [ ] Every constrained page and modal has an escape route.
- [ ] Home page answers the three questions; tagline describes and differentiates.
- [ ] Mobile view is a single column with content in the first screenful and no layer cake.
- [ ] Nothing depends on hover; deep links land on content; zoom enabled.
- [ ] Each form field justified; formats forgiven; hints visible; defaults serve the visitor.
- [ ] Validation keeps data and states field, problem and fix.
- [ ] Gatekeeper forms stripped of distractions but keep trust and contact cues.

## Sources

- Tidwell, J., Brewer, C. and Valencia, A. (2020) *Designing Interfaces*, 3rd edn. O'Reilly Media. Chapters 3 (navigation), 6 (mobile) and 10 (forms and controls).
- Krug, S. (2014) *Don't Make Me Think, Revisited*, 3rd edn. New Riders. Navigation, home page and mobile chapters.
- Companion references in the design engine: `C:/wamp64/www/design-system-skills/skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/` and `C:/wamp64/www/design-system-skills/skills/04-web-and-ui-design/form-ux-design/`.
