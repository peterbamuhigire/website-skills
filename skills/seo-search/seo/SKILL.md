---
name: seo
description: Use when implementing cross-platform search and AI-answer discoverability, including metadata, entity presence, structured data, sitemaps, crawler controls, canonicals, hreflang, internal links, answer clarity, and referral measurement; use seo-audit for read-only diagnosis.
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
- crawler-facing files and internal links must be built
- cross-platform ChatGPT, Bing, or other AI-answer discoverability needs entity
  consistency, crawler controls, answer clarity, and referral measurement.

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
- The task matches this domain: comprehensive search implementation for multilingual static sites and AI-answer discoverability. It covers metadata, evidence-backed JSON-LD, sitemaps, hreflang, robots and snippet controls, IndexNow where supported, analytics, Search Console, Bing Webmaster Tools, canonical URLs, internal links, and localised social metadata. Use `google-ai-search` first for Google AI Overviews, AI Mode, AEO/GEO mythbusting, generative AI reporting, or Google inclusion controls. Read `ai-seo-optimization.md` for the cross-platform layered model. Run after page-builder and before deploy.
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
   Performance, generative AI reporting, `llms.txt`, UGC poisoning, or agentic readiness,
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

These artefacts form the default implementation floor. Apply them only where
the page, business model, locale plan, and verified evidence support them.

### Schema.org JSON-LD — required set

Select only types and properties supported by visible, verified facts. Sitewide
entities may be referenced by stable `@id`; they need not be duplicated on every
page. Page-type candidates include:

1. **Organization** and **WebSite** for the actual publisher and site.
2. **BreadcrumbList** on non-home pages with visible breadcrumb context.
3. **LocalBusiness** or a narrower subtype only for a genuine customer-serving location; include only verified location, hours, contact, service area, profile, and review facts.
4. **Product** and **Offer/AggregateOffer** when the page exposes a real sellable product and current offer facts.
5. **Service** when the visible page describes a real service and provider.
6. **FAQ content** when buyers need it. Google stopped showing FAQ rich results on 7 May 2026; use `FAQPage` only for a documented non-Google consumer.
7. **SoftwareApplication / MobileApplication / WebApplication** for a real software product with verified compatibility, feature, and offer facts.
8. **Article / NewsArticle / BlogPosting** for matching editorial pages, with truthful authorship and publication/modification dates.
9. **Person**, **Review**, and **AggregateRating** only when the page and evidence support the represented person or authentic review data.

Validate the resulting JSON-LD with the Schema.org validator and Google's Rich Results Test before sign-off.

### AI / LLM crawler entry files - optional handover artifacts, not AI-ranking requirements

These files are optional, client-specific handover artifacts. Google's official
guidance says `llms.txt`, AI text files, Markdown mirrors, and special markup are
not used to improve Google Search visibility. Do not sell these files as
Google, Bing, ChatGPT, Claude, Perplexity, or Gemini ranking levers.

Generate them only when the client, CMS, documentation workflow, or project
handover contract explicitly benefits from a plain-text knowledge artifact:

1. **`/llms.txt` or `/llms-full.txt`** — generated, versioned text indexes only for a named consumer or workflow; no fixed size or content quota.
2. **`/robots.txt`** — required crawler policy. Record search, potential-training, and user-triggered agent decisions separately and align them with CDN/WAF controls.
3. **`/.well-known/security.txt`** on every site. RFC 9116 requires `Contact`
   and `Expires`; this engine also requires `Canonical` and `Policy` so
   vulnerability reports have a clear owner and disclosure route.

If `llms.txt` or `llms-full.txt` are generated, regenerate them on every content
change so they cannot become stale or contradict the HTML site.

### Other required artifacts

- Valid XML sitemap coverage, using per-language sitemaps or one suitable sitemap design; reference it in `robots.txt` and submit it through supported webmaster tooling.
- IndexNow notifications for added, updated, or removed canonical URLs when supported; do not call this a sitemap ping or indexing guarantee.
- Canonical URLs on every indexable page and complete reciprocal `hreflang` clusters, including a deliberate `x-default` where appropriate.
- OpenGraph + Twitter card metadata, language-localised, with a real OG image (not a placeholder).
- Favicons: 16, 32, 180 (apple-touch), 192, 512.
- Per-page metadata authored in the project language, never machine-translated from English.
- Google Search Console and Bing Webmaster Tools verification. Review Google's
  generative AI report and control plus Bing AI Performance when the property
  exposes them, using only currently documented dimensions.

## Preserved Domain References
- `references/ai-seo-optimization.md` — layered SEO, AEO, GEO, entity-presence,
  crawler-governance, SXO, and cross-platform measurement doctrine.
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
