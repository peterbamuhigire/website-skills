# Model Metric Definitions and Lead Arithmetic

Parent skill: [marketing-measurement-system](../SKILL.md). Read when writing KPI formulas for a particular business model, choosing between conversion rate and revenue per visitor, working out how many enquiries a site must produce from the client's sales capacity, or reporting on content whose value does not appear in last-click attribution.

This file complements [KPI tree and definitions](kpi-tree-and-definitions.md) (tree shape and definition card) and [one metric KPI contract](one-metric-kpi-contract.md) (admission test, targets and actions). E-commerce mode diagnosis, zero-result search and stock-versus-sales checks live in `../../../commerce/ecommerce-analytics/references/store-mode-diagnosis-and-merchandising-signals.md`.

## 1. Define the words before the numbers

Most reporting disputes are disputes about words. Before any formula, write these sentences with the client and store them with the metric dictionary:

- "An **active** [customer / member / listing] is one that [specific behaviour] within [window]."
- "A **qualified** enquiry is one that sales marks as [criteria] within [days] of receipt."
- "A **repeat** customer is one with a second paid order within [window] of the first."
- "An order counts when [confirmed identifier exists and payment is received / cash on delivery is collected]."

Change a definition only through the honest adjustment rule in the contract file, and restate history under the new definition or mark the break.

## 2. Revenue per visitor before conversion rate

Conversion rate can rise while the business earns less, for example when a discount pulls in small orders. Revenue per visitor holds conversion and order size together.

- **Revenue per visitor** = net revenue ÷ sessions (or ÷ users; state which).
- **Net revenue** excludes cancelled orders, refunds, failed mobile-money collections and refused cash-on-delivery orders.
- **Decomposition:** revenue per visitor = conversion rate × average order value. When it moves, report which factor moved.

Decision rule: for any change that can affect order size, the primary metric is revenue per visitor (or margin per visitor where margin data exists), with conversion rate as a diagnostic.

Worked example (illustrative figures only). Two versions of a Kampala homeware store's category page each receive 10,000 sessions. Version A converts at 2.0% with an average order of UGX 90,000: revenue per visitor UGX 1,800. Version B converts at 2.4% with an average order of UGX 70,000: revenue per visitor UGX 1,680. Version B "wins" on conversion and loses on revenue. Report A as the better page unless the quarter's objective is new-customer count.

## 3. Definitions by business model

State the formula, source and window for each metric used. Numbers below are definitions, not targets.

### All models

| Metric | Formula | Use |
|---|---|---|
| Sessions-to-clicks | sessions that land from a source ÷ clicks recorded by that source | A large gap signals a slow or broken landing page, redirects dropping UTMs, or consent blocking measurement. Investigate before blaming the channel. |
| Reach needed | target customers ÷ expected conversion rate from reach | Tests whether a channel can plausibly deliver the goal before money is spent |
| Campaign contribution (email, SMS or WhatsApp) | incremental revenue − campaign cost − estimated value lost through unsubscribes or opt-outs | Stops list-burning campaigns from looking profitable |

Email open rates are recorded by tracking pixels and are unreliable as a success measure. Verify current behaviour with the email service before reporting opens; judge campaigns on clicks, replies and orders.

### Lead generation and professional services

| Metric | Formula |
|---|---|
| Qualified enquiry rate | qualified enquiries ÷ all enquiries (CRM label, not form count) |
| Cost per qualified enquiry | channel spend ÷ qualified enquiries from that channel |
| Enquiry-to-customer rate | customers won ÷ qualified enquiries, by enquiry month cohort |
| Time to first response | median minutes or hours from enquiry to first human reply |
| Content-influenced conversations | discovery calls or enquiries where the prospect names a piece of content (section 6) |

### Subscription and membership

| Metric | Formula |
|---|---|
| Churn (simple) | members lost in period ÷ members at start; acceptable for a stable base |
| Churn (growing base) | members lost ÷ average members in period, or churn by joining cohort |
| Net adds | new paying members − cancelled paying members, per week or month |
| Inactive | no sign-in or use within a stated window (for example 90 days or less) |
| Time to customer breakeven | acquisition cost ÷ monthly contribution per customer |

Report free-user and paying-customer churn separately.

### Publisher and content sites

| Metric | Formula |
|---|---|
| Page inventory | unique visitors × sessions per visitor × pages per session (× advertising slots per page) |
| Audience churn | new first-time visitors − net change in unique visitors; a campaign spike can hide loss of regular readers |
| Engaged time on content pages | average active time on article pages, excluding the landing page |

### Directories, listings and marketplaces

| Metric | Formula |
|---|---|
| Search success | searches returning at least one result ÷ all searches |
| Active listing | a listing shown in at least [n] searches in the last [window] (client sets n) |
| Engaged buyer | a visitor who searched or enquired within the last [window] |
| Buyers per active listing | engaged buyers ÷ active listings |
| Completed-to-listed ratio | listings that ended in a transaction ÷ listings in period |

## 4. Lead requirement back-solved from sales capacity

Start from what the client's sales team can handle, not from traffic ambitions. The website target is the number of qualified enquiries that keeps sales capacity full, adjusted for the share of raw enquiries that qualify.

