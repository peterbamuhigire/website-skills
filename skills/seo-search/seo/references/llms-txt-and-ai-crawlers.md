# `llms.txt`, AI Crawlers, and Publisher Controls

Parent skill: [`../SKILL.md`](../SKILL.md)

This reference separates optional plain-text knowledge artefacts from crawler
controls. Re-verify every named bot and control against the provider's current
first-party documentation before implementation.

## Governing rule

Do not use one undifferentiated “AI crawler” switch. Record three decisions:

1. Should automatic search products be able to discover and cite the site?
2. May providers crawl the site for potential model training?
3. Should user-triggered agents be able to fetch and operate the site?

These decisions have different user agents, consequences, and owners. A search
allow does not require a training allow.

## `llms.txt` and `llms-full.txt`

These are optional, non-standardised-in-practice handover artefacts. Generate
them only when a named consumer, documentation workflow, internal knowledge
pipeline, or client contract benefits from a maintained text index.

Google states that `llms.txt`, AI text files, Markdown mirrors, and special
machine-readable files are not used for visibility or ranking in Google Search,
including generative AI features. Do not sell these files as Google SEO, AEO, or
GEO levers. Do not claim that other platforms use them without current
first-party evidence.

If a project chooses to publish them:

- generate from the same verified content source as the HTML site;
- include only canonical public URLs and facts visible on the site;
- include a generated-at time, content version, and owner;
- omit private, gated, personal, draft, or unverified information;
- regenerate or remove the files when source content changes;
- test links, encoding, and conflict with canonical HTML;
- measure actual requests before investing further.

Minimal optional shape:

```markdown
# {Site or product name}

> {Accurate one-sentence description, audience, and relevant market.}

Generated: {ISO date and time}
Canonical site: {absolute URL}

## Products and services

- {Verified name}: {absolute canonical URL} — {visible factual summary}

## Documentation

- {Document title}: {absolute canonical URL} — {scope and version}

## Company and policies

- About: {absolute canonical URL}
- Contact: {absolute canonical URL}
- Privacy: {absolute canonical URL}
```

There is no mandatory file size, FAQ count, “most-cited line”, or citation
benefit. Treat all such claims as unsupported unless a named consumer publishes
testable guidance.

## OpenAI controls verified on 2026-09-05

OpenAI documents independent controls:

| User agent | Purpose | Operational rule |
|---|---|---|
| `OAI-SearchBot` | Automatic discovery for ChatGPT search features | Allow when ChatGPT search inclusion is intended; also permit current published IP ranges at infrastructure layers |
| `GPTBot` | Crawling content that may be used for foundation-model training | Decide separately under the owner's data-use policy |
| `ChatGPT-User` | User-triggered page visits and actions | Do not treat as the search-inclusion control; current documentation says robots rules may not apply to these user-initiated requests |

OpenAI says a site may allow `OAI-SearchBot` while disallowing `GPTBot`.
ChatGPT search referral URLs currently include `utm_source=chatgpt.com`; measure
that parameter without assuming every ChatGPT-originated visit will contain it.

Example: search allowed, potential training disallowed.

```text
User-agent: OAI-SearchBot
Allow: /

User-agent: GPTBot
Disallow: /

User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

This is an example, not a global default. Confirm CDN, WAF, hosting, and IP rules
do not contradict `robots.txt`.

## Google controls verified on 2026-09-05

Google Search generative-feature inclusion is controlled in Search Console as
of 31 August 2026. It is separate from `Google-Extended`, which controls certain
non-Search generative AI training and grounding uses.

- Keep Googlebot crawl, index, canonical, and snippet signals coherent for
  ordinary and generative Search eligibility.
- Record the Search Console generative-AI include/exclude decision and property
  inheritance.
- Record the `Google-Extended` decision separately.
- Use `noindex` when the page must not appear in Google Search at all.
- Do not infer Google Search inclusion from a `Google-Extended` setting.

## Other providers

Do not ship remembered user-agent lists. For Anthropic, Perplexity, Apple,
Common Crawl, Amazon, Cohere, and other providers, verify at implementation time:

- exact current user-agent names and published IP ranges;
- whether the bot is for search, training, user-triggered access, or another use;
- whether `robots.txt` is honoured for that use;
- propagation delay and caching behaviour;
- effect of blocking on links, snippets, citations, and user-triggered access;
- provider documentation date and next review date.

If first-party documentation is absent or ambiguous, mark the effect
`NOT_ASSESSED` and let the owner choose the narrowest policy consistent with
legal, privacy, commercial, and infrastructure requirements.

## Decision record

Every project records one row per provider and purpose:

| Field | Required value |
|---|---|
| Provider and user agent | Exact current name |
| Purpose | Search, potential training, user-triggered fetch, or other |
| Decision | Allow, block, rate-limit, or `NOT_ASSESSED` |
| Scope | Site, path, file type, environment |
| Owner and approval date | Named decision owner and ISO date |
| First-party source | URL, publication/update date, access date |
| Expected consequence | Qualified; no invented guarantee |
| Infrastructure alignment | robots, CDN, WAF, host, authentication |
| Measurement | server logs, referrals, platform report, error evidence |
| Review trigger | Date or provider change |

## AI-ready page implementation

The HTML page remains the source of truth.

- Lead with a clear answer when that serves the visitor; use no fixed word count.
- Use descriptive headings that match the reading path; questions are optional.
- Present genuine comparisons, definitions, procedures, and evidence in semantic
  HTML when they improve the task.
- Keep important content crawlable and understandable outside images or scripts.
- Use structured data only when it matches visible, verified facts.
- Preserve authorship, source, publication, substantive revision, version,
  jurisdiction, and limitation information where relevant.
- Design forms and controls accessibly so user-triggered agents and assistive
  technology can identify labels, roles, states, errors, and completion.

## Verification checklist

- [ ] Search, potential-training, and user-triggered purposes are separate.
- [ ] Every named provider was checked against current first-party documentation.
- [ ] Owner approval and review date exist for each allow/block decision.
- [ ] `robots.txt`, meta directives, Search Console controls, CDN, WAF, and host
      policies are coherent.
- [ ] Search inclusion is not promised from crawler permission alone.
- [ ] Optional text artefacts have a named consumer and regeneration owner.
- [ ] No arbitrary length, FAQ-count, citation, ranking, or freshness claim ships.
- [ ] Server-log and referral measurement respects consent and retention policy.
- [ ] Unavailable provider evidence is `NOT_ASSESSED`, not guessed.

## Current sources

- Google generative AI optimisation guide:
  https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google Search generative AI control:
  https://support.google.com/webmasters/answer/16908024
- OpenAI crawler documentation:
  https://developers.openai.com/api/docs/bots
- OpenAI publisher FAQ:
  https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- Claim-level evidence record:
  [`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json)
