---
name: seo-audit
description: Use when performing a read-only audit of an existing website's crawl, indexation, metadata, content, schema, AI citations, answer fidelity, crawler access, referrals, local search, or measurement defects; use seo for implementation.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Seo Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Diagnose search defects and prioritise corrections from reproducible evidence without changing the site by default.

<!-- dual-compat-start -->
## Use When

- An existing site has traffic or indexing concerns
- pre-release search signals need independent review
- remediation priorities need evidence
- AI citations, answer fidelity, crawler access, or AI referrals need repeated,
  read-only diagnosis without changing the site.

## Do Not Use When

- Use `seo` to implement fixes or `google-ai-search` for official AI Overviews and AI Mode guidance.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Target URLs or build, route inventory, intended markets and queries, available crawler and search performance data | Site owner, repository, analytics, and Search Console export | yes | Compare intended and observed search state | Stop or qualify scope if the target cannot be crawled |

## Workflow

1. Confirm read-only scope, target, markets, and available evidence
2. Inspect crawl, index, metadata, intent architecture, answer quality, evidence,
   entity consistency, links, schema, local, performance, and measurement signals
3. When AI-answer visibility is in scope, separate search eligibility, retrieval,
   citation, factual contribution, answer fidelity, referral, and business outcome;
   test repeated prompt paraphrases and platform-specific reports without
   treating a citation as a rank
4. Prioritise findings by impact and confidence and stop release on conflicting critical signals
5. After authorised remediation, rerun only affected checks and a regression sample.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| SEO audit report and remediation register | SEO implementer, content owner, and release owner | Each finding cites URL/evidence, impact, confidence, owner, correction, and retest |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Crawl export, rendered-source samples, schema results, and data-source register | Decision owner | Separates observed facts, inference, and unassessed checks |

<!-- dual-compat-end -->
## Capability Contract

Read, search, crawling, and safe validation are required for full assessment. Default to read-only. Search Console changes, code or content edits, production mutation, and publication require separate authority.

## Degraded Mode

Without network, crawler, rendered source, or performance data, return the narrowest qualified audit and mark affected checks `not assessed`; do not infer an indexation pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Observed index conflict affects priority routes | Block release and correct signals | Lost or duplicate indexation |
| Traffic decline lacks comparable data | Report hypotheses and request evidence | False causal diagnosis |

## Quality Standards

- Cite URLs and data periods, distinguish correlation from cause, prioritise by business impact and confidence, and keep audit separate from remediation.

## Anti-Patterns

- Editing metadata while auditing. Fix: preserve read-only evidence until remediation is authorised.
- Calling a ranking change a penalty without evidence. Fix: state competing hypotheses and needed data.
- Auditing only the homepage. Fix: sample every route and intent family.
- Treating inaccessible Search Console as clean. Fix: mark performance evidence `not assessed`.
- Listing hundreds of equal-priority issues. Fix: rank by impact, confidence, effort, and dependency.
- Treating AEO, GEO, AIO, and SXO as four additional ranking systems. Fix: use
  the layered discoverability model and define each observed outcome.
- Counting one chatbot mention as visibility proof. Fix: repeat versioned prompt
  sets, verify cited support, and connect observations to referrals or outcomes.

## Worked Example

If product pages are absent from the sitemap but indexed through links, cite affected URLs, classify the signal mismatch, assign the sitemap owner, and define the post-fix crawl check.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)
- [Search and AI discoverability operating model](../seo/references/ai-seo-optimization.md)
- [Google generative AI Search playbook](../google-ai-search/references/google-generative-ai-search-playbook.md)


## Preserved Domain Use Guidance
- The task matches this domain: comprehensive, framework-neutral website audit across technical access, index state, intent, content and evidence, entity presence, structured data, performance, mobile, accessibility, local/commerce, links, crawler governance, conventional search, AI-answer visibility, SXO, and measurement. It produces a prioritised evidence register without editing the site.
- The user needs evaluation, findings, prioritization, or remediation guidance.

## Preserved Domain Exclusions
- The user needs direct implementation instead of an audit.
- There is no target artifact or change set to inspect.

## Preserved Domain Inputs
- The site, page, skill, or workflow being audited.
- Any business goals, constraints, or supporting evidence available for prioritization.

## Preserved Domain Workflow
1. Define the audit scope and what success or risk means in context.
2. Inspect the target using the relevant checklist and preserved guidance.
3. Summarize the highest-value findings with clear reasoning.
4. Prioritize remediation so the next actions are obvious.

## Preserved Domain Quality Guidance
- Findings must be evidence-based and ordered by impact.
- Recommendations should be specific enough to implement.
- The audit should reduce risk or ambiguity for the next person acting on it.

## Preserved Domain Anti-Patterns
- Do not provide generic checklist output with no prioritization.
- Do not hide high-severity issues in vague language.
- Do not imply certainty when evidence is missing.

## Preserved Domain Outputs
- Audit report, prioritized findings, remediation notes, or approval status.
