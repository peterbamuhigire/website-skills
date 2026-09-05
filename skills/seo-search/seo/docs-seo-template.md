---
site_url: ""
default_locale: ""
enabled_locales: []
default_og_image: ""
google_site_verification: ""
---

# Search Configuration and Evidence Map

Copy to the project documentation and complete it from approved sources. Blank
means unknown; do not replace missing facts with examples or assumptions.

## Ownership and currentness

| Field | Value |
|---|---|
| Business owner | |
| Search owner | |
| Canonical production origin | |
| Release/environment | |
| Markets and languages | |
| Fact source | |
| Verified on | |
| Review trigger/date | |

## URL and locale policy

Record trailing-slash, host, protocol, redirect, parameter, pagination,
canonical, hreflang, `x-default`, and sitemap rules. Include a route-equivalence
map for every translated page; localise slugs from native search and language
research rather than copying English paths.

## Entity facts

| Entity | Stable `@id` | Verified visible facts | Source/owner | Review date |
|---|---|---|---|---|
| Organisation | | | | |
| Website | | | | |
| Person | | | | |
| Product | | | | |
| Service | | | | |
| Genuine location | | | | |

Choose Schema.org types only after the entity and consumer are known.
`LocalBusiness` is not a fallback for online-only organisations. Omit unsupported
properties, ratings, credentials, prices, locations, and relationships.

## Page contract

Repeat for every indexable canonical page.

| Field | Value |
|---|---|
| Canonical route and locale | |
| Page type and primary job | |
| Audience and intent | |
| Unique accurate title | |
| Useful meta description | |
| H1 and section outline | |
| Primary entity | |
| Material claims and source IDs | |
| Original/practitioner value | |
| Candidate structured data and consumer | |
| Parent, sibling, evidence, and conversion links | |
| OG image and rights source | |
| Next useful action | |
| Analytics event | |
| Publication/substantive modification | |
| Review trigger | |

Preview title and description truncation in relevant surfaces, but use no rigid
character count. Do not force exact keywords, brand names, locations, or calls
to action where they reduce accuracy or readability.

## Crawler and AI controls

| Provider/user agent | Purpose | Allow/block/NA | Owner/source/date | Expected consequence | Review date |
|---|---|---|---|---|---|
| Google Search generative control | Search inclusion | | | | |
| Google-Extended | Non-Search AI use | | | | |
| OAI-SearchBot | ChatGPT search | | | | |
| GPTBot | Potential model training | | | | |
| Other verified provider | | | | | |

Keep search, potential training, and user-triggered agent access separate. Align
`robots.txt`, meta directives, Search Console, CDN, WAF, host, and authentication
controls.

## Webmaster and measurement

| Item | Property/location | Owner | Status/evidence | Limitation |
|---|---|---|---|---|
| XML sitemap | | | | |
| Google Search Console | | | | |
| Google generative AI report/control | | | | |
| Bing Webmaster Tools / AI Performance | | | | |
| IndexNow | | | | |
| Analytics and consent | | | | |
| CRM/offline reconciliation | | | | |

## Release checks

- [ ] Intended statuses, redirects, canonicals, index and snippet controls agree.
- [ ] Sitemaps contain canonical indexable URLs and truthful `lastmod` values.
- [ ] Reciprocal hreflang clusters and language switching use the same route map.
- [ ] Titles, descriptions, headings, links, and content match the page job.
- [ ] Structured data validates, matches visible facts, and has a current consumer.
- [ ] No FAQ/HowTo Google rich-result promise or special AI markup claim exists.
- [ ] Search, potential-training, and user-triggered crawler decisions are owned.
- [ ] Google/Bing reports and analytics are observed or `NOT_ASSESSED`.
- [ ] Accessibility, performance, security, forms, and failure states pass their gates.
- [ ] No indexing, ranking, citation, traffic, or conversion outcome is guaranteed.

Use the engine currentness register at
`docs/source-registers/search-ai-currentness-2026-09-05.json` for current shared
claims and create a project-local register for business facts.
