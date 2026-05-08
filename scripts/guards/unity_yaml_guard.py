#!/usr/bin/env python3
"""Unity YAML guard stub.

Extend this script to block direct edits to Unity scene, prefab, asset, meta,
ProjectSettings, and Packages files unless the task explicitly allows them.

This script is a stub. It does not protect the repository unless explicitly wired
into a local workflow, pre-commit hook, Codex wrapper, or CI check.
"""

from pathlib import Path
import sys

BLOCKED_SUFFIXES = {".unity", ".prefab", ".asset", ".meta"}
BLOCKED_PREFIXES = {"ProjectSettings/", "Packages/"}


def is_blocked(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if Path(normalized).suffix in BLOCKED_SUFFIXES:
        return True
    return any(normalized.startswith(prefix) for prefix in BLOCKED_PREFIXES)


def main() -> int:
    paths = sys.argv[1:]
    blocked = [path for path in paths if is_blocked(path)]

    if blocked:
        print("Blocked Unity direct-edit targets:")
        for path in blocked:
            print(f"- {path}")
        return 1

    print("No blocked Unity YAML targets found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
