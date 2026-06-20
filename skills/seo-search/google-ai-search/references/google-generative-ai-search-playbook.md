# Google Generative AI Search Playbook

Self-contained operating guidance prepared from official Google Search Central
documentation. Verified on 2026-06-19 against official Google Search Central
guidance and current AI-search measurement/security reporting. Primary sources:

- Google's Guide to Optimizing for Generative AI Features on Google Search:
  https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- AI features and your website:
  https://developers.google.com/search/docs/appearance/ai-features
- Guidance on using generative AI content:
  https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- Bing Webmaster Tools AI Performance reporting:
  https://blogs.bing.com/webmaster
- Cornell/arXiv research on deep-research agent poisoning:
  https://arxiv.org/

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

Google reports AI-feature traffic inside Search Console's normal Web search
performance reporting. Do not expect a clean standalone AI Overview report for
every question.

Measure:

- Search Console impressions, clicks, CTR, query/page changes, and coverage
  issues
- engaged sessions, time on site, scroll depth, form starts, lead quality,
  subscriptions, sales, calls, and assisted conversions
- before/after changes by landing page and query class rather than one vanity
  ranking

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

Bing Webmaster Tools has begun exposing AI Performance dimensions that are more
specific than traditional search reports. When Bing/Copilot visibility matters,
track:

- **Citation Share**: the share of citations attributed to the site among all
  citations shown for the same grounding query. Use it as an observational
  trend KPI, not a ranking score, traffic-share metric, or competitor spy tool.
- **Intents**: the purpose or need behind AI answer queries.
- **Topics**: grouped subject areas where the site is being used or ignored.
- **Compare**: period-over-period shifts in AI citation activity.

Operational rule: pair Bing AI Performance with Search Console, analytics, CRM,
and conversion data. A rising citation share is useful only when the cited pages
also support trust, conversion, retention, or qualified demand.

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

- Google: Search Console Web reporting, page/query classes, conversions
- Bing/Copilot: Bing Webmaster Tools AI Performance and Citation Share
- ChatGPT/Perplexity/Claude-style retrieval: server logs, bot requests,
  referral patterns where available, and third-party AI-visibility tracking
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
