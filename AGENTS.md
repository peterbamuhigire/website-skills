# Repository Agents Guide

## Universal agent integration

See `.skills-engine/engine-manifest.yaml` for the declarative contract used by the optional universal coordination package. The router and domain SKILL.md files remain authoritative.

The package may read the router, discover skills, inspect Git, and run only declared checks. Missing evidence is NOT ASSESSED; writes, pulls, publication, submissions, ledger/filing changes, deployment, or control changes require explicit approval.

## Mandatory Digital Research currentness gate for Kaizen

Every Kaizen audit, skill edit, reference update, validator change, and
standardisation decision MUST begin with the Digital Research Engine at
`C:\wamp64\www\digital-research-engine`. Read its `source-evaluation` and
`source-verification` skills and the currentness gate reference
`docs/continuous-improvement/kaizen-currentness-gate.md`.

Before admitting any standard, policy, law, technology, platform capability,
software version, command, security control, benchmark, or lifecycle claim,
record source scope, publication/version date, access date, freshness class,
review date, support status, and uncertainty. Use current authoritative
primary sources; quarantine stale/ambiguous/unsupported claims and mark them
`NOT_ASSESSED`. Books are durable concept inputs only.

The shared agent, command, hook, evidence, and handoff contract is mapped to
website work in [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md);
the central registry lives in `C:\wamp64\www\skills-web-dev\docs\engine-control-plane.json`.

## Purpose

This repository is a portable skill library for building websites and related marketing assets.

- In Claude Code, the repository is typically consumed as a skill library inside a client project.
- In Codex, portable skills live under `skills/<category>/<skill-name>/SKILL.md` across 11 thematic categories (agency-ops, brand, build, commerce, content-copy, launch-ops, meta, orchestration, quality-gates, seo-search, ux-conversion).
- `SKILL.md` is the portable execution unit.
- Detailed domain material belongs in `references/`.
- Deterministic helpers belong in `scripts/`.

Do not assume this repository must live under `.claude/skills/`. Resolve local skills by repository-relative paths such as `skills/orchestration/website-builder/SKILL.md` or `skills/build/design-system/SKILL.md`; resolve relocated design skills such as `sector-strategies` through `skills/manifest.yml` and the global engine-routing table. The repository root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant; root-level operational directories such as `scripts/`, `templates/`, `tests/`, and `tools/` are not skills unless they contain their own `SKILL.md`.

## Baseline Rules

