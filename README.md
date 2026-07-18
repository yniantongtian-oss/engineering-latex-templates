# engineering-latex-templates

**中国本科生工程类 LaTeX 模板库 | LaTeX Templates for Engineering Students**

[![Build template matrix](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml/badge.svg)](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/build-template-matrix.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

仓库提供可在 Overleaf 和本地 TeX Live 使用的工程类中文 LaTeX 模板。所有正式模板使用虚构身份和示例数据，并通过 GitHub Actions 自动编译。

## 已发布模板

### [通用工程课程报告](templates/engineering-report/)

适合课程论文、实验报告和工程设计报告，包含封面、摘要、目录、公式、SI 单位、TikZ 图、三线表、代码和参考文献。

### [学科竞赛技术论文](templates/competition-paper/)

覆盖题目指标分解、总体方案、控制算法、安全策略、测试方法、结果分析和参考文献，适合电子设计及其他工程竞赛技术报告。

### [本科毕业设计通用骨架](templates/undergraduate-thesis-generic/)

包含中英文摘要、绪论、总体方案、理论建模、硬件、固件、通信、实验、不确定度、结论、附录和致谢。它是通用写作骨架，不代替学校官方格式。

### [Beamer 答辩演示](templates/defense-slides/)

16:9 工程项目答辩模板，包含问题、目标、指标、系统架构、控制安全、测试结果、创新点和下一步。

## 快速开始

```bash
git clone https://github.com/yniantongtian-oss/engineering-latex-templates.git
cd engineering-latex-templates/templates/competition-paper
make
```

所有模板都支持以下命令：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Overleaf 用户可上传任意模板的完整目录，将编译器设为 XeLaTeX，然后编译 `main.tex`。

## 自动化验证

`Build template matrix` 工作流会同时编译全部已发布模板，并分别上传 PDF 构建附件。新增模板只有在云端构建成功后才应合入 `main`。

## 质量标准

正式模板必须：

1. 在标准 TeX Live 环境成功编译；
2. 使用虚构姓名、学号、学校和示例数据；
3. 提供依赖、构建方法、适用范围和已知限制；
4. 不冒充学校或赛事官方模板；
5. 确认字体、校徽、图标和第三方素材允许再分发；
6. 通过 Pull Request 自动编译检查；
7. 将示例结果明确标为示例，禁止伪装成真实实验结论。

更多使用与排错文档见 [`templates/`](templates/) 与 [`docs/`](docs/)。本项目采用 [MIT License](LICENSE)。
