# Research Report — Closing the Go-to-Market Gaps from the "Web Design Is Just Getting Started" Reddit Post

**Date:** 2026-06-13
**Author:** Research wave run via the digital-research-engine (4 parallel cohorts), synthesised by the orchestrator.
**Status:** Findings + recommended skill specs — awaiting approval before any SKILL.md is written.

---

## 1. Why this report exists

A Reddit post argued that web design as a *business* is just getting started: AI makes custom builds fast and cheap, the
standard is rising (tracking, SEO/GEO, A/B testing, automated reporting), and the winning go-to-market is **in-person local
sales + hard niching + generous referrals + your own custom tooling**. We mapped the post's 10 themes against the
website-skills engine and ran a 4-cohort research wave on the genuine gaps.

### Coverage map (10 themes)

| # | Theme | Status | Where it lives |
|---|---|---|---|
| 1 | Custom build vs Wix/Squarespace as the new standard | COVERED | `orchestration/premium-website-product`, `agency-ops/agency-positioning` |
| 2 | SEO/GEO (AI search) as standard deliverable | COVERED | `seo-search/google-ai-search`, `seo-search/seo` |
| 3 | Conversion tracking / measurability for SMBs | COVERED | `launch-ops/marketing-measurement-system`, `launch-ops/observability` |
| 4 | Automated monthly performance reports | COVERED | `agency-ops/monthly-report` |
| 5 | A/B testing / optimisation as ongoing service | COVERED | `launch-ops/experimentation` |
| 6 | **In-person / local door-to-door acquisition** | **GAP** | — |
| 7 | **Niche-down agency positioning ("web design for X")** | **PARTIAL** | `build/sector-strategies` is design-side only |
| 8 | **Generous client referral programs + cross-niche** | **GAP** | — |
| 9 | **Custom CMS / internal tooling / automation for speed** | **PARTIAL** | process-design only, not build-for-speed |
| 10 | Productized / fast delivery as advantage | COVERED | `agency-ops/agency-client-retention`, `service-blueprint-website-delivery` |

**Conclusion:** the engine already supports 6 themes well. Four need work: two true gaps (6, 8) and two partial gaps (7, 9).

---

## 2. Research findings by cohort

Full agent outputs (raw, sourced) are retained in conversation. Highlights and the strongest-confidence facts below.
Confidence tiers: **[P]** peer-reviewed/named-org primary, **[A]** stat-aggregator (vendor blog citing unnamed study — treat as
"industry-reported"), **[B]** book/practitioner model (reliable model; confirm exact numbers against the text).

### Cohort A — In-person / local acquisition

- **[P] 82% of buyers accept meetings with sellers who proactively reach out** — RAIN Group Center for Sales Research (488 buyers / 489 sellers). HubSpot ranks "meeting in person" as the #1 most effective sales channel.
- **[A] Door-to-door converts ~2–5% of knocks vs ~1% digital;** well-run teams hit 30–40% contact rate and 30–40% close on qualified leads (SPOTIO).
- **[A/practitioner] Web-design-specific:** ~100 quality contacts → 2–5 clients; 80% of deals need ≥5 touchpoints; reply rates roughly double when a free 5-min video audit is attached (QCFixer — "double" claim UNVERIFIED at primary).
- **The audit-as-door-opener** is the recurring play: a 5-minute checklist (mobile, PageSpeed, SSL, stale footer year, CTA above fold, GBP connected, clickable phone) drives the conversation. White-label tools exist (SEOptimer, Insites).
- **Pitch canon:** SiteSwan 30-second pitch; SPOTIO 10-second opener; lead with a free offer (Selling Signals); walk-in etiquette = be a customer first, never pitch mid-rush.
- **Objection scripts** for the 5 SMB classics ("don't need one / too expensive / no time / I'll DIY / I have Facebook").
- **Cadence + CRM:** 25–50 contacts/day; 2-week follow-up sequence (Day 1/3/7/14); track interactions not just knocks; tools SalesRabbit/SPOTIO; qualify with BANT at the doorstep.
- **Books/people:** Jeb Blount *Fanatical Prospecting* (coins "in-person prospecting"); RAIN Group; Carew International (LAER objection model); SiteSwan (most agency-specific content).

### Cohort B — Niche-down positioning

