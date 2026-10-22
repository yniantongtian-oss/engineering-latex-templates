# Engineering LaTeX Templates

**Reusable report, competition paper, thesis, and presentation templates for engineering students.**

[![Build template matrix](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml/badge.svg)](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml)
[![Lint](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/lint.yml/badge.svg)](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

The templates compile in Overleaf or a local TeX Live 2023 (or newer) installation with XeLaTeX, latexmk, and biber. They support technical writing that requires Chinese typesetting. Published examples use fictional personal data and demonstrative measurements. The machine-readable list of templates is [`templates/catalog.json`](templates/catalog.json).

## Template gallery

| Template | Class | Scaffold id | Example shows |
| --- | --- | --- | --- |
| [Engineering course report](templates/engineering-report/) | `ctexart` | `engineering-report` | Title page, bilingual abstract, formula, SI quantities, TikZ loop, table, C listing, GB/T 7714 references |
| [Laboratory experiment report](templates/lab-report/) | `ctexart` | `lab-report` | RC step response with a circuitikz schematic, uncertainty note, data table, and pgfplots curve |
| [Competition technical paper](templates/competition-paper/) | `ctexart` | `competition-paper` | Requirements, architecture, discrete control, safety rules, firmware sketch, and test table |
| [Undergraduate thesis proposal](templates/thesis-proposal/) | `ctexart` | `thesis-proposal` | Opening report with literature, objectives, technical route, and a schedule |
| [Generic undergraduate thesis](templates/undergraduate-thesis-generic/) | `ctexbook` | `undergraduate-thesis-generic` | Bilingual abstracts, modeling, hardware, firmware, experiments, appendices, and references |
| [Engineering defense slides](templates/defense-slides/) | `ctexbeamer` | `defense-slides` | 16:9 deck for objectives, architecture, control, safety, tests, and next steps |

The proposal, thesis, competition paper, and slides are generic skeletons. Match the current official instructions before submission, and keep illustrative numbers labeled as examples.

## Quick start

```bash
git clone https://github.com/yniantongtian-oss/engineering-latex-templates.git
cd engineering-latex-templates/templates/lab-report
make
```

`make` runs:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

In Overleaf, upload the complete template directory, select XeLaTeX, and compile `main.tex`.

## Start a new document

`scripts/new_document.py` copies one catalogued template and rewrites its `\newcommand` metadata. It does not download packages or run the TeX compiler.

```bash
python scripts/new_document.py --list
python scripts/new_document.py --template lab-report --name rc-step --dry-run
python scripts/new_document.py --template lab-report --name rc-step \
  --set studentname=张同学 --set studentid=20260000000 --json
```

`--json` prints one object and no other text. `--dry-run` validates the plan without writing. An existing destination is left untouched unless it contains this script's `.scaffold.json` marker and `--force` is set. Metadata values are escaped for TeX, and only keys declared for that template are accepted.

## Validation

The [template matrix workflow](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml) reads `templates/catalog.json`, builds every example, rejects logs that still contain warnings or bad boxes, and uploads the PDFs. The [lint workflow](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/lint.yml) runs chktex and the scaffold tests.

From a local TeX Live install:

```bash
make check
```

`make check` lints every `.tex` file, runs the scaffold tests, builds every template, and scans the logs.

## Quality requirements

1. Build successfully with XeLaTeX on TeX Live 2023 or newer, with a warning-free log.
2. Register every template in `templates/catalog.json`, and give it a README, Makefile, and fictional sample.
3. Use fictional names, student numbers, institutions, and test datasets.
4. Document dependencies, build steps, intended use, and limitations.
5. Do not present a generic skeleton as an official university or competition format.
6. Check redistribution rights for fonts, crests, graphics, and third-party assets.
7. Keep chktex clean with the repository `.chktexrc`.
8. Label illustrative data clearly.

Additional guidance is in [templates](templates/) and [docs](docs/). Licensed under [MIT](LICENSE).
