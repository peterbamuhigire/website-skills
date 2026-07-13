---
name: security-gate
description: Use when auditing a website release for dependency, secret, header, SRI, security.txt, supply-chain, privacy, and deployment security evidence; use deploy to perform the authorised release.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Security Gate
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Produce a read-only security release verdict from reproducible checks without silently accepting unavailable surfaces.

<!-- dual-compat-start -->
## Use When

- A build is approaching release
- dependencies or third-party scripts changed
- headers, secrets, supply chain, or compliance evidence needs review.

## Do Not Use When

- Use `deploy` to execute release operations or policy-pages to draft legal text.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Build artefact, dependency locks, deployment configuration, third-party inventory, data flows, and target headers | Repository and hosting configuration | yes | Inspect the complete release surface | Stop if secrets exposure or critical dependency evidence is unresolved |

## Workflow

1. Confirm read-only scope and enumerate dependencies, scripts, data flows, and deployment surfaces
2. Run secret, dependency, header, SRI, security.txt, supply-chain, and applicable privacy checks
3. Classify evidence and stop release on critical or high unresolved defects
4. After authorised remediation, rerun the failed check and regression sample.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Security gate report | Developers, data owner, and release owner | Every check is pass, fail, or not assessed with severity, evidence, correction, and release verdict |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Scanner reports, header capture, dependency inventory, and decision record | Release owner | Evidence is tied to the tested commit and deployment target |

<!-- dual-compat-end -->
## Capability Contract

Read, search, and safe security checks are required. Default to read-only. Dependency changes, credential use, penetration testing, production mutation, disclosure, or publication require explicit authority.

## Degraded Mode

If the network, deployment target, lockfile, or scanner is unavailable, mark the affected checks `not assessed`, return a qualified report, and do not issue an unconditional pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Secret or exploitable critical dependency is confirmed | Block release and rotate or remediate | Credential compromise |
| External header endpoint is unavailable | Report header checks not assessed | False deployment assurance |

## Quality Standards

- Inspect source and deployed controls where applicable; record tool versions and targets; never expose secret values in evidence.

## Anti-Patterns

- Printing a discovered secret in the report. Fix: redact it and cite only location and identifier.
- Running intrusive tests without authority. Fix: limit execution to approved non-destructive checks.
- Scanning dependencies without the lockfile. Fix: mark resolution evidence incomplete.
- Treating unavailable headers as passed. Fix: mark them `not assessed`.
- Approving a third-party script without ownership or SRI review. Fix: inventory, justify, pin, and monitor it.

## Worked Example

If a production API token appears in history, redact the value, block release, require rotation and history remediation, then rerun the secret scan before verdict.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- Every build of a client site, as a CI-time gate before deploy.
- Before accepting any new third-party dependency.
- Before launching a new jurisdiction (new regulator, new data-protection law).
- During a quarterly dependency and policy review.

## Preserved Domain Exclusions
- Conducting a full penetration test — that is out of scope; commission a
  specialist engagement.
- Designing authentication or authorisation flows for a bespoke application —
  this gate audits static marketing sites.

## Core contract
Every primary build passes:
1. Dependency audit with zero "high" and zero "critical" findings.
2. Security header validation against the baseline in
   `references/csp-baseline.md` (HSTS, X-Frame-Options, X-Content-Type-Options,
   Referrer-Policy, Permissions-Policy, CSP).
3. Public vulnerability disclosure route:
   `/.well-known/security.txt` exists, is RFC 9116-compatible, has no
   placeholders, includes at least one `Contact`, exactly one future `Expires`,
   a canonical HTTPS URL, and a `Policy` link to the human disclosure page.
4. Subresource Integrity (SRI) hash on every third-party asset that survived
   design review.
5. Secrets scan with zero findings; any API key, token, private key, or
   credential in the repository blocks the build.
6. Supply-chain scan: lockfile integrity, package-name typosquat check,
   install-script review.
7. Compliance matrix up to date for every jurisdiction the client operates in.

Any "high" or "critical" finding blocks deploy.

## Canonical Command

```bash
bash "$WEBSITE_SKILLS/scripts/security-gate.sh"
```

