#!/usr/bin/env python3
"""Run chktex on every template source and exit non-zero when it reports issues."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RC = ROOT / ".chktexrc"
TEMPLATES = ROOT / "templates"


def tex_sources() -> list[Path]:
    return sorted(path for path in TEMPLATES.rglob("*.tex") if path.is_file())


def lint_file(chktex: str, path: Path) -> dict:
    command = ["-q", "-H1", "-l", str(RC), str(path)]
    env = os.environ.copy()
    env["LC_ALL"] = "C.UTF-8"
    completed = subprocess.run(
        [chktex, *command],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=env,
    )
    output = (completed.stdout or "") + (completed.stderr or "")
    return {
        "path": str(path.relative_to(ROOT)),
        "exit_code": completed.returncode,
        "output": output,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print a JSON summary")
    args = parser.parse_args()
    chktex = shutil.which("chktex")
    if chktex is None:
        message = "chktex is not installed"
        if args.json:
            print(json.dumps({"ok": False, "error": message}, ensure_ascii=False, indent=2))
        else:
            print(message, file=sys.stderr)
        return 1
    if not RC.is_file():
        message = f"missing chktex config: {RC}"
        if args.json:
            print(json.dumps({"ok": False, "error": message}, ensure_ascii=False, indent=2))
        else:
            print(message, file=sys.stderr)
        return 1
    sources = tex_sources()
    results = [lint_file(chktex, path) for path in sources]
    failed = [item for item in results if item["exit_code"] != 0 or item["output"].strip()]
    if args.json:
        print(
            json.dumps(
                {
                    "ok": not failed,
                    "files": len(sources),
                    "failed": len(failed),
                    "results": failed,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for item in failed:
            sys.stdout.write(item["output"])
            if item["output"] and not item["output"].endswith("\n"):
                sys.stdout.write("\n")
        print(f"chktex: {len(sources)} files, {len(failed)} with findings")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
