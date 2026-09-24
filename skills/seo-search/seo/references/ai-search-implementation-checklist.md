# AI-Search Implementation Checklist

Parent skill: [seo](../SKILL.md). Read when implementing pages, entity consistency, cross-channel content, or a citation-observation programme for AI-assisted search, and you need rules that stay within current platform guidance.

Vendor citation studies can suggest hypotheses. They are sample-bound and observational; they do not establish ranking rules, causation, traffic, lead quality, or sales impact. Current Google Search implementation remains governed by the engine's official Google source register.

## Currentness checks

Run these checks before advising; record source and access date:

- Check Google's current AI optimisation guide (the version reviewed here was dated 10 July 2026). It states that `llms.txt` or other AI text files, special schema, artificial chunking, and writing specially for AI are unnecessary for Google Search. Do not present any of them as a Google requirement.
- Check current rich-result eligibility before adding structured data. Google stopped showing FAQ rich results on 7 May 2026.
- Check each AI product's own documentation separately; do not assume shared retrieval sources between providers.

## 1. Page-level checklist

For each important page, confirm:

- [ ] The page is independently useful: it states its subject, audience, answer, evidence, date where material, limitations, and next action.
- [ ] Facts are in crawlable HTML, not only in images, scripts, or downloads.
- [ ] Structured data, where used, matches visible, accurate content and the consumer's current eligibility rules.
- [ ] Headings and lists are used because they help readers, not because a format is assumed to earn citations.
- [ ] The page has a named owner and a review date.

## 2. Topic coverage checklist

- [ ] The topic is covered by connected pages with distinct roles: definition, how-to guide, comparison, implementation detail, frequently asked questions (as visible content), case evidence, and offer page.
- [ ] Each page links to the pages a reader needs next.
- [ ] No two pages compete for the same role; see [entity-and-page-role-contract.md](entity-and-page-role-contract.md).

## 3. Entity consistency checklist

Check the organisation, people, services, products, and places for identical naming and facts across:

- [ ] page copy;
- [ ] titles and meta descriptions;
- [ ] structured data;
- [ ] author and team information;
- [ ] internal links and anchor text;
- [ ] legitimate external references (profiles, directories, partner pages).

## 4. Owned hub and social distribution

- [ ] The owned website is the durable explanation and conversion hub.
- [ ] Social posts (including individual professional profiles) work as standalone answers and distribution paths, and point back to the canonical page where appropriate.
- [ ] Social content never replaces the canonical destination.
- [ ] Author identity is consistent between the website and the author's professional profiles.
- [ ] Hypothesis to test, not a rule: one sample-bound 2026 vendor study of B2B prompts reported that individual professional profiles contributed more citations than company pages, and that structured, question-led posts appeared often among highly cited examples. Test this with the section 7 contract before shifting effort between personal and company channels.

## 5. Independent corroboration

- [ ] Corroboration is earned legitimately: partners, professional directories, reviews, original research, community participation.
- [ ] No fake mentions, reviews, or user-generated content are created or commissioned.
- [ ] Review and endorsement practices are checked against the current platform and consumer-protection rules for the market.

## 6. Refresh rules

- [ ] Refresh when facts, offers, laws, prices, capabilities, or evidence change.
- [ ] Record the substantive change and its date.
- [ ] Never change a date cosmetically.

## 7. Measurement and experiment contract

Track these as separate outcomes: representation, retrieval or citation observation, referral, qualified engagement, and conversion.

For a monthly or quarterly observation cycle, record per prompt:

| Field | Entry |
|---|---|
| `prompt` | exact wording |
| `product` | answer product and model or mode where shown |
| `date` | observation date |
| `locale` | market and language |
| `answer` | saved answer text or capture |
| `target_url` | the page expected to be used |
| `cited_urls` | all URLs cited |
| `brand_accuracy` | accurate / inaccurate / absent, with notes |
| `referral_activity` | analytics evidence for the period |
| `business_outcome` | qualified outcomes where attribution is available |

Rules:

- Hold topic and audience reasonably constant when comparing author, structure, format, or distribution.
- One anecdotal citation is not grounds for a strategy change.
- When quoting any study figure, keep its sample, denominator, date, and source beside it.
- Do not claim that one platform always outranks others, that follower count is irrelevant, or that headings, lists, posting frequency, freshness, or format guarantee citation.

## 8. Evidence register entry for vendor studies

When a vendor or platform study informs a hypothesis, record:

| Field | Entry |
|---|---|
| `publisher` | organisation and document title |
| `date` | publication date |
| `method` | observational, experimental, survey; sample size and scope |
| `bias_risk` | commercial interest, sample limits |
| `use` | hypothesis only / corroborated / rejected |
| `verified` | date checked |

## Sources

- Meltwater (2026) *How LinkedIn Content Wins in AI Search* (report) and supporting article (12 May 2026). Vendor research; hypothesis input only.
- LinkedIn Marketing Blog (21 May 2026) "New research: AI Search and LinkedIn: 5 Takeaways from 9.5 Million Citations". Supporting summary.
- Google Search Central, AI optimisation guide (version reviewed 10 July 2026) — check the current version.
