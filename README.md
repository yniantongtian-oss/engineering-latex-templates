# Engineering LaTeX Templates

**Reusable report, competition paper, thesis, and presentation templates for engineering students.**

[![Build template matrix](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml/badge.svg)](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

The templates compile in Overleaf or a local TeX Live installation. They support technical writing that requires Chinese typesetting, while the repository's maintainer-facing overview is in English. Published examples use fictional personal data and demonstrative measurements. GitHub Actions compiles the complete template matrix.

## Available templates

- [Engineering course report](templates/engineering-report/) — title page, abstract, contents, formulas, SI units, TikZ illustrations, three-line tables, source code and citations.
- [Competition technical paper](templates/competition-paper/) — requirements, design concept, control algorithms, safety strategy, test methods, findings and references.
- [Generic undergraduate thesis](templates/undergraduate-thesis-generic/) — bilingual abstracts, background, modeling, hardware, firmware, communication, experiments, uncertainty, conclusions and appendices. This is not an official university template.
- [Engineering defense slides](templates/defense-slides/) — a 16:9 Beamer deck with objectives, architecture, control and safety, tests, contributions and next steps.

## Quick start

```bash
git clone https://github.com/yniantongtian-oss/engineering-latex-templates.git
cd engineering-latex-templates/templates/competition-paper
make
```

A direct build command for each template is:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

In Overleaf, upload the complete template directory, select XeLaTeX, and compile `main.tex`.

## Validation

The [template matrix workflow](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml) builds the published examples and uploads the resulting PDF artifacts. New templates should not be merged unless the cloud build passes.

## Quality requirements

1. Build successfully in a standard TeX Live environment.
2. Use fictional names, student numbers, institutions, and test datasets.
3. Document dependencies, build steps, intended use and limitations.
4. Do not impersonate official university or competition formats.
5. Check redistribution rights for fonts, crests, graphics, and third-party assets.
6. Run automated compilation checks on pull requests.
7. Label illustrative data clearly; never present examples as real experimental outcomes.

Additional guidance is available in [templates](templates/) and [docs](docs/). Licensed under [MIT](LICENSE).
