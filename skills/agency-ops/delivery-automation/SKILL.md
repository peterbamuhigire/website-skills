---
name: delivery-automation
description: Build the agency's own tooling, templates, and workflow automation so a niche web studio delivers faster and cheaper without dropping quality — the productized-delivery operating model. Use when deciding what to systematise or automate, building vs buying a CMS or stack, designing reusable starter kits / design systems / intake flows, applying AI-assisted delivery honestly (where it speeds work and where it does not), running an automation-opportunity audit, or writing delivery SOPs and playbooks. Anchored on Built to Sell (Teachable/Valuable/Repeatable) and on the primary 2025 evidence about AI coding productivity. Pairs with service-blueprint-website-delivery, design-system, deploy, and monthly-report.
---

# Delivery Automation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when

- Deciding which parts of website delivery to standardise, templatise, or automate.
- Choosing build vs buy for a CMS, stack, or internal tool.
- Designing reusable assets: starter kits, design systems, intake forms, content
  pipelines, QA/deploy automation, reporting automation.
- Deciding where (and whether) AI-assisted coding actually speeds delivery.
- Running an audit to find and prioritise automation opportunities.
- Writing the SOPs and playbooks that make delivery repeatable.

## Do not use when

- The task is the human/process design of a single client engagement's delivery
  journey (use `service-blueprint-website-delivery`).
- The task is the visual design system for a client site rather than a reusable
  internal asset (use `design-system`).
- The task is the CI/deploy pipeline of a specific client project (use `deploy`).
- The task is the agency's offer, pricing, or positioning (use `agency-positioning`).

## Required inputs

- The agency's current delivery workflow (the steps from sale to launch).
- The niche and the typical project shape (so reusable assets fit real work).
- Honest time data on where delivery hours actually go.

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

## Quality standards

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

## Anti-patterns

- Building a custom CMS or tool because it's interesting, not because the audit
  justified it.
- Automating a non-standardised process.
- Trusting AI output on complex/maintenance work without review, then shipping
  "almost-right" code.
- Skipping quality gates to hit a faster timeline.
- A custom tool with no documentation — locking both client and agency in.
- A big-bang automation rollout instead of pilot-measure-expand.
- Confusing this skill's reusable internal assets with a single client's delivery
  blueprint (`service-blueprint-website-delivery`).

## Outputs

- A prioritised automation-opportunity backlog (scored).
- Build-vs-buy decisions per delivery component, with the rationale.
- Reusable assets: starter kit, design-system tokens, intake forms, QA/deploy and
  reporting automation.
- A delivery SOP / playbook set and an internal wiki seed.
- A measured before/after on delivery hours per project.

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
