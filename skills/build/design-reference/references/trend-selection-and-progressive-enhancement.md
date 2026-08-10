# Trend Selection and Progressive Enhancement

Use this reference when a client, competitor, article, or inspiration source proposes a current web-design pattern. Convert trend observations into a style decision that fits the particular client, website, audience, offer, content, trust context, and operating environment. This is an independent synthesis, not a reproduction of any source's wording, layout, assets, or claims.

## Contents

- [Evidence boundary](#evidence-boundary)
- [Style-fit gate](#style-fit-gate)
- [Pattern catalogue](#pattern-catalogue)
- [Implementation contract](#implementation-contract)
- [Verification matrix](#verification-matrix)
- [Decision record](#decision-record)

## Evidence boundary

The following supplied sources informed the catalogue:

- [Wavespace website design examples](https://www.wavespace.agency/blog/best-website-design-examples)
- [Converge web design trends](https://enter.converge.ai/blog/web-design-trends)

Treat trend labels, dates, popularity statements, conversion claims, and tool promotion in those sources as source observations or hypotheses. Verify any market, accessibility, performance, or business claim independently before using it as evidence. A source may suggest a direction; it does not establish that a pattern fits a client.

Do not copy a recognisable composition, distinctive interaction, brand treatment, wording, illustration, image, or code. Extract the underlying usability or communication principle and create a differentiated implementation.

## Style-fit gate

Choose the correct matching style before choosing a trend. Start with the client and website, then use the pattern catalogue only to expand or test the direction. If a gate is unknown, mark it `UNASSESSED` and do not present the style as approved.

| Gate | Required question | Evidence | Failure action |
|---|---|---|---|
| Audience | Who must feel confident, oriented, and able to act? What devices, bandwidth, language, age, ability, and familiarity do they bring? | Discovery, research, task tests | Reject a style that creates avoidable distance or confusion |
| User job | What is the primary task, decision, or reassurance the website must support? | Journey, page-goal, and narrative artefacts | Simplify before styling |
| Offer and sector | What is being sold, explained, supported, or trusted? What level of seriousness, warmth, authority, or energy is appropriate? | Offer brief, sector context, proof register | Adapt tone and visual intensity |
| Brand character | Which approved attributes must the experience express, and which must it avoid? | Brand/style brief | Keep unapproved directions exploratory |
| Content reality | Do the actual words, images, data, products, translations, and update cadence suit the proposed hierarchy and density? | Content inventory and states | Choose a style the content can sustain |
| Trust and risk | Does the sector require calm clarity, provenance, safety cues, consent, or high-legibility decision support? | Claims, privacy, regulatory, and support needs | Reject decorative ambiguity |
| Environment | What browsers, phones, network conditions, assistive technologies, and maintenance capacity must be supported? | Technical and operations brief | Prefer resilient progressive enhancement |
| Differentiation | Does the direction make the client recognisable without resembling a reference brand? | Reference synthesis and competitive context | Abstract the principle and redesign |
| Learning | What reversible test and guardrails will show that this style helps the intended job? | Baseline, hypothesis, metrics, and rollback | Do not standardise on taste or fashion |

Record a short style thesis: `For [audience] doing [job], this website uses [style direction] because [brand/offer reason]. It deliberately avoids [misfit] and proves fit through [evidence].`

Use no more than two high-novelty treatments on a page unless testing shows that their combination supports the same user job without harming comprehension, accessibility, performance, trust, or maintenance.

## Pattern catalogue

These are candidate principles, not a checklist or a claim that every pattern is current or suitable.

| Pattern family | Transferable principle | Main risks | Minimum adaptation |
|---|---|---|---|
| Structural geometry | Make the grid, relationships, and hierarchy legible rather than hiding structure behind decoration. | Harsh contrast, poor scanning, inaccessible borders, fatigue. | Preserve readable measure, semantic headings, clear focus, and calm variants. |
| Kinetic type | Let typography carry sequence and emphasis when it reduces dependence on heavy media. | Motion sickness, unreadable text, layout shift, poor screen-reader experience. | Keep text fully available as static content; animate only enhancement layers with reduced-motion and pause controls. |
| Modular information blocks | Group varied proof or features into a responsive, scannable system. | Card soup, unequal priority, cramped mobile layouts. | Define priority order, meaningful headings, intrinsic sizing, and a list/stack fallback. |
| Context-aware experiences | Adapt content or next actions to known intent rather than showing the same path to everyone. | Intrusive tracking, opaque decisions, stale recommendations. | Use declared context first, explain the reason, offer controls, and retain a useful default path. |
| Intent-first minimalism | Remove competing choices so the primary job is obvious. | Missing proof, vague copy, hidden navigation, weak recovery. | Keep evidence, support, accessibility controls, and secondary routes discoverable. |
| Lightweight spatial interaction | Add depth or pointer response to improve orientation or product understanding. | GPU cost, battery drain, motion discomfort, touch mismatch. | Use CSS or static imagery first; lazy-load enhancement; provide a non-spatial equivalent. |
| Dark display modes | Treat dark mode as a complete semantic theme, not an inversion filter. | Contrast failures, halos, colour meaning loss, unreadable media. | Test both themes, preserve semantic status colours, respect system preference, and measure any performance claim. |
| Voice interaction | Offer hands-free input where speech materially improves access or speed. | Privacy, recognition errors, noisy environments, no visible recovery. | Keep equivalent controls and text input; show listening, transcript, confirmation, correction, and denial handling. |
| Live data storytelling | Make changing data understandable through context, trend, source, and timestamp. | Misleading animation, inaccessible charts, stale data, outages. | Provide a table/summary, units, source, last-updated time, empty/error state, and pause option. |
| Browser AR or 3D preview | Reduce uncertainty about physical scale, placement, or appearance. | Unsupported devices, permissions, heavy assets, inaccurate representation. | Provide static media and specifications; request permission late; disclose limitations; test mobile fallback. |

## Implementation contract

For every selected style treatment, `design-system` and `page-builder` must record:

1. the semantic, static baseline;
2. the enhanced behaviour and its trigger;
3. reduced-motion, keyboard, touch, zoom, screen-reader, offline, and low-bandwidth behaviour;
4. content, locale, empty, error, and permission-denied states;
5. byte, CPU, memory, latency, and interaction budgets;
6. privacy, consent, user-control, and data-retention implications;
7. telemetry for the intended task and guardrail metrics;
8. the owner, expiry/review date, rollback path, and evidence needed to standardise it.

Enhancements must be progressively loaded and must not delay the first meaningful task. A visual enhancement that fails, times out, or is declined must leave the user with a complete and honest path to the same outcome.

## Verification matrix

| Surface | Check |
|---|---|
| Semantic baseline | Headings, landmarks, links, forms, content order, and core task work with enhancement code disabled. |
| Responsive | Narrow mobile, wide desktop, touch, orientation, zoom, long labels, and translated content. |
| Accessibility | Keyboard-only, visible focus, screen reader, contrast, reduced motion, captions/transcript, and non-colour status. |
| Resilience | Slow/failed network, blocked third party, missing/stale data, denied permissions, timeout, and retry. |
| Performance | Realistic low-end device and constrained network; record transfer, LCP/INP/CLS, long tasks, and enhancement cost. |
| Trust | Explain adaptation, source/timestamp, consent, correction, privacy controls, and fallback. |
| Learning | Compare the stated task metric against baseline without worsening accessibility, performance, trust, or support outcomes. |

Visual QA proves rendering only; it cannot prove accessibility, privacy, conversion, data accuracy, or integration health by itself.

## Decision record

```yaml
style_thesis: "<audience, job, style, reason, deliberate avoidance>"
pattern: "<family>"
source_observation: "<URL and page/state>"
decision: ADOPT | ADAPT | REJECT | UNASSESSED
principle: "<abstract principle, not copied expression>"
baseline: "<semantic/static implementation>"
enhancement: "<optional behaviour>"
fallbacks: ["<reduced motion>", "<no JS>", "<unsupported device>"]
budgets: {bytes: "<limit>", cpu_ms: "<limit>", latency_ms: "<limit>"}
privacy_controls: "<data, consent, refusal, retention>"
experiment: "<hypothesis, metric, guardrails, duration>"
owner: "<role>"
rollback: "<reversible action>"
evidence: ["<route>", "<test>", "<trace>", "<review date>"]
```

Do not describe a style or pattern as current, effective, accessible, sustainable, or production-ready without the corresponding evidence. Feed verified learning into the owning skill and the two-level Kaizen loop; keep failed and inconclusive experiments in the record.
