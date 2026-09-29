# Website Skills Engine

The Website Skills Engine is a routed library of agent skills for planning, writing, building, auditing, launching and maintaining static websites built from markdown content and approved assets. Its 62 active skills cover eleven categories: agency operations, brand, build, commerce, content and copy, launch operations, engine maintenance, orchestration, quality gates, search, and conversion. The engine follows WCAG 2.2 AA with the WAI-ARIA Authoring Practices, OWASP ASVS 5.0.0 for verifiable security controls and the OWASP Top 10:2025 for threat awareness, RFC 9116 for `security.txt`, Google Search Essentials and the Google structured-data guidelines with Schema.org, and the Core Web Vitals thresholds published on web.dev. Privacy work is checked against the Uganda Data Protection and Privacy Act 2019, the Kenya Data Protection Act 2019, POPIA, the Nigeria Data Protection Act 2023 and the GDPR. Every release passes through executable gates: performance budgets enforced through Lighthouse CI, an accessibility gate built on axe-core, security and supply-chain checks, visual regression, and a slop scan run by a vendored copy of the `chwezi-slop` detector.

It produces strategy and positioning briefs, sitemaps and page specifications, website copy in English, French and Kiswahili, design tokens and component rules, production pages with structured data and analytics event maps, and scaffolded multilingual static-site projects. It also produces accessibility, security, SEO, conversion and design-quality audit reports, release evidence with rollback plans, privacy and terms pages, monthly client reports, and retainer and referral programmes. It serves website agencies, freelance developers, and in-house marketing and product teams, with particular attention to East African markets: constrained bandwidth, mobile money, and local languages. A syllabus and exam support operator certification. A skill or a passed checklist is evidence for review, not a certificate of a live site's results; field performance, legal compliance and conversion claims still need their own evidence.

## Installation

**Prerequisites.** Node.js 18 or later for the installer (`install.sh` and `install.ps1` exit without it). Python 3.11 or later for the validators and the Codex model-policy helper (CI uses Python 3.12 with `PyYAML` and `pytest`, and Node.js 22 for the slop-pack and hook tests). Git is needed for the manual route and for `new-project` scaffolding.

**Claude Code plugin.** The repository ships `.claude-plugin/marketplace.json` (marketplace `chwezi-website`) and `.claude-plugin/plugin.json` (plugin `website`, version 1.1.0, all 62 skills):

```text
/plugin marketplace add https://github.com/peterbamuhigire/website-skills
/plugin install website@chwezi-website
```

**Installer.** Both entry points delegate to `scripts/install-engine.js`, which copies the engine into `~/.claude` (`--scope user`, the default) or `./.claude` (`--scope project`) and records ownership in `.chwezi/install-state.json`. The script also accepts `--dry-run` and `--json`:

```sh
git clone https://github.com/peterbamuhigire/website-skills
cd website-skills
./install.sh --scope project        # macOS, Linux or Git Bash
.\install.ps1 --scope project       # Windows PowerShell
node scripts/install-engine.js doctor --scope project
```

**Codex.** Codex reads `AGENTS.md`. Its Codex-only section runs `python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`, and `--apply` only when drift is reported. Claude skips that section.

**Manual route.** Clone the repository and point the agent at `CLAUDE.md`, which imports `AGENTS.md`, the runner-agnostic router. Skills live at `skills/<category>/<skill>/SKILL.md`. To start a client site, copy `new-project.sh` (or `new-project.ps1`) into an initialised Git repository and run it. It adds this engine as a submodule at `.claude/skills/`, creates the `en`, `fr` and `sw` content folders, and copies the content templates.

## Capabilities

The table below is generated from `skills/*/*/SKILL.md` (62 files; no aliases or templates are counted) and matches `skills/manifest.yml`.

| Category | Skills | Coverage |
|---|---:|---|
| `agency-ops` | 14 | Agency positioning, offers, sales, delivery, support, reporting, retention and referrals |
| `brand` | 2 | Brand strategy and brand storytelling |
| `build` | 6 | Reference analysis, design systems, internationalisation, pages and image assets |
| `commerce` | 5 | Store strategy, checkout, funnels, analytics and omnichannel retail |
| `content-copy` | 11 | Page, blog, sales and long-form copy; voice; English, French and Kiswahili standards |
| `launch-ops` | 4 | Deployment, experimentation, measurement and observability |
| `meta` | 3 | Skill writing, skill safety review and router documentation |
| `orchestration` | 6 | End-to-end website delivery, experience mapping, premium, hospitality and African-market builds |
| `quality-gates` | 6 | Accessibility, visual QA, design quality, consistency, security and Kaizen review |
| `seo-search` | 3 | SEO implementation, SEO audit and Google AI search |
| `ux-conversion` | 2 | Conversion audit and buyer-question content |
| **Total** | **62** | |

