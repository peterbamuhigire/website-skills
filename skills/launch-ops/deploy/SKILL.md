---
name: deploy
description: Use when a completed website must be built, release-gated, deployed, verified, communicated, and made rollback-ready; use `observability` for telemetry design and quality-gate skills for specialist audits.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Deploy
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Control the final release from verified build artefact through production smoke checks, rollback readiness, and post-launch review.

<!-- dual-compat-start -->
## Use When

- All approved pages and assets are implementation-complete and need a release gate.
- A website needs deployment configuration, promotion, rollback, or post-launch verification.
- A failed launch needs controlled recovery using an existing rollback plan.

## Do Not Use When

- Pages, requirements, content, or design acceptance remain unresolved; return to the owning build skill.
- The task is only telemetry design; use `observability`.
- The task is a specialist accessibility, visual, security, or performance audit; use the respective quality gate.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Release candidate and reproducible build command | Project repository | yes | Stop; no deploy from an unrepeatable local state. |
| Environment, host, domain, secrets ownership, and change window | Project/release owner | yes | Return a release-readiness gap list. |
| Passing quality-gate evidence and approved exceptions | CI and quality owners | yes | Block release; an unavailable gate is not a pass. |
| Deployment, rollback, smoke, runbook, and communication plans | Project files and operations owner | yes | Create drafts where authorised, but do not promote to production. |
| Explicit production authority | User or named release owner | yes for mutation | Stop at deploy-ready handoff. |

## Workflow

1. Inspect repository state, release scope, environment, and upstream acceptance evidence.
2. Stop if production authority, rollback target, secrets ownership, or a blocking gate is absent.
3. Build the release candidate using the documented clean build path.
4. Run the canonical pipeline and project-specific syntax, link, unit, integration, render, accessibility, performance, visual, security, and metadata checks.
5. Verify language routes, forms, analytics, error tracking, redirects, DNS/SSL plan, cache behaviour, and low-bandwidth requirements.
6. Record the release decision, commit/version, artefact identity, approved exceptions, operator, window, and rollback trigger.
7. Promote through the supported deployment path only after explicit authority.
8. Run production smoke checks immediately; if a rollback trigger fires, stop traffic-changing work and execute [the rollback runbook](references/rollback-runbook.md).
9. Communicate the verified result using [the launch communication template](references/launch-communication-template.md).
10. Schedule and record launch-day, 7-day, and 30-day reviews.
11. If deployment fails without a safe rollback, preserve evidence, limit further mutation, and escalate to the named operator.

Recovery: repair the failed gate or environment, then rerun the complete affected release sequence before promotion.

## Quality Standards

- The deployed artefact is traceable to a reviewed commit and reproducible build.
- Every blocking gate passes or has a documented, authorised exception where policy permits one.
- Rollback steps, owner, trigger, and previous good version are tested before promotion.
- Production smoke covers primary routes, language variants, forms, telemetry, and critical conversion paths.
- Secrets never enter source, logs, or handoff documents.
- Release evidence records both successful and unassessed checks.

## Anti-Patterns

- Deploying from an uncommitted workstation state. Fix: build a traceable release candidate.
- Treating an unavailable gate as green. Fix: mark it unassessed and block where required.
- Editing production manually without a recorded path. Fix: use the supported promotion workflow.
- Launching without rollback ownership. Fix: name the operator, trigger, and previous good artefact.
- Checking only the home page. Fix: smoke primary routes, locales, forms, and telemetry.
- Sharing secrets in configuration examples. Fix: reference secret names and approved stores only.
- Claiming success before production verification. Fix: inspect smoke and telemetry evidence first.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Release candidate and deployment configuration | Release operator | Artefact identity, environment inputs, and commands are reproducible. |
| Release decision record | Project and governance owners | Gates, exceptions, authority, operator, window, and rollback trigger are explicit. |
| Deployment and smoke evidence | Client and operations owners | Production routes and critical flows show observed results with timestamps. |
| Rollback-ready handoff | On-call operator | Previous version, procedure, trigger, and verification steps are actionable. |

## References

- [Pre-launch verification](references/pre-launch-verification-checklist.md)
- [QA matrix](references/qa-matrix.md)
- [Deployment runbook](references/deployment-runbook.md)
- [Rollback runbook](references/rollback-runbook.md)
- [Observability baseline](references/observability-baseline.md)
- [Performance gate](references/performance-gate.md)
- [CI troubleshooting](references/ci-troubleshooting.md)
- [Africa calibration](references/africa-calibration.md)
- [Post-launch review](references/post-launch-review-checklist.md)
- [Legacy detailed guidance](references/legacy-guidance.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Gate evidence bundle | CI reports and decision record | Every required gate has pass, fail, approved exception, or unassessed status. |
| Deployment trace | Commit/version, artefact, environment, and timestamp | Production state is reproducible and attributable. |
| Smoke and rollback evidence | Checklist/log | Critical flows are observed and rollback readiness is demonstrated. |

## Capability Contract

Read and execute access are required for validation. Editing configuration is allowed only within the authorised project. Network and production mutation require explicit deployment authority. DNS, secrets, spending, external messages, destructive actions, and rollback require the named authority and least privilege.

The repository rollback adapter requires `ROLLBACK_APPROVED=yes`, an exact
`ROLLBACK_TARGET` equal to `DEPLOY_PATH`, a pre-provisioned
readable `DEPLOY_KNOWN_HOSTS` file path, and a `ROLLBACK_REASON` containing only
bounded log-safe characters. The canonical CI template supplies these values
from named environment variables; it does not turn approval on by default. The
helper records the last-safe symlink pair, validates that both release symlinks
resolve under the declared release root, and verifies recovery after a failed
swap or service reload.

## Degraded Mode

Fallback when network, credentials, CI, rendering, a target environment, or production authority is unavailable: stop at a deploy-ready evidence pack and exact operator runbook. Never claim deployment, visual quality, telemetry, or rollback readiness without observed evidence.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| All blocking evidence passes and authority is explicit | Promote and smoke | Premature release |
| Required check unavailable | Mark unassessed and block per policy | False green status |
| Smoke failure matches rollback trigger | Roll back and verify | Prolonged user impact |
| Failure is non-blocking and exception is permitted | Record owner and expiry | Silent quality debt |
| Remote or environment state differs unexpectedly | Stop and reconcile | Overwriting valid production changes |

## Worked Example

A multilingual site builds successfully but the French contact form cannot be verified because its production secret is unavailable. The release is deploy-ready, not released: the evidence pack records the unassessed form, the secret owner, and the exact smoke step required.

## Read Next

- `observability` owns live telemetry and alerts.
- `security-gate` owns security release evidence.
- `visual-qa` owns rendered-output review.
- `customer-service-website-ops` owns post-launch incident communication and recovery.
