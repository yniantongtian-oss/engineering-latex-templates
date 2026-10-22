# 模板目录 | Templates

目录清单以 [`catalog.json`](catalog.json) 为准。每个模板自包含，可以单独上传到 Overleaf，编译器选择 XeLaTeX。

## 已发布

| 目录 | 文档类 | 脚手架 id | 内容 |
| --- | --- | --- | --- |
| [`engineering-report/`](engineering-report/) | `ctexart` | `engineering-report` | 课程报告：封面、摘要、公式、单位、TikZ、三线表、代码、GB/T 7714 |
| [`lab-report/`](lab-report/) | `ctexart` | `lab-report` | 实验报告：电路、数据表、不确定度和 pgfplots 曲线 |
| [`competition-paper/`](competition-paper/) | `ctexart` | `competition-paper` | 学科竞赛论文：指标、架构、算法、保护和测试 |
| [`thesis-proposal/`](thesis-proposal/) | `ctexart` | `thesis-proposal` | 开题报告骨架：文献、目标、路线和进度 |
| [`undergraduate-thesis-generic/`](undergraduate-thesis-generic/) | `ctexbook` | `undergraduate-thesis-generic` | 本科论文通用骨架 |
| [`defense-slides/`](defense-slides/) | `ctexbeamer` | `defense-slides` | 16:9 答辩幻灯片 |

开题报告、论文、竞赛论文和答辩幻灯片都不是官方格式。示例姓名和测量值是虚构的。

## 编译

```bash
cd templates/<template-id>
make
```

从仓库根目录复制一份新文档：

```bash
python scripts/new_document.py --list
python scripts/new_document.py --template lab-report --name my-lab
```

## 新增模板

新模板需要独立 README、虚构示例、Makefile、`main.tex`，并写入 `catalog.json`。具体学校格式必须注明依据与版本，不能写成官方模板。
