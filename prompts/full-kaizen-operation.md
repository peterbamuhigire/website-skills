# Website Full Kaizen Operation Prompt

Paste the prompt below at the root of a website project built with the Website Skills Engine.

## Configuration

```text
Project/product name: [DISCOVER]
Repository or project root: [CURRENT DIRECTORY]
Primary audience and market: [DISCOVER]
Primary business and user outcomes: [DISCOVER]
Critical journeys and conversions: [DISCOVER]
Production URL or preview URL: [NONE OR URL]
Analytics and user-evidence sources: [DISCOVER]
Known incidents, complaints, or defects: [NONE OR LIST]
Constraints: [BUDGET, DEADLINE, STACK, LEGAL, BRAND, OTHER]
Cycle ID: [YYYY-MM-DD-short-name]
Improvement authority: project-local reversible edits are authorised; external actions are not
```

## Prompt

You are the Kaizen lead for this website product. Run a complete, evidence-backed improvement operation on the current project. Do not merely review it or return advice. Inspect the real artefacts, freeze an honest baseline, implement the smallest high-value reversible improvements within authority, validate the results, standardise proven learning in the project, and leave a reproducible next-cycle handoff.

### Governing routes

Before planning or editing:

1. Read every applicable `AGENTS.md` from the project root upward and inspect the worktree without overwriting unrelated changes.
2. Resolve the canonical `website-skills` repository from the global engine-routing table.
3. Read its `AGENTS.md`, `skills/manifest.yml`, `skills/orchestration/website-builder/SKILL.md`, and `skills/quality-gates/kaizen-engine-and-product-improvement/SKILL.md`.
4. Load only the website skills required by the actual findings. Include the premium website product layer for revenue-critical work and the canonical accessibility, visual, performance, security, SEO, observability, and design-quality gates when applicable.
5. Resolve `design-system-skills` and read its router, doctrine, and matched skills for any typography, colour, layout, interaction, or rendered-output change.
6. Resolve `digital-research-skills`; use source evaluation and verification for current search, platform, accessibility, legal, market, or standards claims.
7. Read `docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md` in the Digital Research engine.

### Authority and stop rules

- Treat this prompt as authority for read-only inspection and reversible edits inside the current project only.
- Do not deploy, publish, change DNS, modify production data, contact users, purchase services, rotate live credentials, or change a canonical engine repository without separate authority.
- Stop execution and return a safe plan if the target is unclear, client data is exposed, a destructive migration is required, no rollback exists, or an action crosses the authority boundary.
- When a tool, render, analytics source, reviewer, or credential is unavailable, record the check as `NOT ASSESSED`; never turn absence into a pass.
- Preserve negative evidence and failed experiments. Do not manipulate weights to improve the score.

### Phase 1: Observe and establish the evidence pack

Create `docs/kaizen/<cycle-id>/` and maintain these files as work proceeds:

- `00-scope-and-evidence.md`
- `01-baseline-scorecard.md`
- `02-improvement-backlog.md`
- `03-experiment-log.md`
- `04-validation-record.md`
- `05-final-report.md`
- `06-next-cycle.md`

Inventory the repository, framework, routes/pages, content sources, design tokens, components, forms, integrations, analytics, tests, CI, deploy configuration, performance budgets, security controls, prior reports, and unresolved defects. Identify the intended audience, page goals, critical journeys, device/network context, locales, consent needs, owners, and release constraints. Capture the current git state and exact commands needed to reproduce checks.

If a runnable build exists, start it safely and inspect representative desktop and mobile renders plus loading, empty, error, validation, success, keyboard, reduced-motion, slow-network, and recovery states. Do not claim interaction or responsiveness from source inspection alone.

### Phase 2: Freeze the capped baseline

Score each dimension from 0 to 100 with concrete evidence, confidence, one-line deficiency, and `PASS`, `FAIL`, `BLOCKED`, or `NOT ASSESSED`. Weight each dimension equally unless an existing project rubric has approved weights:

1. Business purpose, audience fit, value proposition, and page goals.
2. Information architecture, navigation, findability, and critical journeys.
3. Content accuracy, specificity, trust, language quality, and rights/provenance.
4. Visual system, brand coherence, responsive layout, states, and anti-slop quality.
5. Accessibility, semantics, keyboard use, focus, forms, contrast, motion, and media alternatives.
6. Performance and resilience on representative mobile devices, constrained networks, and Save-Data conditions.
7. Technical SEO, metadata, schema, crawlability, internal links, local/ecommerce readiness, and evidence-bounded AI-search claims.
8. Conversion ethics, CTA clarity, forms, commerce, consent, error recovery, and trust signals.
9. Security, privacy, dependencies, headers, secrets, data handling, and abuse controls.
10. Analytics, observability, deployment, rollback, maintenance ownership, and post-launch learning.

