---
name: website-builder
description: Master orchestrator for building static websites from markdown content and photos. Use when the user says "build a website", "create a site", or references docs/ content. Reads content from docs/, photos from photo-bank/, and generates a complete Astro website.
---

# Website Builder

## Use when
- The user wants a full website build, rebuild, or end-to-end orchestration.
- The task matches this domain: Master orchestrator for building static websites from markdown content and photos. Use when the user says "build a website", "create a site", or references docs/ content. Reads content from docs/, photos from photo-bank/, and generates a complete Astro website.

## Do not use when
- The user only needs one narrow subtask and does not need pipeline coordination.
- Core project inputs do not exist yet and the task is still discovery-only.

## Required inputs
- Project docs, content, assets, and any language configuration.
- A working target project or implementation area.

## Workflow
1. Read the core project inputs before generating or changing anything.
2. Route work through sibling skills in the right order using directory-relative names, not a hardcoded install path.
3. Track outputs from each stage so downstream steps consume the correct artifacts.
4. Verify the full pipeline before reporting completion or blockers.

## Quality standards
- Preserve the intended build order and artifact handoffs.
- Stay portable across Claude Code and Codex installs.
- Report clearly what was built, skipped, or blocked.

## Anti-patterns
- Do not assume the skills live only under `.claude/skills`.
- Do not start generation before reading the project inputs.
- Do not skip downstream verification.

## Outputs
- Build plan, orchestrated execution notes, generated artifacts, or a blocker report.

## References
- Start with `references/legacy-guidance.md` when you need the preserved detailed instructions from the previous skill version.
- Use `references/intake-questionnaire-template.md` when the project still needs structured intake or discovery capture before build orchestration.
- Use `references/website-strategy-brief-template.md` as the canonical source-of-truth artifact before design and build work begins.
- Use `references/project-artifact-standard.md` to confirm the minimum project artifact set before orchestrating downstream work.
- Use `references/discovery-to-build-artifact-map.md` to hand off discovery outputs into sibling skills explicitly.
- Use `references/project-stage-gates.md` to verify the current gate and required approvals before moving phases forward.
- Use `references/kickoff-template.md` when converting sold scope into delivery facts for production.
- Read only the specific files under `references/` that match the current task instead of loading the whole directory.
- This skill has no bundled scripts by default; keep execution focused on the documented workflow and any existing project files.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.
