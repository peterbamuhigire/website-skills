# Subscription Economy Model

The recurring-revenue financial and operating model for a premium website agency. It informs how the agency prices, measures, sells and protects retainer revenue.

The commercial model is bimodal: one-time build engagements plus monthly retainers. Retainer revenue is strategically more valuable because buyers usually value it at a higher multiple than project revenue, it smooths cash flow, and it produces behavioural data that compounds. This file sets the operating model for the retainer side. It pairs with `retainer-package-catalog.md` (what we sell), `expansion-offers-matrix.md` (how accounts grow), `post-launch-review-cadence.md` (the review rhythm) and `okrs-and-client-reporting.md` (measurement).

---

## 1. Why recurring revenue outranks project revenue

**Valuation.** Acquirers pay more for revenue that renews without a new sale. Test it yourself: ask two or three brokers or acquirers what multiple they would apply to retainer revenue versus project revenue in a small agency, and record the answers. Do not quote a multiple to a client or investor until you have checked current market evidence.

**Operations.** In a recurring business the client relationship, not the deliverable, is the asset. Consequences:

- Value is earned across the life of the relationship, not at the point of sale.
- Behavioural data (usage, enquiries, conversion trends) feeds back into service design, marketing and pricing.
- The real work starts after launch. The site is not the deliverable; the client's commercial outcome is. The retainer is the vehicle through which that outcome compounds.

**Reasons a subscriber is worth more than a one-off customer** (use as a checklist when arguing the case internally):

1. Raises the value of the company.
2. Higher lifetime value per client.
3. Smooths demand and workload.
4. Gives free market research (what clients actually ask for).
5. Pays automatically, shortening receivables.
6. Is stickier; price-shopping stops once the service is embedded.
7. Buys more, because a trusted retainer client asks for add-on projects.
8. Holds up in downturns, because maintenance spend outlasts new-build spend.

---

## 2. Five-stage operating model: Pipeline, Acquire, Deploy, Run, Expand

Treat the client lifecycle as five subsystems, each with its own owner, metrics and red/amber/green flag.

| Stage | Purpose | Where leverage sits | Where leakage happens |
|-------|---------|---------------------|------------------------|
| Pipeline | Awareness and demand | Clear positioning and narrative | Vague category, generic message |
| Acquire | The buyer's journey | Incentives aligned with the client's results | Accepting any client who will pay; wrong-fit clients distort the service |
| Deploy | Client live and integrated fast | Expectations set before signature; remove onboarding steps | Client logs in twice, then stops |
| Run | Daily and weekly success | Behavioural monitoring; a named client-success owner | Silent decay; the account looks fine until renewal |
| Expand | Retention, growth, advocacy | Cross-sell to a meaningful share of the base | Treating expansion as next year's problem |

Add three back-office subsystems: People, Product (the service), Money. Review one page per subsystem weekly; deep-dive one subsystem each quarter.

**Agency translation**

| Stage | Agency practice |
|-------|-----------------|
| Pipeline | Agency site, case studies, signature talk, podcast slots, a named list of target referrers |
| Acquire | Build sale, with the retainer pre-sold during build discovery |
| Deploy | 30-day post-launch protocol: access handover, reporting cadence, agreed goals, analytics instrumented |
| Run | Monthly cadence: one report, one strategy call, a rolling backlog |
| Expand | Quarterly business review as the expansion moment (tier upgrade or adjacent retainer) |

The build is the Acquire and Deploy event; the retainer is where Run and Expand happen. A client who buys a build but never enters the retainer discipline is a one-time customer with extra steps.

---

## 3. The recurring P&L

A conventional P&L makes growth spend look like a loss in the quarter it is incurred, although it creates revenue for many later quarters. Report in this order instead:

