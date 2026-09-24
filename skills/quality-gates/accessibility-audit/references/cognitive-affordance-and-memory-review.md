# Cognitive Affordance and Memory Review

Parent skill: [accessibility-audit](../SKILL.md). Read when you review whether a template's controls can be found, recognised and understood, and whether any task asks visitors to remember, notice or hold more than people reliably can.

This review sits beside `question-mark-and-scan-audit.md`. That file asks whether a page is findable and scannable; this one tests each important control and each multi-step task against the limits of human perception, attention and memory. It is a design review. It cannot certify accessibility or usability without rendered and user evidence.

---

## 1. The four-stage affordance walk

A cognitive affordance is anything that helps a visitor know what to do: a label, a button shape, an icon, a format hint, a status message. It works only if it passes four stages in order. A failure at any stage breaks the chain, and a later stage cannot compensate for an earlier one.

Walk every primary call to action, every form field, every navigation control and every system message through the four stages.

| Stage | Question | Typical failures | Repair |
|---|---|---|---|
| 1. Presence | Does a cue exist at all? | No label on an icon; no format hint on a date field; no sign that a default is active; no reminder of a step people forget | Add the missing label, hint, state indicator or reminder |
| 2. Visibility | Can the cue be seen? | Not rendered at this breakpoint; covered by a banner or cookie bar; tiny, peripheral or lost in clutter | Render it, uncover it, enlarge it, move it towards the centre of attention |
| 3. Recognisability | Can it be found and identified without searching? | Low contrast; placed outside the visitor's focus; blends into surrounding decoration; looks like body text | Increase contrast and size, separate it from clutter, place it where the eye already is |
| 4. Intelligibility | Once found, is it understood? | Illegible face, size or contrast (legibility); vague or internal wording (meaning) | Fix legibility first, then rewrite the words in the visitor's vocabulary |

### What Presence must cover
Check that cues exist to:
- show which element to act on, and how;
- help the visitor start the task;
- guide entry into each form field (format, units, example);
- show active defaults and the current state or mode;
- remind the visitor of steps they might forget;
- steer away from inappropriate choices;
- support recovery after a mistake;
- help the visitor answer any question the site asks them.

A visitor who continues without the cue proceeds without understanding the consequences. Treat that as a defect, not as consent.

### Known Visibility and Recognisability failures
- **The hidden sign-in.** A small, indistinct sign-in link squeezed among other utilities at the very edge of the header. Visitors waste time hunting for it. Make account access a clearly separated, labelled control.
- **Edge status lines.** Messages placed in a strip at the very top or bottom of the screen are routinely missed. Place feedback next to the element the visitor just used.
- **Inattentional blindness.** A visitor focused on a task can miss even a large element they do not expect, such as a warning, a pre-ticked box or a banner. Never rely on a visitor noticing something outside the path of the task; place critical information on that path.

### Recording
For each item record: template, element, the first stage it fails, evidence type (`static`, `rendered`, `manual`, `live`, `NOT_ASSESSED`), repair and owner. A static file review can check Presence and some Intelligibility; Visibility and Recognisability need rendered evidence.

---

## 2. Recognition over recall

People are good at recognising a thing when they see it and poor at recalling it unprompted. Design so that visitors choose from what is shown rather than remember what is not.

Rules:
- Show options, actions and states; do not make visitors remember them.
- Never ask a visitor to carry a value from one page to the next (a reference number, a price, a chosen option). Carry it for them and display it.
- Never ask for information the site already has. Offer it for confirmation ("Deliver to this address?").
- Label navigation in words. An icon-only menu forces recall of what each icon means.
- Show where the visitor is: page name, current-section marker, breadcrumbs, "Step 2 of 4".
- Offer recent searches, recently viewed items and search suggestions where the site has them.
- Keep critical information out of tutorials and one-time pop-ups; people forget them. Surface it in context, at the moment it is needed.
- Show system state persistently: an item added to the basket, a form submitted, a setting saved.

**Expert exception.** Recognition helps first-time and occasional visitors most. Frequent users of a tool (a booking back office, a client portal) become faster by typing or using shortcuts than by choosing from menus. Where a site has repeat power users, keep the visible menus and add keyboard shortcuts or quick-entry fields alongside them; never remove the visible route.

---

## 3. Working-memory limits

Working memory holds only a handful of items, for a short time, and loses them quickly when something else intervenes. Treat these as design constraints.

| Limit | Design rule |
|---|---|
| Capacity is small (a few items, often fewer than seven) | Keep primary navigation, visible option sets and fields per form step short; group anything longer into labelled sets |
| Duration is short and interruption erases it | Do not place a distraction (pop-up, promotion, chat prompt) between the moment a visitor reads something and the moment they must use it |
| Items are held as chunks, not characters | Display long codes and numbers in groups (for example `0700 123 456`, not `0700123456`); accept input with or without the grouping |
| Longer sentences use more memory | Keep instructions and error messages short; put the action first |

### Chunking procedure
1. List every string a visitor must read and re-type or compare (reference codes, phone numbers, account numbers, voucher codes).
2. Break each into groups of three or four characters for display.
3. Where letters form words, show the words; a meaningful phrase is one chunk, a random string is many.
4. Offer copy buttons for codes so that no memory is needed at all.

### Stacking and closure
When a visitor is interrupted mid-task, they set the current task aside mentally and must later pick it up again. That mental stack is small and unreliable; after a long enough interruption the visitor forgets what they were doing. The moment a sub-task is finished and can be forgotten is closure, and it brings relief.

