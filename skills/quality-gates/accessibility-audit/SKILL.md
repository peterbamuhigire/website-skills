---
name: accessibility-audit
description: Use when auditing rendered website conformance to WCAG 2.2 AA with automated, keyboard, screen-reader, zoom, contrast, and content checks; use visual-qa for screenshot and hierarchy defects.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Accessibility Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Produce a read-only accessibility verdict with reproducible evidence and explicit unassessed checks.

<!-- dual-compat-start -->
## Use When

- A rendered site needs a pre-release accessibility gate
- a regression may affect keyboard or assistive technology
- remediation needs prioritised evidence.

## Do Not Use When

- Use `visual-qa` for screenshot drift or `design-quality-score` for broader aesthetic scoring.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Rendered routes, supported browsers, component states, content, and testing environment | Build artefact and release plan | yes | Exercise the declared user experience | Stop if critical routes or interactive states cannot be reached |

## Workflow

1. Confirm read-only scope, routes, standards, and test environment
2. Run automated checks and manual keyboard, focus, zoom, contrast, form, and screen-reader smoke tests
3. Classify failures and stop release on WCAG AA blockers
4. After authorised remediation, rerun the affected route and regression sample.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Accessibility audit report | Developers, content owners, and release owner | Each issue cites route, element, criterion, severity, reproduction, and correction; verdict names unassessed checks |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Machine reports and manual test record | Release owner | Results are timestamped and tied to the tested build |

<!-- dual-compat-end -->
## Capability Contract

Read, search, execution, browser, and assistive-technology access are required for full assessment. Default to read-only. Code edits or production mutation require separate remediation authority.

## Degraded Mode

If rendering, a browser, a screen reader, or a device is unavailable, mark the affected checks `not assessed`, return the narrowest qualified audit, and never convert them to passes.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Critical route has a keyboard trap or inaccessible control | Block release | User exclusion |
| Automated scan is clean but manual checks are unavailable | Report qualified partial result | False WCAG certification |

## Quality Standards

- Test representative routes and all interactive states; automated results alone cannot establish WCAG 2.2 AA conformance.

## Anti-Patterns

- Reporting zero axe findings as accessible. Fix: complete manual keyboard and screen-reader checks.
- Editing the page during the audit. Fix: preserve read-only evidence and separate remediation.
- Omitting the tested build. Fix: record commit or artefact identity.
- Hiding unavailable assistive technology. Fix: mark the check `not assessed`.
- Listing failures without reproduction. Fix: cite route, element, criterion, steps, and expected behaviour.

## Worked Example

If the menu traps focus at 200% zoom, record the route, viewport, keystrokes, criterion, and blocker severity; do not merely write 'navigation inaccessible'.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- Every build of a client site, as a CI-time gate before deploy.
- Before shipping any new template, component, or interactive feature.
- During QA, for keyboard, focus-order, and screen-reader verification.
- When extracting or reviewing claims about a site's accessibility posture.

## Preserved Domain Exclusions
- Looking for authoring-time guidance on how to write accessible copy or
  components — that lives in `content-writing`, `form-ux-design`, and
  `design-system`. This skill audits output, it does not teach craft.

## Core contract
Every primary template must pass:
1. Automated axe-core scan with zero "serious" and zero "critical" violations.
2. Keyboard-only navigation from first focusable element to primary CTA.
3. NVDA (Windows) and VoiceOver (macOS/iOS) smoke tests for reading order,
   landmark announcement, and form label association.
4. The manual checklist in `references/manual-checklist.md` completed and
   signed by the QA operator.

Any failure blocks deploy.

## Canonical Command

```bash
# From a client project root after resolving this engine as WEBSITE_SKILLS
bash "$WEBSITE_SKILLS/scripts/a11y-gate.sh"
```

The command:
1. Starts a static preview on `:4321` against `./dist/`.
2. Runs `@axe-core/cli` against every primary route.
3. Asserts zero serious/critical violations; writes a full report to
   `reports/a11y/<route>.json` and a human-readable summary to
   `reports/a11y/summary.md`.
4. Exits non-zero on any violation of severity serious or critical.

## Preserved Domain Workflow
1. Confirm the build has produced `./dist/` with the primary route set.
2. Run the canonical command (`a11y-gate.sh`).
3. If the automated gate passes, execute the keyboard-only pass from
   `references/manual-checklist.md`.
4. Run the NVDA and VoiceOver smoke scripts from
   `references/screen-reader-scripts.md` for at least one template per template
   type (home, services, service-detail, contact, blog, blog-post).
5. File the completed checklist under the project's launch log.
6. Any failure blocks deploy; fix and re-run.

## Preserved Domain Inputs
- A built static output at `./dist/`.
- The route list from `performance-budgets.json` (reused, not duplicated).
- A QA operator with keyboard-only and screen-reader familiarity.

## Preserved Domain Quality Guidance
- WCAG 2.2 AA is the floor, not the ceiling.
- Contrast is measured in rendered output, not in the design system alone.
- Focus ring must be visible at all times, never `outline: none`.
- No automated pass is accepted without the manual pass that matches it.
- Screen-reader tests are run, not inferred from markup.

## Preserved Domain Anti-Patterns
- Treating the axe scan as sufficient. Axe catches ~40% of WCAG issues.
- Using placeholder-as-label on forms.
- Invisible skip links or skip links that do not move focus.
- Colour alone as an information channel.
- Modal dialogs without focus trap or `Escape` dismissal.
- Autofocus on page load that breaks reader navigation.
- Custom widgets without ARIA role, name, and keyboard behaviour.

## Preserved Domain Outputs
- `reports/a11y/<route>.json` machine-readable axe result per route.
- `reports/a11y/summary.md` CI-friendly summary.
- A signed manual checklist stored with the project launch log.
- A blocking CI status when any serious or critical violation is found.

## Preserved Domain References
- `references/wcag-baseline.md` — the WCAG 2.2 AA baseline the engine enforces.
- `references/manual-checklist.md` — the keyboard, focus, motion, and zoom pass.
- `references/screen-reader-scripts.md` — NVDA and VoiceOver smoke scripts.
- `references/axe-config.md` — axe-core configuration and rule selection.
- `references/remediation-playbook.md` — the top twenty violations and how to
  fix them.

## Notes
- This skill does not replace `form-ux-design`, `design-system`, or
  `ux-psychology`. It audits what those skills produce.
- Re-run the full gate whenever `design-system` tokens change, whenever a new
  primary template is added, and whenever a third-party script is authorised.
- This skill is part of the canonical CI pipeline (`templates/ci/website.yml`).
  Do not duplicate its logic per project.
