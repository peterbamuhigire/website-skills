# Documentation index

This folder holds the engine's reference documents, its source registers and the records of each improvement cycle. The router is [`AGENTS.md`](../AGENTS.md) and the overview is [`README.md`](../README.md); the skills are under `skills/<category>/<skill>/SKILL.md`.

## Reference documents

| Document | What it holds |
|---|---|
| [`skill-authoring-standard.md`](skill-authoring-standard.md) | The July 2026 skill contract and the gates to run before a release. |
| [`doc-style-guide.md`](doc-style-guide.md) | How to write inside the engine. |
| [`deprecation-policy.md`](deprecation-policy.md) | How skills, references and scripts are renamed or retired. |
| [`relocation-map.md`](relocation-map.md) | Skills that moved to the design engine and where they resolve now. |
| [`licensing-matrix.md`](licensing-matrix.md) | The licence that applies to each path. |
| [`standards-register.md`](standards-register.md) | The standards the engine follows, with dated verification and review dates; the claims behind it are in [`source-registers/`](source-registers/). |
| [`control-plane-adoption.md`](control-plane-adoption.md) | How the engine exposes its manifest to the optional coordination package. |
| [`approval-enforcement.md`](approval-enforcement.md) and [`approval-adapter.json`](approval-adapter.json) | The release and content actions that need approval, and the preview each one must show. |
| [`ai-prompting/`](ai-prompting/domain-prompt-compilation-contract.md) | The local contract for generating a ready-to-paste prompt for a page or journey. |
| [`benchmark-programme.md`](benchmark-programme.md) | The acceptance rule for claiming 95 or more. |
| [`roadmap-public.md`](roadmap-public.md) | The public roadmap, updated at each quarterly review. |
| [`uganda-services-tiers.md`](uganda-services-tiers.md) | Tiered price ranges for Uganda website services, prepared 2026-06-03. |

## Improvement records

| Folder | What it holds |
|---|---|
| [`kaizen/2026-10-engine-kaizen-pass-2/`](kaizen/2026-10-engine-kaizen-pass-2/README.md) | The second October 2026 cycle (31 October): frozen baseline, backlog, experiments, validation, final report and the next-cycle file. Start with `05-final-report.md` and `06-next-cycle.md`. |
| [`kaizen/2026-10-engine-kaizen/`](kaizen/2026-10-engine-kaizen/README.md) | The first October 2026 cycle (29 October), in the same seven files. |
| [`kaizen/`](kaizen/) (three single files) | The first-wave journey fixture, the first-wave measurement contract and the identity, locale and page-role scan from September 2026. |
| [`continuous-improvement/`](continuous-improvement/) | The 14 earlier kaizen and currentness records from August and September 2026, including the book-source retirement. |
| [`audits/2026-09-29-m10-reaudit/`](audits/2026-09-29-m10-reaudit/README.md) | The measured re-audit of 29 September 2026 (published score 55.2 out of 100). |
| [`audits/`](audits/) (two single files) | The 6 September 2026 kaizen record and its independent review. |
| [`engine-upgrade-july-2026/`](engine-upgrade-july-2026/00-executive-summary.md) | The July 2026 upgrade audit (capped score 65 out of 100) and its implementation and conformance reports. |
| [`plans/`](plans/INDEX.md) | Completed plans and [`NEXT_FEATURES.md`](plans/NEXT_FEATURES.md). |
| [`onboarding-validation/2026/report.md`](onboarding-validation/2026/report.md) | The multi-operator validation report; its status line reads "Template". |
| [`superpowers/plans/`](superpowers/plans/2026-05-04-website-skills-uiux-phase2.md) | A historical work record from May 2026. |

The latest published score and the open items are summarised in the "Quality and improvement" section of the [README](../README.md#quality-and-improvement). Dated claims in the registers are checked by `scripts/validate-source-registers.py`; the calendar of dates that will start failing is in the same section.
