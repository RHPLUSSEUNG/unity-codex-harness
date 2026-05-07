#!/usr/bin/env python3
"""Circuit breaker guard stub.

Extend this script to detect repeated errors, repeated Unity Console failures,
or repeated edits to the same file within a short time window.
"""

from collections import Counter
import sys


def main() -> int:
    events = [line.strip() for line in sys.stdin if line.strip()]
    counts = Counter(events)

    repeated = [(event, count) for event, count in counts.items() if count >= 5]

    if repeated:
        print("Circuit breaker warning: repeated failure pattern detected.")
        for event, count in repeated:
            print(f"- {count}x: {event}")
        return 1

    print("No repeated failure pattern detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