| Category | Skill | What it does |
|---|---|---|
| agency-ops | `agency-client-retention` | Designs post-launch retainers, review cadence, expansion offers and churn controls. |
| agency-ops | `agency-positioning` | Defines a premium agency's niche, offer ladder, qualification, fees and scope boundaries. |
| agency-ops | `authority-offers` | Packages expertise into lead magnets, paid audits, workshops and mini-products. |
| agency-ops | `customer-service-website-ops` | Designs post-launch support triage, escalation and recovery language. |
| agency-ops | `delivery-automation` | Audits and automates repeatable delivery work; build-versus-buy and SOPs. |
| agency-ops | `email-sender` | Implements a self-hosted PHP and PHPMailer form-mail flow with spam and CSRF controls. |
| agency-ops | `launch-campaigns` | Sequences an established offer through prelaunch, launch, close and follow-up. |
| agency-ops | `local-in-person-acquisition` | Plans ethical face-to-face acquisition for a niche local web studio. |
| agency-ops | `monthly-report` | Produces an evidence-backed monthly website or SEO client report. |
| agency-ops | `policy-pages` | Drafts privacy and terms pages from verified processing and jurisdiction facts. |
| agency-ops | `premium-sales-conversation` | Qualifies and diagnoses a premium opportunity before any quote or proposal. |
| agency-ops | `referral-program` | Designs a consent-based client referral programme with disclosure rules. |
| agency-ops | `service-blueprint-website-delivery` | Maps frontstage and backstage delivery operations, owners, SLAs and fail points. |
| agency-ops | `social-media` | Plans measurable social channels, content and offer-led campaigns tied to a website. |
| brand | `brand-storytelling` | Turns an approved brand strategy into evidence-based narrative for pages and campaigns. |
| brand | `brand-strategy` | Establishes audience, positioning, differentiation and a decision-ready brand brief. |
| build | `design-reference` | Analyses reference and competitor sites into an implementation-facing design direction. |
| build | `design-system` | Converts an approved brand brief into tokens, component rules, states and motion. |
| build | `i18n` | Implements multilingual routes, locale content, hreflang, canonicals and sitemaps. |
| build | `image-compression` | Generates measured web-image derivatives from approved source assets. |
| build | `page-builder` | Builds approved content, design, schema and analytics into production pages. |
| build | `photo-manager` | Catalogues, selects, approves and places logos and website photographs. |
| commerce | `ecommerce` | Defines an online store's model, experience, trust and growth strategy. |
| commerce | `ecommerce-analytics` | Defines or audits ecommerce events, KPIs, funnels, cohorts and attribution. |
| commerce | `ecommerce-checkout` | Specifies or audits cart, checkout, payment recovery and post-purchase flow. |
| commerce | `ecommerce-funnel` | Designs acquisition, retargeting, lifecycle messaging and repeat-purchase journeys. |
| commerce | `retail-commerce-operating-system` | Specifies an omnichannel retail site integrated with catalogue, POS, fulfilment and finance. |
| content-copy | `blog-idea-generator` | Produces evidence-grounded topic ideas, series and editorial calendars. |
| content-copy | `blog-writer` | Turns an approved topic into a researched, source-disciplined article. |
| content-copy | `brand-voice` | Reproduces a client's actual voice consistently across pages and posts. |
| content-copy | `content-writing` | Writes page and interface copy with clear hierarchy and evidence-aware editing. |
| content-copy | `east-african-english` | Makes English copy read as natural, professional East African English. |
| content-copy | `french-native-copy` | Writes French copy that reads as native for a named francophone market. |
| content-copy | `language-standards` | Sets cross-language tone, terminology and locale-ownership rules. |
| content-copy | `long-form-sales-copy` | Writes long-form sales pages, VSL, webinar and funnel copy for a defined offer. |
| content-copy | `premium-commercial-writing` | Writes authority, offer and SEO copy that justifies premium fees through proof. |
| content-copy | `sales-copywriting` | Builds a page's conversion argument, proof sequence, objection handling and CTAs. |
| content-copy | `swahili-native-copy` | Writes Kiswahili copy that reads naturally for a named East African market. |
| launch-ops | `deploy` | Builds, release-gates, deploys, verifies and makes a site rollback-ready. |
| launch-ops | `experimentation` | Runs pre-registered controlled tests with power checks, guardrails and decisions. |
| launch-ops | `marketing-measurement-system` | Defines a KPI tree, event plan and decision-ready reporting. |
| launch-ops | `observability` | Sets up real-user performance, error tracking, alerts and an operator runbook. |
| meta | `skill-safety-audit` | Reviews a new or changed skill for unsafe instructions and permission inflation. |
| meta | `skill-writing` | Creates or upgrades engine skills under the canonical chwezi-dev-engine standard. |
| meta | `update-claude-documentation` | Reconciles routers, counts and maintainer documentation after catalogue changes. |
| orchestration | `africa-excellence` | Makes a site work in African markets: bandwidth, mobile money, USSD, language, trust. |
| orchestration | `hospitality-website-product` | Designs and builds websites for hotels, lodges, restaurants and venues. |
| orchestration | `premium-ui-ux-design` | Orchestrates build-coupled UX and visual quality before design-system and page work. |
| orchestration | `premium-website-product` | Qualifies a revenue-critical website as a premium product with scope and no-bid rules. |
| orchestration | `website-builder` | Orchestrates a complete website from approved inputs through handover. |
| orchestration | `website-experience-mapping` | Maps journeys, moments of truth and service interactions before page architecture. |
| quality-gates | `accessibility-audit` | Audits rendered pages against WCAG 2.2 AA with automated and manual checks. |
| quality-gates | `cross-page-design-consistency-audit` | Detects competing design systems, template drift and translation drift across pages. |
| quality-gates | `design-quality-score` | Scores a rendered site against the seven-category design-quality and anti-slop rubric. |
| quality-gates | `kaizen-engine-and-product-improvement` | Audits and improves the engine or any web product it produces. |
| quality-gates | `security-gate` | Audits dependencies, secrets, headers, SRI, `security.txt` and supply chain before release. |
| quality-gates | `visual-qa` | Reviews rendered routes for screenshot drift, overflow, empty sections and regressions. |
| seo-search | `google-ai-search` | Advises on Google AI Overviews, AI Mode and Search Console AI measurement. |
| seo-search | `seo` | Implements metadata, structured data, sitemaps, crawler controls and entity presence. |
| seo-search | `seo-audit` | Performs a read-only audit of crawl, indexation, schema, AI citations and measurement. |
| ux-conversion | `cro-audit` | Audits an existing site for evidence-backed conversion barriers and test priorities. |
| ux-conversion | `they-ask-you-answer` | Builds a buyer-question content and assignment-selling system for an agency. |

