# Standards Register

Re-verified 2026-10-31 against the primary source linked in each row; the dated claims, support states and
limits are in `docs/source-registers/standards-currentness-2026-10-31.json`. Row identifiers `STD-001`,
`STD-015` and `STD-016` refer to the portfolio workspace register, which is kept outside this repository.
`scripts/validate-source-registers.py` fails when a review date passes, when a date is missing, or when a
review date sits further from its verification than the cadence allows, so a row cannot be extended without
a check behind it. Owners review changes and record threshold changes under `project-log/decisions/`.

| Standard | Current controlled basis | Applies to | Owner | Cadence | Last verified | Next review |
|---|---|---|---|---|---|---|
| WCAG | [WCAG 2.2, W3C Recommendation 12 Dec 2024](https://www.w3.org/TR/WCAG22/) (STD-001; errata exist) | Accessibility acceptance | accessibility-audit | Quarterly | 2026-10-31 | 2027-01-31 |
| WAI-ARIA | [WAI-ARIA 1.2, W3C Recommendation 6 Jun 2023](https://www.w3.org/TR/wai-aria-1.2/) and [APG](https://www.w3.org/WAI/standards-guidelines/aria/); no later Recommendation named on the 1.2 page | Interactive patterns | accessibility-audit | Quarterly | 2026-10-31 | 2027-01-31 |
| Application verification | [OWASP ASVS 5.0.0, 30 May 2025](https://asvs.owasp.org/); no 5.0.x or 5.1 listed | Risk-based security controls | security-gate | Quarterly | 2026-10-31 | 2027-01-31 |
| Web risk awareness | [OWASP Top 10:2025](https://top10.owasp.org/2025); release date not stated on the page | Threat review; not a verification checklist | security-gate | Quarterly | 2026-10-31 | 2027-01-31 |
| Vulnerability disclosure | [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116), Informational, 2022 | `security.txt` | security-gate | Annual | 2026-10-31 | 2027-10-31 |
| Workflow security | [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use) | Least privilege and immutable action references | deploy | Quarterly | 2026-10-31 | 2027-01-31 |
| Search | [Google Search Essentials](https://developers.google.com/search/docs/essentials) (STD-015; page updated 10 Dec 2025) | Search eligibility and appearance guidance | google-ai-search | Monthly | 2026-10-31 | 2026-11-30 |
| Core Web Vitals | [Web Vitals](https://web.dev/articles/vitals) and [threshold methodology](https://web.dev/articles/defining-core-web-vitals-thresholds) (STD-016; page updated 7 May 2025) | Lab input and field evidence framing; lab checks do not prove field performance | deploy | Quarterly | 2026-10-31 | 2027-01-31 |
| Lab tooling | [Lighthouse 13.6.0, 27 Oct 2026](https://github.com/GoogleChrome/lighthouse/releases/latest); `@lhci/cli` 0.15.1 still pins Lighthouse 12.6.1 | Lab assertions in the performance gate | deploy | Monthly | 2026-10-31 | 2026-11-30 |
| Structured data | [Google structured-data guidelines, updated 10 Jul 2026](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) and [Schema.org 30.1, 16 Sep 2026](https://schema.org/docs/releases.html) | Visible-content-aligned markup | seo | Monthly | 2026-10-31 | 2026-11-30 |
| Privacy risk | [NIST Privacy Framework 1.0](https://www.nist.gov/privacy-framework); 1.1 is an initial public draft | Voluntary privacy risk framing | security-gate | Quarterly | 2026-10-31 | 2027-01-31 |
| Data-protection statutes | Identifiers only, partly read through search summaries: Uganda DPPA 2019, Kenya DPA 2019, Nigeria NDPA 2023, South Africa POPIA 2013, EU GDPR 2016/679. Support is `partially_supported`; see claims `WSK-LEG-001` to `WSK-LEG-005` | Names and regulators cited in the compliance matrix; not clause-level, not applicability | security-gate | Monthly | 2026-10-31 | 2026-11-30 |

## Legal boundary

This register supplies technical and governance information, not jurisdiction-specific legal advice. Privacy, consumer, employment, health, finance, payment, and regulated-sector launches require qualified review in every target jurisdiction. NIST Privacy Framework 1.1 remains an initial public draft as of this verification and must not be described as a final standard.

## Current implementation decisions

- Do not promise FAQ rich results. Google ended the feature in May 2026 and removed its documentation in June 2026.
- Treat structured data as eligibility support, never a display guarantee.
- Use OWASP Top 10:2025 for awareness and ASVS 5.0.0 for verifiable controls.
