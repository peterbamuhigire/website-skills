# Engine Glossary

**Purpose**: Canonical names for every concept, skill, artefact, deliverable,
gate, and stage in the website-agency engine.

**Authority**: This file is the single source of truth for naming. Any
divergence in other docs is drift.

**Enforcement**: `scripts/drift-check.sh` parses this file and fails the build
on references that contradict it.

**Update rule**: An entry here changes only through a decision entry under
`project-log/decisions/`. Renames require a deprecation entry per
`docs/deprecation-policy.md`.

## Concepts

- **Engine** — the system in this repository. Not "platform", "stack", or
  "framework".
- **Canonical CI pipeline** — the 15-step GitHub Actions workflow at
  `templates/ci/website.yml` installed via
  `scripts/install-canonical-ci.sh`. Not "main CI" or "agency CI".
- **Five-layer mental model** — commercial / strategy / build / launch /
  governance. Not "phases", "stages" (those terms are reserved elsewhere),
  or "pillars".
- **Phase** — a numbered unit of the roadmap under
  `docs/plans/website-agency-engine/`. Phases are delivered wholesale, not
  incrementally-merged.
- **Workstream** — a numbered sub-unit of a phase. Each phase is made of
  workstreams.
- **Gate** — a blocking check in the canonical CI pipeline. Performance,
  accessibility, visual-QA, security, drift-check, and design-quality-score
  are the named gates.
- **Rubric** — the design-quality-score rubric at
  `skills/design-quality-score/references/rubric.md`.
- **Scorecard** — the rolling quality record. Internal version at
  `dashboards/quality-scorecard.md`; public version at
  `dashboards/public-scorecard.md`.
- **Africa calibration** — the Africa-realistic performance and pattern layer
  defined in `skills/deploy/references/africa-calibration.md` (performance) and
  `skills/africa-excellence/` (patterns, Phase 12).

## Skills (canonical names)

Build skills:
- `i18n`, `language-standards`, `content-writing`, `brand-alignment`,
  `design-reference`, `sector-strategies`, `website-builder`, `design-system`,
  `photo-manager`, `page-builder`, `seo`, `blog-writer`, `deploy`.

Phase 10 enforcement skills:
- `accessibility-audit`, `visual-qa`, `security-gate`.

Phase 11 discipline skills:
- `observability`, `experimentation`, `design-quality-score`.

Phase 12 authority skills:
- `africa-excellence`.

Support and audit skills:
- `seo-audit`, `blog-idea-generator`, `email-sender`, `form-ux-design`,
  `ux-psychology`, `image-compression`, `policy-pages`, `color-selection`,
  `sales-copywriting`, `brand-strategy`, `brand-storytelling`,
  `brand-style-guide`, `cro-audit`, `social-media`, `skill-writing`,
  `skill-safety-audit`, `update-claude-documentation`, `monthly-report`,
  `agency-positioning`, `agency-client-retention`, `they-ask-you-answer`,
  `ecommerce`, `ecommerce-funnel`, `ecommerce-checkout`,
  `ecommerce-analytics`.

Premium agency operating-system skills (added 2026-05-05):
- `website-experience-mapping` — alignment diagrams, customer journey maps,
  experience maps, ecosystem maps, and mental-model diagrams that drive
  sitemap and content architecture.
- `service-blueprint-website-delivery` — frontstage / backstage service
  blueprint for the agency's own delivery operations and SLAs.
- `premium-sales-conversation` — qualification, premium framing, objection
  handling, and the close for premium website agency sales.
- `customer-service-website-ops` — post-launch service language, triage,
  escalation, recovery, and retention.
- `marketing-measurement-system` — KPI tree, customer insight loop, loyalty
  and retention plan, and the quarterly business review that drives budget
  reallocation.

Legacy (superseded):
- `east-african-english` — superseded by `language-standards` as of 2026-03-21.

Do not invent "english-standards", "voice-guide", "a11y", "perf",
"observe", or "experiment" — those are not canonical.

## Gates (canonical names and order)

Order is fixed in `templates/ci/website.yml`. Do not reorder.