Procedure for any multi-step flow (checkout, booking, application, quote request):
1. List the steps in order.
2. For each step, list what the visitor must hold in mind to complete it.
3. Mark each point where that load drops to zero; these are closure points.
4. If a long stretch has no closure point, split it into smaller steps, each with a clear finish and confirmation.
5. Remove interruptions (upsells, account prompts, newsletter offers) from inside a step; place them after a closure point, if at all.
6. Where an interruption is unavoidable (email verification, payment redirect), restore the visitor's context on return and show what they had completed.

---

## 4. Memory is reconstructive: consequences for evidence

Memory is rebuilt each time it is recalled, and it changes in the process. Visitors confidently remember doing things they did not do, and misremember what a tutorial told them.

- Provide confirmations, save points and summaries; they compensate for memory failure and are not clutter.
- When gathering feedback, ask about specific recent behaviour ("What did you do when the form asked for your ID number?"), not about feelings or general preferences. Treat stated preferences as weak evidence.
- Do not treat post-task satisfaction answers as proof of usability; pair them with observed behaviour.

---

## 5. Attention

Attention is scarce and selective. It is pulled involuntarily by motion, contrast and sound, and directed deliberately by the visitor's goal. People switch attention rapidly; they do not truly do two demanding things at once.

Rules:
- Direct attention on purpose with hierarchy, contrast and size. One primary action per screen.
- If many elements are made to stand out, none does. Reserve strong emphasis for the one or two things that matter most on a screen, and for error and warning states.
- Use motion only where it serves the visitor's task; motion captures attention more strongly than any other signal.
- Remove distractions from critical flows (checkout, forms, sign-up): no promotional banners, secondary offers or unrelated navigation.
- Keep notifications and prompts opt-in. An unrequested prompt spends attention the visitor needed for the task.
- Do not auto-dismiss important messages; the visitor may have been looking elsewhere when it appeared. Let them dismiss it.
- Onboard in stages. Teach a feature when the visitor first needs it, not in an upfront tour.

---

## 6. Perception varies

Perception is shaped by prior knowledge, culture, age and circumstance. The same shape can be read differently in a different context.

- Do not assume an icon or metaphor is universal. Some are generation-bound (a floppy disk for "save") or culture-bound. Pair icons with text.
- Never let colour carry meaning alone. Add a shape, icon or text.
- Provide redundant cues for important states: visual plus text, and haptic or sound on devices where appropriate.
- Include older visitors and people with colour-vision differences in any perception test.

---

## 7. Cognitive accessibility checks

These rules help visitors with attention, memory, reading or executive-function differences, and every other visitor as well.

- [ ] Short sentences, common words, active voice and concrete language in all interface text.
- [ ] A visual hierarchy that can be scanned without reading every word.
- [ ] No step requires remembering information from a previous screen.
- [ ] Every multi-step flow shows progress and saves state.
- [ ] Time limits warn before they expire and allow the visitor to extend them.
- [ ] Error recovery is simple, clearly labelled and keeps entered data.
- [ ] No auto-advancing content (carousels, sliders, auto-play) without visitor control of pace.
- [ ] Readability of body copy is checked against the page-builder readability standard.

---

## 8. Anti-patterns that fail this review

| Anti-pattern | Why it fails |
|---|---|
| Icon-only navigation | Forces recall of icon meaning; culturally and generationally unreliable |
| Asking again for data the site holds | Wastes memory and signals disregard for the visitor's time |
| Validation only after submit | The visitor finishes the whole form before learning of a problem, after spending memory on every field |
| Notifications that vanish on a timer | The visitor may not have been looking |
| Destructive action beside a constructive one with the same styling | Invites slips of the hand and eye |
| Multi-step flow with no progress indicator | The visitor cannot judge remaining effort and loses their place |
| Long tutorial before first use | Forgotten before it is applied; delays the first success |
| Taking stated feelings at face value | Reconstructive memory; stated preference does not predict behaviour |
| Testing only with the team | The team cannot see the site as a newcomer does |
| Colour as the only differentiator | Fails visitors with colour-vision differences and anyone in glare |
| Changing established conventions without warning | Fights habits built on other sites and on earlier visits |

---

## 9. Sign-off checklist

**Perception**
- [ ] Every important cue means the same thing across the intended audiences; icons carry labels.
- [ ] Interactive elements look interactive; non-interactive ones do not.
- [ ] Colour is always backed by a second channel.
- [ ] Spacing shows which items belong together.

**Memory**
- [ ] Every primary control and message passes all four affordance stages.
- [ ] The core task can be completed without remembering anything from an earlier screen.
- [ ] Current state and location are always visible.
- [ ] Long codes and numbers are chunked; closure points exist in every long flow.
- [ ] Conventions are followed, so habit helps rather than hinders.

**Attention**
- [ ] One clear primary action per screen; emphasis reserved for what matters.
- [ ] Critical flows are free of distraction; prompts are opt-in.

**Evidence**
- [ ] Each finding records its evidence type; Visibility, Recognisability and attention findings are rendered or observed, not inferred from source files.

---

## Sources

- Branson, S. (2020) *UX / UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*. Chapters on human memory limitations and cognitive affordance.
- Hodent, C. (2022) *What UX Is Really About: Introducing a Mindset for Great Experiences*. CRC Press. Chapters on perception, memory, attention and accessibility.
- Companion references in the design engine: `C:/wamp64/www/design-system-skills/skills/05-ux-process-research-and-psychology/ux-psychology/references/legacy-guidance.md` (sections "Working memory and cognitive load" and "Four-stage cognitive affordance discipline").
