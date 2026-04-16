# Phase 10 Completion — Hard Enforcement and Visual QA Gates

**Date**: 2026-04-16
**Phase**: 10 of 12 (website-agency-engine roadmap)
**Status**: Repository deliverables complete; external execution open

## Summary

Closed the enforcement gap identified by the 2026-04-12 evaluation. Every
gate described in Phase 10 now has a skill, a canonical command, and a
place in the inherited CI pipeline. Builds cannot ship without passing
them.

## What Changed

### New skills (3)
- **`accessibility-audit`** — WCAG 2.2 AA gate. Owns axe-core config, manual
  checklist, NVDA/VoiceOver smoke scripts, remediation playbook.
- **`visual-qa`** — Rendered-output gate. Owns Playwright screenshot diff,
  structural assertions (hierarchy, overflow, empty-section), AI-slop scan,
  baseline management, structured reviewer checklist.
- **`security-gate`** — Security + compliance gate. Owns CSP baseline, Africa +
  GDPR compliance matrix, dependency policy, secrets response, supply-chain.

### Canonical CI pipeline
- `templates/ci/website.yml` — 15-step inheritance workflow:
  install → lint → unit → build → e2e-smoke → metadata-audit →
  **perf-gate → a11y-gate → visual-qa → security-gate → drift-check →
  design-quality-score** → deploy → post-deploy-smoke → rollback-ready.
- `scripts/install-canonical-ci.sh` — idempotent bootstrap into any client
  project with `.claude/skills/` mounted.

### Canonical scripts (13)
Every gate has a command an operator can run locally and that CI runs on
every PR:
- `perf-gate.sh`, `audit-third-party-js.sh`, `check-font-performance.sh`
- `a11y-gate.sh`
- `visual-qa.sh` (orchestrator; delegates to Playwright specs + slop-scan)
- `security-gate.sh`, `check-security-headers.sh`, `check-sri.sh`,
  `scan-secrets.sh`, `supply-chain-check.sh`
- `metadata-audit.sh`
- `post-deploy-smoke.sh`, `rollback.sh`

### Canonical configs
- `lighthouserc.json` — 3G-throttled mobile profile, perf/a11y/BP ≥ 95,
  SEO = 100, LCP ≤ 2.0s, INP ≤ 200ms, CLS ≤ 0.1.
- `performance-budgets.json` — route-level weight budgets; 350 KB total
  first-load on 3G; 80 KB JS, 30 KB CSS, 200 KB above-fold image.

### References
- `deploy/references/performance-gate.md` — canonical performance reference.
- `deploy/references/ci-troubleshooting.md` — per-step triage for the 15-step
  pipeline.
- `deploy/references/africa-calibration.md` — 3G network profile, weight
  budget, Save-Data respect, device reality, calibration review cadence.

### Directory contracts
- `reports/bundle/README.md` — canonical bundle-analysis output schema.
- `tests/visual/baseline/README.md` — visual baseline directory contract.

### Skill updates
- `deploy/SKILL.md` — added canonical CI section and 3 new reference entries.
- `website-builder/SKILL.md` — added 7-gate build contract; linked
  `install-canonical-ci.sh` as the post-intake step.

### Decision log
- `project-log/decisions/2026-04-16-phase-10-hard-enforcement-gates.md`

## Thresholds

| Gate | Threshold |
|---|---|
| Lighthouse Performance | ≥ 95 on simulated 3G mobile |
| Lighthouse Accessibility | ≥ 95 |
| Lighthouse SEO | = 100 |
| LCP / INP / CLS | ≤ 2.0s / 200ms / 0.1 |
| Total first-load weight | ≤ 350 KB |
| JS (gzip) / CSS (gzip) | ≤ 80 KB / 30 KB |
| axe serious + critical | 0 |
| Visual diff | < 0.1% pixel |
| npm audit high + critical | 0 (CVE-specific suppressions allowed) |

## External Work Still Required

- Run the canonical pipeline against three existing client projects and
  confirm every gate is green.
- Capture first visual baselines per project.
- Validate edge-configured security headers (Nginx, Cloudflare) against
  staging.
- Deploy and consume CSP report endpoint.
- Register with jurisdiction DPAs for active clients where required.

## Evaluation Impact (expected)

- Performance and Accessibility Enforcement: 7.3 → target 9.2+.
- Overall score trajectory: 8.5 → expected 9.0+ after Phase 10 is in use
  on three projects. Full move to 9.5 depends on Phases 11 and 12.

## Next

Phase 11 — World-Class Operating Discipline:
1. Multi-operator validation + certification programme
2. Documentation drift eradication
3. Live telemetry (observability skill)
4. Experimentation + CRO operations
5. Design-quality scoring rubric + anti-slop
6. Cross-cutting discipline integration

## References

- Plan: `docs/plans/website-agency-engine/phase-10-hard-enforcement-and-visual-qa-gates.md`
- Evaluation: `docs/evaluation/2026-04-12/`
- Decision: `project-log/decisions/2026-04-16-phase-10-hard-enforcement-gates.md`
