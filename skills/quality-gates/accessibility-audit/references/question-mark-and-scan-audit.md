# Question-mark and scan audit

This is a read-only review of whether a representative route makes its purpose,
next action, outcome, and recovery path findable without explanation. It
extends accessibility and visual review; it cannot certify rendered
accessibility, usability, or conversion by itself.

## Required input and evidence state

Record the route, user task, locale, viewport or render identity, content and
component states, reviewer, and evidence type. Tag every observation as
`static`, `rendered`, `manual`, `live`, or `NOT_ASSESSED`. A static file review
cannot pass a browser or user-behaviour question.

## Audit record

| Check | Question to answer |
| --- | --- |
| purpose | Can a first-time reviewer say what the page is for? |
| information scent | Are the task term, relevant label, and first plausible action visible early? |
| labels and affordance | Does the control say what happens, and does it look operable? |
| hierarchy | Can the primary action, related content, and current location be identified from structure? |
| scan path | Can a reader recover the page argument from headings, short paragraphs, lists, and restrained emphasis? |
| recovery | Can a wrong click, failed request, or empty state be recovered without losing context? |
| noise | Does each banner, badge, animation, or decorative element have a job? |
| privacy friction | Do forms request only data needed for the stated task, with a clear reason and recovery path? |

For each question mark or scan defect, record:

```yaml
locator: "route + heading, control, or state"
observed_question: "What is unclear?"
evidence_type: "static | rendered | manual | live | NOT_ASSESSED"
owner: "role"
repair: "label, hierarchy, affordance, content, or recovery change"
retest_question: "What should the reviewer be able to answer next time?"
status: "OPEN | RESOLVED | NOT_ASSESSED"
```

## Procedure

1. State one realistic task and the route/state being reviewed.
2. List the questions a reviewer would have: what this is, where to start,
   what happens next, and how to recover.
3. Inspect labels, headings, first viewport, affordance, active location,
   content grouping, and failure/empty states.
4. Put the likely task term, safe first action, and recovery path where a
   scanning reader can find them. Preserve necessary legal, privacy,
   accessibility, and support content.
5. Record each finding with an owner, locator, repair, and re-test question.
6. Re-run the task at the same evidence level. If render, browser, manual, or
   user observation is unavailable, keep that dimension `NOT_ASSESSED`.

## Acceptance oracle

The reviewer can identify the page purpose, primary next step, expected outcome,
and recovery path without bespoke explanation. Headings and labels preserve the
content argument when scanned. Findings have a reproduction locator and owner.
No conclusion about live behaviour is made from static evidence.

## Failure paths

| Finding | Outcome | Repair |
| --- | --- | --- |
| page purpose or first action is unclear | `FAIL` | revise page label, hierarchy, or first action and retest |
| control label does not predict its result | `FAIL` | use an explicit action label and add outcome/recovery copy |
| long copy has no usable scan path | `FAIL` | add meaningful headings, lists, and grouping without deleting required meaning |
| error or empty state has no recovery | `FAIL` | state what happened and provide retry, back, alternate, or support path |
| only static inspection was available | `NOT_ASSESSED` | run rendered/manual task evidence before release |

The representative synthetic record in
`fixtures/website-multilingual/question-mark-scan.json` and
`tests/test_kaizen_phase1.py` checks the normal and failure shapes. It is lab
evidence only; accessibility, browser, and user evidence remain unassessed.

## References

- `../SKILL.md` for the read-only accessibility gate and degraded-mode rules.
- `../../../build/i18n/SKILL.md` for locale expansion and missing-content states.
- `C:/wamp64/www/design-system-skills/skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/SKILL.md`
  for navigation, labels, wayfinding, and hierarchy ownership.
