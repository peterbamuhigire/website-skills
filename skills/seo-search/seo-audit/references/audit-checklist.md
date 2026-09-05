# Search and AI Discoverability Audit Checklist

Parent skill: [`../SKILL.md`](../SKILL.md)

Use this as an evidence checklist, not a scoring shortcut. Sample every route,
intent, locale, template, and conversion family. Record observed facts,
inference, inaccessible evidence, and `NOT_ASSESSED` checks separately.

## 1. Scope and baselines

- [ ] Canonical origin, environments, markets, languages, business outcomes,
      priority tasks, and comparison period are defined.
- [ ] Route inventory and page-type sample are reproducible.
- [ ] Search Console, Bing, analytics, CRM, server-log, and crawl evidence list
      access dates, owners, definitions, and gaps.
- [ ] Release, migration, seasonality, campaign, demand, and platform changes
      are logged before causal interpretation.

## 2. Availability and index eligibility

- [ ] Priority URLs return the intended status and redirect chain.
- [ ] Robots, authentication, CDN, WAF, host, `noindex`, snippet, canonical,
      sitemap, and internal-link signals agree.
- [ ] Canonicals are absolute, successful, indexable, and consistent with links,
      sitemaps, hreflang, and rendered metadata.
- [ ] Important content is available in rendered semantic HTML and is not
      trapped only in images, video, canvas, blocked scripts, or gated widgets.
- [ ] Parameter, filter, duplicate, staging, and alternate-host URLs have an
      intentional policy.
- [ ] Sitemaps contain canonical indexable URLs and truthful significant-change
      `lastmod` values; deprecated ping endpoints are absent.

## 3. Intent and information architecture

- [ ] Every priority page has a primary audience, task, intent, proof burden,
      internal-link role, next action, and measurement event.
- [ ] Page splits represent materially different needs, not keyword variants.
- [ ] Navigation and internal links expose priority pages without relying only
      on a sitemap or site search.
- [ ] Orphans, dead ends, duplicate paths, and incompatible mixed intents are
      identified with business impact.
- [ ] Multilingual routes use native research, localised slugs, reciprocal
      hreflang, coherent canonicals, and equivalent-page switching.

## 4. Page presentation and content

- [ ] Titles, descriptions, H1s, headings, body, links, and media describe the
      page accurately without keyword quotas or stuffing.
- [ ] The page gives the shortest complete answer appropriate to the task and
      preserves conditions, exceptions, jurisdiction, dates, and limitations.
- [ ] Definitions, comparisons, procedures, and tables exist only where they
      help users; no artificial chunking or question-heading quota is present.
- [ ] Original experience, data, examples, specifications, methodology, or
      useful synthesis distinguishes the page from commodity summaries.
- [ ] Authorship, publication, substantive modification, sources, and review
      responsibility are truthful where relevant.
- [ ] AI-assisted content meets the same accuracy, originality, spam, safety,
      and usefulness bar as other content.

## 5. Evidence and entity presence

- [ ] Material factual and commercial claims map to current primary evidence or
      named first-hand evidence with scope and limitations.
- [ ] Organisation, person, product, service, location, contact, policy, and
      offer facts are consistent across owned pages and legitimate profiles.
- [ ] Reviews, ratings, credentials, partnerships, client names, statistics,
      and dates are authentic and approved.
- [ ] Wikipedia, forums, directories, reviews, and social platforms are not
      treated as controllable promotional profiles or manufactured authority.
- [ ] Stale or conflicting public facts have an owner and correction route.

## 6. Structured data

- [ ] JSON-LD syntax and vocabulary validate.
- [ ] Types and properties match visible, verified facts and stable entity IDs.
- [ ] Google rich-result eligibility is checked only for currently supported
      types; Schema.org validity is not misreported as Google eligibility.
- [ ] Google HowTo and FAQ rich-result promises are absent.
- [ ] `FAQPage` exists only for a documented non-Google consumer.
- [ ] Warnings are triaged by consumer and context; missing facts are not
      invented to make a validator green.

## 7. Media, performance, accessibility, and security

- [ ] Images and video add information, have appropriate alternatives or
      transcripts, use responsive delivery, and preserve rights/provenance.
- [ ] Real-user LCP, INP, and CLS are assessed where field data exists;
      laboratory tests are labelled separately.
- [ ] Mobile and desktop task completion, focus, forms, errors, consent, and
      content visibility are tested.
- [ ] HTTPS, headers, dependencies, secrets, abuse controls, uptime, and failure
      behaviour pass their owning quality gates.
- [ ] Performance or accessibility failures are not hidden by an aggregate SEO
      score.

## 8. Local and commerce discovery

- [ ] Real locations or service areas, hours, contacts, categories, products,
      prices, availability, shipping, and returns are current across page,
      profile, feed, and schema.
- [ ] Location pages provide genuine local value and are not doorway variants.
- [ ] Business-profile and merchant accounts have organisation ownership,
      least-privilege access, update procedures, and review-response governance.
- [ ] Local or commerce feature availability is verified for the target market.

## 9. Crawler and AI controls

- [ ] Search inclusion, potential model training, and user-triggered agent access
      are separate owner decisions.
- [ ] Every named bot and IP range is checked against current first-party
      documentation.
- [ ] OpenAI `OAI-SearchBot`, `GPTBot`, and `ChatGPT-User` are not conflated.
- [ ] Google Search generative-AI control, inheritance, and `Google-Extended`
      decision are recorded separately.
- [ ] Optional `llms.txt` artefacts have a named consumer, generation owner, and
      no unsupported ranking or citation promise.

## 10. Conventional and generative visibility

- [ ] Conventional search is analysed by comparable period, page family, query
      class, country, and device with reporting limitations.
- [ ] Google's dedicated generative AI impressions report is reviewed by page,
      country, device, and date where sufficient data exists.
- [ ] Bing AI Performance uses its current public-preview definitions and does
      not call citations a rank or authority metric.
- [ ] Assistant observations use versioned prompt sets, paraphrases, controls,
      repeated runs, logged context, and human citation-support review.
- [ ] Discovery, retrieval, citation, prominence, factual contribution, fidelity,
      referral, and business outcome remain separate measures.

## 11. SXO and business outcomes

- [ ] Search-result or AI-citation promise matches the landing-page message.
- [ ] Visitors can identify fit, evidence, limitations, next action, and what
      happens after acting.
- [ ] Forms request necessary data, expose labels/states/errors, confirm success,
      and respect privacy and consent.
- [ ] Qualified enquiries, task success, lead quality, revenue, retention,
      satisfaction, or public-service outcomes are defined by the business.
- [ ] No universal bounce, time, conversion, ranking, growth, or payback target
      substitutes for the project's baseline and decision band.

## 12. Finding record

Each finding includes URL/template, observation, evidence locator and date,
severity, business impact, confidence, owner, dependency, correction, rollback,
acceptance test, and retest date. Missing account, field, render, or production
evidence stays `NOT_ASSESSED`.

## Currentness

Use the claim register at
[`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json)
and rerun `scripts/validate-search-doctrine.py` before release.
