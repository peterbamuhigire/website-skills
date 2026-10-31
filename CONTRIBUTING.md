# Contributing to Website Skills

This repository accepts changes that preserve the 62-skill portable catalogue, domain knowledge, routing clarity, and release evidence.

## Author or update a skill

1. Read `AGENTS.md`, `docs/skill-authoring-standard.md`, the target `SKILL.md`, its directly needed references, and the closest neighbour descriptions.
2. Start a new skill from `templates/skill/SKILL.md`. Do not add a skill solely to improve a catalogue metric.
3. Preserve the acknowledgement immediately below the first level-one heading.
4. Keep the entrypoint at 500 lines or fewer. Put background, long schemas, catalogues, and cases in directly linked `references/` files; new extracted references link back to the parent skill.
5. Add or update positive, negative, collision, limited-capability, and failure fixtures in `tests/routing/fixtures.json` when routing changes.
6. Run `skill-safety-audit` for a material skill change.
7. Never store book extractions or book summaries in the repository. Turn a book method into a task-oriented reference in original words with a brief citation.

## Local gates

Run these from the repository root. They need Python 3.11 or later with `PyYAML` and `pytest`, and Node.js 18 or later; the README lists what each check needs and what it reports when a dependency is missing.

```sh
python3 -X utf8 scripts/validate-checkout-size.py
python3 -X utf8 scripts/validate-skill-registry.py
python3 -X utf8 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json
python3 -X utf8 scripts/routing-smoke-test.py --min-rank1 92 --lint-fixtures
python3 -X utf8 scripts/validate-search-doctrine.py
python3 -X utf8 scripts/validate-source-registers.py
python3 -X utf8 scripts/check_portable_references.py
python3 -X utf8 scripts/source_ingestion_guardrail.py --root .
python3 -X utf8 scripts/check-vendored-detector.py
node scripts/validate-slop-pack.mjs
for t in hooks/test-*.js; do node "$t" || exit 1; done
python3 -m pytest -q
```

On Windows, run the same commands from Git Bash. The vendored-detector check compares with the design engine when it finds a checkout (set `CHWEZI_DESIGN_ENGINE_ROOT` or `CHWEZI_ENGINES_ROOT`); without one that comparison is `NOT_ASSESSED`, not a pass. When `validate-source-registers.py` or `validate-search-doctrine.py` reports an overdue review date, re-check the source and record the result before moving the date.

Also run the canonical July 2026 validators from the `chwezi-dev-engine` engine:

```sh
python3 -X utf8 <chwezi-dev-engine>/skills/sdlc-meta/skill-writing/scripts/quick_validate.py <skill-directory>
python3 -X utf8 <chwezi-dev-engine>/skills/sdlc-meta/skill-engine-audit/scripts/engine_compliance.py --root <website-skills-root> --active-root skills --details
```

Run `git diff --check`, inspect the complete diff, and remove caches or generated scratch files. The zero-debt baseline is not a suppression list; any structural finding or failed routing fixture blocks release.

## Catalogue changes

Adding, renaming, relocating, deactivating, or removing a skill requires an independent routing reason and repository authority. Regenerate `skills/manifest.yml`, update current counts and routes, and add migration evidence. Preserve inactive knowledge according to `docs/deprecation-policy.md`.

## Release procedure

Fetch `origin`, confirm local `main` is not behind, run every gate, stage only intended files, and review the staged diff. Never force-push. If remote history, branch protection, authentication, or CI blocks the release, preserve the local commit and report the exact blocker.
