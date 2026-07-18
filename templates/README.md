# 模板目录 | Templates

## 已发布

### [`engineering-report/`](engineering-report/)

通用工程课程报告模板，支持中文、英文、公式、单位、TikZ 图、三线表、代码和参考文献。

### [`competition-paper/`](competition-paper/)

学科竞赛技术论文模板，覆盖指标分解、总体方案、控制算法、安全策略、测试结果和参考文献。

### [`undergraduate-thesis-generic/`](undergraduate-thesis-generic/)

工程类本科毕业设计通用骨架，包含中英文摘要、章节结构、公式图表、代码、实验、不确定度、附录和致谢。

### [`defense-slides/`](defense-slides/)

16:9 Beamer 答辩模板，包含问题、指标、架构、算法、安全、实验、结果和总结页面。

## 编译

所有模板优先使用 XeLaTeX：

```bash
cd templates/<template-name>
make
```

也可以上传整个模板目录到 Overleaf，并把编译器设置为 XeLaTeX。

GitHub Actions 会以矩阵方式编译全部已发布模板，并分别上传 PDF 构建附件。

## 计划增加

- 开题报告模板
- 实验报告精简模板
- 适配具体学校公开规范的扩展包

每个新模板都应包含独立 README、虚构示例信息、明确许可证、编译命令和自动构建检查。具体学校格式必须注明依据与版本，不能冒充官方模板。
