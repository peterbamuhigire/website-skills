# Form Layout, Flow and Validation Rules

Parent skill: [page-builder](../SKILL.md). Read when choosing field types, laying out a form, ordering questions, splitting a form into steps, designing gateway, review or confirmation screens, or specifying validation, errors, warnings, time-outs and submission behaviour for any website form.

Companion file: `form-question-wording-and-data-design.md` covers which questions to ask and how to word labels, options, headings, buttons and error text. Wording outranks layout: fix the words first.

Design-engine companion for platform code (web, Android, iOS components): `C:/wamp64/www/design-system-skills/skills/04-web-and-ui-design/form-ux-design/` (see `references/skill-deep-dive.md` and `references/form-validation.md`).

---

## 1. Field-type decision rules

Default to the three native controls. They are familiar, work on every screen, are accessible by default and are cheap to build.

| Need | Use | Do not use |
|---|---|---|
| Choose none, one or many | Checkboxes | Multi-select dropdown |
| Choose exactly one from a short list (up to about 20) | Radio buttons | Dropdown, segmented control |
| Yes/No consent or preference | Two radio buttons ("Yes" / "No") under a question | A single checkbox |
| Long list the user already knows (country, town, category) | Text box with auto-suggest | Long dropdown |
| Long list the user must browse | Custom list widget (last resort; budget build and accessibility testing) | Dropdown if a better option is affordable |
| Precise number or amount | Text box with the right keyboard | Slider or stepper |
| Small numeric range (e.g. 1–5 guests) | Radio buttons or a text box | Stepper |
| Date the user knows (birth, expiry) | Three short text boxes: day, month, year | Date picker alone; three dropdowns |
| Date near today (booking) | Text boxes plus an optional picker | Picker with no typing |

### Dropdown test
Use a dropdown only when the list is too long for radios and users cannot know the options without seeing them, and no better widget can be built. Dropdowns hide options, double the interaction, trap keyboard users and behave poorly on touch.

### Radio buttons on touch
Make the whole option label clickable, not only the circle. Shade or border each option to show its tap area. Large "button-style" radio options are acceptable if they still behave as a radio group.

### Controls to avoid in forms
- **Segmented controls and switches:** the selected state is hard to read, and a switch signals on/off, not a choice. Use radio buttons. Where a switch is used for a genuine on/off setting, never print "ON"/"OFF" inside the graphic; show the active state with colour plus position and a visible text label outside.
- **Sliders:** fiddly and imprecise. Use a text box.
- **Single checkbox:** makes users map ticked/unticked to the wording, and negative wording doubles the burden. Replace with a Yes/No question.

### Date picker rules (when a picker is offered)
1. Keep typing available; the picker is optional, never the only route.
2. Open on a sensible default date.
3. Allow direct jump to month and year, not only one month at a time.
4. Show months as words to avoid day/month order confusion.
5. Disable impossible dates.
6. Write format hints as letters (DD MM YYYY), never example digits, and match the local order and week start of the market.

### Selection controls, chips and mobile filters
- Use chips for compact, visible, tappable filter or tag choices; each chip is a real toggle button or checkbox with a text label.
- On mobile, put filters in a full-height sheet or page with a clear count of results and a single "Show N results" action; do not shrink a desktop sidebar of dropdowns onto a phone.
- Keep selected filters visible as removable chips above results, with "Clear all".

---

## 2. Layout rules

