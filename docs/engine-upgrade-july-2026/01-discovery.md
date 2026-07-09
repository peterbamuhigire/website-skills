# Discovery — Website Skills

## Scope and method

This audit covers only `C:\wamp64\www\website-skills`, inspected 9 July 2026. Before scoring, I enumerated the repository, opened all 59 `skills/**/SKILL.md` files, and read the repository governance surface: `AGENTS.md`, `CLAUDE.md`, `README.md`, `glossary.md`, `docs/doc-style-guide.md`, `docs/deprecation-policy.md`, `docs/licensing-matrix.md`, `docs/roadmap-public.md`, and the meta-skill instructions. I also inspected the canonical CI workflow, root scripts, test tree, asset coverage, stale-route references, duplicate hashes, and obvious temporary artefacts.

## Tree and asset inventory

The repository contains **737 files**, **306 directories**, **7 levels** of maximum observed depth, and **9,360,760 bytes**. It is hierarchical: root governance and operational assets sit beside `skills/`, while 11 categories contain portable skills.

| Category | Skills |
|---|---:|
| agency-ops | 14 |
| brand | 2 |
| build | 6 |
| commerce | 5 |
| content-copy | 10 |
| launch-ops | 4 |
| meta | 3 |
| orchestration | 5 |
| quality-gates | 5 |
| seo-search | 3 |
| ux-conversion | 2 |

Asset types are predominantly Markdown (469 files), followed by 19 shell scripts, four TypeScript files, four Python files, JSON/YAML configuration, a PowerShell bootstrap, a ZIP starter, certification materials, dashboards, decisions, prompts, templates, and visual-test baseline documentation. There are 56 skill-local `references/` directories but no skill-local examples directory containing executable worked examples; the only test asset is `tests/visual/baseline/README.md`. No empty directories or content-hash duplicates were found. One compiled Python artefact is committed: `skills/meta/skill-writing/scripts/__pycache__/quick_validate.cpython-312.pyc`.

The full tree was enumerated recursively during discovery. Material unusual items are: the committed `.pyc`, stale references to relocated skills, a README count of 57 despite 59 actual skills, and a canonical CI deploy path that does not resolve.

## Architecture map

`website-builder` is the main project orchestrator, supplemented by `premium-website-product`, `premium-ui-ux-design`, `website-experience-mapping`, and `africa-excellence`. Its intended flow is commercial/strategy → content/design/build → SEO → deploy → gates → observability/experimentation/retention. Quality gates are centralised in root scripts and `templates/ci/website.yml`; the skills describe handoffs and place deeper guidance in local references. This is a modular architecture with useful hierarchy, but its routers disagree: README/AGENTS say resolve skills from a global table and do not rely on native discovery, while the CI assumes `.claude/skills` and old documentation still names migrated local skills.

## Skill frontmatter register

Every skill has frontmatter and the required acknowledgement. Exact `name` values inspected were: `agency-client-retention`, `agency-positioning`, `authority-offers`, `customer-service-website-ops`, `delivery-automation`, `email-sender`, `launch-campaigns`, `local-in-person-acquisition`, `monthly-report`, `policy-pages`, `premium-sales-conversation`, `referral-program`, `service-blueprint-website-delivery`, `social-media`; `brand-storytelling`, `brand-strategy`; `design-reference`, `design-system`, `i18n`, `image-compression`, `page-builder`, `photo-manager`; `ecommerce`, `ecommerce-analytics`, `ecommerce-checkout`, `ecommerce-funnel`, `retail-commerce-operating-system`; `blog-idea-generator`, `blog-writer`, `content-writing`, `east-african-english`, `french-native-copy`, `language-standards`, `long-form-sales-copy`, `premium-commercial-writing`, `sales-copywriting`, `swahili-native-copy`; `deploy`, `experimentation`, `marketing-measurement-system`, `observability`; `skill-safety-audit`, **`skill-creator`** (in a path named `skill-writing`), `update-claude-documentation`; `africa-excellence`, `premium-ui-ux-design`, `premium-website-product`, `website-builder`, `website-experience-mapping`; `accessibility-audit`, `cross-page-design-consistency-audit`, `design-quality-score`, `security-gate`, `visual-qa`; `google-ai-search`, `seo`, `seo-audit`; and `cro-audit`, `they-ask-you-answer`.

The descriptions claim a broad website and agency operating system: premium commercial positioning; brand, multilingual copy and editorial production; static Astro design/build; retail/ecommerce; SEO and Google AI Search; deployment, security, visual/accessibility/performance QA; African-market calibration; measurement; and agency growth/retention. Notable exact claims include `website-builder` as the “Master orchestrator for building static websites from markdown content and photos”, `accessibility-audit` as the WCAG 2.2 AA hard gate, and `google-ai-search` as an official-guidance layer that rejects AEO/GEO myths.

## Domain contract and benchmark

The engine claims to produce premium, multilingual, accessible, secure, high-performing websites and the agency operating assets that sell, launch, measure, and improve them, especially in African markets. A world-class deliverable is not a visually attractive Astro site alone: it is a strategy-backed, content-credible, accessible WCAG 2.2 AA, performant, secure, searchable, locally appropriate, measurably converting business asset with documented handover and verified release evidence. The benchmark is the combined standard of a leading digital product studio and enterprise web consultancy: GOV.UK-style accessibility discipline, Google Search Central-aligned SEO, Apple/Atlassian-grade system consistency, and a top-tier agency’s signed-off strategy-to-measurement delivery pack.

## Evidence and risks found

- All 59 skills contain the mandatory acknowledgement; all skills with `legacy-guidance.md` reference it.
- Three skills have no local reference material at all: `retail-commerce-operating-system`, `long-form-sales-copy`, and `cross-page-design-consistency-audit`.
- CI has 15 named stages, but uses `SKILLS_DIR: .claude/skills`, contradicting portability guidance. Its deploy command points to `$SKILLS_DIR/deploy/templates/deploy-runner.sh`; neither that path nor `skills/launch-ops/deploy/templates/deploy-runner.sh` exists.
- The local Windows host has no `bash` command on PATH. A Git Bash attempt to run `drift-check.sh` exceeded the 30-second audit window, so no green CI result is claimed.
- `README.md` and `CLAUDE.md` retain obsolete counts and references to relocated design skills. The stale references also occur in templates, plans, and active references, so a future agent can be routed to non-existent files.

Discovery is complete; scoring below is based on this evidence, not on the intended architecture alone.

## Master ranking appendix

| Rank | Engine | Capped score | Verdict |
|---:|---|---:|---|
| 1/1 | website-skills | 65/100 | Broad and disciplined in intent; not yet evidenced as repeatable end-to-end delivery. |
