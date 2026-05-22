# Google AI Search Skill

Date: 2026-05-16

## Decision

Add `skills/seo-search/google-ai-search/` as the engine's official Google Search AI layer
for AI Overviews, AI Mode, AEO/GEO mythbusting, Search Console measurement,
local/ecommerce readiness, and agentic-experience preparation.

## Rationale

Google published a dedicated guide for optimizing websites for generative AI
features on Google Search, last updated 2026-05-15. The guidance is materially
different from much of the generic GEO advice online:

- Google AI Search work is still SEO because AI Overviews and AI Mode are rooted
  in core Search ranking and quality systems.
- `llms.txt`, AI text files, Markdown mirrors, chunking, special schema, and
  artificial fan-out page sets are not Google AI Search requirements.
- Non-commodity, people-first content and a clean technical Search foundation
  remain the durable work.

The repository already had broader AI-search and `llms.txt` guidance. This
decision separates Google-specific guidance from broader LLM visibility work so
operators do not sell non-Google tactics as Google requirements.

## Consequences

- Website briefs that mention Google AI visibility, AI Overviews, AI Mode,
  AEO/GEO, Search Console AI performance, or agentic readiness now route
  through `google-ai-search` before `seo` and `page-builder`.
- `seo` still owns implementation of metadata, schema, sitemaps, robots,
  hreflang, and Search Console setup.
- `llms.txt` remains an engine artifact for broader LLM handover and non-Google
  AI surfaces, but it must not be described as required for Google AI Overviews
  or AI Mode.
