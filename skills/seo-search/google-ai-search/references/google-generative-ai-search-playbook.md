# Google Generative AI Search Playbook

Self-contained operating guidance prepared from current first-party sources.
Verified on 2026-09-05. Re-check by 2026-12-05 or when a platform changes its
inclusion controls, crawler policy, or report definitions. Primary sources:

- Google's Guide to Optimizing for Generative AI Features on Google Search:
  https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Search generative AI control:
  https://support.google.com/webmasters/answer/16908024
- Generative AI performance report:
  https://support.google.com/webmasters/answer/16984139
- Guidance on using generative AI content:
  https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- Bing Webmaster Tools AI Performance reporting:
  https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
- OpenAI crawler controls:
  https://developers.openai.com/api/docs/bots
- Currentness register:
  ../../../../docs/source-registers/search-ai-currentness-2026-09-05.json

## Core position

Google's generative AI features in Search, including AI Overviews and AI Mode,
are not a separate channel with separate tricks. They are rooted in Google's
core Search ranking and quality systems. Treat the work as disciplined SEO:
useful content, crawlable pages, clear technical structure, and good user
experience.

Google describes two important mechanisms:

- Retrieval-augmented generation: Search systems retrieve relevant, current
  pages from the index, then use specific information from those pages to
  support an AI response with links.
- Query fan-out: the model may run related searches across subtopics to answer
  a complex query.

Operational implication: create authoritative, useful pages that deserve to be
retrieved for a topic. Do not manufacture dozens of thin pages for every
possible query variant.

## What Google says to do

### 1. Create non-commodity content

Pass the page only when it has at least one of these durable advantages:

- first-hand experience, practitioner judgment, original testing, or original
  data
- a point of view that is not a rewrite of the current top results
- specific examples, photos, screenshots, methodology, cases, or tradeoffs
- clear structure for humans: useful headings, paragraphs, sections, and
  supporting media
- a satisfying answer to the visitor's real task, not just keyword coverage

Commodity pages such as generic listicles, rewritten summaries, and thin
"what is" pages should be consolidated, improved, or removed.

### 2. Keep the technical base clean

A page is eligible for Google AI Search features only if it is indexed and
eligible to appear in Google Search with a snippet. Inclusion is never
guaranteed.

Check:

- Googlebot can crawl the URL through robots.txt, CDN, firewall, and hosting.
- The page returns a stable 200 status and is not accidentally `noindex`.
- Canonical signals point to the intended URL.
- Important content is available as text, not only in inaccessible images,
  video, canvas, or blocked JavaScript.
- JavaScript-rendered content follows JavaScript SEO basics and is visible to
  Googlebot.
- Internal links expose the page and its related pages naturally.
- Page experience is good on mobile and desktop.
- Duplicate, filtered, thin, and low-value URL variants are reduced or
  canonicalized.

### 3. Use images and video when they help users

Google's AI Search features can surface images and video. Use original,
high-quality media when it clarifies the answer or product/service. Keep image
SEO and video SEO fundamentals in place: descriptive filenames, useful alt
text where appropriate, captions or surrounding context, transcripts for video,
and stable media URLs.

### 4. Keep local and ecommerce data current

For local and ecommerce businesses, Google may use product listings, product
information, and local business information in generative AI Search
experiences.

Check:

- Google Business Profile is claimed, complete, accurate, and actively
  maintained.
- Merchant Center is configured where products are sold.
- Product feeds match visible product pages.
- Prices, availability, shipping, returns, hours, locations, phone numbers, and
  service areas are current.
- Product, offer, review, local business, and organization structured data
  matches visible page content.
- Business Agent or emerging merchant experiences are considered only when the
  client can support the operational response quality.

### 5. Measure value, not only clicks

As of 31 August 2026, Search Console provides a dedicated generative AI
performance report worldwide for AI Overviews and AI Mode. The report exposes
impressions by page, country, date, and device; it does not expose a universal
rank, prompt-level query list, citation fidelity, or business value. Its data is
also included in the overall Web performance report.

Measure:

- dedicated generative AI impressions and page/country/device/date changes
- normal Web impressions, clicks, CTR, queries, pages, and index coverage
- engaged sessions, time on site, scroll depth, form starts, lead quality,
  subscriptions, sales, calls, and assisted conversions
- before/after changes by landing page and query class rather than one vanity
  ranking

Search Console also provides a property-level include/exclude control for
generative AI features. Record the decision, inherited property state, owner,
date, expected impact, and post-change observation. This Search control is
separate from `Google-Extended`, which does not control ordinary Search
inclusion.

## Mythbusting rules

For Google Search, do not recommend these as requirements:

- `llms.txt`, AI text files, Markdown mirrors, or special machine-readable
  files for AI Overviews or AI Mode
