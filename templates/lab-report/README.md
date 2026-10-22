# 实验报告模板

适合一次课程实验的短报告。它不是任何学校的官方实验报告格式。姓名、学号、仪器型号和采样点都是虚构的。

## 编译

```bash
cd templates/lab-report
make
```

需要 TeX Live 2023 或更新版本中的 XeLaTeX、latexmk、biber 和 pgfplots。Overleaf 上传整个目录后选择 XeLaTeX。

复制一份新报告：

```bash
python scripts/new_document.py --template lab-report --name rc-step
```

## 修改入口

- `config/metadata.tex`：题目、课程、姓名、学号、教师和实验日期
- `config/style.tex`：页边距、页眉和文献样式
- `main.tex`：原理、数据表和曲线
- `references.bib`：GB/T 7714—2015 文献库

电路图使用 circuitikz，曲线由 pgfplots 从公式和坐标直接生成。两者都包含在 TeX Live 的 pictures 集合中。
