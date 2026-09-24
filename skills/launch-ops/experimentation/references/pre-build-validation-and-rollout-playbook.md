# Pre-Build Validation and Rollout Playbook

Parent skill: [experimentation](../SKILL.md). Read when an idea, feature, offer or new site section has not yet been built and the team must prove demand before spending design or engineering effort, or when choosing how to release a finished change safely.

Use with `hypothesis-template.md` (write the hypothesis first), `stat-significance-primer.md` (sample size and reading results) and `../../../orchestration/website-experience-mapping/references/validation-research-method-playbook.md` (interview and usability methods).

## 1. Validate in three layers, in order

| Layer | Question | Evidence that passes |
|---|---|---|
| Problem | Does a real, recurring pain exist? | The same specific complaint is heard repeatedly from one identifiable type of person. |
| Market | Who has this pain badly enough to pay? | You can predict that a narrowly defined group has the problem (for example, "owners of clinics with two to five doctors who do their own billing", not "doctors"). |
| Product | Does this solution remove the pain for that market? | A meaningful share of the target market offers money, time or contact details for the solution. |

Rules:

- Do not start with a product idea. Start by observing a market and finding pain.
- Narrow the market until its problems are uniform enough for a small first product to solve.
- The product layer takes longest. Keep asking whether the product solves the identified problem for the specified market.

## 2. Treat every feature as a hypothesis

- Rewrite feature requests as hypotheses: "We believe [change] will move [metric] for [segment] because [reason]. We will know when [measurable signal]."
- A feature is finished only when it has been validated or invalidated against its metric, not when it ships.
- Decide how success will be measured before any design work begins. A change with no pre-agreed metric teaches nothing.
- Where a controlled test is impossible (support tools, internal admin screens), choose a proxy metric in advance (support contacts on the topic, time to complete a task).

## 3. Cheapest-first validation ladder

Climb only as far as needed. Each rung costs more than the last; stop as soon as the evidence is decisive.

| Rung | What you build | What it proves | Watch for |
|---|---|---|---|
| 1. Landing page or smoke test | One page describing the offer with a single action (pre-order, register interest, book a call) | Whether the promise attracts action from the target segment | Traffic source must match the segment; count actions, not visits |
| 2. Explainer or demonstration | A short video or walkthrough of how the product would work | Whether the concept is understood and wanted before it exists | Measure sign-ups after viewing, not views |
| 3. Concierge / Wizard of Oz | The outcome delivered manually behind a simple front end (staff fulfil orders, match requests or compile results by hand) | Whether users value the outcome enough to justify automation | Keep it small; be honest in terms and privacy notices about manual handling |
| 4. Feature stub (fake door) | A button, menu item or price page for a feature that does not exist yet, leading to a "coming soon / tell me when ready" message | Whether existing users try to use the feature | Show the stub to a limited share; never take payment for something that does not exist |
| 5. Interactive prototype | A clickable, rough version tested with target users | Whether the design lets people complete the task | See the prototype rules in the research playbook |
| 6. First iteration | Only the core benefit the landing page promised | Whether real use delivers the promised value | Resist "one more feature" before launch |

Rules:

- Avoid engineering for as long as the lower rungs can answer the question.
- Skip a rung when building the real thing would take about as long as testing the rung, and it can be rolled back cheaply.
- If the rung produces no response, stop building and return to problem discovery.

### Limited versus poor first versions

A first version must be minimum and viable. Check it against this table before launch:

| Acceptable (limited) | Unacceptable (poor) |
|---|---|
| Does a few things well | Attempts many things, none well |
| User understands what to do | User cannot work out how to use it |
| Stable | Unreliable |
| Clear scope | Feature-bloated |

## 4. Landing-page experiment procedure

1. **Define the experiment.** Name the part of the customer experience under test and how it maps to the value proposition. State whether you are testing the proposition, a pivot, or lead acquisition.
2. **Build the page.** One key action. The proposition must land within the time of a short advert: headline, one image or video, the offer, the action. Plan the thank-you page with a clear next step; offer a phone or WhatsApp contact for cautious buyers.
3. **Build variants.** Vary one thing per variant: the proposition, the feature emphasised, the copy, or the pattern.
4. **Run a bounded campaign.** Fix in advance: budget ceiling, keywords or audiences, advert copy, demographic and location targeting, start and end dates (typically a week or less).
5. **Measure validated learnings.** Click-through rate, conversion rate, cost per conversion, and share or referral rate. Record results in the experiment logbook.

Check current advertising platform rules and costs before quoting a budget to a client; do not reuse historical cost-per-click figures.

## 5. Solution prototype for a product that does not exist

When only a storyboard exists, build the smallest set of screens that demonstrates the key experience, the value proposition and a glimpse of the business model:

