#!/usr/bin/env python3
"""Copy a catalogued LaTeX template and fill its metadata commands.

The script stays local: it reads templates/catalog.json, copies one template
directory, and rewrites ``\\newcommand{\\Key}{...}`` definitions. It does not
fetch packages or expand arbitrary TeX.

Examples:
  python scripts/new_document.py --list
  python scripts/new_document.py --list --json
  python scripts/new_document.py --template lab-report --name rc-step --dry-run
  python scripts/new_document.py --template lab-report --name rc-step \\
      --set studentname=张同学 --json
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "templates" / "catalog.json"
GENERATOR = "engineering-latex-templates/new_document.py"
MARKER = ".scaffold.json"
KEY_RE = re.compile(r"[A-Za-z]+")
NAME_INVALID = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WINDOWS_DEVICE = re.compile(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$", re.IGNORECASE)
BUILD_SUFFIXES = {
    ".aux",
    ".bbl",
    ".blg",
    ".bcf",
    ".log",
    ".out",
    ".toc",
    ".lof",
    ".lot",
    ".lol",
    ".fls",
    ".fdb_latexmk",
    ".xdv",
    ".pdf",
    ".nav",
    ".snm",
    ".vrb",
    ".idx",
    ".ilg",
    ".ind",
}
TEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


class UsageError(Exception):
    """Invalid arguments that should exit with status 2."""


class ScaffoldError(Exception):
    """A catalog, template, or destination problem."""


def escape_tex(value: str) -> str:
    return "".join(TEX_ESCAPES.get(char, char) for char in value)


def load_catalog(path: Path = CATALOG_PATH) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ScaffoldError(f"cannot read catalog: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("templates"), list):
        raise ScaffoldError("catalog must be an object with a templates array")
    seen: set[str] = set()
    for item in data["templates"]:
        if not isinstance(item, dict):
            raise ScaffoldError("each catalog template must be an object")
        for field in ("id", "title", "directory", "entrypoint", "document_class", "summary", "metadata"):
            if field not in item:
                raise ScaffoldError(f"template entry is missing {field}")
        identifier = item["id"]
        if not isinstance(identifier, str) or identifier in seen:
            raise ScaffoldError(f"duplicate or invalid template id: {identifier!r}")
        seen.add(identifier)
        if not isinstance(item["metadata"], list) or not all(
            isinstance(key, str) and KEY_RE.fullmatch(key) for key in item["metadata"]
        ):
            raise ScaffoldError(f"{identifier} metadata keys must be TeX command names")
        directory = Path(item["directory"])
        if directory.is_absolute() or ".." in directory.parts:
            raise ScaffoldError(f"{identifier} directory must stay inside the repository")
    return data


def find_template(catalog: dict, identifier: str) -> dict:
    for item in catalog["templates"]:
        if item["id"] == identifier:
            return item
    known = ", ".join(item["id"] for item in catalog["templates"])
    raise ScaffoldError(f"unknown template {identifier!r}. Known ids: {known}")


def valid_name(name: str) -> bool:
    if not name or name.startswith(".") or name in {".", ".."}:
        return False
    if name.endswith((" ", ".")) or NAME_INVALID.search(name) or WINDOWS_DEVICE.fullmatch(name):
        return False
    return len(name) <= 80


def parse_assignments(items: list[str]) -> dict[str, str]:
    assignments: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise UsageError("--set expects KEY=VALUE")
        key, value = item.split("=", 1)
        if not KEY_RE.fullmatch(key):
            raise UsageError(f"invalid metadata key: {key}")
        if "\n" in value or "\r" in value:
            raise UsageError(f"metadata value for {key} must be a single line")
        if len(value) > 240:
            raise UsageError(f"metadata value for {key} is too long")
        if key in assignments:
            raise UsageError(f"duplicate --set key: {key}")
        assignments[key] = value
    return assignments


def is_build_artifact(path: Path) -> bool:
    name = path.name
    if name in {".DS_Store", "Thumbs.db", MARKER}:
        return True
    if name.endswith(".synctex.gz") or name.endswith(".run.xml"):
        return True
    return path.suffix.lower() in BUILD_SUFFIXES


def command_defined(source: Path, name: str) -> bool:
    prefixes = (f"\\newcommand{{\\{name}}}", f"\\renewcommand{{\\{name}}}")
    for path in source.rglob("*.tex"):
        if is_build_artifact(path) or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if any(prefix in text for prefix in prefixes):
            return True
    return False


def replace_command(text: str, name: str, value: str) -> tuple[str, int]:
    escaped = escape_tex(value)
    prefixes = (f"\\newcommand{{\\{name}}}", f"\\renewcommand{{\\{name}}}")
    pieces: list[str] = []
    index = 0
    count = 0
    while index < len(text):
        matched = next((prefix for prefix in prefixes if text.startswith(prefix, index)), None)
        if matched is None:
            pieces.append(text[index])
            index += 1
            continue
        value_start = index + len(matched)
        if value_start >= len(text) or text[value_start] != "{":
            pieces.append(text[index])
            index += 1
            continue
        depth = 1
        cursor = value_start + 1
        while cursor < len(text) and depth:
            if text[cursor] == "{":
                depth += 1
            elif text[cursor] == "}":
                depth -= 1
            cursor += 1
        if depth != 0:
            raise ScaffoldError(f"unbalanced braces in definition of \\{name}")
        pieces.append(matched + "{" + escaped + "}")
        count += 1
        index = cursor
    return "".join(pieces), count


def apply_assignments(destination: Path, assignments: dict[str, str]) -> dict[str, int]:
    counts = {key: 0 for key in assignments}
    tex_files = [path for path in destination.rglob("*.tex") if path.is_file() and not is_build_artifact(path)]
    for path in tex_files:
        original = path.read_text(encoding="utf-8")
        updated = original
        for key, value in assignments.items():
            updated, replaced = replace_command(updated, key, value)
            counts[key] += replaced
        if updated != original:
            path.write_text(updated, encoding="utf-8")
    missing = [key for key, count in counts.items() if count == 0]
    if missing:
        raise ScaffoldError("metadata commands not found: " + ", ".join(missing))
    return counts


def copy_template(source: Path, destination: Path) -> int:
    copied = 0
    for path in source.rglob("*"):
        if not path.is_file() or is_build_artifact(path):
            continue
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied += 1
    if copied == 0:
        raise ScaffoldError(f"template directory is empty: {source}")
    return copied


def is_previous_scaffold(destination: Path) -> bool:
    marker = destination / MARKER
    if not destination.is_dir() or not marker.is_file() or not (destination / "main.tex").is_file():
        return False
    try:
        data = json.loads(marker.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return data.get("generator") == GENERATOR


def assert_safe_destination(destination: Path, source: Path) -> None:
    templates_root = (ROOT / "templates").resolve()
    resolved = destination.resolve()
    if resolved == ROOT.resolve() or resolved == templates_root or templates_root in resolved.parents:
        raise ScaffoldError("refusing to write inside the template catalog")
    if resolved == source.resolve() or source.resolve() in resolved.parents:
        raise ScaffoldError("refusing to overwrite the template source")
    if ROOT.resolve() in resolved.parents and (ROOT / ".git").exists():
        # A destination inside this clone is allowed for local experiments,
        # except the protected template tree checked above.
        return


def build_command(catalog: dict, entrypoint: str) -> list[str]:
    command = list(catalog.get("build") or [])
    if not command or not all(isinstance(part, str) for part in command):
        raise ScaffoldError("catalog build command is missing")
    return command + [entrypoint]


def public_template(item: dict) -> dict:
    return {
        "id": item["id"],
        "title": item["title"],
        "title_zh": item.get("title_zh", ""),
        "directory": item["directory"],
        "entrypoint": item["entrypoint"],
        "document_class": item["document_class"],
        "summary": item["summary"],
        "features": item.get("features", []),
        "metadata": item["metadata"],
    }


def emit(payload: dict, json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    action = payload.get("action")
    if action == "list":
        for item in payload["templates"]:
            print(f"{item['id']}\t{item['title']}\t{item['document_class']}\t{item['directory']}")
        return
    print(f"{payload['action']}: {payload['template']} -> {payload['destination']}")
    print(f"entrypoint: {payload['entrypoint']}")
    print("build: " + " ".join(payload["build"]))
    if payload.get("substituted"):
        print("substituted: " + ", ".join(payload["substituted"]))


def list_templates(catalog: dict, identifier: str | None, json_mode: bool) -> int:
    items = catalog["templates"]
    if identifier:
        items = [find_template(catalog, identifier)]
    emit({"ok": True, "action": "list", "templates": [public_template(item) for item in items]}, json_mode)
    return 0


def scaffold(args: argparse.Namespace, catalog: dict) -> int:
    if not args.template or not args.name:
        raise UsageError("--template and --name are required unless --list is set")
    if not valid_name(args.name):
        raise UsageError(f"invalid destination name: {args.name}")
    assignments = parse_assignments(args.set)
    template = find_template(catalog, args.template)
    unknown = sorted(set(assignments) - set(template["metadata"]))
    if unknown:
        allowed = ", ".join(template["metadata"])
        raise ScaffoldError(
            "unknown metadata for "
            f"{template['id']}: {', '.join(unknown)}. Allowed keys: {allowed}"
        )
    source = (ROOT / template["directory"]).resolve()
    if not source.is_dir() or not (source / template["entrypoint"]).is_file():
        raise ScaffoldError(f"template source is missing: {source}")
    for key in assignments:
        if not command_defined(source, key):
            raise ScaffoldError(f"\\{key} is listed in the catalog but not defined in {template['id']}")
    parent = args.out.resolve()
    destination = (parent / args.name).resolve()
    assert_safe_destination(destination, source)
    if destination.exists() and not (args.force and is_previous_scaffold(destination)):
        raise ScaffoldError(
            f"destination exists: {destination}. Use --force only to replace a directory created by this script."
        )
    command = build_command(catalog, template["entrypoint"])
    plan = {
        "ok": True,
        "action": "dry-run" if args.dry_run else "scaffold",
        "template": template["id"],
        "destination": str(destination),
        "entrypoint": template["entrypoint"],
        "engine": catalog.get("engine", "xelatex"),
        "build": command,
        "substituted": assignments,
    }
    if args.dry_run:
        emit(plan, args.json)
        return 0
    parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    copied = copy_template(source, destination)
    if assignments:
        apply_assignments(destination, assignments)
    marker = {
        "generator": GENERATOR,
        "template": template["id"],
        "catalog_version": catalog.get("version"),
        "substituted": sorted(assignments),
    }
    (destination / MARKER).write_text(
        json.dumps(marker, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    plan["files"] = copied
    emit(plan, args.json)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list", action="store_true", help="list catalogued templates")
    parser.add_argument("--template", help="template id from templates/catalog.json")
    parser.add_argument("--name", help="new directory name")
    parser.add_argument("--out", type=Path, default=Path("."), help="parent directory for the new document")
    parser.add_argument("--set", action="append", default=[], metavar="KEY=VALUE", help="replace one metadata command")
    parser.add_argument("--dry-run", action="store_true", help="validate and print the plan without writing")
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing destination only when it was created by this script",
    )
    parser.add_argument("--json", action="store_true", help="print a single JSON object")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    json_mode = args.json
    try:
        if args.list and (args.name or args.set or args.dry_run or args.force):
            raise UsageError("--list cannot be combined with scaffold options")
        catalog = load_catalog()
        if args.list:
            return list_templates(catalog, args.template, json_mode)
        return scaffold(args, catalog)
    except UsageError as exc:
        payload = {"ok": False, "error": str(exc)}
        if json_mode:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"error: {exc}", file=sys.stderr)
        return 2
    except ScaffoldError as exc:
        payload = {"ok": False, "error": str(exc)}
        if json_mode:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