- **[B] Blair Enns, *Win Without Pitching* — proclamation #1 is "We will specialize."** Three payoffs: higher win rate, price premium, more power in the relationship.
- **[B] Philip Morgan — 5 specialization types** (Pure Vertical, Audience, Pure Horizontal, Platform, Service) + a 6-step selection process with scoring (Aggregate = Impact + Profit + Interest; Risk = 7 − Access − Credibility).
- **[B] Morgan's market guardrails (attrib. to David C. Baker):** target a vertical with **1,000–10,000 prospects** and **10–100 competitors**. <10 competitors = no demand; >100 = red ocean. (The post's "3,000 beauty businesses in our city" sits squarely in range.)
- **[B] David C. Baker — "default should be vertical because it's so easy to find your clients";** vertical vs horizontal decision rules; T-shaped expertise; NAICS codes to define a vertical.
- **[B] April Dunford *Obviously Awesome*** — 5 components of positioning; **Seth Godin — Smallest Viable Market.**
- **Positioning statement formula:** specific audience + expensive problem + distinct approach; pass the 12-second / stranger test; ban buzzwords.
- **Risk + mitigation:** concentration risk; mitigated by "Vertical Core + Horizontal Edge" and staged expansion to *adjacent* niches only after dominance (≈15–20 clients + documented results — figure UNVERIFIED).
- **[A] Pricing claims:** specialist margins 25–40% vs generalist 15–20%; "niche agencies charge 2–4× more" — all vendor-blog, UNVERIFIED at primary. Frame as "industry-reported," not fact.

### Cohort C — Referral programs