## Quality gates and validation

The gate scripts run against a built site: `scripts/perf-gate.sh` (budgets in `performance-budgets.json`, Lighthouse configuration in `lighthouserc.json`), `scripts/a11y-gate.sh`, `scripts/security-gate.sh`, `scripts/visual-qa.sh`, `scripts/slop-scan.sh` (vendored detector in `scripts/vendor/chwezi-slop/`, verified by `scripts/check-vendored-detector.py`) and `scripts/post-deploy-smoke.sh`. The engine's own contracts are checked by `scripts/validate-skill-registry.py`, `scripts/validate-skill-contracts.py`, `scripts/routing-smoke-test.py`, `scripts/validate-search-doctrine.py`, `scripts/source_ingestion_guardrail.py` and `python -m pytest -q`. The registry validator and `tests/test_kaizen_wave1_contracts.py` both require the skill total and category counts in this README to match the filesystem. Operator certification material is in `certification/`.

## References

Citations only. Book methods are paraphrased into task-oriented references with a short attribution. Book extractions and book summaries are never stored in this repository (see `docs/continuous-improvement/book-source-retirement-2026-09-24.md`). Where the repository omits a publisher or year, it is omitted here.

### Books

- Aames, A. *Trilingual Story Book*.
- Agius and Clancey. *Faster, Smarter, Louder*.
- Almasi, Fallon et al. *Swahili Grammar for Introductory and Intermediate Levels (Sarufi ya Kiswahili)*.
- Andrew, R. (2019) *Get Ready for CSS Grid Layout*, 2nd edn, A Book Apart.
- Andrews, G. *Making Your Website Work: 100 Copy & Design Tweaks*.
- Ariely, D. (2008) *Predictably Irrational*, HarperCollins.
- Baker, D. C. *The Business of Expertise*.
- Bank, C. and Cao, J. *Web UI Design Best Practices*.
- Beyer et al. *Site Reliability Engineering*.
- Bhatti et al. *Docs for Developers*.
- Bishop, W. and Starkey, D. (2006) *Keywords in Creative Writing*, Utah State University Press.
- Blauer, I. and Woolley, A. (c. 2021) *Keywords for SEO: Actionable Knowledge Bombs to Help You Rank on Google in 2021*.
- Block. *Flawless Consulting*.
- Blount, J. (2015) *Fanatical Prospecting*, Wiley.
- Bly, R. *The Copywriter's Handbook*, 4th edn.
- Bly, R. *How to Write and Sell Simple Information*.
- Bohnke, C. (2024) *From Zero to UI/UX Hero*.
- Boulares, M. and Frérot, J.-L. *Grammaire progressive du français — Niveau avancé*, CLE International.
- Branson, S. (2020) *UX / UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*.
- Brown, R. (2016) *Build Your Reputation: Grow Your Personal Brand for Career and Business Success*, Capstone (John Wiley & Sons).
- Brunson, R. (2013) *108 Proven Split Test Winners*, DotComSecrets Labs.
- Brunson, R. (2015) *DotCom Secrets*, Hay House.
- Brunson, R. *Expert Secrets*.
- Butterick, M. *Practical Typography*.
- Caples, J. *Tested Advertising Methods* (as relayed in Serling 2002).
- Carter, C. (2026) *The New Rules of AI Search: SEO for Visibility in ChatGPT, Google Gemini, and Generative Search*, John Wiley & Sons.
- Cialdini, R. (2007) *Influence*, Collins.
- Coleman, J. (2018) *Never Lose a Customer Again*, Portfolio.
- Conta, A. (2024) *The Art and Science of UX Design*.
- Cook, P. (2022) *Fundamentals of HTML, SVG, CSS and JavaScript for Data Visualisation*, Leanpub.
- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics: Use Data to Build a Better Startup Faster*, O'Reilly Media.
- Deacon, P. B. (2020) *UX and UI Design Strategy: A Step-by-Step Guide*.
- Debelak, D. (2006) *Business Models Made Easy*, Entrepreneur Press.
- Debelak, D. (2006) *Perfect Phrases for Business Proposals and Business Plans*, McGraw-Hill.
- Devitt, R. et al. *Arrive: A Design Innovation Framework to Deliver Breakthrough Services, Products and Experiences*, Routledge.
- DK. *French–English Bilingual Visual Dictionary*.
- Doerr, J. (2018) *Measure What Matters*, Portfolio.
- Dunford, A. (2019) *Obviously Awesome*.
- Edwards, R. (2018) *How to Write Copy That Sells*, self-published.
- Enders, J. (2016) *Designing UX: Forms — Create Forms That Don't Drive Your Users Crazy*, SitePoint.
- Enns, B. (2010) *The Win Without Pitching Manifesto*.
- Enns, B. *The Four Conversations*.
- Fabian, J. *Language and Colonial Power*.
- Fekeshazi, Z. (c. 2017) *Product Managers' Guide to UX Design*, UX Studio.
- Fishbein, M. *Growth Hacking with Content Marketing*, self-published.
- Fitzpatrick. *The Mom Test*.
- Fox, T. *Anatomy for Artists* (read; no claim is attributed to it).
- Franz, B. (2025) *Usability and User Experience Design*.
- French Hacking. *2000 French Phrases* and *50 Most Used French Verbs*.
- Garner, R. (2012) *Search and Social: The Definitive Guide to Real-Time Content Marketing*, Wiley/Sybex.
- Gerber, M. *The E-Myth*.
- Godin, S. (2018) *This Is Marketing*.
- Goward, C. (2012) *You Should Test That*.
- Graves. *Writing for Profit*.
- Grigorik, I. *High Performance Browser Networking*, O'Reilly.
- Halvorson, K. and Rach, M. *Content Strategy for the Web*, 2nd edn.
- Handley, A. *Everybody Writes*, 2nd edn.
- Hargis, Carey et al. *Developing Quality Technical Information*.
- Hedley, D. (2013) *How to Create $1,600/Month Niche Websites for Passive Income*.
- Heminway, A. *Practice Makes Perfect: Complete French Grammar*, McGraw-Hill.
- Hennessy, B. (2018) *Influencer: Building Your Personal Brand in the Age of Social Media*, Citadel Press (Kensington).
- Hodent, C. (2022) *What UX Is Really About: Introducing a Mindset for Great Experiences*, CRC Press.
- Hoskins, D. *The Product-Minded Engineer*.
- Hunter, V. L. with Tietyen, D. (1997) *Business to Business Marketing: Creating a Community of Customers*, NTC Business Books.
- Hype4. *Frontend Unicorn* and *DESIGN.RIP — Master UI Design Elements*.
- Iny, D. et al. *Blog Post Ideas*.
- InVision. *Design Systems Handbook*.
- Jantsch, J. (2010) *The Referral Engine*, Portfolio.
- Johnson, J. (2021) *How to Become a Social Media Manager*.
- Jones, R. (2010) *Keyword Intelligence*, Wiley.
- Kalbag, L. *Accessibility for Everyone*.
- Karpavičius, A. *Software Craftsmanship Using AI*.
- Kennedy, D. S. (2000) *The Ultimate Sales Letter*, 2nd edn, Adams Media.
- Kennedy, D. S. (2004) *No B.S. Sales Success*, 3rd edn, Entrepreneur Press.
- Kennedy, D. S. and Marrs, J. (2011) *No B.S. Price Strategy*, Entrepreneur Press.
- Kennedy, D. S., Glazer, B. and Skrob, R. (2009) *The Official Get Rich Guide to Information Marketing*, 2nd edn, Entrepreneur Press.
- Klein, L. (2013) *UX for Lean Startups: Faster, Smarter User Experience Research and Design*, O'Reilly Media.
- Kleon, A. (2014) *Show Your Work!*, Workman.
- Kohavi, Tang and Xu (2020) *Trustworthy Online Controlled Experiments*.
- Krug, S. (2014) *Don't Make Me Think, Revisited: A Common Sense Approach to Web and Mobile Usability*, 3rd edn, New Riders.
- Kruger, Z. (2024) *The Art of SXO*.
- Krzyzek, A. and Krzyzek, P. *Made to Sell*.
- LaGrone, B. (2016) *Web Design Blueprints*, Packt Publishing.
- Landa, R. (2022) *Strategic Creativity: A Business Field Guide to Advertising, Branding, and Design*, Routledge.
- Levy, J. (2015) *UX Strategy: How to Devise Innovative Digital Products that People Want*, O'Reilly Media.
- Lexus. *Rough Guide Phrasebook: Swahili*.
- Lima. *Fundamentals of Writing*.
- Lin, L. C. (2013) *Decode and Conquer: Answers to Product Management Interviews*, 2nd edn, Impact Interview.
- Living Language. *Swahili (Spoken World)*.
- Majors, Fong-Jones and Miranda. *Observability Engineering*.
- Malaquias, M. R. *Authentic East African Swahili Cuisine*.
- Mangialardi, M. *Design Systems for Developers: Learn How to Code Design Systems That Scale*.
- Marcos, J., Guesalaga, R., Hough, A. and Vincent, R. (c. 2025) *The High-Performing Key Account Manager: Creating Sustained Value with Strategic Customers*, Kogan Page.
- Marten, L. and McGrath, D. L. *Colloquial Swahili*.
- Maxwell. *7 Steps to Better Writing*.
- McDermott, A. (2023) *Efficient Content Creation: A Practical Guide to Consistently Creating High-Quality Content in a Busy Schedule*, The Recognized Authority.
- McNeil, P. (2010) *The Web Designer's Idea Book, Volume 2*, HOW Books.
- McNeil, P. (2013) *The Web Designer's Idea Book, Volume 3*, HOW Books.
- Miller, C. H. *Digital Storytelling*.
- Miller, D. (2017) *Building a StoryBrand*, HarperCollins Leadership.
- Morgan, P. *The Positioning Manual for Indie Consultants* and *for Technical Firms*.
- Mugane, J. M. *The Story of Swahili*.
- Murtagh, R. (2012–2013) *Build a Better Website* (also published as *The Million Dollar Website*), MillionDollarWebsite.TV.
- Nahai, N. (2012) *Webs of Influence: The Psychology of Online Persuasion*, Pearson.
- Nelson, J. (2019) *The Seven Figure Agency Roadmap: How to Build a Million Dollar Digital Marketing Agency*, Seven Figure Agency LLC.
- Norman, D. *The Design of Everyday Things*, revised edn.
- Nudelman, G. with Kempka, D. *UX for AI*.
- Nurse, D. and Spear, T. *The Swahili*.
- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly Media.
- Paduraru, E. (2024) *Roots of UI/UX Design: Learn to Develop Intuitive Web Experiences*, Creative Tim.
- Panzarella, L. (2022) *UI & UX Web Design Simply Explained*.
- Pickering, H. *Inclusive Components*.
- Pickering, H. and Bell, A. (2019 onward) *Every Layout*, every-layout.dev.
- Plumley, G. (2011) *Website Design and Development: 100 Questions to Ask Before Building a Website*, Wiley Publishing.
- Poisson-Quinton, S. *French Grammar in 44 Lessons* (Level A1).
- Polyglot Planet. *Learn French II — Parallel Text, Short Stories, Intermediate*.
- Pulizzi, J. (2021) *Content Inc.*, 2nd edn, McGraw Hill.
- Reichheld, F. and Markey, R. (2011) *The Ultimate Question 2.0*, HBR Press.
- Robinson, P. *Secrets of Business Value*.
- Roche, M. *Business English Vocabulary: Advanced Masterclass* and *Business English Speaking: Advanced Masterclass*, IDM Business and Law.
- Roetzer, P. (2012) *The Marketing Agency Blueprint*, Wiley.
- Rubinelli, S. *Institutional Health Communication in the Information Age*.
- Russell, J. *Swahili (Teach Yourself)*.
- Sadr, A. *Designing for AI* (early release, chapters 1–3).
- Safie, A. (2010) *Cutting Edge Keyword Research*.
- Schwartz, E. (2021) *Product-Led SEO*.
- Segall, R. et al. (Flux Academy) *The Complete Guide for Choosing Colors*.
- Serling, B. (ed.) (2002) *How To Write Million Dollar Ads, Sales Letters & Web Marketing Pieces*, The Internet Marketing Center.
- Sheridan, M. (2017) *They Ask, You Answer*, Wiley.
- Silver, A. *Form Design Patterns*.
- Skolnick, E. *Video Game Storytelling*.
- Smashing Magazine (2011) *How to Create Selling E-Commerce Websites*, Smashing Magazine.
- Sobia Publication (2022) *Powerful Social Media Marketing for Beginners*.
- Stockwell, J. and Shaw, H. M. (1994) *Direct Marketing Checklists*, NTC Business Books.
- Stutts, P. (2021) *The Undefeated Marketing System*, Scribe Media (Lioncrest).
- Sugarman, J. *The Adweek Copywriting Handbook*.
- Synechron Inc. (2018) *Bridge the User Experience Gap in Enterprise Applications for Financial Services & Insurance*, Synechron.
- *The Chicago Manual of Style*, 17th edn.
- Think French magazine. *Read & Think French, Premium*.
- 3DTotal.com. *Dynamic Characters*.
- Tidwell, J., Brewer, C. and Valencia, A. (2020) *Designing Interfaces*, 3rd edn, O'Reilly Media.
- Torres, T. *Continuous Discovery Habits*.
- Touri Language Learning. *Conversational French Dialogues*.
- Tullis, T. and Albert, B. *Measuring the User Experience*.
- Tzuo, T. with Weisert, G. (2018) *Subscribed*, Portfolio.
- UXPin. *Web UI Design for the Human Eye: Principles of Visual Consistency*.
- Verganti, R. (2016) *Overcrowded: Designing Meaningful Products in a World Awash with Ideas*, MIT Press.
- Wagner, J. *Web Performance in Action*, Manning.
- Walker, J. *Launch*.
- Warrillow, J. (2011) *Built to Sell*, Portfolio.
- Warrillow, J. (2015) *The Automatic Customer*, Portfolio/Penguin.
- Wathan and Schoger. *Refactoring UI*.
- Weinberg, G. and Mares, J. (2014) *Traction: A Startup Guide to Getting Customers*, S-curves Publishing.
- Weiss, A. *Value-Based Fees*.
- Wiebe, J. (2011) *Copy Hackers: 6 Persuasion Strategies*, Copy Hackers; also *Where Stellar Messages Come From*, *The Great Value Proposition Test*, *Buttons* and *Headlines, Subheads & Value Propositions*.
- Williams, R. (1976) *Keywords: A Vocabulary of Culture and Society*, Fontana.
- Wilson, P. M. *Simplified Swahili*, Longman.
- Yellen, P. (1998) *Zero-Resistance Selling*, Prentice Hall Press.
- Cited by title only in the repository: *Applying the Kaizen in Africa* (2018); *LEAN: Ultimate Collection* (2018); *The Art and Business of Online Writing*; *The Bezos Letters*; *Yes!*; *Buyology*; *Book Yourself Solid*; *SPIN Selling*; *Managing the Professional Service Firm*; *Made to Stick*; *Principles*; *Traction* (role-based training map); *The E-Myth Revisited*; *The E-Myth Manager*; *DesignOps Handbook*; *7 Must-Ask Questions Before You Hire a Website Agency*; *Profitable Online Presence*; *BLOGS CONTENTS*. The human-English review also records author-and-genre sources without titles (David, Gupta, Pinnacle, Betsis and Mamas).

