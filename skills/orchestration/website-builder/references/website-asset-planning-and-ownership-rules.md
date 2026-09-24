# Website Asset Planning and Ownership Rules

Parent skill: [website-builder](../SKILL.md). Read when planning a new website or a rebuild with a client, when writing the strategy brief and sitemap, when deciding whether a site needs replacing, or when setting up ownership, budget logic and post-launch monitoring.

This file complements `project-stage-gates.md`, `discovery-to-build-artifact-map.md` and `website-strategy-brief-template.md`. Those files define gates and artefacts; this file supplies the planning rules and decision tests that feed them. The strategic-mistakes pre-check lives in `skills/ux-conversion/cro-audit/references/legacy-guidance.md` ("The 22 Mistakes Checklist").

---

## 1. Planning order (never start with design)

Work in this order. Each step consumes the outputs of the one before; reordering is the commonest cause of a failed site.

| Stage | Outputs | Notes |
|---|---|---|
| Foundation | Website mission statement; website strategy; KPIs; audience personas | KPIs are defined before any other planning. |
| Planning | Audit of the existing site and its analytics history; competitor benchmarking; sitemap; platform selection | Platform is chosen only after requirements are written. |
| Production | Mobile-first design brief; SEO strategy; visual design; content and copy with SEO built in; build | Design begins only after strategy, personas, sitemap and SEO strategy are signed off. Never pick a template and bend the strategy to fit it. |
| Launch and life | Analytics and conversion tracking; social integration; QA and approval; launch; content calendar; ongoing maintenance, analysis and optimisation | Launch ends the project and starts the asset. |

### Website mission statement (one paragraph)

`This website exists to help [primary audience] [achieve outcome] by [what the site does], so that [organisation] achieves [business result], measured by [KPI list].`

### Named owner

Name one person in the client organisation as the website's accountable owner: they hold the strategy, approve changes, and answer for performance. The agency advises; it does not own the client's strategy.

---

## 2. Personas and audiences

### Persona question set

For each audience type, answer:

1. Who are they (role, location, age band, education, income band where relevant)?
2. What are they trying to accomplish?
3. What problem are they solving?
4. What questions do they arrive with?
5. What barriers or objections will stop them?
6. What does a conversion look like for them?
7. In which purchase phase (section 3) do they usually arrive?

### Audience types to consider

Customers or members are rarely the only visitors. Check whether the site must also serve:

- Media and journalists
- Job seekers and current staff
- Investors and funders
- Reviewers, influencers and analysts
- Strategic partners and suppliers
- Affiliates and resellers
- Donors, patrons and benefactors

Give each relevant type a path and a conversion (media enquiry, job application, investor contact), even if it is not the main commercial audience.

Rule: aim for the right visitors, not the most visitors. Traffic from the wrong audience inflates vanity metrics, raises bounce and misleads optimisation.

---

## 3. Build for all three purchase phases

Most sites are built only for visitors ready to buy. Plan content, keywords and conversions for all three phases.

| Phase | Visitor state | Typical queries | Content needed | Conversion to offer |
|---|---|---|---|---|
| Research | Knows the problem, not the brand | Unbranded problem phrases | Educational explainers, problem definitions, category guides | Email opt-in, guide or checklist download, sample, newsletter |
| Comparison | Knows the solution type, weighing options | Qualified phrases, "reviews", "vs", specific requirements | Comparisons, differentiators, case studies, testimonials, proof | Demo, quote, free consultation, buyer's guide |
| Purchase | Knows what they want | Brand, product or service name, transactional phrases | Clear pricing, clear CTA, guarantee, trust signals, low friction | Purchase, booking, enrolment, submitted form |

Test: if the site is invisible in the research phase, it may never be compared or chosen. Map every priority keyword and page to one phase (see `skills/seo-search/seo-audit/references/keyword-research.md`, "Search Funnel Mapping").

### Conversion ladder

Stack the phases as a ladder the site must support end to end: unbranded introduction, then connection and commitment to the brand, then brand-against-brand comparison, then the decision. A page that skips a rung should link to the page that supplies it.

---

## 4. Sitemap and architecture rules

1. Every website has a sitemap, without exception. It precedes design, SEO planning, content writing and any request for proposals, and it guides every later addition.
2. The sitemap shows the conversion mechanism on each page, not only the page hierarchy.
3. Group content into buckets that match how customers think about their problem, not how the organisation is structured. Each bucket becomes a primary navigation item.
4. Use at most four levels: primary (navigation), secondary (section containers), tertiary (supporting content), and a fourth level for deep or restricted pages such as limited-distribution landing pages. Deeper content is harder for people and search engines to find.
5. Do not flatten everything to equal importance.
6. No content more than three clicks from the home page; a conversion route reachable in one click from every page (both also checked in `heuristic-checklist.md` Section 3).
7. Name URLs, directories, files and data fields with search in mind from the start; architecture is where SEO begins.