1. **install** — dependency install.
2. **lint** — lint + typecheck.
3. **unit** — unit tests.
4. **build** — static build into `dist/`.
5. **e2e-smoke** — Playwright smoke.
6. **metadata-audit** — title, description, OG, hreflang.
7. **perf-gate** — Lighthouse CI perf budgets.
8. **a11y-gate** — axe-core blocking scan.
9. **visual-qa** — Playwright screenshot + structural + AI-slop.
10. **security-gate** — dep audit, headers, security.txt, SRI, secrets, supply-chain.
11. **google-ai-search** — Google AI Overviews / AI Mode readiness based on
    official Search guidance; treats AEO/GEO as SEO for Google.
11. **drift-check** — documentation drift CI.
12. **design-quality-score** — advisory on PR, blocking on main.
13. **deploy** — main only, all gates green.
14. **post-deploy-smoke** — production URL smoke.
15. **rollback-ready** — rollback automation hook.

## Artefacts and deliverables

- **Strategy brief** — `docs/brand-brief.md` in a client project; produced
  by `brand-strategy`.
- **Brand style guide** — `docs/brand-style-guide.md` in a client project;
  produced by `brand-style-guide`.
- **Creative brief** — section in strategy brief; not a separate file unless
  the project scale justifies it.
- **Page-goal map** — section in `seo/` deliverables; not a separate file.
- **Design tokens** — implemented in the client project, provisioned by
  `design-system`.
- **Photo bank** — `photo-bank/` directory with categorised subdirs
  (branding, hero, team, services, gallery, about, testimonials, misc).
- **Project log** — `project-log/` directory in the client project;
  contains `decisions/`, `incidents/`, `monthly/`, and `CHANGELOG.md`.
- **Scorecard (internal)** — `dashboards/quality-scorecard.md`; generated
  weekly.
- **Scorecard (public)** — `dashboards/public-scorecard.md`; regenerated
  quarterly.
- **Onboarding validation report** — `docs/onboarding-validation/<year>/report.md`.
- **Cohort record** — `certification/cohort-<year>-<seq>.md`.

## Reports (directory contracts)

In a client project:

- `reports/a11y/<route>.json` and `reports/a11y/summary.md` — axe-core
  output.
- `reports/perf/lhci/` — Lighthouse CI output.
- `reports/visual/` — Playwright screenshot diff output.
- `reports/security/` — security gate output.
- `reports/bundle/` — bundle size per route.
- `reports/drift/drift-report.md` — drift-check output.
- `reports/design-quality/<template>.md` — design-quality-score per primary
  template.
- `tests/visual/baseline/` — committed visual baselines.

## Stages (engagement lifecycle)

Client lifecycle:

1. **Intake** — qualifying conversation and fit check.
2. **Discovery** — strategy brief production.
3. **Design-system** — tokens, palette, type scale, photography direction.
4. **Page-build** — primary templates through to full set.
5. **SEO + content** — implementation and blog production.
6. **Pre-launch QA** — Phase 10 and Phase 11 gates green.
7. **Launch** — canonical CI deploy with post-deploy smoke.
8. **Retainer or handover** — monthly report rhythm or handover packet.

Use these names exactly. Do not write "kickoff", "build phase", or "go-live"
in engine documentation.

## Person roles

- **Founder** — the engine author and current operations lead.
- **Operator** — a certified person running the engine. Tracks: Strategist,
  Designer/Builder, SEO+Content operator, QA+Launch operator.
- **Programme lead** — named owner of the certification programme (Phase 12).
- **Client** — the buyer of a website build or retainer.
- **End user** — a person using the shipped site.

Do not write "contractor", "freelancer", or "junior" in engine documentation
unless those terms are specifically meaningful in the local context.

## Banned terms

These terms create drift. Do not introduce them into SKILL.md, references,
or plan files.

- "best-in-class" (unmeasurable), "world-class" as an adjective outside plan
  rhetoric, "state of the art", "cutting-edge", "innovative", "synergy",
  "holistic", "robust" (as a filler), "leverage" as a verb in the finance
  sense.
- Dated framing: "as of 2024", "the next quarter", "recently", "currently",
  "at the time of writing". Rewrite to state the fact directly or remove.
- Ambiguous roles: "designer" (write Designer/Builder track operator),
  "developer" (write Designer/Builder track operator or specify).
- Pipeline euphemisms: "smart gate", "soft gate". A gate is blocking or
  advisory; name which.

## Cross-references

- `docs/doc-style-guide.md` — how to write inside the engine.
- `docs/deprecation-policy.md` — rename and retirement rules.
- `scripts/drift-check.sh` — enforcement of this glossary.
