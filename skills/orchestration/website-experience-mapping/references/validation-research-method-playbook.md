# Validation Research Method Playbook

Parent skill: [website-experience-mapping](../SKILL.md). Read when planning problem interviews, fast prototype tests, five-second tests, guerrilla sessions, surveys, or research with people who abandoned a product, before committing design or build effort.

Use with `discovery-interview-guide.md` (outside-in buyer interviews). This file covers validation-stage methods and session discipline.

## 1. Pick the method from the question

| Question | Method |
|---|---|
| Do people have this problem? | Contextual inquiry / observation of current work |
| Will people pay or act to solve it? | Landing page, feature stub or pre-order test (see experimentation playbook) |
| Does this design solve the problem? | Prototype test with tasks |
| Does the page communicate clearly at first sight? | Five-second test |
| Where do new users fail? | Guerrilla or unmoderated task test |
| Why do users fail? | Moderated usability session |
| Which version performs better at scale? | A/B test |
| Is a pattern from interviews real across the audience? | Survey |
| Will users like a feature? | Prototype test |
| Will users buy a feature? | Behavioural test only (stub, fake button, A/B); never ask |

Rule: never ask people whether they would use or buy something. Show them something and observe; measure what they do.

## 2. Value-proposition validation (five steps)

1. **Define the primary customer segment** narrowly: demographics, behaviour and context. "Everyone affected by X" is not a segment. Check that the funnel type matches (a business buyer needs a B2B path).
2. **Name the segment's single biggest problem.** One problem, framed as what keeps them awake.
3. **Write provisional personas** explicitly labelled as assumptions: name, demographics, goals, motivations, social/technical/physical environment, pain points and stress points.
4. **Run problem interviews** to validate or invalidate the personas (section 3).
5. **Reassess the value proposition** from what was learned; repeat until product/market fit is evident.

## 3. Problem interview

Keep problem interviews separate from solution interviews. Do not pitch.

- **Screener** (qualifies the participant against the persona): two to four closed questions about recent, factual behaviour, for example "Have you [done the task] in the last [period]?" and "Did you do it in [the target location/context]?"
- **Interview** (open, behavioural, past tense):
  - "How did you go about [the task] last time?"
  - "What were the hardest parts?"
  - "How did you get around them? What did you compromise on?"
  - "Have you heard of or tried [closest alternative]? What happened?"

## 4. Session discipline: the five common interviewer errors

1. **Talking too much.** Give only the context a real user would have. Frame scenarios as situations ("You need X for work; someone recommended this site; show me what you would do"), never as feature tours.
2. **Closed questions.** Replace "Was that easy?" with "How did that go?" and "Do you like this?" with "What do you think of this?"
3. **Not following up.** Treat feeling words ("cool", "confusing", "intuitive") as prompts: "What made it feel that way?"
4. **Rescuing too early.** Let participants fail; the failure point is the finding. Escalate help gradually (no help, small hint, larger hint, direct answer) and log each level used.
5. **Filling silence.** On a new screen, wait. First impressions need time; comments improve once people settle.

When a participant requests a feature, ask why. The underlying pain often has a simpler solution than the one requested.

## 5. Five-second test

