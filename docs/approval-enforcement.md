# Approval enforcement adapter

Website release and content actions are catalogued in
[`approval-adapter.json`](approval-adapter.json) and are governed by the
shared contract from `skills-web-dev/docs/approval-contract.md`.

## Required release preview

The preview must include the URL and route list, changed content, canonical and
hreflang metadata, robots/sitemap/schema changes, links and images, forms and
webhooks, analytics/consent changes, accessibility findings, performance
evidence, deployment target, approved snapshot, rollback, and post-deploy
smoke checks. The deployed artifact must match the approved scope hash.

## Gated actions

Publishing, deploying, unpublishing, deleting assets or pages, changing
indexing controls, forms/webhooks, consent, analytics, or customer-facing
claims is L2/L3 and pauses for approval. High-risk claims, privacy/consent
changes, client content, and production analytics require the second reviewer
declared by policy.

## Stop conditions

Stop on missing render, accessibility, performance, security, rollback,
recipient, consent, or evidence checks. Correction, reject, undo, rollback,
and escalation must remain available. A local build is not permission to
publish. The host must route launch and deployment commands through the gate.

## Acceptance boundary

Drafts and local previews may be generated automatically. Production
publication, deployment, indexing changes, form routing, tracking changes, and
destructive content changes cannot proceed without a fresh approval.
