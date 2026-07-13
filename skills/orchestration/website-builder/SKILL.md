---
name: website-builder
description: Use when orchestrating a complete website from approved documents and assets through strategy, content, design, build, SEO, quality gates, deploy readiness, and handover; use page-builder for implementation-only work.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Website Builder
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Own the end-to-end website delivery sequence and explicit handoffs between specialist skills.

<!-- dual-compat-start -->
## Use When

- A multi-page website must be delivered end to end
- several website skills must be sequenced
- launch evidence and handover must be reconciled.

## Do Not Use When

- Use `page-builder` for approved page implementation only, or `premium-website-product` to define the commercial product before delivery.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Approved scope, client content, asset inventory, language plan, and acceptance criteria | Proposal, discovery, client, and project repository | yes | Establish build truth | Stop and route to discovery when commercial scope or required content is absent |

## Workflow

1. Validate scope, authority, languages, content, and assets
2. Route strategy and experience mapping before design and implementation
3. Coordinate page, search, accessibility, visual, security, and release gates
4. Stop on any hard gate, repair through its owning skill, rerun the gate, then assemble handover evidence.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Deploy-ready website and handover pack | Client, deploy, and support operations | Approved routes render, all hard gates pass, and rollback, ownership, and measurement evidence exist |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Route map, gate results, release evidence, and handover record | Release owner | Every promised page and acceptance criterion maps to inspected evidence |

<!-- dual-compat-end -->
## Capability Contract

Read, search, edit, and execution are required for an authorised build. Network, deployment, external publication, spending, and production mutation require explicit project authority; delegation is limited to bounded independent work.

## Degraded Mode

Fallback: if build, render, network, or deployment capabilities are unavailable, return the narrowest qualified readiness pack, mark affected gates `not assessed`, and do not claim deploy readiness.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Scope and content approved | Enter implementation sequence | Rework and fabricated content |
| Any hard quality gate fails | Block release and return to the owning skill | Defective deployment |

## Quality Standards

- Maintain one source for routes, content, tokens, and acceptance; all inherited hard gates must pass before deployment is described as ready.

## Anti-Patterns

- Starting page code before scope and content approval. Fix: complete intake and route mapping first.
- Letting specialists silently change scope. Fix: record decisions and return commercial changes to the owner.
- Calling a successful build deploy-ready. Fix: require accessibility, visual, security, SEO, and rollback evidence.
- Duplicating locale markup. Fix: use shared templates and locale data.
- Treating an unavailable render as passed. Fix: mark visual gates `not assessed` and block readiness.

## Worked Example

A bilingual services site has approved copy but no French native review. Build shared routes, block French release, and hand the locale to `french-native-copy` before rerunning visual and search gates.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- The user wants a full website build, rebuild, or end-to-end orchestration.
- The task matches this domain: Master orchestrator for building static websites from markdown content and photos. Use when the user says "build a website", "create a site", or references docs/ content. Reads content from docs/, photos from photo-bank/, and generates a complete Astro website.

## Preserved Domain Exclusions
- The user only needs one narrow subtask and does not need pipeline coordination.
- Core project inputs do not exist yet and the task is still discovery-only.

## Preserved Domain Inputs
- Project docs, content, assets, and any language configuration.
- A working target project or implementation area.

## Preserved Domain Workflow
1. Read the core project inputs before generating or changing anything.
2. Route work through sibling skills in the right order using directory-relative names, not a hardcoded install path.
3. Track outputs from each stage so downstream steps consume the correct artifacts.
4. Verify the full pipeline before reporting completion or blockers.
5. For every commercial build, apply `premium-website-product` before page production
   so the site is treated as a premium market asset: strategy, content, SEO, UX,
   conversion, technical quality, launch, measurement, and handoff are planned together.
6. For premium, ecommerce, or revenue-critical builds, apply the premium website
   engine so strategy, acquisition, conversion, measurement, and handoff artifacts are
   planned before page production starts.
7. For retail commerce builds, load `skills/commerce/retail-commerce-operating-system/SKILL.md`
   before page production so product data, search/navigation, PDP, checkout, fulfilment,
   returns, loyalty/CRM, analytics, POS/inventory, and finance/control handoffs are scoped.
8. Before `design-system` and page production on premium or revenue-critical work,
   load `premium-ui-ux-design` so visual voice, conversion hierarchy, color,
   imagery, dashboard/proof presentation, and production polish are explicit.
9. When the brief promises Google AI visibility, AI Overviews, AI Mode, AEO/GEO,
   or agentic readiness, apply `google-ai-search` before `seo` and page
   production so Google-specific work is grounded in official Search guidance.

## Preserved Domain Quality Guidance
- Preserve the intended build order and artifact handoffs.
- Stay portable across Claude Code and Codex installs.
- Report clearly what was built, skipped, or blocked.
- Every project ships through the canonical CI pipeline at
  `templates/ci/website.yml`. A build that does not pass every gate is not
  considered shipped on the world-class engine.

