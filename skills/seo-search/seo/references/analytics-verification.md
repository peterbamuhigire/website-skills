# Analytics and Search Measurement Verification

Parent skill: [`../SKILL.md`](../SKILL.md)

Verify that the approved measurement design produces decision-useful evidence
without violating consent, privacy, security, or performance requirements. Do
not prescribe one analytics vendor, implementation pattern, script size,
performance score, setup duration, or reporting cadence for every project.

## Inputs

- business outcome and page-task map;
- event and parameter dictionary;
- approved analytics/search platforms and account owners;
- consent, lawful basis, retention, identity, and access rules;
- environments, canonical domains, test identities, and release ID;
- attribution model and CRM/offline reconciliation plan.

Stop if collection lacks a stated purpose, owner, consent/governance decision,
or safe test environment.

## Implementation verification

For each environment and consent state:

- inspect the rendered page and network requests;
- verify only approved scripts and endpoints load;
- confirm events fire once with the correct name, parameters, page identity,
  locale, and timestamp;
- test accept, reject, partial, withdrawal, and changed-consent paths;
- verify personal or sensitive data is absent unless explicitly designed,
  minimised, secured, and authorised;
- test SPA/navigation, validation errors, retries, duplicate submission,
  success, and offline/reconnect behaviour where applicable;
- compare performance and reliability before and after instrumentation;
- confirm production secrets or privileged tokens are not exposed client-side.

Browser debug output is structural evidence. Verify receipt and processing in
the destination report where authorised.

## Search Console verification

Choose a currently supported ownership method with the domain owner. Prefer
organisation-controlled ownership and least privilege. Record method, property,
owner, date, recovery path, and whether verification is observed.

Submit the canonical sitemap through supported Search Console mechanisms and
reference it in `robots.txt`. Do not use the deprecated unauthenticated sitemap
ping endpoint. Treat submission and URL inspection as evidence of processing,
not indexing or ranking guarantees.

Review normal Web performance and, as of 31 August 2026, the dedicated
generative AI impressions report and property inclusion control. The latter is
separate from `Google-Extended`.

## Bing verification

Verify the site through a supported method or authorised import, submit the
sitemap, and inspect representative URLs. When available, review AI Performance
using current public-preview definitions: total citations, average cited pages,
sampled grounding queries, page-level citation activity, and trends. Do not
interpret them as ranking, authority, placement, citation support, or business
value.

## Referral and outcome checks

- preserve source/medium and campaign parameters through redirects and locale
  routing where lawful;
- monitor currently documented ChatGPT search referrals carrying
  `utm_source=chatgpt.com`, while allowing for incomplete tagging;
- connect sessions to qualified actions with consent-aware identifiers;
- reconcile web events with CRM, commerce, call, or offline outcomes;
- report unmatched, duplicated, blocked, sampled, and delayed records.

## Acceptance evidence

| Area | Acceptance condition |
|---|---|
| Event contract | Intended events and parameters observed once in each tested state |
| Consent/privacy | Collection follows the approved state and excludes prohibited data |
| Account governance | Organisation owner, least privilege, recovery, and review date recorded |
| Search tools | Property, sitemap, representative URLs, and report access observed or `NOT_ASSESSED` |
| Attribution | Limits, redirects, identity, and reconciliation gaps documented |
| Performance | Before/after evidence meets the project's budgets |
| Release identity | Evidence maps to the deployed build and environment |

## Failure handling

- Disable or roll back instrumentation that leaks data, breaks consent, causes
  duplicate conversions, or breaches performance/reliability guardrails.
- Repair the source event or consent implementation rather than adjusting a
  dashboard to hide the defect.
- Re-run the failed state plus one unaffected regression path.
- Keep delayed, inaccessible, low-volume, or externally processed evidence
  `NOT_ASSESSED` until observed.

## Currentness

Use [`webmaster-tools-setup.md`](webmaster-tools-setup.md),
[`analytics-event-map.md`](analytics-event-map.md), and the claim register at
[`../../../../docs/source-registers/search-ai-currentness-2026-09-05.json`](../../../../docs/source-registers/search-ai-currentness-2026-09-05.json).
