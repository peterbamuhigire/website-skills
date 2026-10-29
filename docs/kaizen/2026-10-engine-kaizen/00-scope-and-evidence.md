# October 2026 website engine Kaizen — scope and evidence

Assessment date: 2026-10-29. Checkout baseline: `2316d440ac0f63ca6e6e049009d0fa989223e8ac`; working branch: `kaizen/2026-10`. Prompt 10 of the supplied October Kaizen PDF was verified from its PDF text against the supplied prompt file. It asks for a five-page service website, a small catalogue with WhatsApp and mobile-money enquiry, and a deliberately defective page, followed by evidence-led skill-engine review.

## Scope

This cycle covers the website-skills checkout only. The website engine router and its `kaizen-engine-and-product-improvement` skill are controlling instructions. The Digital Research Portfolio Kaizen Standard and currentness gate are applied. The adjacent design-system engine was read only to verify the website engine's vendored detector source; it is not part of this change. No doctrine changes, file deletions, public submissions, production deployments, paid model calls, or host model-configuration changes are included.

The requested evidence set is the seven files numbered `00` through `06` in this directory. Temporary task sites, installed JavaScript dependencies, browser artifacts, and reports remain outside the checkout. Practitioner identities, business details, prices, contacts, and payment destinations in those fixtures are synthetic or explicitly absent.

## Evidence method

Baseline commands were run against the unmodified checkout before implementation. Their results and limitations are recorded in `01-baseline-scorecard.md` and `03-experiment-log.md`. Every numeric result is tied to a named command, fixture, source record, or test output in this evidence set. Official source links and access dates appear in `04-validation-record.md`; combined interpretations are marked **(synthesis)** and inferred conclusions **(inference)**. A missing or inapplicable proof is marked **NOT_ASSESSED**.

The exact task outputs are local synthetic artifacts. Static and browser laboratory checks do not establish field Core Web Vitals, production headers, legal compliance, or a deployment/rollback rehearsal.

## Hard package-size rule

Count method: Python `os.walk(followlinks=False)`, counting each regular file and symlink entry once. The baseline checkout contains **837 entries including `.git` and generated/cache files** and **795 entries** after pruning `.git`, `.cache`, `.venv`, `venv`, `node_modules`, and `__pycache__`; both counts have zero symlinks. The cap remains **5,000 entries** for both the full checkout and package-oriented count. These observed counts are from `website-prep/logs/count-checkout.py`, rerun in the checkout before source changes. This cap is a hard constraint, not a target.

## Model and runtime policy

The active Codex assignment is `gpt-6-luna` with high reasoning, per the machine policy; no paid model comparison was run. Official OpenAI model catalogue and changelog were checked on 2026-10-29: the catalogue lists GPT-6.1 Terra, GPT-6.1 Sol, GPT-6 Luna, and GPT-6 Astra, and the changelog dates Terra to 2026-10-26. The assignment is retained for this cycle; current account entitlement, task-level quality/cost/latency comparison, and access to other catalogue entries are **NOT_ASSESSED**. Sources: [OpenAI model catalogue](https://developers.openai.com/api/docs/models), [OpenAI API changelog](https://developers.openai.com/api/docs/changelog), and [Codex availability](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Website skills remain runtime-agnostic. A separate currentness check of official Anthropic pages found releases after the website engine's 2026-09 model record: Anthropic's official model pages list Claude Sonnet 5.5, Opus 5.5, and Haiku 5.5 during September–October 2026. This changes the evidence needed for the engine's existing model-currentness record, not the Codex assignment. Account/runtime availability and comparative task fitness were not tested. Sources: [Anthropic model system cards](https://www.anthropic.com/system-cards), [Anthropic model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations).
