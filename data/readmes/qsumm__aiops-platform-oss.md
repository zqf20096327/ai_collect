<div align="center">

# AI 运维监控平台

**告警响了，AI 已经查完，证据链摆在你面前。**

[![License](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](deploy/docker-compose.yaml)
[![Release](https://img.shields.io/badge/release-v1.7.1-success.svg)]()

*中小团队的 AI 值班运维 —— 告警有人盯、原因有人查、处置有人批。*

![总览大盘](docs/screenshots/tutorials/02-dashboard.png)

</div>

---

## 为什么是它

你有没有过这种凌晨：告警响了，你 SSH 上去翻日志、看进程、猜原因，半小时后发现自己重启了一个根本没坏的服务。

这个平台把那段流程交给 AI——但**不是**让 AI 直接上生产机乱动。它的哲学写在代码里：

> 恢复能力的难点不在"执行"，而在"**敢于不执行**"。

## 一屏看全

| 场景 | 你能用到 |
|---|---|
| 监控 | Agent 拉取式接入（主机 0 入站端口）· 探活四件套（TCP/HTTP/进程/证书）· 多维指标即时查询 · Prometheus 数据源 |
| 告警 | 阈值 / 3σ / 孤立森林 · 指纹去重收敛 · 静默策略链 · 多渠道通知（邮件 / Webhook / **电话语音播报**） |
| 诊断 | ReAct 最多 30 步全留痕 · 技能自动路由 · 向量案例召回 · 置信度三档（查不出也是合法结论） |
| 处置 | 九条护栏准入 · 4 个白名单动作 · 建议 / 人工确认 / 自动三档执行 · 变更单版本化 |
| 运维 | 定时巡检健康日报 · 巡检异常自动建事件 · 通知路由 Pipeline · MCP 接入 |

## 六个核心设计

| | 设计 | 一句话 |
|---|---|---|
| <img src="docs/images/icons/search.svg" width="20" align="top"/> | **AI 诊断带证据链** | 最多 30 步，每步思考/工具调用/返回全留痕；结论必须引用证据——查不出也是合法结论 |
| <img src="docs/images/icons/shield.svg" width="20" align="top"/> | **九条护栏准入判决** | 动作白名单（没有自由文本命令）、限流、熔断、发布窗口互斥、上游异常拒自愈……任何一条不过就不许动 |
| <img src="docs/images/icons/route.svg" width="20" align="top"/> | **拉取式通道穿透 NAT** | Agent 从主机**主动出站**拉任务，主机不开任何入站端口——防火墙后、NAT 后、云安全组零改动 |
| <img src="docs/images/icons/layers.svg" width="20" align="top"/> | **诊断技能可插拔** | 技能就是一个 SKILL.md 文件——告警命中自动装载，Agent 只执行技能预授权的只读命令；GitHub 一键导入，命中与采用次数可查 |
| <img src="docs/images/icons/database.svg" width="20" align="top"/> | **案例库越用越聪明** | 每次诊断沉淀为向量案例，下次同类故障 AI 直接召回"上次怎么修的" |
| <img src="docs/images/icons/zap.svg" width="20" align="top"/> | **5 分钟部署** | 一条 compose 命令，向量检索内置在数据库里，不额外装 Milvus/Pinecone |

## 它做什么 / 不做什么

**做**：主机与服务监控、主动告警（多渠道通知 + 电话语音播报）、AI 根因诊断（带证据链）、诊断技能自动路由（Agent 只读授权命令）、白名单内处置动作（重启/重连/轮转日志）、定时巡检、多维指标即时查询、案例沉淀。

**不做**：替代你的 Prometheus（坐在它后面）、无人值守自治（三档执行模式默认人工确认）、执行白名单外的任何命令（AI 提议 `rm -rf` 在第一层护栏就被拦下）。

## 5 分钟跑起来

```bash
git clone https://github.com/qsumm/aiops-platform-oss.git && cd aiops-platform-oss
cp backend/.env.example .env   # 把 JWT_SECRET / KEY_STORE_SECRET / DB_PASSWORD 换成随机值！
docker compose --env-file .env -f deploy/docker-compose.yaml up -d --build
```

> 首次构建约 3~6 分钟（pip 走阿里云镜像、基础镜像走国内源 `docker.m.daocloud.io`，无需手动拉取）；之后有构建缓存，秒级启动。

打开 `http://localhost:8848`，用**首次启动时系统创建并打印在启动日志里的管理员账号**登录（日志有 warning 提示），登录后第一件事：修改默认口令。
想看它真的干活：`bash deploy/faults/cpu_spike.sh` 触发一次真实 CPU 飙升告警，看着 AI 诊断从取证到结论走完闭环。

> 全部功能与操作说明（含真实截图）：**[用户手册](docs/04-交付与运营/用户手册.md)**。

## 架构一屏

![系统架构图](docs/images/architecture.svg)

**诊断闭环**（点对点全程留痕，每步可回放）：

![诊断闭环流程图](docs/images/diag-loop.svg)

## 文档地图

| 你想 | 去 |
|---|---|
| 全部功能与操作说明（含 33 张真实截图：接入 / 告警 / 诊断 / 处置 / 技能 / 设置） | [docs/04-交付与运营/用户手册.md](docs/04-交付与运营/用户手册.md) |
| 学 SRE / AI 运维（不部署也能学） | [learning/](learning/) |

## 与开源同类工具对比

| # | 核心功能 | **TestOPS（本平台）** | 夜莺 Nightingale | Keep | k8sgpt | HolmesGPT |
|---|---|---|---|---|---|---|
| 1 | Agent 一体化采集（指标+探活+断网续传） | ✅ 拉取式，0 入站端口 | ✅ Categraf（推模式） | ❌ | ❌ | ❌ |
| 2 | 告警引擎（指纹去重 + 静默策略链 + 生效时段） | ✅ | ✅ 强项 | ◐ 告警聚合降噪 | ❌ | ❌ |
| 3 | 分级通知 + 电话语音播报 + 通知路由 | ✅ 含电话实测 | ◐ 渠道多 | ✅ 100+ 集成/路由强项 | ❌ | ❌ |
| 4 | 两级收敛成事件（LLM 因果判定合并） | ✅ | ◐ 屏蔽/分发 | ✅ AI 告警关联强项 | ❌ | ◐ 分析单条告警 |
| 5 | AI 根因诊断（ReAct 证据链留痕 + 技能自动路由） | ✅ | ◐ 有 AI 摘要（源码核实），根因分析经生态方案 | ◐ AI 富化/摘要 | ✅ 限 K8s 对象 | ✅ 强项 |
| 6 | 修复建议先验证（VALIDATED FIXES，没验证不建议） | ✅ | ❌ | ◐ 工作流可自编排验证 | ◐ 给建议，非内置强制 | ◐ 迭代取证后建议，非强制规范 |
| 7 | 白名单处置 + 九条护栏 + 三档执行 | ✅ 一次性审批 | ◐ 自愈执行脚本，无护栏准入层 | ◐ 工作流自动化，无护栏概念 | ◐ K8s 资源层自动修复 | ❌ |
| 8 | 案例库向量召回（"上次怎么修的"自动注入） | ✅ 内置向量检索 | ❌ | ❌ | ❌ | ◐ 商业版有历史沉淀 |
| 9 | 定时巡检 + 健康日报 + 异常自动建事件 | ✅ | ❌ | ◐ 可经工作流拼装 | ❌ | ❌ |
| 10 | 服务级监控 + 日志取证（按告警锚定时间窗回拉相关片段） | ✅ | ◐ 有日志类数据源接入 | ❌ | ❌ | ◐ 可查日志数据源 |
| 11 | K8s in-cluster 深度支持（operator / 自动修复 / 自定义 analyzer） | ❌ | ◐ 云原生集成 | ◐ | ✅ | ✅ |
| 12 | 声明式自动化工作流（YAML 任意编排告警处置） | ◐ 白名单 4 动作 + 自愈策略，无通用编排 | ◐ 脚本自愈 | ✅ 强项 | ◐ | ◐ 结构化 runbook |
| 13 | 事件管理全流程（on-call 排班 / 升级策略 / 工单联动） | ❌ | ◐ | ✅ 强项 | ❌ | ❌ |

**出处**：[K8sGPT](https://k8sgpt.ai) · [HolmesGPT / CNCF](https://www.cncf.io/blog/2026/01/07/holmesgpt-agentic-troubleshooting-built-for-the-cloud-native-era) · [Keep](https://www.keephq.dev) · [夜莺官方](https://n9e.github.io/zh) · [快猫星云案例](https://flashcat.cloud/blog/nightingale-usecase-qingshangongye)

## 安全

- 大模型 key **AES-GCM 加密落库**，接口只返回尾号
- 处置动作**白名单枚举**（4 个），每个动作强制声明后置校验
- 全 API 经过五向量攻击矩阵自测（未认证/越权/路径变异/参数变异/请求体变异），工具开源在 `tools/attack_matrix.py`
- 漏洞报告：通过 GitHub 安全通告（Security Advisories）提交。

## License

[AGPL-3.0](LICENSE)。商业授权与增值能力请通过仓库主页联系方式洽谈。

---

<div align="center">

## 作者

**一鸣** · 公众号「**一鸣AI编程**」

*这个平台从第一行代码到 AI 诊断引擎的完整过程——每一次设计取舍、每一个踩过的坑——都在公众号里连载。*

<img src="docs/images/qrcode-yiming-ai.jpg" width="220" alt="公众号：一鸣AI编程"/>

**扫码关注「一鸣AI编程」**：线上故障复盘 / AI 编程实战 / 这个平台的全过程，更新不迷路。
觉得有用的话，给仓库点个 **Star ⭐**，就是最好的支持。

</div>