1. **One vertical path.** Line up every field and the primary button on one vertical axis. Never place questions side by side. Short answer sets of three or fewer options with short labels (Yes/No; day/month/year) may sit in a row; longer sets stack vertically.
2. **Responsive labels.** On small screens put labels above fields so they stay visible while typing. On wide screens labels may sit to the left, which shortens the form. With left labels, set short labels flush right against their fields; set long labels flush left and add faint alternate-row shading so the eye can track label to field. Where a single rule is preferred for simplicity, labels above on every size is the safe default.
3. **Proximity.** Keep label, help and field of one question close together; put clearly larger space between questions.
4. **Question-level help.** Put format hints above the field; put other help directly under the label. Always show help on the page; never hide it behind an icon, tooltip or hover.
5. **Field widths signal answer length.** Size each box to the typical answer (narrow for day or postcode, wider for email). Visual width does not limit characters.
6. **Field styling.** Show a visible four-sided border and no fill colour; filled fields look like buttons. Read-only pre-filled values drop the border so they read as text.
7. **Nothing inside the field but the answer.** No placeholder text and no floating labels. Placeholders make fields look answered, vanish while typing, get submitted as data, are often too small and are unevenly announced by screen readers. Keep examples in the help text.
8. **Colour sparingly.** Reserve colour for the primary button, error (red), warning (orange), success (green), information and links (blue), progress state and brand marks. Never use colour as the only signal: pair it with an icon, text and shading. Keep text dark grey or black on white.
9. **Required and optional.** Put one line at the top of each screen: "All questions must be answered unless marked (optional)." Add "(optional)" to optional labels; add no asterisks. If most questions are optional, reverse it: "All questions are optional unless marked (required)."
10. **Buttons.** One primary action with the strongest treatment; secondary actions quieter; tertiary as links. No reset or clear button.
11. **Typography.** Use a face that reads well at small sizes; sentence case; no italics for labels; no all-caps; help text slightly smaller or lighter than labels. Aim for label lines of about 25–35 characters on wide screens and full width on mobile.
12. **Strip distractions.** Remove main navigation, fat footers, promotions and surplus branding from focused forms and checkout. Keep enough branding for a sense of place.
13. **Contact route.** Show a support phone number (or live contact route) on every screen of a long or high-stakes form. Hiding it only makes calls longer and angrier.
14. **Touch.** Make fields, buttons and each radio/checkbox row at least 2.75rem (about 44px) tall, avoid hover-only behaviour, and do not assume large screens are not touch screens.

---

## 3. Flow rules

### 3.1 Question order
Order questions as a courteous face-to-face conversation would. Apply these principles, and resolve conflicts between them with user research:
1. Follow the user's mental order.
2. Core before supplementary.
3. Easy and non-sensitive before difficult and sensitive.
4. Related questions together (all contact details, then all financial details).
5. Consistent throughout: never change the order of Yes/No or repeated question sets.

### 3.2 Tab order
Make keyboard tab order match the visual order of fields and buttons exactly.

### 3.3 One screen or several
1. Identify the screen sizes used by at least 60% of the audience.
2. If the form fits within about three screenfuls at those sizes, use one screen.
3. Otherwise split into steps, one topic per step, letting natural question groups define the breaks.
4. Cap the flow at about seven steps. A wizard with only one real step is unnecessary; a long wizard needs streamlining.
5. One-question-per-screen can help low-literacy or small-screen audiences but slows completion; use it only when it can be tested.

### 3.4 Progress indicator
- Minimum: "Step 2 of 5".
- On wide screens, show named steps and distinguish past, current and future; names must match the screen headings exactly.
- Never use percentages, and never understate the number of steps.
- Test whether a very short flow needs an indicator at all.

### 3.5 Step navigation
- Put "Back" and "Continue" either both aligned with the fields or back-left / forward-right; test with the audience.
- On mobile, stack buttons full width with the primary on top.
- Let users move forward only once the current step's required answers are valid, and report exactly what is missing rather than silently blocking.

### 3.6 Modals
Avoid modal windows inside forms. They disorient users, break on small screens, escape screen magnifiers and may not be announced.

### 3.7 Conditional and eligibility logic
- Hide questions that do not apply; show them only after a reliable trigger answer. Answer options may also be conditional.
- Double-check trigger logic so no one is locked out of a question that applies or shown one that does not.
- Put eligibility questions straight after the gateway. Tell ineligible users immediately, explain why, and stop them from continuing.

---

## 4. Screens around the form

### 4.1 Gateway screen (long or complex forms only)
Contents: what the form is for and who should use it; documents, equipment or other people needed; typical completion time if known; save-and-return availability (for forms over about 5–10 minutes); privacy and terms summary with links. One prominent start button. Make the gateway the indexed, linked, single public URL; keep the form itself out of search. Do not count it in the progress indicator.

### 4.2 Review screen
Add before submission when consequences are significant (payment, legal commitment) or the form has several steps. Show every question and answer in form order with a "Change" link per question or section.

### 4.3 Confirmation screen
State that the form is finished and submission succeeded; give the reference number; say whether a confirmation email was sent; explain what happens next and when; say how to track progress; list any remaining actions; offer onward links (never a dead end). Thank the user. Email a copy when an address was collected. Optionally ask one difficulty question on a seven-point scale, clearly optional.

---

