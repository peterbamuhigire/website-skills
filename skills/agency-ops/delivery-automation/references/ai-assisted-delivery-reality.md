# AI-Assisted Delivery: The Honest Reality

**Purpose**: State where AI assistance actually speeds website delivery and where
the primary 2025 evidence says it does not — so the agency uses it for real gains
without believing the hype that erodes quality.

**Read this when**: deciding how much to lean on AI coding tools, or sizing how
fast a project can really go. Assumes you have read `delivery-automation/SKILL.md`.

---

## The claim to resist

The popular narrative — "AI makes building websites 10× faster, anyone can do it,
margins are infinite" — is not supported by the strongest evidence. AI assistance
is genuinely useful, but its gains are uneven and its failure modes are specific.
Promising clients AI-speed magic and then shipping "almost-right" work is how an
agency burns its reputation in a niche.

## What the primary 2025 evidence shows

- **METR randomised controlled trial (July 2025):** 16 experienced open-source
  developers, 246 real issues, AI-allowed vs not (mostly Cursor Pro + Claude
  3.5/3.7 Sonnet). Developers *expected* a 24% speedup and *believed* afterward
  they'd gained ~20% — but AI **increased completion time by 19%** on real,
  mature codebases. Perceived speed ≠ actual speed.
- **Stack Overflow 2025 Developer Survey:** 84% of developers use or plan to use
  AI tools, but trust fell — only ~29% trust the accuracy of AI output (down from
  40%), and a majority report spending **more** time fixing "almost-right" AI code.
- **Faros AI (telemetry from ~10,000 developers, 1,255 teams):** high-AI-adoption
  teams merge far more PRs and complete more tasks — but **PR review time rose
  ~91%**, change-failure rates rose ~30%, and there was **no measurable
  improvement in DORA delivery metrics** org-wide. AI moved the bottleneck to
  review, it didn't remove it.

The pattern: AI accelerates *generation*; it does not accelerate *understanding,
review, or correctness*, and on complex/maintenance work it can be a net negative.

## Where AI genuinely helps (use it here)

- **Greenfield scaffolding** — new components, boilerplate, a starter-kit page
  from a clear spec.
- **First drafts** — copy drafts, content structure, alt-text candidates,
  schema markup (always edited by a human against the engine's content standards).
- **Repetitive transforms** — bulk renaming, format conversions, test stubs.
- **Explaining unfamiliar code** before you touch it.

These map to the "repetitive, rule-based, low-judgment" automations in
`automation-opportunity-audit.md`.

## Where AI slows you down or adds risk (distrust it here)

- **Complex changes in mature client codebases** — the METR slowdown zone.
- **Anything where being "almost right" is expensive** — payment flows, auth,
  data handling, accessibility semantics.
- **Work you can't review competently** — if you can't judge the output, you
  can't ship it. AI doesn't remove the need to understand the code; it raises it.

## Keep the quality gates as the constraint

AI changes how fast code appears; it does not change what "done" means. Every
build still passes the canonical CI gates — performance, accessibility, visual-QA,
security, design-quality — before launch (`deploy`, the `quality-gates/` skills).
If AI-assisted work increases review load, staff and schedule for the review; do
not weaken the gate to hit a date. The gate is the moat that justifies premium
fees in an everyone-has-AI market.

## The honest agency line

AI lets a disciplined studio start faster and reuse more — that is real margin.
It does not let an undisciplined one ship quality work without skill. The
advantage is the *system* (productized delivery, reusable assets, enforced gates),
not the AI by itself.

## Sources

See `sources.md`. METR RCT, Stack Overflow 2025 Developer Survey, and Faros AI are
primary/named-organisation sources and are the most solid quantitative findings in
this skill. Productivity figures circulating in vendor blogs (e.g. "55% faster")
are second-hand — confirm against the original study before repeating.
