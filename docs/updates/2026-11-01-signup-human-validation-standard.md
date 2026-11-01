# Signup human-validation standard

Added a page-builder reference for Cloudflare Turnstile Managed mode on web signup forms. The reference requires server-side Siteverify validation, hostname checks, safe retries, accessible challenge handling, and an explicit provider-outage path. Native Android signup uses Firebase App Check with Play Integrity and a Turnstile WebView fallback when expected attestation is unavailable.

The checks are described as controls against bot-driven and unauthorised automated use, alongside authentication, authorisation, email confirmation and rate limits. They are not identity proof.

Current provider claims were checked against official Cloudflare and Firebase documentation on 1 November 2026. The source record and review date (1 February 2027) are in the linked skill reference.
