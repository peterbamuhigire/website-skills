# Scan-First Page and Goodwill Rules

Parent skill: [page-builder](../SKILL.md). Read when you lay out any page or template and need to check that a hurried visitor can understand it at a glance, choose the right link without hesitation, and leave with their goodwill intact.

Navigation mechanics, the home page questions and mobile rules live in `navigation-mobile-and-form-pattern-rules.md`. Word-cutting rules for copy (omit needless words, remove happy talk and instructions) live in `content-writing/references/legacy-guidance.md` ("Krug's Three Web Writing Rules").

---

## 1. Design for how visitors actually use pages

Build every page on three working assumptions:

| Assumption | What visitors do | Design response |
|---|---|---|
| They scan | Glance, look for words that match their goal, click | Headings, short paragraphs, lists and bold key terms; no walls of text |
| They satisfice | Take the first plausible option, not the best one | Put the right path first and make it unmistakable |
| They muddle through | Skip instructions and form their own theory of how things work | Make the page self-explanatory; never depend on the visitor reading how to use it |

Treat each page as a roadside sign read at speed, not as a brochure read at leisure.

The governing test: a page is right when a visitor can see what it is and how to use it without thinking about it. Every moment of "Is this a link?", "Which of these do I want?" or "Where am I?" is a defect to remove.

---

## 2. Six rules for a page that works at a glance

### 2.1 Use conventions
- Logo top-left and linked home; primary navigation across the top or down the left; search top-right; links visibly styled as links.
- A convention costs the visitor nothing to learn. Depart from one only when the gain is clear and large enough to repay the learning cost, and test the departure.

### 2.2 Build a visual hierarchy with three properties
1. The more important something is, the more prominent it is (size, weight, colour, space around it).
2. Things that are related are grouped visually.
3. Things nested logically are nested visually (a section heading visibly contains its sub-items).

A clear hierarchy does the visitor's sorting before they start reading.

### 2.3 Divide the page into clearly defined areas
Visitors decide quickly which areas to read and which to ignore; they can ignore whole regions they have judged irrelevant, especially anything that resembles an advertisement. Give each area one job and a visible boundary, and never style useful content like an advertisement.

### 2.4 Make clickable things obvious
- Signal clickability with shape, position and colour or underline together.
- Never give links and non-clickable headings the same colour.
- On touch screens there is no hover; every clickable element must look clickable at rest.
- Never make text look like a button, or a button look like text.

### 2.5 Remove visual noise
Look for three kinds of noise:
- **Shouting:** many elements competing for attention; exclamation marks, bright colours and badges everywhere.
- **Disorder:** no grid, inconsistent alignment and spacing.
- **Clutter:** simply too much on the page.

Start from the assumption that every element is noise and keep only what earns its place.

### 2.6 Format for scanning
- Use plenty of headings, and make each heading work as a label on its own.
- Place a heading closer to the text it introduces than to the section above it.
- Keep paragraphs short; single-sentence paragraphs are acceptable.
- Use bulleted lists wherever items are parallel.
- Bold key terms where they first appear, sparingly.

### Tie-breaker: clarity over consistency
When making something slightly inconsistent would make it much clearer, choose clarity. Consistency remains the default; it yields only to a clear, demonstrable gain in understanding.

---

## 3. What navigation does besides moving people around

Navigation also:
1. **Shows what the site contains.** The labels are the table of contents.
2. **Teaches how to use the site.** It is the only instruction most visitors ever read.
3. **Builds confidence.** Clear, well-built navigation tells visitors the business knows what it is doing.

Review menu labels against all three jobs, not only against findability.

---

## 4. Mindless choices and a strong scent

Visitors will make several clicks happily if each one is obvious and unambiguous. One click that requires thought costs more than several that do not. Use this as the rule when depth and clarity conflict: prefer more obvious steps to fewer puzzling ones.

**Keep the scent of information strong.** Every link label must tell the visitor where it leads and why they would want to go there. Ambiguous labels ("Solutions", "Resources", "Learn more") weaken the trail; visitors hesitate, backtrack or leave.

Procedure for a menu or link set:
1. Write the visitor's likely goal for this page.
2. Read each link label and ask: would a visitor with that goal know, without clicking, whether this link serves it?
3. Rewrite any label that fails, using the visitor's words.
4. Where two labels could both plausibly serve the same goal, merge them or make the difference explicit.

