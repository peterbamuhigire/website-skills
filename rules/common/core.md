# Core Rules — Website Engine

> Distilled from this engine's own `CLAUDE.md`.

## Every blog post or article is researched via the digital-research-engine first — never from assumed knowledge

Real examples, statistics, market figures, and any cited research come from a
live research wave with verified sources. Resolve `digital-research-engine`
from the device's global engine-routing table (canonical checkout:
`C:\wamp64\www\digital-research-engine`) — do not substitute a retired alias.

## Attribution is mandatory; never fabricate a citation

Cite real, locatable sources with URLs. Name the researchers, institutions, and
regulators whose work is drawn on. Mark anything unverifiable as **UNVERIFIED**
and either confirm it or frame it without inventing an author, title, or
statistic. Close each piece with a "Sources & the researchers worth crediting"
block.

## Treat search visibility as competitive evidence, never as a ranking promise

Do not invent search volumes. Record query date, provider, exact queries, result
URLs, and read status for every SERP-informed claim.

## Every enforcement gate in `quality-gates/` is a script, not a suggestion

Where this engine already has a runnable check (`a11y-gate.sh`,
`design-quality-score.sh`, `check-security-headers.sh`, `drift-check.sh`), run it
— do not restate its judgement from memory. If it has not been wired as an
automatic hook yet, running it manually before delivery is still mandatory.
