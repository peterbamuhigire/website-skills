---
name: brand-voice
description: Use when copy needs a client's actual voice reproduced consistently across pages, blog posts, and campaigns; use content-writing for page-strategy drafting and premium-commercial-writing's slop gate for the release-time quality floor.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Brand Voice
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Build a reusable voice profile by measuring a client's real, approved writing, then reuse that profile everywhere instead of describing tone in adjectives or defaulting to generic AI phrasing.

<!-- dual-compat-start -->
## Use When

- A client has existing approved copy (site pages, newsletters, social posts, sales emails) and new copy must sound like the same author.
- Multiple writers or sessions need to produce copy that reads as one consistent voice.
- A brand brief describes tone only in adjectives ("friendly", "professional") and copy keeps drifting toward generic AI phrasing despite that brief.
- `content-writing`, `blog-writer`, `sales-copywriting`, or a social-media workflow needs a voice input before drafting.

## Do Not Use When

- No real client-approved source material exists yet and none can be gathered; use `brand-strategy` to establish positioning first, then return here once real copy exists to measure.
- The task is page structure, message hierarchy, or persuasion framework, not voice; use `content-writing`, `sales-copywriting`, or `long-form-sales-copy`.
- The only need is a mechanical banned-phrase check on a finished draft; run `scripts/banned-phrase-scan.sh` directly.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| 5-20 real, client-approved writing samples (site copy, emails, social posts, newsletters, transcripts of the client speaking) | Client, CRM, CMS export, or site crawl | yes | Measure the actual voice instead of guessing it | Stop; state that no voice profile can be built without real samples, and route to `brand-strategy` to source them |
| Channel targets for reuse (web, email, social, ads) | Client brief or upstream skill | conditional | Capture channel-specific variation in the profile | Build a single cross-channel profile and note channels are undifferentiated |

## Workflow

1. Confirm at least 5 real, client-approved samples exist; reject brand adjectives, competitor examples, or generic "voice like X celebrity" requests as substitutes for real source material.
2. Separate samples by channel if the source set clearly splits (e.g. formal site copy vs. casual social captions); note the split rather than averaging it away.
3. Extract, from the samples only: sentence rhythm and length, compression vs. explanation, how claims are made and proved, question use, transition style, capitalisation and punctuation norms, and what the author never does — using [the voice profile schema](references/voice-profile-schema.md).
4. Cross-check every extracted trait against the source set; discard any trait that cannot be pointed to in a real sample.
5. Produce the `VOICE PROFILE` block per the schema, including a `Banned Moves` list of phrasing the samples never use.
6. Merge the profile's `Banned Moves` with the mechanical catalogue in [banned-phrases.md](references/banned-phrases.md); run `scripts/banned-phrase-scan.sh` against the finished draft before handoff, and treat any hit as a stop condition, not a style note.
7. Hand the profile to the downstream drafting skill (`content-writing`, `blog-writer`, `sales-copywriting`, or a social workflow); do not re-derive voice inside those skills once a profile exists for this client.
8. If new approved samples arrive later that contradict the profile, rebuild the affected sections and record the change; do not silently average old and new voice.

Recovery: if the banned-phrase scan fails after drafting, rewrite the flagged lines and rerun the scan only (not the full workflow) before handoff.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| `VOICE PROFILE` block | Downstream content-copy skills, this engine's social-media and launch-campaign workflows | Every trait traces to an observable pattern in the supplied samples; no trait is asserted from adjectives alone |
| Banned-phrase scan result | Editor or release owner | `scripts/banned-phrase-scan.sh` run against the final draft with 0 hits, or hits resolved and rerun |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source sample list with channel and date | Client or editor | Every sample is real, attributable, and dated; none are invented or paraphrased from adjectives |
| Banned-phrase scan output | Release owner | Raw scan output (file, line, matched pattern) preserved, not summarised as "checked voice" |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required to gather source samples. Running `scripts/banned-phrase-scan.sh` requires execute access to a local shell. No network, publish, or production-mutation authority is required by this skill itself.

## Degraded Mode

If fewer than 5 samples are available but at least one clearly attributable sample exists, return the narrowest qualified profile: build only the sections the samples support, mark it `low-confidence`, and mark every unconfirmed trait `not assessed` rather than guessed. If zero real samples exist, do not build a profile — return to `Do Not Use When` and route to sourcing.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Fewer than 5 samples, but at least 1 | Build a `low-confidence` profile and say so | Presenting a guessed voice as measured |
| Samples split cleanly by channel or register | Keep separate `Channel Notes` rather than averaging | A flattened voice that fits no channel well |
| Banned-phrase scan finds a hit | Stop handoff, rewrite the line, rerun the scan | Shipping AI-slop phrasing under a "voice-approved" label |
| New approved samples contradict the current profile | Rebuild the affected profile sections | A stale profile silently drifting from the client's actual current voice |

## Quality Standards

- Every trait in the `VOICE PROFILE` is backed by a specific, citable sample — not an adjective.
- The profile distinguishes what the author does from what the author explicitly never does.
- `scripts/banned-phrase-scan.sh` is run against the final draft and its raw output, not a summary, is kept as evidence.
- Channel-specific variation is preserved when the source set supports it.

## Anti-Patterns

- Building a voice profile from a client's brand adjectives instead of real writing. Fix: stop and request real samples.
- Averaging a source set that clearly splits into "formal site" and "casual social" voices into one flat profile. Fix: keep separate channel notes.
- Treating a banned-phrase scan hit as an optional style suggestion. Fix: treat it as a stop condition before handoff.
- Re-deriving voice from scratch inside `content-writing` or `blog-writer` after a profile already exists for the client. Fix: reuse the existing `VOICE PROFILE`.
- Letting an old profile stand after new, contradictory approved samples arrive. Fix: rebuild the affected sections and record the change.
- Calling generic positive adjectives ("engaging", "authentic") a voice profile. Fix: every entry must trace to an observed pattern.

## Worked Example

A client supplies 12 newsletter issues and 6 landing pages. The newsletters are short, question-led, and informal; the landing pages are longer and claim-led with no questions. The profile records two `Channel Notes` entries rather than one blended voice, lists "never opens with a question" as a landing-page `Banned Move`, and a new blog draft is checked against `scripts/banned-phrase-scan.sh` before handoff — it fails on "In today's fast-paced digital world", the line is rewritten to name the client's actual Tuesday-morning newsletter routine, and the scan is rerun clean.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)
- [Voice profile schema](references/voice-profile-schema.md)
- [Banned phrases — copy draft gate](references/banned-phrases.md)
- [Genuine writing and AI-slop gate](../premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md)
- [`scripts/banned-phrase-scan.sh`](../../../scripts/banned-phrase-scan.sh)