The command:
1. Runs `npm audit --audit-level=high --json`.
2. Runs `scripts/check-security-headers.sh dist` against the CSP baseline.
3. Runs `scripts/check-security-txt.sh dist`.
4. Runs `scripts/check-sri.sh dist .third-party-allowed`.
5. Runs `scripts/scan-secrets.sh` against the committed tree.
6. Runs `scripts/supply-chain-check.sh` against `package-lock.json`.
7. Writes machine-readable results under `reports/security/` and a summary
   at `reports/security/summary.md`.
8. Exits non-zero on any "high" or "critical" finding.

## Preserved Domain Workflow
1. Build the site.
2. Run the canonical command.
3. For any blocking finding:
   - upgrade the offending dependency, or
   - remove or self-host the offending third-party asset, or
   - rotate the leaked credential and purge the history, or
   - strengthen the header at the edge (Nginx, Cloudflare Worker).
4. Complete the compliance review at launch using `references/compliance-matrix.md`.
5. File `project-log/launches/<project>/security-gate.md` with the result.

## Preserved Domain Inputs
- `package.json` and `package-lock.json` at repo root.
- A built static output at `./dist/`.
- A generated `./dist/.well-known/security.txt` file and a public disclosure
  policy page linked from its `Policy` field.
- A live edge-config declaration (Nginx vhost, Cloudflare Worker, equivalent)
  for header validation. If headers are served from a framework middleware,
  the middleware output goes to `dist/` and is audited from there.
- The jurisdiction list for the client (e.g. "Uganda, Kenya, Nigeria").

## Preserved Domain Quality Guidance
- High/critical findings are non-negotiable; no suppression on severity grounds.
- A suppression is allowed only on a specific CVE with a documented
  non-applicable path (e.g. the vulnerable function is never called). Every
  suppression has a review date within 12 months.
- Headers are verified on the deployed site, not only in configuration.
- `security.txt` is treated as stale when `Expires` is in the past and must be
  reviewed at least annually.
- SRI hashes are regenerated on every build; stale hashes break by design.
- Compliance matrix entries are specific to the client, not copied generically.

## Preserved Domain Anti-Patterns
- Treating `npm audit` severity as advisory.
- Disabling HSTS during "migration" without a documented end date.
- Using `'unsafe-inline'` CSP as a permanent position.
- Hosting a payment widget via an inline script without SRI.
- Assuming GDPR coverage is sufficient in Africa; each jurisdiction has its
  own data-protection act with different requirements.
- Forgetting to rotate a leaked secret because "the repo is private".
- Shipping a security-first site without a public security contact and
  disclosure policy.

## Preserved Domain Outputs
- `reports/security/audit.json` — dependency audit output.
- `reports/security/headers.txt` — per-route header validation.
- `reports/security/security-txt.txt` — vulnerability disclosure route check.
- `reports/security/sri.txt` — SRI check result.
- `reports/security/secrets.txt` — secrets scan findings (empty on success).
- `reports/security/supply-chain.txt` — supply-chain posture.
- `reports/security/summary.md` — CI-friendly summary.
- A signed compliance note per launch.
- A blocking CI status on any high/critical finding.

## Preserved Domain References
- `references/csp-baseline.md` — the CSP and security-header baseline.
- `references/compliance-matrix.md` — jurisdiction rules for Uganda DPPA 2019,
  Kenya Data Protection Act 2019, Nigeria NDPR, South Africa POPIA, GDPR.
- `references/dependency-policy.md` — how dependencies are added, upgraded,
  and suppressed.
- `references/secrets-response.md` — rotation, revocation, and history-rewrite
  playbook.
- `references/supply-chain.md` — typosquat detection and install-script review.
- `../../templates/security.txt` — project starter for the required
  `/.well-known/security.txt` artifact.
- `../../templates/security-policy.md` — human-readable disclosure policy
  starter linked from `Policy`.

## Notes
- This gate does not replace a specialist penetration test for authenticated
  applications. For static marketing sites, this gate is sufficient as the
  ongoing CI contract.
- Work in concert with `deploy/references/deployment-runbook.md` on where the
  edge-configured headers live.
- `policy-pages/SKILL.md` produces the public-facing privacy and terms pages;
  this gate audits that they exist and that the compliance matrix they
  describe is correctly enforced.
