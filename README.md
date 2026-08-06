# Website Skills

See [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md) for
website-specific agents, thin commands, lifecycle hooks, evidence, and launch
handoff requirements.

## Mandatory Kaizen contract

Continuous improvement governs the engine and every website it produces. Load
`skills/quality-gates/kaizen-engine-and-product-improvement/SKILL.md` for engine/product audits;
published scores are hard-capped at 65/100 and each plan targets 95/100 with rendered,
accessibility, security, performance, analytics, and reviewer evidence.

Portable website-building and agency-operating skills for Claude Code and Codex.

## Book-derived 2026 capability upgrade

Digital Storytelling, Video Game Storytelling, Designing for AI, Paid for Your Perspective,
Dynamic Characters, LEAN, Applying the Kaizen in Africa, and Facility Move Playbook strengthen
website work with narrative information architecture, empathy, brand expression, meaningful
friction reduction, AI disclosure/control/correction/drift, conversion experiments, accessibility,
readability, security, performance, handoff, and post-launch learning. Websites are treated as
products with evidence-backed iteration and quality gates.

## Kaizen and product-audit contract

Use `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure`.
Publish audits at `min(raw_score, 65)` and target 95/100 with owner, evidence, measure, risk,
rollback, and re-audit. Product audits cover strategy, IA, content, conversion, accessibility,
visual quality, technical quality, SEO, security, performance, handoff, and learning instrumentation.
Route current claims to `digital-research-engine` at `C:\wamp64\www\digital-research-engine` and visual-system decisions to
`design-system-skills`. See `docs/continuous-improvement/` and
`skills/quality-gates/kaizen-engine-and-product-improvement/`.

## Architecture & cross-cutting engines (updated 2026-06-21)

- **No engine is natively discovered anymore.** All skill engines on this machine — including this one — are consulted via the global routing table by globbing `SKILL.md` directly. Do not rely on native skill discovery; read the matching `SKILL.md` files in place.
- **design-system-skills** is the cross-cutting engine for design, typography, UI, UX, visual formatting, and the anti-AI-slop design doctrine. It is **referenced, not mirrored**: resolve its path per device from the global routing table and consult it **in addition** to this engine on visual work.
- **chwezi-accounting-doctrine** (the finance engine) is likewise **referenced, not mirrored**; activate it alongside this engine whenever finance/accounting arises.
- **7 portable design skills were migrated OUT** of this repo to design-system-skills: `color-selection`, `ux-psychology`, `form-ux-design`, `brand-style-guide`, `brand-alignment`, `sector-strategies`, and `legal` (now `legal-sector-ui-ux`). Any name-based reference to a relocated skill now resolves in design-system-skills (a relocation note exists in `CLAUDE.md`/`AGENTS.md`).
- **Build-coupled design skills are KEPT here and now consult the design doctrine** before making visual choices: `design-system`, `page-builder`, `visual-qa`, `website-builder`, and the orchestration `premium-ui-ux-design`. (`design-system` and `visual-qa` were explicitly wired to load the design doctrine first.)
- **Current skill count: 60**, generated and validated from `skills/manifest.yml`.

The machine-readable relocation authority is `skills/manifest.yml`; the human-readable map is `docs/relocation-map.md`.

## Engine integrity

The engine has 60 active skills and one authoring template, discovered from the filesystem. Run these release gates on Windows or Linux:

```powershell
python -X utf8 scripts/validate-skill-registry.py
python -X utf8 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json
python -X utf8 scripts/routing-smoke-test.py
python -m pytest -q
```

The contract baseline is zero debt: it contains no accepted finding. CI runs the same contract, routing, and regression checks on pushes to `main` and pull requests. The canonical CI installer accepts the engine checkout as an explicit second argument and does not depend on `.claude/skills`.

This repository is consumed by reference from the global engine-routing table.
Claude Code and Codex should resolve the local `website-skills` checkout, then
read portable skills under `skills/<category>/<skill-name>/SKILL.md` directly.

Projects share the same skills by referencing the local engine path; they no
longer need a nested skills submodule.

The repository now also functions as a portable website agency engine. It contains build skills plus:

- qualification and intake operations
- strategy and research artifacts
- proof and authority systems
- launch and rollback operations
- governance, onboarding, and maintenance standards

## Portability Contract

