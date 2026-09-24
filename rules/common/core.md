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

## Book extractions and book summaries are never stored in this repository

Books are concept inputs only. Turn a book's method into a task-oriented skill
reference in original words with a brief citation (author, year, title,
publisher); keep verbatim quotes under 25 words and rare; route every volatile
claim through the Digital Research currentness gate. Never create a
`book-extractions/` (or similar) folder or a book-summary file.

## Lab performance results are not user experience

Lab gates block deploy; field Core Web Vitals at the 75th percentile decide
success. Label every performance number as lab or field with its profile or
percentile, period and tool version. Never promise a Lighthouse score.
