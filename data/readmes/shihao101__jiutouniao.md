<div align="center">

# 九头鸟（鬼車）· Jiutouniao

**通用型实战型 AI 渗透测试智能体平台**

An open-source, full-lifecycle AI agent platform for **authorized** penetration testing —
multi-head orchestration, human-in-the-loop approvals, deterministic governance gates,
and evidence-chain reporting.

[![CI](https://img.shields.io/github/actions/workflow/status/shihao101/jiutouniao/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/shihao101/jiutouniao/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/shihao101/jiutouniao?style=flat-square)](https://github.com/shihao101/jiutouniao/releases)
[![License](https://img.shields.io/github/license/shihao101/jiutouniao?style=flat-square)](LICENSE)
**当前版本 v6.0.0** · [完整更新记录](CHANGELOG.md)
![Go](https://img.shields.io/badge/Go-1.23%2B-00ADD8?style=flat-square&logo=go)
![Vue](https://img.shields.io/badge/Vue-3-42B883?style=flat-square&logo=vue)

</div>

---

## ⚠️ 合规声明

**仅供书面授权的渗透测试与安全研究使用。** 对未授权目标使用本项目属违法行为，责任由使用者自行承担。平台内置合规护栏，默认不可绕过：

1. **无授权不开工** — 项目创建时必须填写授权范围与 ROE，强制核验；
2. **审批矩阵** — 只读侦察（L0）自动执行，写/利用类高危动作（L1/L2）必须人工在 Web 界面批准，破坏性命令（FORBIDDEN）直接拒绝；
3. **一键熔断** — 任何时刻可中止全部自主操作并撤销待批工单，另支持 token 预算熔断；
4. **确定性治理门** — Execution Profile 双运行模式（生产档默认禁止植入后门/持久化/批量导出/状态变更，只做存在性证明）+ ROE 注册写门 + strict_scope 范围门，接入全部命令执行通道，先于审批校验并留证。

## ✨ 核心特性

- **全流程编排**：s1 资产 → s2 侦察 → s3 威胁建模 → s4 漏洞发现 →（专项 A/B1/B2）→ s5 利用 → s6 后渗透（可选）→ s7 收尾 → s8 报告，阶段间自动回环直到拿下业务影响证明——八个阶段专家头 + 三个专项头 + 一个主控真头
- **126 个中文攻击剧本**：`skills/` 技能库按需 `load_skill` 注入，覆盖 Web/内网/AD/APP/小程序/云/LLM 目标
- **确定性质量门**：结论-证据硬校验、覆盖对账、孤儿探测归账——零 LLM 成本的引擎级反幻觉
- **防幻觉产出链**：每阶段强制实体文件交付，下一阶段以文件为事实来源承接
- **多模型接入**：OpenAI / Anthropic 双协议，任何兼容端点可用（官方 / 中转站 / Ollama / vLLM）；Web 设置页多模型注册表 + 连通性实测 + 按项目选模型；无 Key Mock 演示模式
- **工程化**：断点续跑、阶段内并行扇出、输出治理、Token 分账、SARIF/JSON 导出、攻击路径缝合图、组织级教训库
- **Kali 工具链底座**：nmap/sqlmap/nuclei/hydra/jadx 等开箱即用，缺什么现场装什么

## 🏗 架构

```
                         ┌─────────────────────────────┐
                         │      Web 控制台 (中文)        │
                         │ 项目看板·执行流·审批队列·报告  │
                         └──────────────┬──────────────┘
                                  WebSocket + REST
┌────────────────────────────────────────┼─────────────────────────────────────┐
│  Go 核心引擎（并发：goroutine 池 / 单二进制）                                     │
│                                        ▼                                      │
│  ┌──────────┐   ┌───────────────────────────────┐   ┌──────────────────────┐ │
│  │ 主控·真头 │──▶│ 执行循环（流程图 E 引擎 9 步）    │──▶│ 审批矩阵 + 熔断器      │ │
│  └──────────┘   │ 决策→分级→审批→执行→观察→       │   └──────────────────────┘ │
│                 │ 反思→记忆→停止                  │   ┌──────────────────────┐ │
│                 └───────────────┬───────────────┘──▶│ 工具执行器(沙箱+留证)  │ │
│                                 ▼                   └──────────────────────┘ │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ 八个阶段头 + 三个专项头（中文提示词 = 方法论编码）                          │  │
│  │ s1资产 s2侦察 s3威胁建模 s4漏洞发现 → [专项A/B1/B2] →                    │  │
│  │ s5利用 s6后渗透 s7收尾 s8报告              （↺ 阶段4↔5 新线索回环）      │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                 ▼                                            │
│  bbolt 记忆库：项目状态 / 资产 / 发现 / 攻击时间线 / 审批 / 证据链                │
└─────────────────────────────────────────────────────────────────────────────┘
                                 ▼
                  LLM（OpenAI / Anthropic 双协议：官方 API / 中转站 / Ollama / vLLM）
```

## 🚀 快速开始

### Docker 部署（推荐：Kali 全量工具链开箱即用）

```bash
git clone https://github.com/shihao101/jiutouniao.git && cd jiutouniao
cp config.example.json config.json    # 必填 llm.api_key/base_url/model；必改 admin_password
docker compose up -d --build          # 首次构建 15-40 分钟（拉底座 + 编译 + 语料克隆）

# 验收
curl http://127.0.0.1:8787/api/public/info
```

浏览器打开 `http://127.0.0.1:8787` → 默认 `admin / jiutou@2026`（**部署后必改**）→ 新建项目（目标/授权范围/ROE）→ ▶ 启动。

### 本地运行（无 Docker）

```bash
make build    # 编译 Go 引擎（Go 1.23+，vendor 自洽）
make web      # 构建前端（Node 20+）
make run      # 启动，默认 http://localhost:8787
```

> 本地模式下安全工具按各阶段头的降级指引执行；完整工具链建议 Docker 部署。

### 配置 LLM

编辑 `config.json`（任何 OpenAI 兼容端点或 Anthropic 协议均可），或在 Web 设置页配置多模型：

```json
{
  "llm": {
    "protocol": "openai",
    "base_url": "https://your-endpoint/v1",
    "api_key": "sk-xxx",
    "model": "your-model",
    "mock": false
  }
}
```

> 无 Key 体验：保持 `"mock": true` 即可以演示模式走完整流程。

## 🛡 审批矩阵（默认规则，config.json 可调）

| 等级 | 含义 | 示例 | 处置 |
|---|---|---|---|
| L0 | 只读侦察 | `nmap -sV`、`cat`、`curl -s`、`dig` | 自动执行 |
| L1 | 写操作/扫描载荷 | `nuclei`、`wget`、`apt install` | 人工批准 |
| L2 | 利用/横向/提权 | `sqlmap --dump`、`exploit`、自研 PoC 执行 | 人工批准 |
| FORBIDDEN | 破坏性/DoS | `rm -rf /`、`mkfs`、`iptables -F` | 直接拒绝 |

## 📚 文档

| 文档 | 内容 |
|---|---|
| [docs/FEATURES.md](docs/FEATURES.md) | 完整功能详解：移植模块表 / Docker 部署细节 / 代理接入 / 部署包 Quickstart / API 一览 / 流程图映射 / 二次开发指引 |
| [CHANGELOG.md](CHANGELOG.md) | 完整版本历史（与 Web「更新记录」同源） |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 开发环境 / 提交规范 / 安全边界 |
| [SECURITY.md](SECURITY.md) | 漏洞私密披露通道 + 部署安全基线 |
| [docs/case-study/](docs/case-study/) | 脱敏实战案例记录 |

## 🤝 贡献

欢迎 Issue / PR——提交前请过 [CONTRIBUTING.md](CONTRIBUTING.md)（含合规护栏自查与敏感信息扫描纪律）。安全漏洞请走 [SECURITY.md](SECURITY.md) 私密通道，勿公开 Issue。

## ⚖️ 许可

[MIT License](LICENSE)。第三方组件：Kali 底座（MIT）/ sqlmap（GPL-2.0，vendored 独立程序）/ projectdiscovery 工具链（MIT）/ Playwright（Apache-2.0）/ Vue/Vite 及 npm 依赖（各自上游）——详见 [docs/FEATURES.md](docs/FEATURES.md) 与各上游声明，商用分发请逐一核对。
