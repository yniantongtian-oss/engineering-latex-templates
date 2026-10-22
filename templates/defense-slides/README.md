# 工程项目答辩模板

16:9 Beamer 幻灯片，使用 `ctexbeamer` 和 XeLaTeX。它不是任何学校或竞赛的官方答辩格式。

## 编译

```bash
cd templates/defense-slides
make
```

输出 PDF 可直接投屏，也可导入支持 PDF 的演示软件。

```bash
python scripts/new_document.py --template defense-slides --name defense
```

## 修改入口

`config/metadata.tex` 中的 `\TalkTitle`、`\TalkSubtitle`、`\AuthorName` 和 `\InstituteName`。

## 已包含页面

- 标题页和目录
- 项目背景、目标和关键指标
- 系统架构图
- 控制算法和安全策略
- 状态机
- 测试方案和结果表
- 创新点、局限和下一步
- 结束页

## 使用建议

- 每页只保留一个主要结论。
- 用实物照片、原理图局部和真实曲线替换示例内容时，确认图片版权和个人信息。
- 结果页必须标注单位、工况、仪器和数据来源。
- 模板中的电流数据是排版示例。
