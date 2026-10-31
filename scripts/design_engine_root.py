"""Locate the design-engine checkout beside this engine (WSK2-04).

The repository was renamed upstream (`chwezi-design-engine` to `design-system-skills`), so a local
checkout may carry either folder name, and a host may keep its engines under another root. Resolution
order, first match wins:

1. an explicit path given by the caller (returned as given; the caller reports it if it is wrong);
2. the `CHWEZI_DESIGN_ENGINE_ROOT` environment variable, when it holds the marker folder;
3. `<CHWEZI_ENGINES_ROOT>/design-system-skills`, then `<CHWEZI_ENGINES_ROOT>/chwezi-design-engine`;
4. the sibling folders of the engine checkout, canonical name first.

A candidate counts only when it contains the marker folder the caller needs (`skills` for routing
checks, `tools/slop-detector` for the vendored-detector comparison), so an empty folder with a
matching name is never taken for the engine. Nothing is ever downloaded or written.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from pathlib import Path

ENV_ROOT = "CHWEZI_DESIGN_ENGINE_ROOT"
ENV_ENGINES_ROOT = "CHWEZI_ENGINES_ROOT"
NAMES = ("design-system-skills", "chwezi-design-engine")


def candidates(base: Path, env: Mapping[str, str]) -> list[Path]:
    """Candidate checkouts in resolution order (steps 2 to 4)."""
    found: list[Path] = []
    if env.get(ENV_ROOT):
        found.append(Path(env[ENV_ROOT]))
    if env.get(ENV_ENGINES_ROOT):
        found.extend(Path(env[ENV_ENGINES_ROOT]) / name for name in NAMES)
    found.extend(base.parent / name for name in NAMES)
    return found


def find_design_engine(
    base: Path,
    explicit: Path | None = None,
    env: Mapping[str, str] | None = None,
    marker: str = "skills",
) -> Path | None:
    """Return the design-engine checkout, or None when none is found.

    `base` is this engine's checkout; its siblings are searched last. `env` defaults to the process
    environment and is a parameter so tests stay hermetic.
    """
    if explicit is not None:
        return explicit
    environment = os.environ if env is None else env
    for candidate in candidates(base, environment):
        if (candidate / marker).is_dir():
            return candidate
    return None
