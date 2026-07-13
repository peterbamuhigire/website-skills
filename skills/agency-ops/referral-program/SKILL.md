---
name: referral-program
description: "Use when designing a consent-based client referral programme with reward, timing, attribution, partner routing, and disclosure rules. Use `agency-client-retention` to earn advocacy and `local-in-person-acquisition` for cold local outreach."
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Referral Program
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Designing a client referral program from scratch for a web/branding studio.
- Choosing reward structures and amounts (cash, credit, charity, tiered, fees).
- Deciding when and how to ask clients for referrals, and writing the scripts.
- Routing referrals that fall outside your niche to partners or a sibling line.
- Setting up referral tracking, attribution, and payout rules.
- Checking referral-fee ethics and disclosure obligations.

## Do Not Use When

- The task is keeping/expanding an existing client's spend (use
  `agency-client-retention` — though its Advocate phase feeds this skill).
- The task is in-person cold acquisition (use `local-in-person-acquisition`).
- The task is the agency's overall offer, pricing, or qualification (use
  `agency-positioning`).
- The task is a paid affiliate / reseller channel with formal contracts and
  product training at scale — that is a partner program; this skill covers the
  client-referral and lightweight-partner case, and points to the distinction.

## Inputs

- A base of delivered, satisfied clients (or a near-term path to one).
- The agency's market and fee floor (from `agency-positioning`) to size rewards.
- A way to capture a referral submission and attribute it (CRM, form, or log).

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Verified client satisfaction and permission posture | Account records | yes | Do not ask; repair or validate the relationship. |
| Reward economics and authority | Finance and leadership | yes | Design options only; do not promise or pay. |
| Attribution, disclosure, and privacy rules | CRM, counsel, and operations | yes | Stop activation and obtain approved rules. |

## Workflow

1. **Earn the referral before asking.** A referral program on top of mediocre
   delivery fails. Confirm the client has reached the Advocate phase — they have
   experienced a clear win (see `agency-client-retention`).
2. **Choose the reward structure.** Default to double-sided (reward both the
   referrer and the new client). Offer a small menu (cash/credit, charity
   donation, or service credit) so professional referrers aren't forced into an
   awkward cash gift. See `references/reward-structures.md`.
3. **Set the ask into the relationship early.** At project kickoff, tell the
   client you'll ask for introductions at the review once they're delighted —
   so the later ask is expected, not a surprise. See
   `references/ask-scripts-and-timing.md`.
4. **Ask at peak happiness.** Trigger the ask right after a measurable win or a
   high satisfaction signal (e.g. within 24–48h of a 9–10 NPS score), not on a
   random calendar date.
5. **Make it effortless.** Give the client the exact words to forward, a
   referral link or form, and a clear description of who is a good fit. The gap
   between willing-to-refer and actually-referring is almost entirely friction.
6. **Route cross-niche referrals.** When a client refers a business outside your
   niche, reward them anyway and route the lead to a partner or sibling line.
   Tell referral-sourced leads you also serve other niches. See
   `references/cross-niche-and-partners.md`.
7. **Track formally and attribute at submission.** Capture every referral with a
   timestamped record and a named source. Pay only after the referral is
   qualified and closed. See `references/tracking-and-ethics.md`.
8. **Check ethics and disclose.** Confirm referral fees are permitted and
   disclosed where the client's sector or your jurisdiction requires it.
9. **Report referral KPIs.** Feed referral count, source, conversion, and value
   into the monthly client/agency reporting (`monthly-report`).

8. Stop activation when consent, disclosure, satisfaction, or payout authority is missing; recover with draft rules and a gap register.

## Quality Standards

- **Generosity is deliberate.** The reward is large enough that clients feel
  genuinely thanked, sized against the lifetime value of a won client — referred
  clients are measurably more valuable and less likely to churn.
- **Double-sided by default.** The new client gets something too, so the
  referrer feels they did their contact a favour, not sold them.
- **Ask at the right moment, with the right words.** Timing (post-win) and ease
  (a ready-to-send intro) matter more than the size of the reward.
