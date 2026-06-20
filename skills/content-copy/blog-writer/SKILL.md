---
name: blog-writer
description: Generate researched, SEO-optimised, bilingual blog articles with featured images, in-article photography, distinctive per-article design, source integrity, genuine voice, and anti-AI-slop editorial review. Articles are drafted and edited as markdown in docs/{lang}/blog/{slug}.md. On instruction, builds Astro blog pages from those markdown files. Works for any client website and any topic. Use when the user says "write a blog article", "create a blog post", "publish a blog", "write about [topic]", or wants to add content to the blog section.
---

# Blog Writer
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Generate researched, SEO-optimised, bilingual blog articles with featured images, in-article photography, distinctive per-article design, source integrity, genuine voice, and anti-AI-slop editorial review. Articles are drafted and edited as markdown in docs/{lang}/blog/{slug}.md. On instruction, builds Astro blog pages from those markdown files. Works for any client website and any topic. Use when the user says "write a blog article", "create a blog post", "publish a blog", "write about [topic]", or wants to add content to the blog section.
- The user needs domain-specific strategy, writing, or planning in this area.

## Do not use when
- Another skill is clearly narrower and better matched to the request.
- The task is unrelated to this domain or needs direct implementation instead.

## Required inputs
- Business context, target audience, and the artifact or decision being developed.
- Any existing materials, constraints, or supporting references already available.

## Workflow
1. Read the current business context and the concrete task to solve.
2. Do not draft from assumed knowledge. Confirm the article brief has target
   reader, buyer question, search intent, point of view, proof available,
   sources, author basis, internal links, and next action. If not, state the gap.
3. Use only the relevant detailed guidance and references for the request at hand.
4. For every public article, load
   `../premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md`
   before drafting and before final approval.
5. For premium, revenue-critical, or authority-building articles, apply `premium-commercial-writing` so the article has a buyer question, authority role, SEO/GEO intent, proof, useful examples, and a next step.
6. Produce the strategy, writing, or framework output this skill is responsible for.
7. Check the result for clarity, realism, source integrity, anti-slop quality,
   and handoff readiness.

## Quality standards
- Outputs must be specific, usable, and grounded in the available evidence.
- Recommendations should support follow-on execution instead of staying abstract.
- The result should remain consistent with the broader repository system.
- Every article must include a visible reason to exist: a buyer question,
  argument, example, comparison, case insight, practical method, or timely
  sourced update. Keyword-only articles fail.
- Every important factual claim must be sourced, attributed, qualified, or
  removed. For time-sensitive topics, verify current sources before drafting.
- Articles must show human judgment: tradeoffs, caveats, examples, constraints,
  regional context, author expertise, or field experience.

## Anti-patterns
- Do not produce generic framework dumps with no decision made.
- Do not invent facts to complete the output.
- Do not ignore the actual audience, offer, or business constraints.
- Do not open with generic industry scene-setting.
- Do not publish anonymous or user-generated content as proof for high-stakes
  claims without independent verification.
- Do not pad FAQs, definitions, or listicles for SEO volume when they do not
  improve the reader's decision.

## Outputs
- Strategy notes, article briefs, writing deliverables, source notes, evidence
  gaps, framework outputs, or implementation-facing recommendations.

## References
- Start with `references/legacy-guidance.md` when you need the preserved detailed instructions from the previous skill version.
- Use `references/series-and-launch-engine.md` when the article is part of a campaign, launch, authority sequence, or deliberate conversion pathway instead of a standalone post.
- Use `../premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md` for every public article draft and final review.
- Use `../premium-commercial-writing/references/blog-and-authority-writing.md` when an article must support topical authority, buyer education, SEO/GEO visibility, sales enablement, or premium positioning.
- Use `../premium-commercial-writing/references/seo-ai-search-writing.md` when the article needs answer blocks, entity clarity, AI-search usefulness, or schema handoff notes.
- Read only the specific files under `references/` that match the current task instead of loading the whole directory.
- This skill has no bundled scripts by default; keep execution focused on the documented workflow and any existing project files.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

