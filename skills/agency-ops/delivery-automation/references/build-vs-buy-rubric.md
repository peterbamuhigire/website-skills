# Build vs Buy Rubric

**Purpose**: Decide, per delivery component, whether to build something custom or
use an existing platform — weighing speed and control against maintenance,
lock-in, and handover risk.

**Read this when**: choosing a CMS, stack, or tool, or considering a custom CMS.
Assumes you have read `delivery-automation/SKILL.md`.

---

## Default to buy; build only when the rubric says so

Custom tooling is a liability until proven otherwise: someone has to maintain it,
document it, and hand it over. Default to a proven platform and build custom only
when the automation audit (`automation-opportunity-audit.md`) shows a repeated,
high-volume, high-time process that no off-the-shelf tool serves well.

## Score each component

For a given component (CMS, intake, deploy, a tool), rate:

| Factor | Build leans higher when… | Buy leans higher when… |
|---|---|---|
| Volume × frequency | The task repeats across most projects | It's occasional or one-off |
| Fit | No tool matches the niche workflow | A tool fits well enough |
| Control needed | You need behaviour no tool offers | Standard behaviour is fine |
| Maintenance capacity | You can own updates/patches long-term | You'd rather the vendor maintain it |
| Handover risk | You can document and hand over cleanly | Clients need self-serve, no-code editing |
| TCO over 3 years | Build cost < cumulative licence + workaround cost | Licence + hosting is cheaper than dev time |

If "buy" wins most rows, buy. Build only where fit and control genuinely have no
adequate purchased option.

## CMS specifically: custom vs off-the-shelf

- **Custom CMS pros:** features tailored to the niche; full ownership of content,
  design, and functionality; add modules without platform limits.
- **Custom CMS cons:** expensive to build; **all maintenance, patching, and
  security fall on you**; you lose the well-tested components a mature platform
  provides.
- **Off-the-shelf pros:** the vendor handles updates and security; clients can
  self-edit via a dashboard with no code.
- **The handover trap:** without clean documentation, code handover, and
  knowledge transfer, a custom CMS **locks the client to one agency** — a
  reputational and ethical risk, and a barrier to the client treating the site as
  a transferable asset. If you build custom, documentation and a handover path are
  part of the deliverable, not optional.

## Platform lock-in spectrum (reference)

- WordPress and headless content export relatively easily (lower lock-in).
- Shopify and Webflow create more lock-in (harder to move off).
- Headless setups give code/content ownership but demand more up-front
  development investment.

Choose deliberately: for clients who must self-edit and own their site long-term,
a maintained platform usually beats a bespoke CMS. For a tightly repeatable niche
product, a templated build on a portable stack can lower TCO — if you commit to
the documentation discipline.

## TCO honesty

Licence and hosting fees understate true cost; maintenance, developer time,
plugins, and migration dominate over a multi-year horizon. Compare build vs buy on
**three-year total cost of ownership**, not sticker price, and include the cost of
*your* time to maintain anything custom.

## Sources

See `sources.md`. Custom-vs-off-the-shelf CMS pros/cons and the handover/lock-in
risk draw on SAM Solutions and Buddy WDD; the lock-in spectrum and TCO points on
Webflow/headless/WordPress comparisons (Webstacks, Bejamas, Kawn, Hubstic).
