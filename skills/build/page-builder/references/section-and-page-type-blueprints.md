# Section and Page-Type Blueprints

Parent skill: [page-builder](../SKILL.md). Read when assembling a page from sections, when building team, trust-logo, statistics, FAQ, contact, footer, sidebar, testimonial or wizard sections, or when planning the section order of an about, profile, blog, product, SaaS, sign-up, sign-in, legal, cart or checkout page.

Related files: `component-design-rules.md` (navbars, hero, features, cards, images, icons, pricing, base FAQ and footer rules), `form-layout-flow-and-validation-rules.md` (all forms), `../../design-system/references/data-tables-charts-and-svg-rules.md` (tables and charts).

---

## 1. Before choosing sections

1. **Check the four experience inputs** for every page: the content it must carry, the user's goal, the business goal and the interactions needed. Content comes first; a layout drawn before the content is known will fail.
2. **Test the interface against four outcomes:** it explains itself, it solves the user's actual problem, a diverse audience can use it, and tasks finish without frustration.
3. **Name the page's top tasks and scenarios** before selecting patterns; pick patterns that serve those tasks, then use visual hierarchy to direct attention before adding more elements.
4. **Judge efficiency:** fewer steps, controls where users expect them, nothing that makes the task slower.

---

## 2. Section rules not covered elsewhere

### 2.1 Team
- Use real face photographs, not abstract or artistic portraits.
- Lead with names; roles come second.
- Keep contrast between photo and background; add a subtle shadow or backdrop if needed.
- Design a fallback (initials on a tinted tile) for people without photographs.

### 2.2 Client and partner logos (trust areas)
- Show colour logos exactly as their owners specify; where colour clashes, use a consistent desaturated set that keeps each logo recognisable.
- Make logos large enough to identify; tiny logos defeat the purpose.
- Soften logo colour on review sections (mid grey rather than pure black) to avoid visual shouting.
- Candidate positions: hero, careers, reviews and the pre-footer band. Pair logos with evidence (link, case study or quote) so they are proof, not decoration.

### 2.3 Statistics
- Set numbers at heading size (H1–H3); small numbers lose impact.
- Leave generous space around each figure; do not crowd many statistics together.
- Icons are decorative only and never replace the number.
- Give every number a text label and, for market-level claims, a source.

### 2.4 FAQ
- Generous line height and clear space between questions.
- Always show an expand/collapse icon so the interaction is obvious; separators are optional.
- Layout options: single list, two columns, or cards.

### 2.5 Contact
- Offer several channels (phone, email, address, form); people differ in preference.
- Ask only what the first contact genuinely needs.
- Put any required consent or terms acceptance in an explicit question, with a link; do not add a terms tick-box by habit.

### 2.6 Footer additions
- Present links in a logical order with enough spacing that none are missed; use colour or weight to give the footer its own hierarchy.
- Always include the copyright symbol, year and owner.
- Include social links; the engagement benefit outweighs the exit risk.
- Consider a subscription call to action: visitors who reach the footer are engaged.
- Add locale controls (language, currency) for multi-market or commerce sites.

### 2.7 Dashboard or portal sidebar
- Place on the left for left-to-right languages, on the right for right-to-left.
- Show main pages directly; nest secondary pages in expandable groups with clear level indicators.
- Make it collapsible for smaller screens.
- Tint icons with the primary colour or reduce them to about 60–70% opacity so they do not overpower labels.
- Highlight the active item unmistakably; group related links; place the logo at the top as the home link; pad even short items for a generous click area; provide light and dark variants when the product supports both themes.

### 2.8 Wizards
- A wizard is justified only when there are at least two genuine steps; more than about seven to ten steps means the process needs simplifying.
- Number the steps or show a step indicator; describe what each step asks for.
- Use plain "Back" / "Continue" labels; gate progress on the current step's required answers.
- Detailed rules: `form-layout-flow-and-validation-rules.md` §3.

### 2.9 Testimonials and reviews
- Use a 1–5 star scale in one consistent star colour.
- Mark testimonials with quotation marks; italics are optional.
- Add the reviewer's company logo where permitted; it adds institutional weight.
- Prepare a fallback for reviewers without photographs.
- Show real, attributable testimonials only.

