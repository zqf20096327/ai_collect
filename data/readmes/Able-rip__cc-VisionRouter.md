# cc-VisionRouter

**中文** | [English](./README.en.md)

> 让不支持图片的主力模型，也能在 Claude Code 里安全跑长程任务——含图片的请求自动分流到多模态模型，session 不再因为一张图就崩。

## 这个噩梦你大概率见过

在 Claude Code 里接第三方 API（mimo、各类国产 / 自建模型）跑活，尤其跑**长程任务**——跑着跑着，蹦出这一行：

```
There's an issue with the selected model (mimo-v2.5-pro). It may not exist
or you may not have access to it. Run /model to pick a different model.
```

任务戛然而止。

根因常常不是"模型不存在"，而是 **你的主力模型不支持多模态**。可一旦上下文里混进**任何**图片——你贴的截图、工具返回的图、甚至 `/compact` 压缩历史时扫到早先的那张图——请求就带着图片打到一个看不懂图的模型上，**直接挂**。

短对话重开一把就算了。但对**长程任务**这是灭顶之灾：几十轮、几十万 token 攒起来的上下文，因为一张图全断，**没法自动续**。这是所有想用三方模型跑 autonomous / 长任务的人共同的噩梦。

## 我们的思路：按内容分流，你无感

cc-VisionRouter 是夹在 Claude Code 和上游之间的**透明代理**。它不替你换模型、不打断你的工作流，只做一件事——**看每个请求里有没有图片，再决定送给谁**：

```
Claude Code → cc-VisionRouter → 上游 API
                    │
          ├─ 含图片 / 文档     → 多模态模型（你指定）
          ├─ 背景 / 压缩任务   → 多模态模型（历史里可能有图）
          └─ 其余纯文本        → 你的主力模型
```

- **日常编码**继续用你最强 / 最省的主力模型，零改变；
- **图片来了**自动分流到多模态模型，主力模型永远不会"看到"它看不懂的东西，session 不会因为一张图崩；
- **长任务里 `/compact` 压缩含图历史**也走多模态，不会在自动压缩那一刻爆掉；
- 全程**不用手动 `/model` 切换**，模型名翻译、`[1m]` 后缀、settings 改写还原，代理全包了。

一句话：**让你能安心用三方模型跑长任务，图片不再是中断点。**

## 安装

> 需要 Node.js ≥ 18（用到原生 fetch / Web Streams）。

**全局安装（推荐）** — 从 npm 装，装完就有 `cc-visionrouter` 命令：

```bash
npm install -g cc-visionrouter
cc-visionrouter
```

**或直接从 GitHub 装**（始终最新，无需等 npm 发版）：

```bash
npm install -g github:Able-rip/cc-VisionRouter
```

**或克隆到本地（开发 / 贡献）**：

```bash
git clone https://github.com/Able-rip/cc-VisionRouter.git
cd cc-VisionRouter
npm install
node cli.mjs
```

> 下文命令以全局安装的 `cc-visionrouter` 为例；本地跑就把它换成 `node cli.mjs`。

## 使用

```bash
cc-visionrouter           # 交互式菜单
cc-visionrouter config    # 配置模型
cc-visionrouter start     # 启动代理
cc-visionrouter stop      # 停止代理
cc-visionrouter status    # 查看状态
cc-visionrouter logs      # 查看日志
```

配置过程中，选择题可选 `← 返回上一级`，也可按 `Esc` 返回；输入框/API Key 框按 `Esc` 返回上一项。

**配置自检**：填完会自动用一个最小请求（`max_tokens:1`）测一遍 baseUrl / key / model 是否真能通，通了才让保存——避免乱填也能存下一个跑不起来的配置。测不通会报具体错误并问你是否仍要保存。

## 语言

界面**自动跟随系统 locale**（中文系统显示中文，其它显示英文）。覆盖方式：

- 环境变量：`CC_VR_LANG=en`（或 `zh`）
- 交互菜单里选「语言 / Language」即时切换，并记住选择

## 更多机制

**背景任务也走视觉模型**：Claude Code 的后台请求（`/compact`、对话压缩、总结等，即 haiku 档）是在**整段历史**上跑的，历史里可能含图片。若塞给不支持图片的主力模型会报错、甚至把会话搞崩。所以代理把背景/haiku 请求也路由到视觉模型（多模态、通常更轻），既安全又省 token。背景请求的识别是自动的（探测 Claude Code 的 haiku / small-fast 模型名），无需配置。

**模型名自动改写**：Claude Code 发来的 `model` 字段会被直接替换成你配置里的真实模型 id，再转发给上游。你无需关心 Claude Code 那边配的是什么模型名——代理屏蔽了「Claude Code 模型命名」与「上游真实 model id」之间的不一致。