---

## 5. SEO integration rules for the plan

These supplement `skills/seo-search/seo/SKILL.md`; they are planning rules, not a technical checklist.

- White-hat methods only; no link schemes, bought links or reciprocal link swaps.
- SEO is part of content writing and content approval, not a post-launch service.
- Use only original content. Syndicated or licensed copies of other people's text add no search value even when legally permitted.
- Use the customer's words, not internal jargon. Keywords come from customer research; treat any SEO supplier who asks the client to hand over a keyword list as a red flag.
- Paid-search keyword data describes advertising competition, not organic opportunity; do not select organic targets from it alone.
- Target many specific phrases, not a short list of head terms; the more specific the phrase per page, the better the landing page performs.
- Optimise every asset: images, video, file names, alt text, metadata.
- Answer questions fully so the site becomes the definitive resource for its topics.
- Remove any contractual requirement to carry links to the web vendor, and do not place a designer or agency credit link in the client's footer.
- On a rebuild, protect existing search equity: inventory ranking URLs and plan redirects before launch.
- Link the site to the organisation's social profiles and the profiles back to the site.
- For local and regional businesses, include city, region and service area in titles, metadata and body content.
- No one can guarantee a first-position ranking; treat such guarantees as a disqualifier.

---

## 6. Copy, content and owned-channel rules

### Copy versus content

| Type | Purpose | Examples |
|---|---|---|
| Copy | Permanent pages with a sales or conversion job | About, services, products, pricing, competitive advantage, guarantee |
| Content | Education, story, opinion and value without a direct ask | Articles, guides, white papers, how-tos, press releases, video |

Plan both. Copy closes; content earns authority and brings in research-phase visitors.

### Content rules

1. Every page must repay the time it takes to read.
2. Follow the sitemap and content calendar so additions keep the architecture intact.
3. Publish on the website first, then distribute elsewhere.
4. Send every external offer (ads, social posts, email, print) to a landing page on the website.
5. Never build a whole campaign on a platform the client does not own.
6. Use breadcrumbs and in-text links so visitors control their path.
7. State the value proposition before asking for the sale.
8. Never hide the unique selling proposition to keep it from competitors; they probably know it already, and hiding it only hurts customers.
9. Keep a content calendar and keep the site visibly current; a site with no new material for months signals neglect to people and search engines alike.

### Owned, earned and paid media

| Type | Examples | Rule |
|---|---|---|
| Owned | Website, blog, email, white papers, video, the organisation's social profiles | The base of the plan; everything else points here. |
| Earned | Reviews, mentions, press coverage, recommendations, shares | Cannot be bought; earned through quality and service. |
| Paid | Search ads, display, sponsored posts, sponsorships | Use for defined campaigns; do not depend on it as the main traffic source. |

Check the current traffic mix in analytics before stating what share should come from search; set the target per client rather than quoting a universal figure.

### Why social audiences must be brought to the website

Use this list when a client wants to run everything on a social platform:

1. The customer relationship is the organisation's to own, nurture and measure.
2. Full behavioural data is available only on the organisation's own site.
3. Links from social profiles support search visibility.
4. Only the website can tell the complete brand story.
5. Conversion design, testing and upsell are controlled only on the website.
6. What the organisation controls, it can keep improving.
7. Customer support is more efficient on the organisation's own platform.

Platforms own the data and can change the rules at any time; treat social as the promotion channel and the website as the destination.

---

## 7. Conversion and KPI rules

### What counts as a conversion

List every conversion type the site supports: purchase, subscription, demo request, membership enrolment, email opt-in, media enquiry, job enquiry, investor enquiry, quote request, booking, registration. Each gets a tracked event.

### Conversion rules

- Always ask for the action; a compelling page with no clear request is a common failure.
- No surprises: any price, condition or barrier revealed only at the end causes abandonment and lasting distrust.
- Make converting the easiest action on the page; one primary CTA per page.
- Incentives (bonuses, event-linked offers, expiring terms) must be real and honoured.
- Track abandonment at each step to find the late information that stops people.

### KPI rules

- The organisation owns its KPIs and the tools that measure them, not the vendor.
- KPIs measure the events that lead to a goal, not the goal itself (for example demo requests, guide downloads, dealer-locator searches, loyalty sign-ups, third-party reviews, active affiliates).
- Define KPIs before any other planning and configure each as a tracked goal or key event at launch. Route event design to `skills/seo-search/seo/references/analytics-event-map.md` and `skills/launch-ops/marketing-measurement-system/references/kpi-tree-and-definitions.md`.