- `SKILL.md` is the concise execution layer for each skill
- Skills live under `skills/<category>/<skill-name>/SKILL.md` across 11 categories (see Skill Categories below).
- Every `SKILL.md` must place this exact line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`
- `references/` holds detailed guidance, including preserved `legacy-guidance.md` files
- `scripts/` holds deterministic helpers where a workflow benefits from automation
- [docs/skill-authoring-standard.md](./docs/skill-authoring-standard.md) defines the July 2026 skill contract; new skills start from [templates/skill/SKILL.md](./templates/skill/SKILL.md)
- [AGENTS.md](./AGENTS.md) defines repository-wide routing and working rules for Codex
- Consumers should not assume the repo must live under a host-specific path such as `.claude/skills/`
- The repository root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant. Operational directories such as `scripts/`, `templates/`, `tests/`, and `tools/` stay at root when they serve the repository rather than a single skill.

## Architecture

```text
website-skills/              <- this repo, referenced from the global engine-routing table
|-- AGENTS.md                Repo-wide routing and quality rules
|-- README.md                Overview and operating model
|-- CLAUDE.md                Claude-specific repo guidance
|-- templates/               Client-facing content templates
|-- prompts/                 Project-specific generation prompts
|-- plans/                   Phase plans and system expansion work
|-- docs/                    Evaluation and system documentation
|-- skills/                  Portable skills, organised under skills/<category>/<skill>/SKILL.md
|   |-- agency-ops/          Agency positioning, retention, sales, delivery, comms (14 skills)
|   |-- brand/               Brand strategy and storytelling (2 skills)
|   |-- build/               Design system, page builder, assets, i18n, references (6 skills)
|   |-- commerce/            E-commerce strategy, retail commerce operating systems, funnel, checkout, analytics (5 skills)
|   |-- content-copy/        Blog, sales copy, language standards, native French/Kiswahili copy, premium writing (10 skills)
|   |-- launch-ops/          Deploy, observability, experimentation, measurement (4 skills)
|   |-- meta/                Skill writing, skill safety audit, documentation (3 skills)
|   |-- orchestration/       Top-level orchestrators incl. website-builder, premium product, africa-excellence (5 skills)
|   |-- quality-gates/       Accessibility, visual QA, security, consistency, design score (5 skills)
|   |-- seo-search/          SEO, SEO audit, Google AI Search (3 skills)
|   `-- ux-conversion/       CRO audit and they-ask-you-answer (2 skills)
|-- certification/           Syllabus, exam bank, cohort records (Phase 11)
|-- dashboards/              Internal and public quality scorecards (Phase 11 + 12)
|-- glossary.md              Canonical-name authority (Phase 11)
|-- scripts/                 Canonical runners for every gate (13+ scripts incl. drift-check, slop-scan, design-quality-score)
|-- tests/visual/            Baseline directory contract for visual QA
|-- reports/                 Per-build output directory (bundle, lighthouse, a11y, visual, security, drift, design-quality)
|-- templates/ci/            Canonical CI pipeline inherited by client projects (15 blocking steps)
|-- project-log/decisions/   Decision log for non-obvious trade-offs
`-- LICENSE                  MIT + CC BY + CC BY-SA + CC BY-NC + proprietary (see docs/licensing-matrix.md)
```

## Core Build Skills

- `website-builder`: orchestrates the website workflow and owns cross-skill operating references
- `i18n`: language routing, multilingual structure, and shared versus locale-specific rules
- `design-reference`: extracts design decisions from reference websites
- `sector-strategies`: industry-specific trust patterns and content priorities
- `premium-ui-ux-design`: premium visual direction, conversion hierarchy, color,
  imagery, data/proof presentation, production polish, and premium website gate
- `design-system`: typography, palette, motion, spacing, and visual-system decisions
- `photo-manager`: image cataloging, naming, dimensions, and logo selection
- `page-builder`: converts content and design decisions into pages and reusable UI
- `seo`: metadata, schema, sitemap, and crawler-facing configuration
- `google-ai-search`: applies official Google Search guidance for AI Overviews,
  AI Mode, AEO/GEO mythbusting, local/ecommerce readiness, Search Console
  measurement, and agentic-readiness planning
- `deploy`: verification, release readiness, rollout, rollback, and post-launch checks

## Enforcement Gates (Phases 10–11)

Every project shipped on the engine must pass the 15-step canonical CI
pipeline at `templates/ci/website.yml`. These skills own the blocking gates:

- `accessibility-audit` (Phase 10): WCAG 2.2 AA — axe-core + manual + screen reader
- `visual-qa` (Phase 10): screenshot diff + hierarchy/overflow/empty-section + AI-slop scan
- `security-gate` (Phase 10): dependency audit, headers, security.txt, SRI, secrets, supply chain, compliance
- `drift-check` (Phase 11): dead links, deprecated references, dated framing, banned terms, 500-line rule
- `design-quality-score` (Phase 11): 7-category rubric + slop-scan, advisory on PR, blocking on main
- `premium-ui-ux-design`: premium, ecommerce, lead-generation, and high-ticket
  websites must pass the premium UI/UX gate before build sign-off and after
  visual QA

Canonical commands (runnable from any client project after resolving this
engine path as `WEBSITE_SKILLS`):

```bash
bash "$WEBSITE_SKILLS/scripts/perf-gate.sh"              # Lighthouse + weight budgets on 3G
bash "$WEBSITE_SKILLS/scripts/a11y-gate.sh"              # axe-core against every route
bash "$WEBSITE_SKILLS/scripts/visual-qa.sh"              # Playwright diff + structure + slop
bash "$WEBSITE_SKILLS/scripts/security-gate.sh"          # dep audit + headers + security.txt + SRI + secrets + supply-chain
bash "$WEBSITE_SKILLS/scripts/drift-check.sh"            # documentation coherence gate
bash "$WEBSITE_SKILLS/scripts/slop-scan.sh"              # banned-pattern static scan
bash "$WEBSITE_SKILLS/scripts/design-quality-score.sh"   # aggregate rubric score
bash "$WEBSITE_SKILLS/scripts/install-canonical-ci.sh" <project>  # one-time bootstrap
```

## Operating Discipline (Phase 11)

- `observability/`: RUM, error tracking, analytics, alert thresholds. Every
  shipped site has live telemetry on day one.
- `experimentation/`: hypothesis template, statistical-significance primer,
  A/B infrastructure (GrowthBook default), quarterly review.
- `design-quality-score/`: 7-category rubric (typography, colour, spacing,
  hierarchy, copy, trust, originality); rendered output must score ≥ 8/10
  per category to ship.
- `certification/`: operator syllabus, 60-question exam bank across 4 tracks,
  cohort records.
- `glossary.md`, `docs/doc-style-guide.md`, `docs/deprecation-policy.md`:
  canonical names, writing standards, rename/retirement rules.

## African Authority Layer (Phase 12)

- `skills/orchestration/africa-excellence/`: low-bandwidth patterns, mobile-money UX, USSD-aware
  design, African language pack (10 first-class languages), country trust
  signals, cultural patterns. Replaces generic global defaults for African-
  market projects.
- `LICENSE` + `docs/licensing-matrix.md`: explicit per-path licensing (MIT
  for code, CC BY for skills/references, CC BY-SA for plans, CC BY-NC for
  certification, proprietary for agency-positioning).
- `dashboards/public-scorecard.md`: quarterly public quality record.
- `docs/roadmap-public.md`: curated public view of the roadmap.

## Cross-Cutting Skills

- `language-standards`: regional language and tone quality; owns cross-language consistency and routes French/Kiswahili to their native-copy skills
- `french-native-copy`: native-quality French copywriting execution (mandatory for French copy; never raw-translate)
- `swahili-native-copy`: native-quality Kiswahili copywriting execution (mandatory for Kiswahili copy; never raw-translate)
- `content-writing`: website copy structure and clarity
- `brand-alignment`: audience and brand coherence
- `sales-copywriting`: conversion-focused messaging (cross-cutting quality lens — PASTOR, 4 P's)
- `long-form-sales-copy`: direct-response long-form execution (Kennedy 28-step + Brunson Star-Story-Solution, Perfect Webinar, OTO Bump) for landing pages, VSLs, webinar funnels, book funnels, order pages, application pages
- `form-ux-design`: user-input flow design
- `ux-psychology`: behavioral and heuristic UX review
- `observability`: live telemetry contract for every shipped site
- `experimentation`: structured learning loop on retainer engagements
- `design-quality-score`: rendered-output quality gate and rubric
- `premium-ui-ux-design`: premium website quality gate and book-derived visual
  design playbook
- `africa-excellence`: Africa-realistic pattern layer

## Support Skills

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

## Agency Engine Layers

The repository currently spans five operating layers:

1. Commercial layer: qualification, offers, proposals, proof positioning
2. Strategy layer: discovery, strategy brief, trust architecture, page-goal mapping, search intent
3. Build layer: design system, assets, pages, SEO, and authority content
4. Launch layer: QA, deployment, rollback, observability, review windows
5. Governance layer: training, maintenance cadence, quality metrics, safety review, documentation hygiene

## Current Phase Additions

Recent agency-engine expansion work added the following reference layers:

- `2026-04-14`: Phase 2 added intake, qualification, proposal, kickoff, artifact standards, and stage-gate operations
- `2026-04-14`: Phase 3 added website strategy briefs, competitor synthesis, trust architecture, page-goal mapping, and intent mapping
- `2026-04-14`: Phase 6 added QA matrix, launch verification, deployment and rollback runbooks, observability baseline, and a Playwright starter
- `2026-04-14`: Phase 9 added role-based training, governance policy, maintenance cadence, quality metrics dashboard, and the handbook index
- `2026-04-16`: Phase 10 added hard enforcement gates — `accessibility-audit`, `visual-qa`, and `security-gate` skills; canonical CI pipeline at `templates/ci/website.yml`; 13 canonical scripts; `lighthouserc.json` and `performance-budgets.json`; Africa 3G calibration; deploy + website-builder skill updates. See [Phase 10 decision](./project-log/decisions/2026-04-16-phase-10-hard-enforcement-gates.md).
- `2026-04-16`: Phase 11 added world-class operating discipline — `observability`, `experimentation`, and `design-quality-score` skills; `drift-check.sh`, `slop-scan.sh`, and `design-quality-score.sh` scripts (CI steps 11 + 12); `glossary.md`, `docs/doc-style-guide.md`, `docs/deprecation-policy.md`; certification programme with 60-question exam bank; onboarding validation template; quality-scorecard contract. See [Phase 11 decision](./project-log/decisions/2026-04-16-phase-11-world-class-operating-discipline.md).
- `2026-04-16`: Phase 12 added the African authority engine — `africa-excellence` skill with six references (low-bandwidth, mobile-money UX, USSD-aware, language pack, trust signals, cultural patterns); public scorecard; `LICENSE` + `docs/licensing-matrix.md`; `docs/roadmap-public.md`; they-ask-you-answer continental publishing rhythm.
- `2026-05-16`: Added `google-ai-search` as the official Google Search AI layer
  for AI Overviews, AI Mode, AEO/GEO mythbusting, Search Console measurement,
  local/ecommerce readiness, and agentic-experience preparation. See
  [Google AI Search decision](./project-log/decisions/2026-05-16-google-ai-search-skill.md).
- `2026-05-31`: Added `french-native-copy` and `swahili-native-copy` as the
  native-language copy execution layers under `language-standards`, with deep
  references (French: register, grammar pitfalls, idiom, anglicisms,
  typography, revision checklist; Kiswahili: noun-class concord, verb system,
  register/greetings, idiom/culture, loanwords, numbers/time/dates, revision
  checklist) so French and Kiswahili copy is written natively rather than
  machine-translated. content-copy skill count is now 10. See
  [native-copy decision](./project-log/decisions/2026-05-31-french-swahili-native-copy-skills.md).
- `2026-06-03`: Enhanced `french-native-copy` and `swahili-native-copy` from a
  new set of reference books (OCR'd where the source was a scanned PDF). French:
  expanded `grammar-pitfalls` (multiple-pronoun order, advanced subjunctive,
  country prepositions, tense/mood for CTAs, past-participle agreement,
  articulateurs logiques, mise en relief, gérondif/passive, concordance des
  temps), new `vocabulary-by-theme`, and richer `idiom-and-flow`/`anglicisms`.
  Kiswahili: value-word lexicon, vetted proverbs + cautions, kanga-style lines,
  prestige/variety guidance, colonial-pidgin and tourist-Swahili cautions,
  telling-time fractions, ordinals concord, and Tanzania/Kenya term tables.
  Sources distilled in `book-extractions/{french,swahili}-language-books-extraction-2026.md`.

## Working Model

When a task is ambiguous, follow this order:

1. Identify the smallest skill that fully owns the request.
2. Read that skill's `SKILL.md`.
3. Load only the reference files required for the exact subtask.
4. Confirm required upstream artifacts exist before proceeding.
5. If the task spans multiple skills, make the handoff explicit: input artifact, output artifact, and next owning skill.

## Quality Expectations

- Preserve repository portability across Claude Code and Codex
- Keep `SKILL.md` concise and execution-focused
- Keep heavy theory and examples in `references/`
- Prefer additive changes over restructures
- Avoid duplicating logic already owned by another skill or shared reference
- Treat scripts and references as part of the skill surface area during review
- Keep every active skill at zero contract debt and within the 500-line entrypoint limit
- Require the expected route in the top three for every routing fixture

## Related Docs

- [AGENTS.md](./AGENTS.md) — repository routing and quality rules
- [CLAUDE.md](./CLAUDE.md) — Claude-specific repo guidance
- [CONTRIBUTING.md](./CONTRIBUTING.md) — authoring, validation, and release procedure
- [Skill authoring standard](./docs/skill-authoring-standard.md) — local July 2026 contract
- [docs/plans/INDEX.md](./docs/plans/INDEX.md) — plans index and status
- [docs/plans/NEXT_FEATURES.md](./docs/plans/NEXT_FEATURES.md) — priority roadmap
- [docs/plans/website-agency-engine](./docs/plans/website-agency-engine) — 12-phase master roadmap
- [docs/evaluation/2026-04-12](./docs/evaluation/2026-04-12) — evaluation driving Phase 10–12
