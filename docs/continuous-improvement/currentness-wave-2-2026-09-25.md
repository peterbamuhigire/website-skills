# Currentness wave 2 integration and model-currentness review, 2026-09-25

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Model-currentness review (Kaizen gate)

- Source: Digital Research register 2026-09-24, claims MR-01 to MR-03 (accessed 2026-09-25); engine record MODEL-001 in `docs/source-registers/performance-currentness-2026-09-25.json`.
- Anthropic lineup checked against the models overview (https://platform.claude.com/docs/en/models/overview, fetched 2026-09-25): Fable 5.1, Opus 5.5, Sonnet 5, Haiku 4.5. Haiku 4.5 retirement is not sooner than 2026-10-15, so review again on that date.
- Active runner: Sonnet 5, session self-report (medium confidence).
- Decision: RETAIN. The engine stays model-agnostic for Claude; no skill names a model, so no edit is required.
- NOT_ASSESSED: account-level availability of newer models; engine-task quality, cost and latency comparison; Codex model pins (out of scope for Claude sessions).

## Changes from this wave

| Area | Change | Claim |
|---|---|---|
| Lab profile wording | 1.6 Mbps / 300 ms is a conservative throttled Slow-4G/3G stress profile, not a market median; measured ranges cited with dates and limits; thresholds unchanged | PERF-009 |
| Kenya speed | 28 ms latency withdrawn; roughly 45-50 Mbps (secondary, 2025) | PERF-010 |
| Ookla and Opensignal | Uganda, Tanzania, Rwanda remain NOT_ASSESSED | PERF-011 |
| WhatsApp | "90%+ of smartphone users" phrasing barred; the phrase was not found in this repository, so a phrasing rule was added to the page-builder facades reference | MKT-001 |
| Consent and disclosure | Uganda DPPA s.26 and PDPO registration, Kenya DPA and Regulations, ODPC guidance, influencer disclosure added as checks to confirm with counsel | LEG-001 to LEG-003 |
