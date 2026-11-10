# Reference sections moved out of AGENTS.md

Moved verbatim on 2026-11-10 to keep the always-loaded file small (token economy; Codex reads at most 32 KiB of AGENTS.md). Open the section you need.

## Repository Structure

### Skill Categories

Skills are organised under `skills/<category>/<skill>/` in 11 thematic categories:

- **`agency-ops/`** (14) — agency-client-retention, agency-positioning, authority-offers, customer-service-website-ops, delivery-automation, email-sender, launch-campaigns, local-in-person-acquisition, monthly-report, policy-pages, premium-sales-conversation, referral-program, service-blueprint-website-delivery, social-media
- **`brand/`** (2) — brand-storytelling, brand-strategy
- **`build/`** (6) — design-reference, design-system, i18n, image-compression, page-builder, photo-manager
- **`commerce/`** (5) — ecommerce, retail-commerce-operating-system, ecommerce-analytics, ecommerce-checkout, ecommerce-funnel
- **`content-copy/`** (11) — blog-idea-generator, blog-writer, brand-voice, content-writing, east-african-english, french-native-copy, language-standards, long-form-sales-copy, premium-commercial-writing, sales-copywriting, swahili-native-copy
- **`launch-ops/`** (4) — deploy, experimentation, marketing-measurement-system, observability
- **`meta/`** (3) — skill-safety-audit, skill-writing, update-claude-documentation
- **`orchestration/`** (6) — africa-excellence, hospitality-website-product, premium-ui-ux-design, premium-website-product, website-builder, website-experience-mapping
- **`quality-gates/`** (6) — accessibility-audit, cross-page-design-consistency-audit, design-quality-score, kaizen-engine-and-product-improvement, security-gate, visual-qa
- **`seo-search/`** (3) — google-ai-search, seo, seo-audit
- **`ux-conversion/`** (2) — cro-audit, they-ask-you-answer

Always reference skills by their full categorised path: `skills/<category>/<skill>/SKILL.md`.

### Core Build Skills

```text
skills/build/i18n/SKILL.md               <- Multi-language infrastructure
skills/content-copy/language-standards/SKILL.md <- Language and tone standards
skills/content-copy/french-native-copy/SKILL.md <- Native-quality French copy execution
skills/content-copy/swahili-native-copy/SKILL.md <- Native-quality Kiswahili copy execution
skills/content-copy/content-writing/SKILL.md    <- Copywriting standards
chwezi-design-engine:brand-visual-identity <- External brand coherence quality gate (brand-consistency gate reference)
skills/build/design-reference/SKILL.md   <- Reference-site analysis
chwezi-design-engine:sector-strategies  <- External industry design and trust signals
chwezi-design-engine:chwezi-infographics-standard <- External infographic, diagram, map and social-card quality standard (child of the Product Excellence Standard)
skills/orchestration/website-builder/SKILL.md    <- Master orchestrator and system owner for operating references
skills/build/design-system/SKILL.md      <- Fonts, colours, visual identity, motion
skills/build/photo-manager/SKILL.md      <- Asset cataloguing, logo selection, image organisation
skills/build/page-builder/SKILL.md       <- Content to pages and components
skills/seo-search/seo/SKILL.md                <- Search-facing implementation
skills/seo-search/google-ai-search/SKILL.md   <- Google AI Overviews / AI Mode readiness
skills/content-copy/blog-writer/SKILL.md        <- Blog production
skills/launch-ops/deploy/SKILL.md             <- QA, launch checks, deployment, rollback, canonical CI pipeline
skills/orchestration/premium-website-product/    <- Premium website-as-product strategy, content, SEO, stack, launch, and agency proof gate
skills/orchestration/premium-ui-ux-design/       <- Premium website UI/UX and visual quality gate
```

### Enforcement Skills (Phase 10 — added 2026-04-16)

