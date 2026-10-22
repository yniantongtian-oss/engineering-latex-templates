# 常见 LaTeX 问题解决 | Common LaTeX Issues

## 中文显示

模板使用 XeLaTeX 和 `ctex`，并固定 `fontset=fandol`，这样在 TeX Live 和 CI 里不依赖商业字体。`config/fontfix.tex` 避免 Fandol 缺少 OpenType CJK script 标记时的 fontspec 警告。不要改用 pdfLaTeX。

## 参考文献

文献库是 `references.bib`，版式为 `biblatex` 的 `gb7714-2015`，后端是 biber。`make` 会让 latexmk 在需要时运行 biber。只执行一次 `xelatex` 时，引用会保持未定义。

## 图片

使用模板目录中的相对路径。优先使用 PDF、PNG 或 JPG。TikZ、circuitikz 和 pgfplots 图不需要外部图片文件。

## 日志里的警告

`scripts/check_latex_log.py` 会拒绝仍含 Warning、Overfull 或 Underfull 的日志。本地可运行 `make check`。chktex 使用仓库根目录的 `.chktexrc`，并依赖发行版自带的 `/etc/chktexrc`。

更多问题请在 Issues 中反馈。
