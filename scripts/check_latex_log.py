#!/usr/bin/env python3
"""Fail when a LaTeX log still contains warnings or bad boxes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERN = re.compile(
    r"(?:^! |Warning|Overfull \\hbox|Underfull \\hbox|"
    r"Overfull \\vbox|Underfull \\vbox|Emergency stop|Fatal error)"
)


def scan(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    hits: list[str] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if PATTERN.search(line):
            hits.append(f"{path}:{number}: {line.strip()}")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logs", nargs="+", type=Path)
    args = parser.parse_args()
    hits: list[str] = []
    missing: list[str] = []
    for path in args.logs:
        if not path.is_file():
            missing.append(str(path))
            continue
        hits.extend(scan(path))
    if missing:
        print("missing logs:\n" + "\n".join(missing), file=sys.stderr)
        return 1
    if hits:
        print("\n".join(hits))
        print(f"{len(hits)} log problem(s)", file=sys.stderr)
        return 1
    print(f"clean logs: {len(args.logs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
