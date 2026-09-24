# Store Mode Diagnosis and Merchandising Signals

Parent skill: [ecommerce-analytics](../SKILL.md). Read when deciding whether a store's website and retention features should favour winning new buyers or keeping existing ones, when choosing between conversion rate and revenue per visitor as the target, or when reviewing on-site search failures and the balance between stock and sales.

This file complements [KPI framework](kpi-framework.md) (dashboard and revenue tree) and [analytics setup](analytics-setup.md) (events, CLV and RFM worksheets). Event names for search follow `retail-commerce-operating-system`. Formulas common to all models are in `../../../launch-ops/marketing-measurement-system/references/model-metric-definitions-and-lead-arithmetic.md`.

## 1. Diagnose the store's mode

A store earns mainly from new buyers (acquisition mode), from a mix (hybrid mode) or from repeat buyers (loyalty mode). The mode decides whether a points programme, a subscription feature or a referral flow is worth building. Diagnose it from the store's own data before recommending any loyalty feature.

### Procedure

1. **Clean the order data.** Exclude staff and test orders, cancelled orders, refused cash-on-delivery orders and failed mobile-money collections. Record the exclusions.
2. **Resolve identity.** Link orders to a customer key. For stores taking WhatsApp and mobile-money orders, the phone number is often the only stable key; record how duplicates were merged.
3. **Compute the 90-day repurchase rate** for each of the last two or three first-purchase cohorts: customers in the cohort who placed a second paid order within 90 days of their first ÷ customers in the cohort.
4. **Compute the annual repurchase rate** where at least two years of history exist: last year's buyers who bought again this year ÷ last year's buyers.
5. **Split by category and by channel** (web checkout, WhatsApp, marketplace). Modes can differ across categories.
6. **Classify** using the check bands below, and state confidence.

### Check bands

Croll and Yoskovitz (2013) report a heuristic from e-commerce consultant Kevin Hillstrom. It is one consultant's rule of thumb from mature United States stores, published more than a decade ago, and has not been verified for East African stores. Use it as a starting check, never as a target.

| Reported band | Annual repurchase | 90-day repurchase (early proxy) |
|---|---|---|
| Acquisition mode | below about 40% | about 1–15% |
| Hybrid mode | about 40–60% | about 15–30% |
| Loyalty mode | above about 60% | above about 30% |

Checks to run before relying on the classification:

- Do the last two or three cohorts fall in the same band? If not, report "mode unclear" and the range.
- Does the 90-day proxy agree with the annual rate where both exist?
- Is the store seasonal (gifts, school supplies, festive food)? Seasonal stores can look like acquisition mode while their customers return every year at the same time; compare same-season cohorts.
- Are repeat buyers moving to a channel the store cannot see (phone or WhatsApp orders not linked to the web account)? If so, the rate is understated.
- Is the result stable when a single large buyer is removed?

The book also reports that annual repurchase rarely moves by a large amount. Treat that as a caution: do not promise that a website feature will shift a store from one mode to another.

### What each mode means for the website

| Mode | Website and measurement priorities | Usually defer |
|---|---|---|
| Acquisition | First-order conversion, landing-page relevance per channel, revenue per visitor, delivery promise clarity, a post-delivery referral ask | Points programmes, account-heavy features |
| Hybrid | Service promises (delivery dates, returns), post-purchase messages, reorder shortcuts, second-order rate | Complex tiered loyalty |
| Loyalty | Accounts, saved baskets, reorder and subscription features, loyalty mechanics, retention cohorts | Heavy spend on cold acquisition pages |

**Handoff.** Budget split between acquisition and retention marketing, and the loyalty offer itself, belong to the digital-marketing engine (social-media-skills) and, for the business case, the business-plan engine. This skill hands over the mode diagnosis as a one-page note: cohorts used, rates, bands, confidence, exclusions and caveats. The receiving strategist owns the marketing decision.

## 2. Target revenue per visitor, not conversion alone

- **Revenue per visitor** = net revenue ÷ sessions. Net revenue excludes refunds, cancellations, refused cash-on-delivery orders and failed collections.
- It equals conversion rate × average order value. Report both factors when it moves.
- For any change that can affect order size (free-delivery thresholds, bundles, discounts, product recommendations, layout of category pages), make revenue per visitor the primary metric and conversion rate a diagnostic.
- Where margin data is available, margin per visitor is better still, because discounts can lift revenue while cutting profit.

Worked example (illustrative figures only). A Nairobi fashion store tests a free-delivery threshold. Conversion falls from 2.2% to 2.0%, but average order value rises from KES 3,000 to KES 3,600. Revenue per visitor rises from KES 66 to KES 72. Check delivery cost per order before calling it a win: if the added delivery cost exceeds the added margin, margin per visitor falls.

