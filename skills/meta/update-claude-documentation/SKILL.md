---
name: update-claude-documentation
description: Use when repository skill paths, catalogue counts, routing rules, or operating gates change and AGENTS.md, CLAUDE.md, README, or maintainer documentation must be reconciled; use skill-writing for skill bodies.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Update Claude Documentation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Keep repository-level instructions accurate after an evidenced operating-model or catalogue change.

<!-- dual-compat-start -->
## Use When

- A skill is added, relocated, renamed, or retired
- validation or release commands change
- active counts or routing handoffs change.

## Do Not Use When

- Do not use for copy edits confined to one skill. Use `skill-writing` for authoring the skill contract.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Approved repository change and current machine evidence | Change owner and filesystem | yes | Identify every stale claim | Stop if the change is unapproved or the active catalogue cannot be measured |

## Workflow

1. Measure current paths, counts, commands, and routing
2. Locate every affected claim
3. Update only current operating documents and explicitly supersede stale statements
4. Stop on conflicting authorities, resolve the owner, then rerun link, registry, contract, and documentation checks.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Reconciled repository documentation | Future maintainers and agents | Counts, paths, commands, and handoffs match machine output |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Documentation diff and validation results | Release owner | Shows each changed claim and the command that verifies it |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Documentation editing and checks require explicit authorisation. Do not rename skills, mutate production, publish, or rewrite history unless separately authorised.

## Degraded Mode

If repository discovery or validation is unavailable, return the narrowest qualified stale-claim list and mark affected facts `not assessed`; do not publish guessed counts.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Machine output contradicts a cached table | Update the table from discovery | Stale catalogue claim |
| Two instruction files conflict | Resolve the higher-scope authority before editing | Split-brain routing |

## Quality Standards

- Change only documents affected by measured reality, preserve unrelated history, and make commands portable across supported runners.

## Anti-Patterns

- Copying a cached active count. Fix: discover `SKILL.md` files from active roots.
- Rewriting unrelated history during a router update. Fix: edit only current operating claims.
- Hard-coding a machine-specific external engine path. Fix: route through the global engine table.
- Updating CLAUDE.md but leaving AGENTS.md contradictory. Fix: reconcile both authorities.
- Claiming docs are current without checks. Fix: run registry, link, and contract validators.

## Worked Example

When active skills remain 59 but CI gains two commands, update release instructions and gates while leaving historical audit scores untouched.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- The task matches this domain: "Update project documentation files (README.md, PROJECT_BRIEF.md, TECH_STACK.md, ARCHITECTURE.md, docs/API.md, docs/DATABASE.md, CLAUDE.md) when significant changes occur. Use for feature additions, architecture changes, dependency updates, API/database modifications. Ensures consistency across all docs."
- The user needs repo-maintenance or skill-authoring support rather than project output.

## Preserved Domain Exclusions
- A build, writing, or audit skill should own the task instead.
- There is no repository or skill-maintenance action to perform.

## Preserved Domain Inputs
- The files, changes, or workflow that need maintenance.
- Current repository conventions and any behavior that must not regress.

## Preserved Domain Workflow
1. Read the current repository state and the exact maintenance goal.
2. Use the preserved guidance and any bundled scripts to perform the minimum effective change.
3. Keep the result aligned with existing repo conventions.
4. Prepare the output so a follow-on safety review or documentation pass is straightforward.

## Preserved Domain Quality Guidance
- Maintenance changes must reduce ambiguity, not add process noise.
- Outputs should preserve portability and existing behavior.
- The result should be easy for another agent to continue using.

## Preserved Domain Anti-Patterns
- Do not introduce product-specific assumptions into portable skill rules.
- Do not bloat SKILL.md when detail belongs in references or scripts.
- Do not leave partially updated conventions behind.

## Preserved Domain Outputs
- Updated skill structure, repo-maintenance changes, authoring guidance, or synchronized documentation.
