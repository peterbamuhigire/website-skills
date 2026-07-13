---
name: i18n
description: Use when designing or implementing multilingual website routes, locale content, hreflang, canonical URLs, switching, and sitemaps; do not use for writing native French or Kiswahili copy or for general SEO alone.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# I18N
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- A website serves multiple locales and needs shared route-equivalence, localized slugs, fallback, switching, canonical, hreflang, and sitemap rules.
- English, French, Kiswahili, or another approved locale must remain structurally aligned while allowing locale-specific pages and metadata.

## Do not use when
- The request is native French or Kiswahili writing; route to the relevant native-copy skill.
- The request concerns metadata/schema for one language only; use `seo` unless locale equivalence is involved.
- Supported locales or fallback policy are undecided; stop before route implementation.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Supported locales, default locale, and fallback policy | Approved content/SEO brief | yes | Stop route implementation and request the locale decision. |
| Route-equivalence and localized-slug map | Content inventory | yes | Create a gap register; never infer translations as approved slugs. |
| Native locale content and metadata | Native-copy skills or client | conditional | Build structure with missing-content states; do not machine-translate for release. |
| Framework and deployment URL rules | Repository and hosting config | yes | Return a framework-neutral contract only. |

## Workflow
1. Confirm locales, default, fallback, URL policy, native-copy ownership, and deployment constraints; stop on unresolved policy conflicts.
2. Inventory every route and classify it as equivalent, locale-specific, missing, or intentionally excluded.
3. Approve localized slugs and generate switching, canonical, reciprocal hreflang, and sitemap behaviour from one map.
4. Implement only reviewed locale content and explicit missing-content states.
5. Test reciprocal routes, 404s, fallbacks, canonical URLs, alternates, and sitemaps.
6. If build or crawl checks fail, keep the route map, remove invalid alternates, and return failing source/target pairs for recovery.

## Quality standards
- Locale switching, canonical, reciprocal hreflang, sitemap, fallback, and 404 behaviour derive from one map.
- Published locale copy and slugs are approved by the correct native-copy owner.
- Tests cover equivalent, missing, locale-specific, redirected, and excluded routes.
- For multilingual websites, slugs must be localized for every supported language. Do not keep English slugs on non-English pages unless the term is a proper noun, brand, acronym, or established search term in that language.
- Language switching, canonical URLs, hreflang tags, and sitemaps must resolve through the same route-equivalence map so users changing languages land on the matching page with the correct localized URL.

## Anti-patterns
- Translating only the URL prefix. Fix: approve a localized slug through the equivalence map.
- Linking non-equivalent pages. Fix: omit hreflang until a true counterpart exists.
- Publishing raw machine translation. Fix: route copy to the native-language owner.
- Maintaining separate switcher and sitemap maps. Fix: generate both from one source.
- Hiding missing content behind English fallback. Fix: apply the documented missing-content policy.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not blindly swap only the language prefix in URLs. `/en/accounting-software/` should become the researched equivalent for the target language, not `/fr/accounting-software/`, unless that slug is intentionally native to the target language.
- Do not emit hreflang entries for missing or non-equivalent pages; omit them until valid.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Locale and route-equivalence map | Content, SEO, and `page-builder` | Every published page maps to valid alternates or documents why none exist. |
| i18n implementation/configuration | Build and deploy workflows | Switching, canonical, hreflang, sitemap, fallback, and 404 behaviour agree. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Locale route test results | Source URL, target locale, expected/actual route | Includes missing translation, fallback, canonical, and alternate-link cases. |

## Capability Contract
Inspect routes and content read-only by default. Edit locale configuration and route files only when implementation is authorised. Never publish machine-translated copy or change approved wording without native-copy authority.

## Degraded Mode
When native copy, crawling, build, or network access is unavailable, deliver the route contract and a missing-content register. Mark hreflang, sitemap, build, and redirect checks not assessed rather than passed.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| True page equivalent exists | Link localized canonical and reciprocal hreflang | Search ambiguity |
| Locale page is absent | Omit alternate and route to documented fallback | False equivalence |
| Slug is an approved proper noun or search term | Preserve with rationale | Harmful over-translation |
| Locale content is unreviewed | Keep unpublished or clearly staged | Low-quality public copy |

## Worked Example
Map `/en/accounting-software/` to approved French and Kiswahili slugs, generate reciprocal alternates from one equivalence record, and test switching from each page. If Kiswahili copy is missing, omit that alternate and record the gap instead of redirecting silently to English.

## References

- [Preserved multilingual implementation guidance](references/legacy-guidance.md)

<!-- dual-compat-end -->
