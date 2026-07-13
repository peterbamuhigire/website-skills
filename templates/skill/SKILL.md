---
name: replace-with-directory-name
description: Use when a concrete website-delivery task needs this procedure; use the named neighbouring skill for its distinct trigger.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Replace With Skill Title
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

State the procedure's purpose and boundary in one or two sentences.

<!-- dual-compat-start -->
## Use When

- Name three to seven concrete positive triggers.

## Do Not Use When

- Name the closest neighbour and the condition that routes there.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Project brief | Client or upstream skill | yes | Establish scope | Stop and request the missing decisions |

## Workflow

1. Validate the inputs and authority boundary.
2. Choose a branch using the decision rules.
3. Produce the artefact and inspect the evidence.
4. Stop on a blocking check; repair it and rerun the affected check.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Named deliverable | Downstream skill or client | A reviewer can observe the stated required fields and checks |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Review record | Release owner | Names checked items, failures, fixes, and unassessed checks |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Editing or execution is allowed only when the request authorises implementation. Production mutation and publication require explicit authority.

## Degraded Mode

If an optional capability or input is unavailable, return the narrowest useful qualified artefact and mark the affected checks `not assessed`.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Required evidence is missing | Stop and request or verify it | Invented project facts |

## Quality Standards

- Define observable domain checks and release blockers.

## Anti-Patterns

- Using a generic input placeholder. Fix: name the actual upstream artefact and provider.
- Routing every adjacent request here. Fix: state the neighbour's winning condition.
- Claiming an unavailable check passed. Fix: mark it `not assessed`.
- Mutating production during analysis. Fix: require explicit mutation authority.
- Returning prose without an inspectable artefact. Fix: use the output contract and acceptance condition.

## Worked Example

Show one realistic input, decision, output fragment, and failure recovery.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)
