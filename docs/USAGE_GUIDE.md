# 模板使用指南 | Template Usage Guide

## 推荐编译环境

- Overleaf：上传整个模板目录，编译器选择 XeLaTeX
- TeX Live 2023 或更新版本，配合 latexmk 与 biber
- 本地编辑器可使用 VS Code 或 TeXstudio

## 从模板生成一份新文档

在仓库根目录：

```bash
python scripts/new_document.py --list
python scripts/new_document.py --template lab-report --name my-lab
cd my-lab
make
```

封面字段集中在各模板的 `config/metadata.tex`。`--set key=value` 只改目录里声明过的命令。

## 基本修改步骤

1. 用脚手架复制模板，或直接进入 `templates/<id>/`
2. 修改 `config/metadata.tex` 中的题目、姓名和单位
3. 替换 `main.tex` 里的章节、图和表
4. 在 `references.bib` 中维护文献
5. 运行 `make` 生成 PDF

## 常见问题

- 中文乱码：确认编译引擎是 XeLaTeX
- 参考文献没有更新：保留 latexmk，让它调用 biber，不要只跑一次 xelatex
- 图片无法显示：使用模板目录内的相对路径

更多说明见各模板 README 和 `docs/COMMON_ISSUES.md`。
