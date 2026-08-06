# Control-plane adoption

This engine adopts the shared ten-engine contract from
`C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md`. Website
doctrine remains authoritative for UX, content, SEO, implementation,
performance, accessibility, security, and launch operations.

## Local roles and commands

| Role | Responsibility | Evidence owner |
|---|---|---|
| Site planner | Define journeys, information architecture, content, and acceptance criteria. | Route and scope record. |
| Builder | Implement the smallest approved change within the declared stack. | Diff and local verification. |
| Accessibility auditor | Run automated and manual WCAG checks, including keyboard and screen-reader smoke. | Accessibility report. |
| Performance benchmarker | Measure budgets and critical journeys on the target device/network profile. | Performance results. |
| Visual reviewer | Inspect rendered pages, responsive states, overflow, hierarchy, and visual consistency. | Render report. |

Route thin commands `build-site`, `visual-qa`, `accessibility-qa`, and
`launch` to existing skills and canonical CI gates.

## Hook and release contract

- `preflight` records the route, target environment, browser/device matrix,
  content source, and deployment/rollback plan.
- `context` loads the current design system, routes, analytics assumptions,
  known defects, and prior render evidence before edits.
- `before_write` checks scope, backup/reversibility, content authority, and
  security or privacy impact.
- `after_write` runs targeted tests plus accessibility, performance, visual,
  and security checks appropriate to the change.
- `release` requires rendered screens, browser-journey evidence,
  performance-budget results, accessibility/security gates, and a post-deploy
  smoke or explicit `NOT ASSESSED` consequence.
- `stop` preserves preview/build state, failed checks, open visual or
  operational risks, and the next owner.

Native hooks are optional; repository scripts and CI are valid adapters. Do
not call a site launch-ready when a required check is missing.
