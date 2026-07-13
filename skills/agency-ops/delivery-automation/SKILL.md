---
name: delivery-automation
description: Use when auditing and automating repeatable agency delivery work, choosing build versus buy, or creating internal starter kits and SOPs. Use `service-blueprint-website-delivery` for one engagement's operating model and `deploy` for project CI.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Delivery Automation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Deciding which parts of website delivery to standardise, templatise, or automate.
- Choosing build vs buy for a CMS, stack, or internal tool.
- Designing reusable assets: starter kits, design systems, intake forms, content
  pipelines, QA/deploy automation, reporting automation.
- Deciding where (and whether) AI-assisted coding actually speeds delivery.
- Running an audit to find and prioritise automation opportunities.
- Writing the SOPs and playbooks that make delivery repeatable.

## Do Not Use When

- The task is the human/process design of a single client engagement's delivery
  journey (use `service-blueprint-website-delivery`).
- The task is the visual design system for a client site rather than a reusable
  internal asset (use `design-system`).
- The task is the CI/deploy pipeline of a specific client project (use `deploy`).
- The task is the agency's offer, pricing, or positioning (use `agency-positioning`).

## Inputs

- The agency's current delivery workflow (the steps from sale to launch).
- The niche and the typical project shape (so reusable assets fit real work).
- Honest time data on where delivery hours actually go.

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Stable workflow and SOP | Delivery operations | yes | Standardise before automating. |
| Volume, time, error, and cost evidence | Time logs and QA records | yes | Run a measured pilot; do not claim savings. |
| Data, permission, and rollback boundary | Process owners | yes | Stop any mutation or integration. |

## Workflow

1. **Productize first, automate second.** Define the repeatable offering — fixed
   scope, fixed price, predictable process — before automating anything. Apply
   the Built-to-Sell test: is the service **Teachable, Valuable, Repeatable**? If
   it is not repeatable, it is not yet automatable. See
   `references/productized-delivery-sops.md`.
2. **Audit the workflow.** Inventory every repeatable step, time it honestly for a
   week, then score each by **Volume × Time × Frequency × Complexity**. A
   spreadsheet, a timer, and honest interviews cover most of it. See
   `references/automation-opportunity-audit.md`.
3. **Decide build vs buy per component.** For each candidate (CMS, stack, tool),
   run the rubric: control and speed gained vs maintenance burden, handover/lock-in
   risk, and total cost of ownership. See `references/build-vs-buy-rubric.md`.
4. **Build reusable assets where they repeat.** Starter kits/boilerplates, a
   token-based design system (`design-system`), conditional intake forms
   (`form-ux-design`), QA/deploy automation (`deploy`), and reporting automation
   (`monthly-report`) are the high-return categories.
5. **Apply AI honestly.** Use AI assistance where the 2025 evidence supports it
   (greenfield scaffolding, boilerplate, first drafts) and distrust it where the
   evidence warns (complex/maintenance work, where review becomes the bottleneck).
   Keep the engine's quality gates as the constraint. See
   `references/ai-assisted-delivery-reality.md`.
6. **Pilot one, measure, then expand.** Implement one automation properly,
   measure the time/quality impact, train the team, then add the next. Never
   automate ten things at once.
7. **Document as SOPs and playbooks.** Onboarding, request handling, communication
   standards, and quality control become checklists new operators can follow. An
   internal wiki precedes scaling.
8. **Protect handover.** Anything custom ships with clean documentation and a
   handover path, so the client is never locked to one operator and the agency is
   never locked to one undocumented tool.

8. Stop when permissions, rollback, or baseline evidence are missing; recover with a read-only pilot specification.

## Quality Standards

- **Repeatable before automated.** No automation of a process that isn't yet
  standardised — you'd be hard-coding chaos.
- **Quality gates non-negotiable.** Speed never bypasses the canonical CI gates
  (perf, a11y, visual-qa, security, design-quality). Faster delivery that fails a
  gate is not delivery.
- **Honest about AI.** No "AI makes it 10× faster" claims. State where AI helps
  and where the primary evidence shows it slows experienced work or shifts the
  bottleneck to review.
- **Build only what earns it.** Custom tooling is justified by measured
  Volume × Time × Frequency, not by novelty. Default to buy unless the rubric
  says build.
