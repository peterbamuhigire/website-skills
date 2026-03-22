---
name: ux-psychology
description: Cognitive psychology for premium web design. Gestalt principles, Nielsen's 10 heuristics, Norman's 3 design levels, System 1/2 thinking with cognitive biases, emotional design, dark patterns to avoid, and affordance principles. Use for premium $20k+ websites to justify quality and prevent common psychological UX mistakes.
---

# UX Psychology

Cognitive psychology and behavioural science applied to premium website design. Complements `universal-guidelines/ux-laws-and-psychology.md` (which covers Miller's Law, Hick's Law, Fitts's Law, Gestalt proximity/similarity overview, Cognitive Load Theory, Flow Theory, etc.). This skill covers the principles not in that file.

---

## 1. GESTALT PRINCIPLES

Perception rules that determine how users group, separate, and interpret visual elements.

### Law of Proximity
Elements close together are perceived as belonging together — no borders required.

- Image caption: gap between image and caption must be smaller than gap between caption and next paragraph. Equal spacing breaks the perceptual link.
- Navigation items grouped tightly = perceived as a single unit. Increase spacing between nav groups (e.g., primary links vs. utility links) to signal categories.
- Form question spacing: increase vertical gap between separate questions; keep label and its input tight. Space alone signals question boundaries — no box borders needed.
- Use whitespace (not dividers) to group related content in most layouts; dividers add visual noise.

### Law of Similarity
Elements sharing visual traits are perceived as the same category.

- ALL interactive elements (buttons, links, toggles) must share ONE consistent visual treatment per type.
- Decorative elements must NEVER use the same treatment as interactive elements — no hover states, underlines, or button-like styling on non-interactive components.
- Same font weight + colour + size = same type of content. Violating this forces users to re-learn the visual grammar on every page.
- If a card has a shadow and a hover state, every card must — inconsistency breaks the similarity rule.

### Law of Continuity
The eye follows lines and curves beyond their endpoints.

- Use alignment to guide the eye toward the next important element: hero headline → subheadline → CTA button must lie on a clean vertical or diagonal axis.
- Visual flow interrupted by unaligned elements = cognitive stumble. Audit every page for broken alignment paths.
- Horizontal rules and divider lines extend into visual infinity — place them intentionally or they will guide the eye off-page.

### Law of Closure
The brain fills in incomplete shapes and implies the rest.

- Partially revealed cards or carousel items at the right edge signal "scroll to see more" — use deliberately and consistently. Showing 80% of a card communicates the rest without labels.
- Do not rely on arrows or "swipe" labels when partial visibility already communicates scrollability.
- Incomplete circles and icons are resolved by the brain — minimalist iconography exploits this; overly detailed icons do not.

### Law of Figure/Ground
Users distinguish foreground content from background by contrast. If the contrast is insufficient, neither reads as primary.

- Modal overlays: backdrop opacity 70–80% (not 30–40%). Low opacity creates figure/ground confusion — the page behind competes with the modal.
- Cards need visible separation from the page background: shadow, border, or colour contrast. Cards that match the page background become invisible as distinct objects.
- Background textures and images behind text must be low-contrast or blurred — they must read unambiguously as ground.

### Gestalt Violations to Eliminate
- Equal spacing above and below an image caption = caption belongs to neither image nor paragraph.
- Decorative graphic styled with a shadow and hover state = users attempt to click it (false affordance).
- Same blue colour for external links AND decorative section headers = users click headers expecting navigation.
- Section with a drop shadow that is not a clickable card = violates the learned affordance of shadows.

---

## 2. NIELSEN'S 10 USABILITY HEURISTICS

Each heuristic with specific, implementable rules.

### H1: Visibility of System Status
Users need to know what is happening at all times.

- Show skeleton screens or loading spinners whenever content loads asynchronously — never a blank space.
- After form submission: show a clear confirmation message (not a blank or unchanged page).
- Submit buttons must change state on press: disabled + spinner while processing; success state on completion.
- Never leave users wondering if their action registered. If processing takes >1s, show progress.

### H2: Match System to Real World
Use the words and mental models of users, not internal technical terminology.

- "Shopping cart" not "order queue." "Inbox" not "message buffer." "Sign in" not "authenticate."
- Error messages in plain language: "That email address is already registered — try logging in instead" not "UNIQUE constraint violation on field: email."
- Navigation labels must use words users search for, not your client's internal category names.
- Date pickers, currency fields, and phone fields must match regional formats (DD/MM/YYYY not MM-DD-YYYY for UK/African markets).

### H3: User Control and Freedom
Users make mistakes; they need safe exits.

- Always provide "Back" or "Cancel" in multi-step flows. Never trap users mid-funnel with no retreat.
- Allow modal exits by clicking the backdrop AND pressing Escape — both, always.
- Destructive actions (delete, cancel subscription) require a confirmation dialog. Provide explicit Confirm AND Cancel with visual distinction.
- "Undo" functionality or a grace period (e.g., "Email will be sent in 5 seconds — Cancel") reduces anxiety and errors.

### H4: Consistency and Standards
Users transfer learned expectations. Violating consistency forces relearning.

- One word per concept: "sign in" OR "log in" — never both on the same site.
- Navigation position must not change between pages. A navigation that moves is a navigation that loses trust.
- Same button style = same action type, everywhere. Primary CTA: one colour. Secondary actions: a different treatment. Destructive actions: always red. Never deviate.
- Icons must be consistent: one icon per concept; one style library (never mix filled and outline variants of the same icon).

### H5: Error Prevention
The best error message is one that never needs to appear.

- Inline validation after the user leaves a field (on blur), not only on submit.
- Show confirmation dialogs before irreversible actions — "Are you sure? This cannot be undone."
- Disable the submit button until required fields are complete (with a visible tooltip explaining why it is disabled).
- Password fields: show requirements upfront, not after the user fails.
- Provide format examples inside form labels: "Phone (e.g., +256 700 000 000)."

### H6: Recognition Rather Than Recall
Never make users remember something from a previous screen.

- Navigation labels must always be visible text on desktop — icon-only navigation requires recall, not recognition.
- Show users their position in multi-step flows: "Step 2 of 4 — Shipping Details."
- Breadcrumbs on pages more than 2 levels deep.
- Never ask users for information they already provided (e.g., ask for name once; pre-fill it if shown again).
- "Recently viewed" or saved items reduce recall load for returning users.

### H7: Flexibility and Efficiency of Use
Novices and experts need different interfaces; serve both.

- Keyboard navigation for all interactive elements (Tab order, Enter to submit, Escape to close).
- Saved preferences and persistent filters for returning users.
- Quick-fill patterns for returning visitors (saved addresses, auto-populated fields).
- Shortcuts and power-user paths should not clutter the interface for novice users — layer them.

### H8: Aesthetic and Minimalist Design
Every element that is not essential is a competitor to the essential.

- One primary message per page. Establish hierarchy, then enforce it ruthlessly.
- One primary CTA per page — five equal-weight CTAs create decision paralysis (see Hick's Law in universal-guidelines).
- Every optional form field is a cognitive tax. Eliminate it or mark it clearly optional.
- No decorative text that does not serve the user's current task. Filler copy is not neutral — it buries signal in noise.
- Remove features until removing one more would break the minimum viable flow.

### H9: Help Users Recover from Errors
When errors happen, minimise damage and frustration.

- Error messages appear inline next to the offending field, not as a list at the top of the page.
- Error message format: [What went wrong] + [What to do]: "Password too short — must be at least 8 characters."
- NEVER clear a form after a failed submission. Repopulate all valid fields; highlight only the invalid ones.
- Offer alternatives in dead-ends: if no search results, suggest related content or a contact path.

### H10: Help and Documentation
When users need help, make it immediately findable and actionable.

- Contextual help at the point of need (inline tooltip, help icon next to the field) — not a separate help centre link.
- Help content must be task-oriented and specific: "Click the blue 'Add Service' button in the top-right corner" not "Services can be added in the admin panel."
- FAQ sections must be structured around user questions, not product features.

---

## 3. NORMAN'S THREE LEVELS OF DESIGN

Apply all three simultaneously. Failure at any level loses the user.

### Visceral Level — Automatic Emotional Response to Appearance
- First impressions form in under 100ms. Visual quality is not superficial — it is the first interaction.
- The Aesthetic-Usability Effect: beautiful interfaces are perceived as more usable, more trustworthy, and worth paying more for — even if the underlying UX is marginally inferior to an ugly competitor.
- This is what clients at the $20k–$50k level are paying for: a visceral experience their competitors cannot afford.
- Practical inputs to visceral quality: photography resolution and mood, whitespace generosity, typographic refinement, colour harmony, and animation smoothness.
- Visceral quality communicates "this business is serious" before a word is read.

### Behavioral Level — Usability: Does It Work?
- This is where Nielsen's heuristics and the UX laws in universal-guidelines operate.
- Frictionless task completion: the user achieves their primary goal (contact, purchase, enquiry) without confusion, dead-ends, or errors.
- If the behavioral level fails, no amount of visceral quality can rescue the site. Users leave frustrated regardless of how beautiful it was.
- Every page has one primary user task. Design the behavioral path for that task first; everything else is secondary.

### Reflective Level — Values, Identity, and Self-Image
- Users ask implicitly: "What does using this site say about me?"
- Brand consistency, ethical practices, and authentic voice all affect reflective assessment.
- Testimonials, case studies, and trust signals operate at this level — they provide social proof for the reflective judgement ("people like me trust this brand").
- Content that aligns with the user's values creates reflective-level loyalty: users return and refer others because the brand reflects who they are or aspire to be.
- Dark patterns destroy reflective-level trust irreversibly: once a user feels manipulated, no visceral quality recovers it.

### The 3-Level Audit for Any Page
1. **Visceral:** Does the design create an immediate positive emotional response?
2. **Behavioral:** Can users accomplish their goals efficiently and without confusion?
3. **Reflective:** Does the experience reinforce the client's values and the user's sense of self?

---

## 4. SYSTEM 1 vs SYSTEM 2 THINKING

Kahneman's dual-process model. Every website interaction is primarily System 1.

**System 1** — fast, automatic, pattern-matching, intuitive. Runs almost all the time.
**System 2** — slow, deliberate, effortful, analytical. Users resist switching to it.

**Design for System 1:**
- If users must think hard to use your interface, it has failed at the behavioural level.
- Use familiar patterns: novel interactions are interesting in demos and costly in production. Novelty forces System 2; familiarity enables System 1.
- Defaults are accepted by System 1 without scrutiny — set defaults that genuinely serve users.
- Familiar layouts (nav at top, logo left, CTA top-right) exploit learned patterns and reduce cognitive load.

### 10 Cognitive Biases with Direct Website Application

**1. Loss Aversion** — the pain of loss is twice as powerful as equivalent gain.
- Ethical use: "Your progress will be lost if you leave now" (when genuinely true).
- Dark pattern: fabricated scarcity ("Only 2 left!" when inventory is unlimited).

**2. Default / Status Quo Bias** — users keep defaults unless strongly motivated to change.
- Set defaults that serve users: opt-IN for marketing emails, most privacy-preserving data settings on by default.
- Dark pattern: pre-checked upsell boxes, auto-enrolled subscriptions, opt-out (not opt-in) recurring charges.

**3. Egocentric Bias** — we assume others experience the world as we do.
- "I find it intuitive" does not mean "it is intuitive." You are not your user.
- The solution is structured user testing with people who have never seen the site.

**4. Goal-Gradient Effect** — motivation increases as a goal approaches completion.
- Ethical use: progress bars in onboarding flows, "3 steps remaining," pre-filling Step 1 so users feel started.
- Dark pattern: streaks that reset to zero if one day is missed (designed to create anxiety, not progress).

**5. FOMO — Fear of Missing Out**
- Ethical use: honest limited-time sales with real deadlines; genuine low-stock notifications.
- Dark pattern: countdown timers that reset on page reload; "14 people viewing this now" with fake or inflated numbers.

**6. Confirmation Bias** — we seek information that confirms existing beliefs.
- The team that built the product cannot conduct unbiased usability tests. Independent user testing is not optional.
- Analytics that confirm your design choices should be scrutinised harder, not accepted more easily.

**7. Curse of Knowledge** — once you know something, you cannot simulate not knowing it.
- Test with people who have NEVER seen the site. They will immediately find the problems you are blind to.
- Never assume that a label, icon, or interaction is "obvious" — test before shipping.

**8. IKEA Effect** — we overvalue things we helped create.
- Product teams keep too many features. Use click analytics and completion rates, not team attachment, to decide what stays.
- Every unnecessary feature you ship imposes cognitive load on every user, forever.

**9. Sunk Cost Fallacy** — we continue investing because of past investment, not future value.
- If a page is not converting, rebuild it. The willingness to discard sunk work is a premium design quality indicator.
- Client expectation management: "We are rebuilding this section because the data shows it is failing" is a professional, not a failure, conversation.

**10. Anchoring** — the first number or option seen biases all subsequent judgements.
- Present the premium tier first in pricing tables. Anchor high; let users "choose down."
- In services lists, lead with the most comprehensive (and expensive) option.

---

## 5. EMOTIONAL DESIGN AND MICROINTERACTIONS

### Emotional Feedback Rules
- **Success states** deserve active celebration: positive colour change, motion, and human language when important tasks complete. "You're in! Check your inbox" not "Form submitted."
- **Error states** deserve empathy: acknowledge the frustration first, then give a clear path forward. "Something went wrong on our end — please try again or contact us directly."
- **Surprise and delight** moments (small unexpected positive touches) increase brand affinity without adding clutter. An animated tick after form submission; a warm thank-you page that sets expectations.
- Custom 404 pages with empathy and helpful next steps turn a negative moment into a brand touch: "We can't find that page, but here's where to go next."
- Onboarding copy should feel welcoming, not like a compliance exercise. Every instruction should feel like a helpful colleague, not a legal disclaimer.
- Write all system copy (confirmations, errors, empty states) in the same human voice as the marketing copy.

### Microinteraction Design Rules
- Button hover and press states communicate that the interface is alive and responsive. Absence of state changes communicates brokenness.
- Loading animations should feel purposeful and brand-consistent — not a generic grey spinner.
- Form field focus states (ring highlight) help users track their position, especially on mobile.
- Transition timing: 150–300ms for small UI feedback (hover, focus, button press); 300–500ms for larger state changes (modal open, panel slide); 500ms+ only for deliberate emphasis.
- Never animate purely for decoration. Every animation must help users understand a state change or spatial relationship.
- Reduced motion media query: always respect `prefers-reduced-motion`. Provide static fallbacks.

---

## 6. AFFORDANCES AND MENTAL MODELS

### Mental Models
Users bring expectations from other websites and from real-world objects. Designing against the dominant mental model is always wrong.

- If users predictably misuse a feature, the feature needs redesigning — not the user manual.
- The thermostat fallacy: users believe turning a thermostat to maximum heats a room faster; users believe more button clicks = faster processing. Design to correct these where it matters.
- Use onboarding to establish accurate mental models for genuinely novel interactions. For conventional interactions, exploit existing mental models — do not fight them.

### Four Types of Affordance

| Type | Definition | Web Application |
|------|-----------|----------------|
| Physical | Shape/size suggests interaction | Scrollbar thumb size implies drag; pill input implies typing |
| Cognitive (signifier) | Label/icon explains the action | Button text states the outcome; envelope icon = messaging |
| Sensory | Visual prominence signals importance | High-contrast CTA is visually "grabbable"; large font = important |
| Functional | Structure implies capability | Filter + sort tools signal that large content is navigable |

### False Affordances (Design Errors)
- Decorative card with a box shadow and hover state = users click expecting a link. If it has hover, it must link.
- Section heading styled to resemble a button = users attempt to click it.
- Segmented control with unclear active state = users cannot tell what is selected.
- Underlined text that is not a hyperlink = violates one of the most established web conventions.
- **Rule:** If it looks interactive, it must be interactive. If it is decorative, it must not look interactive.

### Mental Model Alignment Rules
- Navigation at page top: where users look first (Jakob's Law — covered in universal-guidelines).
- Search = magnifying glass icon. Always. No exceptions.
- Home = logo in top-left. Always.
- Close/dismiss = × in top-right corner. Always.
- Back = left-pointing arrow. Always.
- Never place the primary action in a non-standard location without a compelling, tested reason.

---

## 7. DARK PATTERNS TO AVOID

Premium clients pay to protect their brand. Dark patterns create legal risk and destroy the trust their brand depends on.

**Confirm-shaming:** Opt-out labels that guilt-trip users: "No thanks, I don't want to save money." Never use. Write neutral cancel options: "No thanks" or "Maybe later."

**Pre-checked boxes:** Always require explicit, deliberate opt-in for: marketing emails, upsells, add-on products, subscriptions, recurring charges. Pre-checked = assumed consent = legal risk in GDPR jurisdictions.

**Hidden subscription:** "GET STARTED FREE" that initiates a paid subscription without making the billing terms prominent and explicit. Fatal to trust; increasingly illegal.

**Fake scarcity / urgency:** "Only 2 left!" when inventory is unlimited; countdown timers that reset on page reload; "17 people are viewing this right now" with fabricated or inflated numbers. Users have seen these; they destroy credibility.

**Auto-play media:** Removes the user's decision to engage. Default-off for all audio and video. No exceptions.

**Roach motel:** Easy to sign up; nearly impossible to cancel, unsubscribe, or delete account. The cancellation path must be as accessible as the sign-up path.

**Bait and switch:** Advertising one product, price, or feature; delivering another. Especially common in pricing pages where the most prominent plan has asterisked exclusions.

**Misdirection:** Drawing attention to one area to prevent users from noticing another — e.g., a bold promotional graphic positioned to draw the eye away from a pre-checked upsell box beneath it.

**Disguised advertising:** Sponsored content or affiliate recommendations styled to look identical to editorial content without disclosure.

### The Ethical Test
For every design decision that could be a dark pattern, ask: **Will this feature be genuinely valuable to users, or is it primarily serving a business metric at users' expense?**

If the answer is "primarily at users' expense," it is a dark pattern — regardless of whether it temporarily improves a conversion metric.

### The Premium Client Standard
Clients investing $20k–$50k in a website are buying brand equity. One viral complaint about a dark pattern destroys months of that equity. When a client requests a dark pattern, name it clearly and recommend the ethical alternative. This is part of the expertise they are paying for.

---

## 8. TIDWELL BEHAVIORAL PATTERNS

Patterns from *Designing Interfaces* (Tidwell, Brewer, Valencia — O'Reilly 2020). Full pattern details in `book-extractions/tidwell-cognition-visual-patterns.md`.

### Safe Exploration — "Let me explore without getting into trouble."
- Every destructive action must be reversible or require confirmation.
- Auto-save so exploration costs nothing; any wrong turn is recoverable.
- Extra windows, pop-ups that hijack Back, or irreversible single-clicks break this pattern.

### Instant Gratification — "I want to accomplish something now."
- Predict the first thing a new user will do; make that action stunningly easy.
- Do NOT block first action behind registration, long instructions, or slow loads.
- Provide value before asking for something valuable (email, payment).
- Show partial results as they load — blank screen for >200ms damages confidence.

### Satisficing — "This is good enough; I'll stop here."
- Users stop at the first plausible choice — put the right choice FIRST in every list.
- Labels must be short and scannable; users guess rather than read every word.
- Use calls to action ("Type here," "Tap to begin") to direct users to the most likely first step.
- Visual layout communicates meaning faster than labels — use it to guide first-click behaviour.

### Deferred Choices — "I don't want to answer that now."
- Clearly distinguish required vs. optional fields — never make non-critical fields required.
- Use good defaults so skipped fields don't create broken states.
- A note like "You can change this later in Settings" reduces the anxiety of deciding now.

### Habituation — "That gesture works everywhere else; why not here?"
- Consistent placement of navigation, actions, and labels is the most critical usability rule.
- After first use, help text becomes invisible — layout must self-explain to returning users.
- Announce layout changes explicitly: "We've updated our navigation" prevents disorientation.

### Spatial Memory — "I remember where things were on the screen."
- NEVER move navigation items between pages — users remember locations, not labels.
- Pin primary actions to consistent screen positions (top-right on desktop, bottom on mobile).
- If layout must change (responsive breakpoint), animate the transition so users can follow elements.

### Prospective Memory — "Remind me where I was."
- Breadcrumbs, progress steps, and section titles remind users of their position.
- After any page load, visible context must make the current task obvious without reading body text.
- Email/notification reminders for deferred actions reduce abandonment.

### Incremental Construction — "Let me change this. That's better."
- Support frequent small saves; never require a complete form before any save is possible.
- Show work-in-progress continuously; feedback during creation is essential (Csikszentmihalyi).

---

## SKILL INTEGRATION NOTES

- Run **alongside** universal-guidelines (no duplication — this skill covers the gaps).
- Invoke during `page-builder` and `design-system` steps as a quality gate.
- Use the 3-level Norman audit (visceral / behavioral / reflective) as a pre-launch checklist for every page.
- Use the dark patterns list as a client communication tool when reviewing requirements.
- Cognitive bias awareness (Section 4) should inform copy decisions in `sales-copywriting` and `page-builder`.
- Section 8 Tidwell patterns govern multi-step flows, navigation stability, and form behaviour — cross-reference with `form-ux-design` and `page-builder`.
