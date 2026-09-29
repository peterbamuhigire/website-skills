# Project Artifact Contract v1

Each project copies and completes these six artefacts. JSON files validate against the adjacent schemas. Downstream skills must name the version consumed; release evidence records waivers rather than hiding failures.

| Artefact | Producer | Primary consumers |
|---|---|---|
| strategy brief | premium-website-product | website-experience-mapping, content, SEO |
| content inventory | content-writing | page-builder, SEO |
| route map | website-experience-mapping | i18n, page-builder, SEO |
| design tokens | design-system | page-builder, visual-qa |
| measurement plan | marketing-measurement-system | observability, experimentation |
| release evidence | deploy | all quality gates, handover |

The strategy brief may carry an optional `pages` list (`{"route": "/", "visitor_mode": "persuade"}`). `visitor_mode` is one of `persuade`, `operate`, `read` or `experience` (the design engine vocabulary); when a client project keeps the brief at `project-artifacts/strategy-brief.json` (or sets `STRATEGY_BRIEF`), `scripts/slop-scan.sh` scans that page with `--mode`. The slop scan's design-system drift rules read the design tokens artefact when `.chwezi/slop.json` names it (`"tokens": "project-artifacts/design-tokens.json"`) or when a `design-tokens.json` sits in the project root or another folder above `dist/`; otherwise they are `NOT_ASSESSED`. Checked by `tests/test_project_artifacts.py`.
