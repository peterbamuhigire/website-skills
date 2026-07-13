---
name: skill-safety-audit
description: Use when reviewing a new or changed skill for unsafe instructions, hidden side effects, credential access, installers, or permission inflation; use skill-writing for authoring and update-claude-documentation for router maintenance.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Skill Safety Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Review a skill and its linked scripts or references for safety defects without changing the target by default.

<!-- dual-compat-start -->
## Use When

- A skill is new or materially changed
- linked scripts install software or access external systems
- a reviewer needs a release safety verdict.

## Do Not Use When

- Use `skill-writing` to author the contract. Do not use this audit as permission to edit the target skill.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Skill directory and complete diff | Repository and change author | yes | Inspect instructions, references, and scripts | Stop if the target or linked executable surface is unavailable |

## Workflow

1. Confirm read-only scope and enumerate the full skill surface
2. Inspect instructions, links, scripts, permissions, and side effects
3. Classify evidence by severity and stop acceptance on an unresolved critical or high finding
4. After an authorised repair, rerun the affected checks and issue a fresh verdict.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Safety audit report | Skill maintainer and release owner | Lists evidence, severity, correction, unassessed checks, and an accept/block verdict |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Finding register and inspected-file list | Release owner | Each finding cites a file and line or command result |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required; execution is limited to safe inspection checks. Default to read-only. Editing a finding requires separate remediation authority; installers, credentials, publishing, and destructive actions are never implied.

## Degraded Mode

If a linked script, tool, or external endpoint is unavailable, mark that surface `not assessed`, block an unconditional approval, and return the narrowest qualified finding register.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Unknown installer or credential request | Block acceptance and require provenance or removal | Credential theft or hidden installation |
| Broad write or network access for a read-only role | Reduce permissions before acceptance | Permission inflation |

## Quality Standards

- Inspect the body, references, scripts, manifests, and proposed diff; do not approve a skill with an unassessed high-risk executable surface.

## Anti-Patterns

- Reviewing only `SKILL.md` while ignoring a bundled installer. Fix: enumerate and inspect every linked script and reference.
- Calling suspicious behaviour malicious without evidence. Fix: cite the instruction, permission, destination, and plausible effect.
- Editing during the audit. Fix: preserve read-only scope until remediation is separately authorised.
- Treating an unavailable script inspection as a pass. Fix: mark it `not assessed` and qualify or block the verdict.
- Approving broad credentials for convenience. Fix: require the least permission needed by the declared workflow.

## Worked Example

A skill links to `install.ps1` but the script is missing. Record the executable surface as `not assessed`, withhold approval, and request the missing file rather than assuming safety.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- The task matches this domain: Scan new or updated skills for unsafe or malicious instructions (unknown tools, external installers, credential harvesting) before accepting them into the repository.
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
