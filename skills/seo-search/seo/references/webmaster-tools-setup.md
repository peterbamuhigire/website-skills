# Webmaster Tools Setup and Governance

Parent skill: [`../SKILL.md`](../SKILL.md)

Use this reference to specify or verify Google Search Console, Bing Webmaster
Tools, business-profile, and change-notification setup. Account creation,
verification, property controls, API credentials, submissions, and profile edits
require explicit owner authority.

## Inputs

- canonical production origin and URL policy;
- domain and DNS owner;
- organisation and account owner;
- approved administrators and least-privilege roles;
- sitemap location and release identity;
- target countries, languages, products, services, and genuine locations;
- analytics, consent, CRM, and retention rules;
- crawler and generative-AI inclusion decisions.

Stop if ownership, production origin, or authorised account is unclear.

## Google Search Console

### Property design

- Prefer a Domain property when the authorised owner can verify DNS and needs
  coverage across protocols and subdomains.
- Add URL-prefix properties only for a documented operational reason.
- Keep ownership with the client or organisation, not a departing contractor.
- Grant the minimum role needed and require protected accounts and recovery.

### Verification and sitemap

Use a current supported verification method. Treat DNS propagation and report
population as variable; record observation times instead of promising a fixed
delay.

Submit the canonical sitemap or sitemap index through the Sitemaps report or the
authorised API. Also reference it in `robots.txt`. Submission is a hint and does
not guarantee crawling, indexing, ranking, or generative-AI inclusion.

### Core reports

Review by comparable date range and route/query family:

- Page indexing and sitemap processing;
- URL Inspection for representative priority pages;
- Search performance: clicks, impressions, CTR, position, queries, pages,
  countries, and devices;
- Core Web Vitals field groups, with page-level laboratory diagnostics as
  supporting evidence;
- security, manual-action, and enhancement reports when applicable.

Do not treat an absent report, insufficient data, or inaccessible property as a
pass.

### Generative AI controls and reporting

As of 31 August 2026, Search Console provides:

- a dedicated generative AI performance report for AI Overviews and AI Mode,
  exposing impressions by page, country, date, and device; and
- a property-level include/exclude control for Search generative AI features,
  with parent-property inheritance.

Record control state, inheritance, owner, decision date, reason, expected
consequence, and review date. This control is separate from `Google-Extended`,
which addresses certain non-Search generative AI training and grounding uses.

The report does not provide a universal ranking, prompt list, citation-fidelity
assessment, or business outcome. Pair it with normal Search performance,
analytics, and CRM evidence.

## Bing Webmaster Tools

Verify the canonical property through a currently supported method or authorised
Google Search Console import. Submit the sitemap, inspect representative URLs,
review crawl/index findings, and use Site Scan where its scope fits.

### AI Performance public preview

Microsoft's 10 February 2026 announcement documents:

- total citations;
- average unique cited pages per day;
- sampled grounding queries;
- page-level citation activity; and
- visibility trends.

These measures do not establish rank, authority, placement, factual contribution,
or conversion. Preserve the public-preview label and source date. Pair citation
activity with human claim-support review and downstream outcomes.

## IndexNow

Use IndexNow when the CMS or deployment can reliably emit canonical URLs that
were added, materially updated, or removed.

- follow the current protocol, endpoint, key, batch, and status guidance;
- keep keys out of client-side code, public logs, and repositories unless the
  protocol explicitly requires a public verification file;
- deduplicate URLs and submit only the changed canonical set;
- log deployment, request time, count, response, failures, and retry decision;
- do not repeatedly submit unchanged URLs or promise indexing/citation speed.

IndexNow notifies participating engines of changes. It complements rather than
replaces crawlable links, sitemaps, quality, and index eligibility.

## Local business profiles

Create or change a Google Business Profile or Bing Places listing only for a
real eligible organisation/location and with owner approval.

- use the verified legal/trading name, address or service area, contact details,
  categories, hours, products/services, and media;
- keep the website, page content, profile, feeds, and structured data consistent;
- do not create virtual, duplicate, keyword-stuffed, or review-manipulated
  listings;
- define ownership, response, update, closure, and incident procedures;
- verify platform eligibility and feature availability for the target market.

## Measurement contract

| Stage | Source | Measure | Limitation |
|---|---|---|---|
| Crawl/index | Search Console, Bing tools, server logs | states, errors, canonical selection, processing | Submission is not indexing |
| Conventional search | Search Console and Bing | impressions, clicks, queries, pages, position | Aggregation and privacy limits apply |
| Google generative Search | Dedicated Search Console report | impressions by page, country, device, date | No prompt, rank, or fidelity measure |
| Microsoft AI surfaces | Bing AI Performance | citations, cited pages, sampled grounding queries, trends | Public preview; not rank or business value |
| Referral | consent-aware analytics | source/medium, landing page, qualified actions | Referrer and UTM coverage can be incomplete |
| Business outcome | CRM, commerce, operations | qualified leads, sales, retention, support impact | Attribution requires reconciliation |

Targets come from the project's baseline, strategy, economics, and decision
bands. Do not insert universal month-on-month growth percentages, review quotas,
bounce-rate thresholds, or indexing timelines.

## Handover record

- property and canonical origin;
- verification method without exposing secrets;
- organisation owner and least-privilege users;
- sitemap and robots locations;
- generative-AI control and inheritance state;
- crawler/training policy owner;
- configured reports and exports;
- analytics/CRM handoff and consent basis;
- open defects and `NOT_ASSESSED` checks;
- review and credential-rotation dates;
- recovery process for account loss or agency offboarding.

## Current sources

- Google Search Console documentation: https://support.google.com/webmasters/
- Google sitemap guidance:
  https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Google generative AI performance report:
  https://support.google.com/webmasters/answer/16984139
- Google Search generative AI control:
  https://support.google.com/webmasters/answer/16908024
- Bing AI Performance announcement:
  https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
- Bing sitemap guidance:
  https://www.bing.com/webmasters/help/Sitemaps-3b5cf6ed
- IndexNow documentation: https://www.indexnow.org/documentation
- Claim-level evidence record:
  [`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json)
