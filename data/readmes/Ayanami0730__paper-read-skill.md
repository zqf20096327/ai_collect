# AI Reading Skills

让 AI Agent 深度阅读论文和博客的 prompt 集合。根据内容类型自动路由到对应的分析框架。

## 安装

```bash
npx skills add Ayanami0730/paper-read-skill -g
```

或手动复制 `skills/` 目录下的子文件夹到 `~/.cursor/skills/`。

## 包含的 Skills

### Paper Analysis

根据论文类型自动路由分析框架：

- **Benchmark 论文**：评测数据集与评估框架的深度剖析
- **方法/算法论文**：模型架构、训练策略与技术创新的全面分析
- **综述/观点/博客**：论点结构、覆盖完整性与批判性审视

此外，若论文发表于（或投向）Nature / Science / Cell 系等顶刊，会在上述技术框架之外**额外叠加**一层期刊阅读维度：

- **Nature 期刊阅读 (NEW)**：在技术剖析之上叠加顶刊特有的分析——发表策略（preprint→正式版演变、paper-family / co-timed companion、author-list 机构组合）、Abstract 句 cluster 拆解、Introduction 段落功能 map、Figure 设计与逐图截图分析、方法学诚实度与可复现性、影响力与传播配套、以及顶刊范式批判。

### Blog Reading (NEW)

根据博客类型自动路由分析框架，以中文自然语言段落输出（禁用 markdown 列表）：

- **技术研究型**：深入解读技术原理、评估创新程度与证据强度
- **产品发布型**：穿透营销叙事、提炼真实技术进步与用户价值
- **行业观点型**：解构论证逻辑、识别立场偏见、补充反方声音
- **案例故事型**：区分公关包装与真实经验、提取可迁移模式

## 工具需求

各 agent 自带的 web fetch 工具即可获取论文和博客内容，无需额外配置 Firecrawl 等付费抓取服务。

## 兼容的 Agent

Cursor · Claude Code · Codex · OpenCode

## License

MIT
