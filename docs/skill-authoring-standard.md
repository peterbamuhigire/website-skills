# Website Skills Authoring Standard

This repository applies the July 2026 portable skill contract to every active `skills/<category>/<name>/SKILL.md`. The active catalogue is discovered from the filesystem; `skills/manifest.yml` records it but does not define it.

## Entrypoint contract

Every active skill must meet all of these conditions:

1. YAML frontmatter contains only `name`, `description`, `license`, `allowed-tools`, and `metadata`. `name` matches the directory. `description` is one line, begins with `Use when`, is at most 350 characters, names a concrete trigger, and distinguishes a neighbour.
2. `metadata.portable` is `true`; `metadata.compatible_with` is exactly `claude-code`, then `codex`.
3. The first level-one heading is followed immediately by the repository acknowledgement required in `AGENTS.md`.
4. `Use When` and `Do Not Use When` state positive and negative routing conditions.
5. `Inputs` or `Required Inputs` is a table naming the artefact, source or provider, requirement, purpose, and missing-input behaviour. A genuinely foundational skill may state `None` and explain why.
6. `Workflow` is ordered. It includes a decision point, a stop condition, and recovery after a missing input or failed check.
7. `Outputs` names each artefact, consumer, and observable acceptance condition.
8. `Evidence Produced` names evidence that another operator can inspect. Evidence-bearing delivery may not substitute an assertion for a file, command result, review record, or measured outcome.
9. `Capability Contract` states minimum read, search, edit, execute, network, publish, and delegation needs as applicable. Review, audit, critique, analysis, and planning default to read-only. Mutation, production access, spending, destructive actions, certification, and publication require explicit authority.
10. `Degraded Mode` returns the narrowest useful qualified result. An unavailable check is `not assessed`, never passed.
11. `Decision Rules` is a domain-specific table with the choice, action, and failure or risk avoided.
12. `Quality Standards` is non-empty. `Anti-Patterns` contains at least five concrete mistakes, each paired with a correction.
13. `References` links directly to every resource needed by the entrypoint. New or extracted `references/*.md` files link back to their parent `SKILL.md`.
14. Include a worked example when an output schema, judgement call, or recovery path would otherwise be ambiguous.
15. Keep `SKILL.md` at 500 lines or fewer. Move catalogues, schemas, case studies, and background into directly linked references without moving routing, safety, decisions, workflow, outputs, degraded mode, or acceptance out of the entrypoint.

## Portable wording

Describe capabilities, not runner commands. Say “search the repository” or “execute the repository validator” in a skill body. Put tool names, model settings, and runner syntax in adapters or repository instructions.

Use British English. Keep claims qualified by evidence. Preserve specific domain language and examples; conformance scaffolding is not a replacement for judgement.

## Authoring and release gates

Start new skills from `templates/skill/SKILL.md`. Before merge or release, run:

```powershell
python -X utf8 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json
python -X utf8 scripts/routing-smoke-test.py
python -X utf8 scripts/validate-search-doctrine.py
python -m pytest -q
```

Then run the canonical `quick_validate.py` against each skill directory and the canonical `engine_compliance.py` against the `skills` active root. A zero-debt baseline is an assertion, not a waiver: any finding fails the gate.

## Change boundary

Do not add, rename, deactivate, merge, or remove a skill solely to improve a score. Update `skills/manifest.yml`, routing fixtures, neighbour descriptions, and current catalogue counts whenever an authorised catalogue change occurs.
