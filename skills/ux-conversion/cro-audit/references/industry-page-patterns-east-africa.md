# Industry Page Patterns: East Africa

**Read this when**: planning the page order, primary call to action and trust
block for a client in one of the sectors below, or auditing an existing site in
that sector against what its visitors need to see first.

**Scope**: page order, conversion and trust only. Visual treatment (type,
colour, imagery, density) belongs to the design engine's
`skills/06-sector-and-domain-ux/sector-strategies/SKILL.md`; the "Design pointer" column
names what to ask it for. Uganda is the primary market; Kenya notes are one
line where they were checked. The table shape (sector, visitor job, section
order, CTA, trust) takes its idea from UI UX Pro Max (MIT,
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, commit 09170ee); no
row, pattern name or wording comes from it. The content is original to this
engine.

## How to use a row

1. Start from the visitor job. If the brief's audience research contradicts
   it, the brief wins; record why.
2. Use the section order as the default for the home page or the sector's main
   landing page. Every section still needs approved content; do not invent
   proof to fill a slot.
3. Show only the trust signals the client really holds, with the number and
   the issuing body, and link to the public register where one exists.
   Recheck every regulatory claim by its recheck date (90-day currentness
   rule, `digital-research-engine`), and again before launch.
4. A row marked `NOT_ASSESSED` in the evidence column gives a starting
   hypothesis only.

## Evidence base

Every row cites at least one of these. Grades follow the digital research
engine's `source-evaluation` skill (Tier 1 primary to Tier 5 unvetted; all
regulatory claims are time-sensitive). All were checked on 2026-09-29.

| Key | Source | Grade |
|---|---|---|
| E-TRUST | Harley, A., "Trustworthiness in Web Design: 4 Credibility Factors", Nielsen Norman Group, 8 May 2016, https://www.nngroup.com/articles/trustworthy-design/ | Tier 3; stable principle, Western samples |
| E-ABOUT | Kaley, A. and Nielsen, J., "About Us Information on Websites", Nielsen Norman Group, 26 May 2019, https://www.nngroup.com/articles/about-us-information-on-websites/ | Tier 3; stable |
| E-FOGG | Fogg, B.J., Stanford Guidelines for Web Credibility, Stanford Persuasive Technology Lab, May 2002, https://credibility.stanford.edu/guidelines/index.html | Tier 2; dated, durable principles only |
| E-PAY | Holst, J., "How Users Perceive Security During the Checkout Flow", Baymard Institute (updated 2025), https://baymard.com/blog/perceived-security-of-payment-form; Scott, E., "Payment Method UX", Baymard Institute, 5 Sep 2023, https://baymard.com/blog/payment-method-selection | Tier 3; card-based samples |
| E-MOMO | GSMA, State of the Industry Report on Mobile Money 2026, 1 Apr 2026, https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/gsma_resources/the-state-of-the-industry-report-on-mobile-money-2026/ | Tier 2; headline figures verified |
| E-REACH | Kemp, S., Digital 2026: Uganda, DataReportal, 8 Nov 2025, https://datareportal.com/reports/digital-2026-uganda (22.0% internet penetration; 91.6% of cellular connections 3G or better) | Tier 2/3 |
| E-WA | Uganda Communications Commission, Market Performance Report Q2 2026, https://www.ucc.co.ug/wp-content/uploads/2026/08/UCC-Market-Report-for-Q2-2026-Jun-2026.pdf, as reported by PC Tech Magazine, 20 Aug 2026 (WhatsApp 11.0m subscriptions) | Tier 3; primary figure not yet read by hand |
| I-TRUST | This engine: `skills/orchestration/africa-excellence/references/africa-trust-signals.md` (Uganda "rule of currency": registration number, TIN, street address, tested phone and email) | Internal Chwezi record, last changed 2026-05-22 |
| I-HOSP | This engine: `docs/continuous-improvement/hospitality-hotel-restaurant-kaizen-2026-09-14.md` (task-first hospitality IA with verified facts, rates and policies) | Internal Chwezi record, 2026-09-14 |
| I-NET | This engine: `skills/launch-ops/deploy/references/africa-calibration.md` (network profile, data cost, device reality) | Internal Chwezi record |

Regulator sources are cited in each row (all Tier 1 unless stated).

## Sector table

