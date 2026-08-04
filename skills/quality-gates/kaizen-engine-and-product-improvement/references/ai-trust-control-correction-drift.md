# AI trust, control, correction, and drift gate

[Owning skill](../SKILL.md)

Use this reference for any website feature that predicts, generates, recommends, classifies, ranks, or acts with AI.

## Source basis and limits

*Designing for AI* (Arash Sadr) is an early release. Only Chapters 1-3 were available in the supplied extraction. The admitted principles are problem-first AI selection, system-centred design, human/AI/system layers, model-versus-system distinction, input/output awareness, data and inference transparency, and user understanding. The unavailable chapters on trust, rollout, post-launch drift, governance, culture, and legal detail are not treated as read. Current legal, regulatory, platform, model, or safety claims require Digital Research verification.

## Required product evidence

| Gate | Evidence to inspect |
|---|---|
| Problem fit | Non-AI alternative, user problem, expected value, and reason AI is necessary. |
| System map | Model, surrounding system, inputs, inferred inputs, outputs, automation, human owner, and external dependencies. |
| Disclosure | Plain-language notice of AI involvement and a specific description of what was generated, inferred, recommended, or automated. |
| Control | User review, edit, reject, undo, escalation, and permission boundaries appropriate to the risk. |
| Correction | A visible way to correct inaccurate output and a route for human resolution; record whether the correction changes only the current result or future system behaviour. |
| Drift | Monitoring signal, review cadence, threshold, owner, fallback, and rollback for changing data, audience behaviour, model behaviour, or policy. |
| Accessibility and inclusion | Equivalent non-AI path, readable explanation, keyboard/screen-reader access, language and cultural review, and safe failure state. |

Do not claim that an AI feature is trustworthy because it is disclosed. Trust requires inspectable evidence, meaningful control, correction, and safe recovery.
