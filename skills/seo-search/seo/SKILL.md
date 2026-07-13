---
name: seo
description: Use when implementing website metadata, structured data, sitemaps, robots directives, canonical and hreflang signals, internal links, and search-facing content structure; use seo-audit for read-only diagnosis.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Seo
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Implement the approved search contract in website code and content without inventing business or schema facts.

<!-- dual-compat-start -->
## Use When

- Approved pages need search metadata and schema
- multilingual routes need canonical and hreflang implementation
- crawler-facing files and internal links must be built.

## Do Not Use When

- Use `seo-audit` to diagnose an existing site or `google-ai-search` for official Google AI feature guidance.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Approved route map, search intent, page content, entity facts, locale plan, and deployment URL rules | Strategy, content, client evidence, and build | yes | Implement accurate search signals | Stop when required entity or canonical facts are missing |

## Workflow

1. Validate routes, intent, entities, locales, and URL rules
2. Implement metadata, headings, schema, canonical/hreflang, sitemaps, robots, and internal links
3. Test rendered source and crawler artefacts
4. Stop on invented facts, invalid schema, or conflicting index signals, repair the source, then rerun checks.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Implemented search package | Crawlers, users, seo-audit, and release owner | Every indexable route has unique accurate signals, valid eligible schema, and tested crawler files |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Metadata inventory, schema validation, link and crawler checks | Release owner | Results map to the tested route and build |

<!-- dual-compat-end -->
## Capability Contract

Read, search, edit, and execution are required for authorised implementation. Network validation is optional before deployment; Search Console changes, production mutation, publication, and third-party account access require explicit authority.

## Degraded Mode

Fallback: without network, deployment URL, or validation tools, produce the narrowest qualified implementation, mark external checks `not assessed`, and do not claim indexing or rich-result eligibility.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Entity fact is verified and schema type is eligible | Implement the narrowest accurate schema | Misleading structured data |
| Route should not appear in search | Apply deliberate noindex and remove conflicting sitemap entry | Index-signal conflict |

## Quality Standards

- Use page-specific evidence, keep titles and descriptions truthful, validate schema, and align canonical, hreflang, robots, and sitemap signals.

## Anti-Patterns

- Copying one title across routes. Fix: write unique intent-aligned metadata.
- Adding schema properties the client cannot prove. Fix: omit unverified fields.
- Blocking a URL in robots while expecting noindex to be read. Fix: choose a coherent control.
- Adding hreflang without reciprocal routes. Fix: validate complete locale clusters.
- Claiming ranking improvement from implementation. Fix: report only implemented and measured outcomes.

## Worked Example

A legal service page lacks a verified aggregate rating. Implement `LegalService` facts the client can prove, omit rating properties, and record the missing evidence rather than fabricating stars.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- The task matches this domain: Comprehensive search engine optimization for multi-language static sites and AI visibility. Implements meta tags, JSON-LD structured data, E-E-A-T schema markup, multi-language sitemap generation, hreflang tags, robots.txt, crawler optimization (IndexNow, sitemap pinging), Google Analytics 4 via Partytown, Google Search Console verification, Bing Webmaster Tools, canonical URLs, and language-specific Open Graph tags. Covers traditional SEO and broader AI-search visibility. Use `google-ai-search` first for Google AI Overviews, AI Mode, AEO/GEO mythbusting, Bing AI Performance, and `llms.txt` claims. Supports 3 languages: English, French, Kiswahili. Reads from docs/{lang}/seo.md for per-page, per-language configuration. Generates language-specific sitemaps and SEO audit report. Run after page-builder, before deploy.
- The user needs an implementation-facing skill rather than a general discussion.
- The website content must work as a world-class marketing asset for the owner and as proof of premium website-development quality for the builder.

## Preserved Domain Exclusions
- The prerequisite upstream context is missing and the task is not yet execution-ready.
- Another narrower skill is the clear better fit for the exact subtask.

