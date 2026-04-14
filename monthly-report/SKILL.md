---
name: monthly-report
description: Generate a complete professional monthly client report from raw data. Use when producing monthly reports for website design and SEO clients. Claude gathers data through a structured interview, writes plain-English commentary on every metric, drafts the Executive Summary, What We Did, and Next Month Plan sections, then outputs a formatted markdown report ready to copy into a PDF or email. Integrates with agency-client-retention (template and rhythm), ecommerce-analytics (metrics framework), and seo-audit (SEO commentary).
---

# Monthly Report

## Use when
- The task matches this domain: Generate a complete professional monthly client report from raw data. Use when producing monthly reports for website design and SEO clients. Claude gathers data through a structured interview, writes plain-English commentary on every metric, drafts the Executive Summary, What We Did, and Next Month Plan sections, then outputs a formatted markdown report ready to copy into a PDF or email. Integrates with agency-client-retention (template and rhythm), ecommerce-analytics (metrics framework), and seo-audit (SEO commentary).
- The user needs domain-specific strategy, writing, or planning in this area.

## Do not use when
- Another skill is clearly narrower and better matched to the request.
- The task is unrelated to this domain or needs direct implementation instead.

## Required inputs
- Business context, target audience, and the artifact or decision being developed.
- Any existing materials, constraints, or supporting references already available.

## Workflow
1. Confirm the target month with the user (default: calendar month just ended).
2. Read `project-log/CHANGELOG.md` and filter entries to the target month. If the log
   does not exist or the month has no entries, stop and follow the recovery rules in
   `references/project-log-integration.md` — never fabricate activity.
3. Read every file in `project-log/decisions/` and `project-log/incidents/` dated inside
   the target month. Read the prior month's `project-log/monthly/YYYY-MM.md` if present.
4. Generate the monthly roll-up at `project-log/monthly/YYYY-MM.md` using the format in
   `templates/project-log-template.md`. This is the raw material for the report.
5. Generate the client-facing report from the roll-up using `commentary-formulas.md` for
   plain-English translation of metrics. Apply `report-qa-checklist.md` before delivery.
6. Output as markdown ready for PDF export or email. Confirm every metric in the report
   traces back to a log snapshot dated inside the target month.

## Quality standards
- Outputs must be specific, usable, and grounded in the available evidence.
- Recommendations should support follow-on execution instead of staying abstract.
- The result should remain consistent with the broader repository system.

## Anti-patterns
- Do not produce generic framework dumps with no decision made.
- Do not invent facts to complete the output.
- Do not ignore the actual audience, offer, or business constraints.

## Outputs
- Strategy notes, writing deliverables, framework outputs, or implementation-facing recommendations.

## References
- `references/project-log-integration.md` — the contract between this skill and the client project's `project-log/` directory. Start here.
- `references/commentary-formulas.md` — plain-English translation patterns for metrics.
- `references/report-qa-checklist.md` — pre-delivery quality gate.
- `references/legacy-guidance.md` — preserved detailed instructions from the previous skill version.
- `templates/project-log-template.md` (repo root) — the log format this skill reads from.
- This skill has no bundled scripts. Execution is documentary.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.