```
Retainer ARR (active retainers x annual fee)          X
(Annualised retainer churn)                          (Y)
Net retainer ARR                                      Z

Recurring delivery cost
  Senior capacity allocated to retainers             (A)
  Tooling, hosting, software per client              (B)
  Account operations and reporting time              (C)
Recurring delivery margin                             D    (set a target; test 60%+)

(Own sales and marketing)                            (E)
Recurring net operating income                        F

New retainer ARR added this period                   +G
Ending retainer ARR                                   I

Project revenue and margin reported separately        J, K
```

Principles: costs to serve existing ARR sit above the line; costs to grow ARR sit below it; express each as a percentage of ARR; recurring margin is the amount safe to reinvest. The board question changes from "what did we bill this month?" to "how much retainer ARR did we add this quarter, and how long will it last?"

---

## 4. Recurring-revenue dashboard

| Metric | Definition | Starting target (adjust with data) | Cadence |
|--------|------------|------------------------------------|---------|
| Active retainer count | Paying retainers | Rising | Weekly |
| Retainer MRR | Sum of monthly fees | Rising | Weekly |
| ARR | MRR x 12 | Rising | Monthly |
| Logo churn | Retainers cancelled / active | Under 5% per quarter | Monthly |
| Revenue churn | ARR cancelled / starting ARR | Under 5% per quarter | Monthly |
| Net revenue retention | (Start ARR + expansion - churn) / start ARR | 110% or more | Quarterly |
| Gross revenue retention | (Start ARR - churn) / start ARR | 90% or more | Quarterly |
| ARPA | MRR / active retainers | Rising annually | Quarterly |
| CAC | Own sales and marketing spend / new retainers | Below half of first-year retainer value | Quarterly |
| LTV | Average monthly fee x average months retained x gross margin | LTV:CAC of 3:1 or better | Quarterly |
| CAC payback | S&M spend / (new MRR x gross margin) | Under 12 months | Quarterly |
| Cash up front : CAC | Cash collected at signing / CAC | 1:1 or better | Quarterly |
| Growth efficiency | S&M spend needed per 1 unit of new ARR | Track the trend | Quarterly |
| Recurring profit margin | (ARR - recurring costs) / ARR | 60%+ | Monthly |
| Net new ARR | New ARR - churned ARR | Set each quarter | Quarterly |
| Share of revenue on 12-month contracts | 12-month retainer ARR / total revenue | Rising year on year | Quarterly |
| Largest client share | Largest client revenue / total | Under 20% | Quarterly |
| Clients on two or more retainers | Count | Rising | Quarterly |
| Annual renewal rate | Retainers renewing at month 12 | 90% or more | Annually |

Targets are starting hypotheses. Replace them with your own cohort data after two quarters.

---

## 5. Churn: types, diagnosis, reduction

**Four kinds**

- Voluntary: the client cancels (low adoption, value not visible, price mismatch, competitor).
- Involuntary: failed payment, expired card, bank block. Fixable with retries, reminders and local payment methods (mobile money, bank debit, card).
- Logo churn: number of accounts lost.
- Revenue churn: ARR lost. It diverges from logo churn when small accounts leave and large ones stay, or the reverse.

**Net churn = gross churn - expansion revenue.** When expansion exceeds churn, net churn is negative and the base grows without new sales. This metric decides whether the agency compounds or treads water.

**Diagnosis procedure when churn exceeds new adds**

1. Do not panic; diagnose. Ask which clients you should never have accepted, and which to release.
2. Classify each loss: adoption, value, packaging, price, or payment.
3. Fix the dominant cause first; adoption problems need coaching, packaging problems need a redesigned tier.
4. Cross-sell a second retainer to a meaningful share of the base; two retainers give two reasons to stay.
5. Fix payment infrastructure for involuntary churn.
6. Longer contracts help, but never replace regularly giving clients pleasant surprises.

**Ten churn-reduction tactics**