### Repositories

Repositories studied in the September 2026 ten-repository Kaizen (M10), from which this engine adopted ideas. All adoptions are paraphrased, and no source files were copied:

- Impeccable — https://github.com/pbakaus/impeccable — Apache-2.0, commit `114ea1d` — rule ideas and numeric thresholds behind the vendored `chwezi-slop` detector (typography, colour, glow and heading rules; value-scope waivers). Its font lists are used only as evidence for bans.
- Addy Osmani agent-skills — https://github.com/addyosmani/agent-skills — MIT, commit `2686b62` — the owner-outranks-self routing rule in `scripts/routing-smoke-test.py` and lint refinements in `scripts/validate-skill-contracts.py`.
- Superpowers — https://github.com/obra/superpowers — MIT, commit `8ca22db` — the job-classification step in the website-builder stage gates and the description-narration lint in `skill-writing/scripts/quick_validate.py`.
- Ponytail — https://github.com/DietrichGebert/ponytail — MIT, commit `e3ba2aa` — the `native:` / `delete:` / `yagni:` / `net:` finding format for the page-builder minimalism pass.
- UI UX Pro Max — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill — MIT, commit `09170ee` — the table shape (sector, visitor job, section order, CTA, trust) for the East African industry page patterns. No rows or wording were reused.
- Graphify — https://github.com/Graphify-Labs/graphify — Apache-2.0 — the framing of links as references between documents, used in `scripts/content_link_graph.py`. No code or package is used.
- Awesome Claude Skills — https://github.com/ComposioHQ/awesome-claude-skills — no root licence — its vetting surfaced playwright-skill (next entry).
- playwright-skill — https://github.com/lackeyjb/playwright-skill — MIT, commit `dd47a6a` — the visual-QA pre-flight step: find the running dev server, and never report a pass without inspecting the rendered page.
- Caveman (https://github.com/JuliusBrussee/caveman), Understand Anything (https://github.com/Egonex-AI/Understand-Anything) and Archify (https://github.com/tt-a1i/archify) were studied in the same review. Nothing from them was adopted into this engine.

Other repositories:

- design-system-skills — https://github.com/peterbamuhigire/design-system-skills — source of the vendored `chwezi-slop` detector (`tools/slop-detector`, commit `3fe84a6`, hash-pinned in `scripts/vendor/chwezi-slop/VENDOR.json`).
- chwezi-dev-engine — https://github.com/peterbamuhigire/chwezi-dev-engine — the canonical skill-writing standard that `meta/skill-writing` points to.
- ECC — github.com/affaan-m/ECC — the Windows path fix in `install.sh` and the user/project scope model in `scripts/install-engine.js`.
- codex-astra-luna-orchestrator — https://github.com/donvito/codex-astra-luna-orchestrator — concept reference for the Codex model-policy helper, inspected at commit `21f4561`. It was implemented independently, and the upstream installer was not run.
- Lighthouse — https://github.com/GoogleChrome/lighthouse — default configuration, screen-emulation constants and throttling documentation behind the performance gate.
- web-vitals — https://github.com/GoogleChrome/web-vitals — attribution build used for real-user monitoring.
- WebPageTest — https://github.com/catchpoint/WebPageTest — connectivity presets.
- axe-core — https://github.com/dequelabs/axe-core — accessibility rule engine for the accessibility gate.
- pixelmatch — https://github.com/mapbox/pixelmatch — screenshot-diff comparison for visual QA.

### Standards and official sources

- W3C: WCAG 2.2 (https://www.w3.org/TR/WCAG22/); WAI-ARIA 1.2 and the ARIA Authoring Practices Guide (https://www.w3.org/WAI/standards-guidelines/aria/, https://www.w3.org/WAI/ARIA/apg/).
- OWASP: ASVS 5.0.0 (https://owasp.org/www-project-application-security-verification-standard/); Top 10:2025 (https://owasp.org/Top10/); Top 10 for Large Language Model Applications; Secure Headers Project (https://owasp.org/www-project-secure-headers/); Dependency-Check (https://owasp.org/www-project-dependency-check/).
- IETF RFC 9116, security.txt (https://www.rfc-editor.org/rfc/rfc9116).
- ISO 9241-210:2019, human-centred design for interactive systems, and ISO 9241-110.
- NIST Privacy Framework (https://www.nist.gov/privacy-framework).
- Schema.org, version 30.0 (https://schema.org/version/latest/), and the Schema.org validator (https://validator.schema.org/).
- Google Search Central: Search Essentials; SEO Starter Guide; general structured-data guidelines; featured snippets; page experience; crawlable links; building sitemaps; the generative-AI features guide and the guidance on generative-AI content; the documentation updates log; and the 2023 notice retiring the sitemaps ping (https://developers.google.com/search/docs). Google Search Console Help: the generative-AI performance report and control (https://support.google.com/webmasters/answer/16984139, /16908024). Rich Results Test (https://search.google.com/test/rich-results).
- web.dev: Web Vitals (https://web.dev/articles/vitals), defining the Core Web Vitals thresholds (https://web.dev/articles/defining-core-web-vitals-thresholds), and INP becoming a Core Web Vital (https://web.dev/blog/inp-cwv-launch).
- Microsoft Bing Webmaster Tools: sitemaps help, and the AI Performance public preview (https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview). IndexNow documentation (https://www.indexnow.org/documentation).
- AI crawler and model documentation: OpenAI crawlers (https://developers.openai.com/api/docs/bots) and the publishers and developers FAQ; Perplexity crawlers (https://docs.perplexity.ai/docs/resources/perplexity-crawlers); OpenAI image-generation and image-prompting guides; the Anthropic models overview (https://platform.claude.com/docs/en/models/overview); the llms.txt proposal (https://llmstxt.org/); Model Context Protocol documentation.
- GitHub Actions secure use (https://docs.github.com/en/actions/reference/security/secure-use); GitHub Advisory Database (https://github.com/advisories); OSV-Scanner (https://google.github.io/osv-scanner/).
- Tooling documentation: Playwright snapshot testing (https://playwright.dev/docs/test-snapshots); Deque axe rule index (https://dequeuniversity.com/rules/axe/); NVDA user guide (https://www.nvaccess.org/files/nvda/documentation/userGuide.html); Apple VoiceOver (https://www.apple.com/accessibility/voiceover/); Mozilla Observatory (https://observatory.mozilla.org/); HSTS preload list (https://hstspreload.org/); Astro sitemap integration (https://docs.astro.build/en/guides/integrations-guide/sitemap/); Partytown (https://partytown.builder.io/); npm registry records for `@lhci/cli` 0.15.1 and `web-vitals` 6.2.2.
- Data-protection law and regulators: GDPR, Regulation (EU) 2016/679 (https://eur-lex.europa.eu/eli/reg/2016/679/oj); Uganda Data Protection and Privacy Act 2019 (https://media.ulii.org/files/legislation/akn-ug-act-2019-9-eng-2019-05-03.pdf) and the Personal Data Protection Office (https://pdpo.go.ug); Kenya Data Protection Act 2019 and the Data Protection (General) Regulations 2021 (https://www.odpc.go.ke); South Africa's Information Regulator for POPIA (https://inforegulator.org.za); Nigeria Data Protection Commission (https://ndpc.gov.ng).
- Kenya advertising and endorsement rules: Consumer Protection Act 2012, Competition Act 2010, the ASBK Code, and the Media Council Code 2025 (Legal Notice 88 of 2025).
- Uganda public registers used to verify sector trust signals: URSB business registry, Uganda Tourism Board licensing, UNCHE, Ministry of Education private-schools register, Engineers Registration Board, ICPAU firms portal, the Judiciary advocates roll, NGO Bureau register, URA licensed agents, UMRA SACCO supervision, the Ministry of Trade cooperatives registry, the MLHUD land information system, the eHealth licence search, the government e-procurement supplier list, and the Uganda Communications Commission Q2 2026 market report.

### Websites and articles

- Research: METR (2025), "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; arXiv 2507.09089); Stack Overflow 2025 Developer Survey (https://survey.stackoverflow.co/2025/ai); Faros AI, "The AI Productivity Paradox" (https://www.faros.ai/ai-productivity-paradox); Schmitt, Skiera and Van den Bulte (2011), "Referral Programs and Customer Value", *Journal of Marketing* 75(1) (https://journals.sagepub.com/doi/10.1509/jm.75.1.46); Van den Bulte, Bayer, Skiera and Schmitt (2018), "How Customer Referral Programs Turn Social Capital into Economic Capital", *Journal of Marketing Research* (https://journals.sagepub.com/doi/10.1509/jmr.14.0653); Kahneman and Tversky (1979), "Prospect Theory: An Analysis of Decision under Risk", *Econometrica*; arXiv 2604.25707, "From Citation Selection to Citation Absorption"; arXiv 2607.14035, "Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023–2026)".
- AI search: Meltwater and LinkedIn (2026), *How LinkedIn Content Wins in AI Search* (report, https://www.meltwater.com/en/blog/linkedin-ai-visibility-study), and the LinkedIn Marketing Blog summary of 9.5 million citations.
- Connectivity and market data: Ookla Speedtest Global Index for Uganda and Kenya (https://www.speedtest.net/global-index/uganda, /kenya); GSMA, *State of the Industry Report on Mobile Money 2026*; DataReportal, *Digital 2026: Uganda* (https://datareportal.com/reports/digital-2026-uganda); MTN MoMo merchant information.
- Usability and trust: Nielsen Norman Group on trustworthy design and About-us information (https://www.nngroup.com/articles/trustworthy-design/, /about-us-information-on-websites/); Stanford Web Credibility guidelines (https://credibility.stanford.edu/guidelines/index.html); Baymard Institute on payment-method selection and perceived payment-form security (https://baymard.com/blog/).
- Positioning and agency practice: Win Without Pitching (https://winwithoutpitching.com); Philip Morgan's specialisation guide (https://philipmorgan.net/books-and-guides/specialization-guide/); the 2Bobs podcast on horizontal positioning; Haus Advisors; Epom; Tim Kilroy; Shortform on the smallest viable market; Instrument; Design Studio UI/UX articles on enterprise, dashboard, mobile and SaaS design; Eleken on design consistency and design-system checklists; Converge and Wavespace trend round-ups (treated as trend evidence only).
- Delivery and productisation (industry-reported, to be confirmed before stating as fact): ManyRequests, Wayfront, Assembly, GigRadar, Growth Rocket, Builts.ai, Futran Solutions, SAM Solutions, Buddy WDD, Webstacks, Bejamas, Kawn and Troy Web.
- Sales and acquisition: RAIN Group Center for Sales Research; HubSpot sales statistics; SPOTIO; SalesRabbit; SiteSwan; QCFixer; Selling Signals; Nutshell; SEOptimer; Insites; Jeb Blount's site; Joey Coleman's site.
- Referral programmes: GrowSurf, Referral Factory, Commsor, impact.com, Pipedrive, Tremendous, Viral Loops, Act! CRM, OpenPotion, Thrive Design, Studio1 Design, Kim Tasso, the Neighborly × TradeEngage release, the CFA Institute Standard VI(C) on referral fees, and InnReg on referral-programme compliance.
- Book publisher records: John Wiley & Sons listings for *The New Rules of AI Search* and *Search and Social*; Utah State University Press digital commons for *Keywords in Creative Writing*; Itamar Blauer's keywords page.
