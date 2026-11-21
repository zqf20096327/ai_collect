# 和觅 Hermix

**可私有部署的 AI 智能体平台。**

把大模型变成能真正干活的数字员工 —— 多个智能体各司其职、共享知识库、定时执行任务、通过企业微信 / 飞书 / 钉钉直接对话。整套系统跑在你自己的服务器上，数据不出内网。

**开源内核在这里，官网在 [hermix.cn](https://hermix.cn)** —— 私有化部署、定制开发与技术支持。

> 本项目基于 [Hermes Agent](https://github.com/NousResearch/hermes-agent)（MIT License，Copyright © 2025 Nous Research）二次开发。内核能力归功于上游项目，我们在其之上完成了中文场景适配、可视化控制台与多智能体编排。详见 [NOTICE](NOTICE)。

![和觅 Hermix 控制台总览](docs/screenshots/overview.png)

*控制台总览 —— 系统资源、Agent 一览、服务器拓扑一屏看全*

---

## 它解决什么问题

现成的 AI 助手大多是「一个对话框，问一句答一句」。真要用起来，你需要的是：

- **多个角色分工** —— 开发、销售、运营各有一套人格、知识库和权限
- **能自己动** —— 定时巡检、抓数据、发报告，不用人催
- **有记忆** —— 记得上次聊到哪、你偏好什么
- **能接进现有工具** —— 企业微信里直接 @ 它，不用再开一个 App
- **数据自己拿着** —— 客户信息、对话记录、知识库都在自己服务器上

和觅就是把这些拼成一个完整系统。

---

## 核心能力

### 多智能体

每个智能体是一个独立的 Hermes profile，拥有自己的：

```
人格设定（SOUL.md）   角色定位、说话风格、行为边界
知识库                专属文档，支持全文检索
技能                  可调用的工具集
模型配置              不同角色用不同模型，成本可控
消息通道              各自的企微/飞书/钉钉机器人
```

智能体之间互相独立，一个崩了不影响其他。

### 可视化控制台（Dashboard）

无需命令行，浏览器里完成全部管理：

- **总览** — 系统负载、Agent 状态、服务器拓扑一屏看全
- **Agent 管理** — 启停、配置、查看运行时长与内存占用
- **对话调试** — 实时看智能体怎么想、调了什么工具、花了多少 token
- **知识库** — 上传文档、切片、检索测试
- **定时任务** — Cron 可视化管理，执行记录可追溯
- **技能管理** — 查看、启用、编辑技能
- **费用统计** — 按模型 / 按智能体统计消耗

| 智能体管理 | 知识库 |
|---|---|
| ![智能体管理](docs/screenshots/agents.png) | ![知识库](docs/screenshots/knowledge.png) |

### 技能系统（Skills）

智能体的可复用能力包。一个技能就是一个 `SKILL.md` + 可选脚本：

```
skills/
└── my-skill/
    ├── SKILL.md          触发条件 + 操作步骤 + 踩坑记录
    ├── scripts/*.py      可执行脚本
    └── references/*.md   详细文档
```

智能体会根据任务自动加载相关技能 —— 这是它「越用越顺手」的来源。

### 定时任务

自然语言描述频率，系统生成 Cron 表达式。支持投递到对话、本地文件、或指定消息通道。

### 多消息通道

企业微信、飞书、钉钉、Telegram、邮件 —— 同一套智能体，多个入口。

### 运行监控

系统负载、磁盘水位、服务健康一屏可见。服务器拓扑只画真实节点 —— 演示数据不进图。

---

## 技术栈

```
内核      Python 3.11+ · Hermes Agent
前端      React + TypeScript + Vite
样式      Tailwind CSS
数据      SQLite（本地）
部署      Linux · systemd · nginx / Caddy
模型      DeepSeek · OpenAI · Claude · Qwen · 本地 Ollama
```

---

## 快速开始

### 环境要求

```bash
Python 3.11+    Node.js 20+    Linux / macOS
```

### 安装

```bash
git clone https://github.com/wuyang1979/hermix.git
cd hermix

python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### 配置模型

```bash
hermes config set model.provider deepseek
hermes config set model.api_key sk-xxxxx
```

### 启动

```bash
# 命令行对话
hermes

# 启动 Gateway（消息通道 + HTTP API）
hermes gateway

# Dashboard 开发模式
cd web && npm install && npm run dev
```

Dashboard 默认端口 `3000`，生产环境建议 nginx 反代 + HTTPS。

### 部署第一个智能体

```bash
hermes profile create my-agent
cd ~/.hermes/profiles/my-agent

cat > SOUL.md <<'EOF'
你是我的客服助理，说话简洁，不夸大，不确定的事说不确定。
EOF

hermes gateway --profile my-agent
```

---

## 目录结构

```
hermix/
├── agent/            Agent 核心循环
├── tools/            工具集（终端、文件、搜索、浏览器…）
├── gateway/          消息网关（多平台接入）
├── hermes_cli/       命令行接口
├── web/              Dashboard 前端（React + TS）
├── plugins/          插件（总览、Agent 管理、多服务器管理…）
├── skills/           内置技能
├── environments/     开发环境配置
├── tests/            测试
└── docs/             文档
```

---

## 设计约束

这些不是偏好，是实际踩坑后定下来的规则：

**数据诚实**

- 统计口径以 `visitor_id` 标识访客，不用 IP 当人
- 历史数据缺失就标缺失，不做比例估算填充
- 虚拟 / 演示数据必须显式标记，且不得进入真实展示（报表、拓扑、统计）
- 测试网段一律用 RFC5737 TEST-NET（`192.0.2.0/24` 等）

**安全**

- 密钥只从环境变量读，代码里不出现明文
- 生产环境凭据、客户数据不进仓库
- Dashboard 对外访问必须加认证（Basic Auth 或 OAuth）

**部署**

- 静态产物跨机器部署不能整体覆盖 —— 构建时路径是硬编码的
- 部署后必须自检，不能只看 HTTP 200

---

## 与上游的关系

| 部分 | 来源 |
|---|---|
| Agent 内核、工具系统、Gateway | Hermes Agent（Nous Research，MIT） |
| Dashboard 前端 | 基于上游 Web 界面重构 |
| 中文适配、多智能体编排、插件体系 | 本项目新增 |
| 消息通道适配 | 上游提供，本项目做了国内平台适配 |

**我们不会把上游的东西说成自己的。** MIT 许可允许商业使用和再发布，但要求保留原版权声明 —— `LICENSE` 文件原样保留，修改说明见 `NOTICE`。

上游原始说明保留在 [README.upstream.md](README.upstream.md)。

---

## 基于 Hermix 构建

| 项目 | 说明 | 访问 |
|---|---|---|
| [hermix.cn](https://hermix.cn) | 产品官网、能力说明、在线试用 | 公开 |
| [金陵奇缘](https://jinling.itspacex.cn) | 国潮 H5：人格测试 + 国风写真生成 | 公开 |
| 政策通 | 多租户政策申报 SaaS（FastAPI + React） | 内部部署 |
| AI 外呼 | 智能外呼坐席，接 DeepSeek 做实时对话 | 内部部署 |

这些是团队基于本开源内核落地的业务系统。**核心商业代码不在本仓库**，这里只说明内核的实际承载能力 —— 它跑到过真实业务里，不是玩具。

---

## 许可证

MIT License。可商用、可修改、可闭源分发，保留版权声明即可。

- 上游版权：Copyright © 2025 Nous Research（见 `LICENSE`）
- 本项目修改：见 `NOTICE`
