# Design System Governance and DesignOps

Parent skill: [design-system](../SKILL.md). Read when starting or extending a client's design system, when components or styles are drifting across pages, when setting up who owns and maintains the system, or when design decisions are stalling in committee.

Related files: `../../page-builder/references/component-design-rules.md` (token layers, component documentation contract, reuse-before-create), the cross-page consistency gate in `skills/quality-gates/cross-page-design-consistency-audit/`, and the design engine's `C:/wamp64/www/design-system-skills/skills/04-web-and-ui-design/practical-ui-design/references/visual-consistency.md`.

---

## 1. Audit before building

1. Capture every live instance of each UI element (buttons, inputs, cards, headings, colours, spacing values, icons) into an inventory, grouped by type.
2. Count the variants. The first problem is usually uncontrolled variation, not a lack of ideas.
3. For each group, choose the canonical version, list variants to retire, and record why.
4. Research what users already expect in the category before drawing anything new; designers who start sketching first bias themselves.
5. Only then design missing pieces.

## 2. Standards and components travel together

- **Standards** explain why: principles, usage rules, content rules, accessibility requirements.
- **Components** embody what: the coded, reusable parts.
- Ship both. Components without standards get misused; standards without components are ignored.

## 3. One source of truth

- Name the single maintained reference for tokens, components, states and usage rules (normally the coded library plus its documentation page).
- Check parity between design files, documentation and code at every release. If they disagree, the system is already drifting; fix the source, then propagate.
- Keep tokens in three layers (primitive, semantic, component). Raw values in page code are a governance failure, not a style choice.

## 4. Consistency without sameness

Hold the logic stable across layout, typography, colour and emphasis, component shape and state, language and labels, spacing, icon treatment and interaction feedback. Allow brand character within that logic. Controls must look operable without hover (clear affordances and signifiers). A pattern library lowers users' effort only when applied consistently; unmanaged pattern growth becomes user-experience debt.

## 5. Run the system as a product

| Area | Minimum practice |
|---|---|
| Ownership | Named owner for the system; named owner per component family |
| Contribution | Written route for proposing a new component or variant: need, evidence of reuse failure, draft, review, merge |
| Maintenance | Scheduled clean-up: retire unused variants, merge near-duplicates, update docs |
| Versioning | Change log and version for the library; flag breaking changes to page builders |
| Quality | Every component documents purpose, anatomy, variants, states, content rules, accessibility and responsive behaviour |

"Build once and walk away" does not work; budget ongoing time in retainers (see `agency-ops/agency-client-retention`).

## 6. DesignOps: make good design repeatable

Assess and plan four areas when a client or agency team scales design work:

1. **Workflow:** how work is briefed, reviewed, handed to development and accepted; tooling and file conventions; definition of done.
2. **People:** roles, skills, hiring and onboarding; who critiques and who decides.
3. **Governance:** decision rights, review cadence, standards enforcement, the contribution route above.
4. **Business support:** how design work links to business goals, budget and measurement, so it keeps sponsorship.

Better taste alone does not scale; operational support does.

## 7. Deciding without a committee

- Committees dilute decisions. Run structured critique against the brief and top tasks instead: presenter states the goal, reviewers comment on whether the design meets it, one named decision-maker decides.
- For open problems, use a short design-studio round: everyone sketches independently, presents, critiques, then converges on one direction.
- Record each decision and its reason in the system's change log.

---

## Sources

- *Design Systems Handbook* and *DesignOps Handbook*, as synthesised in the 2026 design-systems review; authors, years and publishers not recorded in the source.
- UXPin, *Web UI Design for the Human Eye: Principles of Visual Consistency*.
- Chris Bank and Jerry Cao, *Web UI Design Best Practices*.
