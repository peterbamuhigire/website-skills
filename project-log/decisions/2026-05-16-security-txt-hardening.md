# Security.txt Hardening Gate

Date: 2026-05-16

## Decision

Every website shipped through the engine must publish
`/.well-known/security.txt` and a linked human-readable vulnerability
disclosure policy page.

The canonical `security-gate.sh` now runs `check-security-txt.sh` against the
built `dist/` output. A launch is blocked when the file is missing, contains
placeholders, lacks `Contact`, lacks exactly one future `Expires`, or omits a
`Policy` URL.

## Rationale

The passive portfolio check did not find valid `security.txt` files for sampled
domains. For an engine positioned around security-first engineering, a public
security contact and disclosure policy are baseline trust signals and reduce
the chance that vulnerability reports are lost.

RFC 9116 defines the machine-readable file and requires `Contact` and
`Expires`. The engine also requires `Policy` so researchers can see scope,
safe-harbor language, and response expectations before reporting.

## Consequences

- New projects bootstrapped with `install-canonical-ci.sh` receive starter
  files at `public/.well-known/security.txt` and `docs/security-policy.md`.
- Downstream projects must replace placeholders before the security gate can
  pass.
- Existing projects must add the file and disclosure page during their next
  maintenance pass before they can claim current engine compliance.
