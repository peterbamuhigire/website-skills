---
name: photo-manager
description: Catalogs photos from photo-bank/, records dimensions, copies to a single flat src/assets/images/ directory, and generates _catalog.json with category metadata. Use whenever photos need to be processed, cataloged, or placed in the website.
---

# Photo Manager
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Catalogs photos from photo-bank/, records dimensions, copies to a single flat src/assets/images/ directory, and generates _catalog.json with category metadata. Use whenever photos need to be processed, cataloged, or placed in the website.
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

## photo-bank cleanup rule (required)
- After a photo-bank file is copied into `src/assets/images/` AND its entry is recorded in `_catalog.json`, DELETE the original from `photo-bank/`. The asset copy is the canonical version; the photo-bank is a staging area, not an archive.
- Delete ONLY files you have actually copied and cataloged in this run. Never delete a photo-bank file that was not copied to assets — unused photos stay in `photo-bank/` for future articles.
- Verify the asset copy exists at its destination path before deleting the source. Do not delete on a failed or partial copy.
- This keeps `photo-bank/` showing only un-placed photos, so it doubles as the "still needs a slot" queue.

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
- Read only the specific files under `references/` that match the current task instead of loading the whole directory.
- This skill has no bundled scripts by default; keep execution focused on the documented workflow and any existing project files.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