1. Sit in the client's routine: tie reports and tools to their weekly meeting.
2. Treat the first 90 days as decisive. Value and margin are largely set by then; the first 30 days are the cross-sell window.
3. Shorten time to first visible win. Ask for the least effort first (for example, agree one goal) before heavier tasks such as uploading data.
4. Charge up front where the client accepts it; prepayment tends to increase commitment. Test it against your own churn.
5. Contact heavily early and more quietly later. Check your own satisfaction data for the point where extra contact stops helping.
6. Send small unexpected gains: a quick fix, an insight, a handwritten note.
7. Favour larger or more stable clients; sole traders churn when their own market shifts.
8. Manage net churn, not gross churn alone.
9. Cross-sell to reduce logo churn.
10. Renew evergreen (automatic unless cancelled) for small tiers; end-dated terms bleed renewals.

**Churn drivers by stage**

| Stage | Driver | Fix |
|-------|--------|-----|
| Days 1-30 | Complexity, poor onboarding, asking for effort before showing value | Fast first win, frequent contact |
| Days 30-90 | Value not realised, no habit | Use-based onboarding, 90-day markers, small gains |
| Months 3-12 | Paying for something unseen; over-contact | Quieter cadence, use-based nudges |
| Anniversary | Renewal friction | Evergreen terms, annual prepay option |
| Year 2+ | Competitor approaches | Continuous service investment |

---

## 6. Pricing and packaging rules

- Re-price at least annually. Most teams spend very little time on pricing; it is often the highest-return lever. Schedule a pricing review each year.
- Use tiers with an explicit upgrade path, for example Care (UGX 900,000/month), Growth (UGX 2,400,000) and Authority (UGX 5,000,000). Upgrades offset gross churn. Figures are illustrative.
- Offer an annual prepay discount. Test 10% to 15% and measure the effect on 90-day churn.
- Use a setup or onboarding fee (framed as a real onboarding package) to raise cash collected at signing.
- Raise prices as proof accumulates; test on new clients first.
- Default to evergreen renewal for small tiers; fixed 12-month terms for clients whose procurement demands them.
- Lead with a tenfold-value argument, not a small discount, whenever a one-off alternative exists.

**Two growth levers.** Classify every pricing move as ARPA-growing (upgrades, add-ons, usage) or account-growing (competitive entry price, trial, free audit). Alternate deliberately: build account count with an accessible entry tier, then grow ARPA through upsell.

---

## 7. Selling the retainer

1. **Ten times, not ten per cent.** Compare the retainer with the cost of hiring the same skills in-house (for example a content lead, an editor and an analyst) rather than discounting.
2. **Rational case for B2B buyers.** Speed, predictability and no retail-style markup.
3. **Ultimatum.** Offer the retainer as the continuing arrangement, not alongside hourly work; when both are offered, clients pick the one-off.
4. **Freemium taste.** A free audit or short report, with the next step behind it. Track your own conversion.
5. **Paid trial.** A small paid first phase that credits against the full retainer. Focus the trial on use, not purchase.
6. **Gift or sponsored subscriptions.** Top-up only; renewal is usually poor.
7. **Time-limited incentive.** Use privately with prospects already close to a decision. Never advertise it.

**Sell internally first.** Brief the team before clients. Lead with stability (predictable workload, fewer peaks) rather than margin, which is an owner's argument. The retainer is a delivery discipline as well as a revenue line.

---

## 8. Client success as a function

Client success is not support (reactive tickets), not classical account management (chasing renewal signatures) and not sales. It comprises:

- Usage and results monitoring, weekly.
- Adoption coaching so the client's people use what was built.
- Feedback loops into service design.
- Identifying upsell and cross-sell.
- Incident learning.

**When to instrument.** With fewer than about 12 retainer clients, the founder and a senior strategist hold the role. Beyond that, hire a Client Success Lead paid for retention, not new logos. Scorecard: logo retention, revenue retention, NRR, expansion bookings, 90-day onboarding completion rate, quarterly review attendance and quality.

---

## 9. Mapping subscription models to retainers

Several models stack inside one retainer.