```text
skills/quality-gates/accessibility-audit/SKILL.md <- WCAG 2.2 AA gate: axe-core + manual + screen reader
skills/quality-gates/visual-qa/SKILL.md           <- Screenshot diff + hierarchy/overflow/empty-section + AI-slop
skills/quality-gates/security-gate/SKILL.md       <- Dep audit + headers + security.txt + SRI + secrets + supply chain + compliance
```

### Operating Discipline Skills (Phase 11 — added 2026-04-16)

```text
skills/launch-ops/observability/SKILL.md        <- RUM + error tracking + analytics + alert thresholds
skills/launch-ops/experimentation/SKILL.md      <- Hypothesis template + stat primer + A/B infra + quarterly review
skills/quality-gates/design-quality-score/SKILL.md <- 7-category rubric + slop-scan (CI step 12)
```

Phase 11 also adds: `glossary.md` (canonical names), `docs/doc-style-guide.md`
(writing standards), `docs/deprecation-policy.md` (rename/retirement rules),
`certification/` (syllabus + 60-question exam + cohort records), and
`dashboards/quality-scorecard.md` (generated-artefact contract).

### Authority Skills (Phase 12 — added 2026-04-16)

```text
skills/orchestration/africa-excellence/SKILL.md    <- Low-bandwidth, mobile-money UX, USSD-aware,
                                 language pack, trust signals, cultural patterns
```

Phase 12 also adds: `LICENSE` (MIT + CC BY + CC BY-SA + CC BY-NC + proprietary),
`docs/licensing-matrix.md`, `docs/roadmap-public.md`, and
`dashboards/public-scorecard.md` (quarterly public quality record).

Canonical scripts under `scripts/`: `perf-gate.sh`, `a11y-gate.sh`,
`visual-qa.sh`, `security-gate.sh`, `drift-check.sh`, `slop-scan.sh`,
`design-quality-score.sh`, `install-canonical-ci.sh`, `metadata-audit.sh`,
`post-deploy-smoke.sh`, `rollback.sh`, `validate-checkout-size.py`, and
gate-specific helpers.
Canonical configs at repo root: `lighthouserc.json`, `performance-budgets.json`.
Canonical CI pipeline at `templates/ci/website.yml`.

### Support And Audit Skills

```text
skills/seo-search/seo-audit/SKILL.md               <- Post-build SEO audit
skills/content-copy/blog-idea-generator/SKILL.md     <- Blog ideation
skills/agency-ops/email-sender/SKILL.md            <- Self-hosted contact-form handler
chwezi-design-engine:form-ux-design                    <- External form UX guidance
chwezi-design-engine:ux-psychology                     <- External behavioural UX review lens
skills/build/image-compression/SKILL.md       <- Build-time image compression
skills/agency-ops/policy-pages/SKILL.md            <- Privacy and terms guidance
chwezi-design-engine:color-selection                  <- External colour palette design
skills/content-copy/sales-copywriting/SKILL.md       <- Persuasion and conversion copywriting
skills/brand/brand-strategy/SKILL.md          <- Brand brief development
skills/brand/brand-storytelling/SKILL.md      <- Narrative and story structure
chwezi-design-engine:brand-style-guide                <- External client-facing style guide
skills/ux-conversion/cro-audit/SKILL.md               <- Conversion audit
skills/agency-ops/social-media/SKILL.md            <- Social strategy and service layer
skills/meta/skill-writing/SKILL.md           <- Skill authoring
skills/meta/skill-safety-audit/SKILL.md      <- Skill safety review
skills/meta/update-claude-documentation/     <- Top-level documentation maintenance
```

### External Skill Set

```text
proposal-skills <- Separate proposal-generation engine resolved from the global routing table
```

## Blog & Article Research — Always Use the Digital Research Engine

**Every blog post, article, or thought-leadership piece must be researched with the digital-research-engine before drafting** (applies to `content-copy/blog-writer`, `content-copy/blog-idea-generator`, and any page carrying editorial/blog content). Never write a blog post from assumed knowledge alone. Real examples, statistics, market figures, and cited research must come from a live research wave, with sources verified and credit given to the original authors (named researchers, institutions, regulators).

