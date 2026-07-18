# engineering-latex-templates

**中国本科生工程类 LaTeX 模板建设项目**  
**LaTeX template project for Chinese undergraduate engineering students**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Documentation%20Phase-orange)

## 项目定位 | Project Scope

本仓库计划提供适用于毕业设计、课程报告、实验报告、学科竞赛论文、开题报告和答辩材料的 LaTeX 模板，并配套中文排版、参考文献、图片表格和 Overleaf 使用说明。

> **当前状态：文档建设阶段。** 仓库已经整理使用指南和模板分类，但 `templates/` 目录目前仍以说明文件为主，尚未发布可直接编译的正式模板版本。

## 计划模板 | Planned Templates

- 本科毕业设计（论文）模板
- 课程报告与实验报告模板
- 学科竞赛论文模板
- 开题报告模板
- Beamer 答辩演示模板

## 当前文档 | Available Documentation

- [`docs/TEMPLATE_CATEGORIES.md`](docs/TEMPLATE_CATEGORIES.md)：模板分类与规划
- [`docs/USAGE_GUIDE.md`](docs/USAGE_GUIDE.md)：基础使用方法
- [`docs/OVERLEAF_GUIDE.md`](docs/OVERLEAF_GUIDE.md)：Overleaf 使用说明
- [`docs/COMMON_ISSUES.md`](docs/COMMON_ISSUES.md)：常见编译与排版问题
- [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)：贡献指南
- [`docs/ACKNOWLEDGEMENTS.md`](docs/ACKNOWLEDGEMENTS.md)：致谢与来源说明

## 目标质量标准 | Quality Goals

正式模板发布前应满足：

- 使用 XeLaTeX 或 LuaLaTeX 可稳定编译
- 提供最小可运行示例和示例 PDF
- 中文字体、页边距、标题、目录、图表和公式配置清晰
- 参考文献流程可复现
- 不把某一学校格式冒充为通用国家标准
- 模板中的姓名、学号、学校等信息全部使用示例占位符
- 通过自动化编译检查，避免提交无法构建的模板

## 仓库结构 | Repository Structure

```text
engineering-latex-templates/
├── templates/          # 正式模板目录；当前持续建设
├── docs/               # 使用、排错和贡献文档
├── LICENSE
└── README.md
```

## 当前使用方式 | Current Usage

现阶段建议先阅读文档、参与模板设计或提交格式需求。待首个可编译模板发布后，再按照以下流程使用：

1. 下载对应模板目录。
2. 使用 TeX Live、MiKTeX 或 Overleaf，并优先选择 XeLaTeX。
3. 根据学校、课程或竞赛的官方格式要求调整参数。
4. 替换示例内容并重新编译检查。

## 贡献 | Contributing

欢迎贡献可编译模板、最小示例、排错说明和格式适配。提交模板时请同时提供：

- 编译引擎与依赖版本
- 主入口 `.tex` 文件
- 示例图片、参考文献和输出 PDF
- 适用场景及已知限制
- 所依据的公开格式要求或来源

详细要求见 [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)。

## 许可证 | License

本项目采用 [MIT License](LICENSE)。第三方字体、学校标识、外部模板和引用材料可能适用不同许可证，贡献者需确认其再分发权限。
