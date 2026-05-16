---
name: google-ai-search
description: Use when optimizing, auditing, or planning a website for Google's generative AI features in Search, including AI Overviews and AI Mode. Applies official Google Search guidance, separates durable SEO work from AEO/GEO myths, and routes technical, content, local, ecommerce, measurement, and agentic-readiness work into the website engine.
---

# Google AI Search
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- A website must be prepared for Google's generative AI Search features,
  including AI Overviews and AI Mode.
- The work mentions Google AI search, AI Overviews, AI Mode, AEO, GEO, query
  fan-out, RAG, Search Console AI traffic, or Google agentic experiences.
- A client asks whether `llms.txt`, chunking, special schema, AI-specific pages,
  or off-site mention campaigns are needed for Google Search.
- Existing SEO/GEO recommendations need to be reconciled with official Google
  Search guidance.

## Do not use when
- The target is primarily ChatGPT, Perplexity, Claude, Bing, or a private RAG
  system; use `seo` and its broader AI-search references first.
- The task is only metadata, sitemap, hreflang, or schema implementation with
  no Google generative-AI decision involved; use `seo`.
- The user expects guaranteed inclusion in AI Overviews or AI Mode. Google
  does not guarantee crawling, indexing, serving, or AI-feature inclusion.

## Required inputs
- Target pages, page roles, business model, and primary user questions.
- Current SEO baseline: crawlability, indexability, snippets eligibility,
  canonical/hreflang state, internal links, JavaScript rendering risks, and
  duplicate-content risks.
- Search Console and analytics access when performance or diagnostics are in
  scope.
- Local business, ecommerce, Merchant Center, Google Business Profile, product
  feed, or Business Agent status when relevant.

## Workflow
1. Load `references/google-generative-ai-search-playbook.md` before making
   recommendations.
2. Start from the Google rule: generative AI features in Search are grounded in
   core Search ranking and quality systems, so the work is still SEO.
3. Audit content for non-commodity value: original experience, expert point of
   view, useful organization, high-quality media, and satisfaction for real
   visitors.
4. Reject manipulative AI-search tactics: query fan-out page factories,
   chunking for AI, special Google AI markup, inauthentic mentions, and
   structured-data overuse.
5. Audit technical readiness: crawlability, indexability, snippets eligibility,
   internal links, textual availability of important content, JavaScript SEO,
   page experience, and duplicate-content reduction.
6. For local and ecommerce sites, verify Google Business Profile, Merchant
   Center, product feeds, visible product/service details, and structured data
   consistency with visible content.
7. Decide content controls deliberately: use Googlebot controls for Search
   crawling, `nosnippet`/`data-nosnippet`/`max-snippet`/`noindex` for preview
   control, and Google-Extended only for non-Search AI training/grounding
   controls.
8. Measure through Search Console's Web performance reporting plus analytics
   outcomes such as conversions, engaged time, subscriptions, leads, or sales.
9. When browser agents or commerce agents matter, load
   `references/agentic-readiness.md` and produce an agent-readiness backlog.

## Quality standards
- Never present AEO/GEO hacks as Google requirements.
- Treat `llms.txt` as a broader engine/LLM artifact, not a Google AI Search
  requirement or ranking lever.
- Structured data must match visible page content and exist for rich-result
  eligibility, not as special AI Overview markup.
- Content recommendations must improve human usefulness first; AI visibility
  is a consequence of useful, crawlable, indexable content.
- AI-assisted content must meet Search Essentials, spam policies, and the
  same accuracy, quality, relevance, and disclosure bar as human-written work.

## Anti-patterns
- Creating many near-duplicate pages to capture every fan-out query variant.
- Breaking useful pages into unnatural fragments only for AI parsing.
- Rewriting copy into robotic answer blocks when the human page gets worse.
- Buying or manufacturing off-site mentions for perceived AI authority.
- Hiding weak content behind schema, Markdown files, or crawler files.
- Blocking Googlebot and expecting AI Overviews or AI Mode visibility.

## Outputs
- Google AI Search readiness audit.
- Content and technical implementation backlog.
- Mythbusting note for stakeholders.
- Search Console and analytics measurement plan.
- Local/ecommerce readiness checklist.
- Agentic-readiness backlog when relevant.

## References
- `references/google-generative-ai-search-playbook.md` - official Google
  Search guidance distilled into engine rules.
- `references/technical-readiness-checklist.md` - implementation checklist for
  crawlability, snippets eligibility, rendering, page experience, and duplicate
  control.
- `references/content-quality-gate.md` - non-commodity, people-first content
  review gate.
- `references/agentic-readiness.md` - optional browser-agent and commerce-agent
  preparation notes.
- `../seo/SKILL.md` - downstream implementation for metadata, schema, sitemaps,
  robots, hreflang, and Search Console setup.
- `../premium-commercial-writing/references/seo-ai-search-writing.md` - use
  when copy must be rewritten for usefulness, proof, entity clarity, and buyer
  intent.

## Notes
- This skill is source-aware: re-check Google's Search Central documentation
  before major client policy changes because the guidance can change.
- Preserve existing project behavior unless the current task explicitly
  requires a change.
