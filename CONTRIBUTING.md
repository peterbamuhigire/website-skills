# Contributing to Website Skills

This repository accepts changes that preserve the 59-skill portable catalogue, domain knowledge, routing clarity, and release evidence.

## Author or update a skill

1. Read `AGENTS.md`, `docs/skill-authoring-standard.md`, the target `SKILL.md`, its directly needed references, and the closest neighbour descriptions.
2. Start a new skill from `templates/skill/SKILL.md`. Do not add a skill solely to improve a catalogue metric.
3. Preserve the acknowledgement immediately below the first level-one heading.
4. Keep the entrypoint at 500 lines or fewer. Put background, long schemas, catalogues, and cases in directly linked `references/` files; new extracted references link back to the parent skill.
5. Add or update positive, negative, collision, limited-capability, and failure fixtures in `tests/routing/fixtures.json` when routing changes.
6. Run `skill-safety-audit` for a material skill change.

## Local gates

```powershell
python -X utf8 scripts/validate-skill-registry.py
python -X utf8 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json
python -X utf8 scripts/routing-smoke-test.py
python -m pytest -q
```

Also run the canonical July 2026 validators from the `skills-web-dev` engine:

```powershell
python -X utf8 <skills-web-dev>/skills/sdlc-meta/skill-writing/scripts/quick_validate.py <skill-directory>
python -X utf8 <skills-web-dev>/skills/sdlc-meta/skill-engine-audit/scripts/engine_compliance.py --root <website-skills-root> --active-root skills --details
```

Run `git diff --check`, inspect the complete diff, and remove caches or generated scratch files. The zero-debt baseline is not a suppression list; any structural finding or failed routing fixture blocks release.

## Catalogue changes

Adding, renaming, relocating, deactivating, or removing a skill requires an independent routing reason and repository authority. Regenerate `skills/manifest.yml`, update current counts and routes, and add migration evidence. Preserve inactive knowledge according to `docs/deprecation-policy.md`.

## Release procedure

Fetch `origin`, confirm local `main` is not behind, run every gate, stage only intended files, and review the staged diff. Never force-push. If remote history, branch protection, authentication, or CI blocks the release, preserve the local commit and report the exact blocker.
