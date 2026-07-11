# Standards Register

Verified 2026-07-11. Links are primary sources. Owners review changes and record threshold changes under `project-log/decisions/`.

| Standard | Current controlled basis | Applies to | Owner | Cadence | Next review |
|---|---|---|---|---|---|
| WCAG | [WCAG 2.2, W3C Recommendation 12 Dec 2024](https://www.w3.org/TR/WCAG22/) | Accessibility acceptance | accessibility-audit | Quarterly | 2026-10-01 |
| WAI-ARIA | [WAI-ARIA 1.2 and APG](https://www.w3.org/WAI/standards-guidelines/aria/) | Interactive patterns | accessibility-audit | Quarterly | 2026-10-01 |
| Application verification | [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) | Risk-based security controls | security-gate | Quarterly | 2026-10-01 |
| Web risk awareness | [OWASP Top 10:2025](https://owasp.org/Top10/) | Threat review; not a verification checklist | security-gate | Quarterly | 2026-10-01 |
| Vulnerability disclosure | [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116) | `security.txt` | security-gate | Annual | 2027-07-01 |
| Workflow security | [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use) | Least privilege and immutable action references | deploy | Quarterly | 2026-10-01 |
| Search | [Google Search documentation updates](https://developers.google.com/search/updates) | Search and AI-feature currency | google-ai-search | Monthly | 2026-08-01 |
| Structured data | [Google structured-data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) and [Schema.org 30.0](https://schema.org/version/latest/) | Visible-content-aligned markup | seo | Monthly | 2026-08-01 |
| Privacy risk | [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | Voluntary privacy risk framing | security-gate | Quarterly | 2026-10-01 |

## Legal boundary

This register supplies technical and governance information, not jurisdiction-specific legal advice. Privacy, consumer, employment, health, finance, payment, and regulated-sector launches require qualified review in every target jurisdiction. NIST Privacy Framework 1.1 remains an initial public draft as of this verification and must not be described as a final standard.

## Current implementation decisions

- Do not promise FAQ rich results. Google ended the feature in May 2026 and removed its documentation in June 2026.
- Treat structured data as eligibility support, never a display guarantee.
- Use OWASP Top 10:2025 for awareness and ASVS 5.0.0 for verifiable controls.