| Screen group | Shows |
|---|---|
| 1. Set-up | Landing page or user dashboard: where the user starts |
| 2. Key interaction A (one to three screens) | The main interaction that delivers the new value |
| 3. Key interaction B (one to three screens) | A second interaction that carries value |
| 4. Value delivered | The end state of a successful transaction |
| 5. Pricing (if relevant) | Price, plans, packages or how the business earns |

Procedure:

1. List the screens as a simple outline.
2. Assemble screens quickly from existing imagery and adapted patterns so the prototype feels real; do not design new UI at this stage.
3. Put the screens into a shareable clickable format that participants can move through at their own pace on a phone or tablet.
4. Test with target users. A prototype that teaches the team nothing was wasted effort.

## 6. Funnel matrix: design for conversion at each engagement level

Build a matrix before designing screens. One row per engagement level; four columns.

| Level | User process | Business task | Required functionality | Validated learning (measurable question) |
|---|---|---|---|---|
| Suspect (might arrive) | | | | e.g. What share of traffic came from search versus social? |
| Lead (gave contact details or first interaction) | | | | e.g. What share of visitors submitted the form? |
| Prospect (engaged with the product) | | | | e.g. What share returned within seven days? |
| Customer (bought, booked, signed up) | | | | e.g. What was the cost per customer? |
| Reference (recommends publicly) | | | | e.g. What share shared or referred? |

Rules:

- Every learning question must be answerable with a number. "How intrigued were visitors?" fails; "What share scrolled to pricing?" passes.
- Triage each item of required functionality on three questions: how many users will use it (user value), how hard it is to build (effort), and whether it differentiates or is a gimmick (business value).
- Revisit the matrix after every release; it is a build-measure-learn instrument, not a one-off document.

## 7. Choose qualitative or quantitative evidence

| Situation | Evidence route |
|---|---|
| Single-variable change (button text, position, colour) | Ship behind an A/B test; qualitative testing adds little |
| Small change produces a surprisingly large swing | Watch a few recorded sessions to rule out a bug before celebrating |
| Multi-part new feature or complex flow | Qualitative prototype testing first, then A/B test the survivors |
| Two substantially different design approaches | Qualitative testing to narrow to one or two, then A/B |
| Why people drop out of a funnel | Qualitative (sessions, interviews) |
| Whether people will buy | Behavioural test only (landing page, stub, real checkout); never ask |
| What to build next | Quantitative: features used most by the highest-value customers, stub clicks. Qualitative: where current users struggle, why lapsed users left, what new users expected in their first 15 minutes |

Combined sequence: qualitative research to understand the problem, qualitative prototype tests to remove broken approaches, A/B test the one or two survivors, then use the A/B results to decide what the next qualitative round should investigate.

## 8. Measure user value with a basket of metrics

No single metric proves users are better off. Each can be distorted:

| Metric | Distortion to watch |
|---|---|
| Retention | Contracts and switching barriers keep unhappy users |
| Revenue | Hidden fees and surprise renewals inflate it briefly |
| Satisfaction or recommendation score | Response bias and small samples |
| Conversion to paid | Says nothing about paying users' satisfaction |
| Engagement | Can be gamed; in utility products high engagement may mean the task is too hard |
| Registrations | Measured before users experience value |
| Support contacts | Fall when support is made harder to reach |

Rule: judge a release by consistent positive movement across several of these, tied back to the business goal.

## 9. A/B pitfalls to check before declaring a result

- A test compares only the options you put in; two weak designs yield the less weak one. Good design work must come first.
- Check significance and sample size (see `stat-significance-primer.md`); a handful of conversions either way is noise.
- Watch effects over time: a discount that lifts this week's revenue may depress next month's.
- Trace every metric back to its business goal; a rise in visits without a rise in enquiries or sales is a vanity result.
- Do not combine winners from separate tests without testing the combination against control; individually winning elements can clash.
- Pre-state the expected effect. Account for seasonality, campaigns, launches and outside events before attributing a change.

## 10. Release strategies

| Strategy | How | Best for | Weakness |
|---|---|---|---|
| Prototype only | Test the change outside production | Large changes; catching obvious problems before code | Not real behaviour |
| Opt-in | Invite users who want early access | Gauging reaction from the most change-tolerant users | If they dislike it, others will dislike it more |
| Opt-out | Release to all with a visible "switch back" | Measuring rejection: a small vocal minority is normal; a large reversion rate signals an unsolved problem | Some users never discover the switch |
| Percentage rollout | Release to a small share, check for failures and extreme reactions, then widen for a proper A/B test | Technical and behavioural risk control | Needs feature-flag infrastructure (see `ab-infrastructure.md`) |
| New users only | Show the change only to new sign-ups | Acquisition and first-impression changes; clean cohorts | Existing users may react differently; data takes longer to accumulate |

## Sources

- Klein, L. (2013) *UX for Lean Startups: Faster, Smarter User Experience Research and Design*. O'Reilly Media.
- Levy, J. (2015) *UX Strategy: How to Devise Innovative Digital Products that People Want*. O'Reilly Media.
