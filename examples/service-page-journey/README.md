# Service page journey prototype

This is a local, synthetic structural prototype to exercise P14's mobile, keyboard and form recovery path. The old internal prompt is not current brand approval: the live website could not be verified, and repository material contains conflicting domains and unapproved claims. The page therefore carries no address, telephone number, testimonial, client logo, performance statistic, price, delivery promise, service catalogue, analytics, external form endpoint, or structured data.

The brand name and draft palette are provisional. All service language, audience, privacy wording, legal basis, contact destination, brand identity, and publish authority require named owner approval. `noindex,nofollow` is present for safety, but that directive alone does not prevent access or guarantee de-indexing. Keep this file outside a public deployment until a release owner approves a content and hosting manifest.

The form is intentionally local. The submit action validates and explains that no data was sent; two preview controls exercise a simulated transient error (preserving input) and a clearly simulated acceptance. No persistence, analytics, network submission or tracking is implemented.

## Checks

Run `python tests/website_service_page_qa.py` from this repository root. This browser check uses a local file URL, the installed Microsoft Edge channel and Playwright. It covers viewport overflow, noindex metadata, keyboard-visible focus, missing/invalid fields, simulated recovery, preserved values, and local-only submission. It is not a WCAG conformance audit or a substitute for screen readers, assistive technology, user research, cross-browser checks, field performance or production deployment proof.