## Build Contract

Every project built under this orchestrator must satisfy:

1. **Performance gate** — `perf-gate.sh` passes Lighthouse and route weight
   budgets at 3G simulation (`deploy/references/performance-gate.md`).
2. **Accessibility gate** — `a11y-gate.sh` passes WCAG 2.2 AA with zero
   serious or critical axe violations (`accessibility-audit/SKILL.md`).
3. **Visual QA** — `visual-qa.sh` passes screenshot diff, structural
   assertions, and AI-slop scan (`visual-qa/SKILL.md`).
4. **Security gate** — `security-gate.sh` passes dependency audit, security
   headers, `/.well-known/security.txt`, SRI, secrets scan, and supply-chain check
   (`security-gate/SKILL.md`).
5. **Design quality score** — the rendered-output rubric score is recorded
   and meets the world-class floor (`design-quality-score/SKILL.md`).
6. **Premium UI/UX gate** — premium, ecommerce, lead-generation, and
   high-ticket projects pass `premium-ui-ux-design/SKILL.md` before build sign-off
   and again after visual QA.
7. **Premium website product gate** - commercial websites pass
   `premium-website-product/SKILL.md` so content, SEO, conversion, launch,
   handover, stack philosophy, and agency proof are not bolted on after design.
8. **Africa calibration** — performance, trust, and UX patterns align with
   `africa-excellence/SKILL.md` and `deploy/references/africa-calibration.md`.
9. **Live telemetry** — RUM, error tracking, and analytics are wired per
   `observability/SKILL.md`.
10. **Google AI Search readiness** — projects that mention AI Overviews,
   AI Mode, AEO/GEO, or Google agentic experiences pass
   `google-ai-search/SKILL.md` before SEO implementation.

Any gate failure blocks deploy.

## Preserved Domain Anti-Patterns
- Do not assume the skills live only under `.claude/skills`.
- Do not start generation before reading the project inputs.
- Do not skip downstream verification.
- Do not claim a project is shipped on the engine without the canonical CI
  pipeline installed and green.

## Preserved Domain Outputs
- Build plan, orchestrated execution notes, generated artifacts, or a blocker report.

## Preserved Domain References
- Use `references/intake-questionnaire-template.md` when the project still needs structured intake or discovery capture before build orchestration.
- Use `references/website-strategy-brief-template.md` as the canonical source-of-truth artifact before design and build work begins.
- Use `references/project-artifact-standard.md` to confirm the minimum project artifact set before orchestrating downstream work.
- Use `references/discovery-to-build-artifact-map.md` to hand off discovery outputs into sibling skills explicitly.
- Use `references/project-stage-gates.md` to verify the current gate and required approvals before moving phases forward.
- Use `references/kickoff-template.md` when converting sold scope into delivery facts for production.
- Use `references/role-based-training-map.md` when onboarding operators or assigning ownership by role.
- Use `references/governance-policy.md` for repository change rules, safety-review expectations, and deprecation discipline.
- Use `references/quality-metrics-dashboard-definition.md` when connecting repository evolution to commercial and delivery metrics.
- Use `references/premium-website-engine-playbook.md` when the project is for a
  premium client, ecommerce client, high-ticket service business, lead-generation site,
  or any engagement where the website must operate as a measurable business asset.
- Use sibling skill `premium-ui-ux-design` for premium visual direction, conversion
  hierarchy, color/imagery/data presentation, production polish, and the premium
  website gate.
- Use sibling skill `skills/commerce/retail-commerce-operating-system/SKILL.md`
  when ecommerce depends on retail operating systems, inventory, fulfilment,
  returns, loyalty, POS, ERP, or dashboards.
- Use sibling skill `premium-website-product` for premium website service packaging,
  owner-facing content/SEO strategy, stack philosophy, launch campaign discipline,
  handover, measurement, and agency proof.
- Use sibling skill `google-ai-search` when Google AI Overviews, AI Mode,
  Search Console AI performance, AEO/GEO mythbusting, or agentic readiness is
  in scope.
- Use `references/maintenance-calendar.md` for weekly, monthly, quarterly, and annual review cadence.
- Use `references/agency-operations-handbook-index.md` as the index into the broader agency playbook library.
- Route to sibling skill `launch-campaigns` when the website brief includes a timed offer, campaign window, waitlist, announcement, webinar, or coordinated prelaunch/launch/follow-up sequence.
- After intake is complete and before build starts, resolve this engine path
  from the global routing table and install the canonical CI pipeline:
  `bash "$WEBSITE_SKILLS/scripts/install-canonical-ci.sh" <project-path>`.
- The sibling gate skills the orchestrator is responsible for invoking:
  `accessibility-audit`, `visual-qa`, `security-gate`, `observability`,
  `design-quality-score`, `premium-website-product`, `premium-ui-ux-design`,
  `google-ai-search`, and `africa-excellence`.