| Sector | Primary visitor job | Section order (home or main landing page) | Primary CTA and placement | Trust signals to show (verify; never assume) | East African context | Evidence, checked 2026-09-29 (recheck by) | Design pointer |
|---|---|---|---|---|---|---|---|
| Hotel, lodge, restaurant | Check the room or table is right, see the real price, and book or reserve | Rooms or menu with prices → availability and rates → location with landmark directions → policies (check-in, cancellation, children, deposits) → guest reviews → contact | "Check availability" or "Reserve a table" in the first screen and on every room or menu page; WhatsApp as the second channel | UTB licence number (format `UTB/AFC/<category>/<year>/<no.>`), linked to the UTB licensed-accommodation list; accepted payment rails; named manager | Many bookings start on WhatsApp or a phone call; show both beside the form. Deposits by mobile money need the merchant name the guest will see | I-HOSP; E-TRUST; UTB licensing notice https://utb.go.ug/registration-and-licensing-of-tourism-facilities-and-services-in-uganda/ and list https://qasystem.utb.go.ug/display-licenced/accommodation (restaurant list not found: partial) (2026-12-28) | Hospitality photography and warmth; ask `sector-strategies` for the hospitality profile |
| Private clinic or hospital | Find whether this facility treats my problem, when it is open, and how to get seen today | Services by condition → hours and emergency line → doctors with specialities → fees or fee guidance → insurers accepted → location and directions → booking | "Call now" (tap-to-call) above the fold on mobile; "Book an appointment" second; emergency number repeated in the footer | UMDPC facility operating licence number and each doctor's practising licence, verifiable at https://ehealthlicense.go.ug/index.php/search; insurers accepted | Visitors often search in a hurry on a phone with little data; the phone number must work in the first screen (I-NET). Kenya: KMPDC licenses facilities (snippet only) | UMDPC https://www.umdpc.go.ug/; eHealth licence search; E-FOGG (make facts verifiable); I-TRUST (2026-12-28) | Calm, high-legibility clinical profile; no decorative imagery near the emergency line |
| School or university | Decide whether this school fits my child or this programme fits me, what it costs, and how to apply | Programmes or classes → admission requirements and deadlines → fees and payment schedule → accreditation → campus life and results → how to apply → contact | "Apply" or "Book a visit" in the header and after fees; admissions WhatsApp line | Schools: Ministry of Education and Sports registration or licence (downloadable lists only: partial). Universities: NCHE licence or charter and each programme's accreditation, linked to https://unche.or.ug/all-academic-programs/ | Parents compare fees and payment plans first; show fees in UGX with instalment dates. Programme accreditation is the most-checked claim for tertiary | NCHE https://unche.or.ug/ (verified); MoES https://www.education.go.ug/private-schools-institutions/ (partial); E-ABOUT (2026-12-28) | Institutional profile; ask for the education profile |
| NGO or nonprofit | Decide whether this organisation is real and effective enough to fund, partner with or join | Mission in one sentence → programmes with places and numbers served → results with dates → governance (board, audited accounts) → partners and funders → donate or partner → contact | "Partner with us" or "Donate" after results, not before; volunteer route secondary | National Bureau for NGOs registration number and current operating permit (register page partial); audited accounts; named board | Funders and partners check registration and accounts before anything else; show the permit's validity dates | NGO Bureau register https://ngobureau.go.ug/en/updated-national-ngo-register (partial: table did not render); E-TRUST (disclosure); E-FOGG (2026-12-28) | Documentary photography of real programmes; no stock "helping hands" |
| SACCO or microfinance | Decide whether my savings are safe here, and how to join or borrow | Who can join → savings and loan products with rates and fees → how to join (documents) → licence and supervision → branches and agents → member stories → contact | "Become a member" after the products; branch and agent finder second | **`NOT_ASSESSED`**: regulator in transition. UMRA licenses Tier 4 SACCOs, but Parliament approved folding UMRA into the Ministry of Finance on 6 Nov 2024 (assent unconfirmed); large SACCOs move to Bank of Uganda licensing (deadline reported as 30 Sep 2026). Show whichever licence the client holds today, with its issuer | Members compare interest and fees and ask about mobile-money deposits; show rates as annual percentages with every fee | **`NOT_ASSESSED`** for the regulatory column (contested). UMRA https://umra.go.ug/licensing-regulation-and-supervision-of-saccos-in-uganda/; Parliament of Uganda news, 7 Nov 2024; *The Cooperator*, 21 Sep 2026 (recheck 2026-10-06). Not counted towards the ten | Trustworthy, plain financial profile; no gradients |
| Professional services (law, audit, consultancy) | Decide whether this firm can handle my matter and who will do the work | Practice areas → named partners with qualifications → selected matters or clients (with permission) → how engagements work and fees basis → contact | "Book a consultation" on every practice-area page; direct partner email or phone | Audit firms: ICPAU firm licence number (for example `L227/26`), verifiable at https://icpauportal.com/index.php/external_portal/firms. Law firms: each advocate's current Law Council practising certificate (expires 1 March) and ULS membership. Consultancies: URSB registration; e-GP supplier number if bidding for government work | Buyers want the named person, not the brand; a named partner with photo is expected (I-TRUST cultural patterns) | ICPAU register (verified); Judiciary advocates page https://judiciary.go.ug/data/ladvocates/106/Advocates.html (partial); E-ABOUT; I-TRUST (2026-12-28) | Restrained editorial profile |
| Agribusiness or cooperative | Buyers: can this supplier deliver the volume and grade I need; farmers: how do I join and get paid | Products with grades and seasons → capacity and certifications → where we source and how farmers are paid → buyer enquiry → member or farmer route → contact | "Request a quote" for buyers; "Join the cooperative" as a separate path | Cooperative society registration number from the Registrar of Cooperatives (MTIC); **public registry `NOT_ASSESSED`** (the online system was a test address); export or quality certificates held | Farmer members are often reached by phone, SMS or radio rather than the web; keep the farmer path short and phone-first (I-NET) | MTIC https://www.mtic.go.ug/cooperatives-registration/ (registry unverified); **`NOT_ASSESSED`** for trust signals; not counted towards the ten (2026-12-28) | Earthy, documentary profile; real produce photography |
| Real estate | Find a property or plot that fits my budget and check that the title is real | Listings with price and location filters → each listing's title type and status → how viewing and payment work → title verification route → agent contact | "Book a viewing" on each listing; WhatsApp enquiry with the listing reference | No agent licensing regime is in force in Uganda (a Real Estate Bill is being fast-tracked); show URSB registration and invite buyers to verify titles through the Ministry of Lands UgNLIS portal https://ugnlis.mlhud.go.ug/public | Title fraud is the buyer's main fear; explain title types (freehold, mailo, leasehold) and the verification step before the price | MLHUD UgNLIS https://mlhud.go.ug/ugnlis/ (verified); Monitor, 11 Sep 2026 (Tier 3) on the Bill; E-FOGG (2026-12-28) | Listing-first layout; ask for the property profile |
| Tour and safari operator | Decide whether this operator is licensed and safe, and what a trip really costs | Signature trips with duration and price from → what is included and excluded → licence and memberships → guides and vehicles → reviews → enquire | "Plan my trip" or "Enquire" on each itinerary; WhatsApp for fast questions | UTB tour-operator licence number, linked to https://qasystem.utb.go.ug/display-licenced/tour-operators; AUTO membership (voluntary; directory partial); gorilla-permit handling stated honestly | International visitors check licensing and reviews before paying a deposit; show prices in USD with what the price includes; local visitors need UGX | UTB tour-operator list (verified); E-TRUST; E-PAY (2026-12-28) | Wildlife and landscape photography of the operator's own trips |
| Retail or e-commerce with mobile money | Find the product, see the full price with delivery, and pay safely | Categories and search → product with price and stock → delivery areas, times and fees → payment methods → returns → contact | "Add to cart" on the product; the pay button names the method ("Pay with MTN MoMo") | URSB registration number; MTN MoMoPay 6-digit merchant code and the merchant name the payer will see; Airtel Money Pay code (format unverified); physical shop address | Mobile money is the default rail (E-MOMO); buyers fear paying before delivery, so state pay-on-delivery rules plainly. A TIN on the site is a disclosure, not a checkable credential | MTN MoMo merchant page https://www.mtn.co.ug/momo/merchant/ (verified); URSB search https://obrs.ursb.go.ug/search; E-PAY; E-MOMO (2026-12-28) | Product-first commerce profile |
| Logistics and transport | Get a quote and know when my goods will arrive and who is accountable | Services (clearing, freight, local delivery) → routes and transit times → how to get a quote → tracking → licences → contact | "Get a quote" in the first screen; tracking lookup second | URA licence for clearing agents (list page partial); operator licences from the Ministry of Works and Transport (public check `NOT_ASSESSED`); insurance cover | Cross-border routes (Mombasa, Malaba, Busia) and transit times are the buyer's first question | URA licensed agents page https://ura.go.ug/en/choose-agents/licensed-import-export-tax-agents/ (partial); E-TRUST (2026-12-28) | Operational, data-dense profile |
| Construction and engineering | Decide whether this contractor can deliver my project safely, on time and to specification | Project types → completed projects with client, value band and year → engineers and registrations → safety and quality → how tendering works → contact | "Request a site visit" or "Invite us to tender" after the projects | ERB registration numbers for named engineers (ERB Register 2026, https://www.erb.go.ug/erb-register/); e-GP supplier reference, verifiable at https://egpuganda.go.ug/suppliers; UNABSEC (formerly UNABCEC) membership, voluntary | Public-sector buyers check e-GP registration and past contracts; show project photographs with dates | ERB (verified, individuals only); PPDA e-GP (verified); E-FOGG (2026-12-28) | Project photography; ask for the construction profile |

Rows with a non-`NOT_ASSESSED` evidence source: 10 (all except SACCO or
microfinance and agribusiness or cooperative, whose regulatory columns could
not be verified on 2026-09-29).

## Kenya notes (snippet-level; verify before use)

- Tourism: Tourism Regulatory Authority. Health facilities: KMPDC. SACCOs:
  SASRA publishes an annual list of licensed SACCOs. Audit firms: ICPAK firm
  search. NGOs: the Public Benefit Organisations Regulatory Authority replaced
  the NGO Coordination Board in May 2024. Construction: National Construction
  Authority contractor search.

## Open items

- Read the UCC Q2 2026 chart by hand before citing WhatsApp figures (E-WA).
- Recheck the SACCO row after the 30 September 2026 Bank of Uganda deadline
  and when UMRA's dissolution is gazetted.
- Replace "partial" register links when the NGO Bureau, URA and MTIC pages
  render their lists.
- Add rows from Peter's own client projects (project-log decisions) as they
  close; a client-work record outranks a general source for page order.
