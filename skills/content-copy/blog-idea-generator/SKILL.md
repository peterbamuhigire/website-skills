---
name: blog-idea-generator
description: Use when a website needs evidence-grounded blog topics, editorial series, or a topic backlog; use `blog-writer` for drafting articles and `content-writing` for page-copy standards.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Blog Idea Generator
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Turn business evidence, buyer questions, and search opportunities into a prioritised editorial backlog that another writer can execute without guessing.

<!-- dual-compat-start -->
## Use When

- A client needs 15-25 useful blog ideas rather than a list of generic keywords.
- A team needs topic clusters, a recurring series, or a launch-supporting editorial sequence.
- Existing website material, interviews, search data, or sales questions should be converted into article briefs.

## Do Not Use When

- The article topic is approved and the task is to research or draft it; use `blog-writer`.
- The task concerns service-page, home-page, or interface copy; use `content-writing`.
- No business, audience, or evidence source is available and the user will not supply one; stop rather than invent a market.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Business offer and website content | Client brief or current site | yes | Request or inspect the minimum available material; do not create a full backlog from a company name alone. |
| Target readers and buyer questions | Interviews, sales notes, support logs, or brief | yes | Produce a short discovery-question list instead of fabricated topics. |
| Search, competitor, or campaign evidence | Search data, verified research, or campaign plan | conditional | Mark search demand and timing as unverified; prioritise first-party questions. |
| Publishing constraints | Editorial owner | conditional | State assumed cadence, language, and article depth. |

## Workflow

1. Inspect the offer, audience, existing content, and available evidence.
2. Stop for discovery if neither buyer questions nor credible business material exists.
3. Group evidence into customer questions, objections, proof, comparisons, process, local context, and timely updates.
4. Select only the ideation methods that fit those sources; use [ideation frameworks](references/ideation-frameworks.md) for the relevant branch.
5. Remove duplicates and ideas that cannot support a specific claim, example, decision, or action.
6. Cluster the remaining ideas into standalone posts, pillar/supporting groups, or a deliberate series.
7. Score each idea for reader value, business relevance, evidence readiness, distinctiveness, and effort.
8. Write an execution brief for each selected idea, then check the set for coverage and overlap.
9. If evidence fails during briefing, downgrade the idea to a research question or remove it; never disguise the gap.

Recovery: repair the evidence or scope, then rerun clustering and collision review before approval.

## Quality Standards

- Every idea names a reader, a real question, a point of view, an evidence source, and a useful next action.
- Titles are distinct enough that two briefs would not produce the same article.
- The set balances buyer-stage needs and does not become a keyword-volume dump.
- Local or time-sensitive claims remain qualified until verified.
- The backlog is implementable by `blog-writer` without another strategy exercise.

## Anti-Patterns

- Generating "10 tips" variants from one keyword. Fix: derive each topic from a different buyer decision or evidence source.
- Inventing search demand. Fix: mark demand unverified and prioritise first-party questions.
- Treating every idea as a standalone post. Fix: identify pillar, supporting, series, and campaign relationships.
- Writing titles without article arguments. Fix: add the promised answer and editorial point of view.
- Ignoring existing coverage. Fix: inspect the site and flag refresh, merge, and cannibalisation risks.
- Producing 25 weak ideas to meet a count. Fix: return the smaller defensible set and name the evidence gap.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Prioritised topic backlog | Content owner | Each row has title, reader, question, intent, evidence, format, priority, and status. |
| Article briefs | `blog-writer` | Each brief states argument, outline, proof needed, internal links, CTA, and unresolved research. |
| Cluster or series map | SEO and campaign owners | Relationships and publishing order are explicit with no duplicate intent. |

## References

- [Legacy detailed guidance](references/legacy-guidance.md) for preserved interview and output conventions.
- [Ideation frameworks](references/ideation-frameworks.md) for selecting a method from the evidence available.
- [Idea sources and series](references/idea-sources-and-series.md) for source buckets, clusters, and recurring formats.
- [Content formats](references/content-formats.md) for matching an idea to a useful article form.
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Source-to-topic trace | Backlog fields or notes | Every approved idea points to a real input or is labelled as a research question. |
| Collision review | Short checklist | Duplicate intent, existing-site overlap, and series relationships are recorded. |

## Capability Contract

Read access to supplied business material is required. Search or network access is optional and may verify demand or current facts. Editing is allowed only when the user authorises writing the backlog into project files; publishing is outside this skill.

## Degraded Mode

Fallback when website access, search data, interviews, or network verification is unavailable: return a smaller, first-party-evidence backlog with every unverified assumption labelled. Do not turn an unresearched topic into an approved recommendation.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Strong buyer evidence and distinct intent | Approve and brief | Generic content that attracts the wrong reader |
| Useful question but missing proof | Keep as research candidate | Fabricated authority |
| Existing page already answers the intent | Refresh or extend that page | Cannibalisation and duplicate content |
| Several ideas form one learning journey | Build a sequenced series | Isolated posts with no commercial path |

## Worked Example

Input: a Ugandan solar installer has sales notes showing repeated questions about battery life, rainy-season output, and maintenance, but no keyword data. Output: three first-party-evidence briefs, each tied to the relevant sales question; search demand is marked unverified and no volume claim is made.

## Read Next

- `blog-writer` drafts and publishes an approved brief.
- `content-writing` supplies general website writing standards.
- `premium-commercial-writing` applies when the series must build authority or support premium fees.
