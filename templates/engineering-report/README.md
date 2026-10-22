# 通用工程课程报告模板

适合课程设计、实验报告和工程项目总结。它不是任何学校的官方模板。示例姓名、学号和测量值都是虚构的。

## 编译环境

- 推荐：Overleaf，编译器选择 **XeLaTeX**
- 本地：TeX Live 2023 或更新版本、XeLaTeX、latexmk、biber

## 使用

```bash
cd templates/engineering-report
make
```

也可以运行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

生成文件为 `main.pdf`。从仓库根目录也可以用脚手架复制一份再改：

```bash
python scripts/new_document.py --template engineering-report --name my-report
```

## 修改入口

- `config/metadata.tex`：标题、课程、姓名、学号、班级、教师和日期
- `config/style.tex`：页边距、行距、页眉页脚、链接和代码样式
- `config/fontfix.tex`：Fandol 字体的 OpenType 脚本设置
- `main.tex`：正文结构和示例内容
- `references.bib`：BibLaTeX 文献库，样式为 GB/T 7714—2015

## 已覆盖的内容

中文和英文、目录、公式、SI 单位、TikZ 流程图、三线表、C 代码、参考文献、附录及 PDF 元数据。

## 发布前检查

- 使用虚构信息开发模板，公开时不要提交真实学号、电话或私人邮箱。
- 校徽、字体、图标和其他素材必须确认允许再分发。
- 根据具体学校要求调整，不要把本模板称为官方模板。
