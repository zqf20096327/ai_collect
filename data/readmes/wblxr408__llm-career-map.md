# LLM Career Map · 大模型学习与就业知识地图

把大模型笔记、面试题库、面经和就业资料整理成一张可以按岗位学习的地图。内置可操作的步骤动画，从理解技术原理一路连接到项目证据、简历投递和面试复盘。

[在线体验](https://llm-master-web.vercel.app) · [就业知识地图](https://llm-master-web.vercel.app/#/map) · [English](README.en.md) · [来源清单](docs/sources.md)

![CI](https://github.com/wblxr408/llm-career-map/actions/workflows/ci.yml/badge.svg)
![React 19](https://img.shields.io/badge/React-19-149eca)
![Vite 7](https://img.shields.io/badge/Vite-7-646cff)
![Code license MIT](https://img.shields.io/badge/code_license-MIT-green)

![就业知识地图：七个求职阶段与十八个主题](docs/assets/career-map.jpg)

## 这里有什么

截至 2026-10-12，收录 **24 个仓库、1,987 份资料、18 个 Topic、6 条岗位路线、8 组交互演示**。1,206 份资料可在站内阅读全文，781 份保留原文索引；包含 7 篇本站就业导读。统计单位是文档。

| 能力 | 使用方式 |
|---|---|
| 就业知识地图 | 按岗位选择路线，查看 Topic 前置知识、后续方向、完成标准 |
| 资料检索 | 按主题、岗位、来源和资料类型筛选，搜索笔记与正文摘要 |
| 步骤动画 | 播放、暂停、逐步前进、重置、调整速度和实验参数 |
| 阅读体验 | Markdown/HTML、代码高亮与复制、KaTeX 公式、Mermaid 流程图、阅读目录 |
| 图片注释 | 编号、来源、放大、读图提示与浏览器本地个人图注 |
| 学习记录 | 收藏、学完记录、阅读进度、深色主题与手机布局 |
| 来源追溯 | 保留原仓库、路径、固定提交、Git blob 指纹与许可证 |
| 更新同步 | LLM Master 前台每 60 秒检查；扩展库提供版本刷新与核验脚本 |

## 一条清晰的学习主线

**岗位定位 → 基础能力 → 专业方向 → 项目证据 → 简历投递 → 面试复盘 → Offer 与入职成长**

| 阶段 | Topic |
|---|---|
| 岗位定位 | 目标岗位与准备策略 |
| 基础能力 | 算法与编码、计算机基础、ML 基础、Transformer 与模型原理 |
| 专业方向 | LLM 应用、RAG、Agent、微调与训练、部署与推理、后端、前端、系统设计 |
| 项目证据 | 项目作品与可验证成果 |
| 简历投递 | 简历、作品集与投递 |
| 面试复盘 | 技术面试与面经、行为面试与沟通 |
| 入职成长 | Offer 决策与职业成长 |

岗位路线覆盖 **AI 应用/Agent、算法/ML/LLM、AI Infra、后端、前端、C/C++/系统**。每条路线补齐需要的前置 Topic；可在地图视图与顺序路线间切换。

## 交互实验室

8 个演示分别讲解 RAG 全链路、Attention 的 Q/K/V、切片与重叠、ReAct、MCP、流式生成、KV Cache 和 LoRA。Attention 支持调整参数并查看小矩阵计算，切片实验可调整长度与重叠。

这些是使用固定样例的教学演示，无需模型 API key。技术说明和演示边界见 [实现文档](docs/implementation.md)。

## 本地运行

要求 **Node.js 22.12+、npm、Git**。Windows PowerShell 可以将以下命令中的 npm/npx 替换为 npm.cmd/npx.cmd。

```bash
git clone https://github.com/wblxr408/llm-career-map.git
cd llm-career-map
npm ci
npm run dev
```

构建和检查：

```bash
npm test
npm run build
npm run preview
```

资料快照已经包含在仓库中，常规构建无需重新采集上游。默认开发服务为 http://127.0.0.1:5173，构建目录为 dist/。

## 部署到 Vercel

在 Vercel 导入本仓库，框架选择 **Vite**，安装命令 npm ci，构建命令 npm run build，输出目录 dist。仓库已包含 vercel.json。

也可在登录 Vercel CLI 后执行：

```bash
npx vercel --prod
```

阅读和地图使用 hash 路由，分享地址保留 #/read/… 或 #/map… 部分。站点使用静态文件，无需数据库和服务端函数。当前在线实例是已发布版本；本仓库提供独立部署的完整实现，尚未自动绑定现有 Vercel 项目的 Git 发布。

## 更新资料

**原始 LLM Master**：网页打开且处于前台时，每 60 秒检查 GitHub 提交；首次打开、切回页面和恢复网络时也检查。仅下载新增/修改的笔记，全成功后切换完整版本，删除上游已移除笔记，缓存到 IndexedDB。页面关闭时不会后台检测，GitHub 限流可能延后检查。

**23 个扩展仓库**：采用固定提交快照，维护时运行以下命令，检查变更后重新发布：

```bash
npm run sync:content
npm run sync:library
npm test
npm run build
```

采集缓存保存在 .cache/career/，可通过 CAREER_CACHE_DIR 指定其他位置。来源清单、许可证、分类规则和同步边界见 [实现文档](docs/implementation.md)；已有固定版本可用 npm run collect:library 重新采集。

导出：[地图 JSON](https://llm-master-web.vercel.app/career-map.json) · [资料 CSV](https://llm-master-web.vercel.app/career-resources.csv)。

## 项目结构

```text
src/                  React 界面、阅读器、演示、同步和 Topic 模型
content/              原始 LLM Master 笔记与固定版本信息
curated/              7 篇原创就业导读
public/library/       扩展来源索引、分仓库正文与许可证
scripts/              构建、更新、采集、测试与线上核验
docs/                 实现文档、来源清单、截图与验证记录
.github/workflows/    GitHub Actions 测试与构建
```

## 验证与贡献

20 项测试覆盖同步失败回滚、限流/并发、Topic 依赖闭包、来源唯一性、正文指纹、许可、HTML/公式/链接以及导出。已检查 320/390/1440 像素布局、岗位与来源筛选、跨仓库阅读；已核对线上 1,987 份资料的索引和全文包。[验证记录](docs/verification/) 保存检查时间与实际边界。

线上部署核验：node scripts/verify-deployment.mjs https://your-site.vercel.app，报告写入 docs/verification/deployment.json。GitHub Actions 对推送与 PR 执行 npm ci、npm test 和 npm run build。

欢迎通过 Issue 报告问题、推荐资料，通过 PR 改进分类、动画和体验。新增来源请说明主题/岗位关联、原始链接、固定提交和许可证，详见 [贡献指南](CONTRIBUTING.md)。

## 来源与许可

网站实现的原创代码采用 [MIT](LICENSE)。原始 LLM Master 保留 [上游 MIT 许可](LICENSE.upstream)；扩展资料遵守各自许可证，正文包中保存完整许可，详见 [第三方说明](THIRD_PARTY_NOTICES.md) 与 [来源清单](docs/sources.md)。本站原创导读采用 CC BY 4.0。

未声明许可及仅适合索引的来源提供原文链接。面经保留作者经验、社区汇编和 AI 辅助题解标识；没有逐条独立核验招聘事件。本轮收录为已检索核验的相关来源，不声称穷尽互联网。实现、分类和导读由 AI 辅助完成。

感谢 [LLM Master](https://github.com/youngyangyang04/llm-master) 与所有资料作者。视觉灵感来自 [Codex Resets · Tibo 28](https://codex-resets.com/zh-CN/tibo-28)。

**关键词**：大模型、LLM、面试题、面经、求职、就业笔记、学习路线、知识地图、RAG、Agent、Transformer、微调、AI Infra、系统设计、React、Vite、Vercel、interactive learning、interview preparation、career roadmap。
