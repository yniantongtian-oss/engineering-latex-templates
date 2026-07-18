# engineering-latex-templates

**中国本科生工程类 LaTeX 模板库 | LaTeX Templates for Engineering Students**

[![Build LaTeX templates](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/latex.yml/badge.svg)](https://github.com/yniantongtian-oss/engineering-latex-templates/actions/workflows/latex.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

仓库现在包含一个真实可编译、可在 Overleaf 和本地 TeX Live 使用的通用工程报告模板。

## 已发布模板

### [通用工程课程报告](templates/engineering-report/)

包含：

- 中文与英文混排
- 封面元数据集中配置
- 摘要、目录、章节和附录
- 公式、SI 单位、TikZ 流程图和三线表
- C 代码清单
- 参考文献
- `Makefile` 和 GitHub Actions 自动编译

## 快速开始

```bash
git clone https://github.com/yniantongtian-oss/engineering-latex-templates.git
cd engineering-latex-templates/templates/engineering-report
make
```

Overleaf 用户可上传 `engineering-report` 整个目录，将编译器设为 XeLaTeX，然后编译 `main.tex`。

## 质量标准

正式模板必须：

1. 在标准 TeX Live 环境成功编译；
2. 使用虚构姓名、学号、学校和示例数据；
3. 提供依赖、构建方法、适用范围和已知限制；
4. 不冒充学校官方模板；
5. 确认字体、校徽、图标和第三方素材允许再分发；
6. 通过 Pull Request 自动编译检查。

更多模板和使用文档见 [`templates/`](templates/) 与 [`docs/`](docs/)。本项目采用 [MIT License](LICENSE)。
