# Design Critique Scorecard

Parent skill: [cro-audit](../SKILL.md). Read when a client, stakeholder or prospect asks for a judgement of a page, feature or competitor site ("Is our home page any good?"), when an audit needs a defensible section of expert opinion, or when preparing a one-page teardown before a first meeting.

This file complements [the heuristic checklist](heuristic-checklist.md), which scores pass or fail against fixed items. A critique answers a judgement question instead. It stays defensible because the criteria are declared before the judgement is made. Findings from a critique are heuristic unless backed by analytics or research; label them so, as the parent skill requires.

## 1. The four steps

1. **Declare the criteria.** Name three (at most four) standards before judging.
2. **Walk through the product.** Describe how it actually works before saying whether it works well.
3. **Weigh pros and cons per criterion**, with evidence and one comparison.
4. **Give the verdict.** One judgement, one priority change, a confidence level, and what would change your mind.

## 2. Step 1: declare the criteria

Choose criteria that fit the page's job and audience. Write each one as a testable sentence, not a single word.

### Criteria pool

Lin (2013) draws on Dieter Rams's ten principles of good design. Paraphrased, good design is: innovative; useful; aesthetic; understandable; unobtrusive; honest; long-lasting; thorough down to the last detail; environmentally friendly; and as little design as possible. Lin recommends useful, understandable, honest and innovative as the strongest to cite.

| Criterion | Testable sentence (template) |
|---|---|
| Useful | "Helps [audience] complete [task] without leaving the page for missing information." |
| Understandable | "A first-time [audience] on [device] can say what is offered and what to do next." |
| Honest | "Price, fees, conditions and limits are shown before commitment, and every claim can be evidenced." |
| Innovative | "Solves [problem] in a way competitors in [market] do not." |
| Unobtrusive | "Nothing interrupts the visitor before they have read the main offer." |
| As little design as possible | "Every element on the first screen earns its place for the page's job." |

### Rules

- Declare the criteria to the client before the walk-through, and get agreement where possible. A critique against agreed standards is harder to dismiss as taste.
- Do not use objective standards as criteria to hold opinions about. Accessibility is checked against WCAG 2.2 Level AA (register CW-05) and speed against Core Web Vitals (register CW-01). Route those to the relevant audit as pass or fail checks and cite the results.
- Visual judgements (typography, colour, layout, visual identity) are routed to the design-system-skills engine; cite its guidance rather than improvising.
- Keep "honest" in the set for any page that asks for money or personal data. It links the critique to the [ethical persuasion gate](ethical-persuasion-gate.md).

## 3. Step 2: walk through before judging

Critiquing a version of the product the audience does not recognise destroys credibility.

1. State the page, journey, device, viewport and date.
2. Describe the visitor's path in neutral language: what they see first, what they can do, what happens when they do it, where the path ends.
3. Capture screenshots of each state, including errors and the confirmation state.
4. Confirm with the client that this is the version and journey they mean.
5. If you have not used the product or could not reach a state (logged-in pages, payment), say so and mark it `not assessed`.

## 4. Step 3: pros and cons per criterion

For each criterion, record specific evidence and one comparison with a similar product or a reference site the client respects.

| Criterion | Pros (evidence) | Cons (evidence) | Comparison | Confidence |
|---|---|---|---|---|
| [Criterion as testable sentence] | [What works, with capture reference] | [What fails, with capture reference] | [How a named comparable handles it] | High / medium / low |

Rules:

- Every pro and con points to a capture, a quote or a data source.
- One comparison per criterion is enough. Choose a comparable in the same market where possible, because a global brand's approach may not suit a local audience.
- Critique your own recommendation briefly: state the strongest argument against it.

### Optional score

A 1–5 score per criterion helps comparison over time. Define the anchors before scoring:

- 1: fails the testable sentence for most visitors.
- 3: meets it with visible friction or gaps.
- 5: meets it fully, with evidence.

Do not add the scores into a single total; the criteria are not equal and a sum suggests false precision.

## 5. Step 4: the verdict

Write one short paragraph:

- The overall judgement against the declared criteria.
- The single change that would matter most, and why it beats the alternatives.
- The confidence level and its basis (observation only, or supported by analytics or research).
- What would change the verdict: the test, research or data that should follow. Hand test candidates to the backlog in [the evidence-led conversion system](evidence-led-conversion-system.md).

Do not promise a result from the recommended change.

### Phrase bank

- "We judged the page against three standards agreed with you: [criteria]."
- "Before judging, here is how the page works today on a mid-range Android phone: [walk-through]."
- "On [criterion], the page does [pro]; however, [con], as screenshot [n] shows. [Comparable] handles this by [approach]."
- "Our verdict: [judgement]. The change that matters most is [change], because [reason]. This is an expert judgement; we recommend [test or research] to confirm it."
- "The strongest argument against this recommendation is [argument]. We still recommend it because [reason]."

## 6. Worked example (illustrative)

A Kampala private school asks whether its admissions page is good.

- **Criteria agreed:** understandable ("a parent on a phone can find fees, entry requirements and how to apply within one screen of scrolling"); honest ("all fees, including uniform and development levies, are shown before the enquiry form"); useful ("a parent can book a visit without phoning").
- **Walk-through:** on a 360-pixel-wide Android viewport, the page opens with a photo carousel, then a welcome letter, then an enquiry form. Fees appear in a PDF linked from the footer. Visit booking is by phone only.
- **Pros and cons:** understandable scores 2 (fees and requirements are hidden below the form); honest scores 2 (the PDF omits levies that parents report in reviews); useful scores 1 (no online booking). A comparable school in the same area shows a fees table and a visit calendar on the page.
- **Verdict:** the page does not meet the agreed standards. The priority change is a fees table with every levy, placed above the form, because parents' main question is cost and hiding it undermines trust. Confidence: medium (observation plus review quotes, no analytics yet). Next: add form-start and PDF-click events and review four weeks of data.

## 7. Pre-meeting teardown (sales use)

A one-page critique of a prospect's public page can open a first meeting. Keep it to three criteria, one walk-through, one priority change.

- Use public pages only. Do not log in, submit forms with false details or collect personal data.
- Label it as an outside, heuristic view prepared without the prospect's data.
- Present it as a conversation starter, not a verdict on the prospect's team.
- Do not promise outcomes. Commercial wording for any follow-on proposal belongs to the proposal-skills engine.

## 8. Anti-patterns

| Anti-pattern | Correction |
|---|---|
| Judging before stating the criteria | Declare and agree criteria first |
| Critiquing a version the client does not recognise | Walk through and confirm the version |
| "It feels cluttered" with no evidence | Point to captures, quotes or data |
| Treating accessibility or speed as opinion | Route to WCAG and Core Web Vitals checks |
| Summing criterion scores into one number | Report scores per criterion |
| Presenting a heuristic verdict as proven | Label confidence; propose the test |

## Sources

- Lin, L. C. (2013) *Decode and Conquer: Answers to Product Management Interviews*, 2nd edn. Impact Interview. (Design critique method: declared criteria from Dieter Rams's ten principles, walk-through before judging, pros and cons with comparison, verdict; pre-meeting redesign.)
- Currentness register 2026-09-23, claims CW-01 and CW-05.
