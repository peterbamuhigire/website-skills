# Phase 6 - Delivery, QA, and Launch Operations

## Objective

Build the launch discipline that premium agencies need: quality gates, technical verification,
deployment reliability, content readiness checks, and post-launch stability.

## Why This Phase Matters

The analysis repeatedly identifies operational gaps around deployment, CI/CD, infrastructure,
testing, and observability. For a website agency, those gaps do not need enterprise-scale cloud
complexity on day one, but they do need to be closed enough that launches are safe, repeatable,
and credible.

Premium agencies do not improvise launches.

## Core Outcomes

- define a launch-ready technical baseline
- implement repeatable QA and testing standards
- create robust deployment and rollback procedures
- make monitoring and issue detection part of the delivery model

## Workstreams

### 1. Pre-launch quality system

Create a mandatory QA matrix covering:

- responsive behavior
- content completeness
- link integrity
- performance
- accessibility
- SEO implementation
- analytics events
- form handling
- browser verification

### 2. Build verification and E2E coverage

For the repository itself, this phase should add or sharpen:

- build verification scripts
- smoke testing
- Playwright-based E2E coverage for core flows
- checklists for forms, language switching, and navigation

### 3. Deployment standard

Create the standard deployment model for agency websites:

- hosting patterns you support
- DNS and SSL checklist
- environment variable management
- staging to production promotion
- rollback procedure
- post-launch validation routine

### 4. Operational observability

For premium delivery, you need enough monitoring to avoid blind launches.

Minimum standard:

- uptime checks
- form delivery verification
- analytics verification
- error logging for scripts and forms
- post-launch review window

If the agency expands into more dynamic builds, this phase should then connect to the broader
analysis recommendations around:

- CI/CD pipelines
- observability platform
- infrastructure-as-code

### 5. Launch ritual and post-launch care

Standardize:

- launch-day checklist
- client approval confirmation
- launch communication template
- 7-day post-launch review
- 30-day performance review

## Repository Outputs Required

- QA checklist
- pre-launch verification checklist
- deployment runbook
- rollback runbook
- E2E test starter for website projects
- post-launch review checklist

## Success Criteria

- every website can be launched with a repeatable checklist
- testing covers the flows clients actually care about
- failed forms, broken links, and missing metadata are caught before launch
- the repository begins to close its deployment and testing weaknesses
- clients experience launches as controlled, not chaotic

## Risks to Avoid

- treating manual spot-checking as enough
- launching without rollback planning
- having no defined browser and device verification standard
- shipping analytics or forms untested
- assuming static websites do not need operations discipline

## Reading Material To Buy And Provide At This Stage

- *Continuous Delivery* by Jez Humble and David Farley: release discipline and deployment thinking
- *The DevOps Handbook* by Gene Kim, Jez Humble, Patrick Debois, and John Willis: practical operational systems
- *Testing JavaScript Applications* by Lucas da Costa: usable testing depth for front-end and flows
- *Observability Engineering* by Charity Majors, Liz Fong-Jones, and George Miranda: monitoring and feedback loops
