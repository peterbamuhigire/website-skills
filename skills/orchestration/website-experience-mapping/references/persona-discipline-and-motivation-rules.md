# Persona Discipline and Motivation Rules

Parent skill: [website-experience-mapping](../SKILL.md). Read when you write or review personas and the stories built on them, settle arguments about edge cases, check the team for bias before research, or decide whether a site should aim for engagement at all.

Persona validation through interviews is in `validation-research-method-playbook.md`. Persona fields for the discovery meeting are in `orchestration/premium-ui-ux-design/references/ux-discovery-and-wireframe-procedure.md`.

---

## 1. Personas carry stories

A persona and a scenario are only a skeleton. The story is what makes the person real enough to design for. A design story is a person in a situation with a problem and a resolution.

Procedure for writing a persona story:
1. Start from a frustrating situation the persona actually meets. This locates the pain.
2. Add context: place, time, what they are holding, who is with them, what is at stake.
3. Write how the situation plays out today, with the current site or the competitor.
4. Rewrite the ending as it would go with the new site. The difference between the two endings is the design opportunity.
5. Apply the realism check below before using the story.

**Realism check.** Did everything go too smoothly? Is the persona unusually patient, well informed or well equipped? If so, stop, take a short break and rewrite. Teams easily write stories about the visitors they wish they had rather than the ones they have.

---

## 2. Designing for one real person, not "somebody"

### Edge cases
Do not try to serve every edge case. A site that delights its primary visitors earns loyalty and recommendations; a site stretched to cover every rare case satisfies nobody well.

Use the persona to settle edge-case arguments. The pattern:
- "What if a visitor wants to do X?"
- "[Persona name] does not need to do X."
- "But somebody might."
- "Perhaps, but we are designing for [persona name], not for somebody."

Record rejected edge cases, and revisit them only when evidence shows they are common or high-stakes (legal, safety, accessibility requirements are never dismissed this way).

### Choosing the primary persona
Where one role has several candidate personas:
- Choose the primary persona whose design would at least work for the others.
- Check the reverse: a design built for any other candidate may not work for the primary.
- Never average personas into a composite. A design for a blend of everyone fits nobody.

### Stopping designers from designing for themselves
Designers slip into imagining themselves in the persona's place. A specific, richly described persona (name, photograph, biography, habits, frustrations) makes that substitution hard. Vague personas invite it.

---

## 3. Persona mechanics

Each persona has:
- a fictional first and last name (protect real participants);
- a photograph (a consenting volunteer or properly licensed image; never a real participant without consent);
- a short biography: role, goals, main tasks, typical use stories, problems, concerns and biggest obstacles.

**Keep personas in sight.** A persona that lives only in a slide deck is forgotten. Put personas where the whole team and the client meet them: printed posters in the workspace, cards on the table in reviews, the persona's name in ticket titles and review agendas. The aim is that everyone, not only designers, knows who the site is for.

**Profiling tools to avoid.** Do not build personas on personality-type systems without scientific support (for example Myers-Briggs types). The Big Five personality model is the best-supported, but personality does not reliably predict specific behaviour; base personas on observed goals and behaviour.

---

## 4. Team bias check before research and review

Run this check at the start of discovery and before each design review.

| Bias | How it shows up | Countermeasure |
|---|---|---|
| Egocentric bias | "I find it obvious, so visitors will" | Test with people outside the team |
| Curse of knowledge | The team cannot see the site as a newcomer does | Recruit participants who have never seen the site |
| Confirmation bias | Researchers who built the design run gentle tests and hear what they hoped | Use a facilitator who did not design it; pre-write tasks and success criteria |
| IKEA effect | Features the team built feel too valuable to cut | Decide what stays using usage and completion evidence |
| Sunk cost | Continuing to polish a failing design because of time already spent | Set a kill criterion before work starts; rebuild when evidence says so |
| Hindsight bias | "We knew it all along" after launch | Write predictions down before testing and compare afterwards |

