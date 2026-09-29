# AI-Slop Detection Rules for Rendered Output

Extends `design-system/references/ai-slop-prevention.md` with rules that only
make sense against rendered HTML and CSS.

## What `scripts/slop-scan.sh` enforces

`scripts/slop-scan.sh` is a wrapper over the design engine's `chwezi-slop`
detector (M10-09), vendored and hash-checked in `scripts/vendor/chwezi-slop/`
(`VENDOR.json`, checked by `python -X utf8 scripts/check-vendored-detector.py`).
It runs:

```bash
node scripts/vendor/chwezi-slop/cli.mjs --json --tier deep --fail-on warning \
  --extra-rules quality/slop-rules.website.json <dist>
```

The detector's registry supplies the font, colour, motion, layout and
accessibility rules. The website pack `quality/slop-rules.website.json`
supplies the copy patterns from
`design-quality-score/references/banned-patterns.md`. The scan takes one
argument (the dist directory) and no flags. It writes
`reports/design-quality/slop.json` (canonical, the detector report shape) and
renders `reports/design-quality/slop-scan.md` from it, under the working
directory or `$REPORTS_DIR/design-quality/`.

Exit codes: **0** no blocking findings; **1** blocking findings (any `block`
or `warning` severity finding, because the scan runs with
`--fail-on warning`); **5** `NOT_ASSESSED`: no dist directory, no Node 18 or
later, a missing or tampered vendored detector, an invalid pack or a detector
operational failure. Exit 5 is never treated as clean. The former per-family
codes 2-4 are retired (`project-log/decisions/2026-09-29-slop-scan-exit-contract.md`).
`CHWEZI_SLOP_DETECTOR` may point at a local chwezi-design-engine checkout
instead of the vendored copy; the report records which detector ran.

Evidence modes: `cli` is a static finding from the built source (measured
presence of the pattern); `browser` is a rendered-page finding from the
detector's optional browser tier, which slop-scan does not run; `human_review`
means no detector rule exists and a reviewer decides.

| Family | Enforcement | Detector rule IDs (severity) | Evidence mode | Fail fixture proves |
|---|---|---|---|---|
| 1. Gradients | automatic block | `purple-blue-gradient` (block), `gradient-text` (block); other named pairs `human_review` | cli | `purple-blue-gradient` |
| 2. Easing | automatic block | `bounce-easing` (block), `missing-reduced-motion` (warning); `web-universal-standard-curve`, `web-ease-in-out-entrance` (advisory) | cli | `bounce-easing` |
| 3. Headlines | automatic block | `web-headline-*`, 14 pack rules (block) | cli | `web-headline-welcome-to` |
| 4. Low-information hero | review gate | none | human_review | none |
| 5. Icon overuse | review gate | none | human_review | none |
| 6. Filler adjectives | automatic block (h1 and h2) | `web-heading-filler` (block), `web-heading-filler-context` (advisory); body-copy counts `human_review` | cli | `web-heading-filler` |
| 7. Three-column grid | automatic block | `identical-three-column-feature-grid` (warning) | cli | `identical-three-column-feature-grid` |
| 8. Hero imagery | review gate | `placeholder-image-host` (warning) for placeholder hosts only | cli, human_review | none |
| 9. Copy blocks on dedicated pages | review gate | none | human_review | none |
| 10. Colour discipline | review gate | `design-system-color` (advisory; needs `design-tokens.json`) | cli (advisory), human_review | none |
| 11. Typography discipline | automatic block (banned fonts) | `banned-primary-font` (block), `conditional-source-sans-primary` (block), `design-system-font` (block; needs tokens), `body-leading-tight`, `body-leading-loose`, `heading-wide-tracking`, `flat-type-hierarchy` (warning); family and size counts `human_review` | cli | `banned-primary-font` |
| 12. Spacing discipline | review gate | none | human_review | none |
| 13. Visual no-ship boundary | automatic block | `glassmorphism`, `neon-glow` (block), `ai-beige-ground` (warning); other surfaces `human_review` | cli | `glassmorphism` |
| Pure `#000` body text | automatic block | `pure-black-body-text` (warning) | cli | `pure-black-body-text` |
| Unlinked trust row | automatic block | `web-trust-row-unlinked` (block) | cli | `web-trust-row-unlinked` |
| Copy shortcuts and transitions | automatic block | `web-copy-shortcut` (block) | cli | `web-copy-shortcut` |

