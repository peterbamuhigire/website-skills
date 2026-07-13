---
name: image-compression
description: Use when generating measured web-image derivatives from approved source assets; do not use for cataloguing, selecting, or licensing photographs, which belongs to photo-manager.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Image Compression
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- Approved raster assets need responsive, measured derivatives that meet the project's image-weight and quality budgets.
- A build pipeline needs reproducible encoding settings and a manifest of source/output dimensions, bytes, and formats.

## Do not use when
- The work is asset selection, rights, naming, cataloguing, or placement; use `photo-manager`.
- The source image is unapproved or its intended display size is unknown; measure only and request the missing input.
- The task is runtime image delivery/component markup; route to `page-builder` after derivatives exist.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Approved source images and usage mapping | `photo-manager` catalogue | yes | Stop; do not process unknown or unapproved files. |
| Target dimensions, formats, quality, and weight budget | Performance/design brief | yes | Measure originals and propose settings without overwriting assets. |
| Build tool and output paths | Repository | yes | Return a command/config plan only. |

## Workflow
1. Inventory approved sources and target placements; stop if rights, destination, or budgets are unresolved.
2. Measure source dimensions, format, bytes, alpha, and animation before selecting an encoder path.
3. Generate bounded responsive derivatives without upscaling or overwriting sources.
4. Decode and visually inspect outputs, then record before/after facts in the manifest.
5. Reject outputs that fail decode, budget, or quality and retry by reducing dimensions or changing format.
6. If tooling fails, preserve originals and partial evidence, remove unusable derivatives, and return reproducible recovery settings.

## Quality standards
- Every derivative decodes, stays within source dimensions, and has measured bytes/dimensions recorded.
- Quality and weight decisions reflect actual placement rather than one global quality number.
- Sources remain intact until downstream asset reconciliation is complete.

## Anti-patterns
- Compressing before placement sizes are known. Fix: derive widths from rendering needs.
- Upscaling a raster source. Fix: cap derivatives at source dimensions.
- Using one quality setting for all assets. Fix: inspect each output class.
- Reporting savings without measurement. Fix: record bytes and decode status.
- Overwriting originals. Fix: generate separate derivatives and preserve sources.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not upscale raster images; cap output at the source dimensions.
- Do not replace originals or delete sources until derivatives and catalogue links are verified.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Optimised image derivatives | `page-builder` and build pipeline | Files decode, meet declared dimensions/format/budget, and preserve acceptable visual quality. |
| Compression manifest | QA and maintainers | Records source, output, dimensions, bytes, format, and reduction for every derivative. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Before/after measurements | Manifest plus decode check | Every claimed saving is calculated from actual file sizes. |

## Capability Contract
Inspect and measure read-only by default. Generate derivatives only when file mutation is authorised. Never delete sources, change rights metadata, or install tooling without explicit authority.

## Degraded Mode
If the encoder or visual inspection is unavailable, produce recommended settings and an unassessed manifest; do not claim compression, quality, or decode success. Preserve all source files.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Photo supports modern formats | Generate responsive AVIF/WebP plus required fallback | Excess transfer weight |
| Graphic needs lossless edges/transparency | Use lossless-capable output | Artefacts and broken transparency |
| Output exceeds budget | Reduce dimensions before excessive quality loss | Blurry large files |
| Derivative fails decode or visual check | Reject and retain source | Broken production media |

## Worked Example
For a 2400-pixel hero photograph, generate bounded responsive widths, record WebP and AVIF byte sizes, decode each output, and retain the source. If the 1280-pixel candidate misses the project budget, reduce dimensions before forcing visibly damaged quality.

## References

- [Preserved image-compression guidance](references/legacy-guidance.md)

<!-- dual-compat-end -->
