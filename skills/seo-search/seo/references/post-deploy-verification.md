# Post-Deploy Search Verification

Parent skill: [`../SKILL.md`](../SKILL.md)

Use after an authorised deployment. Verification is read-only unless the owner
separately authorises webmaster-tool changes, IndexNow submission, or production
configuration changes.

## Current submission model

Do not call unauthenticated Google, Bing, or Yandex sitemap “ping” endpoints.
Google's sitemap ping endpoint is deprecated and returns `404`; Google reported
that Bing also found unauthenticated sitemap submissions unhelpful.

Use supported mechanisms:

- expose a valid sitemap or sitemap index at a stable canonical URL;
- reference it in `robots.txt`;
- submit it in Google Search Console or through the authorised Search Console
  API when the owner wants processing/error visibility;
- submit or import it in Bing Webmaster Tools;
- send added, updated, or removed canonical URLs through IndexNow when supported;
- use truthful sitemap `lastmod` values only for significant content changes.

Submission is a discovery hint, not an indexing, ranking, or citation guarantee.

## Verification sequence

### 1. Resolve the release identity

Record deployment ID or commit, environment, canonical origin, release time,
route inventory, locale map, and rollback owner. Stop if the tested build cannot
be tied to the released artefact.

### 2. Check representative routes

Sample every route and intent family, including home, product/service, article,
location, locale alternates, conversion paths, redirects, expected 404s, and any
deliberately excluded pages.

For each sample record:

- final status and redirect chain;
- canonical URL and index directive;
- rendered title, description, H1, and primary content;
- internal-link discovery path;
- reciprocal hreflang and `x-default` decision where applicable;
- structured-data syntax, visible-content match, and consumer eligibility;
- mobile, accessibility, security, and performance gate result.

### 3. Check crawler artefacts

- `robots.txt` returns `200`, contains the intended rules, and references the
  actual sitemap location;
- sitemap files return `200`, parse as XML, contain canonical indexable URLs,
  and exclude redirects, errors, blocked pages, and deliberate `noindex` URLs;
- `lastmod` reflects significant source changes rather than deployment time;
- canonical, sitemap, internal links, hreflang, Open Graph URLs, and redirects
  agree on URL form;
- CDN, WAF, host, and authentication rules do not contradict crawler policy.

### 4. Check webmaster evidence

When authorised access exists:

- verify property ownership and submitted sitemap state in Google Search Console
  and Bing Webmaster Tools;
- inspect priority URLs rather than assuming submission means indexing;
- record exclusions, canonical selection, crawl/render findings, and processing
  errors with observation dates;
- inspect Google's dedicated generative AI performance report and inclusion
  control where relevant;
- inspect Bing AI Performance when available, preserving its public-preview and
  interpretation limits.

Without account access, mark these checks `NOT_ASSESSED`.

### 5. Send change notifications

IndexNow is appropriate for canonical URLs that were added, materially updated,
or removed. Use the provider's current endpoint, key format, batch limits, and
verification method. Submit once per change event; do not repeatedly resubmit in
an attempt to force indexing.

Record request time, URL count, response, failed URLs, retry decision, and the
deployment that generated the set. Protect keys as operational credentials and
do not embed them in client-side code or logs.

### 6. Connect visibility to outcomes

Validate analytics and consent before interpreting traffic. Track conventional
search, Google generative-AI impressions, Bing citations/grounding queries,
ChatGPT referrals carrying `utm_source=chatgpt.com`, and downstream qualified
outcomes as separate measures. Do not infer conversion, citation support, or
ranking from crawler activity.

## Acceptance evidence

| Evidence | Pass condition |
|---|---|
| Release identity | Tested routes map to the released artefact |
| Route sample | Intended statuses, canonicals, index controls, content, and links agree |
| Sitemap and robots | Valid, reachable, internally coherent, and source-controlled |
| Structured data | Valid syntax, visible fact match, and current consumer interpretation |
| Webmaster tools | Observed state recorded, or explicitly `NOT_ASSESSED` |
| IndexNow | Only changed canonical URLs submitted; responses and failures logged |
| Outcome telemetry | Consent-aware events tested without invented performance claims |
| Rollback | Owner and trigger recorded for release-critical regressions |

## Failure handling

- Roll back or block promotion on accidental `noindex`, canonical-to-error,
  robots denial, broken locale cluster, widespread 5xx, or missing priority
  content.
- Repair generated sitemap and source URL maps instead of hand-editing build
  output.
- Re-run affected checks plus one unaffected regression sample.
- Preserve unavailable external checks as `NOT_ASSESSED`; never convert delay or
  absent data into a pass.

## Current sources

- Google sitemap submission and construction:
  https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Google sitemap ping deprecation:
  https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping
- Bing sitemap guidance:
  https://www.bing.com/webmasters/help/Sitemaps-3b5cf6ed
- IndexNow protocol documentation:
  https://www.indexnow.org/documentation
- Claim-level evidence record:
  [`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json)
