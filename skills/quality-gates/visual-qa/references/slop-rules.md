# AI-Slop Detection Rules for Rendered Output

Extends `design-system/references/ai-slop-prevention.md` with rules that only
make sense against rendered HTML and CSS.

## What `scripts/slop-scan.sh` actually checks

The script automates only part of this catalogue. It hard-codes its own
patterns (it does not read this file), takes one argument (the dist
directory; there are no flags) and writes a Markdown report to
`reports/design-quality/slop-scan.md` under the working directory (or
`$REPORTS_DIR/design-quality/` when `REPORTS_DIR` is set). It writes no JSON.

| Family | Script coverage |
|---|---|
| 1. Gradients | Partial: purple/blue hex and Tailwind `from-purple`/`from-indigo` signatures only; the 30-RGB-unit comparison is not implemented |
| 2. Easing | None |
| 3. Headlines | Yes, against the script's own pattern list (it differs from the regexes below) |
| 4. Low-information hero | None |
| 5. Icon overuse | None |
| 6. Filler adjectives | Partial: fillers inside `<h1>`/`<h2>` only, not body-copy counts |
| 7. Three-column grid | None |
| 8. Hero imagery | None |
| 9. Copy blocks on dedicated pages | None |
| 10. Colour discipline | None |
| 11. Typography discipline | None |
| 12. Spacing discipline | None |
| Script-only checks | Pure `#000` body text, "Trusted by" logo rows without links, filler copy transitions |

Exit codes: 0 pass; 1 headline, filler or transition; 2 gradient or pure
black; 4 trust row; 5 dist directory missing. Code 3 is declared in the
script header but never emitted.

**Fonts:** slop-scan performs no banned-font check. Typeface bans are
enforced by the design engine: `design-system-skills` hook
`hooks/banned-font-gate.js`, reading
`doctrine/references/ai-slop-banned-fonts.json`. A release without that gate
records the font check as `NOT_ASSESSED`.

Where a family below is marked not automated, a passing slop-scan says
nothing about it: the reviewer checks it by hand and records the result, or
records `NOT_ASSESSED`.

## 1. Banned Gradient Backgrounds

The following gradient patterns are banned on hero sections, card backgrounds,
and primary CTAs:

- Purple-to-pink generic SaaS gradient (`#6366f1` → `#ec4899` or near variants).
- Teal-to-cyan generic fintech gradient (`#0d9488` → `#06b6d4` or near variants).
- Orange-to-red generic "bold" gradient (`#f97316` → `#ef4444`).
- Any two-stop linear gradient between pastel colours without a third stop
  or a photographic overlay.

Detection: scan compiled CSS for `linear-gradient(...)` rules with two colour
stops that fall within 30 RGB units of the banned pairs.

## 2. Banned Easing Curves

- `ease-in-out` on hero animations (too slow to feel premium).
- `cubic-bezier(0, 0, 0.2, 1)` on anything longer than 500 ms (feels generic).

Intended detection: scan compiled CSS for `transition-timing-function` and
`animation-timing-function`; compare against the allowlist defined in
`design-system/tokens.css`.

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## 3. Banned Headline Patterns

The hero `<h1>` fails if it matches any of the following regex, case-insensitive:

- `/^welcome to\s/` — "Welcome to <brand>".
- `/^we are (passionate|dedicated|committed)/` — generic agency opener.
- `/your one[-\s]?stop/` — "Your one-stop <x>".
- `/^transform(ing)? your (business|life|journey)/` — generic promise.
- `/^innovative\s(solutions?|services?|platform)/` — adjective noise.
- `/^leading\s.*(provider|company|brand|studio)\s/` — unearned superlative.
- `/^revolutionize\s/` — overused verb.
- `/cutting[-\s]?edge/` — dated phrase.

Detection: extract `<h1>` text from every primary route; run the regex set.

## 4. Low-Information Hero

A hero fails when:

- `<h1>` is shorter than 3 words; or
- visible copy above the fold is shorter than 12 words total; or
- the hero contains only a single short verb-led phrase and a button.

Intended detection: render the homepage at 1280x800; capture visible text
nodes above the 800px fold; count words.

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## 5. Generic Icon Overuse

A page fails when:

- More than 8 icons visible above the fold; or
- More than 20 icons total on a non-services page; or
- A stretch of 3 or more consecutive sections share a "feature row of three
  icons" pattern.

Intended detection: count `<svg>` and icon-font elements with a visual
bounding box greater than 12x12 CSS pixels.

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## 6. Filler Adjectives in Body Copy

A page warns (not fails) when any of these adjectives appears more than 3
times total: *innovative, seamless, cutting-edge, bespoke, synergistic,
robust, world-class, state-of-the-art, game-changing, leading*.

Detection: count occurrences in visible body text.

