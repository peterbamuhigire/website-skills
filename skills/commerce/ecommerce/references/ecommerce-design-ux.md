# E-Commerce Design and UX Reference

Parent skill: [ecommerce](../SKILL.md). Read when scoping a store, designing product pages, checkout, search and filters, photography, trust signals, or planning a conversion programme.

Organised by task. Figures such as conversion targets, image sizes and thresholds are starting points: test them against the store's own analytics. Platform, payment and tax rules change; check current provider and revenue-authority requirements before committing.

---

## 1. Scope the store before building

Answer with the client before choosing a platform or writing code:
1. What is sold: physical goods, digital goods, subscriptions, donations, services?
2. What shopping functionality: single item or multi-item cart, variants (size, colour), categories, tags, related items, special offers?
3. How is payment taken: mobile money, hosted payment page, or full API integration?
4. How is fulfilment done: carriers or couriers, free-delivery threshold, digital download links, order tracking?
5. What admin and reporting: CSV export, stock control, partial fulfilment, invoices, accounting integration?

### Accounts and order tracking
- Make registration optional and offer it at the end of checkout.
- Show order status: processing, shipped, delivered.
- Include password reset and contact-detail updates.

### Payment routes
- Hosted or wallet-based checkout is the quickest to launch with the lowest barrier; suit early-stage stores. In East Africa this typically means an aggregator covering mobile money (MTN MoMo, Airtel Money, M-Pesa) and cards; check current coverage and fees.
- Card acceptance directly needs a merchant account set up for online (card-not-present) use; a face-to-face account is not enough.
- Two gateway integration types:

| Type | Advantage | Drawback |
|---|---|---|
| Hosted payment page (customer goes to the provider) | Site never touches card data; provider handles authentication changes | Less UX control; some brand disruption |
| API integration | Full control of look and feel | Site owner carries card-security duties and the full compliance burden |

- Rule: never store card data on the server, even encrypted. For recurring billing use the gateway's tokenisation.
- Compliance: hosted page only implies the lightest self-assessment questionnaire; API integration implies full compliance and periodic scans. Confirm the current scheme rules with the acquirer.

### Tax and currency
- Account for the taxes that apply in every territory sold to (for example VAT in Uganda and Kenya); confirm current rates and registration thresholds with the revenue authority.
- Multi-currency: either set currencies with the payment provider, or show informational prices with a clear disclaimer of the currency actually charged (UGX, KES).

### Shipping and delivery
- Offer more than one delivery option (standard and express).
- Free delivery above a threshold is common practice; test the threshold.
- Digital goods: protect downloads behind a link or account page and issue licence codes where needed.

### Platform selection
- Start simple and scale: a single product can begin with a payment button.
- Hosted platforms: lower upfront cost, monthly fee, limited customisation.
- Open-source or off-the-shelf: full control; check the plugin architecture before modifying core code, and confirm basic purchasing works without JavaScript.
- Custom build: only when off-the-shelf cannot meet the need; write the exact specification first and build only what is needed now.

## 2. Principles that govern every decision

1. Design for the target customer, not for the owner. A large share of carts is abandoned, much of it before checkout begins (measure your own rate). Anything that forces visitors to think costs sales.
2. Good UX is invisible. Usability, design, writing, psychology, metrics and brand combine into trust.
3. Avoid the recurring pitfalls:
   - Product page: it holds the most user time. Offer alternate images on hover, prompt required fields before errors appear, and zoom on hover.
   - Checkout: fewest steps; do not ask for card details too early; never hide tax or delivery costs.
   - Security: a footer link to a policy is not enough; make security visible throughout.
   - Page weight: every image, library and asset counts.
4. Content and social features drive engagement: add share buttons on product and content pages, allow saved preferences, publish feeds for changing content, and A/B test promotions and copy. Check current channel usage in the target market before choosing platforms (WhatsApp often matters more than others in East Africa).
5. Colour and type influence behaviour. Design for the actual demographic; write lively copy rather than dry catalogue labels; keep brand colour out of error messages (if the brand is red, errors should use another colour); keep a living style guide for creative and copy standards.

## 3. Design the checkout

Apply these twelve rules:
1. Do not require registration before purchase; move it after the order.
2. Show stock levels prominently, including on results pages; offer pre-order for out-of-stock items.
3. Let customers change orders easily: a "remove" link, not typing zero; edit quantity in the cart.
4. Provide real-time help during checkout (chat or phone, including WhatsApp); a FAQ alone is not enough for complex purchases.
5. Keep the Back button working and preserve form data.
6. Show photos, specifications and links in the basket: thumbnail, size, colour, format, link back to the product.
7. Show a progress indicator with every step labelled and the current position marked.
8. Keep the interface simple: remove navigation, category links and promotional banners; leave a "Return to shopping" link and clear "Next" buttons.
9. Do not send customers out of checkout; show help in a modal or panel rather than a new page.
10. State delivery times early, from the product page, and update estimates dynamically as options change.
11. Say what happens next: a thank-you message plus what to expect (confirmation, dispatch notice timings).
12. Send a confirmation email with order details, delivery estimate, specific size, colour and format, and a way to change the order before dispatch.

