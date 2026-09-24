# AI-Search Response-Mode Planning

Parent skill: [google-ai-search](../SKILL.md). Read when planning pages, entity facts, measurement, or experiments for visibility in AI-assisted search and answer products, and you need a planning lens that does not invent platform rules.

This is a planning method, not a platform manual. Current platform behaviour is admitted only from dated primary sources recorded in the engine's source register. Where a fact about a platform is needed, phrase it as a check to run, not as a rule.

## Currentness checks (run before advising)

Confirm against current primary documentation before stating any of these; record the source and access date:

- Check Google's current AI optimisation guide (the version reviewed in this engine was dated 10 July 2026). That guide states that `llms.txt` or other AI text files, special schema, artificial chunking, and writing specially for AI are unnecessary for Google Search. Do not recommend them as Google requirements.
- Check Google's current rich-result documentation before proposing FAQ markup. Google stopped showing FAQ rich results on 7 May 2026; do not promise an FAQ rich result.
- Check the current Bing Webmaster Tools documentation for its AI Performance report; treat it as a measurement surface, not a ranking or authority score.
- Check OpenAI's current crawler documentation. Keep search inclusion (`OAI-SearchBot`), potential model training (`GPTBot`), and user-triggered access (`ChatGPT-User`) as separate decisions. See [llms-txt-and-ai-crawlers.md](../../seo/references/llms-txt-and-ai-crawlers.md).
- Check each product separately. Do not infer that one answer product retrieves from another provider's index.

## 1. Plan for response modes, not model brands

Answer products respond to a query in broadly different ways. Use three modes as a planning lens only; products route queries differently and change without notice.

| Response mode | What the answer draws on | Website work that serves it |
|---|---|---|
| Remembered knowledge | what a model already holds about an entity or topic | consistent, long-standing identity and offer facts across the site and legitimate third-party profiles |
| Retrieved, current information | pages fetched or indexed at answer time | crawlable canonical pages, truthful dates, time-stamped updates when facts change |
| Deeper reasoning or comparison | several sources weighed for a complex decision | expert guides that show working, evidence, limitations, and first-hand experience |

Assign each important page a primary mode and record it in the page's role record (see [entity-and-page-role-contract.md](../../seo/references/entity-and-page-role-contract.md)).

## 2. Make the entity unambiguous

This is a writing and information-architecture heuristic. It is not a token or keyword manipulation technique and carries no guarantee.

1. State core facts in plain subject–predicate–object sentences: "[Organisation] provides [service] to [audience] in [place]."
2. Use one consistent name for the organisation, each service, each product, and each place. Record approved variants.
3. Make relationships explicit: offer to audience, offer to location, person to role, product to category.
4. Link related topic pages so coverage is connected and each page's role is clear.
5. Add structured data only where it matches visible, proven facts and the consumer's current eligibility rules.

## 3. Match content to the job

| Job | Content type | Rule |
|---|---|---|
| Identity and offer | evergreen pages | keep facts current; record a fact owner |
| Changed facts | dated update pages or sections | state what changed and when; do not change dates cosmetically |
| Complex decisions | expert guides | show working, evidence, limitations, original experience |
| Reputation context | off-site profiles, reviews, community presence | keep accurate; participate authentically and rights-safely; never manufacture mentions |

## 4. Separate the outcomes

Treat each of these as a different observation with its own evidence. Never collapse them into one "AI ranking".

| Outcome | Question it answers | Typical evidence |
|---|---|---|
| Training exposure | Could the content have been used to train a model? | crawler access policy and logs; cannot be confirmed from answers |
| Retrieval / indexing | Can the product fetch or index the page? | crawl and index checks, server logs |
| Citation / answer contribution | Is the page cited or used in an answer? | recorded prompt observations, webmaster AI reports where offered |
| Representation | Is the entity described accurately? | brand-accuracy review of recorded answers |
| Referral | Did a person click through? | referrer and analytics data |
| Conversion | Did the visit produce a qualified outcome? | goal events, CRM records, lead self-report |

Wording rules:

- A mention is not a citation; a citation is not a visit; a visit is not a qualified lead.
- Name the exact measure (mention, citation, cited page, referral, sentiment, conversion) rather than "ranking".
- Mark any outcome without evidence `NOT_ASSESSED`.

## 5. Baseline before optimising

Combine partial sources; none alone shows total AI visibility.

1. Lead self-report ("How did you find us?" field with an AI-assistant option).
2. Referrer and analytics review.
3. Search Console and Bing Webmaster Tools evidence.
4. Recorded prompt observations (prompt, product, date, locale, answer, cited URLs).
5. Server-log review for relevant crawlers and user-triggered fetches.

Record the baseline date and the limits of each source.

## 6. Run reversible experiments

Test one variable at a time: one topic, page, profile, source, measurement field, or agent handoff.

Experiment record:

| Field | Entry |
|---|---|
| `hypothesis` | the expected change and why |
| `variable` | the single thing changed |
| `primary_outcome` | one outcome from section 4 |
| `guardrail` | trust, accuracy, and accessibility conditions that must hold |
| `stop_rule` | the evidence that ends the test early |
| `rollback` | how to restore the previous state |
| `review_date` | when results are judged |

Do not adopt as universal rules: a fixed opening word count, an FAQ on every page, a fixed update cadence, a load-time threshold presented as an AI rule, or a promised citation lift. Any of these may be a local acceptance choice when justified and recorded.

## 7. Prepare for agent tasks only when a real task exists

Useful readiness work when the business has a task an agent could perform:

- visible, accurate facts in accessible HTML;
- clear, labelled controls and an accessible DOM;
- current feeds or APIs where the business already maintains them;
- explicit consent and approval boundaries;
- a tested failure path.

Protocol servers, `llms.txt`, Markdown mirrors, commerce protocols, and custom agents are optional experiments, not default visibility requirements. See [agentic-readiness.md](agentic-readiness.md).

## 8. Implementation map

| Planning idea | Safe website practice | Evidence to record |
|---|---|---|
| Response modes | evergreen identity pages; current update pages; expert guides with sources | page role, source map, last review, support state |
| Entity clarity | consistent organisation, service, and product facts; valid schema only where facts are proven | fact owner, visible locator, schema check |
| Retrieval | crawlable canonical pages, truthful dates, internal links, coherent sitemap and robots rules, IndexNow where supported | crawl and index checks, change log |
| Whole-journey measurement | webmaster data, analytics and referrers, lead-source field, qualified outcomes | metric definition, denominator, consent, attribution limit |
| Agent readiness | accessible DOM, clear controls, current feeds, explicit approval boundaries | task scenario, permissions, failure path, test result |

## 9. Acceptance rule

Ship a recommendation only when it is either:

- a durable planning principle clearly labelled as such; or
- a current claim backed by a source-register record containing source scope, publication or version date, access date, verification date, freshness class, review date, support status, uncertainty, and owner.

Otherwise narrow the claim or mark it `NOT_ASSESSED`. Re-audit this reference whenever Google, Bing, or OpenAI crawler guidance changes, and at least quarterly.

## Sources

- Crystal Carter (2026) *The New Rules of AI Search: SEO for Visibility in ChatGPT, Google Gemini, and Generative Search*, John Wiley & Sons. Used as a qualified planning lens only; its statistics and tool claims are not admitted.
- Google Search Central, AI optimisation guide (version reviewed 10 July 2026) — check the current version.
- Bing Webmaster Blog, AI Performance in Bing Webmaster Tools (public preview announcement, February 2026) — check the current version.
- OpenAI, crawler documentation — check the current version.