## 7. Generic Three-Column Feature Grid

A page fails when:

- A section contains exactly three equal columns;
- each column starts with a coloured icon;
- each column has a one-line heading of 1-3 words and a subhead of 8-14 words;
- the three headings are parallel single-word or two-word phrases (e.g.
  "Fast / Secure / Reliable").

Intended detection: DOM pattern match against a section with three grid
children, each matching the above shape; cross-check with
`design-system/references/ai-slop-prevention.md`.

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

This rule allows three-column grids in general; it bans the specific generic
pattern.

## 8. Template Hero Imagery

A hero fails when the image matches any of these patterns (flagged, not
automatically blocked — manual review required):

- Stock photo of a diverse team in a glass-walled office pointing at a
  laptop.
- Stock photo of a smiling woman on a phone, generic business background.
- AI-generated image with visible artifacts (extra fingers, melted ear,
  noisy background text).

Intended detection: surface a warning when the hero image references a
known stock library hostname (shutterstock, gettyimages, adobe stock) or
carries no EXIF (a heuristic for AI generation).

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## 9. Banned Copy Blocks on Dedicated Pages

- About page that starts with "Our Story" plus a founder photo plus a
  paragraph that contains "passion" and "journey" in the same sentence.
- Services page that introduces services with "Whether you are a <x> or a
  <y>, we have the right solution for you."
- Contact page that starts with "Let's get in touch."

Intended detection: string match on the first 200 characters of `<main>`.

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## 10. Colour Discipline

The page fails when:

- More than 5 distinct hues are used in the rendered colour palette
  (measured by reducing every used colour to the nearest HSL hue bucket).
- Any hue outside the project's declared palette appears on a non-photograph
  element.

Intended detection: compare every rendered colour against
`design-system/tokens.css` as the source of truth. No script implements this
today.

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## 11. Typography Discipline

The page fails when:

- More than 2 font families are loaded.
- More than 5 distinct font sizes are used.
- Line-height on body copy is less than 1.5 or greater than 1.9.
- Any heading sits on the page with letter-spacing > 0.04em (bad default from
  generic design tooling).

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## 12. Spacing Discipline

The page fails when:

- More than 4 distinct top margins are used on direct children of `<section>`.
- A section uses non-8px spacing without a design-system reason code.

**Automation status:** documented; not automated; manual review required; script result `NOT_ASSESSED`.

## Invocation

```bash
bash "$WEBSITE_SKILLS/scripts/slop-scan.sh" dist
```

Output is a Markdown report at `reports/design-quality/slop-scan.md`
(relative to the working directory, or under `$REPORTS_DIR` when set). There
is no JSON output.

## Escalation

- Automatic block (script exit non-zero): rule 3, the automated part of
  rule 1, heading fillers from rule 6, and the script-only checks (pure black
  body text, unlinked trust rows, filler transitions).
- Reviewer block (not automated; a human finding blocks release): rules 2, 4,
  5, 7 and 10, and the unautomated part of rule 1.
- Warning with review: rules 6 (body copy), 8, 9, 11 and 12.

Warnings require a one-line reviewer acknowledgement in the PR before merge.
Automatic and reviewer blocks require a fix. A family nobody reviewed is
reported as `NOT_ASSESSED`, never as a pass.

## 13. Visual no-ship boundary

The following decorative choices block release: purple gradients, glassmorphism, neon glow,
AI-beige defaults, decorative editorial scaffolding, and decorative motion. Replace them with a
brief-specific surface, hierarchy, asset, or task interaction. Functional state transitions,
accessibility affordances, and data encodings require an explicit reason and evidence mode; an
unavailable browser/render check is `NOT_ASSESSED`.

The boundary is the AS1-AS7 overlay from Digital Research. In particular, check default convergence
(AS1), unearned labels/metrics (AS2), identical or nested modules (AS3), decorative attention
(AS4), placeholder material (AS5), copy tells (AS6), and polish-covered delivery debt (AS7).

## Reading

## Machine-error review overlay

Add the Digital Research machine-error gate to the rendered review. Record ME1-ME7 for copy and
interface structure: repeated meaning, decorative symmetry, over-explanation, inflated promise,
generic example, repeated rhetorical tic, and insight-shaped filler. Compare adjacent sections and
component instances, not just isolated screenshots. A repeated navigation label, state message, or
accessibility cue is a valid exception when its function is documented; otherwise cut or redesign the
repetition. Unavailable source or flow evidence is `NOT_ASSESSED`.

- `design-system/references/ai-slop-prevention.md` — the token-level slop
  rules this file extends.
- `content-writing/references/banned-phrases.md` — full banned phrase list
  used by rule 3 and rule 6.
- `design-quality-score/SKILL.md` — the rubric that scores rendered output
  beyond pass/fail slop detection.
