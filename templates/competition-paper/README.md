# 学科竞赛论文模板

## 编译

```bash
cd templates/competition-paper
make
```

需要 TeX Live 2023 或更新版本中的 XeLaTeX、latexmk 和 biber。也可以把整个目录上传到 Overleaf，并将编译器设为 XeLaTeX。

```bash
python scripts/new_document.py --template competition-paper --name contest-paper
```

## 修改入口

- `config/metadata.tex`：`\ProjectTitle`、`\TeamName`、`\University`、`\Competition`
- `config/style.tex`：页边距、页眉和文献样式
- `main.tex`：摘要、指标、系统方案、算法、测试结果
- `references.bib`：GB/T 7714—2015 文献库

## 使用原则

- 表中的结果是排版示例，不是真实实验数据。
- 参赛前必须核对官方论文格式、页数、匿名要求和文件命名。
- 图表应从原始数据生成，并保留可复现脚本或 CSV。
- 不要把学校标识或第三方图片直接加入公开仓库，除非确认再分发权限。
- 模板不是任何赛事或学校的官方模板。
