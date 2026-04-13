# Dual Compatibility Report

## Scope

This report documents the repository upgrade completed on 2026-04-13 to make the skill system work cleanly in both Claude Code and Codex without restructuring the repository.

## What Was Wrong

- Every `SKILL.md` used ad hoc narrative structure instead of a stable execution format.
- Codex-facing routing guidance did not exist at the repository root.
- Several skills contained Claude-oriented path assumptions or implied host-specific installation context in their detailed guidance.
- One skill frontmatter included an extra metadata field beyond `name` and `description`.
- Many skills mixed execution steps and long-form reference material in a single file, which made portable loading less predictable.

## What Was Improved

- All 40 `SKILL.md` files now use the same execution-oriented structure:
  - `Use when`
  - `Do not use when`
  - `Required inputs`
  - `Workflow`
  - `Quality standards`
  - `Anti-patterns`
  - `Outputs`
  - `References`
- Frontmatter is now normalized to `name` and `description` across all skills.
- Each skill preserves its previous long-form body in `references/legacy-guidance.md`.
- `SKILL.md` now acts as the concise, portable control surface for both Claude Code and Codex.
- Path portability is now explicit in the standardized skill guidance.

## What Was Added

- Root [AGENTS.md](/C:/wamp64/www/website-skills/AGENTS.md) to provide:
  - repository purpose
  - baseline operating rules
  - task-to-skill routing
  - quality expectations
  - safety expectations
- New `references/legacy-guidance.md` files inside each skill directory to preserve detailed prior behavior without leaving `SKILL.md` overloaded.

## Why These Changes Matter

- Claude Code keeps working because the same directories and `SKILL.md` entry points still exist.
- Codex now has a clear root instruction file and consistent skill schema to follow.
- The repository no longer depends on hidden structure assumptions for skill discovery.
- Reference handling is clearer: concise skill entry points, heavy detail in `references/`, scripts kept in `scripts/`.
- The system is more composable because each skill now advertises activation conditions, inputs, outputs, and execution boundaries.

## Validation Performed

- Verified that all 40 `SKILL.md` files contain the new section schema.
- Verified that all 40 skills now have only `name` and `description` in frontmatter.
- Verified that every skill preserves its prior body at `references/legacy-guidance.md`.

## Optional Next Improvements

- Refresh `README.md` so it explicitly states the repository is dual-compatible, not only Claude-oriented.
- Add targeted nested `AGENTS.md` files only if future domains develop their own routing complexity.
- Review the preserved `legacy-guidance.md` files over time and extract reusable shared references where duplication remains high.
