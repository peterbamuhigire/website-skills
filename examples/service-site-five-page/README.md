# Five-page service site: worked example

A complete, synthetic deliverable for a fictional bicycle repair workshop: the brief it was built from, five pages, a release record that says which gates ran and which did not, and a rollback plan. It shows what finished output and honest release evidence look like for the `website-builder` route. Every business detail is fictional and the domain is `example.com`, which is reserved for documentation. **Do not deploy it.**

| File | What it is |
|---|---|
| [`brief.md`](brief.md) | The source document. Every claim on the pages comes from it; nothing was added. |
| [`site/`](site) | The built site: five pages, one stylesheet, no JavaScript, a decorative SVG mark, a share image, `robots.txt`, `sitemap.xml`, `.well-known/security.txt`. The folder is not called `dist` because that name is git-ignored. |
| [`release-evidence.json`](release-evidence.json) | The release record, in the engine's `release-evidence` artefact format (`templates/project-artifacts/`). |

`tests/test_worked_service_site.py` runs every gate named below and fails if the record and the real result disagree, so this page cannot drift into a claim nobody checked.

## How it was built

The build followed the `website-builder` sequence, using only what the brief supplies.

1. **Scope and content.** One audience (commuters and school-run parents), one conversion (a booking request by email), five pages. The brief rules out a form, a calendar, payment, analytics and photography, so none appear. With no price list in the brief, the site explains how quoting works and states no price.
2. **Language.** One language, British English, `lang="en-GB"`. No locale routing.
3. **Design system.** Public Sans for text and Source Serif 4 for headings, the pairing the engine's passing slop fixture uses, with a system fallback. Reason: both are plain and readable at small sizes on low-end phones. No font files are bundled (licence and the 5,000-entry package cap), so the page renders in the fallback face and the font weight in the budget gate reads 0 KB. **That figure is not representative of a shipped site.** A real build self-hosts WOFF2 files with `font-display: swap` and preloads the one face used above the fold. Colour is one blue on white; every text pair is above 4.5:1; there are no gradients and no motion.
4. **Pages.** Text-first. The largest-contentful element is the `h1`. Skip link, landmarks, one `h1` per page, a labelled navigation, a real table with a caption and header cells, visible focus, targets of at least 44 px.
5. **Search and metadata.** Unique title and description per page, canonical URL, share tags, sitemap, `robots.txt` that allows crawling, and a `security.txt` with the fields the engine requires.
6. **Release.** The offline gates below, then the decision and plan in this file.

## Gate results

Run from the engine checkout. `{site}` is `examples/service-site-five-page/site`. Results are those the test reproduces.

| Gate | Result | What it proves, and its limit |
|---|---|---|
| `html-perf-lint` | Pass, no warnings | No render-blocking head script, every image sized, no `document.write`. |
| `route-weight-budget` | Pass, 2.4 to 2.7 KB per route | Inside the engine's budgets. Font weight is 0 KB (see above). |
| `metadata-audit` | Pass | Title, description, canonical, share tags, `html lang`, zoom-safe viewport. |
| `banned-phrase-scan` | Pass, 0 hits in 26 patterns | No catalogued filler phrase. It cannot judge whether the copy is good. |
| `content-link-graph` | Pass, 5 pages, 20 links | No broken link, orphan or unreachable page. |
| `sri` | Pass | No external script or stylesheet at all. |
| `slop-scan` | Pass, 0 findings | The vendored detector's registry finds no banned font, gradient or filler headline. |
| `secrets-scan` | Pass | No credential-shaped string in a scratch repository holding the site. |
| `security-txt` | **Fail, by design** | One failed check, `placeholder value found`: the gate rejects `example.com`. Every other check passes. |

Each of these gates also fails when its defect is injected into a copy of the site: a missing `lang`, a zoom-blocking viewport, a missing canonical link, a filler phrase, a broken link, an external script without integrity metadata, an image without dimensions, a render-blocking script, a 300 KB image above the fold, a banned font and a credential-shaped string. The test runs all eleven.

### Not assessed