Every row marked "automatic block" is proved by `tests/gates/fail/slop-dist/`
(the named rule fires and `slop-scan.sh` exits 1) and by
`tests/gates/pass/slop-dist/` (it does not fire and the scan exits 0); the
pytest `tests/test_slop_scan.py` reads this table. A row marked "review gate"
is not proved by a passing scan: the reviewer checks it and records the
result, or records `NOT_ASSESSED`.

**Truthfulness correction (2026-09-29, M10-11).** Earlier versions marked
rules 4, 5 and 10 as automatic blocks. No detector rule can check 4 and 5
statically, and the detector reports 10 as advisory only, so they are
relabelled "review gate (`human_review`)". The doctrine ban is unchanged; only
the enforcement claim changed. Flagged for Peter's review.

**Fonts.** Banned primary fonts now fail client CI through
`banned-primary-font` and `conditional-source-sans-primary`, which read the
vendored `doctrine/references/ai-slop-banned-fonts.json`. Write-time
enforcement (the `banned-font-gate.js` hook) still needs the design plugin.

### Migration note for existing client sites

The first run after upgrading may fail on rules the old scan did not have:
banned fonts, bounce easing, glassmorphism, neon glow, gradient text, AI-beige
ground, nested cards, kicker and eyebrow labels, missing reduced-motion,
tight or loose body leading, tiny text, skipped headings, removed focus
indicators, placeholder image hosts and broken local images. Fix the finding,
or record a waiver (below). The canonical policy is unchanged: the design
quality job is advisory on pull requests and blocking on `main`.

### Waivers

A waiver needs a reason in the form `<who>: <evidence>` (for example
`Peter Bamuhigire: status stripe paired with a text label, brand book 2026`).
Inline waivers use the detector's comment syntax
(`chwezi-slop-disable-next-line <rule> -- <who>: <evidence>`); project waivers
live in `.chwezi/slop.json`. Agents may grant `value` waivers only; any wider
scope needs `"granted_by": "human"`. An invalid waiver makes the scan exit 5.
The format is defined in the design engine's `tools/slop-detector/README.md`
(Waivers, M10-09). List every waiver in the release evidence.

## 1. Banned Gradient Backgrounds

The following gradient patterns are banned on hero sections, card backgrounds,
and primary CTAs:

- Purple-to-pink generic SaaS gradient (`#6366f1` → `#ec4899` or near variants).
- Teal-to-cyan generic fintech gradient (`#0d9488` → `#06b6d4` or near variants).
- Orange-to-red generic "bold" gradient (`#f97316` → `#ef4444`).
- Any two-stop linear gradient between pastel colours without a third stop
  or a photographic overlay.

Detection: `purple-blue-gradient` (block) catches purple or violet paired with
blue, cyan or pink, and `gradient-text` (block) catches gradient-filled text.
The teal-to-cyan, orange-to-red and pastel two-stop pairs are reviewer checks
(`human_review`).

## 2. Banned Easing Curves

- `ease-in-out` on hero animations (too slow to feel premium).
- `cubic-bezier(0, 0, 0.2, 1)` on anything longer than 500 ms (feels generic).

- Bounce or elastic (overshooting) curves anywhere.

Detection: `bounce-easing` (block) fails overshooting curves;
`missing-reduced-motion` (warning) fails motion with no reduced-motion path.
The two curves above are reported as advisory by `web-ease-in-out-entrance`
and `web-universal-standard-curve`; whether they sit on a hero or run longer
than 500 ms is a reviewer check (`human_review`).

## 3. Banned Headline Patterns

