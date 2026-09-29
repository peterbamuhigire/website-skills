# Claude Code repository memory

@AGENTS.md

## Claude-only notes

- Apply `AGENTS.md` in full, including its runner-agnostic doctrine; skip only its explicitly
  Codex-only sections (e.g. "Codex-only model setup").
- Recommended Claude Code plugins before website development work:

  ```text
  /plugin marketplace add obra/superpowers-marketplace
  /plugin install superpowers@superpowers-marketplace
  /plugin marketplace add anthropics/claude-code
  /plugin install frontend-design@claude-code-plugins
  ```

  Use plugins where they materially improve design, implementation, debugging, or QA output.