- **Engine location:** resolve `digital-research-engine` from the device's global engine-routing table. Use the checkout that table names; do not substitute a retired checkout alias.
- **Method:** Start with `research-orchestration/SKILL.md` and run a planned multi-agent wave — one research agent per cohort/region, each briefed per the engine's standard agent-brief structure. The orchestrator does the synthesis; research agents return raw, sourced findings only.
- **Article SEO/SERP standard:** Before drafting any article, run the digital-research-engine's three-wave article study: map intent and 3–7 query clusters; read the accessible top five results for each cluster; then synthesise the content gap, AI-answer opportunities, keyword map, internal links and verified primary-source plan. Use an approved search/API tool rather than direct Google SERP scraping. Record query date, provider, exact queries, result URLs and read status. Treat search visibility as competitive evidence, never as proof or a ranking promise; do not invent search volumes. For bilingual content, research English and French intent separately and translate the decision, not just the words.
- **Attribution is mandatory.** Cite real, locatable sources with URLs; name the student/academic researchers, universities, and regulators whose work you draw on. Mark anything unverifiable as UNVERIFIED — confirm it or frame it without inventing authors, titles, or statistics. Never fabricate a citation. Close each piece with a short "Sources & the researchers worth crediting" block.

## Enforcement and Quality Gates (Phases 10 + 11)

Every project shipped on the engine inherits the 15-step canonical CI pipeline at
`templates/ci/website.yml` via `scripts/install-canonical-ci.sh`. The
pipeline is the single source of enforcement. Adjustments to thresholds or
suppressions require a decision entry under `project-log/decisions/`.

Pipeline order is fixed: install → lint → unit → build → e2e-smoke →
metadata-audit → perf-gate → a11y-gate → visual-qa → security-gate →
drift-check → design-quality-score → deploy → post-deploy-smoke →
rollback-ready. Any gate failure blocks deploy. Thresholds live in
`lighthouserc.json` and `performance-budgets.json` and are non-negotiable.
Full reference: `skills/launch-ops/deploy/references/ci-troubleshooting.md`,
`skills/launch-ops/deploy/references/performance-gate.md`, `skills/launch-ops/deploy/references/africa-calibration.md`.

- Canonical commands: `perf-gate.sh`, `a11y-gate.sh`, `visual-qa.sh`,
  `security-gate.sh`, `drift-check.sh`, `slop-scan.sh`,
  `design-quality-score.sh`.
- Canonical configs: `lighthouserc.json`, `performance-budgets.json`.
- Reports directory contract: `reports/bundle/`, `reports/lighthouse/`,
  `reports/a11y/`, `reports/visual/`, `reports/security/`, `reports/drift/`,
  `reports/design-quality/`.
- Visual baseline contract: `tests/visual/baseline/`.
- Africa calibration: `skills/launch-ops/deploy/references/africa-calibration.md` (labelled
  low-end stress profile, not a median; 350 KB weight budget enforced per category by
  `scripts/route-weight-budget.mjs`; Save-Data handling) + `skills/orchestration/africa-excellence/`
  skill for pattern-level standards. Lab gates block deploy; field p75 decides success; INP is
  enforced from field/RUM data.

## Hard Repository Expectations