### 2.10 Comments and articles
- In comment forms, place the "Post comment" action at the end of the reading line (right in left-to-right layouts).
- Articles: use the type scale for hierarchy and the standard body line height throughout.

### 2.11 Statistics, charts and tables inside marketing pages
Use real data (never placeholder text) and follow `data-tables-charts-and-svg-rules.md`.

---

## 3. Mobile principles for every section

1. Navigation that always shows where the user is and how to go back.
2. Tap targets of at least 44 × 44px with 8–10px between neighbours.
3. Key actions in the thumb-reachable lower part of the screen.
4. Clear, uncluttered screens; remove anything that does not serve the task.
5. Body text readable without zoom, typically larger than desktop.
6. Touch-native controls rather than mouse-precision widgets.
7. Minimal typing: fewer fields, autofill, correct keyboards.
8. Consistent look and behaviour between the website and any companion app, adapted to screen size.

---

## 4. Page-type blueprints

Use these as starting orders, then adapt to the page goal matrix (`page-goal-matrix.md`). No auto-rotating carousels on any page type; use static grids or user-controlled tabs.

| Page type | Section order |
|---|---|
| About | Hero (title, short description, CTA) → client/partner logos → distinctive attributes → team → confidence statistics → notable projects → footer |
| Profile (person or author) | Hero (avatar, name, short bio, follow or contact action) → their work → reviews or testimonials → contact form → footer with social links |
| Blog index | Hero (brand, navigation, category links, search) → featured and recent posts with dates and subscribe CTA → pagination or "load more" → footer (about, contact, privacy, terms, newsletter) |
| Blog post | Article → related "other articles" → subscribe → footer |
| Product | Hero (name, price, stock status, short description) → delivery, returns and category tags → ratings and reviews → related products → pre-footer subscription → footer with language and currency |
| SaaS / application | Hero (navigation, primary "Start" CTA) → features with headings and icons → integrations with logos → side-by-side pricing with CTA per plan → testimonials → footer (copyright, privacy, terms, contact) |
| Sign up | Email and password (or social sign-in) → explicit terms acceptance where required → "Already have an account? Sign in" link |
| Sign in | Email and password → "Remember me" (Yes/No or clearly labelled checkbox) → prominent sign-in button → forgotten-password link → "No account? Sign up" link |
| Legal (terms, privacy, cookies) | Sticky side navigation of anchor links → sections that highlight in the navigation as the reader scrolls → strong heading hierarchy and readable measure |
| Cart | Line items (image, name, quantity control, price, subtotal) → summary including tax and delivery → primary "Checkout" plus quiet "Continue shopping" → recommendations based on the cart → support contact and policies |
| Checkout | Autofill and address look-up → order summary visible throughout → one visually distinct "Proceed to payment" action (see `commerce/ecommerce-checkout`) |

---

## 5. Reference-site technique catalogue

When analysing admired sites (see `../../design-reference/references/reference-library-analysis.md`), name the technique, not the brand, and check it fits the client's sector and performance budget:

- Animated or gradient hero backgrounds that add depth.
- Device mock-ups that show the product in context.
- Real operating figures in statistics sections.
- Interactive maps or globes for geographic reach.
- Progress bars on user-controlled carousels.
- Duotone or lightly animated icons.
- Two-layer realistic shadows; heavier shadows to separate layers in dark mode.
- Gradient or oversized headline type; a guiding line or shape that leads the eye to the headline.
- Background blur to push secondary layers back.
- Buttons with an animated border as the single signature interaction.
- Cards that reveal extra detail on hover (with a tap and keyboard equivalent).
- Light and dark themes.

---

## Sources

- Elisa Paduraru (2024) *Roots of UI/UX Design: Learn to Develop Intuitive Web Experiences*, Creative Tim. Includes her use of Corey Stern's CUBI experience model (content, user goals, business goals, interactions).
- Chris Bank and Jerry Cao, *Web UI Design Best Practices* (top tasks before patterns; hierarchy before additions).