### Formula chain

1. **Sales capacity** = sales staff × contacts per person per day × working days per month.
2. **Qualified enquiries needed** = sales capacity × share of contacts that need a fresh enquiry (the rest are follow-ups and existing customers).
3. **Raw enquiries needed** = qualified enquiries needed ÷ qualified share (from CRM history).
4. **Sessions needed** = raw enquiries needed ÷ enquiry rate on the relevant pages.
5. **Budget check** = raw enquiries needed × cost per raw enquiry for each channel, compared with the allowable cost the client's finance owner sets.

Worked example (illustrative figures only). A solar installer has 6 field staff making 3 site visits a day on 22 working days: 396 visits a month. Half need a fresh qualified enquiry: about 200 a month. CRM history shows 25% of lead-form enquiries qualify, so the site and campaigns need about 800 raw enquiries a month. At an illustrative UGX 8,000 per raw enquiry the lead budget is about UGX 6.4 million a month. Compare with a channel that yields fewer but better-qualified enquiries, such as radio call-ins or referral.

### Qualification by effort

- An enquiry that costs the prospect effort (a specific question typed into WhatsApp, a phone call, a detailed form) is usually better qualified than a one-tap lead form. Check this against the client's own CRM labels.
- When sales capacity is the bottleneck, add qualifying friction (a budget or timing question, a required project description) and watch qualified share and cost per qualified enquiry.
- When the pipeline is empty, reduce friction and accept a lower qualified share.
- Test friction changes through `experimentation`; do not assume the direction.
- Reconcile monthly: qualified enquiries reported by sales against qualified enquiries the site recorded. Show the gap and its owner.

## 5. Echo effect: sales that happen elsewhere

Many buyers see a website or campaign and then buy by phone, WhatsApp or walk-in, where no code or link records the source. Measure that echo rather than under-credit the site.

1. Take a baseline of untracked sales (walk-in, phone, untagged WhatsApp orders) over at least six months before the campaign.
2. During the campaign, record tracked sales (coded links, QR codes, WhatsApp keywords, "how did you hear" answers) and untracked sales.
3. Echo percentage = (untracked sales during campaign − baseline untracked sales) ÷ tracked campaign sales.
4. Report total effect as tracked sales plus the echo, labelled as an estimate.
5. State seasonality, price changes and other campaigns running in the window. Echo is an estimate of association, not a causal measurement.

Worked example (illustrative figures only). A Nairobi bakery averages 150 coded WhatsApp orders a week during a campaign. Untracked walk-in and phone orders averaged 120 a week over the prior six months and 155 a week during the campaign. Echo = 35 ÷ 150 ≈ 23%.

## 6. Body of work and the B2B attribution caution

Thought-leadership content for professional and B2B clients rarely shows up as a last click. A buyer reads six articles over four months, then types the firm's name into a search engine or asks a colleague for an introduction. Last-click reports credit "direct" or "branded search" and make the content look worthless.

Report these alongside pipeline metrics, never instead of them:

| Measure | Definition | Source |
|---|---|---|
| Body of work | published pieces per content pillar, cumulative | Content calendar |
| Content-influenced conversations | enquiries or discovery calls where the prospect names a specific piece | CRM "how did you hear" field and call notes |
| Authority signals | speaking invitations, media requests, guest invitations, partnership approaches | Log kept by the account lead |
| Recruitment signals | applicants who cite the content | HR log |
| Publishing consistency | planned slots actually published ÷ planned slots | Content calendar |

Rules:

- Label these as influence, not attribution. Do not convert them into revenue claims.
- Add a required "how did you hear about us" field to enquiry forms and sales notes, with a free-text option.
- Review the pattern quarterly in the [quarterly business review](quarterly-business-review.md).
- If a client chooses not to publish content at all, measurement shifts to referral and network sources; that is a legitimate choice, recorded as such.

## 7. Anti-patterns

| Anti-pattern | Correction |
|---|---|
| Optimising conversion rate while order value falls | Use revenue or margin per visitor as primary |
| Traffic targets with no link to sales capacity | Back-solve enquiries from capacity (section 4) |
| Counting form submissions as leads | Count CRM-qualified enquiries; reconcile monthly |
| Crediting only coded sales | Estimate echo with a baseline (section 5) |
| Judging B2B content on last click | Report body-of-work and influence measures alongside pipeline |
| Reporting email opens as success | Report clicks, replies and orders |

## Sources

- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics: Use Data to Build a Better Startup Faster*. O'Reilly Media. (Revenue per visitor, model metric definitions, churn options, campaign contribution, sessions-to-clicks, audience churn.)
- Stockwell, J. and Shaw, H. M. (1994) *Direct Marketing Checklists*. NTC Business Books. (Lead requirement from sales capacity, qualification by effort, echo effect.)
- Weinberg, G. and Mares, J. (2014) *Traction: A Startup Guide to Getting Customers*. S-curves Publishing. (Reach needed.)
- McDermott, A. (2023) *Efficient Content Creation: A Practical Guide to Consistently Creating High-Quality Content in a Busy Schedule*. The Recognized Authority. (Body of work, content-influenced conversations, B2B attribution caution.)
