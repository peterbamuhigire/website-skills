# Technical Readiness Checklist

Use this checklist when auditing implementation readiness for Google's
generative AI Search features.

## Eligibility

- [ ] Page is intended for public Google Search visibility.
- [ ] Page returns HTTP 200.
- [ ] Page is not blocked by robots.txt, CDN rules, authentication, firewall, or
  host-level bot controls.
- [ ] Page is not `noindex`.
- [ ] Page is eligible to show a snippet unless there is a deliberate business
  reason to restrict snippets.
- [ ] Canonical tag points to the intended URL.
- [ ] URL appears in the XML sitemap where appropriate.
- [ ] Page can be discovered through internal links, not only sitemap discovery.

## Content Availability

- [ ] Main answer, product/service facts, price posture, location, and contact
  information are available as text.
- [ ] JavaScript-rendered content is visible to Googlebot in URL Inspection.
- [ ] Lazy-loaded content has crawlable fallbacks where needed.
- [ ] Critical images have descriptive context and useful alt text when
  appropriate.
- [ ] Video has visible summary text or transcript where the information matters.

## Structure

- [ ] One clear H1.
- [ ] H2/H3 hierarchy matches the page's human reading path.
- [ ] Internal links connect the page to parent, sibling, and conversion pages.
- [ ] Structured data matches visible page content.
- [ ] Duplicate, filtered, and low-value URL variants are canonicalized,
  noindexed, or removed.

## Page Experience

- [ ] Mobile rendering is complete and usable.
- [ ] Main content is easy to distinguish from ads, promos, and navigation.
- [ ] Core Web Vitals are monitored in Search Console.
- [ ] Intrusive popups or interstitials do not block the main task.
- [ ] Forms and CTAs work for visitors arriving from Search.

## Controls

- [ ] Googlebot access is intentionally allowed or blocked.
- [ ] `nosnippet`, `data-nosnippet`, `max-snippet`, and `noindex` are used only
  where the business accepts the visibility tradeoff.
- [ ] Google-Extended decisions are documented separately from Google Search
  crawling decisions.

## Evidence

- [ ] Search Console property verified.
- [ ] URL Inspection confirms Googlebot sees the intended content.
- [ ] Sitemap submitted and accepted.
- [ ] Analytics events connect Search visits to meaningful outcomes.
