# Sales Copywriting Skill — Design Document

> **Approved:** 2026-03-05
> **Approach:** Option B (multiple focused skills/references), Option 3 (hybrid cross-cutting + on-demand), Level 2 persuasion

## Goal

Create a `sales-copywriting` skill with 5 reference files, enhance 3 existing reference files, and add integration points in 3 existing skills. Extracted from 3 copywriting books: Ray Edwards (PASTOR, 21 bullets, guarantees), Paul Hollingshead/AWAI (4 P's, Theory of Resistance, research methods), Angie Lee (sales page structure, value anchoring, pricing psychology).

## Architecture

- **Hybrid skill:** Core principles are cross-cutting (active during all page-builder and blog-writer work). Sales-specific frameworks activate only for landing/sales/product pages.
- **Level 2 persuasion:** Confident persuasion (PASTOR, fascination bullets, named guarantees, value anchoring). No hard-sell tactics (popovers, countdown timers, strikethrough pricing) unless explicitly requested.
- **Reference files hold the detail:** SKILL.md stays under 500 lines; dense templates and examples live in references.

## Deliverables

### New Files (6)
1. `sales-copywriting/SKILL.md` — master skill (hybrid cross-cutting + on-demand)
2. `sales-copywriting/references/pastor-and-4ps.md` — PASTOR + 4 P's + 15 building blocks
3. `sales-copywriting/references/fascination-bullets.md` — 21 bullet templates + mixing rules
4. `sales-copywriting/references/resistance-and-objections.md` — Theory of Resistance + 4 buyer fears + preemptive countering
5. `sales-copywriting/references/closing-and-guarantees.md` — 5 closing templates + 10-part guarantee + 9 offer types
6. `sales-copywriting/references/headline-mastery.md` — consolidated headline formulas from all 3 books

### Enhanced Files (3)
7. `page-builder/references/website-copywriting.md` — add cross-references, value anchoring, proof integration
8. `blog-writer/references/storytelling.md` — add DSI, Forde's story construction, Godin's 9 qualities, 6 story sources
9. `blog-writer/references/writing-craft.md` — add Schwartz's research method, Golden Nuggets, Stevens' authenticity rules

### Integration Edits (3)
10. `page-builder/SKILL.md` — add reference to sales-copywriting for headlines, bullets, sales pages
11. `blog-writer/SKILL.md` — add reference to sales-copywriting for headlines and persuasive articles
12. `brand-alignment/SKILL.md` — add note that sales-copywriting must align with brand voice

### Documentation Updates (2)
13. `CLAUDE.md` — add sales-copywriting to utility skills list
14. `README.md` — add sales-copywriting to skill descriptions

## Source Attribution
- Ray Edwards: "How to Write Copy That Sells" (PASTOR, 21 bullets, 5 closes, 10-part guarantee, O.P.E.N. scale, DSI, PAC email formula)
- Paul Hollingshead/AWAI: "Accelerated Program for Six-Figure Copywriting Part 2" (4 P's, Theory of Resistance, Golden Nuggets, Gene Schwartz research, John Forde story construction, Seth Godin story qualities, Jen Stevens authenticity)
- Angie Lee: "Sales Copy that Sells like Crazy" (33-step sales page structure, value anchoring, pricing psychology ending in 7, no-period bullet rule, PAS pattern)
