# Behaviour and Visual Pattern Rules

Parent skill: [design-system](../SKILL.md). Read when you design page templates, layout systems, action controls, or visual style rules and need to check them against how visitors actually behave on screen.

This file is the full pattern reference behind the compressed layout, action and visual-style rules in `legacy-guidance.md` sections 9 to 11. It adds the ten behaviour patterns that every layout decision must respect, plus the style and control rules that the compressed sections omit.

---

## 1. Procedure: run every template through the behaviour patterns

For each template (home, service, article, form, checkout, 404), answer each question below. A "no" is a design defect; record it with the template name and the fix.

| # | Behaviour pattern | The visitor's stance | Test question for the template |
|---|---|---|---|
| 1 | Safe exploration | "Let me look around without getting lost or into trouble." | Can every click be undone with Back, Cancel or Undo, and does nothing irreversible happen on a single click? |
| 2 | Instant gratification | "I want to get something done now." | Is the most likely first action obvious and possible without registration, a wall of instructions, or a slow load? |
| 3 | Satisficing | "This is good enough; I will take it." | Is the right choice placed first in every list, with short labels a visitor can guess from? |
| 4 | Changes in midstream | "I have changed my mind about what I was doing." | Can the visitor leave a flow and return without losing entered data? |
| 5 | Deferred choices | "I do not want to decide that now." | Are optional questions genuinely optional, with safe defaults if skipped? |
| 6 | Incremental construction | "Let me change this, then change it again." | Can work be saved in small increments, with a continuous preview of the result? |
| 7 | Habituation | "That works everywhere else; why not here?" | Do navigation, actions and labels sit in the same place and behave the same way on every page? |
| 8 | Microbreaks | "I have just come back. Where was I?" | Can a returning visitor tell the context from the page title, headings and step indicator alone? |
| 9 | Spatial memory | "I remember where that was on the screen." | Do navigation items and primary actions keep a fixed position across pages? |
| 10 | Prospective memory | "I meant to do something next; remind me." | Do breadcrumbs, step indicators or reminders show the task in progress? |

### Rules per pattern

**Safe exploration**
- Make destructive actions reversible, or require an explicit confirmation that names the consequence.
- Keep the browser Back button working predictably. Do not open unrequested windows or intercept Back.
- Save automatically where the visitor is composing anything, so a wrong turn costs nothing.

**Instant gratification**
- Predict the first thing a new visitor will try and make that step effortless.
- Give value before asking for something valuable (email address, payment, account).
- Show partial content as it loads. Never leave the visitor looking at a blank area.

**Satisficing**
- Put the most likely choice first in every list, menu and option group.
- Keep labels short and scannable; visitors guess rather than read.
- Use a direct prompt at the most likely starting point ("Search courses", "Book a table").
- Use layout, not explanation, to steer the first click.

**Changes in midstream**
- Preserve form state across refresh, navigation and device sleep.
- Allow backwards movement in multi-step flows without data loss (re-entrance).
- When a visitor returns to an unfinished flow, restore where they were.

**Deferred choices**
- Mark required and optional fields clearly; do not make non-essential fields required.
- Use good defaults so that a skipped field never breaks the result.
- Let a purchase or registration complete without answering optional questions.
- Reassure: state where the choice can be changed later.

**Incremental construction**
- Never require a complete form before any save is possible.
- Show work in progress continuously; keep the preview-edit cycle short so creative flow is not broken.

**Habituation**
- Treat consistent placement as the highest-priority usability rule.
- Remember that help text becomes invisible after first use; the layout must explain itself to returning visitors.
- When navigation must change, announce the change on the site.

**Microbreaks**
- Write page titles and section headings that carry full context without the body text.
- In a multi-step flow, show completed steps clearly on re-entry.

**Spatial memory**
- Never move navigation items between pages; visitors remember locations more than labels.
- Pin primary actions to consistent positions (for example top-right on desktop, bottom of the viewport on mobile).
- If a responsive change must move an element, animate the transition so the eye can follow it (respect `prefers-reduced-motion`).

**Prospective memory**
- Use breadcrumbs, step indicators and section titles as reminders of the current task.
- For deferred actions (saved basket, unfinished application), offer an opt-in reminder by email or notification.

---

## 2. Layout pattern decision rules (additions to legacy-guidance section 9)

**Module tabs versus accordion**
- Use tabs only when modules are similar in length, the visitor needs one at a time, and the set is stable.
- Use an accordion when the visitor may need several sections open at once.
- Never use an accordion for primary navigation; reserve it for secondary or supplementary content.

**Responsive enabling**
- Enable a control only when its prerequisite is satisfied.
- A greyed-out control means "possible, but not yet"; always explain why (tooltip or adjacent helper text).
- Never silently hide an action the visitor expects; either disable it with a reason or show it as inactive.