- **Formal record, not informal intros.** Every referral has a timestamped
  submission and an unambiguous source; payout rules are written and known.
- **Ethical and disclosed.** No undisclosed fees in contexts that forbid them.
- **Built on real delivery.** The program amplifies genuine satisfaction; it
  never substitutes for it.

## Anti-Patterns

- Launching before clients experience a win. Fix: require a verified satisfaction trigger.
- Using a one-sided reward that embarrasses the referrer. Fix: offer an approved double-sided or non-cash structure.
- Asking on a fixed date. Fix: ask after a verified outcome and with no pressure.
- Relying on informal "send people my way" with no submission record or
  attribution — the most common reason programs quietly fail.
- Setting a token reward without economics. Fix: size and approve it against the qualifying event and margin.
- Paying on an unqualified lead. Fix: tie payout to the documented qualifying event.
- Ignoring disclosure rules. Fix: obtain and record the required sector-specific disclosure.

## Outputs

- A documented referral program: reward structure, amounts, and payout rules.
- The kickoff expectation-setting line and the post-win ask scripts/templates.
- A referral submission + attribution mechanism and a tracking log.
- A cross-niche / partner routing rule and reward.
- Referral KPIs wired into monthly reporting.

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Referral programme rules | Clients, partners, finance, and sales | Names eligibility, reward, attribution, disclosure, privacy, payout, expiry, and disputes. |
| Ask and routing plan | Account owner | Uses earned timing, permission, one clear submission route, and no-pressure language. |
| Referral register | Finance and reporting owners | Every record has source, consent, status, attribution, reward, and outcome. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Satisfaction trigger | Dated verified win or explicit advocacy signal | No ask rests on assumed happiness. |
| Reward audit trail | Referral, rule version, approval, payout evidence | Rewards reconcile and disclosures are recorded. |

## Capability Contract
Design and review default to read-only. Sending asks, sharing contact data, changing CRM, promising or paying rewards, or creating partner obligations requires explicit authority and consent.

## Degraded Mode
Fallback if satisfaction, economics, consent, or legal review are unavailable: return draft rules and a gap register. Do not ask, introduce, promise, pay, or claim programme performance.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Client has a verified win and consents | Make a specific low-pressure ask | Extractive request before advocacy |
| Professional rules restrict rewards | Use permitted recognition or no reward | Undisclosed conflict or ethics breach |
| Referral is outside niche | Route through an approved partner rule | Poor-fit acceptance and attribution dispute |

## Worked Example
At a 90-day review, a client confirms the site reduced missed enquiries. With permission, ask for one introduction to a similar business, disclose a service credit, record the introduction source, and pay only after the documented qualifying event.

<!-- dual-compat-end -->

## References

- `references/reward-structures.md` — double-sided vs one-sided, cash / credit /
  charity / tiered options, agency referral-fee norms, and how to size rewards.
- `references/ask-scripts-and-timing.md` — setting the expectation at kickoff,
  NPS-triggered and post-win timing, and copy-ready ask scripts and email templates.
- `references/cross-niche-and-partners.md` — rewarding and routing referrals
  outside the niche, building a reciprocal partner network, and the client-referral
  vs partner-program distinction.
- `references/tracking-and-ethics.md` — formal submission, attribution, payout
  gating, the informal-intro failure mode, and referral-fee ethics / disclosure.
- `references/sources.md` — attributed sources (Schmitt/Skiera/Van den Bulte,
  Jantsch, Coleman, Reichheld) with confidence flags.

## Notes

- This skill is a portable execution layer for both Claude Code and Codex.
- Upstream: `agency-client-retention` (Advocate phase) earns the referral.
  Downstream: `local-in-person-acquisition` and `agency-positioning` convert the
  referred lead; `monthly-report` reports referral performance.
- Africa calibration: in relationship-first markets, personal introductions carry
  high trust; charity-donation and service-credit rewards often fit professional
  networks better than cash. Frame rewards in the local market band — see
  `../../orchestration/africa-excellence/SKILL.md`.
- This skill has no bundled scripts; the workflow is documentary.
