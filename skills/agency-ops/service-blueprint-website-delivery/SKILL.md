---
name: service-blueprint-website-delivery
description: Use when mapping frontstage and backstage website-delivery operations, owners, promises, fail points, SLAs, and recovery across discovery through retainer. Use `website-experience-mapping` for the customer journey and `customer-service-website-ops` for live support.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Service Blueprint Website Delivery
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Pricing or scoping a premium engagement and the operational cost of delivery must be visible.
- A website's promise depends on backstage operations the agency or client must change to honour.
- Retainer or maintenance commitments need explicit SLAs, evidence, and recovery procedures.
- Onboarding a new client and the operating rhythm must be agreed before design starts.
- A delivery is at risk and the cause is operational, not design or technical.

## Do Not Use When

- The work is a single deterministic implementation with no ongoing service component.
- The client refuses to discuss operations and expects the agency to absorb unbounded service work.

## Inputs

- The future-state customer experience map or proposal scope.
- Agency capacity, roles, and rates.
- Client side decision rights, content owners, and approval cadence.
- SLAs implied by the website (response time on contact form, quote turnaround, support window, refund policy).
- Tooling and systems for project management, content review, deployment, monitoring, and support.

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Experience map or approved scope | Client and upstream planning | yes | Stop and map the customer outcome first. |
| Roles, decision rights, capacity, costs | Agency and client operations | yes | Mark ownership and costing unresolved; do not promise SLAs. |
| Website claims and obligations | Content, proposal, and contract | yes | Inventory claims before blueprint approval. |

## Workflow

1. Lay out the lanes: customer actions, frontstage evidence (what the customer sees), frontstage staff (agency + client people the customer meets), backstage staff (people who never appear), support processes, systems.
2. Walk the engagement phases across the lanes: discovery, strategy, content, design, build, QA, launch, observability, retainer.
3. Identify each website promise and trace it to the lane that must keep it. Examples: "We respond within one business day" depends on a backstage triage rota; "Photos of real projects" depends on a photo production pipeline.
4. Add fail points and recovery: where can a promise break, who notices first, what is the recovery script and SLA.
5. Cost the operations honestly. If the cost exceeds the price, raise the price or remove the promise.
6. Convert the blueprint into delivery artefacts: kickoff agreement, content production plan, review SLA, retainer scope, support runbook, escalation matrix.
7. Re-read the blueprint at every stage gate. Update before launch, after launch, and at every retainer renewal.
8. Stop release when a public promise lacks an owner, capacity, system, recovery path, or funded scope; recover by assigning, pricing, narrowing, or removing it.

## Quality Standards

- Every promise on the website is traceable to a lane that owns it.
- Every fail point has a named owner, recovery time, and customer-facing language.
- The blueprint distinguishes work the agency does from work the client does, with sign-off rights for each.
- Retainer hours match the blueprint, not a guess. Hidden work is named and either priced or removed.
- The blueprint is shared with the client and signed; it is not an internal document only.

## Anti-Patterns

- Selling response times without a rota or backup. Fix: fund the operating lane or narrow the promise.
- Showing case-study photos without rights. Fix: record permission and source before publishing.
- Promising weekly content without capacity. Fix: assign inputs, owner, hours, review, and recovery.
- Letting unwritten founder service hide scope. Fix: document, price, or remove the activity.
- Treating the blueprint as a one-time document. Fix: review it at launch, incidents, and renewal.

## Outputs

- Service blueprint diagram or table covering customer actions, frontstage evidence, frontstage staff, backstage staff, support processes, systems.
- Promise-to-lane traceability list.
- Fail-point and recovery register.
- Operations cost estimate and resulting price floor.
- Kickoff and retainer agreements aligned to the blueprint.
- Escalation matrix and on-call rota where applicable.

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Service blueprint | Agency and client owners | Every phase shows customer, frontstage, backstage, support, system, owner, and evidence lanes. |
| Promise and fail-point registers | Content, support, and release owners | Every item has ownership, SLA, detection, recovery, and cost. |
| Delivery operating agreement | Project and account teams | Decision rights, cadence, exclusions, escalation, and sign-off are approved. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Promise trace | Claim-to-operation matrix | No live claim ends at an unnamed team or system. |
| Stage-gate review | Dated pass/fail log | Uncosted or unowned commitments block the stage. |

## Capability Contract

Read and search are required. Editing the blueprint requires project authority. Changing signed scope, assigning people, committing SLAs, purchasing systems, or publishing promises requires explicit authorised approval.

## Degraded Mode

Fallback if required capabilities are unavailable:

Without capacity, cost, system, or client-owner evidence, produce a partial blueprint with gaps marked `not assessed`. Never infer that a promise is deliverable.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Promise has owner, capacity, system, and recovery | Keep and cost it | Unsupported premium claim |
| Promise is valuable but capability is missing | Add funded operation before release | Website-to-service trust breach |
| Promise cannot be operated within scope | Narrow or remove it | Hidden recurring loss and SLA failure |

## Worked Example

"Reply within one business day" requires monitored form delivery, a weekday rota, backup owner, ticket evidence, and a holding message. If the client has no backup owner, revise the promise or fund agency triage before launch.

<!-- dual-compat-end -->

## References

- `references/agency-delivery-blueprint.md` — full lane templates for discovery, build, launch, and retainer phases.
- `references/promise-to-operations-traceability.md` — turn website claims into operational commitments.
- `references/fail-point-recovery-playbook.md` — recovery scripts, SLAs, and escalation rules.
- `references/retainer-and-support-design.md` — designing retainer scope, hours, and renewal rules.
