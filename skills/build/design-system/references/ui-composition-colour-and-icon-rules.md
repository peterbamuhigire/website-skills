# UI Composition, Colour and Icon Rules

Parent skill: [design-system](../SKILL.md). Read when you turn a wireframe into visual design and must decide what dominates each page, how elements align and group, how colour and contrast set reading order, and how icons and interactive states are drawn.

Typeface selection, palette construction and token scales come from the design engine (`C:/wamp64/www/design-system-skills`). Layout, action and behaviour patterns are in `behaviour-and-visual-pattern-rules.md` and `legacy-guidance.md` sections 9 to 11. The squint test is in `ux-quality-checklist.md`.

---

## 1. What visual design is for

Visual design is a working language that directs the eye, explains the content and moves the visitor to act. It is not decoration, personal expression, or a template with a new logo and colours. It carries every structural decision from discovery and wireframing into the finished page.

Before styling any template, answer these questions in writing:

1. Which colours are used, and what does each one mean?
2. Which typefaces, and why (per the design engine's typography doctrine)?
3. What images are used, and what job does each do?
4. How are clickable areas shown?
5. How is the planned reading order enforced visually?
6. How is the business objective emphasised?
7. How are buttons, body text, titles and subtitles made clearly different from each other?
8. How is the main column distinguished from any sidebar?
9. How do elements align with each other?
10. What is the dominant element of the page?
11. How is a comfortable reading pace achieved?
12. How are the client's existing brand assets brought in?

**Avoid the generic interface:** a structure seen a thousand times, borrowed colours, text treated like everyone else's. It may be clean, but it is forgettable and builds no relationship with the visitor. The answers above must be specific to this business.

---

## 2. Dominance

The dominant element is noticed first and sets the reading order for the whole page. A page with no dominant element has no reading order: everything competes, the visitor's path becomes unpredictable, and they lose patience.

Create dominance with three tools:

| Tool | How it works |
|---|---|
| Size | Larger elements are seen first; this is why titles are larger than paragraphs |
| Contrast | A small element with strong contrast beats a large low-contrast one |
| Negative space | Surrounding an element with empty space puts it centre stage whatever its size or position |

Procedure for each template:
1. List the elements the visitor needs to make their decision on this page.
2. Choose one as the dominant element, normally the headline or the primary call to action.
3. Apply size, contrast or space to it, and remove competing emphasis elsewhere.

**Logo requests.** Clients often ask for a large logo. A visitor arriving at an unfamiliar business has not come to admire its logo. Keep the logo recognisable but not dominant; give dominance to what drives the business objective, and explain this reasoning to the client.

---

## 3. Alignment

Aligned elements are faster to read and interpret, look related, and create a calm, trustworthy impression, which is the right state for a visitor about to act.

- Left-align body text. Every line then starts at the same point; centred text forces the eye to hunt for each new line's start.
- Centre only short headlines.
- Align images, cards and text to a shared grid so that the eye travels in straight lines.
- Alignment is optical, not only mathematical. Shapes with different visual weight (a round icon beside a square one, a quotation mark hanging before text) may need nudging to look aligned even when the grid says they are. Judge by eye at final size.

---

## 4. Rhythm

When the interval between repeated elements is always the same, the eye learns the pattern and predicts where the next item starts. That rhythm lets visitors scan long lists and grids without fatigue.

- Give every element in the same logical group identical treatment: same shape, typeface, size, spacing and container.
- Give different logical groups visibly different treatment.
- Keep spacing between repeated items exactly consistent; a single irregular gap breaks the rhythm and reads as a new group.

---

## 5. Consistency

The visual language must stay the same across pages and within each page. Each change forces the visitor to unlearn one rule and decode another.

Decide these in advance and never deviate:
- one type family system (per the design engine), with fixed sizes for H1, H2, H3 and body;
- a colour palette in which each colour always has the same meaning;
- a small set of button sizes and styles (three or four at most);
- one icon style (stroke weight, fill, corner radius);
- one link style.

Check that each of these is clearly different from the others (a link never resembles a button; a subtitle never resembles body text).

Carry the same language across every channel the business uses (site, app, email, social), so that visitors recognise they are in the same place.

---

## 6. Proximity

Elements placed close together are read as one group; elements far apart are read as separate. Proximity is strong enough to override colour differences and even dividing lines.

- Place a caption closer to its image than to the next paragraph.
- Place a card title where it can be scanned on its own, with clear space above and below, so visitors can skim headlines before deciding to read.
- Split navigation into spaced groups to show hierarchy without labels (for example products on one side, support and account on the other).
- Use precise spacing instead of borders to form cards and columns wherever possible.
- Cluster related controls (such as search filters) tightly; they belong to one operation.
- On very dense layouts spacing alone may not be enough; add containers or borders there.

For every element ask: how does this relate to what surrounds it? Its position should answer that.

---

## 7. Colour

Colour has three jobs. Assign each colour to a job before using it.

### 7.1 Attention and mood
- Red and green carry strong interface conventions: red for urgency, errors and required attention; green for success, completion and safety. Do not reverse them.
- Other colour associations vary by culture and sector. Check the target audience's associations before relying on one; do not assume a single universal meaning.

### 7.2 Showing what is interactive
Visitors scan for colour to find what they can act on. Reserve the interactive colour for interactive elements only.
- Test: remove every neutral element from a screenshot. What remains coloured should be exactly the set of available actions and key statuses.
- Use distinct colours for "you can act here", "this is the current state" and "this is only status information", and keep them distinct everywhere.

### 7.3 Brand identity
Colour becomes part of the brand only through strict, repeated use. Inconsistent use gives no recognition benefit.

### 7.4 Four questions before finalising any design
1. Am I using few colours, each with a defined meaning? Aim for three to five in the working palette.
2. Does each colour reinforce the message, or fight it?
3. Is each colour used consistently for the same function everywhere?
4. Does any meaning depend on colour alone? If so, add text or an icon, so that visitors with colour-vision differences are not excluded (for example, a form error needs an icon and message, not just a red border).

---

## 8. Contrast and reading order

The eye moves from highest contrast to lowest. Use this to set reading order before a word is read.

- Dark text on a light background gives the easiest reading. Low-contrast text makes the visitor work harder and tires them.
- High contrast is not the same as readable: some complementary pairs (for example saturated red on green) contrast strongly but vibrate and are hard to read.
- Use several shades of one colour to create reading levels: for example a dark background band, a lighter header area and a lightest content area give three priority levels.
- Give the most important button the highest-contrast treatment on the page.
- For each text or button, ask how important it is relative to everything else on the page, and set its contrast to match.

**Distance test.** Step two to three metres back from the screen. Whatever remains clearly visible is the highest-contrast element; it should be the primary call to action or the most important message. Use alongside the squint test in `ux-quality-checklist.md`.

---

## 9. Affordance and interactive states

Visual design should invite visitors to interactive areas and steer them away from non-interactive ones, without any instruction text. If a design needs "click here" to be understood, the design is not yet clear enough.

- Borrow physical metaphors where they fit (a handle suggests a drawer that opens; a draggable handle on a slider invites dragging).
- Place interactive cues where the visitor's hand and eye already are.
- **Inactive states must look inactive**, like a switched-off light: dimmed and without the interactive colour. Pair a disabled control with the reason it is disabled.
- **Toggle states** (on/off, selected/unselected) must be unambiguous at a glance, without relying on colour alone.
- **False affordances** are defects: a decorative card with a shadow and hover effect that is not a link; a heading styled like a button; underlined text that is not a link. If it looks interactive, it must be interactive; if it is decorative, it must not look interactive.

---

## 10. Icons

Icons catch the eye, save space and can be understood without reading, but only when their meaning is unambiguous to this audience. If visitors cannot predict what an icon does, it is a usability defect.

Pair icons with text labels by default, and always for less technically confident audiences.

Four rules for an icon set:

| Rule | Check |
|---|---|
| Consistent perceived size | Icons of equal pixel size can look different in weight because of their shape and stroke. Adjust until they look equal; a visually heavier icon draws unintended attention. |
| Consistent level of detail | A more detailed icon attracts more attention. Choose one level of detail for the set and hold it. |
| One style | Do not mix outline, filled, rounded, illustrative or pastel styles within a set. |
| Respect conventions | The few near-universal icons (home, search, print, back, close) should look as visitors expect. Do not reinvent them. |

---

## 11. Visual appeal as a screening device

Visual quality decides whether visitors stay long enough to judge the content at all. A cluttered or careless-looking page loses visitors on the next click, before they assess what it offers. Visitors who have already chosen a supplier will push through friction and defend their choice, but first-time visitors will not.

Appropriateness depends on context. The same audience that enjoys bright colour and movement in entertainment may reject it on a job application, a bank or a government service. Match visual energy to the visitor's task and expectations, not only to their demographic.

Visual appeal does not excuse usability failures; it only buys the chance to be evaluated.

---

## 12. Sign-off checklist

- [ ] The twelve visual design questions are answered specifically for this business.
- [ ] Each template has one dominant element that sets the reading order; the logo is not it unless there is a reason.
- [ ] Body text left-aligned; optical alignment checked at final size.
- [ ] Repeated elements share identical treatment and spacing.
- [ ] Type sizes, colours, buttons, links and icons are fixed in advance and used consistently.
- [ ] Grouping is shown by spacing; borders only where density requires them.
- [ ] Palette of three to five colours, each with one job; interactive colour used only for interactive elements.
- [ ] No meaning carried by colour alone.
- [ ] Contrast order matches importance; distance test and squint test passed.
- [ ] Inactive and toggle states unambiguous; no false affordances.
- [ ] Icon set consistent in perceived size, detail and style; labelled; conventions respected.
- [ ] Visual energy suits the visitor's task context.

## Sources

- Panzarella, L. (2022) *UI & UX Web Design Simply Explained*. Part 2 (UI design).
- Branson, S. (2020) *UX / UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*. Section on beauty and usability.
- Hodent, C. (2022) *What UX Is Really About: Introducing a Mindset for Great Experiences*. CRC Press. Section on affordances and false affordances.
