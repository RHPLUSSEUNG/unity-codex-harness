#!/usr/bin/env python3
"""Dangerous command guard stub.

Extend this script to inspect proposed shell commands before allowing an AI agent
to execute them.

This script is a stub. It does not protect the repository unless explicitly wired
into a local workflow, pre-commit hook, Codex wrapper, or CI check.
"""

import sys

BLOCKED_PATTERNS = [
    "rm -rf",
    "git reset --hard",
    "git clean -fd",
    "git push --force",
    "del /s",
    "rmdir /s",
]


def main() -> int:
    command = " ".join(sys.argv[1:])
    lowered = command.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in lowered:
            print(f"Blocked dangerous command pattern: {pattern}")
            return 1

    print("Command allowed by dangerous_cmd_guard.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
