# Automation-Opportunity Audit

**Purpose**: Find which parts of delivery to automate or templatise, prioritise by
return, and roll them out without breaking delivery.

**Read this when**: deciding what to systematise next. Assumes you have read
`delivery-automation/SKILL.md`.

---

## The four-step audit

1. **Inventory every repeatable process.** List each step from sale to launch and
   beyond: onboarding, intake, content collection, design, build, QA, deploy,
   reporting, invoicing, status updates. Be granular.
2. **Time it for a week.** Track the actual hours each step consumes across live
   projects. Honest interviews with whoever does the work plus a timer cover most
   of what matters — you don't need elaborate tooling.
3. **Cost it.** Multiply time by loaded cost, and note error-proneness and how
   many systems the step touches.
4. **Score and rank** each step by:

   **Priority = Volume × Time × Frequency × Complexity**

   - **Volume** — how many projects/clients hit this step.
   - **Time** — hours per occurrence.
   - **Frequency** — how often it recurs.
   - **Complexity** — how error-prone or multi-system it is.

   A task done 100× a day returns far more from automation than one done monthly.

## What to automate vs systematise vs leave

- **Automate** repetitive, rule-based, high-volume steps: status updates, task
  assignment, reminders, onboarding emails, invoicing, report generation,
  deploy/QA checks.
- **Templatise / systematise** judgment-light but variable steps: intake (with
  conditional logic), briefs, proposals, design starting points.
- **Leave to humans** anything requiring real judgment, taste, or relationship.
  Heuristic: **"If the task requires judgment, hire. If it's repetitive and
  rule-based, automate it first."**

## High-return categories for a web studio

- **Starter kits / boilerplates** — a repo with auth, layout, and components
  pre-wired cuts the cold-start on every project.
- **Design system / tokens** — reusable components and machine-readable tokens
  (CSS variables / JSON) cut build time and rework (`design-system`).
- **Conditional intake forms** — questions adapt to service type; capture files,
  context, and brand assets once (`form-ux-design`).
- **QA / deploy automation** — the canonical CI gates run automatically (`deploy`).
- **Reporting automation** — monthly client reports generated from live data
  (`monthly-report`).
- **Content pipeline** — structured collection and placement of client copy/images.

## Roll out: pilot, measure, expand

- **Start with one.** Implement a single automation properly, measure the impact
  (hours saved, errors avoided), and train the team before adding the next.
- **Measure the right thing.** The metric is delivery hours saved at held quality,
  not number of tools built. If quality drops or a gate starts failing, the
  automation is not done.
- **Document each automation** as it ships (see `productized-delivery-sops.md`) so
  it survives staff changes and stays handover-safe.

## Sources

See `sources.md`. The four-step audit and "spreadsheet + timer" point draw on
Builts.ai; the Volume/Frequency prioritisation and automate-vs-hire heuristic on
Futran Solutions and ManyRequests; the high-return categories on the productized-
service literature (ManyRequests, Wayfront, Assembly).
