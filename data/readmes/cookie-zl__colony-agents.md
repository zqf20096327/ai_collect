<div align="center">

# Colony Agents

**把 dsh 部署到云上，做成团队共用的 Agent 基础设施**

一套镜像起一个团队实例：租户隔离、账号准入、闲置休眠、会话不丢；
技能与 MCP 走市场，带版本、按团队分发；
网页里能对话，钉钉 / 飞书群里能 `@`，还能按岗位配成数字员工。

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/cookie-zl/colony-agents?color=blue)](https://github.com/cookie-zl/colony-agents/releases)
[![Node](https://img.shields.io/badge/node-%E2%89%A522-3c873a.svg)](https://nodejs.org)
[![Docker](https://img.shields.io/badge/docker-compose%20%7C%20helm-2496ed.svg)](deploy/)
[![Self-hosted](https://img.shields.io/badge/self--hosted-yes-111.svg)](#快速开始)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

![主界面：和 Agent 对话，带思考过程、token 用量和完整会话历史](docs/images/hero.png)

---

## 这是什么

一句话：**把 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（下称 dsh）部署到云上，做成一套多租户的 Agent 基础设施——团队共用、能力可装、群里可用。**

它同时是四件事，少一件就不像一个能交给公司用的平台：

| 维度 | 具体是什么 |
| --- | --- |
| **云上部署** | 一套镜像 + 一份 profile：`make up` 起单机，Helm 上 K8s。一个团队一个实例，不是「一个进程里塞多个团队」 |
| **团队与租户** | 账号、角色、准入、审计；卷 / 子域 / 数据 / 密钥全隔离，配额与休眠按团队算 |
| **能力分发** | 技能与 MCP 进市场，带版本与安装台账，按团队分发，支持点对点分享 |
| **使用入口** | 网页对话、钉钉 Stream / 飞书回调；同一个会话，还能按岗位配多个数字员工 |

dsh 本身是单人视角的：一个进程、一份会话、一个 `$DSH_HOME`。一个人用很顺手，
交给一个团队就会撞墙——谁都能进、会话互相污染、能力散落在各自机器上、机器不敢重启。
本项目补的就是它外面那一层。

它不重写 Agent，也不做新的聊天前端。它是 Agent 的**物业**——门禁、水电、保洁、消防。

---

## 具体解决的三个问题

### 一、团队要共用 Agent，但租户之间必须互不可见

**现实**：研发想让 Agent 查日志、改配置、跑脚本，但不能让 A 组看到 B 组的会话和产物；
也不能给每人发一台机器、每人维护一份配置。

**做法**：一个团队 = 一个实例 = 一套卷。不是「同一个实例里加个 `team_id` 字段」，
而是从进程、文件系统、入口域名到数据库行全部切开：

| 隔离维度 | 粒度 |
| --- | --- |
| 运行时 | 一个 compose 项目（`dsh-<team>`）/ 一个 Helm release，一个团队一个容器 |
| 文件 | 独立命名卷，团队回收即删，不与其他团队共享任何路径 |
| 会话与产物 | 独立 `$DSH_HOME` + 独立对象层，侧栏里只看得到自己的会话 |
| 网页入口 | 独立子域（如 `team-a.localhost:8080`），登录态与 dsh token 一团队一份 |
| 数据 | 事实库按 `team_id` 分区：成员、技能台账、密钥、消息流水、审计 |
| 密钥 | 模型 Key 信封加密入库，容器只拿可吊销的短令牌，看不到明文（[docs/18](docs/18-密钥网关.md)） |
| 算力 | 闲置 30 分钟自动停、访问自动拉起（实测唤醒到健康 5.8 秒，用户 2~4 秒看到页面，[docs/09](docs/09-休眠与唤醒.md)） |

这一层还包括「谁能进」：账号服务管登录、改密、团队角色、加入团队、跨团队票据，
每一次进出都记审计。dsh 自己的 token 关在反向代理后面，外部拿不到
（[docs/07](docs/07-多团队账号.md)、[docs/06](docs/06-访问控制.md)）。

建团队也是一个按钮的事：门户点一下 → 控制面分配端口、建卷、起容器、写配置，
配额不够就拒绝，起不来就回滚（[docs/08](docs/08-动态建团队.md)）。

### 二、能力要变成可分发、可版本化的资产（Skill / MCP + 市场）

**现实**：每个团队各写一份提示词、各自配一遍连接器；改一次要挨个通知，
谁装了什么版本没人知道；token 散落在各自的配置文件里，人一走就断。

**做法**：把能力做成带版本的「包」进市场，凭据在安装时填、落团队自己的卷——
版本、台账、分发三件事一起解决。

| 能力 | 说明 |
| --- | --- |
| 两类包 | `skill`（提示词 / 工作流程）、`mcp`（连接器：GitHub、文件系统……），同一套索引与安装流程 |
| 版本 | 每个包带 `version`；安装台账记录「装了哪一版、谁装的、从哪个团队来的」。索引里一个包名只保留当前版本，发布新版本即替换，所以升级路径是「重装」而不是「在多版本里挑」 |
| 升级 | 重装同名包会**替换**配置里的标记块而不是叠加（叠加会出现「升级了却还跑旧版」，极难查），写完用 `dsh --dump-config` 校验，不通过自动回滚 |
| 分发 | 三种可见性：公共（全员可装）、团队私有、**点对点分享**（对方可以接收或拒收） |
| 凭据 | MCP 需要的 env（如 `GITHUB_TOKEN`）在安装时填，落进**团队自己的卷**，不进控制面日志 |
| 隔离 | 每个团队一份台账，卸载只影响自己；市场里的私有包别的团队看不到 |
| 真相在库里 | 技能不从磁盘读：`@colony-agents/dsh-market-skill` 运行时向控制面拉，多文件包按 `<name>@<version>-<digest>` 物化并按 digest 判重——所以「门户里停用了但容器里还生效」这种两套事实不会发生 |

安装、启停、卸载都在侧栏「市场」面板里，改完不需要重启容器；
连接器写配置失败会回滚，团队实例不受影响（[docs/11](docs/11-技能与连接器.md)）。

### 三、数字员工要进群，而且一个团队可以有多个

**现实**：群里问「昨天那个报表怎么样」，得有人复制到网页里再贴回来；
问了半天没动静，也不知道是在跑、挂了、还是压根没收到。

**做法**：每个数字员工 = 一个机器人 + 一套人设；群里 `@` 它，回复回到那个群，
**一个群一条对话**——同一个机器人在 A 群聊过的内容不会串到 B 群。

| 能力 | 说明 |
| --- | --- |
| 多个数字员工 | 一个团队可以建多个助理，各绑各的机器人（钉钉 AppKey / 飞书 App ID），人设、会话、流水彼此独立 |
| 一群一对话 | 对话的唯一键是「机器人 + 群」。机器人在哪个群被 @，就续哪条会话；群与群之间上下文完全隔离 |
| 只接某些群 | 可以给助理配群白名单，只处理列出来的群；不配就接它被拉进的所有群 |
| 专属提示词 | 每个助理自带 `system_prompt`，首轮注入建立口径，后续靠会话上下文延续（不污染每条消息） |
| 入站免公网 | 钉钉走 **Stream 长连接**：内网机器主动外连，不用公网 IP、不用内网穿透；飞书走 HTTP 回调 |
| 出站不靠临时地址 | 换 `access_token` 走 OpenAPI 主动发送，不受 `sessionWebhook`（约 1.5 小时）限制，长任务也能回 |
| 不重复、不沉默 | `msgId` 幂等去重；同一助理串行、全局并发 2；失败或超时会在群里回一句，而不是让人对着空气等 |
| 可查、可追 | 每轮落流水（提问、思考过程、回复、token 用量、耗时），助理会话以普通会话出现在侧栏「代理工作区」，点开就是完整对话 |

一条真实链路（真机验证过，不是设计稿）：

```
群里 @机器人
  → 钉钉经 Stream 长连接推一帧事件（不需要公网回调）
  → 控制面归一化 → 消息流水落库（msgId 去重）
  → docker exec dsh --profile headless（session 固定在该助理上，多轮续聊）
  → OpenAPI 主动发送回原群（不依赖 1.5 小时就过期的 sessionWebhook）
```

### 合起来看：数字员工的日常

| 日常问题 | 谁在问 | 靠什么 |
| --- | --- | --- |
| 群里问「上周留存多少」「这个口径对吗」 | 运营 / 产品 | 技能（口径与 SQL 规范）+ MCP（数据库 / BI） |
| 让它翻仓库、读 issue、提 PR | 研发 | MCP（GitHub）+ 工作区里的代码 |
| 按既有流程改配置、跑脚本、看日志 | 运维 | Agent 自带的文件与命令能力，权限边界在卷与准入层 |
| 按模板整理成文、核对数据 | 全员 | 技能（模板与检查项） |

这些能力都不是内置写死的：**装了什么技能与 MCP，数字员工就会什么**——所以第二节的市场不是附加功能，
而是决定它能干什么的那一层。网页和群里是同一个会话，问过一次的事换个入口不用重讲。

### 三条横切的能力

上面三件事都建立在同一套底座上，它们不是「顺便做的」：

- **会话不会丢**：会话与归档进对象层（内容寻址），容器是可丢的缓存，
  `docker rm` 之后重建，会话、产物、token 用量都还在（[docs/14](docs/14-对象层.md)、[docs/15](docs/15-会话存算分离.md)）。
- **改了什么都查得到**：`changes-collector` 每轮记下改了哪些文件、产出在哪（[docs/20](docs/20-产物归因与配置热生效.md)）；
  平台侧有访问审计与操作日志。
- **能力以插件形态进入**：6 个自研插件都是纯 ESM、零第三方依赖、无构建步骤的进程内 bundle，
  改完 `make reload` 十秒生效。装社区插件等于让作者在你服务器上跑代码，所以 `plugins.txt` 逐行锁版本并过审
  （[docs/03](docs/03-社区插件.md)）。

---

## 能力一览

| 能力 | 一句话 | 入口 |
| --- | --- | --- |
| **多团队、一团队一实例** | 一个 compose 项目 / Helm release 一个团队，主机名、端口、卷、入口全独立 | `deploy/compose/team-up.sh`·[docs/07](docs/07-多团队账号.md) |
| **账号与准入** | 登录、改密、团队角色、加入团队、跨团队票据、访问审计 | `deploy/auth/`·[docs/07](docs/07-多团队账号.md) |
| **控制面** | 点一下门户按钮 = 建一个容器；配额校验、失败回滚、容器对账 | `deploy/orchestrator/console.mjs`·[docs/08](docs/08-动态建团队.md) |
| **休眠与唤醒** | 四条判据判断闲置，访问即拉起，唤醒态对用户透明 | `runtime.mjs`·[docs/09](docs/09-休眠与唤醒.md) |
| **技能 / MCP 市场** | 两类包 + 索引 + 安装台账；版本、升级校验回滚、公共 / 团队私有 / 点对点分享 | `deploy/market/`·[docs/11](docs/11-技能与连接器.md) |
| **IM 数字员工** | 钉钉 / 飞书 `@` 机器人 → 同一个 Agent 会话 → 回原群；一个团队可建多个，各带人设，可绑定指定群 | `assistants.mjs`·[docs/features/11](docs/features/11-助理与消息机器人.md) |
| **密钥网关** | 模型 Key 信封加密进库，容器只拿可吊销的短令牌，不落明文 | `llm-gateway.mjs`·[docs/18](docs/18-密钥网关.md) |
| **会话存算分离** | 会话与归档进对象层（内容寻址），容器是可丢的缓存 | `objects.mjs`·[docs/14](docs/14-对象层.md)·[docs/15](docs/15-会话存算分离.md) |
| **产物归因** | 每轮对话改了哪些文件、产出在哪，可查可追 | `changes-collector`·[docs/20](docs/20-产物归因与配置热生效.md) |
| **可观测** | `/metrics` 暴露团队数、唤醒时长、配额占用，直接喂 Prometheus | `metrics.mjs`·[docs/10](docs/10-平台运维.md) |

自研插件 6 个，全部纯 ESM、无构建步骤：`dsh-workspace-guard`、`dsh-changes-collector`、
`dsh-market-skill`、`dsh-client-ui-market`、`dsh-client-ui-assistants`、`dsh-hello`（样板）。

### 群里的样子

![助理面板：钉钉 / 飞书一键接入、回调地址、机器人列表与沟通记录](docs/images/assistants.png)

细节、失败兜底、踩过的坑：[docs/features/11](docs/features/11-助理与消息机器人.md)。

---

## 快速开始

需要 Docker（macOS / Linux 都行），以及 `make`。

```bash
git clone https://github.com/cookie-zl/colony-agents.git && cd colony-agents

make seed      # 生成 accounts.json / nodes.json / .env（演示账号 alice / bob / carol / dave，口令 dsh-demo-1234）
make up        # 构建镜像并起 team-a → http://team-a.localhost:8080/
```

首次构建要装依赖，几分钟；之后改插件 `make reload`，约 10 秒替换容器。

> **模型 Key 可以留空**：默认走免费模型车道。要接自己的模型，用团队级密钥
> `make team-key TEAM=team-a KEY=sk-xxx`——Key 会加密进库，容器里看不到明文。

`make help` 有全部目标。跑完想拆：`make down`（`make clean` 连数据卷一起删）。

### 目录结构

```
plugins.txt                 # 要装进镜像的社区插件清单（锁版本）
profile/                    # dsh profile：配置即代码
plugins/                    # 6 个自研插件（npm 包形态的 bundle）
deploy/
  image/                    # Dockerfile + entrypoint + 运行期 patch
  compose/                  # 单机 / 本地跑法（Caddy 入口 + team-up.sh）
  auth/                     # 账号服务：登录、门户、成员、审计（零依赖 Node）
  orchestrator/             # 控制面：建团队、休眠唤醒、对账、助理、市场、指标
  market/                   # 技能与连接器市场的包与索引
  helm/colony/              # K8s
docs/                       # 20 篇设计记录 + 11 篇功能清单
```

---

## 两个仓库

| 仓库 | 放什么 | 给谁用 |
| --- | --- | --- |
| **本仓**（平台） | 镜像、profile、控制面、账号服务、助理、市场，**外加 6 个自研插件** | 想「一条命令把团队版 Agent 跑起来」 |
| [colony-dsh-plugins](https://github.com/cookie-zl/colony-dsh-plugins) | 只有那 6 个插件包 | 已经有 dsh，只想装 `workspace-guard` / `changes-collector` |

依赖是单向的：**插件仓不需要知道平台存在**，`dsh plugin add <目录>` 就能用；
插件仍然在本仓开发和验证（行为测试要 dsh 容器与数据库夹具），
用 `make mirror-plugins` 导出到插件仓，`make mirror-check` 在 CI 里防漂移。

不用 git submodule 是刻意的：私有仓的 submodule 要额外配凭据，`git clone` 忘了 `--recurse-submodules`
就构建失败——这是开源项目最常见的劝退点。

---

## 架构

```mermaid
flowchart TB
  B[浏览器] -->|Cookie / 登录| EDGE[Caddy 入口<br/>登录态 → 团队成员 → dsh token]
  G[钉钉 / 飞书群] -->|@机器人| STREAM[Stream 长连接<br/>或 HTTP 回调]

  EDGE --> AUTH[账号服务<br/>登录·团队·审计]
  EDGE -->|反代| DSH[团队实例<br/>dsh + 插件]

  STREAM --> CONSOLE[控制面<br/>建团队·配额·休眠唤醒·助理调度·市场]
  CONSOLE -->|docker / k8s| DSH

  AUTH --> DB[(事实库<br/>团队·技能·密钥·流水)]
  CONSOLE --> DB
  DSH --> OBJ[(对象层<br/>会话·归档·产物)]
  DSH -.->|/metrics| PROM[Prometheus]
```

三层配置，改哪一层是明确的：**镜像**（工具链与版本）→ **profile**（装哪些插件）→ **cordis.patch**（用户覆盖层）。

---

## 和同类不是一层的东西

| 项目 | 它解决什么 | 和 Colony Agents 的关系 |
| --- | --- | --- |
| [Open WebUI](https://github.com/open-webui/open-webui) / [LibreChat](https://github.com/danny-avila/LibreChat) | 多模型聊天前端 | 它们替代 **UI**；本项目默认用 dsh 自己的 UI，重心在运营层 |
| [Dify](https://github.com/langgenius/dify) / [n8n](https://github.com/n8n-io/n8n) | 编排工作流、搭 AI 应用 | 它们产出的应用可以被本平台的 Agent 当技能 / MCP 连接器调用 |
| [Coder](https://github.com/coder/coder) / [code-server](https://github.com/coder/code-server) | 给每人一套云端 IDE | 形态最接近：同样是「一用户一实例 + 休眠 + 反代」，但对象是 IDE 而不是 Agent |
| 直接跑 DeepSeek Harness | 单人用 Agent | 本项目在它之上补租户、能力分发、IM 入口、持久化与运维 |

---

## 说清楚边界

开源项目最容易骗人的地方，是把「做了一半」写成「支持」。这里反过来：

1. **单实例有状态。** dsh 把会话放进程内存 + `$DSH_HOME`，所以 `replicas` 只能是 1，PVC 必须 `ReadWriteOnce`，升级只能 `Recreate`。要扩容就加实例，不要加副本。
2. **插件是进程内代码，不是沙箱。** `apply(ctx)` 跑在 dsh 主进程里，权限等于 dsh 本身。装社区插件 = 允许作者在你服务器上执行代码，所以 `plugins.txt` 每行都锁到确切版本并过审。
3. **鉴权只有一层，且在 dsh 之外。** dsh 用「URL 里的 token → 签名 Cookie」认人。所以「只允许自己人用」必须在反代 / 网关上做（IP 白名单、Basic Auth 或公司 SSO），见 [docs/06](docs/06-访问控制.md)。
4. **平台状态：生产自用，不是 1.0。** 单人维护，接口会变；钉钉链路真机验证过，飞书走 HTTP 回调、需要公网可达，Stream 版还没做。
5. **只处理 `@` 的消息。** 全量群消息是敏感权限，钉钉 / 飞书默认都只推 `@`。
6. **一个机器人只能对应一个数字员工。** 表上有 `UNIQUE(platform, robot_key)`：同一个 AppKey / AppID 不能同时派生两个助理。想要多个角色就多建几个应用——好处是权限、人设天然隔离，代价是机器人数量等于数字员工数量。
7. **群内上下文按群隔离。** 一个机器人 × 一个群 = 一条 `session_id`。同一个群里的追问续同一条会话，换个群就是新会话；机器人被拉进 20 个群，就是 20 条会话。并发也按群算，`DEFAULT_CONCURRENCY` 是「同时跑几个群」而不是「几个机器人」，2 GiB 容器上 2~3 比较稳。

---

## 文档

设计记录写「为什么这么选、踩过什么坑」，功能清单写「做到什么程度、落在哪个文件、有没有验证过」。

**上手**

| 文档 | 内容 |
| --- | --- |
| [01 · 本地运行](docs/01-本地运行.md) | compose 起服务、Caddy 入口、常见启动失败 |
| [02 · 插件开发](docs/02-插件开发.md) | 插件形态、开发循环、工具 / 命令 / 配置 |
| [04 · 镜像与 profile](docs/04-镜像与profile.md) | 镜像分层、seed 策略、升级插件不丢会话 |

**运营**

| 文档 | 内容 |
| --- | --- |
| [06 · 访问控制](docs/06-访问控制.md) | 白名单、Basic Auth、SSO 网关、多实例方案 |
| [07 · 多团队与账号](docs/07-多团队账号.md) | 一团队一实例、加入团队、token 接缝 |
| [08 · 动态建团队](docs/08-动态建团队.md) | 点按钮 = 建容器：控制面、端口分配、失败回滚 |
| [09 · 休眠与唤醒](docs/09-休眠与唤醒.md) | 闲置停实例、访问拉起来、四条判据、实测延迟 |
| [10 · 平台运维](docs/10-平台运维.md) | 配额、对账、归档备份、审计、指标 |

**深水区**

| 文档 | 内容 |
| --- | --- |
| [11 · 技能与连接器](docs/11-技能与连接器.md) | 凭据落点、市场、发布 / 安装 / 分享 / 版本 |
| [14 · 对象层](docs/14-对象层.md) · [15 · 会话存算分离](docs/15-会话存算分离.md) | 内容寻址、容器变成可丢缓存 |
| [18 · 密钥网关](docs/18-密钥网关.md) | 信封加密、容器只拿短令牌 |
| [20 · 产物归因](docs/20-产物归因与配置热生效.md) | 每轮改了哪些文件、配置怎么热生效 |

全量索引（含功能清单 11 篇）：[docs/features/README.md](docs/features/README.md)。
还没做的、以及**明确不做**的：[docs/ROADMAP.md](docs/ROADMAP.md)——按「不做会不会出事」排序，每条写清现状与目标。

---

## 开发

没有构建步骤：插件是纯 ESM，改完 `make reload` 就生效。自测是离线脚本，不联网、不依赖 docker、不碰生产库：

```bash
make verify-all             # 15 个脚本一把跑（CI 跑的就是这个）
make verify-assistants      # 助理调度：路由、幂等、失败兜底、思考过程落库（79 条）
make verify-stream          # 钉钉 Stream：建连、探活、换票、去重（46 条）
make verify-workspace-guard # 工作区落点与补登记（20 条）

make mirror-plugins         # 把 plugins/ 导出到插件仓
make mirror-check           # 只比对，不改文件（CI 用）
```

CI 会在每个 PR 上跑全部自测 + 语法检查 + 密钥扫描，见 [.github/workflows/ci.yml](.github/workflows/ci.yml)。

想加一个插件？从 `plugins/hello-dsh` 抄骨架；想加一个 IM 平台（比如 Slack），
改 `assistant-channels.mjs` 的归一化 + `ASSISTANT_PLATFORMS` 一张表，前端不用动。

---

## 参与

- 提交前请读 [CONTRIBUTING.md](CONTRIBUTING.md)（分支、提交信息、自测要求）
- 安全问题请走私信，不要开 issue：[SECURITY.md](SECURITY.md)
- 行为准则：[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## 名字

`Colony Agents`：一个巢（一套部署），一群个体（Agent / 数字员工），各司其职。
一个公司一个巢，巢里住着网页里的对话、群里的数字员工，能力靠市场装着。

名字带复数后缀是有依据的：`colony` 在 GitHub 上有 8,054 个同名仓库，还撞了一家同名的区块链公司；
`colony-agents` 只有 9 个同名，搜得到、不歧义。所以产品、仓库、镜像、包名统一成一套：

| 用途 | 名称 |
| --- | --- |
| 产品 | `Colony Agents` |
| 平台仓 | `colony-agents` |
| 插件仓 | `colony-dsh-plugins` |
| 镜像 | `colony-agents:<version>` |
| npm scope | `@colony-agents/*` |

## 许可

[Apache-2.0](LICENSE)。上游 dsh 本体不在本仓库，以 npm 依赖锁版本引入，遵循其自身许可。
