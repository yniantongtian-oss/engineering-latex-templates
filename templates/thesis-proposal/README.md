# 毕业设计开题报告模板

这是工程类本科开题的通用骨架，不是任何学校的官方开题表。封面字段、进度和指标都是示例。

## 编译

```bash
cd templates/thesis-proposal
make
```

Overleaf 上传整个目录并选择 XeLaTeX。本地需要 TeX Live 2023 或更新版本、latexmk 和 biber。

```bash
python scripts/new_document.py --template thesis-proposal --name proposal
```

## 修改入口

- `config/metadata.tex`：题目、姓名、学号、学校、学院、专业、导师和日期
- `main.tex`：背景、目标、技术路线和进度
- `references.bib`：GB/T 7714—2015 文献库

学校当年的页数、签字栏和盲审要求优先于本模板。
