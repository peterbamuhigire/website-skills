# Experience, Expertise, Authority, and Trust Evidence

Parent skill: [`../SKILL.md`](../SKILL.md)

Use E-E-A-T as a content-quality and evidence lens, not as a schema type,
numeric score, or guaranteed ranking/citation mechanism. Trust is the most
important operational outcome: can a user verify who is responsible, what is
claimed, why it is credible, and what its limits are?

## Evidence model

| Lens | Useful evidence | Common failure |
|---|---|---|
| Experience | first-hand method, original images/data, dated case notes, tested procedures | invented experience or generic claims |
| Expertise | relevant qualifications, role, work history, reviewed technical reasoning | credential stuffing unrelated to the claim |
| Authority | legitimate independent references, standards work, respected partnerships, useful public resources | bought links, manufactured mentions, self-awarded labels |
| Trust | accurate claims, ownership, contact, policies, security, corrections, limitations, current sources | hidden ownership, fake reviews, stale facts, unsupported certainty |

The burden rises with potential harm. Health, finance, legal, safety,
procurement, and public-interest pages require suitable domain review and
primary current sources.

## Page evidence contract

For every material page, record:

- responsible organisation and page owner;
- author and reviewer when authorship affects credibility;
- claim-to-source map;
- first-hand versus sourced evidence;
- jurisdiction, product version, data period, and methodology;
- conflicts, sponsorship, affiliate, or client relationship;
- publication and substantive modification dates;
- limitation, correction, and next-review path.

Do not add a biography, qualification, logo, client, award, association,
testimonial, statistic, or case result without approval and evidence.

## Organisation and contact

- Use the verified legal and trading names consistently.
- Explain what the organisation does, where it operates, and how users can
  contact or escalate to it.
- Publish applicable privacy, terms, security, returns, cancellation, support,
  editorial, and correction information.
- Keep location, hours, prices, availability, and service areas current across
  pages, profiles, feeds, and structured data.
- Do not imply a physical location, certification, regulatory status, or client
  relationship that cannot be proved.

## Authors and reviewers

Use named attribution when it helps the reader evaluate responsibility or
expertise. A useful profile states relevant role, experience, qualifications,
professional links, disclosures, and reviewed topics. Omit irrelevant status
signals.

For high-stakes content, record who reviewed the claim, their relevant basis,
the review date, and when another review is required. A name or `Person` JSON-LD
block is not a substitute for review evidence.

## Original evidence and case studies

A result needs:

- baseline and intervention;
- period and sample;
- definition and method;
- owner of measurement;
- outcome and guardrails;
- limitations and alternative explanations;
- permission to identify the client or use anonymised evidence.

Avoid vague “improved efficiency” claims. Do not generalise one case result to
all clients.

## External corroboration

Earn references through useful work: original research, documentation, tools,
datasets, case studies, professional contributions, partnerships, or expert
commentary. Assess relevance and source quality; citation count alone is not
authority.

Do not buy links, manufacture reviews, plant forum comments, create promotional
Wikipedia content, or misrepresent paid coverage as independent endorsement.

## Structured data

Structured data represents supported visible facts; it does not create
experience, expertise, authority, or trust.

- Use `Organization`, `Person`, `Article`, `Product`, `Service`, review, or
  industry types only where accurate and useful to a named consumer.
- Keep stable entity `@id` values and consistent canonical URLs.
- Omit unknown or unverified credentials, affiliations, ratings, dates, and
  `sameAs` links.
- Validate syntax separately from current Google rich-result eligibility.
- Do not use FAQ or HowTo markup as a Google visibility tactic.

## AI-answer representation

Clear ownership, specific evidence, and stable public facts can make content
more defensible and easier to verify. They do not guarantee retrieval, citation,
or accurate representation by an AI system.

Audit AI answers with repeated prompts and claim-level citation support. Track
incorrect entity merges, outdated product facts, omitted conditions, false
endorsements, and unsafe recommendations. Correct the authoritative source first,
then use each platform's current correction or feedback process where available.

## Acceptance checklist

- [ ] Responsible organisation, author, reviewer, and contact path are truthful.
- [ ] Every material claim has suitable evidence, scope, date, and limitation.
- [ ] First-hand evidence is distinguishable from sourced evidence and inference.
- [ ] Credentials, reviews, clients, partners, awards, and outcomes are approved.
- [ ] High-stakes content has domain-appropriate review and current primary sources.
- [ ] Public entity facts are consistent across owned pages and legitimate profiles.
- [ ] Structured data contains no invisible or invented assertions.
- [ ] Correction, disclosure, and review paths exist.
- [ ] No ranking, citation, or trust-score guarantee is made.

## Currentness

Use [`ai-seo-optimization.md`](ai-seo-optimization.md) and the claim register at
[`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json).
