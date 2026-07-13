---
name: skill-writing
description: Use when creating or upgrading portable website-engine skills, triggers, contracts, references, validators, or routing fixtures; use skill-safety-audit for independent safety review and update-claude-documentation for router-only changes.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Skill Writing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Author reusable website-delivery procedures that route cleanly and expose inspectable inputs, outputs, permissions, failures, and evidence.

<!-- dual-compat-start -->
## Use When

- A repeatable website procedure needs a new skill
- a legacy skill needs conformance repair
- routing fixtures or contract validators need updating.

## Do Not Use When

- Do not create a skill for a one-off task or generic knowledge. Use `skill-safety-audit` for independent safety review.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Reusable problem, neighbour descriptions, and trigger examples | Requester and active catalogue | yes | Prove a distinct route and contract | Stop if the procedure is not repeatable or neighbours cannot be inspected |

## Workflow

1. Inspect the active catalogue and neighbours
2. Choose workflow, standard, or domain shape and declare inputs and outputs first
3. Author decisions, permission boundaries, degraded behaviour, recovery, examples, and references
4. Stop on a routing collision, repair the distinction, then run local and canonical validators plus routing fixtures.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Normalised skill package | Catalogue maintainer and routing engine | Entrypoint is at most 500 lines, validators pass, and fixtures place it in the expected top three |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Validator, routing, line-count, link, and safety results | Release owner | Commands and outcomes identify zero unresolved findings |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Editing and validator execution require an authorised authoring task. Network access is optional for current facts; publication, catalogue removal, and destructive actions require explicit authority.

## Degraded Mode

Without editing or execution, return the narrowest qualified patch plan and mark validation `not assessed`; never claim the skill conforms without results.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| One repeatable trigger and output contract | Normalise or create one skill | Duplicate routes |
| Two independent triggers with different permissions or outputs | Split only after collision analysis | Oversized irrelevant context |

## Quality Standards

- Preserve domain judgement, keep portable instructions runner-neutral, and require positive, negative, collision, limited-capability, and failure-path fixtures.

## Anti-Patterns

- Creating a skill to improve catalogue metrics. Fix: require a repeatable distinct procedure.
- Copying the same body into runner adapters. Fix: keep one canonical skill and thin adapters.
- Writing only positive triggers. Fix: name the neighbour and its winning condition.
- Granting edit access to a review procedure. Fix: default review to read-only.
- Claiming validation from file appearance. Fix: run both local and canonical gates and inspect results.

## Worked Example

For a new form workflow, compare `page-builder` and the external form-design route, declare the distinct output and permissions, then add positive and neighbour-collision fixtures before activation.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- The task matches this domain: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
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

## Preserved Domain References
- Use bundled tools in `scripts/` when they cover the task more reliably than redoing the work manually.
