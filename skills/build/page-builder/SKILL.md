---
name: page-builder
description: Use when implementing approved website content, design rules, assets, routes, conversion goals, schema, and analytics as reusable production pages; do not use to invent the design system or write missing native-language copy.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Page Builder
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- Approved page content, design rules, locale routes, assets, SEO, schema, and events are ready for production implementation.
- Astro or the repository's chosen framework needs reusable page templates, components, content loading, interaction states, and route tests.

## Do not use when
- The task is visual-token or component-rule definition; use `design-system` first.
- The task is photo selection/cataloguing or image encoding; use `photo-manager` or `image-compression`.
- Approved content or page goals are absent; stop the affected route instead of inventing them.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Approved page content, page-goal matrix, and acceptance criteria | Content/strategy artefacts | yes | Stop the affected page; do not invent commercial claims or copy. |
| Tokens, components, and state rules | `design-system` | yes | Build only a structural prototype clearly marked incomplete. |
| Asset catalogue and image derivatives | `photo-manager` / `image-compression` | conditional | Use explicit placeholders in development; do not ship them. |
| Locale route map | `i18n` | conditional | Build only approved locales and record missing routes. |
| Framework, build, analytics, SEO, and schema contracts | Repository/upstream skills | yes | Stop at an implementation plan if contracts conflict. |

## Workflow
2. Stop the affected route when approved content, page goals, design rules, or route contracts are missing.
3. Choose the smallest set of references needed for the current job.
3. On commercial websites, preserve the `premium-website-product` brief: page goal, search intent, proof, CTA, schema, analytics event, and developer-quality evidence must survive implementation.
4. Produce the implementation, configuration, or guidance this skill owns.
5. Exercise decision, error, empty, loading, disabled, focus, and locale states where applicable.
6. Run build, route, accessibility, responsive, schema, and event checks available in the repository.
7. Recovery: if a check fails, retain the last working slice, isolate and repair the page/component, then rerun the failing acceptance check.

## Quality standards
- Each route preserves its approved audience, goal, proof, CTA, schema, event, and locale contract.
- Reusable components cover applicable loading, empty, error, focus, disabled, and reduced-motion states.
- Build, route, accessibility, responsive, and integration evidence names failures and unassessed checks.

## Anti-patterns
- Inventing missing copy or proof. Fix: stop and request the approved source.
- Rebuilding patterns per page. Fix: create one accessible reusable component.
- Shipping only the happy state. Fix: implement all applicable states.
- Dropping page-goal metadata. Fix: trace CTA, schema, and event acceptance per route.
- Calling source inspection a visual pass. Fix: render or mark visual checks not assessed.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- **Never write a generic author bio on blog or article pages.** The author bio must be specific to the article's topic — describing the author's (or organisation's) credentials and experience *relevant to what the article covers*. See `blog-writer/references/article-design.md` → Author Bio Standard for the full rule, examples, and bilingual requirements.
- Do not ship missing loading, empty, error, focus, or disabled states for interactive components.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Production pages and reusable components | Build/deploy pipeline | Build passes; routes render; content, CTA, schema, analytics, states, and responsive behaviour match approved inputs. |
| Page implementation evidence | QA and project owner | Maps each page goal and acceptance criterion to a test or inspected result. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Build and page QA results | Command output, route matrix, screenshots where available | Failures and unassessed visual checks are explicit. |

## Capability Contract
Inspect source read-only for review requests. Edit application files and run local builds when implementation is authorised. Never publish, change production data, install unapproved dependencies, or invent claims, testimonials, prices, or credentials.

## Degraded Mode
When build, browser, device, font, or network capability is unavailable, implement the smallest locally verifiable slice and list routes, visuals, analytics, schema, and integrations as not assessed. A source review is not a rendered pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Pattern repeats across pages | Build one accessible reusable component | Drift and duplication |
| Content or claim is unapproved | Stop that section and request the source | Fabricated copy |
| Component has interactive states | Implement and test every applicable state | Dead-end UX |
| Framework contract conflicts with brief | Preserve repository behaviour and escalate | Breaking the build |

## Worked Example
Implement a multilingual service template from the approved page-goal matrix, bind locale-safe routes and catalogued imagery, emit the agreed schema and CTA event, then verify build output, keyboard focus, missing-content behaviour, and the mobile layout before marking the route accepted.

## References
- `references/page-conversion-checklist.md` — per-template anatomy, conversion QA gate, instrumentation minimums, pre-launch review. Use when building or reviewing any page.
- `references/authority-content-matrix.md` — content architecture by page type, cornerstone pages, pillar + cluster system, editorial ops. Use when planning the content system for Growth / Authority tiers.
- `references/page-goal-matrix.md` — convert strategy into page-specific audience, goal, proof, CTA, SEO decisions.
- `../premium-commercial-writing/references/website-page-writing-patterns.md` — use when implementation must preserve premium page copy structure for home, service, pricing, about, case-study, contact, or FAQ pages.
- `../premium-commercial-writing/references/professional-writing-quality-gate.md` — use before implementation when supplied copy needs final proof, claim, tone, CTA, and scannability checks.
- `references/conversion-sequence-implementation.md` — use when the build must preserve value-proposition clarity, CTA ladders, cluster linking, or launch-stage page states.
- `../website-builder/references/premium-website-engine-playbook.md` — use when page
  production must preserve the premium strategy, acquisition, conversion, measurement,
  and handoff artifacts for high-value clients.
- `../premium-website-product/references/premium-website-market-asset-gate.md` - use when page production must preserve premium content, SEO, UX, stack, launch, and agency proof requirements.
- `references/legacy-guidance.md` — preserved detailed instructions from the previous skill version.
- `../design-system/references/math-for-web-design.md` — use when implementing pages with fluid type, bounded spacing, intrinsic grids, aspect-ratio media, full-bleed sections, calculated CTA placement, or JS-driven sizing/motion.

<!-- dual-compat-end -->
## Notes
- Route upstream to `launch-campaigns` when page states or CTA swaps depend on campaign timing.
- Route upstream to `sales-copywriting` when the implementation needs revised value propositions, button labels, or objection handling.
- Route upstream to `premium-commercial-writing` when the page copy, SEO/GEO content, document download, blog excerpt, or offer section must meet the premium commercial writing gate before build.

