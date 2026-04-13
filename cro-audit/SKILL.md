---
name: cro-audit
description: Conversion Rate Optimisation audit for any website. Use after a website is built (or to audit an existing client site) to identify and prioritise conversion improvements. Covers heuristic evaluation, split-test-proven rules (Brunson), attention flow, CTA scoring, form audit, trust signal gap analysis, mobile usability, and hypothesis generation for A/B tests. Outputs docs/cro-audit-report.md.
---

# Cro Audit

## Use when
- The task matches this domain: Conversion Rate Optimisation audit for any website. Use after a website is built (or to audit an existing client site) to identify and prioritise conversion improvements. Covers heuristic evaluation, split-test-proven rules (Brunson), attention flow, CTA scoring, form audit, trust signal gap analysis, mobile usability, and hypothesis generation for A/B tests. Outputs docs/cro-audit-report.md.
- The user needs evaluation, findings, prioritization, or remediation guidance.

## Do not use when
- The user needs direct implementation instead of an audit.
- There is no target artifact or change set to inspect.

## Required inputs
- The site, page, skill, or workflow being audited.
- Any business goals, constraints, or supporting evidence available for prioritization.

## Workflow
1. Define the audit scope and what success or risk means in context.
2. Inspect the target using the relevant checklist and preserved guidance.
3. Summarize the highest-value findings with clear reasoning.
4. Prioritize remediation so the next actions are obvious.

## Quality standards
- Findings must be evidence-based and ordered by impact.
- Recommendations should be specific enough to implement.
- The audit should reduce risk or ambiguity for the next person acting on it.

## Anti-patterns
- Do not provide generic checklist output with no prioritization.
- Do not hide high-severity issues in vague language.
- Do not imply certainty when evidence is missing.

## Outputs
- Audit report, prioritized findings, remediation notes, or approval status.

## References
- Start with `references/legacy-guidance.md` when you need the preserved detailed instructions from the previous skill version.
- Read only the specific files under `references/` that match the current task instead of loading the whole directory.
- This skill has no bundled scripts by default; keep execution focused on the documented workflow and any existing project files.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.
