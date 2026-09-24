# Plain-Language Explainer Recipe

Parent skill: [blog-writer](../SKILL.md). Read when an article, or a section of a technical service page, must explain a technical idea (hosting, caching, domain records, payment integration, data backups, two-factor login, a compliance requirement) to a buyer who decides but does not build. Complements [writing craft](writing-craft.md) and [reader experience](reader-experience.md), which cover prose and register in general; this file is a fixed procedure for one job.

Confused buyers do not buy. A technical service is sold to the person who pays, and that person needs to understand what they are paying for well enough to explain it to a colleague or a board.

## 1. The recipe

Work through the five moves in order. Each move is one short paragraph or less.

| Move | Job | Test |
|---|---|---|
| 1. Definition | State the accurate, formal definition in one sentence. | A specialist would accept it as correct. |
| 2. Notice where it fails | Name the word or idea in the definition the reader will not follow. | You can point to the exact term that loses a non-specialist. |
| 3. Analogy | Replace the failing idea with an everyday comparison from the reader's own world, and say where the comparison stops. | The reader could repeat the analogy to someone else. |
| 4. Drop the advanced detail | Move specifications, edge cases and vendor names out of the main text into a "for your technical team" box or a linked page. | The main text contains nothing the decision does not depend on. |
| 5. Answer the objection | State the reader's most likely doubt or cost worry and answer it directly. | The answer includes a number, a trade-off or a condition, not reassurance alone. |

Close with what the reader should do or ask next (one step).

## 2. Choosing the analogy

1. Draw it from something the reader handles every week: a shop and its stock room, a matatu route, a mobile-money agent, a school timetable, a filing cabinet, a building's security guard.
2. Match the analogy to the part of the concept that matters for the decision. An analogy for how DNS works is wasted if the decision is only about who controls the domain.
3. State the limit in one clause: "Unlike a real warehouse, the copies update themselves within minutes."
4. Use one analogy per concept. Mixed comparisons confuse more than jargon does.
5. Avoid analogies that could offend or stereotype a group, and avoid ones tied to a single ethnic, religious or political reference.
6. Test it: read the analogy to someone outside the field and ask them to explain the idea back in their own words. If they cannot, change the analogy, not the reader.

## 3. Keeping the detail out without hiding it

- Main text: what it is, why it matters to this buyer, what it costs or risks, what to ask.
- "For your technical team" box: specifications, standards, configuration choices, vendor options.
- Glossary link for any term you must keep. Define it once, the first time it appears, then use it consistently.
- Never simplify to the point of being wrong. If a simplification changes the decision, keep the accurate version and explain it.

## 4. Building the objection answer

List the doubts buyers actually raise, from call notes, emails and the buyer-question register in [they-ask-you-answer](../../../ux-conversion/they-ask-you-answer/SKILL.md). The common ones for technical services:

| Doubt | Shape of the answer |
|---|---|
| "Do I really need this?" | The condition under which they do and the condition under which they do not. |
| "What does it cost?" | A price range or the drivers of cost, with the source; if unknown, say how to find out. |
| "What happens if we skip it?" | The concrete failure and how likely it is for a business like theirs, stated honestly. |
| "Will it slow us down or disrupt staff?" | Time, steps and who does them. |
| "Can we switch later?" | What lock-in exists and how to avoid it. |

Answer the objection even when the honest answer is "you may not need this yet". Candour here is what makes the rest of the page credible.

## 5. Options tables for "how do we reduce or fix X" articles

When the article compares approaches (for example, ways to reduce downtime or protect customer data), lay the options in a table, then recommend.

| Approach | What it is | Pros | Cons | How to reduce the con |
|---|---|---|---|---|

Then state the recommendation in two or three sentences: what you recommend, why it suits this reader, and why it beats the alternatives. Recommending a combination is legitimate if you say why.

## 6. Placement on a technical service page

1. Hero: the buyer's outcome, not the technology.
2. Short explainer block (the five moves, compressed to four to six sentences).
3. What is included and what the buyer receives.
4. Objection block.
5. Technical detail box or link.
6. Next step.

## 7. Worked example (illustrative)

Topic: explaining a content delivery network to a hotel owner in Entebbe whose booking page loads slowly for guests abroad.

1. Definition: "A content delivery network stores copies of your website's files on servers in many countries and serves each visitor from the nearest one."
2. Where it fails: "servers in many countries" and "serves from the nearest" mean little to a hotel owner.
3. Analogy: "Think of it like keeping a stock of your brochures at travel agents in London, Dubai and Nairobi instead of posting each one from Entebbe when someone asks. Unlike brochures, the copies update themselves when you change the site."
4. Detail moved to the technical box: caching rules, which files are cached, provider options, how updates are purged.
5. Objection: "Will this cost much?" Answer with the price range from the provider's current price page (checked on the day of writing, with the date recorded), what the hotel receives, and the condition under which it is not worth paying: "If nearly all your bookings come from within Uganda, fix image sizes first; that usually matters more."

Next step: "Ask your developer how long your booking page takes to load from London, and whether images are compressed."

## 8. Before and after (illustrative)

- Generic: "We implement scalable, next-generation cloud infrastructure using advanced CDN technology for optimal performance."
- Plain and professional: "Your booking page is slow for guests in Europe because every file travels from one server. We keep copies of the page closer to them, so it opens quickly wherever they are. If most of your guests book from within Uganda, we will tell you that this is not your first fix."

## 9. Acceptance checklist

- [ ] The formal definition is accurate and a specialist has checked it.
- [ ] The failing term is named and replaced by one analogy with its limit stated.
- [ ] The analogy passed an explain-back test with a non-specialist.
- [ ] Specifications and vendor detail sit outside the main text.
- [ ] The main objection is answered with a number, trade-off or condition.
- [ ] Any price, speed or statistic is sourced and dated, or presented as a check the reader should run.
- [ ] The section ends with one next step.

## Sources

- Lin, L. C. (2013) *Decode and Conquer: Answers to Product Management Interviews*, 2nd edn, Impact Interview — explaining a hard concept to a lay listener (definition, notice it fails, everyday analogy, keep advanced detail out, answer the main objection) and the solution-space options table.
- Debelak, D. (2006) *Business Models Made Easy*, Entrepreneur Press — "confused customers never buy" and the explain-back test for concept statements.
- Landa, R. (2022) *Strategic Creativity: A Business Field Guide to Advertising, Branding, and Design*, Routledge — use the exact word rather than an impressive one; let the reader decode a little but never be cryptic.