## 5. Validation and messages

### 5.1 Error types
- **Omission:** a required answer is missing. Report which questions.
- **Commission:** an answer is present but invalid. Check only obvious, damaging errors (an email with no "@"); over-validation rejects real but unexpected answers.
- Accept users' formats (spaces, brackets, different date orders) and normalise them in code. Demanding one format is a coding shortcut, not a user requirement.
- Always validate on the server as well; client checks are easily bypassed.

### 5.2 Primary button
Keep it enabled until submission. A disabled button tells users something is wrong without saying what. During processing, disable it, show a repeating animation with text ("Sending your enquiry…") and block further input to prevent double submission.

### 5.3 Inline validation
Use only on short forms (under about ten questions) where most checks can run inline. Wait until the user leaves the field; never validate while they are still typing; do not rely on browser-default validation bubbles. Mixed inline and server checks must still show all server errors clearly.

### 5.4 Error presentation
- Place each message immediately **above** its question, not beside it, not only at the top, never in a pop-up or tooltip.
- Shade the whole question light red, add an exclamation icon and the message text.
- On long forms, list all errors at the top with anchor links to each; otherwise move focus to the first error.
- Budget design time for error states comparable to the main layout.

### 5.5 Warnings
Warnings allow the user to continue (weak password, approaching time-out). Style them like errors but orange, and keep the two clearly distinguishable.

### 5.6 Time limits
Allow at least 20 minutes; warn well before expiry; offer an extension at least as long as the original limit; on multi-step forms, restart the clock on each step.

---

## 6. Reducing workload

| Technique | Rule |
|---|---|
| Right keyboard | Set input `type` (`email`, `tel`, `url`, `number`) or `inputmode`, plus `autocomplete` tokens |
| No double entry | Never ask for email or password twice; offer easy reset and, if needed, email verification |
| Show/hide password | Start hidden; use the words "Show" / "Hide", not only an icon |
| Pre-population | Pre-fill what the organisation already knows; editable values look like normal fields; locked values look like plain text |
| Defaults | Pre-select only with strong evidence of the likely answer and low cost of a missed change; always editable |
| Save and return | Offer for forms longer than about 5–10 minutes |
| Autofill and address look-up | Use on checkout and delivery steps to speed completion |

---

## 7. Resolving conflicting advice

Some general UI guides recommend placeholder examples in every field, icons inside inputs, dropdowns from five options up, a terms checkbox on every data form and live validation as users type. Apply this file's stricter rules instead: examples go in visible help text; icons inside inputs only when they carry meaning and never replace the label; radios up to about 20 options; consent captured as an explicit question with a link to the terms, only where law or contract requires it; validation after the field is left. Rounded input corners and success ticks are acceptable styling choices provided borders stay visible and success is not colour-only.

---

## 8. Layout and flow sign-off checklist

- [ ] Native controls used; no single checkboxes, sliders, switches-as-choices or long dropdowns.
- [ ] One vertical path; labels responsive or above; help visible and correctly placed.
- [ ] No placeholder or floating labels; bordered, unfilled fields sized to answers.
- [ ] Optional questions marked in words; no asterisks; no reset button.
- [ ] Colour never the only signal; errors red-shaded with icon above the question; warnings orange.
- [ ] Question order follows the five principles; tab order matches visual order.
- [ ] Step count within limits; honest step-based progress; step names match headings.
- [ ] Gateway, review and confirmation screens present where warranted.
- [ ] Primary button enabled until submit; processing state blocks double submission.
- [ ] Time limits of at least 20 minutes with warning and extension.
- [ ] Correct keyboards and autocomplete; no double entry; show/hide password.
- [ ] Contact route visible on every screen of long forms; navigation and fat footer removed.

---

## Sources

- Jessica Enders (2016) *Designing UX: Forms — Create Forms That Don't Drive Your Users Crazy*, SitePoint. Includes her citation of Luke Wroblewski on layout economy and of UK Government Digital Service research on long option lists and progress indicators.
- Elisa Paduraru (2024) *Roots of UI/UX Design: Learn to Develop Intuitive Web Experiences*, Creative Tim (forms, toggles and wizard sections; conflicting advice resolved in section 7).
- Hype4, *Frontend Unicorn* (selection controls, chips and mobile filtering), and *DESIGN.RIP — Master UI Design Elements* (form and selection-control standards); publication details as available in the source files.
