# Search and AI Discoverability — 2026 Operating Model

Parent skill: [`../SKILL.md`](../SKILL.md)

This reference governs cross-platform search and AI-answer discoverability. Use
[`../../google-ai-search/SKILL.md`](../../google-ai-search/SKILL.md) for Google-specific
generative Search decisions. Verify platform capabilities and crawler policies
against current first-party documentation before implementation.

## Doctrine

SEO, AEO, GEO, AIO, and SXO are not five equivalent ranking systems.

- **SEO** is the technical, content, and authority foundation for discovery,
  crawling, indexing, retrieval, and conventional search presentation.
- **AEO** is a useful label for making answers clear and reusable. It is not a
  separate Google ranking system.
- **GEO** is an emerging, probabilistic practice concerned with retrieval,
  citation, representation, and contribution to generated answers.
- **AIO** is ambiguous. Do not use it in a client artefact without defining it.
  Never promise placement in model-training data.
- **Entity and knowledge presence** is the preferred operational replacement:
  create a consistent, verifiable public record for the organisation, people,
  products, services, locations, and claims.
- **SXO** is the post-discovery experience and conversion layer. It does not
  automatically improve ranking.

The operating model is layered:

1. technical availability and index eligibility;
2. intent-aligned, useful content;
3. answer clarity and evidence;
4. entity consistency and supported structured data;
5. legitimate distribution and corroboration;
6. platform-specific retrieval and citation observation;
7. accessible task completion and conversion;
8. measurement, learning, and substantive maintenance.

## Keep training and retrieval separate

Model training and live retrieval are different systems with different controls.

| Concern | Publisher control | Appropriate outcome |
|---|---|---|
| Potential model training | Platform-specific training crawler policy where offered | A documented allow/block decision; no visibility promise |
| Automatic search retrieval | Search crawler access, indexability, quality, and platform inclusion controls | Eligibility for retrieval or citation; never guaranteed inclusion |
| User-triggered fetching | Accessible pages and interfaces; platform-specific user-agent behaviour | Successful task completion when a user asks an agent to visit |

Do not treat presence in training data as a ranking, visibility KPI, or reliable
route to current brand representation. Prefer controllable, observable retrieval
and public-source quality.

## Cross-platform workflow

### 1. Establish availability

- return the intended HTTP status;
- keep priority information publicly crawlable and indexable;
- align canonical, sitemap, robots, noindex, and snippet controls;
- expose meaningful internal links in rendered HTML;
- make important text available without fragile client-side execution;
- provide transcripts or visible summaries for information locked in media;
- test mobile, accessibility, security, and real-user performance.

Eligibility is not an inclusion guarantee.

### 2. Build an intent architecture

Map each priority user task to the page best able to satisfy it. Separate page
roles where user needs materially differ, but do not manufacture near-duplicate
pages for keyword variants or speculative query fan-out.

Each priority page records:

- audience and job;
- search or discovery intent;
- primary entity and claim set;
- proof burden and source owner;
- internal-link role;
- next useful action;
- measurement event;
- update trigger.

### 3. Make answers useful and extractable

Use the shortest complete answer that preserves conditions and exceptions. Clear
headings, definitions, steps, comparisons, and tables can improve comprehension
and make passages reusable, but there is no universal paragraph length, heading
formula, or machine-chunking rule.

A reusable claim should identify its subject, scope, period, jurisdiction, and
limitations without depending on vague pronouns or surrounding promotional copy.

### 4. Publish evidence worth retrieving

Prefer primary sources, original data, methods, product documentation, versioned
specifications, measurable case studies, and practitioner experience. For a
material result, disclose the measurement owner, period, sample, method, and
limitations. Never invent statistics, reviews, credentials, dates, or experience.

Freshness is query-dependent. Update dates only after a substantive change such
as corrected facts, current procedures, new evidence, changed product behaviour,
or repaired references. Preserve publication and modification history.

### 5. Establish entity and knowledge presence

Keep legal and trading names, descriptions, locations, contacts, products,
services, authors, and policies consistent across owned properties and legitimate
third-party profiles. Use the narrowest accurate Schema.org types and only facts
visible on the page or otherwise supported by project evidence.