- Preserve existing Claude Code behavior unless a task explicitly requires a change.
- Premium is the default commercial standard for this website engine. Website work is accepted only when it can be delivered as a credible business asset with premium strategy, content, SEO, UX, technical quality, measurement, and handover. If the brief cannot support that standard, recommend paid discovery, a smaller premium scope, or a no-bid/no-build decision.
- Prefer the skill-local `SKILL.md` first, then load only the specific files needed from that skill's `references/`.
- Every `SKILL.md` must include this exact acknowledgement line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`
- Treat `references/legacy-guidance.md` as preserved detailed guidance from the pre-standardized version of the skill.
- Do not bulk-load every reference file in a skill. Read only what the current task needs.
- Use bundled scripts when they are the safest or most repeatable path.
- Keep outputs implementation-oriented. Avoid abstract summaries when a concrete deliverable is expected.
- Author or normalise active skills against `docs/skill-authoring-standard.md` and start new entries from `templates/skill/SKILL.md`.
- Before releasing any skill-engine change, run the zero-debt contract validator, routing smoke test, registry validator, tests, canonical per-skill quick validator, and canonical engine scanner. A missing or unavailable check is not a pass.
- When search, AI-answer visibility, crawler policy, structured data, or
  webmaster reporting changes, also run `scripts/validate-search-doctrine.py`.

## Routing

Use these skills as the default router:

- `premium-website-product`: Default premium website product layer. Use for every revenue-critical website and for agency-side positioning where website design itself must be sold as a premium, market-making service.
- `website-builder`: Full website orchestration from docs and assets through deploy readiness.
- `i18n`: Language routing, multilingual structure, and shared versus locale-specific rules.
- `design-reference`: Extracting decisions from example websites.
- `design-system-skills:sector-strategies` or `sectors/legal`: Sector-specific patterns and trust signals.
- `design-system`: Typography, palette, motion, spacing, and visual system decisions.
- `photo-manager`: Image cataloging, naming, dimensions, and logo selection.
- `page-builder`: Converting content and design decisions into pages and reusable UI.
- `seo`: Implementation of metadata, schema, sitemaps, crawler controls, and
  the layered cross-platform discoverability model: SEO foundation, answer
  clarity, probabilistic GEO, entity presence, and post-discovery SXO.
- `google-ai-search`: Official Google Search guidance for AI Overviews, AI Mode,
  AEO/GEO mythbusting, Search Console measurement, local/ecommerce readiness,
  and agentic-experience preparation.
- Do not route ambiguous “AIO” or model-training placement as a separate ranking
  system. Separate training, live retrieval, citation, representation, referral,
  and conversion outcomes.
- `deploy`: Build verification, deployment artifacts, and release readiness. Owns the canonical CI pipeline at `templates/ci/website.yml` and its troubleshooting reference.
- `accessibility-audit`: WCAG 2.2 AA enforcement gate — axe-core, manual checklist, screen-reader smoke scripts. Runs in the canonical CI pipeline as a hard gate.
- `visual-qa`: Rendered-output review loop — Playwright screenshot diff, heading/overflow/empty-section assertions, AI-slop scan. Runs in the canonical CI pipeline as a hard gate.
- `security-gate`: Dependency audit, security headers, `security.txt`, SRI, secrets scan, supply-chain, and Africa + GDPR compliance matrix. Runs in the canonical CI pipeline as a hard gate.
- `observability`: RUM, error tracking, analytics, and alerting contract for every shipped site. Feeds `dashboards/quality-scorecard.md`.
- `experimentation`: Hypothesis template, statistical-significance primer, A/B infrastructure (GrowthBook default), quarterly review.
- `design-quality-score`: 7-category rubric and slop-scan. Runs as canonical CI step 12 (advisory on PR, blocking on main).
- `africa-excellence`: Africa-realistic pattern layer (low-bandwidth, mobile-money UX, USSD-aware, language pack, trust signals, cultural patterns).
- `premium-ui-ux-design`: Premium website UX and visual-quality layer. Use before design-system/page-builder on premium, lead-generation, ecommerce, high-ticket, or public proof work.

Use these cross-cutting skills whenever their lens materially improves the output:

- `language-standards`: Regional language and tone quality; owns the cross-language consistency policy and routes French and Kiswahili to their native-copy skills.
- `french-native-copy`: Native-quality French copywriting execution. Mandatory for any French page, microcopy, email, or metadata; never produce French by raw translation.
- `swahili-native-copy`: Native-quality Kiswahili copywriting execution. Mandatory for any Kiswahili page, microcopy, email, or metadata; never produce Kiswahili by raw translation.
- `premium-commercial-writing`: Premium-fee-worthy commercial writing across website copy, landing pages, blogs, SEO/GEO pages, documents, and offer pages.
- `content-writing`: Website copy structure and clarity.
- `design-system-skills:brand-alignment`: Audience and brand coherence.
- `sales-copywriting`: Conversion-focused messaging.
- `design-system-skills:form-ux-design`: Any user-input flow.
- `design-system-skills:ux-psychology`: Behavioural and heuristic UX review.

Use these support skills on demand:

- `blog-idea-generator`, `blog-writer`
- `brand-strategy`, `brand-storytelling`, `brand-style-guide`
- `color-selection`
- `policy-pages`
- `email-sender`
- `ecommerce`, `retail-commerce-operating-system`, `ecommerce-funnel`, `ecommerce-checkout`, `ecommerce-analytics`
- `agency-positioning`, `agency-client-retention`, `monthly-report`
- `they-ask-you-answer`, `social-media`
- `seo-audit`, `cro-audit`
- `skill-writing`, `skill-safety-audit`, `update-claude-documentation`
- `observability`, `experimentation`, `design-quality-score`, `africa-excellence`

Premium agency operating-system skills (added 2026-05-05):

- `website-experience-mapping`: outside-in alignment diagrams, journey maps,
  experience maps, ecosystem maps, mental-model diagrams. Run before
  page-builder on every premium build that must change behaviour.
- `service-blueprint-website-delivery`: frontstage / backstage blueprint for
  the agency's own delivery operations, SLAs, and recovery. Use during
  proposal scoping, kickoff, and every retainer review.
- `premium-sales-conversation`: structured premium discovery and objection
  handling. Use before any quote, proposal, or scoping document.
- `customer-service-website-ops`: post-launch service language, triage,
  escalation, recovery, retention. Use to design SOPs, train support, and
  recover trust after incidents.
- `marketing-measurement-system`: KPI tree, customer insight loop, loyalty
  layer, and quarterly business review that drives budget reallocation.
- `local-in-person-acquisition`: in-person, door-to-door client acquisition for a
  niche studio — territory and cadence, the free-audit door-opener, walk-in pitch
  and objection scripts, follow-up sequence, pipeline KPIs. Use to run the
  "go in person" channel after the niche is chosen in `agency-positioning`.
- `referral-program`: generous, systematic client referrals — reward structures,
  ask scripts and timing, cross-niche/partner routing, formal tracking and the
  ethics check. Use once clients reach the Advocate phase.
- `delivery-automation`: the agency's own tooling, reusable assets, and workflow
  automation for faster/cheaper delivery — build-vs-buy, the automation-opportunity
  audit, the honest AI-assisted-delivery reality, productized-delivery SOPs.

## Cross-Engine Handoffs

- Proposal to website delivery: consume approved proposal scope, discovery assumptions, content/SEO promises, timeline, commercial exclusions, support package, and acceptance criteria before build planning.
- Proposal to SRS: route portal, ecommerce, SaaS, AI, integration, data, governance, or regulated workflow scope to the SRS engine before committing to page-builder or implementation detail.
- SRS to website delivery: use signed requirements, UX/content/form specifications, acceptance criteria, analytics events, and launch readiness conditions as build inputs.
- Website delivery to Google AI Search: when a brief promises Google AI
  visibility, AI Overviews, AI Mode, AEO/GEO, Search Console AI performance, or
  agentic readiness, route through `google-ai-search` before `seo` and
  `page-builder`.
- Website delivery to implementation: route custom backend, API, SaaS, AI, infrastructure, security, observability, and reliability work to the master engineering engine with clear artefacts and constraints.
- Website launch to observability, experimentation, retention: after launch, route evidence to `observability`, `experimentation`, `marketing-measurement-system`, `agency-client-retention`, `monthly-report`, and `customer-service-website-ops`.
- Website maintenance/support to proposal engine: when support scope, SLA, retainer, or change-request language must be sold or renewed, route commercial wording back to the proposal engine.

## Enforcement and Quality Gates (Phases 10 + 11)

Every project shipped on the engine inherits the 15-step canonical CI pipeline at
`templates/ci/website.yml` via `scripts/install-canonical-ci.sh`. The
pipeline is the single source of enforcement. Adjustments to thresholds or
suppressions require a decision entry under `project-log/decisions/`.

- Canonical commands: `perf-gate.sh`, `a11y-gate.sh`, `visual-qa.sh`,
  `security-gate.sh`, `drift-check.sh`, `slop-scan.sh`,
  `design-quality-score.sh`.
- Canonical configs: `lighthouserc.json`, `performance-budgets.json`.
- Reports directory contract: `reports/bundle/`, `reports/lighthouse/`,
  `reports/a11y/`, `reports/visual/`, `reports/security/`, `reports/drift/`,
  `reports/design-quality/`.
- Visual baseline contract: `tests/visual/baseline/`.
- Africa calibration: `skills/launch-ops/deploy/references/africa-calibration.md` (3G profile,
  350 KB weight budget, Save-Data handling) + `skills/orchestration/africa-excellence/` skill for
  pattern-level standards.

## Governance (Phase 11)

- `glossary.md` — canonical-name authority; `drift-check.sh` enforces.
- `docs/doc-style-guide.md` — writing standards for every file.
- `docs/deprecation-policy.md` — rename and retirement rules.
- `certification/` — operator programme (syllabus, exam bank, cohort records).
- `docs/onboarding-validation/2026/report.md` — multi-operator validation.
- `dashboards/quality-scorecard.md` — internal generated scorecard contract.

## Public Authority (Phase 12)

- `LICENSE` + `docs/licensing-matrix.md` — explicit per-path licensing.
- `docs/roadmap-public.md` — public view of the roadmap.
- `dashboards/public-scorecard.md` — quarterly public quality record.

## Working Model

When a task is ambiguous, follow this order:

1. Identify the smallest skill that fully owns the request.
2. Read that skill's `SKILL.md`.
3. Load only the reference files required for the exact subtask.
4. If the skill depends on upstream artifacts, confirm those artifacts exist before proceeding.
5. If the task spans multiple skills, keep the handoff explicit: note the input artifact, the output artifact, and the next skill that should consume it.

## Quality Expectations

- Preserve repository portability across Claude Code and Codex.
- Avoid product-specific path assumptions in skill instructions and execution.
- Keep `SKILL.md` concise and execution-focused.
- Keep heavy theory, examples, and long-form detail in `references/`.
- Prefer additive changes over restructures.
- Do not duplicate the same logic across multiple skills when a shared reference or upstream skill already owns it.

## Safety

- Run `skill-safety-audit` when a skill changes materially.
- Treat scripts and reference files as part of the skill surface area during review.
- Do not accept hidden side effects, installers, or instructions that bypass repository norms.

<!-- design-system-skills:trigger v1 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`design-system-skills`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from your global engine-routing table** (`~/.claude/CLAUDE.md`,
or `AGENTS.md` for Codex) — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from design-system-skills. Hard rule: never use a banned AI-slop font
(Inter, Geist, Roboto, Arial, Open Sans, Lato, Space Grotesk, bare system stacks) as primary
type — state the chosen typeface and reason before producing any artifact.
<!-- /design-system-skills:trigger -->
<!-- design-system-skills:relocated v1 -->
**Relocated design skills.** These skills were moved OUT of website-skills into the
`design-system-skills` engine (resolve its path from your global routing table). Any reference
to them by name resolves there, NOT in this repo:
`color-selection`, `ux-psychology`, `form-ux-design`, `brand-style-guide`, `brand-alignment`,
`sector-strategies`, `legal` (now `legal-sector-ui-ux`), `data-visualization`,
`premium-ui-ux-design` (the general design version; website keeps its build-coupled orchestration entry).
Still build-coupled and kept here: `design-system`, `page-builder`, `visual-qa`, `website-builder`.
<!-- /design-system-skills:relocated -->

## Human-English editorial standard (2026-08 Kaizen)

Load [`book-extractions/human-english-craft-synthesis-2026.md`](book-extractions/human-english-craft-synthesis-2026.md) for every web page, landing page, blog, SEO/GEO asset, CTA, form, error message, email, and support message. Apply its five passes with `language-standards`, `content-writing`, `premium-commercial-writing`, the relevant native-copy skill, and the anti-slop/visual/accessibility gates.

Website copy must be reader-first, specific, grammatical, scannable, and honest about the offer, proof, process, limits, and next action. Do not create “human” copy with fake colloquialisms, errors, generic welcome language, keyword stuffing, or unsupported superlatives. Record page job, audience, source/proof map, language and market, state-copy review, proof status, gaps, reviewer, and date.

Apply Digital Research's `docs/continuous-improvement/machine-errors-editorial-gate-2026-09-03.md`
to page copy and repeated interface modules. Review ME1-ME7 for semantic repetition, decorative
symmetry, over-explanation, inflated promise, generic examples, rhetorical mannerisms, and
insight-shaped filler. Preserve repeated navigation, state, accessibility, or legal copy only when
its function is documented; unavailable evidence is `NOT_ASSESSED`.

Apply AS1-AS7 from the shared gate to website visuals and repeated modules. Purple gradients,
glassmorphism, neon glow, AI-beige defaults, decorative editorial scaffolding, and decorative motion
are no-ship choices; record `cli`, `browser`, `llm_only`, or `human_review` evidence and mark missing
render evidence `NOT_ASSESSED`.

## PORTFOLIO CRAFT CONTRACT

Load `C:\wamp64\www\chwezi-engine-agents\docs\operations\portfolio-craft-standard-2026-09-04.md` when available. Build a website one user journey and state at a time: frame the job and conversion, inspect the current page/data flow, implement one meaningful slice with real content and assets, render it at relevant breakpoints, exercise loading/empty/error/focus/consent paths, refine, and record browser/accessibility/performance proof. Motion must explain a state or action; typography, layout, colour, assets, and copy need product reasons. Do not generate an entire site and call it finished. Apply `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure` to kaizen itself. Missing browser, render, live, or stakeholder evidence is `NOT ASSESSED`, never a pass.
