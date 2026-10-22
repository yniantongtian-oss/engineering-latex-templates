# 贡献指南 | Contributing Guide

## 可以贡献的内容

- 新的可编译模板
- 现有模板的警告修复和版式改进
- 使用说明和常见问题

## 提交前

1. 在 `templates/catalog.json` 登记新模板，并提供 `main.tex`、Makefile、README 和虚构示例。
2. 运行 `python scripts/lint_tex.py`，chktex 不应有新的发现。
3. 运行 `python -m unittest discover -s scripts -p 'test_*.py'`。
4. 在 TeX Live 2023 或更新版本中运行 `make check`。日志需要通过 `scripts/check_latex_log.py`。
5. 不要把真实学号、联系方式或未授权的校徽放进示例。
6. 不要把通用骨架写成某所学校或某项赛事的官方模板。

Fork 后提交 Pull Request。模板矩阵和 lint 工作流都需要通过。
