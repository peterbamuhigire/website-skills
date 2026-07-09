# Target Architecture

```text
website-skills/
├── skills/
│   ├── manifest.yml                 # NEW: source of truth for routing/contracts
│   ├── <category>/<skill>/
│   │   ├── SKILL.md
│   │   ├── references/              # source-linked domain rules
│   │   ├── examples/                # NEW: completed, reviewed outputs
│   │   └── contracts/               # NEW: input/output schemas where needed
├── fixtures/                        # NEW: runnable benchmark projects
│   ├── website-basic/
│   ├── website-multilingual/
│   └── website-commerce/
├── tests/
│   ├── registry/
│   ├── gates/
│   └── visual/baseline/
├── templates/
│   ├── ci/website.yml
│   └── project-artifacts/           # NEW: versioned handoff templates
├── scripts/
│   ├── validate-skill-registry.py   # NEW
│   └── ...existing gates
├── docs/
│   ├── standards-register.md        # NEW
│   ├── relocation-map.md            # NEW
│   ├── benchmark-programme.md       # NEW
│   └── engine-upgrade-july-2026/    # this audit
└── project-log/decisions/
```

Existing category structure remains. The key architectural change is a machine-readable contract layer, so documentation describes the same reality that the installer, CI, skills, and benchmark projects execute.

## Master ranking appendix

| Rank | Engine | Capped score | Verdict |
|---:|---|---:|---|
| 1/1 | website-skills | 65/100 | Keep the taxonomy; add a verified registry and fixture layer. |