- Prefer zero unnecessary JS
- Prefer self-hosted assets over third-party runtime dependencies
- Keep outputs distinctive; avoid generic templates
- Source content from project docs rather than inventing client facts
- Design mobile-first and check multilingual expansion risks
- Treat privacy and terms pages as standard trust infrastructure
- Update top-level docs when the operating model changes materially
- Every skill uses the canonical SKILL.md structure in `docs/doc-style-guide.md`
- Every skill also satisfies the July 2026 contract in `docs/skill-authoring-standard.md`; new skills start from `templates/skill/SKILL.md`
- Run `scripts/validate-skill-contracts.py` against `quality/skill-contract-baseline.json` and `scripts/routing-smoke-test.py` before release; the baseline accepts no findings and routing requires the expected skill in the top three
- Every skill keeps the required acknowledgement line directly under the first `# ...` heading without duplicating it
- Run `scripts/validate-checkout-size.py` before release; it fails closed if either the full checkout or package-oriented entry count exceeds 5,000, symlinks escape the checkout, files cannot be read, or marketplace skill paths/identities diverge from the registry.
- Run `scripts/check_portable_references.py` before release. It fails on machine-specific
  absolute paths (a user-profile path or the local web-server folder) in active content and on any
  Markdown relative link that does not resolve or leaves the checkout; history documents and
  client prompts are held to the ceilings in `quality/portable-references-policy.json`. Write a
  cross-engine reference as a skill name resolved through the engine-routing table
  (`chwezi-design-engine:form-ux-design`), never as a path.
- Canonical names live in `glossary.md`; renames follow `docs/deprecation-policy.md`
- Every project ships through the canonical CI pipeline; if the pipeline
  is not installed and green, the project is not shipped on the engine
- Thresholds in `lighthouserc.json` and `performance-budgets.json` are set
  against a deliberate conservative throttled Slow-4G/3G stress profile
  (WebPageTest "3G" values: 1.6 Mbps, 300 ms RTT, with a 4x CPU slowdown and
  Lighthouse mobile emulation). It is a worst-case floor, not a market median
  (measured Uganda figures found are roughly 5-16 Mbps UCC drive tests and 8.4
  Mbps SpeedOf.Me, each with limits; Ookla and Opensignal for Uganda, Tanzania
  and Rwanda are NOT_ASSESSED); see
  `skills/launch-ops/deploy/references/africa-calibration.md` and
  `docs/source-registers/performance-currentness-2026-09-23.json`. Lab gates
  block deploy; field Core Web Vitals at p75 decide success. INP is enforced
  from field/RUM data, never from Lighthouse navigation runs.
- `scripts/perf-gate.sh` enforces every budget category through
  `scripts/route-weight-budget.mjs` and runs `scripts/html-perf-lint.mjs`.

## Direct-Response Copy for Sales Pages

When building landing pages, sales pages, VSL scripts, webinar funnels,
book funnels, order pages, upsell/OTO pages, or application pages, use
the `long-form-sales-copy` skill, which applies the engine's own
procedures (informed by Kennedy and Brunson, cited in each reference):

- a sales-letter build procedure in six workstreams (promise and
  headline, credibility and honest admissions, offer and value build,
  risk reversal and guarantee, close and postscript, sequence and
  follow-up)
- funnel scripts in five movements, plus webinar closes, one-time
  offers, follow-up email sequences, the phases of a lead and a
  100-visitor test
- an offer-proposition stack (unique selling, value, offer, safety and
  experience propositions) with copy-level price framing

The working procedures live in task-oriented references:
`skills/content-copy/long-form-sales-copy/references/sales-letter-build-procedure.md`,
`funnel-scripts-and-sequences.md` and `offer-propositions-and-price-framing.md`;
price strategy in `skills/agency-ops/authority-offers/references/price-strategy-and-discount-policy.md`;
premium selling in `skills/agency-ops/premium-sales-conversation/references/sales-process-and-takeaway-selling.md`.
Pricing and packages pages use
`skills/content-copy/sales-copywriting/references/pricing-page-choice-architecture.md`;
headline generation and the mandatory direct-response ethics filter use
`skills/content-copy/sales-copywriting/references/headline-families-and-ethics-filter.md`.

For brand-level messaging, use
`skills/brand/brand-storytelling/references/sb7-brandscript-worksheet.md`
(customer = hero, brand = guide) as the upstream foundation; the long-form
procedures then drive the actual sales-page copy.

