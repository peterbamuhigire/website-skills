# Form Question Wording and Data Design

Parent skill: [page-builder](../SKILL.md). Read when writing the questions, labels, help text, answer options, titles, headings, button labels or error text of any website form (contact, enquiry, booking, quote, sign-up, application, checkout), or when deciding which questions a form should ask at all.

Companion file: `form-layout-flow-and-validation-rules.md` covers field types, layout, flow, validation display and the multi-step checklist.

---

## 1. Operating model

Every form has three dimensions. Work on them in this order of influence:

1. **Words** — what the form says and how it says it. Users can work around poor layout; they cannot work around poor wording.
2. **Layout** — how questions, fields and actions are presented.
3. **Flow** — the order and path through the form.

Guiding rule: start from an empty screen and add only what communicates something the user needs. For every element a stakeholder asks to add, ask "Will this help the user, and how?" If it serves only the organisation or repeats something already said, leave it out.

Treat the form as a conversation between two parties. Write each question the way a courteous, competent staff member would ask it face to face.

---

## 2. Decide which questions to ask

Procedure:

1. **Begin with the end.** Imagine the completed submission. List who uses each answer and for what decision.
2. **Strike any question without a named data user.** Every extra question lowers completion, lowers data quality and raises error rates.
3. **Strike any question users cannot answer accurately.** Poor-quality data is worse than none because it steers decisions wrongly. Example of a weak question: "How did you hear about us?" — recall is poor and most people pick any option.
4. **Test perceived length, not field count.** There is no correct length. What matters is whether the form feels proportionate to the user's goal in that context. Splitting one hard question into two easy ones can make a form feel shorter.
5. **Check the claim before quoting any conversion uplift** from removing fields; published case figures vary widely and date quickly.

---

## 3. Question-answering model: four stages

Users pass through four mental stages for every question. Check the label, the question-level help and the answer field against each stage.

| Stage | What the user does | Design check |
|---|---|---|
| Comprehension | Understands the words | Plain, audience-appropriate vocabulary; one concept; no ambiguity |
| Retrieval | Finds the answer in memory or a source | Is the answer knowable? Is a document or another person needed? |
| Judgement | Decides whether and how to answer | Is the question appropriate in this context? Is the scope precise? |
| Answering | Physically enters the answer | Do the field type and options fit the answer? |

### 3.1 Comprehension rules

- Use short, familiar words and short sentences with one idea each. Prefer the active voice.
- Match vocabulary to the audience: lay terms for the public, technical terms only for specialists who use them daily.
- Remove ambiguity with a frame of reference. "Where do you work?" can mean employer, place or role; "In which town or city do you work most often?" cannot.
- Ask about one concept per question. Never combine two questions in one label.

### 3.2 Retrieval rules

- If the answer lives in a document (bill, ID, policy number) or with another person, warn users **before** the form starts, say exactly what they need and where to find it, and offer save-and-return where the form is long.
- Memory is most reliable for conscious, emotional, essential, first-and-last, recent and strongly associated events. Do not ask for precise detail about routine, forgettable events.

### 3.3 Satisficing defences

People stop reading as soon as they think they have enough to answer. Design for this:

1. **Put the frame of reference first.** Write "Since your last invoice, has your address changed?" rather than "Has your address changed since your last invoice?"
2. **Put critical information in the label, not the help text.** Help is skipped even more than labels. Write "Including weekends, how many days did you work last month?"
3. **Turn important instructions into questions.** Replace "Leave blank if same as above" with "Is your postal address different from your home address? Yes / No".
4. **Keep the burden low.** Fatigue guarantees skimming and abandonment.

### 3.4 Judgement rules

- Context changes what feels acceptable. A date of birth is expected on a government form and resented on a guest checkout.
- When a sensitive question is necessary, add question-level help that says **why** it is needed and how it will be used.
- Replace vague frequency words ("regularly", "rarely") with measurable units (days per week, hours per day).
- Be explicit about time frames, units, currency, edge cases and definitions.
- Remember that answer options tell users how you interpret the question; the same label with different options is a different question.

### 3.5 Answering: open or closed

Make a question closed (choose from options) only when you know the full valid set of answers and can maintain it. Otherwise keep it open.

Six tests for closed answer sets:

1. **Appropriate** — covers the main answers, from a reputable source, at the right level of detail, reviewed periodically.
2. **Complete** — every user has an option; add "Other (please specify)", "Don't know", "None of these" or "Not applicable" as needed; open-ended scale ends ("More than 12 months ago").
3. **Mutually exclusive** — no overlaps (e.g. age bands 18–24, 25–34, not 18–25, 25–35).
4. **Self-explanatory** — every option understood without effort.
5. **Sensibly ordered** — natural or logical order first. Use alphabetical order only when each option has one well-known name and no better order exists (a list of regions is fine; an agreement scale is not).
6. **Unbiased** — options do not lean in one direction.

---

## 4. Defaults for common questions

