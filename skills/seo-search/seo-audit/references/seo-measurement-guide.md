# Search and AI Discoverability Measurement Guide

Parent skill: [`../SKILL.md`](../SKILL.md)

Measure the chain from technical eligibility to business or public-service
outcome. Never use universal traffic-growth, CTR, bounce, conversion, ranking,
review-count, or payback benchmarks as portable acceptance criteria.

## Measurement hierarchy

| Stage | Core question | Evidence examples | Do not infer |
|---|---|---|---|
| Availability | Can systems and users reach the intended page? | statuses, robots, render, internal links, sitemap | Indexing or quality |
| Index state | Is the intended canonical eligible and selected? | webmaster reports, URL inspection, canonical sample | Ranking or demand |
| Conventional visibility | Where and when is the site shown? | impressions, queries, pages, country, device, position | Causality or conversion |
| Generative visibility | Is the page shown or cited in AI features? | Google generative impressions, Bing citations, cited URLs | Rank, fidelity, or value |
| Representation | Is the answer supported and accurate? | claim-citation review, omissions, contradiction log | Referral or persuasion |
| Referral | Did a person arrive from the surface? | consent-aware source/medium and landing page | Full exposure or causality |
| Experience | Did the visitor complete the page's task? | task success, errors, form completion, accessibility | Revenue without reconciliation |
| Outcome | Did the visit contribute to a useful result? | qualified leads, sales, retention, satisfaction, service completion | Sole-channel credit |

## Metric contract

Every KPI or diagnostic records:

- definition and formula;
- grain and segmentation;
- source and property;
- owner and decision it informs;
- collection and processing latency;
- comparison period and seasonality treatment;
- consent, identity, retention, and access controls;
- known aggregation, sampling, privacy, and attribution limitations;
- baseline, decision band, and review trigger;
- quality status and reconciliation evidence.

## Google Search Console

Analyse normal Web search by page, query class, country, device, and comparable
period. Position and CTR are diagnostics, not stable universal targets; result
features, brand demand, intent, device, and query mix change their meaning.

As of 31 August 2026, the dedicated generative AI report covers AI Overviews and
AI Mode impressions by page, country, device, and date. It does not expose a
universal rank, prompt list, citation fidelity, or downstream outcome. Record the
separate property include/exclude control and inheritance state.

## Bing Webmaster Tools

Bing AI Performance is a public-preview report. Use its currently documented
measures: total citations, average cited pages, sampled grounding queries,
page-level citation activity, and trends. Microsoft states these do not indicate
rank, authority, placement, or a page's role in an answer.

## Assistant observation protocol

For ChatGPT, Perplexity, Claude, Gemini, Copilot, or another assistant:

1. freeze a representative prompt set and natural paraphrases;
2. record platform, surface, visible product/model label, market, locale,
   signed-in state, device, and date;
3. use repeated runs and controls;
4. record whether search occurred and every cited/linked URL;
5. verify whether each citation supports the answer at claim level;
6. log material omissions, contradictions, hallucinations, and uncertainty;
7. match referrals and qualified outcomes where consent and data permit;
8. report distributions and instability rather than one screenshot.

Separate discovery, retrieval, citation, prominence, factual contribution,
fidelity, referral, and outcome. A change in one is not proof of a change in the
others.

## Diagnostic comparisons

Use the site's own history, matched route/query cohorts, pre-declared experiment,
or a justified external benchmark with source, definition, market, and date.
When a metric changes, test competing explanations:

- demand or seasonality;
- campaign and brand activity;
- tracking, consent, attribution, or report changes;
- crawl, render, canonical, index, or migration defects;
- content, internal-link, offer, or conversion changes;
- platform update or feature availability;
- competitor and result-layout change.

Do not label a decline a penalty without evidence.

## Alerts

Alert thresholds come from business impact and observed variance. Immediate
investigation is appropriate for release-linked widespread 4xx/5xx, accidental
noindex/robots blocks, broken canonicals, failed conversions, security incidents,
or analytics loss. Visibility movement without technical breakage normally needs
comparable data and a recorded hypothesis before remediation.

## Reporting shape

1. Answer the named decision first.
2. State evidence period, coverage, quality, and missing sources.
3. Show the funnel stages separately.
4. Explain material changes with confidence and competing hypotheses.
5. Name owned actions, guardrails, rollback, and re-measurement date.
6. Preserve `NOT_ASSESSED` where account, prompt, render, CRM, or production
   evidence is unavailable.

## Currentness

Use the claim register at
[`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json).
