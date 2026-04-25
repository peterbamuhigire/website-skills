---
name: seo
description: "Comprehensive search engine optimization for multi-language static sites and AI visibility. Implements meta tags, JSON-LD structured data, E-E-A-T schema markup, multi-language sitemap generation, hreflang tags, robots.txt, crawler optimization (IndexNow, sitemap pinging), Google Analytics 4 via Partytown, Google Search Console verification, canonical URLs, and language-specific Open Graph tags. Covers both traditional SEO and Generative Engine Optimization (GEO) for AI platforms. Supports 3 languages: English, French, Kiswahili. Reads from docs/{lang}/seo.md for per-page, per-language configuration. Generates language-specific sitemaps (sitemap-en.xml, sitemap-fr.xml, sitemap-sw.xml) and SEO audit report. Run after page-builder, before deploy."
---

# Seo
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Comprehensive search engine optimization for multi-language static sites and AI visibility. Implements meta tags, JSON-LD structured data, E-E-A-T schema markup, multi-language sitemap generation, hreflang tags, robots.txt, crawler optimization (IndexNow, sitemap pinging), Google Analytics 4 via Partytown, Google Search Console verification, canonical URLs, and language-specific Open Graph tags. Covers both traditional SEO and Generative Engine Optimization (GEO) for AI platforms. Supports 3 languages: English, French, Kiswahili. Reads from docs/{lang}/seo.md for per-page, per-language configuration. Generates language-specific sitemaps (sitemap-en.xml, sitemap-fr.xml, sitemap-sw.xml) and SEO audit report. Run after page-builder, before deploy.
- The user needs an implementation-facing skill rather than a general discussion.

## Do not use when
- The prerequisite upstream context is missing and the task is not yet execution-ready.
- Another narrower skill is the clear better fit for the exact subtask.

## Required inputs
- Project context, current files, and any constraints that affect implementation.
- Upstream artifacts produced by earlier skills when this skill is part of a pipeline.

## Workflow
1. Read only the relevant project inputs and preserved guidance before acting.
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. Validate that the result stays compatible with the rest of the repository workflow.

## Quality standards
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.

## Anti-patterns
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not generate generic output that ignores the actual project context.

## Outputs
- Implementation guidance, configuration, generated artifacts, or concrete follow-on steps.

## References
- `references/premium-seo-package.md` — the default SEO package delivered on every Growth/Authority engagement. Strategy-first SEO, intent map, metadata, schema, internal linking, GEO/AI visibility, local SEO, measurement.
- `references/analytics-event-map.md` — minimum instrumentation for every site: event taxonomy, conversion goals, UTM convention, attribution model, consent, pre-launch checklist.
- `references/seo-topic-and-intent-map.md` — align search intent with page roles, proof burdens, CTA posture.
- `references/conversion-intent-and-launch-seo.md` — use when SEO work must support content clusters, launch windows, conversion-aware metadata, or state changes between prelaunch, open, and closed offers.
- `references/legacy-guidance.md` — preserved detailed instructions from the previous skill version.
- Read only the specific files under `references/` that match the current task instead of loading the whole directory.
- This skill has no bundled scripts by default; keep execution focused on the documented workflow and any existing project files.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