## Preserved Domain Inputs
- Project context, current files, and any constraints that affect implementation.
- Upstream artifacts produced by earlier skills when this skill is part of a pipeline.

## Preserved Domain Workflow
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. For premium or revenue-critical websites, align with `premium-website-product` so SEO is connected to buyer intent, authority content, conversion, launch distribution, and measurement.
5. When the task mentions Google AI Overviews, AI Mode, AEO/GEO, Bing AI
   Performance, Citation Share, `llms.txt`, UGC poisoning, or agentic readiness,
   run `google-ai-search` first and treat its output as an upstream input to SEO
   implementation.
6. Validate that the result stays compatible with the rest of the repository workflow.

## Preserved Domain Quality Guidance
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.
- Every enabled language must have SEO slugs written in that language, based on that language's search intent and keyword vocabulary. English slugs are not acceptable defaults for French, Kiswahili, or any other non-English version.
- Canonical URLs, internal links, hreflang tags, Open Graph URLs, and sitemap alternates must all use the same localized route map so search engines see clean equivalent URLs per language.
- Every money page must have a search intent, proof burden, CTA, internal-link target, schema requirement, and analytics event; metadata alone is not acceptable SEO.

## Preserved Domain Anti-Patterns
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not publish translated pages at English slug paths for convenience. Localize the slug, then wire language switching and sitemap alternates to the correct equivalent URL.

## Preserved Domain Outputs
- Implementation guidance, configuration, generated artifacts, or concrete follow-on steps.

## Mandatory deliverables (every project, every tier)

These artifacts MUST ship on every site this skill touches. They are the floor, not the ceiling.

### Schema.org JSON-LD — required set

Always emit on every relevant page (in addition to the foundational Organization, WebSite, BreadcrumbList):

1. **LocalBusiness** (or the most specific subtype: `MedicalBusiness`, `MedicalOrganization`, `Hospital`, `Dentist`, `Restaurant`, `Store`, `LegalService`, etc.) — with `address`, `geo`, `areaServed`, `telephone`, `openingHoursSpecification`, `sameAs` profiles, and `aggregateRating` when authentic reviews exist.
2. **Product** — for every distinct sellable offering (SaaS plan, package, physical good). Pair with **`Offer`** (price, priceCurrency, availability, url) and **`AggregateOffer`** when multiple price points exist.
3. **Service** — for every service line. Include `serviceType`, `provider`, `areaServed`, `hasOfferCatalog` enumerating the sub-services with their `Offer`s.
4. **FAQ content** — publish useful, visible answers when buyers need them. Do not require `FAQPage` for Google: Google ended the FAQ rich-result feature on 7 May 2026 and removed its documentation in June 2026. Use `FAQPage` only for a documented non-Google consumer and keep markup aligned with visible content.
5. **SoftwareApplication / MobileApplication / WebApplication** — for any software product, with `applicationCategory`, `operatingSystem`, `offers`, `featureList`.
6. **Article / NewsArticle / BlogPosting** — on every editorial page, with `author` (Person with `sameAs`), `publisher` (Organization with `logo`), `datePublished`, `dateModified`, `image`.
7. **Person** — for every named author/founder/expert, with `jobTitle`, `worksFor`, `sameAs` (LinkedIn, scholar, professional registries), `knowsAbout`, `alumniOf` where appropriate.
8. **Review / AggregateRating** — when authentic reviews exist (never synthesised).
9. **Industry-specific subtypes** when the business fits: `Hospital`, `MedicalClinic`, `Pharmacy`, `Dentist`, `LegalService`, `FinancialService`, `EducationalOrganization`, `LodgingBusiness`, `TouristAttraction`, etc. Pick the narrowest type that fits.

Validate the resulting JSON-LD with the Schema.org validator and Google's Rich Results Test before sign-off.

### AI / LLM crawler entry files - optional handover artifacts, not AI-ranking requirements

