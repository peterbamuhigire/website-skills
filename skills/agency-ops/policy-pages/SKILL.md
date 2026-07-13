---
name: policy-pages
description: Use when drafting or implementing website privacy and terms pages from verified processing, ownership, audience, and jurisdiction facts. Use legal counsel for legal conclusions and `form-ux-design` for consent-control interaction design.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Policy Pages
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- The task matches this domain: Design Privacy Policies and Terms of Use that are legally compliant, user-friendly, accessible, and trustworthy. Use when building any website to ensure proper legal protection, regulatory compliance (GDPR, CCPA, COPPA, PIPEDA, LGPD), and user trust through clear, plain-language documents. Covers design patterns, placement strategies, implementation examples, and jurisdiction-specific requirements. Every website needs both documents.
- The user needs an implementation-facing skill rather than a general discussion.

## Do Not Use When
- The prerequisite upstream context is missing and the task is not yet execution-ready.
- Another narrower skill is the clear better fit for the exact subtask.

## Inputs
| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Controller identity, contacts, audience, jurisdictions | Client and counsel | yes | Stop substantive drafting and return a fact questionnaire. |
| Data inventory, purposes, vendors, retention, rights process | Technical and operations owners | yes | Produce no compliance claim; mark missing facts. |
| Approved legal position | Qualified counsel | conditional | Draft operational plain-language content for legal review, not legal advice. |

## Workflow
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. Validate that the result stays compatible with the rest of the repository workflow.
5. Trace every statement to an observed practice or approved legal input; stop release when the page promises a right or control the organisation cannot operate.

6. Stop release when a material fact or counsel decision is missing; recover with a marked draft and fact register.

## Quality Standards
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.

## Anti-Patterns
- Copying another site's policy. Fix: derive clauses from this site's processing inventory.
- Naming laws that have not been scoped. Fix: obtain jurisdictional review and qualify uncertainty.
- Claiming data is never shared while vendors process it. Fix: disclose verified processor roles.
- Publishing rights instructions nobody owns. Fix: name the operational contact and tested workflow.
- Hiding material terms in dense prose. Fix: use plain headings, summaries, and accessible links without weakening legal review.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Privacy notice draft | Users, counsel, and site implementer | Covers verified collection, purpose, sharing, retention, rights, contacts, and effective date. |
| Terms draft | Users, counsel, and business owner | Matches actual service, eligibility, payments, acceptable use, liability position, and dispute path. |
| Implementation register | Website and operations owners | Maps every promise and contact route to a working control and owner. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Clause-to-fact matrix | Clause, source, owner, review status | No substantive clause is supported only by assumption. |
| Counsel and release status | Dated approval/gap register | Legal review and unassessed jurisdictions are explicit. |

## Capability Contract
Default to read-only fact gathering and drafting. Editing requires authorisation. Publishing, changing consent settings, certifying compliance, or representing the draft as legal advice requires explicit client authority and, where needed, qualified counsel approval.

## Degraded Mode
When a complete data inventory or jurisdictional review is unavailable, return a marked draft plus a fact-and-counsel gap register. Mark legal compliance `not assessed`.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Processing fact is unknown | Ask and mark the clause pending | Invented legal representation |
| Practice contradicts draft | Fix the practice or revise the promise | Paper compliance with operational breach |
| Child, health, finance, or cross-border data is involved | Require specialist review | Under-scoped high-risk processing |

## Worked Example
For a contact form using a hosted analytics provider, document the submitted fields, analytics events, vendor role, retention owner, and deletion contact. Acceptance: the notice does not say "we do not share data" and the stated deletion route has been tested by the operations owner.

<!-- dual-compat-end -->

## References

- [Privacy policy detailed guidance](references/privacy-policy-detailed.md)
- [Terms of use detailed guidance](references/terms-of-use-detailed.md)
- [Preserved legacy guidance](references/legacy-guidance.md)