- **[P] Referred customers are ~16% more valuable and ~18% less likely to churn** — Schmitt, Skiera & Van den Bulte, *Journal of Marketing* 2011 (10,000 customers, 33 months; MSI Root Award). This is the anchor fact.
- **[A] The intention–action gap:** 83% of satisfied customers say they'd refer, only 29% do — the gap is *asking + making it easy* (GrowSurf).
- **[A] 78% of referral programs are now double-sided** (reward both parties) — reduces B2B awkwardness.
- **[B] John Jantsch *The Referral Engine*:** reframe the ask as "helping them get more of what they want"; set the referral expectation **at project kickoff**; build a "referral toolbox." Know→Like→Trust→Try→Buy→Repeat→Refer.
- **[B] Joey Coleman *Never Lose a Customer Again*:** 8 phases ending in **Advocate**; 20–70% of new customers churn in the first 100 days — earn the referral first.
- **[B] Reichheld NPS:** ask Promoters (9–10); trigger the referral ask within 24–48h of a high score.
- **Agency reward norms:** ~$500 per referral that becomes a website sale + 10% on other services; or 10% of project up to a cap; general range 5–25%. Pay only after qualified/closed. Charity-donation and reward-menu options suit professional networks.
- **Cross-niche:** route referrals outside your niche to partners / sibling lines (Neighborly 19-brand cross-referral model). Reward the client who refers another vertical, and tell referral-sourced leads you serve other niches too (the post's exact move).
- **Systematise:** the #1 failure is informal intros with no timestamped record/attribution (Pipedrive). Need a formal submission + CRM attribution. Distinguish *client referral* (light) from *partner program* (contracted).
- **Ethics flag:** some professional contexts restrict referral fees / require disclosure — keep a disclosure + ethics check in scope.

### Cohort D — Custom tooling & delivery automation

- **[P/named-org] AI reality check (critical, anti-hype):** METR RCT (July 2025) — experienced devs *expected* 24% speedup, *got 19% slowdown* on real codebases. Stack Overflow 2025 — 84% use AI but trust fell to 29%; 66% spend more time fixing "almost-right" code. Faros AI (10k devs) — more PRs merged but review time +91%, change-failure +~30%, no DORA gain. **Lesson: AI accelerates greenfield/boilerplate, not maintenance/review; quality gates become the constraint.**
- **[A] Productized/specialist agencies report 40–75% gross margin vs 18–22% industry average** (Predictable Profits via Wayfront — UNVERIFIED at primary, frame as industry-reported). Mechanism: repeat the same service → templates → kill the learning curve.
- **[B] John Warrillow *Built to Sell*:** a sellable service = **Teachable, Valuable, Repeatable** → productize the one thing you do best at fixed scope/price. **Gerber *E-Myth*:** work *on* the business via systems.
- **What agencies build:** starter kits/boilerplates, design systems/token libraries, conditional intake forms, content pipelines, QA/deploy automation, reporting automation (already our `monthly-report`), proposal/contract automation.
- **Build vs buy:** custom CMS gives control but **handover/lock-in risk without clean docs + knowledge transfer**; off-the-shelf gives auto-maintenance. TCO hidden costs are real.
- **Automation-opportunity audit:** inventory repeatable processes → time them for a week → score by **Volume × Time × Frequency × Complexity**; pilot one, measure, then expand. Heuristic: "judgment → hire; repetitive + rule-based → automate."
- **SOPs/playbooks** make output repeatable: onboarding, request handling, comms standards, QC checklists; internal wiki before scaling.

---

## 3. Recommended skill build (for approval)

Premium-default, African-3G-aware, SKILL.md canonical structure per `docs/doc-style-guide.md`, acknowledgement line under
the H1, sourced references with attribution (per the digital-research-engine mandate). Proposed:

### S1 — `agency-ops/local-in-person-acquisition` (NEW skill) — closes Theme 6
The post's centrepiece. Operational playbook for niche-first, in-person local prospecting as the anti-spam channel.
- **SKILL.md:** the case (in-person = #1 channel); territory/route planning; daily cadence (25–50 contacts); the audit-as-door-opener; the 30-second pitch + opener templates; reaching the decision-maker; walk-in etiquette; 5-objection script bank; 2-week follow-up sequence; visit→conversation→meeting→sale funnel KPIs; CRM logging + BANT.
- **References:** `walk-in-pitch-scripts.md`, `5-minute-audit-checklist.md` (ties into our `seo-audit`/`visual-qa`), `objection-bank.md`, `cadence-and-crm.md`, `sources.md` (Blount, RAIN Group, SPOTIO, SiteSwan, QCFixer + URLs).
- **Africa calibration:** brick-and-mortar SME density, cash/mobile-money pricing framing, relationship-first cultural norms (links `orchestration/africa-excellence`).

### S2 — `agency-ops/referral-program` (NEW skill) — closes Theme 8
- **SKILL.md:** why referrals (the [P] 16%/18% anchor); reward-structure menu (double-sided, cash/credit/charity, tiered, agency fee norms); the ask (kickoff expectation, NPS-triggered timing, scripts + email templates); make-it-easy mechanics; cross-niche/partner routing + rewarding cross-vertical referrals; formal tracking/attribution (anti-"informal intro" failure mode); ethics/disclosure check.
- **References:** `reward-structures.md`, `ask-scripts-and-timing.md`, `cross-niche-and-partners.md`, `tracking-and-ethics.md`, `sources.md` (Schmitt/Skiera/Van den Bulte, Jantsch, Coleman, Reichheld + URLs).
- **Integrates:** `agency-client-retention` (Advocate phase), `monthly-report` (referral KPIs).

### S3 — Enhance `agency-ops/agency-positioning` (EDIT) — closes Theme 7
Add a **niche-down positioning** section rather than a new skill (positioning already lives here).
- Enns "specialize" argument; Morgan's 5 types + selection scoring; **1,000–10,000 prospect / 10–100 competitor guardrails**; vertical-vs-horizontal decision; positioning-statement formula; concentration risk + "Vertical Core + Horizontal Edge"; staged adjacent-niche expansion. New reference: `niche-selection-rubric.md`. Cross-link `build/sector-strategies` (design-side) so the two halves connect.

### S4 — `agency-ops/delivery-automation` (NEW skill) — closes Theme 9
- **SKILL.md:** the productization economics (Built to Sell: Teachable/Valuable/Repeatable); what to build (starter kits, design-system/token reuse — links `build/design-system`, intake forms — links `ux-conversion/form-ux-design`, QA/deploy automation — links `launch-ops/deploy`, reporting — links `monthly-report`); build-vs-buy rubric incl. handover/lock-in risk; **honest AI-assisted-delivery section** (METR/Faros/SO 2025 — accelerate greenfield, not review; quality gates are the constraint); automation-opportunity audit (Volume×Time×Frequency×Complexity, pilot-then-expand); SOP/playbook library.
- **References:** `build-vs-buy-rubric.md`, `automation-opportunity-audit.md`, `ai-assisted-delivery-reality.md`, `productized-delivery-sops.md`, `sources.md` (Warrillow, METR, Faros, Stack Overflow 2025 + URLs).

### Cross-cutting
- Update root `CLAUDE.md` agency-ops count (11 → 13) and the orchestration narrative ("Commercial layer" gains local acquisition + referrals).
- Add a one-line index entry per skill; run `meta/skill-safety-audit` after the build.
- Add a `sources.md` to each skill with full attribution + UNVERIFIED flags (digital-research-engine mandate).

---

## 4. Honest cautions baked into the specs

- **AI-speed claims are oversold.** Cohort D's primary evidence (METR, Faros, SO 2025) contradicts the Reddit optimism for
  maintenance/complex work. The `delivery-automation` skill must state this plainly, not parrot "AI makes it 10× faster."
- **Pricing/margin premiums for niching are vendor-blog claims**, not primary research. Frame as "industry-reported."
- **Referral fees carry ethics/disclosure obligations** in some contexts — kept in scope, not assumed away.
- **Door-to-door numbers** are mostly aggregator/practitioner; the one solid primary is RAIN Group's 82% meeting-acceptance.

---

## 5. Decision requested

Approve the build of S1–S4 (2 new skills + 1 enhancement + 1 new skill, plus cross-cutting updates), or adjust scope.
On approval, recommended order: S3 (quick enhancement) → S1 (the post's core idea) → S2 → S4, then doc updates + safety audit.