**When a choice is unavoidably hard**, add guidance that is:
- **Brief:** the least text that resolves the doubt.
- **Timely:** shown exactly at the point of decision.
- **Unavoidable:** formatted so that it will be seen (next to the choice, not in a help page).

---

## 5. Explain what this is

Teams become too close to their own business and forget to say what it does. Visitors may not know the business, its category, or even basic web conventions.

- State plainly, near the top of the home page and each landing page, what the business offers and for whom. Well-known companies still do this.
- Never assume a visitor arrives knowing everything and needing only a buy button.
- Never assume technical literacy; explain unfamiliar steps in plain words.
- A competitor is one click away. Make the purpose of each page explicit.

---

## 6. Predictability: five checks

Visitors who can predict what will happen feel calm and are ready to act. Check each page for five kinds of predictability:

| Kind | Test |
|---|---|
| Navigation | Can the visitor always say where they are and what comes next? |
| Interaction | Can the visitor tell clickable from non-clickable without hovering? |
| Convention | Does every familiar signal (a downward arrow for a menu, a magnifying glass for search) behave as it does elsewhere? |
| Consistency | Does the site obey its own rules on every page? Breaking a self-set rule once makes the whole site less predictable. |
| Copy | Does short microcopy say what will happen after an action (who sees a post, what signing in gives, what booking includes)? |

---

## 7. The goodwill reservoir

Every visitor arrives with a limited reserve of goodwill. Each frustration drains it; when it runs out, they leave and may not return.

**Drains (remove these):**
- Hiding what visitors want to know: price, phone number, delivery terms, requirements.
- Demanding registration before showing anything useful.
- Asking for information the task does not need.
- Sending visitors on a trail ("go to X, click Y, scroll to Z") instead of linking straight to the thing.
- Looking careless: typing errors, broken images, inconsistent styling.
- Punishing visitors for not entering data the site's way (see forgiving formats in the navigation, mobile and form rules).

**Fills (add these):**
- Know the main thing visitors come for and make it obvious and easy.
- Tell visitors what they need to know up front (accepted formats, costs, delays, eligibility).
- Save steps wherever possible.
- Give straight answers to the questions visitors actually ask.
- Make it easy to recover from mistakes.
- Apologise plainly when the site cannot do what they want.

Procedure: for the top three visitor tasks, walk the route and list every drain met. Fix drains before adding new features.

### Error messages that keep goodwill
Moments of difficulty are where lasting impressions form. A considerate message turns a frustration into a reason to trust the business. The field, problem and fix structure is in `ux-writing-patterns.md`; add these rules:
- Avoid the words "error", "invalid" and "mistake" in visitor-facing text; visitors hear blame.
- Open with a brief acknowledgement where the visitor has lost effort ("Sorry, that password does not match our records").
- Name exactly what went wrong; never "There is a problem on this page".
- Mark the specific field visually, with text and an icon as well as colour.
- Offer the way out as a direct link in the message ("Forgotten your password?", "Find your username").
- Have a copywriter or content designer write the messages, not the developer who wrote the validation.

---

## 8. The trunk test

Use on wireframes and on built pages. Show the page, cold, to someone familiar with browsers but not with the site, and ask them to point to or answer:

1. What site is this?
2. What page is this?
3. What are the main sections of the site?
4. What can I do from here, and where can I go?
5. Where am I in the site's structure?
6. How did I get here, and how would I search?

Any question they cannot answer at a glance marks a missing or weak element: site identity, page name, section navigation, "you are here" marker, breadcrumbs or search.

---

## 9. Sign-off checklist

- [ ] Conventions followed; any departure has a written reason and a test.
- [ ] Visual hierarchy: prominence matches importance; grouping and nesting are visible.
- [ ] Page divided into areas with one job each; nothing useful looks like an advertisement.
- [ ] Every clickable element looks clickable without hover; nothing non-clickable looks clickable.
- [ ] No shouting, disorder or clutter.
- [ ] Headings label content on their own; paragraphs short; lists used.
- [ ] Every link label passes the scent test; hard choices carry brief, timely, unavoidable guidance.
- [ ] Page says plainly what the business does.
- [ ] Five predictability checks pass.
- [ ] Goodwill drains removed on the top three tasks.
- [ ] Trunk test passed on every template.

## Sources

- Krug, S. (2014) *Don't Make Me Think, Revisited: A Common Sense Approach to Web and Mobile Usability*, 3rd edn. New Riders.
- Panzarella, L. (2022) *UI & UX Web Design Simply Explained*. Chapters on simplicity, predictability and error messages.