1. Show the page or mockup for five seconds.
2. Ask: What does this product or business do? Who is it for? What would you do next to get it?
3. Run 10–15 participants (remote tool or in person). Cluster the words used.
4. If answers diverge from the intended message, fix hierarchy and copy before buying traffic.
5. Also note tone mismatches: if participants misjudge the audience (for example, reading an adult product as children's), the visual tone is wrong for the market.

## 6. Guerrilla sessions

### Quick task test (about ten minutes per person)

1. Load the prototype or site on the device the audience uses.
2. Give one task with only the information a real visitor would have.
3. Watch silently; do not demonstrate, explain or answer questions during the task. Note the questions asked.
4. Ask how it went afterwards.
5. After four or five people: if all succeed, test another task; if all fail the same way, treat it as a real design defect.

Use it for first-time comprehension and onboarding. It cannot show whether people will like or keep using the product.

### Organised guerrilla research day

1. **Set objectives**: the hypothesis and the concrete questions the day must answer.
2. **Prepare questions**: screener plus open behavioural questions, then prototype tasks.
3. **Choose venues and roles**: a place the target audience already frequents; an event coordinator (greets, manages flow), an interviewer, and an observer from the client team.
4. **Recruit**: targeted posts, adverts or notices where the audience gathers; offer a modest, appropriate incentive.
5. **Screen and schedule**: filter non-matching people; stagger arrivals so one no-show does not waste the slot.

Session script: greet, seat, offer a drink, run a 30–45 minute interview with the prototype, debrief, thank.

## 7. Clickable prototype test

1. Build the prototype in the medium closest to production (HTML/CSS/JS preferred; avoid slide software for anything interactive).
2. Recruit three to five participants matching the persona.
3. Give goal-based tasks ("Buy this item", "Book a consultation").
4. Watch without helping; record where confusion starts.
5. Fix the prototype, then run the next three to five.
6. Repeat until tasks complete without confusion.
7. When comparing versions, rotate the order each participant sees them; people improve on later versions regardless of design.

Always prototype and test before engineering: multi-step signup, checkout or payment, search and browse, sharing, uploads and editing, full navigation, and any flow of more than two steps. Testing is mandatory when mistakes are slow or costly to fix, or when harm could follow.

Skip the prototype when the change is a single step or single CTA, or when the real feature can be built and shipped in about the time a prototype would take and rolled back cheaply.

## 8. Rapid iterative testing (RITE)

- Run three or four rounds of three or four participants.
- Update the prototype between rounds (same day where possible) to fix the most critical issue found.
- Keep the prototype deliberately rough; polished work signals "decided" and suppresses criticism.
- Stop running sessions without iterating: patterns appear after three to five people, and repeating the same round wastes time.

## 9. Unmoderated remote tests

Useful for: checking whether a brand-new user with no background can find and complete a specific task, especially immediately after release (order a few recordings and watch for a shared wrong starting point).

Not useful for: predicting liking, predicting use, understanding daily real-world use, or deciding how to fix a problem.

## 10. Surveys

- Survey only after qualitative work has produced patterns; never survey first.
- Good for confirming at scale whether a pattern seen in a handful of interviews holds, and for specific factual follow-ups.
- Poor for generating hypotheses, understanding motives, or deciding what to build next.
- Include screening questions, ask specific answerable questions, keep it short, and remember that preset options bias answers and "Other" is under-used.

## 11. Research with people who stopped using the product

Call them rather than emailing; people say on the phone what they will not type. Ask:

- What were you expecting when you signed up?
- What did the product actually offer you?
- How was that different from what you expected?
- How much time did you spend with it, and what was your reaction?
- Where did you hear about it?
- Did you talk to anyone else about it? (Reveals who they think it is for.)

Also watch new users through their first 15 minutes: if the experience does not match the promise that brought them, fix either the product or the promise.

## 12. Research integrity rules

- Never substitute AI-generated personas or simulated users for real participants. Generated "findings" can contain fabricated detail that researchers then accept.
- AI tools may assist with transcription, first-pass affinity grouping (with human review), synthesis of large survey sets, translation, and drafting discussion guides that a human reviews.
- Test with under-represented groups deliberately; majority-group sessions miss exclusion and bias.

## Sources

- Levy, J. (2015) *UX Strategy: How to Devise Innovative Digital Products that People Want*. O'Reilly Media.
- Klein, L. (2013) *UX for Lean Startups: Faster, Smarter User Experience Research and Design*. O'Reilly Media.
- Nudelman, G. with Kempka, D. *UX for AI* (year and publisher not recorded in the source notes).