Cart and checkout structure:
- Ideal: one page for billing and shipping (two columns reduce apparent length) plus a confirmation page.
- Adding an item returns the shopper to the previous page or uses a mini-cart.
- Show a delivery estimate before checkout; allow quantity edit and removal.
- From an internal search result to add-to-cart should take at most two clicks.

## 4. Build reviews and ratings

Why: user feedback reliably lifts sales for many stores (test the effect on yours); people tend to write positive reviews more often than negative, and shoppers distrust a wall of purely positive reviews; fresh user content keeps pages current.

Rating design:
- Use familiar metaphors (1 to 5 stars); allow one-click rating with hover preview.
- Label star levels ("Poor" to "Excellent"); show votes per rating as a distribution.
- Display the rating beside the product name; allow filtering and sorting results by rating.
- Show reviews on one page rather than paginated, so all the text is indexed together.

Collecting:
- Email customers to request reviews, timed to the product (days for electronics, longer for books or courses).
- Offer predefined pros and cons; let reviewers preview before submitting.
- State the moderation policy and when reviews will appear.

Displaying:
- Show reviewer name, location and user type, plus the date.
- Add "Was this helpful?" voting; allow sorting by helpfulness, rating, date and user type.
- Allow indented replies so threads form.

Negative reviews:
- Reply directly and professionally.
- Remove only abusive or untruthful content; keep fair criticism visible because it validates the positive reviews.

## 5. Design search and filtering

Effective search shortens the path to purchase and builds trust.

Approaches:
- Parameter ("advanced") search: often avoided; use very few focused fields and call it "Search", not "Advanced".
- Faceted search (recommended default): keyword search first, then narrowing on the results page with drill-down links (single choice) or checkboxes (multiple non-overlapping choices), showing item counts beside each option.

Facet architecture:
- Working memory is limited to about seven items, give or take two, so cap visible facets at about 10 and hide the rest under "More filters".
- Order facets by importance; show only values that match available stock; hide surplus options beyond seven or eight.
- Keep taxonomy mutually exclusive and exhaustive, with no "Other" bucket.
- Keep category hierarchy shallow.

Enhancements: silent spell-correction; auto-suggest for unfamiliar names; dynamic filtering; best-bets for common queries; show the query on the results page.

Usability rules: search box persistent at the top; results sorted by relevance rather than commercial interest; easy refinement; any filter can be undone without losing the search; short prompts and hints, not overloaded.

## 6. Avoid the common mistakes

Audit a store against these fifteen:
1. Thin product information: size, materials, weight, dimensions, care, fit; descriptive words over jargon.
2. Hidden contact details: phone, email, address and form on every page; costlier products need more contact options.
3. Long or confusing checkout.
4. Forced account creation.
5. Weak site search: keyword, category and feature filters, sorting (popular, price, newest).
6. Poor customer service: ticketing or contact triage; FAQ covering returns, replacements and common issues.
7. Tiny images: allow zoom to at least about 1024 by 768 pixels.
8. One image per product: aim for four or five (front, back, sides, detail, colour variants).
9. Poor cart design (see section 3).
10. Few payment options: cards, mobile money, and where suitable bank transfer.
11. No related products: surface them on every product page; hand-curated beats automatic (outfits, functional bundles).
12. Confusing navigation: no empty or single-item categories; prefer horizontal navigation.
13. No delivery rates: use a calculator or flat rate, never "we will email a quote".
14. No store policies: delivery, returns and replacement policies visible in one place.
15. Not focusing on the products: every element must showcase them.

## 7. Photograph products

Photos are the customer's only contact with the product, so treat photography as the most important design element. A redesign driven mainly by better photography often lifts sales sharply (measure it).

Required shots per product:
1. Overall: the whole product, isolated and uncluttered.
2. Action: in use, from another angle, or with complementary items.
3. Zoomed: detail, materials, craftsmanship.

Trigger a re-shoot when conversion is very low (a store below roughly half a per cent needs fundamental review), when the photos are first-version, or when they no longer match the redesigned site.

Process:
1. Prepare: inspect for tears, stains, chips and wrinkles; solid items need a polish, textiles need hours of pressing and arrangement, with collars straight.
2. Light: a light tent with two lamps either side for small items; two soft boxes for larger items such as clothing; a reflector to fill shadows (silver strongest, gold warm, white soft).
3. Camera: lowest ISO for sharpness; maximum resolution; white balance matched to the light; tripod with foot positions marked on the floor for consistency; grey card for colour accuracy; a horizontal extension arm for overhead shots to avoid distortion.
4. Edit: mask the background; a white or neutral background is the most versatile and will not clash with any site design; soft or selective focus can add depth to food, jewellery and watches; keep the lighting style identical across the catalogue.

