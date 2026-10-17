<p align="center">
  <img src="banner.png" width="100%" alt="Grok Build 从零到精通蓝皮书" />
</p>

# Grok Build 从零到精通蓝皮书

> 智见 AI 蓝皮书系列 · 大鹏主编 · 公开测试版 v0.1.0 · 资料截止 2026-08-15

一本面向零基础读者，以及 Claude Code / Codex 用户的 Grok Build 实战指南。

全书 150 页，从第一次打开终端开始，逐步覆盖任务合同、上下文、权限、Skill、MCP、Hooks、会话恢复、Headless、CI、多 Agent、自动化与迁移，并配有 12 个递进项目和可运行示例。

## 在线阅读

[**打开 GitHub Pages 在线版 →**](https://zjp1997720.github.io/grok-build-bluebook/)

网页版与仓库中的单文件 HTML 内容一致，无需下载即可直接阅读。首次打开需要加载完整书籍，移动网络下请稍候。

## 下载

| 格式 | 文件 | 说明 |
|---|---|---|
| PDF | [**Grok-Build-Bluebook-zh-v0.1.0.pdf**](Grok-Build-Bluebook-zh-v0.1.0.pdf) | 适合本地阅读与转发，150 页 A4 |
| 在线 HTML | [**直接阅读网页版**](https://zjp1997720.github.io/grok-build-bluebook/) | GitHub Pages 在线预览，无需下载 |
| HTML 文件 | [Grok-Build-Bluebook-zh-v0.1.0.html](Grok-Build-Bluebook-zh-v0.1.0.html) | 单文件自包含版，适合离线保存 |

> PDF 建议下载后阅读。GitHub 在线预览大文件时可能加载不完整。

## 这本书解决什么问题

- **零基础也能开始**：终端、目录、仓库、权限和验证都从人话讲起。
- **从 Claude Code / Codex 丝滑迁移**：不是简单列功能，而是告诉你哪些资产能直接带走、哪些需要适配、哪些必须重做。
- **不只讲命令**：把 Agent 的任务合同、上下文、工具、权限、会话和自动化串成一套可操作的心智模型。
- **强调可验证结果**：每个关键项目都有输入、执行、验收、失败语义和恢复路径。
- **把安全边界说清楚**：重点解释最小权限、沙箱、网络、第三方扩展、Headless 与 CI 中的真实风险。
- **图片不是装饰**：知识图、终端实录与智见小蓝场景图共同承担解释任务。

## 全书结构

| 部分 | 内容 |
|---|---|
| 基础认知 | Coding Agent 心智模型、Grok Build 产品边界、安装与诊断 |
| 第一次可验证任务 | 任务合同、终端与仓库、计划—执行—验证闭环 |
| 上下文与协作 | 压缩恢复、规则冲突、Git、测试与多人协作 |
| 扩展系统 | 模型与模式、Skills、MCP、Plugins、Hooks、LSP |
| 控制与安全 | 配置、inspect、权限、工具、沙箱、网络、隐私与 worktree |
| 高阶能力 | 会话交接、Headless、JSON、CI、ACP、多 Agent、Workflow 与 Goal |
| 项目集 | 12 个递进项目，从第一次任务走到自动化审查与跨工具迁移 |
| 附录 | 命令速查、配置样例、术语、故障恢复、FAQ、迁移矩阵与安全清单 |

## 可运行示例

[`examples/`](examples/) 提供书中公开示例，包括：

- 两阶段、无长期密钥的 CI 审查参考实现；
- CSV 清洗、重试策略、Bug 修复与多任务编排项目；
- Claude Code / Codex 向 Grok Build 迁移时的扩展桥接样例；
- 配套测试、固定输入和预期输出。

示例是学习材料，不代表真实线上模型、网络或 GitHub Actions 已替你完成端到端认证。接入真实仓库前，请先在隔离环境中验证。

## 版本与时效边界

本书冻结于 **Grok Build CLI 1.0.3**，对应快照 `1a29d5bc12d4`，资料截止日期为 **2026-08-15**。

AI Agent 产品变化很快。书中的产品行为、命令和默认值都应放在这个版本边界内理解；使用更新版本时，请同时核对官方文档和本机 `grok version`、`grok doctor`、`grok inspect --json` 的结果。

## 许可

- 本书原创正文与编译成品：[`CC BY-NC-SA 4.0`](licenses/CC-BY-NC-SA-4.0.md)，允许署名、非商业分享和改编，并要求相同方式共享。
- [`examples/`](examples/) 下的原创示例代码：[`MIT`](licenses/MIT.txt)。
- 智见 AI 名称、Logo、智见小蓝角色及品牌母资产保留权利，不因本仓库公开而获得再许可。
- xAI、Grok、Claude、Claude Code、OpenAI、Codex 等名称和商标归各自权利人。

完整边界见 [`LICENSES.md`](LICENSES.md)。

## 关于作者

**大鹏｜智见 AI**

智见科技创始人，AI 落地顾问、企业与高校培训讲师，长期研究 Agent、Skill、Context Engineering 与 AI 编程工作流。

- 公众号 / 视频号：智见AI
- GitHub：[@zjp1997720](https://github.com/zjp1997720)

## 仓库边界

这个仓库只发布读者交付物和可运行示例，不包含内部写书 Skill、研究控制面、审稿记录或生产工作流。