A heading (`h1`-`h6`) fails when it matches a pattern in
`design-quality-score/references/banned-patterns.md` ("Banned headline and hero
patterns"), for example "Welcome to our", "We are passionate about", "Your
one-stop shop", "Transform your business", "Innovative solutions", "The
leading", "Revolutionising" and "Cutting-edge". That file is the single list;
the patterns formerly listed here were consolidated into it on 2026-09-29.

Detection: pack rules `web-headline-*` (block), one per pattern, each with a
flag fixture line in `tests/slop-pack/headlines.flag.html`.

## 4. Low-Information Hero

A hero fails when:

- `<h1>` is shorter than 3 words; or
- visible copy above the fold is shorter than 12 words total; or
- the hero contains only a single short verb-led phrase and a button.

Detection: none. A static scan cannot see the fold, and the detector has no
rule for it. **Review gate (`human_review`)**: the reviewer checks the rendered
homepage at 1280x800 and records the word count, or `NOT_ASSESSED`.

## 5. Generic Icon Overuse

A page fails when:

- More than 8 icons visible above the fold; or
- More than 20 icons total on a non-services page; or
- A stretch of 3 or more consecutive sections share a "feature row of three
  icons" pattern.

Detection: none. The detector has no icon-count rule. **Review gate
(`human_review`)**: the reviewer counts icons above the fold and on the page.

## 6. Filler Adjectives in Body Copy

A page warns (not fails) when any of these adjectives appears more than 3
times total: *innovative, seamless, cutting-edge, bespoke, synergistic,
robust, world-class, state-of-the-art, game-changing, leading*.

Detection: filler words in an `h1` or `h2` fail the scan (`web-heading-filler`,
block; `robust` and `scalable` are advisory through
`web-heading-filler-context`). The body-copy count is a reviewer check
(`human_review`).

## 7. Generic Three-Column Feature Grid

A page fails when:

- A section contains exactly three equal columns;
- each column starts with a coloured icon;
- each column has a one-line heading of 1-3 words and a subhead of 8-14 words;
- the three headings are parallel single-word or two-word phrases (e.g.
  "Fast / Secure / Reliable").

Detection: `identical-three-column-feature-grid` (warning; fails the scan
because slop-scan runs with `--fail-on warning`) matches three identical icon,
heading and text columns in the built HTML.

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

Detection: `placeholder-image-host` (warning) fails placeholder image hosts.
Stock and AI-generated imagery is a reviewer check (`human_review`).

## 9. Banned Copy Blocks on Dedicated Pages

- About page that starts with "Our Story" plus a founder photo plus a
  paragraph that contains "passion" and "journey" in the same sentence.
- Services page that introduces services with "Whether you are a <x> or a
  <y>, we have the right solution for you."
- Contact page that starts with "Let's get in touch."

Detection: none. **Review gate (`human_review`).**

## 10. Colour Discipline

The page fails when:

- More than 5 distinct hues are used in the rendered colour palette
  (measured by reducing every used colour to the nearest HSL hue bucket).
- Any hue outside the project's declared palette appears on a non-photograph
  element.

Detection: `design-system-color` compares every colour in the built CSS with
the project's `design-tokens.json` (CIEDE2000 difference above 2.0) and reports
it as **advisory**, so it never fails the scan; with no token file it is
`NOT_ASSESSED`. The hue count is not automated. **Review gate
(`human_review`)**: the reviewer reads the advisory findings and decides.

## 11. Typography Discipline

The page fails when:

- More than 2 font families are loaded.
- More than 5 distinct font sizes are used.
- Line-height on body copy is less than 1.5 or greater than 1.9.
- Any heading sits on the page with letter-spacing > 0.04em (bad default from
  generic design tooling).

Detection: banned fonts fail the scan (`banned-primary-font`,
`conditional-source-sans-primary`, and `design-system-font` for faces outside
the token file). Body line-height outside 1.5-1.9 (`body-leading-tight`,
`body-leading-loose`) and wide heading tracking (`heading-wide-tracking`) are
warnings and fail the scan. The family count and the size count are reviewer
checks (`human_review`; `design-system-font-size` reports off-token sizes as
advisory).

## 12. Spacing Discipline

The page fails when:

- More than 4 distinct top margins are used on direct children of `<section>`.
- A section uses non-8px spacing without a design-system reason code.

Detection: none. **Review gate (`human_review`).**

## Invocation

```bash
bash "$WEBSITE_SKILLS/scripts/slop-scan.sh" dist
```

Output: `reports/design-quality/slop.json` (canonical) and
`reports/design-quality/slop-scan.md` (relative to the working directory, or
under `$REPORTS_DIR` when set).

## Escalation

- Automatic block (slop-scan exit 1): every row marked "automatic block" in
  the table above, and every other `block` or `warning` finding the detector
  reports.
- Reviewer block (a human finding blocks release): rules 4, 5 and 10, and the
  `human_review` parts of rules 1 and 2.
- Warning with review: advisory findings, rules 6 (body copy), 8 (stock and
  AI imagery), 9, 11 (counts) and 12.

Advisory findings and warnings with review require a one-line reviewer
acknowledgement in the PR before merge. Automatic and reviewer blocks require
a fix or a waiver in the format above. A family nobody reviewed is reported as
`NOT_ASSESSED`, never as a pass.

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
