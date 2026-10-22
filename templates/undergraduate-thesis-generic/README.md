# 本科毕业设计（论文）通用骨架

这是一个可编译的工程类本科论文结构，不代表任何学校的官方格式。

## 编译

```bash
cd templates/undergraduate-thesis-generic
make
```

Overleaf 中上传整个目录并选择 XeLaTeX。本地需要 TeX Live 2023 或更新版本、latexmk 和 biber。

```bash
python scripts/new_document.py --template undergraduate-thesis-generic --name thesis
```

## 修改入口

`config/metadata.tex` 集中修改中英文题目、姓名、学号、学校、学院、专业、指导教师和日期。正文在 `main.tex`，文献在 `references.bib`。

## 已覆盖结构

- 中英文封面信息
- 中文摘要、英文摘要与关键词
- 自动目录
- 绪论、需求与总体方案
- 理论建模与控制策略
- 硬件、固件和通信
- 实验设计、结果与不确定度
- 结论、附录、参考文献和致谢
- 公式、TikZ 图、三线表、代码清单和 SI 单位

## 正式使用前必须调整

- 以学校最新规范为准修改页边距、字体、字号、页眉、封面和参考文献。
- 某些学校要求盲审版，必须移除姓名、学号、导师和致谢。
- 示例数值和引用占位不能直接提交。
- 校徽、字体和学校模板源文件可能有独立授权，不应默认放入公开仓库。
