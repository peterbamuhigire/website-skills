# README measured refresh and photo caption standard, 5 November 2026

## Photo caption standard

Commit `4323eab` (1 November 2026) changed two files:

- `skills/build/photo-manager/SKILL.md`: a quality-bar line and an anti-pattern. Rights, licence, permission, source and representation details belong in the asset catalogue or internal notes. A disclaimer is never a reader-facing caption.
- `skills/content-copy/blog-writer/references/article-design.md`: the captions row now reads "When used, connect the image to a practical point in the article", and a new Caption Standard section forbids disclaimer captions (for example, saying that a photo is illustrative or shows no real project) and asks for a caption that names a decision, check, handover, responsibility or next step.

The README did not mention it. The README's "Quality and improvement" section now does.

## Re-run on 2026-11-05

Run from the repository root on Linux in a fresh virtual environment (Python 3.14.10, pytest 9.2.0, PyYAML 6.0.3):

| Command | Exit | Result |
|---|---|---|
| `python3 -X utf8 scripts/validate-skill-registry.py` | 0 | `design routes: PASS (15 routed design skills exist)`, `registry valid: 62 skills` |
| `python3 -m pytest -q -p no:cacheprovider` | 0 | 280 passed |

The README's "At a glance" test bullet now carries the date and versions of this run. No other check was re-run, so the 2026-10-31 results elsewhere in the README stand as written.

## Not assessed

The browser gates, `npm audit`, post-deploy smoke checks and rollback were not run on this host. They need a consuming project with the locked tools installed.
