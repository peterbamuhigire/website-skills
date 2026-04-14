---
name: deploy
description: Builds multi-language Astro site, verifies output for all language versions, generates deployment scripts and Nginx configuration with language-aware routing. Supports English, French, Kiswahili. Use after all pages are built, as the final step.
---

# Deploy

## Use when
- The task matches this domain: Builds multi-language Astro site, verifies output for all language versions, generates deployment scripts and Nginx configuration with language-aware routing. Supports English, French, Kiswahili. Use after all pages are built, as the final step.
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
- Start with `references/legacy-guidance.md` when you need the preserved detailed instructions from the previous skill version.
- Use `references/qa-matrix.md` for the minimum launch QA standard across responsive behavior, content, links, performance, accessibility, SEO, analytics, forms, and browsers.
- Use `references/pre-launch-verification-checklist.md` immediately before production release.
- Use `references/deployment-runbook.md` for supported hosting patterns, env management, DNS/SSL, and promotion flow.
- Use `references/rollback-runbook.md` to prepare and execute rollback safely.
- Use `references/observability-baseline.md` for uptime, form delivery, analytics, and issue-detection expectations.
- Use `references/post-launch-review-checklist.md` for launch-day, 7-day, and 30-day review windows.
- Use `references/launch-communication-template.md` to standardize live-site notifications and internal launch comms.
- Read only the specific files under `references/` that match the current task instead of loading the whole directory.
- Use `templates/playwright-starter/` when a project needs a minimal E2E baseline for smoke, navigation, and form coverage.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.