| Retainer | Primary model | Secondary models | Sales narrative (illustrative) |
|----------|---------------|------------------|-------------------------------|
| Care and Maintenance | Simplifier | Peace of mind, priority access | "We handle updates, backups and security checks so you do not have to." |
| SEO Foundation | Simplifier | Membership resources, content library | "Next year's organic pipeline builds from month one." |
| Content Growth | Content library | Membership, simplifier, surprise element | "A strategist, writer and editor for less than one hire." |
| CRO | Peace of mind | Priority access | "We watch your conversion rate while you sleep." |
| Technical Support | Priority access | Peace of mind, simplifier | Published response-time tiers |

**Conversion pattern.** A firm moving from hourly billing to fixed monthly fees usually meets internal resistance first. Expect it: sell internally on stability, then offer clients the retainer as the way of continuing to work together. Expect a cash inflow at conversion (roughly the advance payments of the first months); plan for it.

---

## 10. Founder rhythm

**Daily:** inbound leads (build and retainer); new activations; cancellations with reasons.

**Weekly:** active retainers and MRR; share of the recent cohort reaching 90-day markers; onboarding drop-offs; project pipeline value (keep 90 days of capacity covered).

**Monthly:** MRR; gross and net logo and revenue churn; upgrade revenue; CAC by channel; 90-day marker completion by cohort; client satisfaction score for the newest cohort; churn reasons; recurring margin.

**Quarterly:** LTV:CAC by retainer type, segment and channel; cash-up-front ratio; cohort lifetime curves; pricing tests; usage-to-churn correlation; NRR and GRR; ARPA trend; growth efficiency; share on 12-month contracts.

**Annual:** what multiple the agency could fetch today (check current evidence); renewal rate at month 12; average client lifetime; largest-client share.

The cohort dashboard is the most important artefact; waiting years for lifetime-value truth is fatal. Use 90-day markers as leading indicators, for example "did the client put the new dashboard in a sales meeting?" and "did they act on the first two recommendations?" Tune onboarding against them.

---

## 11. Eight growth levers

Work two or three at a time.

1. Acquire the right first cohort; you become your clients.
2. Reduce churn.
3. Hybrid sales: self-service entry tier, assisted upgrades.
4. Upsell and cross-sell.
5. New segments by size, sector or geography.
6. New markets (language and payment methods matter more than borders).
7. Acquisitions (later stage; needs cash and an integration plan).
8. Pricing and packaging, the lever behind the other seven.

In years 1 to 3 of building the retainer book, focus on levers 1, 2, 4 and 8. Levers 3, 5 and 6 emerge later; lever 7 is distant.

---

## 12. Anti-patterns

1. Running retainer and one-off models in parallel without an ultimatum; clients default to one-off.
2. Judging the recurring P&L by conventional framing, so growth spend looks catastrophic.
3. Ignoring team resistance.
4. Letting a project-minded seller sell the retainer; they favour the big single ticket.
5. Scaling sales before churn is under control.
6. Accepting every client in the first cohort.
7. Spending almost no time on pricing.
8. Delaying new markets.
9. Confusing support with client success.
10. Ignoring payment infrastructure.
11. Depending on gifted or sponsored subscriptions.
12. Ignoring the first 90 days.
13. Over-contacting after day 90.
14. Selling expertise at commodity prices; the retainer is the on-ramp, not the destination.
15. The treadmill: new MRR only replaces churned MRR, and growth stalls.

---

## 13. Lines for retainer conversations

Write your own one-line versions of these arguments and rehearse them:

- "We would rather sell you an outcome than a website."
- "The real work starts after launch."
- "A retainer only works if you are happy, so we have every reason to keep you happy."
- "Pricing is what lets us fund the rest."
- "The first 90 days set how much value you get from this."

---

## Sources

- Tzuo, Tien, with Gabe Weisert (2018) *Subscribed*, Portfolio. Informed the lifecycle operating model, recurring P&L presentation, and growth-lever and churn frameworks.
- Warrillow, John (2015) *The Automatic Customer*, Portfolio/Penguin. Informed the case for subscribers, churn-reduction tactics and methods for selling a recurring model.
