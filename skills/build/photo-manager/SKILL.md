---
name: photo-manager
description: Use when cataloguing, renaming, dimensioning, selecting, approving, and placing the correct logo and website photographs; do not use for derivative encoding alone, which belongs to image-compression.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Photo Manager
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- New photos or logos must be inspected, deduplicated, named, rights-qualified, catalogued, and assigned to website placements.
- A photo library needs the correct logo or website photographs selected, renamed, dimensioned, and catalogued before encoding.
- `photo-bank/` needs safe staging reconciliation with `src/assets/images/` and `_catalog.json`.

## Do not use when
- The task is derivative format/quality/weight optimisation only; use `image-compression`.
- The task is page markup or responsive image rendering; use `page-builder` after cataloguing.
- Rights, source location, or destination are unknown; inventory only and stop before placement.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Source asset directory and existing catalogue | Project files | yes | Stop; do not search unrelated paths or invent catalogue records. |
| Placement needs, brand rules, alt-text context, and rights status | Content/design brief | yes | Catalogue technical facts only and mark placement/rights pending. |
| Destination and naming convention | Repository | yes | Return a proposed mapping without copying files. |

## Workflow
1. Inventory staging and existing assets, rights evidence, catalogue entries, and placement needs; stop on unauthorised sources.
2. Inspect decode, dimensions, orientation, duplicates, subject, and naming collisions without inventing metadata.
3. Decide approve, quarantine, or reject for each asset and assign stable names and usage metadata.
4. Copy approved assets, update `_catalog.json`, and validate destination decode and reconciliation.
5. Apply the cleanup rule only to source files copied and catalogued in this run.
6. Recovery: on copy/catalogue failure, preserve the source, repair or roll back the incomplete entry, and recheck reconciliation.

## photo-bank cleanup rule (required)
- After a photo-bank file is copied into `src/assets/images/` AND its entry is recorded in `_catalog.json`, DELETE the original from `photo-bank/`. The asset copy is the canonical version; the photo-bank is a staging area, not an archive.
- Delete ONLY files you have actually copied and cataloged in this run. Never delete a photo-bank file that was not copied to assets — unused photos stay in `photo-bank/` for future articles.
- Verify the asset copy exists at its destination path before deleting the source. Do not delete on a failed or partial copy.
- This keeps `photo-bank/` showing only un-placed photos, so it doubles as the "still needs a slot" queue.

## Quality standards
- Catalogue records reconcile to real decodable files, dimensions, placements, alt intent, and rights status.
- Names are stable, descriptive, collision-free, and independent of a single host install path.
- Every staging deletion traces to a verified destination and catalogue entry from the same run.

## Anti-patterns
- Selecting imagery from filenames. Fix: inspect the decoded asset and placement context.
- Inferring rights, people, or locations. Fix: record unknown until evidence is supplied.
- Allowing name collisions. Fix: assign stable descriptive unique names.
- Omitting alt intent or rights status. Fix: store both in the catalogue.
- Deleting staging files early. Fix: verify destination decode and catalogue first.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not infer licences, subjects, locations, or consent from filenames; record unknown.
- Do not delete a staging file until its destination exists and its catalogue entry validates.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Asset files in approved destination | `image-compression` and `page-builder` | Names are unique, files decode, and only authorised sources were copied. |
| `_catalog.json` | Build and content teams | Every placed asset has path, dimensions, category, usage, alt-text status, and rights status. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Asset reconciliation | Source-to-destination-to-catalogue register | Counts match and every deletion traces to a verified copy. |

## Capability Contract
Inventory and assess read-only by default. Copy, rename, update catalogues, or apply the staging cleanup rule only when file mutation is authorised. Never delete unplaced files or assert usage rights without evidence.

## Degraded Mode
If metadata extraction, decoding, rights evidence, or write access is unavailable, return an inventory with unknown fields and proposed placements. Do not delete, copy, or mark an asset approved.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Rights and placement are approved | Copy, catalogue, verify, then clean staging source | Orphaned or unlawful use |
| Destination name collides | Derive a stable descriptive unique name | Silent overwrite |
| Asset is decorative | Record empty alt intent | Noisy accessibility text |
| Subject or rights are unknown | Quarantine from production placement | Misrepresentation or rights risk |

## Worked Example
For an approved team portrait, record dimensions and rights evidence, copy it under a stable descriptive name, add its page-specific alt-text status to `_catalog.json`, verify the destination decodes, and only then remove that exact staging file. Leave every unused photo in `photo-bank/`.

## References

- [Preserved photo-management guidance](references/legacy-guidance.md)

<!-- dual-compat-end -->
