# Infographics, diagrams and downloads: the Chwezi standards family reaches the website engine, 8 November 2026

## Why

The design engine adopted the Chwezi standards family on 8 November 2026: the Product Excellence
Standard as parent (product UI/UX, tokens, accessibility, performance, brand adaptation and quality
assurance, including mobile and tablet UI) and four child systems (dashboards and analytics,
documents and publishing, presentations and slide decks, infographics and visual communication). A
cross-check of this engine found that it had chart, table and SVG rules but nothing for infographics,
process or cycle diagrams, timelines, maps, social cards or downloadable posters, decks and reports,
which sites carry often.

## Change

- New `skills/build/design-system/references/infographics-and-explanatory-visuals-rules.md`
  (original words; working rules for the web: source register, lie factor and area scaling, maps by
  rate with a sourced current boundary, diagram structure as data, live text and no synthetic
  photorealism, figure markup with a long text equivalent, 320 px reflow, phone canvas scale for social
  cards, downloads with an HTML counterpart and a version note, release checklist). It points to the
  design engine for the full standard and its checker; nothing is copied, so there is one source.
- `design-system/SKILL.md`: reference link, and Step 0 now also names the matching child standard
  for infographics, decks and documents.
- `data-tables-charts-and-svg-rules.md`: related-files pointer.
- `visual-qa` and `accessibility-audit`: one Quality Standards bullet each for routes that carry
  complex graphics.
- `AGENTS.md`: the design-engine infographics, presentation and document-publishing standards listed
  as cross-engine support skills, and the infographics standard added to the tree.

## Currentness

Admitted claims and their status are in the reference's Sources section: the internal Chwezi
standard (read 2026-11-08), Tufte's lie factor (durable concept), and the W3C WAI Complex Images
tutorial (live page not read on 2026-11-08: current wording `NOT_ASSESSED`, review by 2027-02-08).
The arithmetic (lie factor, radius against area, Web Mercator area factor 1/cos^2, ppi from viewing
distance) was computed on 2026-11-08. Screen-reader support for individual ARIA techniques is
`NOT_ASSESSED` and is tested per project.

## Checks (2026-11-08, Windows, Python 3.14)

| Command | Result |
|---|---|
| `validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | zero debt, 62 active skills |
| `routing-smoke-test.py` | precision@1 93.2%, precision@3 100%, owned negatives 24 of 24 (unchanged) |
| `check_portable_references.py` | PASS |
| `validate-checkout-size.py` | PASS (full 4,882 of 5,000 entries before this file; 4,883 after) |
| `validate-source-registers.py` | PASS (4 registers, 53 claims) |
| `check-vendored-detector.py --source <design engine>` | manifest PASS, source comparison PASS |
| `pytest tests` | 250 passed, 9 skipped, 21 failed: all 21 are in `test_worked_service_site.py`, whose gates run through `bash`; on this machine `bash` is WSL2 and fails with "Failed to attach disk ... to WSL2". Environment fault, not a content failure; the bash-script gates are `NOT_ASSESSED` on this host and need a re-run on Linux or a working WSL2 |

## Not assessed

No website has yet been built or reviewed against the new reference; the bash-script gates above.
The package is close to its entry cap (4,883 of 5,000), so the next additions should fold into
existing references.
