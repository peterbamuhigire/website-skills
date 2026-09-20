# Banned Phrases — Copy Draft Gate

**Read this when**: writing or reviewing draft copy (blog posts, landing
pages, emails, social) before it reaches `dist/`, or when tuning
`scripts/banned-phrase-scan.sh`.

**Purpose**: a single, code-enforced catalogue of AI-slop phrases banned
from client copy at DRAFT stage, before a build exists. It intentionally
overlaps with (does not replace) `skills/quality-gates/design-quality-score/references/banned-patterns.md`,
which `scripts/slop-scan.sh` enforces against *rendered* `dist/` HTML for
the design-quality gate. That gate only sees copy after a build. This one
lets a writer check a draft the moment it exists — a markdown file, a Google
Doc export, a CMS field dump — with no build step required.

Each entry below is either:
- a **regex pattern** (`scripts/banned-phrase-scan.sh` greps drafts for it), or
- a **judgment-only pattern**, which no regex can reliably catch without
  false positives; flag it in human review instead.

## Regex-checkable phrases

Sourced from this engine's own `banned-patterns.md` (already enforced
post-build by `slop-scan.sh`) plus ECC's `skills/article-writing/SKILL.md`
and `skills/brand-voice/SKILL.md` Banned/Hard-Bans lists, restricted to the
entries specific enough to regex without high false-positive risk:

- `In today's (rapidly evolving|fast-paced)( digital)? (landscape|world)` — generic AI opener (ECC `article-writing`; this engine's `banned-patterns.md`)
- `game[- ]changer` — unearned superlative (ECC `article-writing`)
- `cutting[- ]edge` — dated buzzword (this engine's `banned-patterns.md`)
- `revolutionary` / `revolutionis(e|ing)` — overclaim verb (this engine's `banned-patterns.md`; ECC `article-writing`)
- `state of the art` — dated buzzword (this engine's `banned-patterns.md`)
- `world[- ]class` — unverifiable superlative (this engine's `banned-patterns.md`)
- `best[- ]in[- ]class` — unverifiable superlative (this engine's `banned-patterns.md`)
- `innovative solutions?` — double-generic (this engine's `banned-patterns.md`)
- `seamless(ly)?` — vague filler (this engine's `banned-patterns.md`)
- `holistic` — vague filler (this engine's `banned-patterns.md`)
- `synerg(y|istic)` — vague filler (this engine's `banned-patterns.md`)
- `next[- ]gen(eration)?` — dated buzzword (this engine's `banned-patterns.md`)
- `Welcome to (our|the)` — generic welcome framing (this engine's `banned-patterns.md`)
- `We('re| are) passionate about` — passion claim without proof (this engine's `banned-patterns.md`)
- `Your one[- ]stop (shop|solution|destination)` — category bloat (this engine's `banned-patterns.md`)
- `Empowering (businesses|people|teams)` — abstract empowerment (this engine's `banned-patterns.md`)
- `Crafted with care` — sentimental filler (this engine's `banned-patterns.md`)
- `Take your (business|brand|project) to the next level` — template framing (this engine's `banned-patterns.md`)
- `In the digital age` — generic opener (this engine's `slop-scan.sh` copy-transitions list)
- `At the end of the day` — filler transition (this engine's `slop-scan.sh` copy-transitions list)
- `Let's (unpack|dive into)` / `Dive into` / `Unpacking the` — filler verb-as-bridge (this engine's `slop-scan.sh` copy-transitions list)
- `we understand your unique needs` — empty empathy (`genuine-writing-and-ai-slop-gate.md`)
- `whether you're a small business or (a )?large enterprise` — fake balance (`genuine-writing-and-ai-slop-gate.md`)
- `no fluff` — hollow self-description (ECC `brand-voice` Hard Bans)
- `Excited to share` — LinkedIn thought-leader cadence (ECC `brand-voice` Hard Bans)
- `here's why this matters` — standalone bridge, no argument (ECC `article-writing`)

## Judgment-only patterns (do not regex; flag in human review)

- Fake curiosity hooks ("You won't believe...", "The secret to...")
- "Not X, just Y" construction used as a rhetorical crutch rather than a real distinction
- Fake vulnerability arcs (manufactured personal struggle with no evidence it happened)
- Generic founder-journey filler that doesn't move the argument
- Corny parentheticals used as forced personality rather than qualification
- A closing question added only to juice engagement, with no real invitation to respond
- Stacked adjectives even when no single one is individually banned (e.g. three
  vague positive adjectives in one sentence with no concrete noun between them)
- Paragraphs that only restate the heading above them (ME1/ME3 in the
  machine-error editorial gate, see `genuine-writing-and-ai-slop-gate.md`)

## Maintenance

Add a new entry here — cited to a real source, same as every rule in this
engine's `rules/` layer — before adding it to `scripts/banned-phrase-scan.sh`.
Do not add a phrase to the script without adding it here first; the script
parses this file, it does not carry its own separate list.
