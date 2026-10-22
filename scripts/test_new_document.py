"""Tests for the template catalog and document scaffold."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import new_document

ROOT = new_document.ROOT
SCRIPT = Path(new_document.__file__)


class CatalogTest(unittest.TestCase):
    def test_catalog_matches_template_directories(self) -> None:
        catalog = new_document.load_catalog()
        declared = {item["directory"] for item in catalog["templates"]}
        found = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "templates").iterdir()
            if path.is_dir() and (path / "main.tex").is_file()
        }
        self.assertEqual(declared, found)

    def test_metadata_commands_exist(self) -> None:
        catalog = new_document.load_catalog()
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for item in catalog["templates"]:
            self.assertIn(item["id"], readme)
            self.assertIn(item["directory"], readme)
            source = ROOT / item["directory"]
            self.assertTrue((source / item["entrypoint"]).is_file())
            self.assertTrue((source / "Makefile").is_file())
            self.assertTrue((source / "README.md").is_file())
            makefile = (source / "Makefile").read_text(encoding="utf-8")
            self.assertIn("-xelatex", makefile)
            self.assertIn("halt-on-error", makefile)
            for key in item["metadata"]:
                self.assertTrue(
                    new_document.command_defined(source, key),
                    f"{item['id']} is missing \\{key}",
                )

    def test_escape_tex(self) -> None:
        self.assertEqual(new_document.escape_tex(r"A & B_100%"), r"A \& B\_100\%")
        self.assertEqual(new_document.escape_tex("ok"), "ok")


class ScaffoldCliTest(unittest.TestCase):
    def run_cli(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_list_json(self) -> None:
        completed = self.run_cli(["--list", "--json"])
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["ok"])
        ids = [item["id"] for item in payload["templates"]]
        self.assertIn("lab-report", ids)
        self.assertIn("defense-slides", ids)

    def test_dry_run_does_not_write(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "rc-step"
            completed = self.run_cli(
                [
                    "--template",
                    "lab-report",
                    "--name",
                    "rc-step",
                    "--out",
                    tmp,
                    "--set",
                    "studentname=Ada & Bob",
                    "--dry-run",
                    "--json",
                ]
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            payload = json.loads(completed.stdout)
            self.assertEqual(payload["action"], "dry-run")
            self.assertEqual(payload["substituted"]["studentname"], "Ada & Bob")
            self.assertFalse(destination.exists())

    def test_scaffold_substitutes_and_refuses_unmarked_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            completed = self.run_cli(
                [
                    "--template",
                    "engineering-report",
                    "--name",
                    "course-report",
                    "--out",
                    tmp,
                    "--set",
                    "studentname=Ada & Bob",
                    "--set",
                    "studentid=20260001",
                    "--json",
                ]
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            destination = Path(tmp) / "course-report"
            metadata = (destination / "config" / "metadata.tex").read_text(encoding="utf-8")
            self.assertIn(r"\newcommand{\studentname}{Ada \& Bob}", metadata)
            self.assertIn(r"\newcommand{\studentid}{20260001}", metadata)
            self.assertTrue((destination / ".scaffold.json").is_file())
            self.assertTrue((destination / "main.tex").is_file())
            blocked = self.run_cli(
                ["--template", "lab-report", "--name", "course-report", "--out", tmp, "--json"]
            )
            self.assertEqual(blocked.returncode, 1)
            self.assertIn("destination exists", json.loads(blocked.stdout)["error"])
            replaced = self.run_cli(
                [
                    "--template",
                    "lab-report",
                    "--name",
                    "course-report",
                    "--out",
                    tmp,
                    "--force",
                    "--json",
                ]
            )
            self.assertEqual(replaced.returncode, 0, replaced.stderr)
            self.assertTrue((destination / "config" / "metadata.tex").is_file())
            lab_metadata = (destination / "config" / "metadata.tex").read_text(encoding="utf-8")
            self.assertIn(r"\newcommand{\experimentdate}", lab_metadata)

    def test_unknown_key_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            completed = self.run_cli(
                [
                    "--template",
                    "defense-slides",
                    "--name",
                    "talk",
                    "--out",
                    tmp,
                    "--set",
                    "studentname=Ada",
                    "--json",
                ]
            )
            self.assertEqual(completed.returncode, 1)
            self.assertFalse((Path(tmp) / "talk").exists())
            self.assertIn("unknown metadata", json.loads(completed.stdout)["error"])

    def test_force_does_not_delete_unmarked_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "notes"
            destination.mkdir()
            (destination / "keep.txt").write_text("keep", encoding="utf-8")
            completed = self.run_cli(
                ["--template", "lab-report", "--name", "notes", "--out", tmp, "--force", "--json"]
            )
            self.assertEqual(completed.returncode, 1)
            self.assertEqual((destination / "keep.txt").read_text(encoding="utf-8"), "keep")


if __name__ == "__main__":
    unittest.main()
