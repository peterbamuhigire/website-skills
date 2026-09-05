---
name: google-ai-search
description: Use when a website brief promises Google AI Overviews, AI Mode, AEO/GEO, Search Console AI measurement, local or ecommerce AI readiness, or agentic experience preparation; use seo for implementation after guidance.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Google AI Search
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Translate current official Google Search guidance into qualified website requirements without promising AI feature inclusion.

<!-- dual-compat-start -->
## Use When

- A brief mentions AI Overviews, AI Mode, AEO, GEO, agentic search, or Search Console AI reporting
- claims need official-source verification.

## Do Not Use When

- Use `seo` for routine implementation or unsupported tactics that claim guaranteed AI citations.
- Use `seo` for cross-platform ChatGPT, Bing, entity-presence, crawler-control,
  or referral-measurement implementation after platform guidance is settled.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Specific AI-search claim, target market, website type, existing search plan, and current official Google sources | Brief, client, and verified official documentation | yes | Separate supported requirements from myths | Stop when current official guidance cannot be verified |

## Workflow

1. Frame the claim and verify current official Google sources
2. Distinguish standard search requirements, feature-specific availability, measurement limits, and unsupported AEO/GEO claims
3. Produce qualified requirements for content, entities, commerce/local data, and agentic readiness
4. Stop on unverifiable or guaranteed-outcome language, recover by narrowing the claim, then hand implementation to seo.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Google AI Search guidance brief | SEO, content, commerce, local, and measurement owners | Every recommendation cites current official guidance and labels availability or measurement limits |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Official-source register and claim disposition table | Client and release owner | Each claim is supported, rejected, or marked not assessed with source date |

<!-- dual-compat-end -->
## Capability Contract

Read, search, and network verification are required for current guidance. Planning is read-only by default. Website edits, Search Console changes, publication, spending, and account access require explicit authority.

## Degraded Mode

Without network or current official sources, return the narrowest qualified list of questions and stable principles, mark current feature claims `not assessed`, and do not provide tactical certainty.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Claim is supported by current official guidance | Translate it into a testable requirement | Speculative AEO tactic |
| Brief promises inclusion or ranking | Remove the guarantee and state controllable work | Misleading commercial claim |

## Quality Standards

- Use official Google sources for current claims, cite at point of recommendation, distinguish availability by market, and never guarantee inclusion or ranking.

## Anti-Patterns

- Presenting AEO as a separate technical standard. Fix: map work to documented Search fundamentals and specific eligible features.
- Guaranteeing an AI Overview citation. Fix: state controllable quality and eligibility work only.
- Using a third-party blog as authority for Google behaviour. Fix: verify against official documentation.
- Claiming Search Console exposes unavailable AI detail. Fix: document actual measurement limits.
- Reusing stale feature availability. Fix: verify market and date before advising.

## Worked Example

If a proposal guarantees AI Overview placement, replace it with a scoped programme for crawlability, helpful content, entity clarity, merchant or local data, and measurement, citing current official Google guidance.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- A website must be prepared for Google's generative AI Search features,
  including AI Overviews and AI Mode.
- The work mentions Google AI search, AI Overviews, AI Mode, AEO, GEO, query
  fan-out, RAG, Search Console AI traffic, or Google agentic experiences.
- A client asks whether `llms.txt`, chunking, special schema, AI-specific pages,
  off-site mention campaigns, Reddit/UGC placement, or "AI citation hacks" are
  needed for Search or AI assistants.
- The work needs Google generative AI reporting or Bing Webmaster Tools AI
  Performance measures such as citations, cited pages, grounding queries, or
  page-level activity.
- The work involves brand-safety risk from user-generated content, poisoned
  snippets, weak sources, fabricated citations, or volatile ranking updates.
- Existing SEO/GEO recommendations need to be reconciled with official Google
  Search guidance.

