---
name: email-sender
description: Use when implementing a self-hosted PHP and PHPMailer form-mail flow with spam, CSRF, validation, delivery, and confirmation controls. Use `email-sender` for transactional form delivery, not campaign broadcasts or general form UX.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Email Sender
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- The task matches this domain: Secure email sending from static websites using PHP + PHPMailer on Apache/WAMP. Self-hosted contact form handler with 4-layer spam prevention (honeypot, timing, content scan, rate limiting), stateless CSRF, beautiful branded HTML emails, and bilingual support. No external services required.
- The user needs an implementation-facing skill rather than a general discussion.

## Do Not Use When
- The prerequisite upstream context is missing and the task is not yet execution-ready.
- Another narrower skill is the clear better fit for the exact subtask.

## Inputs
| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Form fields, consent text, recipient, and success states | Approved form specification | yes | Stop implementation and request the missing contract. |
| Hosting, PHP, mail transport, and secret-storage facts | Runtime owner | yes | Return configuration requirements; do not invent credentials. |
| Brand and locale copy | Brand/content owner | conditional | Use plain unbranded English and label localisation pending. |

## Workflow
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. Validate that the result stays compatible with the rest of the repository workflow.
5. Test valid, invalid, spam, CSRF, rate-limit, mail-failure, and duplicate-submit paths; stop release on any unassessed security or delivery path.

6. Stop release on an unassessed security or delivery path; recover by fixing and retesting the failed path.

## Quality Standards
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.

## Anti-Patterns
- Committing SMTP credentials. Fix: inject secrets outside the repository and document rotation.
- Trusting client-side validation. Fix: validate and normalise every field server-side.
- Returning raw transport errors. Fix: log a correlation ID and show safe user copy.
- Treating a honeypot as complete protection. Fix: combine timing, rate, content, and CSRF controls.
- Claiming delivery after queue acceptance. Fix: distinguish accepted, delivered, bounced, and unassessed states.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Form-mail handler and configuration contract | Website implementer | Uses server validation, safe secrets, CSRF, spam controls, structured errors, and no header injection. |
| Email and confirmation templates | Visitor and site owner | Escaped content, correct locale, usable text fallback, and one clear next step. |
| Verification record | Release owner | Records the result of every required success and failure-path test. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Test matrix | Scenario, expected, actual, result | Includes mail failure and abuse paths; unrun checks say `not assessed`. |
| Secret and transport review | Redacted configuration checklist | Contains no credential value. |

## Capability Contract
Read and search are required. Editing and local execution require implementation authority. Network delivery tests, DNS changes, credential creation, production deployment, and sending to real recipients require explicit authority; never expose secrets in output.

## Degraded Mode
Without a mail transport, credentials, network, or execution, provide a configuration-ready patch and test plan. Mark deliverability, DNS authentication, and inbox rendering `not assessed`; never report a send as successful.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Static host cannot execute PHP | Choose an approved transactional endpoint | Deploying a handler the host cannot run |
| Sensitive or regulated submission | Minimise email content and store securely | Personal data leakage through mail |
| Delivery cannot be tested | Block release or qualify evidence | False assurance from syntax-only checks |

## Worked Example
A bilingual enquiry form accepts name, email, locale, and message. A failed SMTP connection returns a neutral retry message with a correlation ID; it does not echo the exception. Acceptance: forged CSRF, newline injection, a fast bot submit, and a transport failure all produce the documented safe result.

<!-- dual-compat-end -->

## References
- Use `references/launch-and-confirmation-flows.md` when the form must support waitlists, events, applications, campaign enquiries, or flow-specific confirmation emails and thank-you pages.

