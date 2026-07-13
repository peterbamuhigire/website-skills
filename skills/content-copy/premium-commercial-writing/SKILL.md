---
name: premium-commercial-writing
description: Use when website, authority, offer, SEO, or sales-enablement writing must justify premium fees through buyer insight, proof, clear claims, and editorial restraint; use the owning execution skill for publishing or page implementation.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Premium Commercial Writing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Apply a commercial editorial layer that makes important writing specific, credible, useful, and worthy of a serious buyer's attention.

<!-- dual-compat-start -->
## Use When

- Website copy, articles, offer pages, SEO content, case studies, or sales documents must support premium fees.
- Existing writing is generic, hype-led, synthetic, under-researched, or weak on proof.
- A page must persuade human buyers while remaining useful to search and AI-answer systems.

## Do Not Use When

- The task is purely technical or visual with no language implication.
- A regulated claim cannot be supported; stop rather than improve its persuasion.
- The task is implementation or publication; the owning page, blog, SEO, or document skill retains that authority.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Audience, offer, page type, and next action | Commercial brief | yes | Return the missing commercial decisions; do not draft generic premium copy. |
| Voice-of-customer and objection evidence | Interviews, sales/support notes, reviews, or search queries | conditional | Mark the draft inference-led and lower claim confidence. |
| Proof and source material | Client records and verified research | yes for material claims | Soften or remove unsupported claims and list evidence needed. |
| Brand, sector, language, and SEO constraints | Upstream owners | conditional | State provisional assumptions and route specialist questions. |

## Workflow

1. Define the writing's commercial job: rank, educate, compare, reassure, qualify, convert, retain, or enable sales.
2. Stop if the buyer, offer, proof burden, or next action is unresolved.
3. Build a market-message-offer brief: segment, problem, desired result, mechanism, objections, proof, risk, CTA, and follow-up.
4. Mine buyer language where evidence exists; label inference when it does not.
5. Draft around the buyer's decision sequence, not a prestige vocabulary list.
6. Place proof beside the claim and handle material objections without pressure tactics.
7. Add search and AI-answer structure only where it improves human usefulness.
8. Edit with [the genuine-writing gate](references/genuine-writing-and-ai-slop-gate.md) and [professional quality gate](references/professional-writing-quality-gate.md).
9. Return finished copy, source notes, evidence gaps, acceptance criteria, and implementation notes to the owning skill.
10. If evidence fails, revise or remove the dependent claim before handoff.

Recovery: repair the brief or evidence map, then rerun the professional and anti-slop gates.

## Quality Standards

- The opening or first screen orients the right buyer and makes the next step clear.
- Every important claim is proved, softened, attributed, or removed.
- Tone is confident and commercially serious without luxury adjectives, fake scarcity, or empty superlatives.
- CTAs name the buyer reward and next step.
- The draft contains specific business, buyer, sector, geography, proof, process, or source detail.
- Search structure never substitutes for a useful argument.

## Anti-Patterns

- Polishing before the page strategy exists. Fix: resolve buyer, offer, proof, and action first.
- Treating SEO as keywords or AI visibility as crawler files. Fix: answer real decisions with explicit entities and evidence.
- Borrowing authority from named frameworks. Fix: use the client's offer, buyer language, and proof.
- Copying source-book wording. Fix: distil operational principles and write original copy.
- Writing for everyone. Fix: qualify the right-fit buyer and acknowledge exclusions.
- Using fake urgency or unsupported prestige. Fix: state genuine constraints and verifiable value.
- Publishing clean but generic prose. Fix: add specific evidence and authored judgment or cut it.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Premium commercial draft or revision | Owning content skill and approver | Buyer, offer, proof, objections, CTA, and voice are explicit and coherent. |
| Message, proof, objection, and CTA banks | Future page and campaign owners | Entries are sourced, reusable, and labelled by audience or stage. |
| Editorial QA record | Release owner | Claims, source gaps, anti-slop checks, and implementation notes are complete. |

## References

- [Genuine writing and AI-slop gate](references/genuine-writing-and-ai-slop-gate.md) for every public draft.
- [Professional writing quality gate](references/professional-writing-quality-gate.md) for final editorial acceptance.
- [Website page patterns](references/website-page-writing-patterns.md) for common page types.
- [Offer and landing-page writing](references/offer-and-landing-page-writing.md) for direct-response flows.
- [Blog and authority writing](references/blog-and-authority-writing.md) for thought leadership and topical authority.
- [SEO and AI-search writing](references/seo-ai-search-writing.md) for answer structure and entity clarity.
- [Document and sales-enablement writing](references/document-and-sales-enablement-writing.md) for longer commercial assets.
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Market-message-offer brief | Structured notes | Buyer, problem, result, mechanism, proof, risk, CTA, and follow-up are present. |
| Claim and source record | Table or annotations | Each material claim has status and source. |
| Editorial gate result | Checklist | Unresolved evidence and implementation constraints remain visible. |

## Capability Contract

Read access to briefs, evidence, and existing copy is required. Search and network access are optional for current fact verification. Review defaults to read-only; editing requires authority. Publishing, production mutation, spending, and external communication are outside this skill unless separately authorised.

## Degraded Mode

Without research, source files, voice-of-customer evidence, or editing access, return a narrower qualified draft or review with assumptions and missing proof named. Never convert an unverified claim into polished certainty.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| High-value claim with strong proof | State specifically near the evidence | Vague differentiation |
| Important claim with weak proof | Soften, attribute, or remove | Misrepresentation |
| Buyer insight is inference-led | Label and propose validation | Synthetic certainty |
| Direct-response structure dominates | Compose with `sales-copywriting` | Weak conversion logic |
| Publishing or implementation requested | Hand off to owning skill | Unauthorised mutation |

## Worked Example

A consultancy calls itself "the leading digital partner" but supplies no ranking evidence. Replace the superlative with the firm's documented sector focus, delivery method, named proof, and a consultation CTA; record the missing comparative evidence.

## Read Next

- `content-writing` owns general website page copy.
- `blog-writer` owns article research and publishing handoff.
- `sales-copywriting` owns conversion frameworks.
- `seo` owns metadata, schema, and crawler implementation.