Use the following exhaustive audit checklist inside those dimensions. Inspect every route, template, reusable component, locale, breakpoint, and meaningful state; do not infer site-wide quality from the home page.

#### UI and UX

- Verify audience-task fit, first-use comprehension, wayfinding, navigation depth, search, breadcrumbs, information scent, CTA priority, task completion, backtracking, and recovery.
- Exercise header, footer, menus, drawers, modals, tabs, accordions, carousels, forms, authentication, checkout/booking, search/filter/sort, pagination, downloads, embeds, and outbound journeys where present.
- Inspect default, hover, active, focus, selected, disabled, loading, skeleton, empty, validation, error, success, offline, timeout, permission-denied, and recovery states.
- Test keyboard order, visible focus, skip links, touch targets, zoom/reflow, reduced motion, screen-reader names, error announcements, autofill, password managers, and mobile keyboards.
- Check mobile-first behaviour on narrow and wide phones, tablets, laptops, large screens, portrait/landscape, long content, magnification, and constrained networks.

#### Style, general design, and design-system fidelity

- Audit brand alignment, visual concept, distinctiveness, typography, type scale, line length, hierarchy, palette, contrast, grid, spacing rhythm, alignment, density, borders, radii, elevation, iconography, illustration, charts, motion, and whitespace.
- Verify token use, component variants, cross-page consistency, deliberate exceptions, dark/high-contrast themes, print styles, and browser/platform differences.
- Check that visual hierarchy supports the page goal; decoration must not compete with comprehension, trust, or action.
- Compare implemented renders with approved design sources and record drift. Never approve a changed visual baseline without human inspection.

#### Content and commercial truth

- Read every visible page, navigation label, CTA, form label, helper text, validation/error message, confirmation, email-triggering message, metadata field, FAQ, legal/policy page, and structured-data value.
- Verify claims, names, dates, prices, addresses, contacts, credentials, testimonials, case studies, statistics, guarantees, availability, and calls to action against approved sources.
- Check specificity, audience language, scanning, answer-first structure, objections, trust, tone, grammar, duplication, broken promises, stale content, placeholder text, and content-design fit.
- Confirm legal, privacy, cookie, returns/refunds, terms, accessibility, and regulated-sector content is present and professionally reviewed when required.

#### Languages and translations

- Build a route-and-string parity matrix for the primary language and every secondary language, including navigation, footer, pages, forms, validation, system states, emails, metadata, schema, image text, alt text, consent, and legal content.
- Route French to the French native-copy skill and Kiswahili to the Kiswahili native-copy skill. Never accept raw machine translation or word-for-word translation as finished copy.
- Review each locale for native meaning, tone, terminology, grammar, cultural fit, reading length, line breaks, truncation, font glyph coverage, names, dates, numbers, currencies, units, phone/address formats, and locale-specific search intent.
- Verify language switcher behaviour, persistent locale choice, canonical/hreflang rules, translated URLs where required, fallback behaviour, missing-key handling, and absence of mixed-language screens.
- Mark a locale `NOT ASSESSED` when no qualified native reviewer or authoritative glossary is available; do not inherit a pass from the primary language.

#### Images, video, icons, and other media

- Create or verify an asset manifest covering source, rights/licence/consent, owner, purpose, dimensions, crop, focal point, format, file size, colour profile, variants, and renewal/expiry where relevant.
- Inspect logo correctness, image relevance, authenticity, cultural/context fit, consistency, composition, art direction, responsive crops, retina density, captions, credits, and text embedded in images.
- Check descriptive alt text, decorative-image treatment, complex-image alternatives, video captions/transcripts, audio controls, autoplay, motion, poster frames, and reduced-data fallbacks.
- Validate responsive `srcset`/`sizes`, modern formats with fallbacks, compression, lazy/eager loading, priority hints, intrinsic dimensions, layout shift, broken assets, CDN/cache behaviour, and low-bandwidth substitutions.
- Reject irrelevant stock imagery, fake people or events, anatomy/text artefacts, inconsistent AI-generated styles, rights ambiguity, and images used to manufacture social proof.

#### Technical, search, trust, and operations

- Verify browser console/network errors, semantic HTML, client/server boundaries, hydration, third-party scripts, consent ordering, dependency health, secrets, headers, abuse controls, and data minimisation.
- Crawl internal and external links; inspect status codes, redirects, canonicals, robots, sitemap, metadata, Open Graph/social cards, structured data, pagination, search filters, and duplicate/thin/orphan content.
- Check event names, triggers, consent, deduplication, conversion definitions, error/RUM signals, dashboards, alerts, ownership, backup, deploy, smoke test, rollback, content maintenance, and incident response.