| Gate | Why it did not run |
|---|---|
| `a11y-gate` | Needs a consuming project with exact locked Playwright and axe-core versions and a browser. The static `lang` and viewport checks in `metadata-audit` are partial twins only. |
| `perf-gate-lighthouse` | Needs a locked Lighthouse CI toolchain and a browser. Field Core Web Vitals are a separate measure. |
| `visual-qa` | Needs locked Playwright, a browser and committed baselines. |
| `security-headers` | Needs a served preview or staging URL. Local preview does not prove edge configuration. |
| `security-gate-audit-and-supply-chain` | Needs the project's `package-lock.json`. The audit step stops with exit 6 when it cannot run; it is never read as zero findings. |
| `design-quality-score-rubric` | The score is a reviewer judgement; no scored report exists. |
| `post-deploy-smoke` | No deployment target for a fictional business. |
| `remote-rollback` | No host. Local validation of the helper's inputs passes (see the plan below). |

## Release decision: BLOCKED

1. `security-txt` fails: the domain and the security contact are placeholders.
2. Eight checks above are not assessed; an unassessed gate is not a pass.
3. No owner, domain, hosting target, legal review of the privacy page or rollback rehearsal exists. The privacy page describes only what this site does (no cookies, analytics or forms) and says it needs review against the law that applies; that review is not done.

To release a real site built this way: supply the owner's domain and contacts, install and lock the QA tools in the project, run the unrun gates in the canonical pipeline, have a reviewer score the design rubric, have the privacy wording reviewed, rehearse the rollback, and record the result in `release-evidence.json`. Do not edit the record to "pass" without a run.

## Rollback plan

For a real release of this pattern on a VPS or static host. The mechanism is the engine's own: `scripts/rollback.sh`, described in `skills/launch-ops/deploy/references/rollback-runbook.md`.

- **Release layout.** Each release lives in `releases/<release-id>/`. `current` is a symlink to the live release and `previous` to the last known-good one. Keep at least three releases.
- **Last known-good release.** The release id recorded in `release-evidence.json` before promotion. For a first release there is no earlier build, so the rollback is to point `current` at a holding page the owner has approved. If nobody can name the last known-good release, the release is not ready.
- **Rollback triggers.** The booking email link is missing or wrong; any of the five pages is missing, corrupted or returns an error; navigation is broken; the canonical URL points at the wrong host; the deployed artefact does not match the recorded one.
- **Authority.** The site owner approves; the release lead executes. The helper refuses to run unless `ROLLBACK_APPROVED=yes`, `ROLLBACK_TARGET` equals `DEPLOY_PATH`, a readable pre-provisioned known-hosts file exists and `ROLLBACK_REASON` is recorded. Credentials come from the pipeline's secret store, never from this repository.
- **Procedure.** Declare the rollback and pause other changes. Run the helper: it checks that `current` and `previous` are distinct release folders inside `releases/`, swaps the two symlinks atomically, verifies the pair, reloads the web server and, if any step fails, restores and re-verifies the original pair. Then verify the restored site.
- **Verification after rollback.** Run `scripts/post-deploy-smoke.sh` against the live URL, open all five routes, and click the booking email link. Record the incident with the rollback record template in the runbook, and tell the owner using the launch communication template.
- **What was tested here.** With `ROLLBACK_VALIDATE_ONLY=1` and no host, the helper exits 3 when authority is missing, exits 3 when the target differs from the deploy path, and exits 0 for an authorised exact target, stating that remote state is not assessed. The test in `tests/test_worked_service_site.py` repeats those three cases. A remote rollback has never run for this example.

## Reproduce

```bash
python3 -m pytest tests/test_worked_service_site.py        # with pytest installed
bash scripts/metadata-audit.sh examples/service-site-five-page/site
node scripts/html-perf-lint.mjs examples/service-site-five-page/site
```

Gate scripts write reports to the current directory's `reports/` folder, which is git-ignored.

## What this example does not show

A site with images, a form, several languages or a catalogue; the browser-based gates passing on a real toolchain; field performance; a real deployment. It is the smallest complete deliverable, not a template to copy copy from.