## Preserved Domain Exclusions
- The target is primarily ChatGPT, Perplexity, Claude, Bing, or a private RAG
  system; use `seo` and its broader AI-search references first.
- The task is only metadata, sitemap, hreflang, or schema implementation with
  no Google generative-AI decision involved; use `seo`.
- The user expects guaranteed inclusion in AI Overviews or AI Mode. Google
  does not guarantee crawling, indexing, serving, or AI-feature inclusion.

## Preserved Domain Inputs
- Target pages, page roles, business model, and primary user questions.
- Current SEO baseline: crawlability, indexability, snippets eligibility,
  canonical/hreflang state, internal links, JavaScript rendering risks, and
  duplicate-content risks.
- Search Console and analytics access when performance or diagnostics are in
  scope.
- Local business, ecommerce, Merchant Center, Google Business Profile, product
  feed, or Business Agent status when relevant.

## Preserved Domain Workflow
1. Load `references/google-generative-ai-search-playbook.md` before making
   recommendations.
2. Start from the Google rule: generative AI features in Search are grounded in
   core Search ranking and quality systems, so the work is still SEO.
3. Audit content for non-commodity value: original experience, expert point of
   view, useful organization, high-quality media, and satisfaction for real
   visitors.
4. Reject manipulative AI-search tactics: query fan-out page factories,
   chunking for AI, special Google AI markup, inauthentic mentions, UGC spam,
   poisoned snippets, and structured-data overuse.
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
8. Measure Google generative Search through the dedicated Search Console report
   for AI Overviews and AI Mode, then connect impressions to normal Web search,
   analytics, and outcomes such as conversions, subscriptions, leads, or sales.
   Record the separate Search Console include/exclude control and its owner.
9. When Bing/Copilot or multi-assistant visibility matters, use the currently
   documented Bing AI Performance measures: total citations, average cited
   pages, sampled grounding queries, page-level citation activity, and trends.
   Do not interpret these as ranking, authority, placement, or business value.
10. For editorial, FAQ, review, forum, or community-heavy work, run a
   source-integrity pass before publishing: primary sources first, named experts
   where possible, no anonymous UGC as sole proof for money or safety claims,
   and no copied claims from unverified AI summaries.
11. When browser agents or commerce agents matter, load
   `references/agentic-readiness.md` and produce an agent-readiness backlog.

## Preserved Domain Quality Guidance
- Never present AEO/GEO hacks as Google requirements.
- Treat `llms.txt` as an optional broader engine/LLM handover artifact, not a
  Google AI Search requirement, ranking lever, or default client priority.
- Structured data must match visible page content and exist for rich-result
  eligibility, not as special AI Overview markup.
- Content recommendations must improve human usefulness first; AI visibility
  is a consequence of useful, crawlable, indexable content.
- AI-assisted content must meet Search Essentials, spam policies, and the
  same accuracy, quality, relevance, and disclosure bar as human-written work.
- AI-citation strategy must be source-quality strategy: cite authoritative,
  durable, original sources; monitor UGC surfaces for poisoning and brand-safety
  risk; do not attempt to manipulate assistants with planted comments.

## Preserved Domain Anti-Patterns
- Creating many near-duplicate pages to capture every fan-out query variant.
- Breaking useful pages into unnatural fragments only for AI parsing.
- Rewriting copy into robotic answer blocks when the human page gets worse.
- Buying or manufacturing off-site mentions for perceived AI authority.
- Hiding weak content behind schema, Markdown files, or crawler files.
- Blocking Googlebot and expecting AI Overviews or AI Mode visibility.

## Preserved Domain Outputs
- Google AI Search readiness audit.
- Content and technical implementation backlog.
- Mythbusting note for stakeholders.
- Search Console generative AI, Bing AI Performance, citation-support review,
  and analytics measurement plan.
- Local/ecommerce readiness checklist.
- Source-integrity and UGC-risk notes when the content may be cited by AI tools.
- Agentic-readiness backlog when relevant.

## Preserved Domain References
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
