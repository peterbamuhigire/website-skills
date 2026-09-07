# First-wave website journey fixture

Status: IMPLEMENTED FIXTURE SPECIFICATION, not a completed client build. Date: 7 September 2026.

This bounded fixture operationalises W01–W04. It is content-neutral: no client names, performance results, market claims or invented proof are included.

## Required packet

1. Approved or explicitly fictional brief with audience, page job, primary action, authority and gaps.
2. Route/action map using `skills/orchestration/website-experience-mapping/SKILL.md`.
3. Claim/proof register with source, permission and status.
4. Page implementation record using `skills/build/page-builder/SKILL.md`.
5. Render, keyboard, form-error and event traces, each labelled `REAL`, `FICTIONAL` or `NOT_ASSESSED`.
6. Reviewer decision and handoff owner.

## Normal and negative cases

Normal: approved content renders, the primary action is reachable, a valid form records one authorised event, and handoff names the next operator. Negative: missing proof, duplicate event, long-copy overflow, form timeout, unavailable render or ownerless approval. A negative case blocks release and records the owning skill.

This file defines evidence collection; it does not prove browser behaviour, accessibility, security, conversion, deployment or client value until a completed packet is attached.