Selling rules:

| Rule | Application |
|---|---|
| Show benefits | Let the photograph show the product doing its job |
| Give no reason not to buy | Remove anything that could raise an objection |
| Show in use | Communicates purpose and fit with the buyer's life |
| Sell a lifestyle | Place the product in an aspirational context |
| Match the brand | Mismatched imagery creates mental disconnect |
| Avoid clichéd stock | Real photographs beat polished but generic ones |
| Convey scale | Include a reference object of known size |
| Show detail | Large zoomable images let buyers check their deal-breakers |
| Encourage interaction | Zoom and rotate raise engagement and confidence |
| Stay consistent | Uniform lighting and styling read as one brand |
| Choose the angle | Three-quarter suggests power and scale; eye-level is relatable; low angle is imposing |
| Try unusual vantage points | An everyday item becomes interesting |
| Show packaging | Sets correct expectations of what arrives |

Approach guide: white background for clean gallery pages; natural setting to show purpose; model shots cropped so the product remains the hero. Never include props (accessories, ties, cufflinks) that are not part of the purchase.

## 8. Apply conversion principles

### Structure pages with attention, interest, desire, action
- Attention: the headline and hero image must catch a new visitor.
- Interest: copy explains how the product helps.
- Desire: a story of someone like the buyer benefiting; sell benefits, not features.
- Action: a clear call to action at the end of the flow ("Order now", "Sign up").
- Write the copy first, then design to deliver it; never design first and fill with words.

### Design-to-sell tactics
1. Priming: images shape behaviour; every image needs a job, and clichéd stock sends wrong signals.
2. Prevent choice paralysis: too many options stalls decisions; highlight a recommended default ("Most popular") and say what each option suits.
3. Show the product: screenshots for software, large images for physical goods; appearance signals usability.
4. Let people try it: freemium, demo or trial; invested time raises conversion.
5. Guide attention: arrows, aligned flow and images that point toward calls to action; structure content to flow linearly to the conversion action.
6. Always provide a next action: no dead ends ("Ready to order?", "Learn more", "Take the tour", "Shop now").
7. Place calls to action where the eye ends: on left-to-right, top-to-bottom pages, attention tends to finish at the bottom right, and the bottom left is weakest. Verify with your own heat maps and tests, since layout and reading direction vary.

### Further tactics
- Footnotes: for supplementary detail only; never bury price or conditions in small print.
- Testimonials: attribute with name, company and town; add case studies describing the process.
- Scannable feature lists: headings, icons, white space, because people scan before reading.
- Sign-up forms: required fields only, real-time validation, a tick on valid fields, no navigation on the page.
- White space to separate elements and aid scanning.
- Typography: large headings, dark text on light background unless the audience is design-forward, high contrast for scan targets and lower contrast for body.

### Layout and redesign
Consider a redesign when the design is the first version, was built for aesthetics rather than usability, uses few or mediocre photos, or converts very poorly.
- Keep it simple; remove unnecessary clicks.
- Prefer horizontal navigation; vertical bars off-centre are often skipped (confirm with heat maps).
- Let products, not the design, attract attention.
- Build an email opt-in with an incentive (for example a small first-order discount) for visitors who like the store but are not ready to buy.
- Match landing pages exactly to the promise of the ad; segment messages for novices (basic explanation) and experts (technical differentiators).
- Do not make design elements look like adverts; users ignore ad-like blocks.
- Keep users in control: experts want search and filters, newcomers want menus. Deliver the right information at the right time, because the buyer has a question at every stage.

## 9. Build trust and credibility

- Professional, simple design separates legitimate businesses from amateurs; trust has functional and emotional sides.
- Money-back or returns guarantee, displayed in the cart (check what local consumer law requires).
- Transparent delivery cost: hidden charges are a leading trust-killer; show the final price early.
- Contact details on every page through several channels; team photos; the founder's story.
- Visible security indicators through checkout.
- Third-party ratings (Google, Trustpilot, sector aggregators) are more credible than a self-run system; mark verified purchases.
- Mobile-money users often distrust unfamiliar payment routes; name the payment methods and show the merchant name customers will see on their phone prompt.

Free delivery is often the single strongest conversion lever; test it. If it cannot be free for all:
- Free above a minimum order, with progress toward the threshold shown.
- Free on the first order, as the price of acquiring a customer.
- Time-limited free delivery with a visible countdown.
- A flat rate labelled clearly, never a surprise.

## 10. Convert after the purchase

