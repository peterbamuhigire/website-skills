# Documentation wave: follow-ups (31 October 2026)

The documentation wave brought the README, `AGENTS.md`, `CONTRIBUTING.md`, `docs/skill-authoring-standard.md` and `docs/relocation-map.md` in line with the repository, and added `docs/README.md`. Everything below was found during that wave and deliberately left alone, because it is a skill, a control file or a decision for the owner. Every figure was measured on 2026-10-31.

## Changes the documentation wave did not make

| Item | Where | Why it is open |
|---|---|---|
| No `CHANGELOG.md` | repository root | The engine has never kept one: the references to a changelog in `glossary.md` and `templates/README.md` describe a client project's `project-log/CHANGELOG.md`. The commit history and the two kaizen final reports carry the record. Starting a changelog is an owner decision; none was created. |
| Declared and CI-run validators differ | `.skills-engine/engine-manifest.yaml`, `.github/workflows/skill-engine-quality.yml` | The manifest declares eight validators with `python`; CI also runs the size check, the vendored-detector comparison, the slop-pack validator and the hook tests, and does not run `validate-skill-registry.py`. The manifest is a control contract, so it was not edited. `python` resolves on this host; `python3` is the portable spelling. The README documents the real difference. |
| An agent-integration test pytest does not run | `tests/agent-integration/test_website_agent_contract.py` | pytest collects zero tests from it because it is a script with `main()`; run directly it prints `PASS`. It is not a CI step. Its catalogue lookup builds `ROOT.parent / "chwezi-engine-agents"`, so it does not honour `CHWEZI_ENGINES_ROOT`. It works on this host only because the sibling has that folder name; a configurable root would match `scripts/design_engine_root.py`. |
| A Node test outside CI | `tests/a11y-gate-context.test.mjs` | Two tests, pass under `node --test`, referenced by no workflow and no manifest entry. |
| `unittest` cannot run the suite | nine modules under `tests/` | They import `pytest`; `python3 -m unittest discover -s tests` ran 10 tests and failed to import nine modules. The README now states that pytest is a hard prerequisite. Converting the suite is the existing P2 item in `06-next-cycle.md`. |
| Public roadmap not reviewed since 2026-08-11 | `docs/roadmap-public.md`, `docs/plans/INDEX.md` | The roadmap states a quarterly cadence and its "In-flight" and "Priorities for next quarter" lists predate both October cycles. They are public commitments, so the owner should refresh them; the documentation wave did not. |
| Evidence READMEs describe branches | `docs/kaizen/2026-10-engine-kaizen/README.md`, `docs/kaizen/2026-10-engine-kaizen-pass-2/README.md` | They say the work is on `kaizen/2026-10` and `kaizen/2026-10-pass2` and unpushed. Both branches are now contained in `main` (`git branch --contains` lists `main`). They are frozen records and were not edited; the README "Quality and improvement" section states where the work lives now. |
| Behaviour of the slop scan after a re-sync | `scripts/slop-scan.sh`, `skills/quality-gates/visual-qa/references/hierarchy-overflow-checks.md` | See "The vendored detector re-sync" below. No skill text was changed. |

## Cross-engine mismatches found, not edited

- Any portfolio note that says this engine embeds `proposal-skills` is out of date. At this commit it does not: there is no `.gitmodules` and no gitlink in `git ls-tree HEAD`, and commit `37780ba` (2026-06-17, "Remove cross-engine submodule; routing handles engine awareness") removed the submodule. `AGENTS.md` ("External Skill Set") and `docs/licensing-matrix.md` already say it is external, and the README now says the same. The `proposal-skills` README does not name this engine, so there was no wording to match; nothing was edited there.
- The portfolio catalogue (`catalog/engines.yaml` in `chwezi-engine-agents`, lines 100 and 101) gives the repository name of the research engine as `digital-research-skills`. `gh api repos/peterbamuhigire/digital-research-skills` returns a repository whose `full_name` is `peterbamuhigire/chwezi-research-engine` (id 1221137180), and `digital-research-engine` returns 404. This README therefore links no research-engine URL and refers to the engine by name through the routing table. The other three renamed engines resolve to `chwezi-design-engine`, `chwezi-dev-engine` and `chwezi-sdlc-documentation` as stated.

## The vendored detector re-sync

The first P0 row of `06-next-cycle.md` asked for a reviewed re-sync of `scripts/vendor/chwezi-slop/` after the design engine's cycle settled. It was done in commit `ae6487c` with `check-vendored-detector.py --sync-from`, from a read-only snapshot of the design engine at commit `72a3a37` (the snapshot was clean, 0 uncommitted files).

| Item | Before | After |
|---|---|---|
| `VENDOR.json` `source_commit` | `3fe84a6dc22d954483e1afce06c3e9b53fc2f5ca` | `72a3a37817a8c94b39e4edd083d24b730151c17d` |
| Files changed | | `lib/browser-rules.mjs`, `lib/checks.mjs`, `rules/registry.json`, `VENDOR.json` (133 lines added, 8 removed); the other 17 vendored files were byte-identical |
| Registry rules | 49 | 51 (`positive-tabindex`, tier deep, warning; `target-size-minimum`, tier browser, warning) |
| `check-vendored-detector.py` | exit 1, `DRIFT` on three files | exit 0, manifest and source comparison PASS |
| `validate-slop-pack.mjs` | 20 pack rules against 49 registry rules | 20 against 51 |
| Full pytest (pytest 9.0.3, clean clone with the change applied) | 280 passed | 280 passed |
| Slop scan of `examples/service-site-five-page/site` | 0 block, 0 warning, 0 advisory | 0 block, 0 warning, 0 advisory |

Behaviour change to know about: `slop-scan.sh` runs the detector with `--tier deep --fail-on warning`. A test page holding `<a href="/contact" tabindex="3">` passed before the re-sync and fails after it with one warning, which blocks. The target-size rule is browser tier, so the deep-tier scan does not run it; it needs a browser and was not run (`NOT_ASSESSED`). Whether the website slop pack (`quality/slop-rules.website.json`) should carry entries for the two rules, and whether `skills/quality-gates/visual-qa/references/hierarchy-overflow-checks.md` should name the positive-tabindex warning, are decisions left to the owner. The design engine moved on after the snapshot (its checkout is now at a later commit); the three vendored files still match it, so the default check passes against both.