Wikipedia is not a controlled company profile. Do not create or edit an article
for promotion, manufacture notability, or conceal a conflict of interest. Route
corrections through the platform's current policies and independent sources.

### 6. Govern crawlers by purpose

Use [`llms-txt-and-ai-crawlers.md`](llms-txt-and-ai-crawlers.md). Record separate
decisions for search inclusion, potential training, and user-triggered access.
Re-check first-party bot documentation and published IP ranges at implementation
time. Do not copy a global allowlist into every project.

### 7. Measure the whole funnel

| Stage | Examples | Interpretation limit |
|---|---|---|
| Crawl and index | response codes, blocked URLs, canonical/index state | Eligibility, not visibility |
| Conventional search | impressions, queries, positions, clicks | Platform-specific observations |
| Generative search | impressions, cited URLs, citation counts, grounding queries | Citation is not ranking, accuracy, or business value |
| Representation | claim fidelity, source support, omitted qualifications | Requires human review |
| Experience | task completion, meaningful engagement, accessibility defects | Define by page job |
| Conversion | qualified enquiries, demos, sign-ups, revenue, assisted outcomes | Respect consent and attribution limits |
| Downstream quality | lead quality, retention, support burden, satisfaction | Needs CRM or operational reconciliation |

For ChatGPT search referrals, monitor the currently documented
`utm_source=chatgpt.com` parameter. For Google and Bing, use the current official
report definitions rather than assumed dimensions.

### 8. Test probabilistic AI visibility responsibly

An AI-visibility observation records:

- platform, surface, model or product label where visible, date, market, locale,
  signed-in state, and device;
- a versioned prompt set with natural paraphrases and control prompts;
- repeated runs rather than one screenshot;
- whether search was invoked;
- cited and linked URLs;
- whether each citation supports the generated claim;
- material omissions, contradictions, and uncertainty;
- referral and conversion evidence where available.

Separate at least these outcomes: discovery, retrieval, citation, prominence,
factual contribution, fidelity, referral, and business outcome. Do not infer one
from another. Current research is useful for hypotheses, not universal ranking
rules; cross-platform causal evidence remains limited.

## Structured data boundary

Structured data can help eligible consumers understand page entities and can
qualify pages for supported rich results. It is not special AI markup and does
not guarantee a rich result, citation, or ranking.

- Google deprecated HowTo rich results in 2023.
- Google stopped showing FAQ rich results from 7 May 2026.
- FAQ content may still help users; `FAQPage` markup requires a documented
  non-Google consumer and visible matching content.
- Validate Schema.org syntax separately from eligibility for a current Google
  search feature.

## Priority order

1. Resolve crawling, indexing, canonical, rendering, and security failures.
2. Build clear product, service, category, documentation, and comparison pages.
3. Add original local or sector expertise and auditable proof.
4. Establish entity consistency and accurate structured data.
5. Permit only the search crawlers the owner intends to support.
6. Improve answer clarity without degrading human writing.
7. Earn legitimate independent corroboration.
8. Improve the post-arrival task and conversion experience.
9. Observe AI citations and representation with a repeatable protocol.
10. Reallocate effort only when visibility connects to a useful outcome.

## Reject these tactics

- mass-produced AI articles or fan-out page factories;
- arbitrary word counts, question-heading quotas, or artificial chunking;
- schema properties absent from visible, verified facts;
- indiscriminate FAQ or HowTo markup;
- date changes without substantive revision;
- `llms.txt` sold as a Google or universal AI-ranking lever;
- training-data placement services presented as controllable visibility work;
- manufactured Wikipedia, forum, review, or social mentions;
- one-run chatbot mention counts presented as ranking evidence;
- guarantees of indexing, ranking, citation, recommendation, or conversion.

## Current evidence boundary

The claim-level currentness record for this doctrine is
[`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json).
Re-verify time-sensitive platform claims by 2026-12-05 or sooner when a provider
changes its crawler, reporting, structured-data, or inclusion controls.
