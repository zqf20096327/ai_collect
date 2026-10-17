# 🚀 飞书 + cc-connect + Claude Code：把 AI 编程助手装进聊天框

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![cc-connect](https://img.shields.io/badge/cc--connect-v1.3.2-green)](https://github.com/chenhg5/cc-connect)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-latest-orange)](https://docs.anthropic.com/en/docs/claude-code)

**在飞书上用自然语言指挥 AI 写代码、处理数据、生成报告，所有操作在你的云服务器上执行。**

> **七大卖点：**
> - 🇨🇳 **不用梯子** — 飞书 + DeepSeek + 国内云服务器，全链路墙内直连
> - 📱 **手机控电脑** — 飞书即终端，手机上发消息就能操控云服务器，跑代码/处理文件/查状态
> - 💾 **对话可保存** — 记忆系统跨会话持久化，偏好、规范、上下文永不丢失
> - 📖 **长文本便携** — 手机/电脑随时接入，长篇对话随身走，碎片时间也能推进任务
> - 💰 **成本极低** — DeepSeek API 仅官方 1/10 价格，日均不到一杯咖啡
> - ⏰ **24 小时在线** — 云服务器 + systemd 守护进程，永不休眠
> - 👁️ **多模态可用** — 可读图、读 PDF、接入视觉小模型处理图文混合任务

[English](README_EN.md) | [飞书配置](docs/setup-feishu.md) | [Claude Code](docs/setup-claudecode.md) | [DeepSeek](docs/setup-deepseek.md) | [进阶](docs/advanced.md)

---

## 整体架构

```
飞书客户端（手机/电脑）
    │  「@机器人 帮我把这个 ZIP 处理了」
    ▼
飞书开放平台 Bot API
    │
    ▼
cc-connect（消息桥接层，systemd 守护进程，断线自动重连）
    │
    ▼
Claude Code CLI（AI 编程代理）
    │
    ├─→ DeepSeek / Anthropic API（推理后端）
    ├─→ MCP 工具链（文件系统 / 浏览器 / GitHub）
    └─→ 你的云服务器文件系统
```

**核心思路**：飞书 = 交互入口 → cc-connect = 消息桥接 → Claude Code = 执行引擎 → DeepSeek API = AI 大脑。

## 为什么选这套方案？

| 对比维度 | 官方 Claude Code | 本方案 |
|:--|:--|:--|
| 交互方式 | 终端命令行 | **飞书聊天**（手机/电脑均可） |
| API 成本 | $15-75 /百万 token | **¥2-8 /百万 token** |
| 数据安全 | 本地执行 | **你的云服务器上执行** |
| 多设备 | 仅终端所在设备 | **任意设备登录飞书即用** |
| 多人协作 | 不支持 | **飞书群里多人共用** |
| 定时任务 | 无 | **Cron 定时自动执行** |

## 快速开始（5 分钟）

### 前置条件

- 一台云服务器（Ubuntu 20.04+，2核4G 即可，推荐 [阿里云 ECS](https://www.aliyun.com/product/ecs) / [腾讯云 CVM](https://cloud.tencent.com/product/cvm)）
- 飞书管理员权限（创建机器人应用）
- DeepSeek API Key（[platform.deepseek.com](https://platform.deepseek.com) 注册即送额度）

### 一键安装

```bash
git clone https://github.com/miaojiee/feishu-claude-code.git
cd feishu-claude-code
bash scripts/install.sh
```

### 手动安装

```bash
# 1. 安装 Node.js 18+
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# 2. 安装核心组件
npm install -g cc-connect
npm install -g @anthropic-ai/claude-code

# 3. 创建配置
mkdir -p ~/.cc-connect ~/.claude
cp config/config.toml.example ~/.cc-connect/config.toml
cp config/settings.json.example ~/.claude/settings.json

# 4. 修改配置文件，填入你的飞书 App ID/Secret 和 DeepSeek API Key
# vim ~/.cc-connect/config.toml
# vim ~/.claude/settings.json

# 5. 启动服务
cc-connect daemon install
cc-connect daemon status
```

### 验证

在飞书中找到你的机器人，发送：

```
@机器人 列出当前目录的文件
```

收到回复即表示配置成功。

## 详细配置

| 步骤 | 文档 |
|:--|:--|
| 飞书机器人创建与权限配置 | [docs/setup-feishu.md](docs/setup-feishu.md) |
| cc-connect 安装与启动 | [docs/setup-ccconnect.md](docs/setup-ccconnect.md) |
| Claude Code 安装与配置 | [docs/setup-claudecode.md](docs/setup-claudecode.md) |
| DeepSeek API 接入（Anthropic 兼容端点） | [docs/setup-deepseek.md](docs/setup-deepseek.md) |
| MCP 工具链扩展 | [docs/setup-mcp.md](docs/setup-mcp.md) |

## 最佳实践

### Agent Team —— 像管理团队一样管理 AI

一台服务器 + 一个 cc-connect，通过多项目配置将不同飞书群映射为不同"AI 员工"。人在群中发号施令，CEO 角色。上下文隔离、独立记忆、互不干扰。

### 数据产线 —— 一条消息从原始文件到成品

将完整的数据处理规范沉淀为 AI 记忆，此后每次上传原始文件，AI 自动按规范执行全流程，人在关键节点确认即可。

效果：手动 2-3 小时 → 自动化 6-10 分钟，格式一致性 100%。

详见：[docs/examples.md](docs/examples.md)

## API 成本对比

| API 提供商 | 模型 | 输入 (per 1M tokens) | 输出 (per 1M tokens) | 月均费用 |
|:--|:--|:--|:--|:--|
| Anthropic 官方 | Claude Opus 4 | $15 | $75 | ~$200-500 |
| Anthropic 官方 | Claude Sonnet 4 | $3 | $15 | ~$50-150 |
| **DeepSeek** | **v4-pro** | **¥2** | **¥8** | **¥50-100** |
| **DeepSeek** | **v4-flash** | **¥0.5** | **¥2** | **¥10-30** |

> 实测：日均 5-10 次复杂数据处理任务，月均费用 ¥50-100（约 $7-14）。

## 进阶玩法

- **Cron 定时任务**：每天定时检查数据更新、每周定时生成报告
- **多项目隔离**：不同飞书群 → 不同工作目录，互不干扰
- **记忆系统**：AI 记住你的偏好、规范、工作流细节
- **MCP 工具链**：接入浏览器自动化、GitHub 操作等

详见：[docs/advanced.md](docs/advanced.md)

## 配置模板

| 文件 | 用途 |
|:--|:--|
| [config/config.toml.example](config/config.toml.example) | cc-connect 飞书桥接配置 |
| [config/settings.json.example](config/settings.json.example) | Claude Code + DeepSeek API 配置 |

## 项目文件结构

```
feishu-claude-code/
├── README.md                       # 主文档（中文）
├── README_EN.md                    # English version
├── LICENSE                         # MIT
├── .gitignore
├── docs/
│   ├── setup-feishu.md             # 飞书配置详解
│   ├── setup-feishu.md             # 飞书机器人配置
│   ├── setup-ccconnect.md          # cc-connect 安装与配置
│   ├── setup-claudecode.md         # Claude Code 安装与配置
│   ├── setup-deepseek.md           # DeepSeek API 接入
│   ├── setup-mcp.md                # MCP 工具链
│   ├── examples.md                 # 最佳实践详解
│   └── advanced.md                 # 进阶玩法
├── config/
│   ├── config.toml.example         # cc-connect 配置模板
│   └── settings.json.example       # Claude Code 配置模板
└── scripts/
    └── install.sh                  # 一键安装脚本
```

## 常见问题

### 国内用户必读

这套方案的所有环节都可在国内直连：

| 组件 | 归属 | 国内访问 |
|:--|:--|:--|
| 飞书开放平台 | 字节跳动 | ✅ 直连 |
| DeepSeek API | 深度求索（中国） | ✅ 直连，低延迟 |
| 阿里云/腾讯云 ECS | 中国公司 | ✅ |
| cc-connect (npm) | GitHub 开源 | ⚠️ 需淘宝镜像 |
| Claude Code (npm) | Anthropic | ⚠️ 需淘宝镜像 |
| settings.json 中的遥测 | anthropic.com | 已默认关闭 |

**安装脚本已自动处理 npm 淘宝镜像**（`registry.npmmirror.com`）。手动安装的话：

```bash
npm config set registry https://registry.npmmirror.com
npm install -g cc-connect @anthropic-ai/claude-code
```

### 其他问题

| 问题 | 解决 |
|:--|:--|
| 飞书不回复 | `cc-connect daemon logs -f` 查看日志 |
| API 报错 401 | 检查 DeepSeek API Key 和 Base URL |
| 处理超时 | 增大 `API_TIMEOUT_MS`，建议 600000（10分钟） |
| 服务宕机 | `cc-connect daemon restart` 重启 |
| DeepSeek 模型改名 | 查看 [DeepSeek 文档](https://platform.deepseek.com/api-docs) 获取最新模型名 |

## 安全提醒

- `config.toml` 和 `settings.json` 包含 API Key，**不要提交到 Git**
- `bypassPermissions` 仅在单人私密环境使用
- 建议在云服务器上创建专用用户运行 cc-connect
- 定期查看 `~/.cc-connect/logs/cc-connect.log` 审计日志

## 依赖与致谢

- [cc-connect](https://github.com/chenhg5/cc-connect) — 消息平台桥接框架
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic 的 AI 编程 CLI
- [DeepSeek](https://platform.deepseek.com) — 高性价比 AI API

## License

MIT © 2026