- **Handover-safe.** Every custom artefact has documentation and a clean exit.
  Undocumented custom tooling is lock-in risk, not an asset.
- **Margin visible.** The point is lower delivery cost at held quality — track the
  delivery hours saved, not the tools built.

## Anti-Patterns

- Building a custom CMS or tool because it's interesting, not because the audit
  justified it.
- Automating a non-standardised process. Fix: stabilise the SOP and exception owner first.
- Trusting AI output on complex/maintenance work without review, then shipping
  "almost-right" code.
- Skipping quality gates to claim speed. Fix: measure cycle time only after required gates pass.
- A custom tool with no documentation — locking both client and agency in.
- Using a big-bang rollout. Fix: pilot, measure, correct, and expand within a rollback boundary.
- Confusing this skill's reusable internal assets with a single client's delivery
  blueprint (`service-blueprint-website-delivery`).
- Claiming savings from unmatched periods. Fix: compare the same workflow definition and cohort basis.
- Deploying without a manual fallback. Fix: document the fallback owner and test rollback before release.

## Outputs

- A prioritised automation-opportunity backlog (scored).
- Build-vs-buy decisions per delivery component, with the rationale.
- Reusable assets: starter kit, design-system tokens, intake forms, QA/deploy and
  reporting automation.
- A delivery SOP / playbook set and an internal wiki seed.
- A measured before/after on delivery hours per project.

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Automation register | Operations owner | Scores volume, time, error, value, risk, owner, and dependency. |
| Build-versus-buy decision | Leadership and implementer | Records total cost, reversibility, data boundary, support, and rejected option. |
| Automated workflow and runbook | Delivery team | Has tests, approval points, observability, manual fallback, rollback, and owner. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Before/after measure | Same definition and period basis | Savings and quality claims are reproducible. |
| Failure-path test | Scenario/result record | Permissions, partial failure, retry, duplicate, and rollback are assessed. |

## Capability Contract
Analysis defaults to read-only. Editing or execution requires implementation authority. Connecting accounts, processing client data, purchasing tools, deploying automation, or deleting records requires explicit authority and rollback.

## Degraded Mode
Fallback if tools, logs, or execution are unavailable: return a scored register, pseudoflow, and test plan. Mark savings, reliability, and integration behaviour `not assessed`.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Process is unstable or judgement-heavy | Standardise or keep human-owned | Automating inconsistency or trust work |
| Commodity capability has a viable vendor | Buy and integrate reversibly | Undifferentiated maintenance burden |
| Repeated niche logic is strategic and measurable | Build a bounded internal asset | Vendor mismatch or recurring manual cost |

## Worked Example
Automate image naming only after the convention and exception owner are stable. The tool previews changes, rejects collisions, logs the mapping, and supports rollback; time saved is measured against the same project cohort.

<!-- dual-compat-end -->

## References

- `references/build-vs-buy-rubric.md` — when to build custom vs use
  WordPress/Webflow/Wix/headless; TCO, lock-in, and handover risk.
- `references/automation-opportunity-audit.md` — the inventory → time → score
  (Volume × Time × Frequency × Complexity) method and the pilot-then-expand rule.
- `references/ai-assisted-delivery-reality.md` — the honest 2025 evidence on AI
  coding productivity; where it speeds work, where it slows it, and how to keep
  quality gates as the constraint.
- `references/productized-delivery-sops.md` — the Teachable/Valuable/Repeatable
  test, the SOP/playbook categories, and the systemisation tradition.
- `references/sources.md` — attributed sources (Warrillow, METR, Faros AI, Stack
  Overflow 2025) with confidence flags.

## Notes

- This skill is a portable execution layer for both Claude Code and Codex.
- It builds the *internal* capability behind the engine's existing client-facing
  skills: `design-system` (tokens/components), `form-ux-design` (intake),
  `deploy` (CI/QA), `monthly-report` (reporting). It does not replace them.
- Africa calibration: lower-cost reusable delivery makes premium quality viable at
  local market floors; bandwidth and device realities make the engine's
  performance and a11y gates more important, not less — see
  `../../launch-ops/deploy/references/africa-calibration.md` and
  `../../orchestration/africa-excellence/SKILL.md`.
- This skill has no bundled scripts of its own; it orchestrates the canonical
  scripts under `scripts/` (perf-gate, a11y-gate, visual-qa, security-gate, etc.).