| Question | Default treatment |
|---|---|
| Title / honorific | Avoid. If needed, ask "How would you like us to address you?" as optional free text. Never infer sex, gender or marital status from it. |
| Name | One text field with a precise label (e.g. "Full name, as shown on your ID"). If it must be split, use "Given name(s)" and "Family name". Accept apostrophes, hyphens, spaces, diacritics and non-Latin scripts. |
| Address | Always state which address (home, postal, billing, delivery). Prefer one field with address look-up where reliable local data exists; otherwise research the local address structure before designing fields. Accept apostrophes and hyphens. |
| Email | Label "Email address". One field, `type="email"`, generous length. Validate only for text before and after "@". Make optional where some users lack email; explain why it is collected. |
| Phone | State which number (mobile, work, daytime). One field, `type="tel"`. Accept spaces, hyphens, brackets, full stops and a leading "+". |
| Date of birth | Avoid; ask an age range or "Are you 18 or over?" instead. If required, use three short text fields (day, month, year) with the format hint above; a picker may be offered but never as the only method; never three dropdowns. |
| Sex / gender | Ask only when genuinely needed and lawful. Sex: radio options including "Prefer not to say". Gender: optional free text. |
| Card payment | Detect card type from the number; never ask users to choose it. One field for the number. Ask only number, name on card, expiry and security code. Show accepted payment methods early (header or footer, at decision points and at payment). |

---

## 5. Other words on the form

### 5.1 Form title
- Every form has a visible title on every screen.
- Keep it to about five words, unique within the organisation, descriptive.
- Drop filler words such as "form", "online", "web", "the", "a", "for". Pattern: `<Object> <Action or Product>` — "Home Loan Application", "Event Booking".

### 5.2 Section and step headings
- Start without section headings; add them only if they help. They can make a form look longer.
- Users decide whether a section applies to them from its heading, so headings must be accurate.
- Never phrase a heading as a question; headings are often skipped.
- Multi-step forms always carry a step heading: brief, unique, descriptive, without "information" or "details". Step numbers are optional and best avoided when there are many steps.

### 5.3 Button labels
- Use an action word that names the outcome: "Send message", "Get quote", "Book table", "Pay now", "Create account", "Continue".
- Avoid "Submit"; it names the mechanism, not the result.
- Use the right word at the right time: "Done" or "Finish" only on the final step.

### 5.4 Error messages
Each message, in a polite and non-accusatory tone, must:
1. say that something needs attention,
2. say exactly what and where, and
3. say how to fix it or move past it.

Pattern: `<What is wrong, specifically>. <What to do>.` — "Your email address is missing an '@'. Add it and try again." Prefer "Please answer this question" to "Required field". Never blame the user.

### 5.5 General instructions
- Most users do not read instructions. Design so the form can be completed without them.
- Start with none. Convert any critical instruction into a question (see 3.3).
- Keep any remaining section-level instruction short and never a barrier to starting.

### 5.6 Pronouns
- Start without "your" and "my"; they add reading load quickly.
- Use "My ..." for signed-in areas the user owns (My bookings).
- Use "Your ..." when the organisation addresses the user. Where a third party is involved, use "your" for the user and a descriptive noun for the other party ("the applicant's employer").

---

## 6. Question-by-question (QxQ) specification

For any non-trivial form, keep a QxQ document so content can change independently of code and decisions survive staff turnover. One row per question:

| Field | Record |
|---|---|
| Label | Final wording |
| Question-level help | Wording and placement |
| Answer field | Type and width |
| Required / optional | And why |
| Open / closed | If closed: options, order, source standard, single or multiple, "Other" write-in |
| Open-field constraints | Min/max length, accepted characters, HTML input `type` and `autocomplete` token |
| Validation | Ranges, date limits, format tolerance |
| Conditional logic | Trigger question and rule; which users see it |
| Eligibility determinant | Yes / No |
| Data use | Who uses the answer and for what |
| Research notes | Evidence behind the wording |
| Change history | Date, change, reason |

Benefits to state to clients: it answers developers' questions before build, preserves organisational knowledge, and gives an audit trail for question changes.

---

## 7. Wording review checklist

- [ ] Every question has a named data user.
- [ ] Every label covers one concept, in audience vocabulary.
- [ ] Frames of reference sit at the start of labels.
- [ ] Critical conditions are in labels, not only in help.
- [ ] Instructions users must act on are questions.
- [ ] Sensitive questions explain why.
- [ ] Closed sets pass all six tests.
- [ ] Common questions follow the defaults table, localised for the market.
- [ ] Title, step headings and buttons follow section 5.
- [ ] Every error message names the problem and the fix.
- [ ] QxQ exists for any form with more than a handful of questions.

---

## Sources

- Jessica Enders (2016) *Designing UX: Forms — Create Forms That Don't Drive Your Users Crazy*, SitePoint. Includes her use of Tourangeau's four-stage survey response model, Herbert Simon's concept of satisficing, and Caroline Jarrett and Gerry Gaffney's view of forms as conversations.
