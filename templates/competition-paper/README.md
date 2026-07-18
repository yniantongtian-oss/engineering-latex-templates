# 学科竞赛论文模板

## 编译

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

也可以把整个目录上传到 Overleaf，并将编译器设为 XeLaTeX。

## 修改入口

在 `main.tex` 顶部修改：

- `\ProjectTitle`
- `\TeamName`
- `\University`
- `\Competition`

然后按题目要求替换摘要、指标、系统方案、算法、测试结果和参考文献。

## 使用原则

- 表中的结果是排版示例，不是真实实验数据。
- 参赛前必须核对官方论文格式、页数、匿名要求和文件命名。
- 图表应从原始数据生成，并保留可复现脚本或 CSV。
- 不要把学校标识或第三方图片直接加入公开仓库，除非确认再分发权限。
- 模板不是任何赛事或学校的官方模板。