**自动剥离 `[1m]` 等后缀**：很多 ccswitch / 国产 1M 模型的配置里模型名带 `[1m]`（如 `mimo-v2.5-pro[1m]`）。Claude Code 会对这类后缀做**客户端校验**，上游若不认识就直接报 “issue with the selected model”（请求都到不了代理）。`start` 时 cc-VisionRouter 会自动把 `~/.claude/settings.json` 里模型字段的 `[...]` 标记剥掉（原值已备份，`stop` 时还原）。

## 内置预设

| 预设 | 主力模型 | 视觉模型 |
|------|----------|----------|
| 从 Claude Code 导入 | 你已配置的模型里选 | 同左 |
| mimo | mimo-v2.5-pro | mimo-v2.5 |
| Claude | claude-opus-4 | claude-sonnet-4 |
| 自定义 | 手动配置 | 手动配置 |

## Claude Code 配置

`cc-visionrouter start` 会**自动**改写 `~/.claude/settings.json` 的 `ANTHROPIC_BASE_URL` 指向代理（`http://127.0.0.1:<port>`），并在 `stop` 时还原（原始配置备份在 `~/.cc-visionrouter/settings.backup.json`）。无需手动改。

> ⚠ **改完必须完全退出并重启 Claude Code**。Claude Code 只在启动时读 `settings.json`，运行中的会话不会切到代理。

## 协议兼容性（重要）

本工具是 **Anthropic Messages API**（`/v1/messages`）的透明代理，只改 `model` 字段做路由，其余原样转发。

- ✅ **支持**：Anthropic 官方 API，以及提供 Anthropic 兼容端点的网关（小米 MiMo `/anthropic`、OpenRouter 等）。
- ❌ **不支持**：OpenAI 格式上游（`/v1/chat/completions`）。DeepSeek、SiliconFlow、智谱 BigModel、阿里 DashScope 的默认 API 都是 OpenAI 格式，**不能**直接配进来（除非它们另外提供了 Anthropic 兼容端点）。

鉴权同时发送 `x-api-key` 和 `Authorization: Bearer`，两类网关都能兼容。

## 默认透传

只有 `/v1/messages` 和 `/v1/messages/count_tokens` 会做「图片检测 + 模型路由」，**其余所有路径/方法**（含带查询串如 `?beta=true`、Claude Code 未来新增的端点）都原样转发给上游，不会被挡。`HEAD/GET /` 健康探活本地直接回 200。

## 与 ccswitch 共存

cc-VisionRouter 和 ccswitch 都会改 `~/.claude/settings.json` 的 `env`。**代理运行期间不要再用 ccswitch 切换供应商**，否则 `stop` 还原时可能覆盖掉 ccswitch 的改动。正确顺序：先 `cc-visionrouter stop`，再用 ccswitch 切换。

## 已知限制

- 路由是二元的：含 `image` / `document`（PDF 视觉）块 → 视觉模型；否则 → 主力模型。
- 流式（SSE）已支持，按字节透传上游响应。
- 上游超时默认 10 分钟（可用环境变量 `CC_VR_TIMEOUT_MS` 覆盖），`429/503` 自动退避重试一次。
- API key 以明文存于 `~/.cc-visionrouter/config.json`，请注意该文件权限。

## 故障排查

**启动代理后还是报 “model 不存在 / 无权限”，或日志里没有任何请求记录？**

99% 是 **Claude Code 没重启**。它只在启动时读 `settings.json`，已开着的会话不会切到代理 → 继续直连旧地址。

→ **完全退出 Claude Code，再重新打开。** 用 `cc-visionrouter logs` 确认请求是否真的经过代理（应能看到 `text → primary` / `image → vision` 记录）。日志全空 = 没走代理。

**深度排查**：用 `CC_VR_DEBUG=1` 启动代理（如 `CC_VR_DEBUG=1 cc-visionrouter start`），会把**每一个进来的请求**（`>>> METHOD URL`，含被透传的端点）都记进日志。新版本 Claude Code 若改了请求形态，这能一眼看出它实际打了什么。

## 测试

```bash
npm test    # node --test：检测逻辑 / i18n / 代理流式·路由·透传·header 集成测试
```

## 版本规范

遵循 [SemVer](https://semver.org/lang/zh-CN/)，版本号唯一来源是 `package.json` 的 `version`（菜单标题等都由它派生，不要硬编码）。

- **MAJOR** — 破坏性变更（config.json schema 不兼容、命令行为变更）
- **MINOR** — 向后兼容新功能
- **PATCH** — 向后兼容修复 / 文档

发布：改 `package.json` 版本 → 在 [CHANGELOG.md](./CHANGELOG.md) 加一条 → `git tag v<x.y.z>`。

## License

[MIT](./LICENSE)
