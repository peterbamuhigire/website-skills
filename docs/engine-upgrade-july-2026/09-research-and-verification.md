# Research and Verification Record — 11 July 2026

## Research frame

Research type: comparative benchmarking. Decision: which current primary-source requirements must change the engine's executable contract. The research used the digital-research-skills evidence discipline, source verification, gap analysis, critical reasoning, and anti-slop rules.

## Verified changes that affected implementation

| Finding | Primary evidence | Engine decision |
|---|---|---|
| WCAG 2.2 remains the current W3C Recommendation; the dated Recommendation is 12 December 2024. | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Keep WCAG 2.2 AA as the accessibility baseline and retain human evaluation. |
| ASVS 5.0.0 was released 30 May 2025. | [OWASP ASVS project](https://owasp.org/www-project-application-security-verification-standard/) | Use ASVS 5.0.0 for verification controls. |
| OWASP Top 10:2025 is current. | [OWASP Top 10:2025](https://owasp.org/Top10/) | Use it for threat awareness, not as a substitute for ASVS. |
| Full-length action commit SHAs are GitHub's immutable-reference control. | [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use) | Pin every action in the canonical workflow; set read-only repository permission by default. |
| Google ended FAQ rich results on 7 May 2026 and removed the documentation in June. | [Google Search documentation updates](https://developers.google.com/search/updates) | Remove mandatory FAQPage and AI-citation claims; keep useful visible FAQ content. |
| Structured data must match visible content and does not guarantee display. | [Google structured-data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | Make schema conditional, validate it, and prohibit display promises. |
| Schema.org 30.0 was published 19 March 2026. | [Schema.org 30.0](https://schema.org/version/latest/) | Record the vocabulary version and review monthly with Google feature guidance. |
| NIST Privacy Framework 1.1 is still presented as an initial public draft. | [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | Do not mislabel it final; use it only as voluntary risk-management guidance. |

## Source-verification result

All load-bearing links above resolved on 11 July 2026. No direct quotes or external statistics ship in the implementation. GitHub action SHAs were resolved from each official `actions/*` repository tag using `git ls-remote` on the same date. The standards register records ownership and next-review dates so these facts can expire visibly.

## Countercase and limits

Repository fixtures can prove deterministic contracts and failure handling; they cannot prove client outcomes, native-language quality, or independent visual judgment. Those require named external reviewers and post-launch telemetry. A 95+ certification is therefore an evidence state, not a score that can be created by adding files.
