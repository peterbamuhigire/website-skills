# Claude Code repository memory

@AGENTS.md

## Claude-only notes

- Apply `AGENTS.md` in full, including its runner-agnostic doctrine; skip only its explicitly
  Codex-only sections (e.g. "Codex-only model setup").
- **Optional plugins (engine gates remain authoritative):** these Claude Code plugins can help
  with website development work:

  ```text
  /plugin marketplace add obra/superpowers-marketplace
  /plugin install superpowers@superpowers-marketplace
  /plugin marketplace add anthropics/claude-code
  /plugin install frontend-design@claude-code-plugins
  ```

  Use a plugin only where it materially improves design, implementation, debugging, or QA
  output. A plugin never replaces or overrides an engine gate, stage gate or verification step.
