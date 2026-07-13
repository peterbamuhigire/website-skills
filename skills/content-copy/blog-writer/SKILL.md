---
name: blog-writer
description: Use when an approved topic must become a researched, source-disciplined article or publishable blog file; use `blog-idea-generator` for topic discovery and `content-writing` for general page copy.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Blog Writer
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Produce useful articles with a stated argument, verified claims, genuine voice, and an implementation-ready handoff.

<!-- dual-compat-start -->
## Use When

- An approved topic or buyer question must become a full article.
- An existing post needs a source-backed rewrite, refresh, or editorial review.
- A campaign or authority series needs an article that supports a defined next action.
- The user has authorised writing or updating a project blog file.

## Do Not Use When

- The task is to discover or prioritise topics; use `blog-idea-generator`.
- The work is general website page copy; use `content-writing`.
- The brief lacks a reader, useful question, or source basis and these cannot be established; stop before drafting.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Article brief: reader, question, purpose, point of view, next action | Content owner or `blog-idea-generator` | yes | Return a brief-completion checklist; do not draft a generic article. |
| Business facts and author basis | Client files, interviews, or approved notes | yes | Mark unsupported sections and narrow the article to evidenced material. |
| Factual sources | Verified research or supplied references | conditional | Remove time-sensitive or material claims that cannot be checked. |
| SEO, internal-link, language, and publishing constraints | SEO/content/project owner | conditional | State assumptions and omit irreversible publishing actions. |

## Workflow

1. Validate the brief: reader, buyer question, search intent, point of view, proof, author basis, internal links, and next action.
2. Stop if the article would exist only to target a keyword or if its central claim cannot be supported.
3. Build a claim-and-source map; distinguish first-party evidence, external facts, opinion, and inference.
4. Choose a structure from [article design](references/article-design.md) that fits the reader's decision rather than a default listicle.
5. Draft the argument with specific examples, trade-offs, constraints, and regional context where supported.
6. Attribute material claims at the point of use and record update-sensitive facts.
7. Edit for reader experience, human voice, scannability, and the standards in [the genuine-writing gate](../premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md).
8. Add metadata, internal-link suggestions, image requirements, and implementation notes when the publishing contract requires them.
9. Run a final source, anti-slop, and handoff review. If a source fails, remove or qualify the dependent claim and re-check the argument.
10. Publish or edit project files only with explicit authority; otherwise return the draft and handoff.

Recovery: repair the brief, source, or claim, then rerun source and editorial checks before handoff.

## Quality Standards

- The article answers a real question and contains a defensible argument or practical method.
- Every important factual claim is sourced, attributed, qualified, or removed.
- Examples and quotations are genuine and traceable; placeholders are labelled.
- The opening earns attention with the reader's problem or decision, not generic industry scene-setting.
- Headings, links, CTA, and metadata support the reader rather than pad search volume.
- The draft sounds like the named author or brand and records any evidence gap.

## Anti-Patterns

- Drafting from assumed knowledge. Fix: create the claim-and-source map first.
- Opening with a broad industry trend. Fix: begin with the reader's concrete decision or observed problem.
- Publishing keyword-shaped filler. Fix: require an argument, example, comparison, or method.
- Using anonymous comments as high-stakes proof. Fix: find independent evidence or remove the claim.
- Adding invented case details or quotations. Fix: label missing proof and request it.
- Treating clean grammar as editorial quality. Fix: test specificity, intent, judgment, and usefulness.
- Publishing without authority. Fix: return the draft and exact implementation steps.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Article draft or revised blog file | Content owner and page builder | Complete argument, usable headings, CTA, and no unresolved placeholder presented as fact. |
| Claim-and-source map | Editor or approver | Every material claim has a source, qualification, or removal decision. |
| Publishing handoff | SEO and implementation owners | Slug, metadata, internal links, image needs, update date, and unresolved gaps are explicit. |

## References

- [Legacy detailed guidance](references/legacy-guidance.md) for preserved end-to-end conventions.
- [Ideation and research](references/ideation-and-research.md) for research planning after topic approval.
- [Article design](references/article-design.md) for structure selection.
- [Editorial standards](references/editorial-standards.md) and [human voice standards](references/human-voice-standards.md) for revision.
- [Reader experience](references/reader-experience.md) and [writing craft](references/writing-craft.md) for prose and navigation.
- [Series and launch engine](references/series-and-launch-engine.md) when the article belongs to a campaign.
- [Genuine-writing gate](../premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md) for every public draft.
- [Blog and authority writing](../premium-commercial-writing/references/blog-and-authority-writing.md) for premium positioning.
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Source register | Claim-to-source table | Material facts are traceable and time-sensitive facts carry dates. |
| Editorial gate result | Checklist or review note | Source integrity, voice, anti-slop, and unresolved gaps are recorded. |
| Change evidence | Diff or revision notes | A refresh identifies material additions, removals, and retained claims. |

## Capability Contract

Read and search access are required for research-backed work. Network access is required only for current external facts; otherwise mark them unverified. Editing and asset generation require explicit authority. Publishing, deployment, and external communication require separate explicit authority.

## Degraded Mode

Fallback when network, files, image generation, or rendering is unavailable: produce the narrowest supported draft and a verification or asset checklist. Do not treat missing research, image review, link checking, or rendering as passed.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Central claim is well supported | Draft and attribute | Unsupported authority claims |
| Central claim is useful but evidence is incomplete | Narrow or qualify the article | Confident wrongness |
| Topic duplicates an existing article | Refresh, merge, or redirect the brief | Cannibalisation |
| Topic is timely and facts may change | Verify current primary sources and date the review | Stale advice |
| Publishing authority is absent | Return draft and handoff only | Unauthorised external mutation |

## Worked Example

Brief: "How Kampala clinics can reduce missed appointments" with clinic scheduling data but no sector-wide statistic. The article uses the clinic's measured pattern as a labelled first-party example, avoids claiming a national rate, and ends with a practical reminder checklist.

## Read Next

- `premium-commercial-writing` for authority-building and premium-fee editorial quality.
- `language-standards` for multilingual or regional language routing.
- `seo` for metadata, schema, sitemap, and crawler implementation.