**Titled sections**
- If a block cannot be given a short, plain title, the grouping is wrong. Regroup the content before styling it.

---

## 3. Action control rules (additions to legacy-guidance section 10)

**Hover tools (pointer devices only)**
- Never make hover the only route to an action; touch screens have no hover state.
- On touch, reveal the same tools in a panel or menu when the item is tapped.
- Reveal hover tools immediately and without layout shift; do not rearrange the page on hover.
- Make the same tools reachable by keyboard focus.

**Cancelability**
- Any operation that takes more than about two seconds must be stoppable, with the Cancel control next to the progress indicator.
- On cancel, restore the prior state fully; leave no partial data.
- If cancelling discards substantial work, confirm first and name what will be lost.

**Preview before commit**
- For uploads, bulk operations, messages, payments and publishing, show the result (thumbnail, count and list, summary) before the irreversible step.

---

## 4. Visual style rules (additions to legacy-guidance section 11)

### Preattentive signals
- Colour, size, shape, orientation and motion are noticed before reading. Spend them only on priority content: the primary call to action, error states, the page headline.
- Test hierarchy in greyscale. If the order of importance disappears without colour, the hierarchy depends on colour alone and must be strengthened with size, weight or position.
- Never let colour carry meaning alone; pair it with shape, icon or text.

### Colour temperature and saturation
| Choice | Reads as | Use for |
|---|---|---|
| Warm hues (red, orange, yellow, brown) | Energy, warmth, urgency | Alerts, urgent actions, hospitality warmth |
| Cool hues (blue, green, purple, grey) | Calm, trust, professionalism | Institutional, financial, clinical contexts |
| High saturation | Vivid, attention-grabbing | Calls to action and alerts only, sparingly |
| Low saturation | Calm, muted | Backgrounds and body content areas |
| Dark background | Premium, dramatic or edgy | Only as a deliberate brand decision, never by default |

Avoid bright complementary pairs (for example saturated blue on red) as text on background; they vibrate and tire the eye. For palette construction, use the design engine's colour skills.

### Typography for screens
- Left-align body text. Centre only very short text (two lines or fewer). Never justify narrow columns.
- Keep line length to roughly 10 to 12 words for comfortable reading.
- Reserve all capitals for very short labels (badges, tags); never set body text in capitals.
- Do not set body text in italic, script or ornamental faces.
- Pair typefaces by contrast (serif with sans serif), never two similar faces. Within one family, differentiate by weight and style.
- At very small sizes, prefer faces with open forms and simple terminals that render cleanly on low-density screens. Typeface choice itself follows the design engine's anti-slop doctrine.

### Space as a signal
- Generous white space reads as openness, calm and premium quality.
- Tight spacing reads as urgency, density and activity.
- Elements pressed against edges or each other create tension; use it only on purpose.
- Spacing is never only aesthetic: it tells the visitor which items belong together.

### Lines, angles and curves
- Straight lines and right angles read as calm and stable.
- Diagonals read as energy and direction; use them to lead the eye towards a call to action.
- Curves read as flow and warmth.
- Focal points form where lines converge; place the element you want noticed at those points.

### Photography
- A subject's gaze directs the viewer's gaze. Have people in images look towards the headline or call to action, not out of the frame.
- Avoid stock clichés: the smiling team around a laptop, the road to the horizon, the handshake, the sunset.
- Prefer commissioned photography of the real business to establish brand voice.
- Keep decorative images out of functional screens such as forms and checkouts.

### Icons
- Use one icon style throughout: all filled or all outline, one stroke weight.
- Pair icons with text labels; an icon alone is ambiguous to many visitors.
- Use established metaphors (magnifying glass for search, envelope for messages, house for home). Inventing a new icon language requires teaching it; avoid that on websites.

---

## 5. Template sign-off checklist

- [ ] All ten behaviour-pattern questions answered "yes" for every template.
- [ ] Tabs and accordions chosen by the decision rules above.
- [ ] Every disabled control explains why it is disabled.
- [ ] No action is reachable only by hover.
- [ ] Every operation longer than two seconds can be cancelled cleanly.
- [ ] Hierarchy survives the greyscale test.
- [ ] Body text left-aligned, line length within limits, no body text in capitals.
- [ ] Spacing, line direction and image gaze all lead to the primary action.
- [ ] Icons share one style and carry text labels.

## Sources

- Tidwell, J., Brewer, C. and Valencia, A. (2020) *Designing Interfaces*, 3rd edn. O'Reilly Media. Chapters 1 (behaviour patterns), 4 (layout), 5 (visual style) and 8 (actions).
- Companion pattern catalogue in the design engine: `C:/wamp64/www/design-system-skills/skills/04-web-and-ui-design/interaction-design-patterns/` (sections `01-behavior.md`, `03-layout.md`, `04-actions.md`).