## 3. Review zero-result searches

On-site search shows what buyers want in their own words. A search that returns nothing is either a lost sale or a demand signal.

### Metrics

| Metric | Formula |
|---|---|
| Zero-result rate | searches returning no results ÷ all searches |
| Search exit rate | searches followed by leaving the site ÷ searches |
| Searcher conversion | orders from sessions with a search ÷ sessions with a search (compare with non-search sessions as a segment, not as proof that search causes purchase) |

Event: `search_zero_results`, with the query text, as defined in `retail-commerce-operating-system`. Strip personal data (phone numbers, names) from stored queries.

### Weekly review

1. Export the top zero-result queries by count.
2. Classify each query's cause and act:

| Cause | Example | Action |
|---|---|---|
| Spelling, synonym or local term | Brand nickname, Luganda or Swahili product name, British versus American spelling | Add synonyms; test the query again |
| Out of stock and hidden | Product exists but is excluded when out of stock | Show it with the restock date or an alternative |
| Not stocked | A product the store does not sell | Send to buying as a demand signal with query counts |
| Taxonomy or attribute gap | Search by size, colour or use that is not an attribute | Add the attribute or filter |
| Unclear intent | Very short or generic queries | Improve suggested searches and category links |

3. Record the zero-result rate each week and the fixes shipped. A falling rate after fixes is the evidence the review works.

## 4. Balance stock against sales

### Share-of-sales versus share-of-inventory

For each category, compare its share of sales with its share of inventory (at cost value or units; state which).

| Category | Share of sales | Share of inventory | Ratio (sales ÷ inventory) | Reading |
|---|---|---|---|---|
| Example A | 30% | 15% | 2.0 | Selling faster than stocked; check stock-outs and lost sales |
| Example B | 10% | 25% | 0.4 | Overstocked or under-promoted; check visibility before discounting |

Rules:

- Reconcile stock figures with the inventory system of record; the website's cached stock is not the source.
- A category with a high ratio and frequent stock-outs needs buying attention; record out-of-stock product views as lost demand.
- A category with a low ratio may be poorly placed on the site. Check its visibility (navigation position, search ranking, home-page slots) before recommending markdowns, which are a commercial decision for the client.

### Out-of-stock handling

- Demote out-of-stock items in category lists and search results, or show them with a restock date and an alternative.
- Track out-of-stock product views per week.
- Never show an item as available when stock is unconfirmed.

### Allocate page space by expected return

Home-page tiles, category-page slots and featured positions cost the same visitor attention. Stockwell and Shaw allocated printed catalogue space by expected revenue and reviewed each item's return against its space, using a three-to-one revenue-to-space-cost ratio as their planning rule. Adapt the logic rather than the ratio:

1. List the prominent slots (hero, featured products, category tiles).
2. Assign each slot an expected revenue or margin for the month, agreed with the client.
3. After the month, compare actual with expected.
4. Increase the space of items that beat expectation, maintain those near it, reduce those well below it.
5. Keep a slot for new products, and judge them over a longer window.

## 5. Monthly review checklist

- [ ] Mode diagnosis refreshed with the newest cohort; change in band noted.
- [ ] Revenue per visitor reported with conversion and average order value.
- [ ] Top zero-result queries classified; fixes and demand signals logged.
- [ ] Share-of-sales versus share-of-inventory table updated from the inventory system.
- [ ] Out-of-stock product views reported.
- [ ] Prominent slots reviewed against expected return.
- [ ] Exclusions, identity merges and data gaps stated.

## 6. Anti-patterns

| Anti-pattern | Correction |
|---|---|
| Recommending a loyalty programme without diagnosing mode | Run section 1 first |
| Treating the reported bands as targets | Use them as checks against the store's own cohorts |
| Celebrating a conversion rise while order value falls | Report revenue or margin per visitor |
| Ignoring what buyers search for | Weekly zero-result review |
| Discounting slow categories that are simply hard to find | Check visibility before markdowns |
| Promising a mode change from a website feature | State that annual repurchase moves slowly |

## Sources

- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics: Use Data to Build a Better Startup Faster*. O'Reilly Media. (Mode diagnosis citing Kevin Hillstrom, revenue per visitor, on-site search and zero-result searches, stock availability and share of sales versus share of inventory.)
- Stockwell, J. and Shaw, H. M. (1994) *Direct Marketing Checklists*. NTC Business Books. (Space allocation by expected revenue with review.)
