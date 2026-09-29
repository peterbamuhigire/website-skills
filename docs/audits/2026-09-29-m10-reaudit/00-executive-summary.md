# Executive summary

**Published overall: 55.2 / 100** (raw 55.3; measured-constrained 55.2; cap of 65
not binding). **Engine Eval Readiness: 59.6 / 100** (measured).

## Verdict

The engine is solid but visibly short of world-class. It is strongest where it
has executable evidence (quality gates, deployment, search currentness) and
weakest where it would need applied proof (worked artefacts, behavioural runs,
end-to-end sample sites) or breadth beyond its core marketing-site path
(catalogue commerce, African languages other than French and Kiswahili).

## Headline findings

1. **Applied proof is the binding constraint (worked examples 40/100).** All 62
   `SKILL.md` files carry a `## Worked Example` section, but each is a one-to-three
   sentence scenario (for example `skills/quality-gates/security-gate/SKILL.md`,
   `skills/build/i18n/SKILL.md`). `examples/` contains two files (one service-page
   prototype). `skills/quality-gates/design-quality-score/references/scored-examples.md`
   states its examples are "descriptive, not real client sites". Tier 3 has zero
   `grading.json` files. No output type has a complete worked deliverable.
2. **Routing precision is high but coverage is thin.** The lexical smoke test gives
   precision@1 35/37 (94.6 %) and 21/21 owned negatives, but only 30 of 62 skills
   have any positive fixture and 1 of 62 has the three positives and two owned
   negatives the coverage slot requires (T2_cov 0.0161). Half the catalogue is
   unrouted by any fixture.
3. **Normalisation is uneven beneath a uniform contract.** The contract validator
   reports zero debt, yet 15 skills still carry `## Preserved Domain …` sections
   that restate the contract in older form, 10 retain the generic trigger "The task
   matches this domain: …" (for example `skills/agency-ops/monthly-report/SKILL.md`),
   32 keep a `references/legacy-guidance.md`, and five skills have no reference
   files at all (`retail-commerce-operating-system`, `hospitality-website-product`,
   `cross-page-design-consistency-audit`, `skill-writing`, plus single-reference
   `photo-manager`, `image-compression`, `east-african-english`).
4. **Two output types are under-served.** E-commerce-lite or catalogue sites (45)
   have no skill for a static catalogue with enquiry, WhatsApp or mobile-money
   ordering; the five commerce skills assume a full store or omnichannel stack.
   African-language delivery (52) claims "10 first-class African languages" in
   `skills/orchestration/africa-excellence/references/african-language-pack.md`
   while only French and Kiswahili have native-copy skills; the speaker figures in
   that table carry no source.
5. **Doctrine contains a contestable owner rule and router drift.** `blog-writer`
   requires every internal link to open in a new tab (`target="_blank"`), which sits
   uneasily with the engine's own accessibility gate (unrequested context changes;
   judged, no fresh external research). The 559-line `AGENTS.md` mixes routing with
   phase history, lists design-engine skills (`brand-style-guide`, `color-selection`)
   as local support skills, and describes `proposal-skills` as external while the
   portfolio routing table says this engine embeds it (no `.gitmodules` exists at HEAD).

## What is strong

- Uniform, validated contracts: `validate-skill-contracts.py` reports "62 active
  skills … zero debt"; `validate-skill-registry.py` reports "registry valid: 62 skills".
- Executable, tested gates: 131 pytest tests pass, including the slop-scan exit
  contract, a tampered-vendor test and visitor-mode runs; the vendored chwezi-slop
  detector passes its manifest and source comparison (20 files, commit `3fe84a6`).
- Evidence discipline: every sampled skill has capability, degraded-mode and
  decision-rule sections that forbid converting an unassessed check into a pass.
- Dated currentness records for search and performance
  (`docs/source-registers/search-ai-currentness-2026-09-05.json`,
  `performance-currentness-2026-09-23.json` and `-09-25.json`), enforced by
  `validate-search-doctrine.py` (18 canonical files).
- Deployment last mile: a fixed 15-step CI template, an approval-gated rollback
  adapter, lab-versus-field calibration and a client asset ownership register.

## Movement since the 6 September 2026 audit

The prior audit published no numeric score (overall `NOT ASSESSED`, cap 65). Since
then: 60 to 62 skills; 31 routing fixtures to 37 plus 21 owned negatives with a
92 % rank-1 floor and fixture lint; 38 to 131 tests; a slop-scan gate over a
vendored detector; a native-controls minimalism check; a content link-graph
checker. This report is the first numeric baseline, so movement is structural,
not numeric.

## Path to the bar

P0 (target published about 59): fixture coverage for the 20 most-used skills,
worked artefacts for the eight output types, removal of the preserved sections.
P1 (target about 63–65): a catalogue-commerce skill, an intake skill or declared
route, a hand-over pack template, a Luganda native-copy route or a withdrawn
language claim. Beyond 65 requires Tier 3 behavioural evidence and the portfolio
craft standard's acceptance evidence. See `10-roadmap-to-world-class.md`.