---

## 8. Budget logic

Treat the website as an investment in a revenue-producing asset, not a marketing expense. Budget should follow goals; the budget must not define the site.

One planning heuristic from the source (Murtagh) splits the build budget evenly across five workstreams. Use it as a conversation tool, not a rule, and adjust per project:

| Workstream | Share in the heuristic |
|---|---|
| Strategy and planning | one fifth |
| SEO | one fifth |
| Design and usability | one fifth |
| Build | one fifth |
| Copywriting | one fifth |

The same source suggests sizing the whole budget as a proportion of the annual revenue the site is expected to produce, or, where that is unknown, as a proportion of the annual marketing budget. Agree the proportion with the client from their own economics; do not quote a fixed percentage as a standard.

### Acquisition cost test

`Website acquisition cost = total cost of creating and running the site for the period / customers acquired through the site in that period`

The site pays its way only when this cost is below customer lifetime value. See `skills/commerce/ecommerce-analytics/references/analytics-setup.md` for the lifetime-value calculation.

---

## 9. Usability and stickiness checks

### Four-question usability pulse

Ask test users (and, after launch, a sample of visitors) to rate agreement with:

1. This website is easy to use.
2. I can find what I need quickly.
3. I enjoy using this website.
4. It is easy to move around this website.

These four items are drawn from the System Usability Scale; use the full scale when a scored benchmark is required.

### Persona walk-through

Walk each persona through each purchase phase on desktop and mobile. Record where they hesitate, what they cannot find, and where the path ends without a next step. Never trade function for decoration; hidden navigation loses visitors.

### Stickiness

A visit that ends on the landing page is a missed opportunity. For every key landing page:

- Confirm within seconds that the visitor is in the right place and deliver the promise of the link or search that brought them.
- Convey the brand and offer an obvious next click.
- Provide content that rewards further exploration: related guides, tools, calculators, case studies.
- Give a reason to return (fresh content from the calendar).
- Build at least one memorable, interactive or multi-sensory moment where it suits the brand.

Page speed is simultaneously a usability, conversion and search factor; set targets from current field data and the project's performance budget rather than quoting fixed abandonment figures.

---

## 10. Ownership and monitoring

### Ownership rules (verify at kickoff and at handover)

- The organisation owns the domain registration, in its own name and contact details.
- The organisation owns the hosting account.
- The organisation owns every analytics, search console, tag manager and advertising account, registered to an organisational (not personal, not vendor) email address, with the agency added as a user.
- Analytics ownership often cannot be transferred cleanly later; if a vendor holds the account and leaves, history can be lost.
- Regular backups of files, database and media, with a tested restore.

Cross-check with `skills/agency-ops/agency-positioning/references/website-asset-value-due-diligence.md`.

### Monitoring rhythm

| Check | Cadence | Looks for |
|---|---|---|
| Analytics review | Weekly | Traffic quality, conversions by type, abandonment points |
| Search console | Weekly | Crawl errors, indexing problems, security or manual-action notices, robots.txt changes |
| Uptime | Continuous, with alerts | Outages and slow responses |
| Brand and review mentions | Weekly | New mentions, reviews needing a response, misuse of the brand |
| Backlink quality | Monthly | Unnatural or harmful links, lost valuable links |
| Content currency | Monthly | Stale pages, outdated dates, broken links, footer year |

Choose current tools for each check at the time of setup; do not hard-code vendor names into the plan.

---

## 11. Rebuild decision test

Recommend a new site (rather than a refresh) when several of these hold. One alone usually calls for targeted fixes.

- [ ] The site cannot perform in organic search because of its structure or platform.
- [ ] It no longer produces leads or customers.
- [ ] Acquisition cost through the site has risen above the benefit it produces.
- [ ] The organisation keeps losing business to competitors whose sites serve buyers better.
- [ ] The people who manage the brand cannot update the content themselves.
- [ ] It cannot publish a feed or support sharing and social integration.
- [ ] Site-wide engagement is poor (most visits end on the first page) and page-level fixes have not moved it.
- [ ] The bottom line shows no benefit from the site.
- [ ] Customers increasingly complain about the site experience.

Before any rebuild, preserve analytics history, rankings and redirects (section 5).

---

## Sources

- Murtagh, R. (2012–2013) *Build a Better Website* (also published as *The Million Dollar Website*), MillionDollarWebsite.TV.
- Krug, S. *Don't Make Me Think* (New Riders), cited within the above for scanning and navigation principles.
