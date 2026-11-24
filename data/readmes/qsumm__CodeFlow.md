<div align="center">

# CodeFlow

**AI 需求交付平台:需求进,交付出。**

AI 数字员工按交付流程完成分析/开发/测试/验证/交接,全过程留痕可回看。

[![License](https://img.shields.io/badge/License-GPL--3.0-blue)](LICENSE)
[![Java](https://img.shields.io/badge/Java-21-orange)](https://spring.io/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.3-green)](https://spring.io/)
[![Docker](https://img.shields.io/badge/Docker-Compose%20v2-2496ED)](platform/docker-compose.yml)

**开源自托管的 AI 需求交付平台**

<img src="assets/wechat-qrcode.jpg" width="120" alt="公众号「一鸣AI编程」">

**公众号「一鸣AI编程」**——从第一行代码到交付引擎的完整过程都在连载。觉得不错的话，欢迎点个 ⭐ Star 支持一下。

</div>

<div align="center">

### 它是怎么工作的

</div>

![架构一屏](assets/architecture.png)

浏览器里写需求 → AI 数字员工先反问澄清，再按四步交付流程干完开发、测试、验证 → 干活的节点装在你自己的机器上（主动回连，零入站端口）→ 交付结论自动写回禅道 / TAPD。**每一步留痕，验收权在人。**

---

## ⚡ 30 秒跑起来

```bash
git clone https://github.com/qsumm/CodeFlow.git && cd CodeFlow/platform
./deploy.sh up        # 生成密钥 → 构建 → 启动 → 等就绪（首次 5~10 分钟）
```

打开 `http://localhost:7001/register` 注册首个用户 = **平台管理员**。国内 clone 慢用镜像：

```bash
git clone https://gh-proxy.com/https://github.com/qsumm/CodeFlow.git
```

## 📊 真实交付实测

| | |
|---|---|
| **20~50 分钟** | 单条需求全自动交付耗时 |
| **19 个** | AI 澄清真实反问的问题数 |
| **8 个** | 一次交付自动归档的产物 |
| **0 个** | 需要开放的入站端口 |

以上数字来自真实交付环境（含完整审计日志），不是设计目标值。

## 🧩 它能干什么

- **需求澄清** — AI 先反问 19 问，结论落成 spec/plan 落档，确认了才开工
- **交付流程** — 四步模板 + 完成门：不达标停在当前步，说明原因
- **运行节点** — 主动回连领任务，代码在内网照样干活；6 种 CLI（Claude Code / Codex / Cursor / Gemini / Qoder）
- **结论回写** — 交付备注自动写回禅道 / TAPD；只写结论，不代改状态
- **过程留痕** — 失败按指数退避排队重试，前几轮记录一条不少；产物随交付归档
- **交付度量** — 周期 / 一次通过率 / Token 消耗 / 操作审计，全部在平台内

![交付进度跟踪](assets/41-workitem-delivery-tracking.png)

## 🎯 六个核心设计

| 设计 | 一句话 |
|---|---|
| 澄清前置 | 验收标准先写成可执行检查项，开工前把"没说清"问出来 |
| 完成门卡步 | 每步达标才往下走，不达标停下并说明原因 |
| 执行器主动回连 | 防火墙后、NAT 后、云安全组零改动 |
| 失败留痕可重试 | 派发独立编号，前几轮记录全保留 |
| 产物随交付归档 | 过程文档、脚本、报告入库，可下载可预览 |
| 验收结论由人给 | 只回写结论，不代改外部单据状态 |

## 🆚 和编排工具的区别

Paseo / Conductor 这类工具管理**你正在跑的 Agent 会话**；CodeFlow 管理**一条需求从说不清到验收完**的全过程。Paseo 列基于 2026-11 源码比对。

| 能力 | CodeFlow | Paseo | 直接用 Claude Code |
|---|---|---|---|
| 澄清对话 → spec/plan | ✅ | ❌ | ❌ |
| 交付流程 + 完成门 | ✅ | ❌ | ❌ |
| 禅道 / TAPD 双向同步 | ✅ | ❌ | ❌ |
| 交付度量 + 操作审计 | ✅ | ◐ | ❌ |
| MCP Server（外部 Agent 操作平台） | ✅ 19 工具 | ✅ | ❌ |
| 移动端接管 | ❌ 路线图 | ✅ | ❌ |
| Git worktree 隔离 | ❌ 路线图 | ✅ | ❌ |

## 🔌 接入执行器（真正干活的节点，可与平台同机）

```bash
pip install -e .
python scripts/register_executor.py --agent-id <数字员工ID> --workspace-id <工作空间ID> \
  --out runtime.env --provider claude
export AINATIVE_AGENT_CMD=claude
python -m runtime.daemon        # 常驻等待派发
```

模型任意 Anthropic 兼容端点（Claude / MiniMax / GLM / DeepSeek…），改执行器 env 三个变量即换，平台不绑定。

<details>
<summary><b>📦 部署前置条件</b></summary>

| 项 | 要求 | 说明 |
|---|---|---|
| Docker + Compose | Docker 20.10+，compose v2 | `docker compose version` |
| 内存 | 建议 ≥ 4GB | SeekDB 要求可用内存 ≥ 2GB，不足时直接退出（不报错） |
| 磁盘 | ≥ 10GB 空闲 | 镜像与依赖缓存 |
| 端口 | 7001 / 33060 | `APP_PORT=8080 ./deploy.sh up` 可覆盖 |

</details>

<details>
<summary><b>❓ 常见问题</b></summary>

| 现象 | 解法 |
|---|---|
| 数据库反复 Restarting，日志只有 `exited unexpectedly` | 资源不足：SeekDB 不报错直接退出。核对磁盘空闲 / 可用内存 ≥ 2GB / 停同机其它数据库 |
| git clone 超时 | 用上方 gh-proxy 镜像 |
| 端口被占用 | `APP_PORT=8080 ./deploy.sh up` |
| 派发停在"排队中" | 「等待运行节点上线」= 执行器没连上；「容量已满」= 等空闲。上线后自动唤醒 |
| 交付失败先看哪 | 交付进度 → 失败派发 → 查看执行：通常是模型端点、仓库权限、完成门未达标 |
| 禅道状态没变 | 设计如此：只回写结论，不代改状态 |
| 换环境后绑定失效 | `AINATIVE_SECRET_MASTER_KEY` 变了；恢复原密钥或重新保存绑定 |
| 想换模型 | 改执行器 env 三个变量后重启 daemon |

</details>

## 🔒 安全

- 外部凭据 AES 加密存库，接口只返回掩码
- MCP 令牌只展示一次，列表仅前缀不可反查
- 全量操作审计，可按操作人 / 类型筛选
- 漏洞走 GitHub Security Advisories 私下报告

## 🤝 贡献

① 开 Issue（真实日志 + 复现步骤）→ ② `fix/<issue号>-<短描述>` 分支 → ③ PR（`Closes #N`）→ ④ 合并。

```bash
cd platform/ainative/server-v2 && scripts/run-tests.sh    # 53 用例，宿主无需装 Maven
```

## 📄 License

[GPL-3.0](LICENSE)。第三方依赖归属见 [NOTICE](NOTICE)。

## ✍️ 作者

**一鸣** · 公众号「一鸣AI编程」——从第一行代码到交付引擎的完整过程都在公众号连载。

官网：**[codeflow.com.cn](https://www.codeflow.com.cn)**

<div align="center">

<img src="assets/wechat-qrcode.jpg" width="200" alt="公众号「一鸣AI编程」">

**微信扫码关注「一鸣AI编程」** · 回复 `codeflow` 进 **CodeFlow 专属技术答疑群**，拿手册、部署包与演示环境

</div>
