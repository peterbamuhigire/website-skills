# OKRs and Client Reporting

The agency runs two separate measurement systems. Confusing them makes both useless.

1. **Internal OKRs** set what the agency focuses on each quarter. Three to five objectives, visible to the team, never tied directly to pay.
2. **Client KPIs** show what each retainer delivered each month: an always-on dashboard with plain-English commentary.

If they are mixed, the team treats client metrics as goals (vanity) or treats OKRs as reporting (theatre). Kept apart, OKRs focus the agency and KPIs prove the retainer.

Pairs with `monthly-report-template.md` (client report), `retainer-package-catalog.md`, `post-launch-review-cadence.md` and `subscription-economy-model.md` (founder's recurring-revenue dashboard).

---

## 1. Internal OKRs

### Definition and test

- **Objective:** qualitative, significant, action-led, time-bound. It says what to achieve.
- **Key result (KR):** quantitative and verifiable. It says how you will know. Test: did we hit the number, yes or no? A KR needing interpretation is badly written.

Limit each cycle to three to five objectives and three to five KRs per objective. More turns focus into a to-do list.

### OKRs versus annual management by objectives

| Annual objectives model | OKRs |
|-------------------------|------|
| What only | What and how |
| Annual | Quarterly or monthly |
| Private, siloed | Public, transparent |
| Top-down | Roughly half bottom-up or sideways |
| Tied to pay | Mostly separate from pay |
| Risk-averse | Aspirational |

We run the right-hand column.

### Four working principles

1. **Focus.** Cap objectives; picking everything means picking nothing.
2. **Alignment.** Everyone's OKRs are visible; dependencies surface early.
3. **Tracking.** Living documents: weekly check-in, mid-cycle re-scope, end-of-cycle score from 0.0 to 1.0.
4. **Stretch.** Aspirational OKRs should average about 0.6 to 0.7. Routine 1.0 means the bar is too low.

### Committed versus aspirational

- **Committed:** must reach 1.0 (revenue, delivery, operations). A miss requires a post-mortem. Example: ship four client builds on time and to scope.
- **Aspirational:** expected 0.6 to 0.7; 0.4 or more is acceptable if direction was right. Example: become the default authority-website firm in your region.
- If aspirational OKRs reach 1.0 two quarters running, raise the bar.

### Quarterly cycle for a five-person agency

| When | Activity |
|------|----------|
| Two weeks before quarter | Founder drafts two or three company objectives; team drafts personal KRs bottom-up |
| One week before | Two-hour summit; agree company OKRs; each person agrees one personal objective aligned to one company objective |
| Quarter start | Post all OKRs in a shared workspace |
| Weekly (30 minutes) | Each person gives RAG status per KR and one blocker; no deep dives |
| Mid-quarter (week 6) | 90-minute re-scope: kill obsolete KRs, promote unexpected wins |
| Last week | Score 0.0 to 1.0; each owner writes a paragraph reflection per objective |
| First week of next quarter | Two-hour retrospective and kick-off |

Expect about two hours per week plus about six hours per quarter.

### Illustrative company OKRs (invented figures, UGX)

**Objective 1 (committed): lock in recurring revenue so retainer MRR covers fixed costs with margin.**

- KR1: grow active retainer MRR from UGX 12,000,000 to UGX 18,000,000.
- KR2: raise six-month retainer renewal rate from 70% to 90%.
- KR3: ship 12 monthly client reports with no missed deadlines.

**Objective 2 (aspirational): become the obvious choice for authority website systems in our target segment.**

- KR1: publish four cornerstone pages and eight pillar articles; raise organic sessions from 1,200 to 4,000 a month.
- KR2: secure two speaking slots where the target buyer attends.
- KR3: capture three case studies with a stated business outcome.

**Objective 3 (committed): productise delivery so a Foundation build ships in six weeks without the founder as bottleneck.**

- KR1: document the three-tier build playbook; every build this quarter follows it.
- KR2: cut founder hours per Foundation build from 40 to 20.
- KR3: post-launch satisfaction of 9/10 or higher on all builds.

Each team member writes one personal objective laddering to one of these. Three company plus five personal objectives is manageable and still ambitious.

### Writing a good key result

- Start the objective with a verb: launch, eliminate, establish.
- Write KRs as "from X to Y" or "N of N".
- Mix leading indicators (proposals sent, discovery calls booked) with lagging ones (revenue, retained clients). All lagging means no steering.
- Favour outputs (organic sessions) over inputs (posts published); activity alone becomes theatre.
- A KR is a result, not a task. "Write eight case studies" is a task. "Publish eight case studies and lift case-study-to-enquiry conversion from 1% to 3%" is a KR.

### Pitfalls

1. **Tying pay to OKR scores.** The main error: people sandbag. Let OKR history inform pay decisions, never determine them.
2. **Vanity metrics as KRs.** "Increase awareness" fails; "raise aided recall from 18% to 28% in a named market by a date" passes.
3. **Sandbagging.** Cure: explicit 0.7 target for aspirational OKRs.
4. **Theatre.** Writing OKRs, never checking in, scoring everything green. Cure: weekly cadence, public scores, written reflection.
5. **Too many.** Eleven priorities means none.
6. **Top-down only.** Imposed OKRs have no commitment; aim for about half bottom-up.
7. **Scores as punishment.** It kills risk-taking; scores are learning tools.
8. **Lagging-only indicators.**

### OKRs versus KPIs

- **KPIs** are health metrics: always-on, slow-moving (MRR, gross margin, satisfaction, uptime, churn, pipeline value, utilisation).
- **OKRs** are change metrics: quarter-specific, moving something from X to Y.

Rule of thumb: if you would report it monthly forever, it is a KPI. Rewrite a KR as a delta ("from X to Y by quarter end") or move it to the dashboard.

---

## 2. Client KPI reporting

The monthly client report (`monthly-report-template.md`) is a KPI dashboard with commentary. OKRs do not appear in it. It answers one question: did this retainer earn its fee this month?

### Eight standing blocks

Use the blocks relevant to the retainer's scope; keep the format identical so the client experience is consistent.

| Block | KPIs | Source |
|-------|------|--------|
| Traffic and visibility | Sessions, new users, channel mix, top landing pages, branded versus non-branded search share | Analytics |
| Rankings | Tracked keyword movement, share of voice against three competitors, featured-result wins | Search Console plus a rank tracker |
| Engagement | Engagement time, scroll depth, pages per session, bounce rate on key pages | Analytics |
| Conversion | Enquiry form submissions, qualified leads (agency-scored), quote requests, phone and WhatsApp clicks | Analytics plus CRM |
| Pipeline impact | Leads sourced, accepted by sales, opportunities created, revenue attributed | Client CRM |
| Technical health | Core Web Vitals, uptime, broken links, schema validity | Speed test plus crawler |
| Content shipped | Articles, case studies, pages published; internal links added | Project log |
| Next-month plan | Three priorities and what we will test | Commentary |

### Report rules (non-negotiable)

1. Every KPI carries a delta against last month and, where data exists, the same month last year. A number without comparison is not a KPI.
2. Commentary explains why a number moved, not just that it did. Example: "Organic traffic up 18%, driven by two new articles now on page one for the service cluster, adding about 740 sessions."
3. A section titled "What we changed" lists the activities behind the deltas: the proof the retainer earned its fee.
4. A section titled "What we recommend" proposes two or three bets for the next 30 days.
5. Write from the project log. No log entries means the report does not proceed; never fabricate.
6. Plain English. Say "the site loads 1.2 seconds faster on mobile, so fewer visitors leave before it appears", not "LCP improved 1.2 s".
7. Name the attribution method for every claim, for example "revenue attributed via first-touch page on form submissions matched to closed-won deals in your CRM". If you cannot name the method, do not make the claim.

### Separation rule

Never show the client the internal OKR scorecard. The client sees KPIs, commentary and recommendations. Internally we also see retainer-margin views, OKRs and continuous performance management (Section 3). Showing OKRs makes the relationship feel transactional; reading client KPIs as OKRs makes the team game client metrics instead of growing the agency.

### Thresholds that trigger action (starting values; tune per client)

| Event | Response |
|-------|----------|
| Traffic down over 25% month on month | Diagnostic email within 24 hours; call within three business days |
| Conversion rate down over 30% | Same protocol |
| Critical search event (de-indexing, target-query ranking down over 50%) | Diagnostic within one business day; recovery plan within three |
| Downtime over one hour | Immediate notice; post-incident report within 24 hours |
| Bounce rate on a key page over 80% | Flag in next report with hypothesis and test |
| CRM lead-quality score down two points | Raise at next call; investigate channel attribution |

These are operational health indicators, not OKRs. Crossing one means act, not score.

---

## 3. Continuous performance management: conversations, feedback, recognition

Replace the annual review with frequent short loops.

- **Weekly one-to-one** (30 minutes): KR status, blockers, one piece of feedback each way, one career thought. No forms.
- **Peer feedback and recognition channel:** a kudos channel; feedback delivered within 72 hours of the work, in person or in a thread.
- **Monthly retrospective** (one hour): what went well, what did not, what to change; ten minutes per column. Record decisions in the project log.
- **Quarterly growth conversation** (60 minutes), separate from OKR scoring: which capability to build, and how the founder supports it.
- **No annual review.** Review pay on its own annual cycle, informed by OKR history.

**Anti-theatre rules:** no ratings or stack-ranking; no 360 surveys; no self-assessment forms (the OKR reflection is the self-assessment); no HR software at five people. Add structure (review schedule, role-based KR templates, capacity tooling) beyond about 12 staff.

---

## 4. Founder's monthly dashboard

Beyond client KPIs and internal OKRs, the founder reads the agency as a recurring-revenue business (definitions in `subscription-economy-model.md`).

| Metric | Starting target | Cadence |
|--------|-----------------|---------|
| Active retainer MRR | Rising quarter on quarter | Weekly |
| Net new retainer ARR | Quarterly target by tier | Weekly |
| Logo churn | Under 5% per quarter | Weekly |
| Revenue churn | Under 5% per quarter | Weekly |
| Net revenue retention | 110% or more | Quarterly |
| Gross revenue retention | 90% or more | Quarterly |
| ARPA | Rising annually | Quarterly |
| Growth efficiency (S&M spend per unit of new ARR) | Track the trend | Quarterly |
| LTV:CAC | 3:1 or better | Quarterly |
| Recurring profit margin | 60%+ | Monthly |
| Build pipeline value | 90 days of capacity covered | Weekly |
| 12-month renewal rate | 90% or more | Annually |
| Clients on two or more retainers | Rising | Quarterly |

This dashboard informs which OKRs to set each quarter.

---

## 5. Summary

Two systems, never mixed. Client KPIs: monthly, plain English, with deltas, named attribution and recommendations. Internal OKRs: quarterly, team-visible, three to five objectives, mixed committed and aspirational, scored 0.0 to 1.0 with written reflection, never tied directly to pay. Performance management runs on weekly one-to-ones, prompt feedback, recognition and quarterly growth talks. The founder adds a third view, the recurring-revenue dashboard. Three views, one operating system.

Short lines for team materials (write your own): execution matters more than ideas; focus on everything and you focus on nothing; feedback works best soon after the work; OKRs pace the team, they are not a performance-review document; reflection turns experience into learning; what gets measured gets managed.

---

## Sources

- Doerr, John (2018) *Measure What Matters*, Portfolio. Informed the objectives-and-key-results method, the committed/aspirational scoring approach and the continuous-feedback model.
- Tzuo, Tien, with Gabe Weisert (2018) *Subscribed*, Portfolio. Informed the founder's recurring-revenue dashboard.