Also: a team drawn from one background, tested only on people like itself, builds exclusion into the site. Recruit participants across age, ability, language and device.

Treat analytics as a record of what happened, never of why. Pair numbers with observation before drawing conclusions.

---

## 5. Motivation: what brings visitors back

### Four sources of motivation
1. **Implicit drives** such as hunger, tiredness or discomfort; largely outside conscious control, but they shape context (a hungry visitor ordering food has little patience).
2. **Personality**, which varies but predicts specific behaviour poorly.
3. **Extrinsic motivation**: rewards and penalties from outside the activity.
4. **Intrinsic motivation**: doing something because it is satisfying in itself.

Do not base design decisions on Maslow's hierarchy of needs as a strict ladder; modern research does not support it as a reliable predictive model. Use the needs below instead.

### Three needs behind intrinsic motivation
| Need | Visitor feels | Website application |
|---|---|---|
| Competence | Capable and progressing | Early wins, clear feedback, visible progress, no dead ends that make visitors feel foolish |
| Autonomy | In control, with meaningful choices | Real choices of path or option that affect the outcome; no trivial or fake choices; no forced sequences where freedom is possible |
| Relatedness | Connected to other people | Community, reviews, sharing and co-operation features where the audience values them |

### Extrinsic rewards
- Use honest success states (clear confirmation, a warm thank-you) and progress indicators to reward completion.
- Points, badges and streaks help only when the underlying activity is worth doing. Added on their own they motivate briefly and can undermine interest: paying people for something they already enjoyed can reduce their own interest in it.
- Never punish disengagement (expiring points, resetting streaks) or use unpredictable reward schedules to drive compulsive checking. Treat them as dark patterns and apply `ux-conversion/cro-audit/references/ethical-persuasion-gate.md` and the design engine's `00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns/references/dark-pattern-catalog.md`.

### Does this site need engagement?
Decide explicitly, per site and per section:
- **Entertainment, learning and community sites:** engagement is a goal. Design for motivation, emotional pleasure and a well-judged challenge (see flow below).
- **Task sites (booking, paying, finding a phone number, service portals):** visitors do not want to be engaged; they want to finish quickly. Measure success by speed and completion, not time on site.
- **Social features:** visitors engage with other people, not with the platform. Design to support the human connection.

### Flow, where engagement is the goal
Flow occurs when:
1. the challenge is slightly beyond current skill but not overwhelming;
2. the goal is always clear;
3. feedback on each action is immediate;
4. concentration is not interrupted.

Too easy produces boredom; too hard produces anxiety. Break flow and you lose the visitor to "How do I do this?" thinking.

Flow breakers to remove: forced tutorials that interrupt exploration, loading pauses mid-task, confusing controls, irrelevant prompts, and errors with no clear way forward.

Prefer designing the core activity to be satisfying (clear progression, meaningful choices, shared experience) over bolting game mechanics onto an unsatisfying one.

---

## 6. Checklist

- [ ] Each persona has a story that starts from real frustration and passes the realism check.
- [ ] One primary persona per role; no averaged composites.
- [ ] Rejected edge cases recorded; mandatory legal, safety and accessibility cases retained.
- [ ] Persona mechanics complete; personas visible to the whole team and the client.
- [ ] No unsupported personality typologies in persona profiles.
- [ ] Team bias check run; testing done by or with people outside the design team.
- [ ] Engagement goal decided per section; task sections measured by speed and completion.
- [ ] Motivation features support competence, autonomy or relatedness; no punishing or compulsive mechanics.

## Sources

- Branson, S. (2020) *UX / UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*. Chapter on personas, drawing on Alan Cooper.
- Hodent, C. (2022) *What UX Is Really About: Introducing a Mindset for Great Experiences*. CRC Press. Sections on cognitive biases, motivation, self-determination theory (Ryan and Deci) and flow (Csikszentmihalyi).
