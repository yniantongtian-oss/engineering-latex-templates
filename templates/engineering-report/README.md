# 通用工程课程报告模板

这是仓库中的第一个可编译模板，适合课程设计、实验报告和工程项目总结。它不是任何学校的官方模板。

## 编译环境

- 推荐：Overleaf，编译器选择 **XeLaTeX**
- 本地：TeX Live 2024 或更新版本、XeLaTeX、latexmk

## 使用

```bash
cd templates/engineering-report
make
```

也可以运行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

生成文件为 `main.pdf`。

## 修改入口

- `config/metadata.tex`：标题、课程、姓名、学号、班级、教师和日期
- `config/style.tex`：页边距、行距、页眉页脚、链接和代码样式
- `main.tex`：正文结构和示例内容
- `references.bib`：可选的 BibTeX 数据库示例

## 已覆盖的内容

中文和英文、目录、公式、SI 单位、TikZ 流程图、三线表、C 代码、参考文献、附录及 PDF 元数据。

## 发布前检查

- 使用虚构信息开发模板，公开时不要提交真实学号、电话或私人邮箱。
- 校徽、字体、图标和其他素材必须确认允许再分发。
- 根据具体学校要求调整，而不是把本模板称为“官方模板”。
- GitHub Actions 会在每次提交和 Pull Request 时自动执行 XeLaTeX 编译。