These files are optional, client-specific handover artifacts. Google's official
guidance says `llms.txt`, AI text files, Markdown mirrors, and special markup are
not required to appear in AI Overviews or AI Mode, and current field data shows
very low AI-search crawler demand for `llms.txt`. Do not sell these files as
Google, Bing, ChatGPT, Claude, Perplexity, or Gemini ranking levers.

Generate them only when the client, CMS, documentation workflow, or project
handover contract explicitly benefits from a plain-text knowledge artifact:

1. **`/llms.txt`** - Markdown file (~2-4 KB) following the [llmstxt.org](https://llmstxt.org) spec: H1 site name, blockquote summary, then linked sections (Docs, Products, Services, Policies, Contact). Treat as a convenience file, not an SEO lever.
2. **`/llms-full.txt`** - Concatenated full-text of the most important pages (home, about, services/features, pricing, FAQ, contact, key blog cornerstones), 20-60 KB. Plain prose, no nav chrome, includes structured fact blocks (NAP, hours, prices, supported regions).
3. **`/robots.txt`** - Always required. State the search crawler policy clearly, reference all language sitemaps and the index sitemap, and do not block AI crawlers unless the client has explicitly opted out in writing.
4. **`/.well-known/security.txt`** on every site. RFC 9116 requires `Contact`
   and `Expires`; this engine also requires `Canonical` and `Policy` so
   vulnerability reports have a clear owner and disclosure route.

If `llms.txt` or `llms-full.txt` are generated, regenerate them on every content
change so they cannot become stale or contradict the HTML site.

### Other required artifacts

- Per-language XML sitemaps + sitemap-index.xml, ping submitted via IndexNow on deploy.
- Canonical URLs and `hreflang` (including `x-default`) on every page.
- OpenGraph + Twitter card metadata, language-localised, with a real OG image (not a placeholder).
- Favicons: 16, 32, 180 (apple-touch), 192, 512.
- Per-page metadata authored in the project language, never machine-translated from English.
- Google Search Console and Bing Webmaster Tools verification, with Bing AI
  Performance/Citation Share reviewed when the property exposes it.

## Preserved Domain References
- `references/premium-seo-package.md` — the default SEO package delivered on every Growth/Authority engagement. Strategy-first SEO, intent map, metadata, schema, internal linking, GEO/AI visibility, local SEO, measurement.
- `../google-ai-search/SKILL.md` — use before this skill when Google AI
  Overviews, AI Mode, AEO/GEO mythbusting, Search Console AI performance, or
  agentic readiness is in scope.
- `../premium-commercial-writing/references/seo-ai-search-writing.md` — use when SEO/GEO work needs stronger content structure, answer blocks, entity clarity, E-E-A-T notes, and AI-citable facts before implementation.
- `../premium-commercial-writing/references/blog-and-authority-writing.md` — use when SEO depends on articles, pillar pages, clusters, or sales-enablement content rather than metadata alone.
- `../premium-website-product/references/premium-website-market-asset-gate.md` - use when SEO must support premium website positioning, content authority, launch distribution, and agency proof.
- `references/analytics-event-map.md` — minimum instrumentation for every site: event taxonomy, conversion goals, UTM convention, attribution model, consent, pre-launch checklist.
- `references/seo-topic-and-intent-map.md` — align search intent with page roles, proof burdens, CTA posture.
- `references/conversion-intent-and-launch-seo.md` — use when SEO work must support content clusters, launch windows, conversion-aware metadata, or state changes between prelaunch, open, and closed offers.
- `references/legacy-guidance.md` — preserved detailed instructions from the previous skill version.
- `references/llms-txt-and-ai-crawlers.md` — optional format and templates for `llms.txt`, `llms-full.txt`, AI-crawler robots rules, and per-page AI-citability hooks.
- `references/required-schema-catalog.md` — concrete JSON-LD templates for active schema types and the retired Google FAQ rich-result note, with multi-language examples.
