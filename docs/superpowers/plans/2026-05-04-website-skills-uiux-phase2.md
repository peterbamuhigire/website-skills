# Website-Skills UX/UI Phase 2: Work Record

> **Historical record.** This file was originally a task-by-task implementation plan that embedded draft reference content taken from five UX/UI books. Under the owner's copyright rule that content, and the `book-extractions/` folder it came from, was removed on 2026-09-24. This file now records only what was planned and which files were touched. The capabilities that survive live in the skill references named below; see the capability preservation map in `docs/continuous-improvement/book-source-retirement-2026-09-24.md`.

## Goal

Add UX/UI strategy, cognitive-science, maturity-scoring, competitive-analysis and data-visualisation capabilities to five core skills and two universal-guideline documents, using eight new reference files, eight extensions and five `SKILL.md` pointer edits (21 file edits in total). The work was documentation only: no code and no automated tests. Verification was by file existence and section-heading checks, with one commit per skill cluster.

## Conventions adopted

- New reference files carried a provenance header and a "Used by" line.
- Extensions to existing files were added as clearly marked new sections, leaving existing front matter untouched.
- No emojis.

Note: the provenance-header convention has since been replaced by a closing `## Sources` section under the repository's copyright brief.

## Clusters and files touched

Paths are relative to `C:\wamp64\www\website-skills\skills\` unless stated.

| Cluster | Skill | New files | Extended files | `SKILL.md` |
|---|---|---|---|---|
| A | premium-ui-ux-design | `references/levy-four-tenets.md`, `references/enterprise-five-outcomes.md`, `references/pm-collaboration-rules.md` | none | pointer added |
| B | ux-psychology | `references/three-paradigms-of-hci.md`, `references/three-levels-of-ux-scope.md` | `references/legacy-guidance.md` (working-memory and cognitive-affordance sections) | pointer added |
| C | design-quality-score | `references/enterprise-ux-maturity-checklist.md` | `references/rubric.md`, `references/score-calibration.md` | pointer added |
| D | design-reference | `references/levy-competitive-matrix.md` | `references/competitor-analysis-worksheet.md` | pointer added |
| E | design-system | `references/enterprise-data-viz-rules.md` | `references/ux-quality-checklist.md`, `references/ai-slop-prevention.md` | pointer added |
| F | universal-guidelines (`C:\wamp64\www\website-skills\universal-guidelines\`) | none | `UNIVERSAL-DESIGN-GUIDELINES.md`, `ux-laws-and-psychology.md` | not applicable |

## What each cluster was meant to add

- **A. premium-ui-ux-design.** A strategy-first framing for UX work, a set of enterprise outcome criteria to check before launch, and rules for working with product managers, including an audit checklist for an existing site.
- **B. ux-psychology.** Complementary views of human-computer interaction, a scoping rule for single interactions, journeys and relationships, and working-memory and perceivability rules for design review.
- **C. design-quality-score.** A design-maturity scale used as an additional scoring category, a premium-pricing gate, and a protocol for reconciling disagreement between scorers.
- **D. design-reference.** A structured competitive-analysis matrix adopted as the canonical worksheet.
- **E. design-system.** Data-visualisation rules for enterprise interfaces, a first-impression checklist, and additional anti-patterns for generic-looking output.
- **F. universal-guidelines.** Foundations, working-memory laws and interaction-paradigm guidance added to the two shared guideline documents.

## Verification step

A final end-to-end check confirmed that every named file existed, every new section heading was present, and each `SKILL.md` pointed to its new references. No commit was made for that step.

## Status

Delivered on 2026-05-04. The reference files listed above have since been rewritten as the engine's own syntheses where required by the copyright brief; consult each file's `## Sources` section for attribution.