- chunking pages into tiny sections for AI comprehension
- writing in a special AI-only style
- creating pages for every long-tail or fan-out query variant
- pursuing inauthentic mentions to manipulate AI answers
- adding special schema.org markup for generative AI Search

Structured data still matters for rich-result eligibility and machine-readable
clarity, but it must match visible content and should not be sold as an AI
Overview hack.

### llms.txt operating rule

Google Search ignores `llms.txt` and similar machine-readable AI/Markdown files
for Search visibility and ranking. Treat those files as optional handover
artifacts for developer documentation, agentic coding workflows, internal
knowledge packaging, or a client-specific non-Google crawler requirement.

Do not spend strategy budget on `llms.txt` before the durable work is handled:

- crawlable, indexable HTML
- original, useful content with specific proof
- accurate schema that matches visible content
- strong internal links and page intent
- complete Google Search Console and Bing Webmaster Tools measurement
- local, product, author, and organization facts that remain current

If a CMS generates `llms.txt` automatically, keep it accurate and harmless. Do
not sell it as an AI-citation lever.

## Bing/Copilot AI measurement

Bing Webmaster Tools introduced AI Performance in public preview on 10 February
2026. Its documented measures are:

- **Total Citations**: displayed source citations in the selected period;
- **Average Cited Pages**: average unique site pages cited per day;
- **Grounding queries**: a sample of phrases used to retrieve cited content;
- **Page-level citation activity**: citation counts for individual URLs; and
- **Visibility trends**: change in citation activity over time.

Microsoft explicitly warns that these measures do not indicate ranking,
authority, placement, or a page's role in an answer. Pair them with citation
support review, analytics, CRM, and conversion evidence. Use IndexNow for added,
updated, or removed URLs when the project supports it; submission accelerates
discovery but does not guarantee indexing or citation.

## Source-integrity and UGC poisoning guardrail

AI assistants and deep-research agents can over-trust user-generated content
when it is lexically close to the query. Treat Reddit, Quora, Wikipedia-style
comments, forum posts, review snippets, and community Q&A as high-variance
sources: useful for language and objections, unsafe as sole evidence for
recommendations, finance, health, legal, safety, or procurement claims.

Before publishing AI-search-oriented content:

- prefer primary sources, regulator pages, official documentation, named
  researchers, original data, and signed expert commentary
- separate "what users say" from "what is true"
- do not cite anonymous UGC as proof unless independently verified
- monitor high-value brand and category queries for misleading snippets,
  impersonation, spam recommendations, and poisoned comments
- keep correction paths ready: update own content, publish clarifications,
  request platform moderation where appropriate, and preserve evidence
- never plant comments or manufacture UGC to influence AI assistants

## Multi-assistant visibility

AI-search visibility is not one engine. Google, Bing/Copilot, ChatGPT, Gemini,
Claude, Perplexity, and vertical assistants can retrieve, cite, or summarize
different sources. Build the common foundation first, then measure by engine:

- Google: dedicated generative AI impressions, normal Web reporting, page
  classes, and conversions
- Bing/Copilot: total citations, cited pages, sampled grounding queries,
  page-level activity, and trends in Bing Webmaster Tools AI Performance
- ChatGPT: OAI-SearchBot access, server logs, cited URLs, answer-support review,
  and referrals carrying `utm_source=chatgpt.com` where present
- other assistants: current first-party crawler guidance, server logs, cited
  URLs, answer-support review, and referral patterns where available
- Brand monitoring: cited pages, source quality, answer accuracy, and unsafe
  recommendations

Do not infer global AI visibility from one assistant.

## Volatility discipline

During confirmed or suspected ranking volatility, avoid reactive rewrites. First
separate:

- tracking noise and seasonality
- known core updates or unconfirmed volatility windows
- indexation/crawl problems
- site releases, redirects, content changes, or technical regressions
- query-class movement versus whole-site movement

Use a 7- to 14-day watch window for non-critical drops unless there is clear
technical breakage, legal risk, or business-critical conversion loss. Record the
hypothesis and evidence before changing pages.

## AI-assisted content rule

AI can help research, structure, summarize internal notes, and improve drafts.
It becomes a risk when it creates many pages with little originality or added
value. Apply the same Search Essentials and spam-policy standards to AI-assisted
content as to any other content.

For ecommerce, AI-generated product images and product data may have separate
Merchant Center labeling and metadata requirements. Route product-feed or
AI-generated-product-media questions to ecommerce and Merchant Center review.

## Stakeholder script

Use this when a client asks for "AEO/GEO hacks":

"For Google Search, AI Overviews and AI Mode are still based on Google's Search
index and quality systems. The work is not to game a new bot. The work is to
make the right pages crawlable, indexable, useful, original, technically clear,
and satisfying enough to be retrieved and linked when Google answers complex
questions."