Show dimension scores, raw overall calculation, and `published_baseline = min(raw_overall, 65)`. Freeze this baseline before making improvements. List all release blockers separately; no average may cancel a blocker.

### Phase 3: Select root causes and plan to 95

Convert findings into a P0/P1/P2 backlog. Prioritise user harm, legal/accessibility/security risk, broken critical journeys, repeated defects, missing evidence, and root causes before cosmetic expansion. For every action record:

- dimension, observed gap, evidence, and affected users/pages;
- root cause and owning file, component, skill route, test, or process;
- falsifiable hypothesis and expected outcome;
- owner, effort, dependencies, and due date;
- primary measure plus accessibility, trust, security, performance, and conversion guardrails;
- smallest reversible change, blast radius, stop condition, and rollback method;
- exact acceptance evidence and re-audit date;
- expected contribution toward the 95/100 target.

Choose the smallest set of changes that can materially improve the product. Do not add pages, animation, AI, dependencies, tracking, or design novelty without a demonstrated user or business need.

### Phase 4: Run controlled improvement cycles

Implement one bounded change at a time. Before each edit, record the hypothesis, baseline measure, guardrails, rollback, and files in scope. After each edit:

1. Run the narrowest relevant automated checks.
2. Inspect the changed journey or render at representative viewports.
3. Test the failed path, not only the happy path.
4. Compare before/after evidence and counter-metrics.
5. Accept, revise, or roll back the experiment using the predeclared rule.
6. Commit no change and update no visual baseline merely to hide a regression.

Continue through authorised P0 items and the highest-value safe P1 items. If genuine outcome measurement needs time or production traffic, implement only the measurement-ready change and mark the outcome pending.

### Strict anti-AI-slop gate

Apply the engine's anti-AI-slop rules while inspecting and editing, after every major iteration, and again as the final release gate. A grade F or any fabricated claim, fake testimonial, fake case study, fake statistic, misleading image, raw machine translation, inaccessible decorative excess, or unreviewed AI feature blocks release.

Actively find and remove generic hero copy, empty superlatives, repetitive three-card sections, interchangeable feature grids, default bento layouts, gratuitous gradients/glows/orbs, excessive pill shapes, random icons, emoji decoration, template-like spacing, over-smoothed brand voice, repeated sentence patterns, vague CTAs, keyword padding, synthetic testimonials, placeholder counters, and unjustified animation. Do not replace these with a different trend. Rebuild from the organisation's evidence, audience tasks, content hierarchy, brand character, and measurable page goal.

Treat visual AI slop as a defect: inconsistent people or products, malformed hands/text/logos, impossible lighting, plastic skin, mixed illustration styles, culturally implausible scenes, fake documentary evidence, and assets with unclear rights. Record each finding, owning file/component, correction, and before/after render. A polished appearance is not evidence of originality, usability, accessibility, or trust.

### Phase 5: Validate the integrated product

Discover and run the project's documented install, lint, type, test, build, and CI commands. Run applicable website gates for:

- broken links, headings, landmarks, overflow, empty sections, and browser journeys;
- WCAG 2.2 AA automated checks plus the manual keyboard and screen-reader smoke checklist;
- responsive visual comparison and design-quality scoring;
- bundle size, Core Web Vitals or Lighthouse budgets, image/font loading, caching, and constrained-network behaviour;
- dependency and secrets scanning, headers, `security.txt`, SRI where relevant, privacy and consent;
- metadata, canonical URLs, robots, sitemap, structured data, local/ecommerce search requirements;
- analytics event correctness, error monitoring, alerts, deployment checks, and rollback readiness.

Record the exact command, environment, result, output path, and limitation for every check. A green structural test is not proof of production behaviour.

### Phase 6: Standardise, teach, and re-measure

For every accepted improvement, update the project source of truth: component, content file, token, test, fixture, runbook, decision record, quality budget, or release gate. Remove temporary duplication. Record rejected experiments and why they must not be repeated.

Re-score only with new evidence. Report the raw re-score and whether 95/100 is actually evidenced. Do not cap the re-score, but do not claim 95 merely because the plan targeted it. Retain unresolved blockers, residual risks, `NOT ASSESSED` checks, evidence owners, and dates.

Write `05-final-report.md` with an answer-first summary, before/after table, implemented changes, validation results, rolled-back tests, release verdict, and remaining risks. Write `06-next-cycle.md` with the next smallest experiment, trigger, owner, evidence needed, and re-audit date. Add an engine-learning proposal only when the finding is repeatable across projects; do not edit the engine itself.

### Final response

Return a concise handoff containing: published baseline and raw baseline; evidenced final score; release verdict; P0/P1 changes completed; validation commands and results; rolled-back or pending experiments; blockers and `NOT ASSESSED` items; evidence-pack path; and the next re-audit date. Link directly to the created files. Do not describe work as complete if required evidence is missing.
