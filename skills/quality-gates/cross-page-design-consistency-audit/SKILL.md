---
name: cross-page-design-consistency-audit
description: Detects and fixes the most common premium-site failure — one polished page (usually the homepage) wired to a real component system while every interior page is hand-built from ad-hoc utilities, emoji, off-brand grays, generic gradients, and glassmorphism. Owns the "two design systems on one site" check, the per-language markup-duplication / translation-drift check, and the find-and-replace content-artifact scan. Co-activates with design-quality-score and the design-system-skills anti-slop doctrine.
---

# Cross-Page Design Consistency Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- Auditing or upgrading an existing multi-page site (the homepage looks good — check whether the rest does).
- Before launch on any site with more than ~3 templates, especially multilingual sites.
- After a content find-and-replace pass (these reliably leave duplicate-word artifacts).
- Whenever interior pages "feel cheaper" than the homepage.

## Do not use when
- Scoring a single template's intrinsic quality — that is `design-quality-score`.
- The site is one page.

## Why this exists (the BIRDC finding, 2026-06)

A real institutional site scored **67/100** not because any one page was bad, but because it
ran **two design languages at once**:

- The **homepage** used a proper component layer (`global.css` classes: section labels, section
  titles, feature cards, authored CTA, custom shadow tokens, a distinctive serif display) — an
  authored, anti-slop page.
- **Every interior page** (about, products, innovation, impact, contact, gallery × 3 languages)
  was hand-built from raw utilities and carried textbook AI-slop tells the homepage did not.

The homepage alone scored ~88; the interior pages ~52. **The gap — not any single page — is
what drags a site down.** Discerning clients read the *inconsistency* as "no system."

## The root cause is almost always architecture

The homepage was a shared component driven by a per-language content file
(`HomePage.astro` + `homeContent.ts`). The interior pages **duplicated full markup in every
`en/`, `fr/`, `sw/` file.** That single decision caused three separate defects:

1. **Design drift** — each duplicated page was hand-tweaked, so the system never propagated.
2. **Find-and-replace artifacts** — a global "matooke → banana flour" replace sprayed
   `"banana flour, banana flour"` and `"Tooke Tooke"` across many files at once, including into
   JSON-LD `keywords` (keyword stuffing).
3. **Translation drift** — when EN was later de-slopped, FR/SW were *not* updated, so the
   non-English pages silently kept older hype copy ("20+ Ans d'Innovation", "première
   entreprise africaine").

**Fix the architecture and the other problems stop recurring.**

## Required architecture (per page)

```
src/content/<page>Content.ts     ← typed content, Record<Language, …>, ALL languages
src/components/<Page>Page.astro   ← ONE markup source using the shared class layer
src/pages/<lang>/<page>.astro     ← thin: import BaseLayout + <Page>Page + SEO from content
```

Structural things that are the same in every language (SVG icon paths, image imports, grid
shape) live in the **component**, never in content. Translatable strings live in **content**.
This makes "two design systems" structurally impossible and makes a find-replace touch one
content file, not nine page files.

## The shared class layer (promote the good page's system)

Don't invent per-page styles. Lift the homepage's voice into reusable classes in `global.css`
and route every page through them. The BIRDC set (adapt names per project):

- Heroes: one editorial `PageHero.astro` (left-weighted, photographic) — not a centered
  eyebrow→title→subtitle stack repeated per page.
- Labels/titles/copy: `.section-label` / `.section-label-light`, `.section-title`, `.body-copy`,
  `.body-copy-sm`, `.eyebrow`.
- Cards: `.feature-card`, `.product-card`, `.info-card`. Highlight boxes: `.highlight-panel`.
- Iconography: `.icon-badge` / `.icon-badge-gold` holding **inline SVG** (heroicons-outline).
- CTAs: one authored `cta-shell` + `.cta-panel` with `.button-primary` / `.button-secondary`.
- Links: `.link-arrow` / `.link-arrow-light`. Lists: `.check-item` with a tick SVG.

## The slop tells to grep for (interior-page edition)

Run these from the site root. Each hit is a finding to fix, not necessarily a failure — judge in
context, but on a premium site the target is **zero**.

| Tell | Detector | Fix |
|---|---|---|
| Off-brand neutrals | `rg "text-gray-[0-9]"` | Use the warm brand neutral ramp (`text-neutral-*`) or `.body-copy*`. |
| Emoji as iconography | `rg "[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]" src` | Inline SVG in an `.icon-badge`. Emoji reads as unconsidered for institutional UI. |
| Generic gradient CTA band | `rg "bg-gradient-to-r from-primary-800 via-primary-900"` | Replace with the authored `cta-shell` + `.cta-panel`. |
| Glassmorphism | `rg "backdrop-blur-(xl\|2xl\|3xl)"` | Prefer a solid, opaque authored panel; it reads stronger and stays legible over photos. Glassmorphism is a listed convergence tell. |
| Banned easing | `rg "cubic-bezier\(0\.[0-9]+, 1\.[0-9]"` (overshoot/back/elastic) | Use exponential ease-out (`--transition-smooth`). No bounce on institutional UI. |
| Over-wide eyebrow tracking | `rg "tracking-\[0\.2"` | Short uppercase labels ≈ 0.15–0.18em, not 0.22–0.24em. |
| Centered generic hero | `rg "text-center" src/pages` in a hero block | Use the shared editorial `PageHero`. |

## Content-artifact + translation-drift checks

```
# Duplicate-word artifacts from a botched find-replace (tune the words to the project):
rg -n "(\b[\w-]+\b) \1" src            # naive "word word" repeats
rg -n "Tooke Tooke|banana flour, banana flour"   # project-specific example

# Translation drift: EN is canonical. After de-slopping EN, diff intent against FR/SW.
# If pages are duplicated per language (the anti-pattern), FR/SW will lag — extract to
# content.ts and retranslate from the CURRENT EN, matching its restrained tone.
```

Also scan JSON-LD `keywords`/`description` for the same duplications — find-replace hits
structured data too, and duplicated keywords read as stuffing.

## Workflow

1. **Inventory templates.** List every page × language. Flag any `pages/<lang>/<x>.astro` that
   contains substantial markup instead of importing a shared component — that is the
   duplication anti-pattern.
2. **Score the gap.** Score the best page and a typical interior page separately
   (`design-quality-score`). A gap > 1.5 points is the headline finding.
3. **Promote the system.** Lift the best page's voice into `global.css` component classes +
   shared hero/CTA components.
4. **Refactor each page** into content + component + thin per-language files. EN is the
   canonical tone; retranslate FR/SW from current EN.
5. **Run the grep tables.** Drive every tell to zero.
6. **Rebuild and visual-QA** (`visual-qa`), then re-score every primary template ≥ 8/10.

## Authority

Presentation-layer rules (banned fonts, glassmorphism-as-slop, easing, colour, type scale)
trace to the cross-cutting design engine: `C:\wamp64\www\design-system-skills` — start at its
`README.md` and `doctrine/design-doctrine.md`. This skill is the *site-wide consistency* lens on
top of that doctrine; `design-quality-score` is the *per-template* lens. Run all three together.