### The thank-you page
The customer has just agreed to your payment and delivery terms and given data and trust. Use the page to:
- Offer newsletter sign-up with an explicit value proposition.
- Give a short-window free-delivery offer on the next order.
- Show what others bought with this item.
- Offer a voucher for an upcoming sale or preview forthcoming offers.
- Lead to the account area to save the delivery address.
- Ask for a review or testimonial.

### Personalisation
- Base follow-up on real purchase data, not only browsing.
- Store session configurations and comparisons; tell users preferences are saved in cookies.
- Do not silently restore abandoned carts on shared devices (privacy).
- Start with email plus password; use the first conversion to trigger a second (a voucher that asks for a little more information).
- Observe the local data-protection law (Uganda's Data Protection and Privacy Act, Kenya's Data Protection Act) on consent for marketing.

### Service as marketing
A satisfied customer repeats purchases, ignores alternatives and spreads word of mouth. No optimisation method should compromise service quality or store performance: the more responsive the store, the fewer reasons to switch.

## 11. Run A/B and multivariate tests

A/B testing: two versions run simultaneously with traffic split evenly; measure conversions; keep the winner.

Test candidates: call-to-action wording, size, colour and placement; headline and description; form length and field types; layout; price and offers; images; text length.

Do not:
- Run A one week and B the next; run both at once.
- Stop before statistical confidence (use a sample-size or duration calculator).
- Test on returning visitors who know the old design; use new visitors.
- Let taste override the result (an unattractive button may win).

Do:
- Show a returning visitor the same variation each time and keep it consistent site-wide.
- Run many tests; small wins compound.

Five-step process:
1. Identify one clear goal (sign-ups, downloads, purchases, bounce rate).
2. Form a hypothesis from critical review, analytics and usability testing.
3. Create variations: one element for A/B; several for multivariate, with the tool generating combinations.
4. Run and analyse: equal traffic split; track the goal event (for example a visit to the order-confirmed page).
5. Learn: ship the winner, document the insight, feed the next test.

Lessons that often hold, to be verified on your own site: a "free" cue near or on the call to action grabs attention and should be clickable; a coloured button converts best when paired with persuasive copy; a larger call to action signals importance; wording of buttons and headlines can move results noticeably; treat published lift figures as hypotheses, not promises.

## 12. Use video carefully

- Authentic video (real people, real reactions) often outperforms polished advertising; sales staff explaining advantages on camera can convert well.
- Show the product in real use: outdoor gear on a trail, furniture in a home.
- Community formats (voting on the best video) build engagement.
- Budget is not the barrier; keep file weight and mobile data cost in mind for East African connections.

## 13. Structure navigation and information

- Prefer horizontal navigation; every category holds several products; merge or remove empty and single-item categories.
- Visitors must grasp the page layout within seconds; confusion produces exits.
- Keep the user in control and answer the question they have at each stage.

## 14. Checklists

### Pre-build
- [ ] Product type defined (physical, digital, subscription).
- [ ] Payment provider chosen; compliance duties understood.
- [ ] Local tax calculation handled.
- [ ] Delivery options and costs calculated in real time.
- [ ] Guest checkout available.
- [ ] Basic purchasing works without JavaScript.

### Product pages
- [ ] Four or five images minimum (overall, action, zoomed, variants), zoomable to about 1024 by 768.
- [ ] Alternate view on hover, no click needed.
- [ ] Full details: size, material, weight, dimensions, care.
- [ ] Stock shown on listing and product page; pre-order for out-of-stock.
- [ ] Related products shown.
- [ ] Rating and reviews beside the product name.
- [ ] Add-to-cart returns to the previous page or uses a mini-cart.

### Checkout
- [ ] Guest checkout; progress indicator; cart with thumbnail, specifications and links.
- [ ] Back button works and keeps form data.
- [ ] Navigation and promotions removed; help in modals, no external redirects.
- [ ] Dynamic delivery estimates; order review page before submission.
- [ ] Thank-you page with next steps; confirmation email with a change window.

### Trust
- [ ] Contact details on every page; returns guarantee shown.
- [ ] Delivery cost shown early; security indicators in checkout.
- [ ] Policies reachable from every page; third-party ratings displayed; team and story on the About page.

### Conversion
- [ ] Attention-interest-desire-action structure on landing and product pages.
- [ ] Calls to action at the end of the content flow; no dead ends.
- [ ] Attributed testimonials; scannable feature lists; minimal forms.
- [ ] A/B testing framework in place.

### Photography
- [ ] Neutral or white background; consistent lighting.
- [ ] Three shot types per product; benefits shown.
- [ ] No misleading props; scale reference where size matters.

## Sources

- Smashing Magazine (2011) *How to Create Selling E-Commerce Websites*, Smashing Magazine (Andrew, Chapman, Chudley and others). Informed the checkout, search, review, photography, trust and testing methods, restated here with original examples and without its case figures.
