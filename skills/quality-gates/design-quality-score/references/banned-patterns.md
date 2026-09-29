# Banned Patterns

**Read this when**: tuning `scripts/slop-scan.sh` or scoring a template
against the rubric's copy and originality categories.

**Purpose**: The catalogue of banned headline patterns, banned colour
combinations, and banned pattern language. `scripts/slop-scan.sh` reads the
copy lists in this file through the data pack
`quality/slop-rules.website.json` (one detector rule per pattern, each citing
the heading below it came from). A pattern added here is enforced once the same
pattern is added to the pack with a flag fixture line in `tests/slop-pack/`;
`node scripts/validate-slop-pack.mjs` proves each one. Colour, motion, font and
layout bans are enforced by the design engine's detector rules, named per
section below.

## Banned headline and hero patterns

- `Welcome to (our|the)` — generic welcome framing.
- `We (are|'re) passionate about` — passion claim without proof.
- `Your one-stop (shop|solution|destination)` — category bloat.
- `Bringing the future of` — vague futurism.
- `Empowering (businesses|people|teams)` — abstract empowerment.
- `Revolutionising` — overclaim verb.
- `The leading` — unverifiable superlative.
- `Cutting-edge` — dated buzzword.
- `State of the art` — dated buzzword.
- `Innovative solutions` — double-generic.
- `Crafted with care` — sentimental filler.
- `Take your (business|brand|project) to the next level` — template
  framing.
- `We (are|'re) (dedicated|committed)` — generic agency opener.
- `Transform(ing) your (business|life|journey)` — generic promise.
- `Innovative (services|platform)` — adjective noise (same family as
  "Innovative solutions").

The last three were listed only in `visual-qa/references/slop-rules.md` §3;
they were consolidated here on 2026-09-29 (M10-11) so that one list feeds the
scan.

Rule: any of the above in a heading (`h1`-`h6`) fails the scan (pack rules
`web-headline-*`, severity block).
Contextual use in body copy that discusses the phrase (e.g. "we avoid
calling ourselves 'cutting-edge' because…") is allowed.

## Banned filler words (in heroes and sub-heroes)

These words appearing in a hero or sub-hero headline suggest vague
positioning. One of them in an `h1` or `h2` fails the scan (pack rule
`web-heading-filler`, severity block; the former slop-scan behaved the same).
`robust` and `scalable` depend on context, so pack rule
`web-heading-filler-context` reports them as advisory and a reviewer decides:

- `seamless`, `seamlessly`
- `holistic`
- `synergy`, `synergistic`
- `robust` (as an adjective)
- `scalable` (as a selling point, not a fact)
- `next-generation`, `next-gen`
- `best-in-class`
- `world-class` (as an adjective)

## Banned colour combinations

Derived from `design-system/references/ai-slop-prevention.md`:

- Pure `#000000` text on pure `#FFFFFF` background for body copy.
- Any rainbow-gradient hero without a content reason.
- Purple-to-blue gradient background as default "SaaS" visual.
- Off-palette accent hex used once and nowhere else.

Enforcement: detector rules `pure-black-body-text` (warning; blocks the scan)
and `purple-blue-gradient` (block). Off-palette colours are reported by
`design-system-color` (advisory, needs `design-tokens.json`); the rainbow
gradient and the "used once" test are reviewer checks.

## Banned easing curves

Motion must follow the 100/300/500 ms rule and use the engine's
approved easing curves. Banned defaults:

- `cubic-bezier(0.4, 0, 0.2, 1)` as the universal curve for every
  transition — fine for one utility, drift when applied everywhere.
- `ease-in-out` on entrance animations that should ease-out only.
- Bounce or elastic easing on primary content reveals.

Enforcement: bounce and elastic curves fail the scan through the detector rule
`bounce-easing` (block). The first two items are reported as advisory by pack
rules `web-universal-standard-curve` and `web-ease-in-out-entrance`, because
only a reviewer can tell a universal curve or an entrance animation from a
legitimate single use.

## Banned generic layouts

- Three-column feature grid with identical icons, identical heading
  length, and identical two-line body copy.
- Generic testimonial carousel with three slides and no attribution.
- "Team" section with six circular headshots and titles but no specific
  roles (e.g. "Founder" without context).

The rubric allows these layouts when the content, typography, or
photography makes them distinctive; the ban applies to the default
instantiation.

Enforcement: the identical three-column grid fails the scan through the
detector rule `identical-three-column-feature-grid` (warning; slop-scan runs
with `--fail-on warning`). The carousel and team patterns are reviewer checks.

## Banned icon patterns

- Heroicons default set used across the entire site without a chosen
  style (outline vs solid) and without consistent colour treatment.
- Emoji substituted for icons.
- Decorative icons that duplicate the heading label.

Enforcement: reviewer checks (`human_review`); no detector rule exists.

## Banned trust patterns

- "Trusted by" row with three greyscale logos and no link or proof.
- Star ratings from unnamed sources.
- "Featured in" with logos of publications that never wrote about the
  client.
- Stock photography for team, customers, or testimonials.

Enforcement: an unlinked logo row fails the scan through pack rule
`web-trust-row-unlinked` (block): "Trusted by" or "Featured in" followed by
three logos with no link before the section ends. The other three items are
reviewer checks.

## Banned copy shortcuts

- Sentences starting with "In today's fast-paced world".
- Sentences starting with "In the digital age".
- "At the end of the day" as a transition.
- "Unpack" as a verb for explaining anything.
- "Dive into" as a verb for starting any section.

Enforcement: pack rule `web-copy-shortcut` (block) over the whole rendered
page, with the former slop-scan variants "Let's unpack", "Let's dive into" and
"Unpacking the".

## How the slop-scan uses this

`scripts/slop-scan.sh` wraps the design engine's `chwezi-slop` detector
(vendored and hash-checked in `scripts/vendor/chwezi-slop/`). It runs every
static detector rule plus the pack `quality/slop-rules.website.json` over the
built `dist/`, with `--fail-on warning`, and writes
`reports/design-quality/slop.json` (canonical) and `slop-scan.md`. Block and
warning findings fail the scan (exit 1); advisory findings are reported only;
a missing prerequisite is `NOT_ASSESSED` (exit 5), never a pass. Rule IDs,
severities and evidence modes per family are in
`visual-qa/references/slop-rules.md`. Items marked as reviewer checks above
are not proved by a passing scan.

## Updating the list

- A new banned pattern is added through a decision entry that cites the
  occurrence (internal or external) that motivated the addition, and to
  `quality/slop-rules.website.json` with a flag and a pass fixture line.
- A banned pattern cannot be removed once added without an explicit
  decision entry overturning it.
- The list is reviewed at the quarterly documentation audit.
