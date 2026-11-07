# Per-URL response evidence

Date: 2026-11-07. Kaizen action WE-KZ-04, bounded work items W01–W03.

The existing audit checklist named access and index signals but did not require
an ordered record of the response, method and origin. The added procedure
separates those observations and gives the Google readiness checklist one
pointer to the same procedure. The status/body mismatch label is an audit
decision inferred from Google's distinction between successful responses and
soft-404 content; it is not a provider status code.

## Primary-source register

All rows were accessed on 2026-11-07. Support is limited to the listed claim;
the owner is the website search maintainer. Review before a dependent live
audit, when the provider changes these documents, or by 2026-12-07, whichever
comes first. No claim about an actual site's access or indexing is established.

| Source | Document date | Freshness | Supported scope and limit |
|---|---|---|---|
| [Google HTTP status handling](https://developers.google.com/crawling/docs/troubleshooting/http-status-codes) | 2026-02-04 | Platform | Successful response versus indexing; error-like bodies and soft 404. Google scope only. |
| [Google robots specification](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec) | 2026-10-23 | Platform | Host, protocol and port scope; Google response/cache handling. Not all crawlers. |
| [Google robots meta and X-Robots-Tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) | 2026-03-24 | Platform | Access prerequisite and response directives, including non-HTML resources. |
| [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) | 2022-09 | Standard | Sections 2.3–2.4, robots retrieval and caching; not proof of implementation by every bot. |
| [URL Inspection result fields](https://developers.google.com/webmaster-tools/v1/urlInspection.index/UrlInspectionResult) | 2025-01-21 | Platform | Fetch, crawl, robots and indexing report fields; not a raw response capture. |
| [Search Console introduction](https://developers.google.com/search/docs/monitor-debug/search-console-start) | 2025-12-10 | Platform | Live URL test capability; not evidence that any site was tested. |

Non-Google fetcher semantics and the proposed initial-HTML requirement W04
remain unassessed. No target site, Search Console property or live crawler
evidence was supplied. A source-grounded procedure and synthetic decision
review cannot establish live-site acceptance.

Recovery: revert the two checklist additions together; retain this dated
source record. Do not change robots, CDN, authentication or indexing controls
without the site owner's applicable authority.
