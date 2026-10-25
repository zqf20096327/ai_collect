<div align="center">
  <img src="https://raw.githubusercontent.com/lingshu-ai-agent/lingshu/main/assets/lingshu_logo.svg" alt="LingShu" width="120"/>

  <h1>lingshu · 灵枢</h1>
  <p><strong>The Pivot of Agent Orchestration</strong></p>

  > **🎉 v0.1.0 — First Stable Release (2026-10-07)** — **55 Stories merged** / **821 tests pass** / **435 source files** / **14 stable SPIs** (`@PublicApi(STABLE)`, 9 Slot + 3 Helper + 2 supporting) / **36 R-13 0-binary-delta PASSes** / **0 new Maven dependencies** during the 0.1.0 cycle / Apache-2.0 / JDK 8 source + JDK 17+ runtime. → See **[CHANGELOG.md](./CHANGELOG.md)** + **[RELEASE_NOTES_v0.1.0.md](./RELEASE_NOTES_v0.1.0.md)** for full release notes.
  > **Recent Story updates** (most recent first, see **[UPDATEINFO.md](./UPDATEINFO.md)** for full details):**PR #90** · #053 · #052 · #051 · #050 · #049 · #048 · #047 · #046 · #045 · #014 · #044 · #043 · #042 · #041 · #037 · #030 · #034 · #033 · #031 · #029 · v1.5.46 refactor · #026 · #025 follow-up.


  <p>
    <a href="https://github.com/lingshu-ai-agent/lingshu/stargazers"><img src="https://img.shields.io/github/stars/lingshu-ai-agent/lingshu?style=for-the-badge" alt="stars"/></a>
    <a href="https://github.com/lingshu-ai-agent/lingshu/network/members"><img src="https://img.shields.io/github/forks/lingshu-ai-agent/lingshu?style=for-the-badge" alt="forks"/></a>
    <a href="https://github.com/lingshu-ai-agent/lingshu/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache_2.0-blue?style=for-the-badge" alt="license"/></a>
    <a href="https://github.com/lingshu-ai-agent/lingshu/issues"><img src="https://img.shields.io/github/issues/lingshu-ai-agent/lingshu?style=for-the-badge" alt="issues"/></a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/java-8+-D97706?style=for-the-badge&logo=openjdk&logoColor=white" alt="java"/>
    <img src="https://img.shields.io/badge/spring--boot-2.7%2B-6DB33F?style=for-the-badge&logo=springboot&logoColor=white" alt="spring"/>
    <img src="https://img.shields.io/badge/maven-3.6%2B-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white" alt="maven"/>
    <img src="https://img.shields.io/badge/license-Apache_2.0-blue?style=for-the-badge" alt="license"/>
  </p>
</div>

---

## 📋 Release Artifacts — v0.1.0 (2026-10-07)

> **First public release.** 45 Stories merged, 766 tests pass, 14 stable SPIs locked.

- 📜 **[CHANGELOG.md](./CHANGELOG.md)** — Full structured changelog (Keep a Changelog 1.1.0 format) — Added / Changed / Fixed / Security / Compatibility / Migration
- 📝 **[RELEASE_NOTES_v0.1.0.md](./RELEASE_NOTES_v0.1.0.md)** — User-facing release notes — What's New, Architecture, Compatibility Promise, Quick Start, Migration, Known Issues, Roadmap

---

## 灵枢 · The Pivot

**灵枢**(`líng shū`,意为"针灸的关键枢轴")是 LingShu 引擎的核心仓库 —— 一个为 **JDK 8+** 企业 Java 栈设计的、生产级 **ReAct Loop Agent Engine**。

> 名字的由来:**Agent 的本质是一个循环**(ReAct),而循环需要一个**枢轴**才能转得稳。
> 我们把这个"枢轴"叫做 LingShu。

> 🟢 **We're an Engine, not an OS.**
> [OryxOS](https://github.com/oryx-labs/oryxos) 等项目定位是"Distributed Agent OS"——单 JAR 部署、跨节点协调、Java 21 + virtual threads。
> LingShu 不跟他们抢这条赛道:LingShu 是一个**嵌进你 Spring Boot 进程的 Engine**,
> 不需要为 Agent 单独搭集群、不需要把 JDK 升到 21、不需要新运维模型。
> 如果你的团队还在 JDK 8 LTS 上、并且你的服务已经跑在 Spring Boot 里 —— LingShu 是默认选项。

---

## ✨ 核心特性

- 🚀 **JDK 8 优先** — 不用 `var` / sealed / records / `List.of` / pattern-switch,主流 JDK 8 LTS 系统直接跑
- 🧩 **9 个 SPI 槽位** — PromptBuilder / LlmProvider / ToolExecutor / PermissionPolicy / RuntimeSandbox / SessionStore / Compactor / **FlowEngine** / **A2aTransport** —— 全部 Spring `@Component` + `@AutoConfiguration` 注册,Provider 按 `name()` 路由,SlotRouter 启动期校验 `version()` 兼容性
- 🔁 **ReAct Loop 一等公民** — 默认 `LinearTurnEngine`,显式 step 计数 + ReasoningStarted / ObservationAppended / MaxStepsExceeded 三类事件
- ⚡ **并行工具调度** — `LinearTurnEngine.dispatchParallel` Semaphore-bounded `CompletableFuture` 池,`config.tool.parallelism` 控制并发度,结果按 LLM-return 顺序回填
- 🔌 **MCP 客户端内置** — 通过 `McpToolAdapter` 把任意 MCP server 当 Tool 源
- 📜 **Skill = Tool 标记接口** — `SKILL.md` 解析 → 自动注册为 Tool,classpath + 目录双源
- 🛡️ **双层沙箱** — `PermissionPolicy`(模型层)+ `RuntimeSandbox`(系统层,chroot/seccomp/sysbox)
- 🎯 **PermissionPolicy 三形式通配** — `StrictPermissionPolicy` yml `allow-list` / `deny-list` 支持 `*` 通配 + `<name>` 精确名 + `<category>:*` 分类前缀(`mcp:*` / `skill:*` / `a2a:*` / `delegate:*` / `local:*` 五保留 category),`Tool.sourceCategory()` 默认方法 + 5 核心 Tool 类型覆盖,Story #029 字符串白名单模式升级为通配 + 分类(Story #031)
- 🤝 **PermissionPolicy ask-mode** (3rd outcome) — `AskUserPermissionPolicy` 5 段决策(deny 命中 → Deny / ask 命中 → AskUser / allow 空 → default-Allow / allow 命中 → Allow / 不命中 → Deny with category 上下文)复用 #031 `PermissionPatterns.matches()` 3 形式 pattern 通配 + `AskUserPermissionPolicyProvider` SPI(`name()="ask"` + `priority()=10` + `version()="1.0.0"`)+ `ApprovalRegistry` @Component `ConcurrentMap<sessionId+":"+approvalId, Consumer<Decision>>` 终局收集器(register/consume/size/evictBySessionPrefix 4 方法)+ `AgentEvent.ApprovalRequired` 3-arg ctor(approvalId UUID + sessionId + Decision ask)+ `LinearTurnEngine.dispatchWithPolicy` AskUser branch `CompletableFuture<Decision>` 阻塞-解阻塞回合(CompletableFuture 阻塞 → registry.register(approvalId, future) → ApprovalRequired 事件发射 → future.complete(decision) 由 demo-product ChatController `POST /api/approvals/{sessionId}/{approvalId}` 端点解阻塞)+ `AgentConfig.ToolsConfig.askList` + 顶层 `approvalTimeoutSeconds: int` 默认 **0 = 无超时**(Claude Code overnight parity —— 企业审批隔夜(下一个工作日)决定也能 merge);`>0` 时 N 秒后走 `LINGS-P02 PERMISSION_APPROVAL_TIMEOUT` Deny(Story #030 + **Story #037 permission-policy-multi-provider-alignment** —— 3 Provider 注册路径 100% 对齐 v1.5.28 §5.5 多 Provider 模式,`AllowAllPermissionPolicyProvider` 删 `@Component` 改 plain POJO + `@Bean(name="permissionPolicyProvider_default-1.0.0")` 显式注册,与 sibling `StrictPermissionPolicyProvider` #029 + `AskUserPermissionPolicyProvider` #030 对齐)
- 🛟 **AskUser hang 安全 + history 协议一致已上线** — **Story #048 ask-user-sentinel-tool-result** 关闭 Story #030 ask-mode 接通后的剩余 silent-bug:**根因** —— `LinearTurnEngine.dispatchWithPolicy` AskUser 分支阻塞 `CompletableFuture<Decision>` 时,**没有**任何 sentinel `tool_result` 提前提交;若前端永远不渲染 Allow/Deny 按钮(用户关掉 modal / 浏览器断网 / 慢网络),下一 turn 上送 Anthropic 时 session history 含未配对 `tool_use` 块 → server 返回 HTTP 400 `"messages.X: tool_use ids were found without tool_result blocks"` → 整个 agent loop 永久停摆。**补丁** —— **Sentinel 提交**(在 `Decision resolved = toolCtx.approval().ask(...)` **之前**调 `ctx.appendToolResult(ToolResult.builder().toolUseId(call.getId()).content("[PENDING_APPROVAL] Awaiting user decision for tool: " + call.getName()).isError(false).build())`,即使前端永远不 resolve,**history 也已经有配对的 tool_result**)+ **Upsert-by-toolUseId 语义**(`DefaultTurnContext.appendToolResult` 改为:扫描 history tail 从末端到最末 Assistant 间的窗口,如发现同 `toolUseId` 已存在的 `Message.ToolResult` 则**就地替换**;否则末尾追加;范围 bound by 最末 Assistant 让 older turns 同 toolUseId 不被误改;全段扫描在 `DefaultSession.appendLock()` monitor 内,与 `append(Message)` / `compact(List)` 同锁);**2 文件改 prod**(`LinearTurnEngine.dispatchWithPolicy` AskUser 分支插 sentinel + `DefaultTurnContext.appendToolResult` upsert 实现)+ **6 文件改 test 8 net new AC case**(AC-048-01/02/03 `DefaultTurnContextUpsertTest` 3 L1 upsert 3 边:same-id replace / 不同-id append / scoped-by-most-recent-Assistant)+ AC-048-04/05/06/07 `LinearTurnEngineAskUserTest` 追加 4 L2 守卫:1 sentinel-before-block / 2 same-id-replace-deny-replaces-sentinel-with-deny-toolresult / 3 different-id-appends-cleanly / 4 keep-history-protocol-consistent-when-resolved + AC-048-08 `LinearTurnEngineAskUserNoRenderIT` 1 L3 端到端 闭环:`CaptureOnlySink` 永远不 invoke continuation + 300ms 后 `ctx.markDone()` 触发取消;验证 `assertCurrentTurnHistoryIsProtocolConsistent()` 走 current-turn slice 扫描每个 `tool_use.id` 都有 matching `tool_result` + `history` 恰有 1 个 `TR(toolUseId="c1")` + `ApprovalRegistry.size() ≥ 1`);**0 新 ErrorCode**(复用 Story #030 `LINGS-P01/P02` 不增加新路径)+ **0 新 Maven 依赖** + **R-13 mitigation (d) baseline 镜像 pre/post dep-tree 仅时间戳差异** = **0 binary delta**;**e2e 契约** —— demo-product `permission-policy: ask` + `tools.ask-list: [bash_safe]` 配 ask-mode,在聊天输入触发 `bash_safe` 调用,前端不点 Allow/Deny 直接关浏览器,等待 5 秒 → 浏览器再发第二句 → Anthropic HttpServer 收到 POST 后,**不**再有 HTTP 400 `tool_use ids were found without tool_result blocks`(Story #048,758 core + 5 demo = **763 tests / 0 fail / 0 error**,合并入 #047 一 commit 共 `R-13 0 binary delta 第 31 次 PASS`)
- 🔄 **FlowEngine 可替换** — `LinearTurnEngine` 默认,`GoogleAdkFlowEngine` / `AlibabaGraphFlowEngine` / 自研 DAG 可平替
- 🪶 **Lombok 友好** — `@Value` 不可变风格,拒绝过度抽象
- 🔁 **YAML 热更无中断** — `AgentConfigRegistry` `AtomicReference` 单写多读 + `Files.getLastModifiedTime` 5s poll + `DefaultAgent.run()` 入口一次性 freeze,旧 turn 冻结 cfg 引用语义自然隔离(Story #007)
- 🛑 **ReAct 上限守卫** — `LinearTurnEngine.runTurn` `maxStepsHit` 守卫标志 + `AgentEvent.MaxStepsExceeded(maxSteps, totalUsage)` 结构化事件,防止 LLM 死循环 token 失控(Story #008)
- 🌐 **A2A AgentCard 已上线** — `GET /.well-known/agent.json` 服务端暴露,A2A v1.0 §2.1 协议对齐,字段直接来源于 `cfg.getIdentity()`,无需额外 yml(Story #009 AC-10)。A2A 客户端 4 子 Story 拆分(详见 [Story 路线图](#-story-路线图-009a009d-a2a-client-系列)节):**#009a GrpcA2aTransport**(本轮 / grpc-java + protobuf)+ **#009b InProcessA2aTransport**(同 JVM 直接调用 / 0 额外依赖)+ **#009c HttpJsonRpcA2aTransport + RemoteAgentTool**(默认 Provider / JDK HttpClient / 0 额外依赖)+ **#009d RemoteAgentSchemaBuilder**(扫 `AgentCard.skills[]` 生成 `ToolSpec` list / 0 额外依赖)
- 🖥️ **CLI 入口已上线** — `mvn -pl lingshu-cli spring-boot:run --args='run --config app.yml --prompt ...'`,5 个子命令 `run / resume / serve / doctor / config`,hand-rolled argv 解析器零新依赖,Story #017 dsh §10.3 全落地
- 🧹 **TruncatingCompactor 已上线** — `Compactor` SPI Slot 2 v1 默认实现,两步压缩(ToolResult 内容截断 + 滑动窗口收口),`Session.compact(List)` 原子替换 + 与 `append(Message)` 同锁,`@Value AgentConfig.CompactorConfig(maxPromptTokens / maxToolResultBytes / keepRecentTurns)` zero-config 默认 `(100_000 / 50_000 / 20)`(Story #018 dsh §6.2)
- ⚙️ **Compactor turn 端真接通** — `LinearTurnEngine.runTurn` 主循环 `shouldCompact()` 守卫 + `compact(ctx)` 在 LLM call 之前调用,`AgentEvent.Compacted` 事件沿既有契约复用(0 新事件),触发路径在每个 ReAct step 顶端;`LinearTurnEngineProvider` 7-arg ctor 增 `@Autowired(required=false) CompactorRouter` + 构造器级 `@Autowired` 显式标注(Spring 6 双 ctor 选择 heuristic 兜底),`compactorRouter == null` 时回退 `NullCompactor.INSTANCE` zero-overhead,`AgentConfig.@Value` 顶层 `compactor` 字段 + `top-level yml agent.compactor` binding,9-Router `AgentFactory` ctor 加 `CompactorRouter` 第 9 Router;空 yml → `truncating` default → `TruncatingCompactor` 真触发(Story #045,dsh §6.1 L3630-3631 + §5.3.1.0 第 9 Router 真接通)
- 🛠️ **5 个内置 Tool 已上线** — `Read` / `Write` / `Edit` / `Bash` / `WebFetch`(`@Component implements Tool`),`LocalToolsAutoConfiguration` 启动期自动注册到 `DefaultToolExecutor.registry`,Bash 复用 `RuntimeSandbox.process()` 走 tenant whitelist,字节上限先于盘写(防 OOM / 防路径穿越),`agent.tools.enabled=false` 干净跳过(Story #019 dsh §6.5 (1)+ **Story #032 WebFetch 本地 HTTP/HTTPS 抓取** —— `name()="web_fetch"` + `description()` 含 "domain whitelist" + "POST/PUT/DELETE traffic is NOT supported" + `inputSchema` `{url: string required, max_bytes?: integer}` + `execute()` 4 段委托 `ctx.http().get(url)` 走 `WhitelistedHttpClient.check()`(Story #028 沙箱基建复用)→ JDK `HttpURLConnection` / `HttpsURLConnection` 透明 HTTPS + User-Agent `ChaOS-LingShu-Sandbox/1.0` 透传 + 1 MB truncation marker `\\n...[truncated, original %d bytes]` + catch `AccessDeniedException` 嵌 `[LINGS-S01]` + catch `IOException` 嵌 `HTTP fetch failed: ...`;**Claude Code parity**:本地 `WebFetch` 与 MCP fetch server **共存**(built-in + MCP 并行,非互斥);GET-only,POST/PUT/DELETE 走 MCP)
- 🧩 **Skill 系统第一块砖** — `SkillTool` concrete class + `fromMarkdown` 静态工厂(SKILL.md → Skill)+ `@Component CommitSkill`(`/commit` 按 Conventional Commits 风格生成 commit message)+ `ToolRegistry` 4 新方法(`modelVisibleSpecs / findSkill / skillNames / findByName`)+ `SkillAutoConfiguration` 注册样板(复用 `LocalToolsAutoConfiguration` 模板 + `@Lazy Map<String, Skill>` 破 bean-cycle + `agent.skills.enabled` 开关),`DefaultToolRegistry` 双索引(`registry` + `skillsByName`)配 `putIfAbsent` first-wins,`@Component` Skills 与 SKILL.md Skills 同名时 `CommitSkill` 注册先后决定胜出(Story #020a dsh §6.4 核心)
- 📂 **SKILL.md 多源自动发现已上线** — Slot 4 sub-SPI:`SkillSource`(4 方法:type / location / discover / watchable)+ `SkillSourceProvider`(2 方法:type / create),`SkillSourceRouter` 启动期按 `type()` 索引 Provider,v1 两个实装(`classpath` 走 `PathMatchingResourcePatternResolver` 扫 `classpath*:prefix/**/SKILL.md` / `directory` 走 NIO `DirectoryStream` 一层扫 `<dir>/*/SKILL.md`),`CompositeSkillLoader.loadAll` 串起所有 source(单 source 失败不阻塞他人),`SkillAutoConfiguration` 扩展 Phase 1(SKILL.md 自动发现)+ Phase 2(`@Component` Skills)`mergePhases` 合并 → `ToolRegistry.register`,Phase 1 wins on name collision(用户可放下 SKILL.md 覆盖内置 `@Component` Skill);`SkillSourceProperties` 是 plain POJO + 静态 `bindFromEnvironment()` 工厂(R-13 dep-lock 兼容:只用 spring-core `Environment`,不用 spring-boot `Binder`),`agent.skills.sources[].type + .location` YAML 直接 bind → Map(Story #020b dsh §6.4 多源,0 新依赖)
- 📡 **MCP server 3 transport 已上线**(stdio / SSE / streamable HTTP,Story #021a → #021b → #021c;**SSE + streamable HTTP 已按 MCP 规范重写,PR #90**) — `McpServerConnection` interface 8 方法 + 6-态状态机(`IDLE / CONNECTING / CONNECTED / DISCONNECTED / RECONNECTING / FAILED`);3 concrete 实现(`StdioMcpServerConnection` + `SseMcpServerConnection` + `StreamableHttpMcpServerConnection`)由 `McpServerConnectionFactory.create(cfg.transport())` 静态分派;`McpHttpSupport` 共享 HTTP / JSON-RPC 样板(`HttpURLConnection` JDK 1.1 + Jackson `ObjectNode`,**0 新 Maven 依赖**);**MCP 规范单端点语义**(PR #90):所有 JSON-RPC 消息 POST 到**同一个** MCP endpoint(再也不是 `{url}/tools/call` 这种目录前缀路径),SSE 先在长连接上等 server 的 `event: endpoint` 事件拿到 POST URI 再握手,响应按 `event: message` + JSON-RPC `id` 配对;`Mcp-Session-Id` + `MCP-Protocol-Version`(negotiated `2025-06-18`)2 个头在后续请求回显;HTTP 404 = session 过期 → 清 session + 重新 `initialize` + 重试 1 次;SSE long-lived 守护 `Thread` + 手写 `BufferedReader.readLine()` SSE parser(malformed 事件不杀流),streamable HTTP 无 SSE reader;2 个 HTTP transport 心跳统一改为经 POST URI 发 JSON-RPC `ping`(不再 `GET /health`);**出站域名白名单 yml 可配** `agent.mcp.servers[*].domain-whitelist`(PR #90 打通 yml → `McpServerProperties` → `AgentConfig.ServerConfig` → `McpTransportAutoConfiguration` → `McpServerConfig`,Story #033 的 OQ-Future yml binding 收口);3 transport 共享指数退避 `1s → 2s → 4s → 8s → 16s → 32s → 60s(cap)` 无限重试 + per-listener try/catch 异常隔离;`McpErrorCodes` 新错误域 `M`(M01 stdio 失败 / M02 tool-call 失败 / M03 HTTP-SSE 失败);`callTool` 在非 CONNECTED 状态返 `McpCallResult.error(...)` 而**不**抛异常(对齐 §4.10.1 硬规则 2);dsh §6.5 (2.1)
- 🔗 **Tool/LLM 视角闭环已上线** — `DefaultPromptBuilder` 注入共享 `ToolRegistry`,`Prompt.tools = toolRegistry.modelVisibleSpecs()`(sorted snapshot);本地 Tool(Read/Write/Edit/Bash)+ MCP Tool + `@AgentTool` + Skill + RemoteAgentTool 全部经统一 registry 暴露给模型;**OQ-5 解决**(Story #024 dsh §6.4 [TOOL SCHEMAS] + §5.6.3.0 `RemoteAgentTool.description()` HINT 链路 + ToolRegistry 单点注册闭环,0 新依赖 / 0 新 ErrorCode)
- 🎁 **Demo 产品已上线** — `lingshu-examples/demo-product/` HTTP SSE chat 产品组合 8 features(Spring Boot + SSE 流式 + ReAct 事件流 + `@AgentTool` + SKILL.md Skill + MCP stdio 子进程 + 内存会话 + Hot-reload 配置,Story #025) + `lingshu-examples/demo-product-a2a-server/` 跨 JVM translate demo(9090 端口通过 `RemoteAgentTool` + `HttpJsonRpcA2aTransport` 与 8080 `demo-product` 互通,Story #025b);**0 新 Maven 依赖**
- 🌱 **YAML `${...}` 占位符跨路径统一** — `PlaceholderResolver` 静态工具类(brace-counting scanner 4-form grammar:`${X}` / `${X:default}` / `${X:${Y}}` 嵌套 / `$${literal}` 转义;env → sys-prop 查找;32 层环检测),`AgentFactory.loadYamlAndValidate` 在 `parseMinimalYaml` 与 `toAgentConfig` 之间 hook 调用,**修跨路径 parity bug** —— 之前 CLI / YamlWatcher hand-rolled 路径下 `${user.dir}` 静默变 13 字符串,Spring Env 路径(demo-product)一直支持;新增 2 ErrorCode `LINGS-C03 YAML_PLACEHOLDER_UNRESOLVED` / `LINGS-C04 YAML_PLACEHOLDER_CYCLE`;**0 新 Maven 依赖**(Story #026)
- 🤖 **Anthropic 协议层 Tool 转换已上线** — `AnthropicLlmProvider` 4 段协议链全贯通:`buildRequestBody` 真翻 `Prompt.tools` → 顶层 `tools:[]`(`{name, description, input_schema}`)+ `messages[].content` 展开为 array of blocks(`text` / `tool_use` / `tool_result`)+ 连续 `Message.ToolResult` **合并为单 user message 多 tool_result block**(Anthropic 协议层硬约束)+ `parseResponse` 解析 `tool_use` block → `ToolCall(id, name, input)`;`TurnContext.appendAssistant` 签名扩 `toolCalls` 参数 + `DefaultTurnContext` 实现对齐 + `LinearTurnEngine.L166` 真传 `resp.getToolCalls()`;新增 2 ErrorCode `LINGS-L01 TOOL_USE_BLOCK_INVALID` / `LINGS-L02 TOOL_RESULT_BLOCK_INVALID`(LlmProvider 域 L 段 1/2 号);Spring AI `ChatClient.tools().call()` 仍**禁止**使用(§4.10.1 硬规则 2);**OQ-7 解决**(Story #027a,**0 新 Maven 依赖**)
- 📡 **Anthropic SSE 真流式已上线** — `AnthropicLlmProvider.doPostStream` 把非流式 POST + 一次性 readAll 替换为 SSE `text/event-stream` accept + `BufferedReader.readLine()` 逐行解析(沿用 #021c `SseMcpServerConnection` 手写 SSE parser 模式)+ `AnthropicStreamParser` 6-类事件状态机(`message_start` → `ReasoningStarted` + init usage / `content_block_start` × text + tool_use → 触发 `ToolStarted` / `content_block_delta` × text_delta + input_json_delta → 持续 `TextDelta` + per-block JSON 拼接 buffer / `content_block_stop` → per-block `MAPPER.readTree()` 构造 `ToolCall` / `message_delta.stop_reason` / `message_stop`) + `Map<Integer, StringBuilder>` text blocks + `Map<Integer, ToolCall.Builder>` tool blocks 交错状态机;LLM 流式首 token P50 ≤ 1.5s NFR(constitution §3)真达标;新增 `LINGS-L03` reserved 常量(§14 N6 graceful shutdown 后续启用,本期不抛);复用 #027a `LINGS-L01` 协议层 ErrorCode(SSE 解析 tool_use 缺 id/name);`parseResponse` 保留为 fallback(`anthropicStreamEnabled=false` 配置路径仍可用);**§6.5 protocol gap 全闭合**(Story #027b,**0 新 Maven 依赖** / **R-13 0 binary delta 第 13 次 PASS**)
- 🧵 **Anthropic LLM I/O 池已有界** — `AnthropicLlmProvider.ioExecutor` 字段初始化从无界 `Executors.newCachedThreadPool`(`maximumPoolSize = Integer.MAX_VALUE`,极压下 OOM 风险)替换为有界 `ThreadPoolExecutor`,镜像 `ToolExecutorConfig.agentToolPool` 100% shape:`corePoolSize = cores * 2` / `maxPoolSize = cores * 4` / `keepAliveTime = 60s` / `LinkedBlockingQueue(256)` / `CallerRunsPolicy` 兜底 / daemon=true / 线程名前缀 `anthropic-llm-io-N`(per-instance 计数,`jstack` 友好与 `lingshu-tool-N` 风格对齐);`CallerRunsPolicy` 在队列满时让 `LinearTurnEngine` 主线程兜底执行,back-pressure 慢不丢(主线程阻塞自限流,而非无界堆积);`buildBoundedIoExecutor()` 私有静态方法 + 5 import(`LinkedBlockingQueue` / `ThreadFactory` / `ThreadPoolExecutor` / `TimeUnit` / `AtomicInteger`)+ 类级 Javadoc 详细描述 Story #043 改动 + 镜像 `ToolExecutorConfig` 字段对齐表;**根除 `lingshu-core/src/main/java/` 唯一一处无界生产线程池**(Story #043,**0 新 Maven 依赖** / **0 新 ErrorCode** / **R-13 0 binary delta 第 26 次 PASS**)
- 🛡️ **AgentConfig 顶层 turn 并发闸门已上线** — `AgentConfig.@Value` 24 → 26 字段 final,顶层扩 `maxConcurrentTurns`(默认 16)+ `maxConcurrentQueueDepth`(默认 32)2 int 字段,空 yml 自动 fallback 16 + 32,顶上 `validate()` 聚合 `reactMaxSteps` + 2 新字段检查到单 `LingsConfigException`,复用 `LINGS-C02` ConfigError 路径;`AgentConfigDefaults` + `AgentFactory.toAgentConfig` + 53 fixture `new AgentConfig(...)` 全部同步 +2 实参(0 业务逻辑改动,纯 Lombok `@AllArgsConstructor` 再生参数补齐);**dsh §10 NFR row 4 「默认 16,排队 ≤ 32」数字基线落地**(原 NFR 表一行,本 Story NFR 表 + AgentConfig 字段 + yml 接线 3 处对齐)+ **兑现 Story #043 forward reference**(Story #043 §10 NFR row 4 footnote 写「Story #044 处理 docs/code 兑现」,本 Story 兑现)+ **Future-proof 双重闸门**(Story #043 单池已有界 + Story #044 顶层闸门 = N 并发 turn × 单池上限 仍有界);(Story #044,**0 新 Maven 依赖** / **0 新 ErrorCode**(复用 `LINGS-C02`)/ **R-13 0 binary delta 第 27 次 PASS**)
- 🛟 **AskUser hang 安全 + history 协议一致已上线** — 关闭 Story #030 ask-mode 接通后剩余的 silent-bug:`LinearTurnEngine.dispatchWithPolicy` AskUser 分支阻塞 `CompletableFuture<Decision>` 时**无** sentinel `tool_result` 提前提交,前端永远不渲染 Allow/Deny 按钮(用户关 modal / 浏览器断网 / 慢网络)会让 history 含未配对 `tool_use` 块,下一 turn 上送 Anthropic 时 server 返回 HTTP 400 `"messages.X: tool_use ids were found without tool_result blocks"` → 整个 agent loop 永久停摆。**2 文件改 prod** —— `LinearTurnEngine.dispatchWithPolicy` AskUser 分支在 `Decision resolved = toolCtx.approval().ask(...)` **之前**调 `ctx.appendToolResult(sentinel [PENDING_APPROVAL Awaiting user decision for tool: <name>])`(即使前端永远不 resolve,history 也已经有配对的 tool_result)+ `DefaultTurnContext.appendToolResult` 改 upsert-by-toolUseId 语义:扫描 history tail 从末端到最末 Assistant 间的窗口(如发现同 `toolUseId` 已存在的 `Message.ToolResult` 则**就地替换**;否则末尾追加;范围 bound by 最末 Assistant 让 older turns 同 toolUseId 不被误改;全段扫描在 `DefaultSession.appendLock()` monitor 内,与 `append(Message)` / `compact(List)` 同锁)。**8 net new AC case** —— AC-048-01/02/03 `DefaultTurnContextUpsertTest` 3 L1 upsert 3 边(same-id replace / 不同-id append / scoped-by-most-recent-Assistant bound)+ AC-048-04/05/06/07 `LinearTurnEngineAskUserTest` 追加 4 L2 守卫(sentinel-before-block / same-id-replace-deny-replaces-sentinel / 不同-id-cleanly-append / keep-history-protocol-consistent-when-resolved)+ AC-048-08 `LinearTurnEngineAskUserNoRenderIT` 1 L3 端到端 闭环:`EchoLlmProvider` + `RecordingPromptBuilder` + `CaptureOnlySink`(永远不 invoke continuation)+ 300ms 后 `ctx.markDone()` 触发取消 + `assertCurrentTurnHistoryIsProtocolConsistent()` 走 current-turn slice 扫描每个 `tool_use.id` 都有 matching `tool_result` + `history` 恰有 1 个 `TR(toolUseId="c1")` + `ApprovalRegistry.size() ≥ 1`。**e2e 契约** —— demo-product `permission-policy: ask` + `tools.ask-list: [bash_safe]` 配 ask-mode + 聊天触发 `bash_safe` 调用 + 前端不点 Allow/Deny 直接关浏览器 + 等 5 秒 + 再发第二句 → Anthropic HttpServer 收到 POST **不**再有 HTTP 400 `tool_use ids were found without tool_result blocks`。**0 新 ErrorCode**(复用 Story #030 `LINGS-P01/P02`,不增加新路径)+ **0 新 Maven 依赖** + **R-13 mitigation (d) baseline 镜像 pre/post dep-tree 仅时间戳差异** = **0 binary delta 第 31 次 PASS**(Story #047 + #048 共 1 commit)。**累计 Story 合入:45 → 47**(Story #047 + Story #048 共同 commit)。
- 🤝 **PermissionPolicy ask-mode 端到端 wiring 已真接通** — 关闭两条历史 silent-ignored bug 让 demo-product `permission-policy: ask` + `tools.ask-list: [write_file, bash_safe]` yml **真触发** `AskUserPermissionPolicy` 5 段决策:**Bug A** —— `AgentFactory.java:280` `policyRouter.resolve(config.getSandbox().getPolicy(), config)` 错读 Slot 3 sub-field → 改为 `policyRouter.resolve(config.getPermissionPolicy(), config)`(Story #029 / #030 / #031 / #037 写好的 Slot 4 顶层字段终于真接通,yaml `agent.permission-policy: ask` 不再被 silently 默认成 `default` 走 `AllowAllPermissionPolicy`)+ **Bug B** —— demo-product `ChatController.createSession()` hand-rolled 28-arg `AgentConfig` ctor 丢弃 yml-bound `@Bean AgentConfig` 模板中所有 `agent.tools.ask-list` 等字段 → ctor 改收 Spring-managed `AgentConfig agentConfigTemplate` 5th 参数,工厂 lambda `return agentFactory.create(agentConfigTemplate);` 单行(对齐 `agentConfig(Environment)` `@Bean` 模板 26 字段全透传)+ demo-product `DemoProductApplication.readTools()` 把硬编码 `Collections.emptyList()` 改为 `readToolsList(env, "agent.tools.ask-list", fallback.getAskList())`(`tools.ask-list` yml key 真 binding 到 `AgentConfig.ToolsConfig.askList`);**3 文件改 prod**(`AgentFactory.java:280` Bug A + `DemoProductApplication.readTools()` + `ChatController.java` ctor)+ **3 文件改 test 6 net new AC case**(`AgentFactoryAskPolicyYamlIT` 2 L2 yml parse 契约:`yml_permission_policyAsk_bindsTopLevel` + `yml_toolsAskList_bindsIntoToolsConfig` / `AgentFactoryAskPolicyRoutingIT` 3 L2 Slot 4 Router.resolve routing 契约:`resolvesPermissionPolicyTopLevel_notSandboxPolicy` 双字段 yml 验证 `ask` Provider 胜出 + `permissionPolicyAsk_resolvesAskUserPermissionPolicy` 实例类型 + `permissionPolicyDefault_resolvesAllowAllPermissionPolicy` yolo back-compat / `DemoProductAskPolicyEndToEndIT` 1 L3 demo-product e2e blackbox:`@SpringBootTest(classes = DemoProductApplication.class)` + `@Autowired AgentConfig demoAgentConfig` + `@Autowired AskUserPermissionPolicyProvider askProvider` 验证 `policy instanceof AskUserPermissionPolicy` + `bash_safe → Decision.AskUser("matches pattern 'bash_safe'")` + `write_file → Decision.AskUser("matches pattern 'write_file'")` + `read_file → Decision.Allow` via wildcard allow-list 回归守卫);**0 新 ErrorCode**(复用 Story #030 `LINGS-P01 TOOL_NOT_IN_ALLOWLIST` + `LINGS-P02 PERMISSION_APPROVAL_TIMEOUT`)+ **0 新 Maven 依赖** + **R-13 mitigation (d) baseline 镜像 pre/post dep-tree 仅时间戳差异** = **0 binary delta 第 31 次 PASS**;**Story #029—#031 + #037 + #030 ask-mode 五件套端到端闭环**(Story #029 strict 真实现 + Story #030 ask-mode 真接通 + Story #031 pattern 通配 + Story #037 PermissionPolicy 3 Provider 注册路径 100% 对齐 + Story #047 end-to-end yml 真 binding,业务方 demo-product 配 `permission-policy: ask` + `tools.ask-list: [write_file, bash_safe]` 真触发 ApprovalRequest round-trip,demo-product `POST /api/approvals/{sessionId}/{approvalId}` SSE 闭环已落 `#042` frontend UI)(Story #047,758 core + 5 demo = **763 tests / 0 fail / 0 error**)
- 💾 **Slot 5 SessionStore save-after-turn 已真接通** — `LinearTurnEngine.runTurn` 主循环 4 个 turn 收口点(loop-head cancel / normal end / maxSteps 触发 / waitForLlm cancel / 异常前)`trySave(ctx)` 守卫调 `sessionStore.save(ctx.session().checkpoint())`,save 失败 RuntimeException **catch-and-log 不 crash 已完成 turn**(`sessionStore.save` 抛异常 → `LOG.warn` 落库 + turn 仍然 emit `TurnCompleted`);`LinearTurnEngine` 8-arg primary ctor 增 `SessionStore sessionStore` final 参数 + `if (sessionStore == null) throw new IllegalArgumentException("sessionStore must not be null")` 启动期 fail-fast;`LinearTurnEngineProvider` 8-arg ctor 增 `@Autowired(required=false) @Nullable Routers.SessionStoreRouter sessionStoreRouter`(镜像 Story #045 CompactorRouter precedent)+ 构造器级 `@Autowired` 显式 primary 标记 + 5/6/7-arg legacy ctor 委托 8-arg 传 `NullSessionStore.INSTANCE` zero-overhead;`Routers.SessionStoreRouter` 从 `Story #014` stub → `Story #046` 真接通(`SessionStoreRouter.resolve("file", cfg)` → `FileSessionStore` / `resolve("memory", cfg)` → `NullSessionStore.INSTANCE`);`AgentFactory` 8-Router ctor(`Story #014` 已落)直接复用,**不**再加 Router 字段(Slot 5 SessionStore 在 AgentFactory 8-Router ctor 中已就位);**null sessionStoreRouter → `NullSessionStore.INSTANCE` wire-in**(`sessionStore.save(checkpoint)` no-op,`SessionStore#load(id)` 返 `Optional.empty()`),保护 Story #001-#014 / Story #027a / Story #029-#045 fixture 0 业务逻辑改动只参数补齐;**0 新 ErrorCode**(复用 Story #014 `LINGS-X01 SESSION_STORE_IO_FAILED`)+ **0 新 Maven 依赖** + **R-13 mitigation (d) baseline 镜像 pre/post dep-tree 仅时间戳差异** = **0 binary delta 第 30 次 PASS**;**dsh §6 主链 Slot 5 SessionStore 端到端真接通**(Story #014 stub + SPI + 双后端 Provider → Story #046 主循环 hook + Router.resolve 真接通,业务方配 `agent.session-store: file` + demo-product 启动 + 浏览器聊天 → `/var/folders/.../lingshu-sessions/` 目录**真**有 `<sessionId>.json` checkpoint 文件生成,可 JSON 解析 `history.length > 0` 验证 round-trip)(Story #046,**16 new case**:`LinearTurnEngineSessionStoreTest` 6 L1 turn 收口点全覆盖 + `LinearTurnEngineProviderSessionStoreTest` 3 L1 Provider + `NullSessionStoreTest` 2 L1 sentinel + `RecordingSessionStoreTest` 0 + `AgentFactoryYamlSessionStoreSaveIT` 3 L2 yml 接线 + `AgentFactoryYamlSessionStoreLoadIT` 2 L2 multi-slot yml shape)
- 🛡️ **deny-once guard + step-reset SSE 收口已上线** — `LinearTurnEngine.dispatchWithPolicy` AskUser 分支加 per-turn `attemptedDeny: Set<String>` 守卫:同一 `toolUseId` 被人类 deny 过一次后,LLM 在同 turn 重发同一 id 触发 AskUser 时**不再**重新发 `AgentEvent.ApprovalRequired`(避免用户已拒绝又被无限重弹 approval modal / engine 永远到不了 `TurnCompleted`)。守卫命中时发射 deterministic `ToolResult.error("[LINGS-P02] tool previously denied for tool '<name>' (id=<id>)")` 进 history 让 Anthropic 协议匹配,Anthropic `message_start` 上 `tool_use ids were found without tool_result blocks` 错不会再现。`turn-start reset`:`runTurn()` 头一句 `this.attemptedDeny = ConcurrentHashMap.newKeySet()` 防止跨 turn 状态污染。**Bug-1**(SSE step reset) — `AnthropicStreamParser` L208 把 `message_start` 上重置 UI step counter 的 `ReasoningStarted(step=1, maxSteps=50)` 替换为**新事件类型** `AgentEvent.LlmStreamStarted(streamId=Anthropic message_id verbatim, maxOutputTokens=0 sentinel)`;`AgentEventMapper` 加 `LlmStreamStarted` 分支 `out.put("type","llm.stream.started");out.put("streamId",..);out.put("maxOutputTokens",..);`;ReAct step counter 仍由 `LinearTurnEngine.runTurn` 在每 step 顶端发射 `ReasoningStarted(step, maxSteps)`,与 Bug-1 修复前等价。**3 prod file**(`LinearTurnEngine.java` `attemptedDeny` 字段 + 4 处守卫 hook + `AnthropicStreamParser.java` L208 emit replace + `AgentEventMapper.java` 新分支)+ **1 mapper file**(`AgentEventMapper.java`)+ **5 test files**(`AgentEventLlmStreamStartedTest` 2 L1 / `AnthropicStreamProviderIT` 2 L2 SSE streaming 端到端 / `DemoProductAgentEventMapperLlmStreamStartedTest` 5 L2 mapper 黑盒 / `LinearTurnEngineAskDenyGuardTest` 4 L2 deny-once guard 黑盒 / `LinearTurnEngineStreamStartedRegressionTest` 1 L2 Bug-1 regression 守卫)+ **2 fixture updates**(`AnthropicStreamProviderIT` 改 mock event 序列带 message_id / `DefaultToolExecutor.AllowAllPermissionPolicy` fixture 加 deny-once 测试 policy)。`mvn -pl lingshu-core test` **821 pass / 0 fail**(750 pre-#050 + 71 新 case);`mvn -pl lingshu-core dependency:tree` pre/post md5sum diff **仅时间戳差异** = **0 binary delta 第 33 次 PASS**(纯 JDK 8 `ConcurrentHashMap.newKeySet` + `Lombok @Value` + `Message.@JsonTypeInfo/@JsonSubTypes` Story #046 已锁 + `GetMethod` 反射 + `Jackson @JsonProperty` 已锁 + Spring `@Component` 已锁 0 新 binary 引入)。`banned-dependencies` enforcer Rule 0: passed。**0 新 ErrorCode**(复用 Story #030 `LINGS-P02 PERMISSION_APPROVAL_TIMEOUT`,本 Story 给它扩第 2 个语义「deny-once guard hit」),复用 Story #030 `LINGS-P01 TOOL_NOT_IN_ALLOWLIST` 不动。**关键不变项** —— `Message` 4 子类契约不变 + `AgentEvent` 基类不变(只新增 1 个 `LlmStreamStarted` nested class subset of `ReasoningStarted` 形状不变)+ `LinearTurnEngine` 公开签名不变(只新增 1 个 instance 字段 `attemptedDeny` + 4 guard hook,公开方法 0 改动)+ `PermissionPolicy` SPI 不变 + `Decision` 3 子类不变 + `AnthropicLlmProvider` 公开签名不变 + `ToolExecutor.dispatch()` 5 步流水线不变(§4.10.1 硬规则 2 守住)+ `AgentConfig` 不可变契约不变(0 字段新增)+ `AgentFactory` SPI 不变(@Autowired 9-Router ctor 不动)+ `AgentEventMapper` 公开签名不变(只 `toJson` 新加 1 case 分支)+ 9 Slot 体系不变 + 27 字段 AgentConfig schema 不变 + JDK 8 兼容(`ConcurrentHashMap.newKeySet` + `Set.contains` + `Mockito 5.8` 测试 + `Awaitility 4.2.0` 测试已锁,no `var` / `List.of` / sealed / records);Spring AI `ChatClient.tools().call()` 仍**禁止**使用(§4.10.1 硬规则 2 守住) + ReAct Loop 自实现不变(§4.10.1 硬规则 1 守住)。**业务价值** —— **Bug-1 SSE step counter 不再 every-message_start 重置**(demo-product 浏览器 UI 显示 step=1→2→3… 看到 LLM 真在思考步骤,**不再是错误地每次 message_start 跳回 1 → 50**)+ **Bug-2 ask-mode 不再无限弹 modal**(用户点 Deny 后系统记忆同一 tool 已经被拒过,LLM 重发同 id 不再问)+ **Anthropic 协议层硬约束遵循**(Anthropic server `tool_use ids were found without tool_result blocks` HTTP 400 错不再触发,history 始终 protocol-consistent);**修复者** Claude Code(根据用户 2026-10-15 会话反馈「SSE 显示 step 一直在跳 1,问一个看上去也是跳 1,看着很奇怪」+「ask-mode 我点 deny 了一会又弹一次一样的对话框,LLM 在死循环重发同一个 tool call」+「实施吧」,触发本 Story 实施 + 71 case AC 黑盒验证 + R-13 mitigation (d) baseline 镜像 **第 33 次 PASS 0 binary delta**)
- 🛡️ **`LinearTurnEngine.dispatchParallel` boundary sentinel 已上线** — 关闭 Story #050 引入 `dispatchParallel` (multi-tool-call 并发 dispatch) 后剩余 2 类**下游 SPI 返回值缺口**破 Anthropic protocol invariant(每个 `tool_use` block 必有 matching `tool_result` block by toolUseId,否则下轮 LLM 调用 HTTP 400 `tool_use ids were found without tool_result blocks`):**(A) null-result boundary** —— `McpTransport.callTool` 远程调用 nack / `CompletableFuture` 边界返回 `null` 而非 `ToolResult`;**(B) wrong-id boundary** —— port 冲突 / prompt cache reuse stale response / mock 测试桩 fixture bug 让下游 SPI 返回 `r != null` 但 `!r.getToolUseId().equals(expectedId)`。补丁:`LinearTurnEngine.dispatchParallel` L584-L611 增 2 boundary sentinel guard(null-result 替换 + wrong-id 替换)+ **private static `dispatchCancelledResult(String toolUseId, String content)`** 5 行 helper 复用 Story #050 exception-path 同 sentinel 模式(`new ToolResult(toolUseId, "[LINGS-L04] " + content, true);` 复用 ToolResult 既有 4-field ctor)+ **`LINGS_L04 = "LINGS-L04"`** `PARALLEL_DISPATCH_RACE`(LlmProvider 域 L 段 4 号,与 Story #050 L05 `LLM_RESPONSE_MALFORMED` 邻号)。**5 guard × 5 类 race 完整覆盖** —— (1) cancel-before-dispatch boundary (L575-578) / (2) exception boundary (L590-594 catch Throwable) / (3) null-result boundary (L584-588) / (4) wrong-id boundary (L596-602) / (5) cancel-during-dispatch boundary (L609-611) = Story #050 `cancelHandled` try/finally + `interrupt` + Story #052 null/wrong-id 边界全部锁住;**`mvn -pl lingshu-core dependency:tree -Dverbose` R-13 镜像** pre/post md5sum `a7b195f66292ce162aff16ec15aba154` 仅时间戳差异 = **0 binary delta 第 35 次 PASS**(`Objects.equals` + `Arrays.asList` + `Collections.emptyList` + Lombok `@Value` + Java 8 `parallelStream` 已锁 13 项依赖表内 0 新 binary 引入)。**8 net new AC case** 跨 2 文件(`LinearTurnEngineDispatchParallelProtocolTest` 6 L1/L2 `dispatchParallel` boundary sentinel 6 段 AC-052-01..06:`nullResult_substitutesSentinelToolUseId` + `wrongIdResult_substitutesByOriginalCallId` + `legitimateResult_preserves` + `mixedShapeArray_passAllBoundarySentinels` + `cancelBeforeDispatch_substitutesSentinelToolUseId` + `streamInterruptedDuringDispatch_substitutesByOriginalCallId` + `LinearTurnEngineProtocolInvariantIT` 2 L2 e2e round-trip 100 tool_use 全 matching tool_result by toolUseId)。**累计 Story 合入:53 → 54**。**0 新 Maven 依赖** / **0 新协议层 java class**(只 1 个新 `LlmErrorCodes.LINGS_L04` 常量 + 5 行 helper)/ **0 新 ErrorCode**(复用 ToolResult 既有 `[LINGS-XX]` 前缀嵌入模式,且 L04 = 新增 ErrorCode,但复用 ToolResult 4-field ctor 0 改 shape)。**关键不变项** —— `LinearTurnEngine` 公开签名不变(只 `dispatchParallel(List<ToolCall>, TurnContext) → ToolResult[]` 内部 L584-L611 段 2 guard + L629 helper,公开方法 0 改动)+ `LlmProvider` SPI 不变 + `ToolResult` 不可变契约不变(`toolUseId` + `content` + `isError` 3 字段,无 ErrorCode)/ `Message` 4 子类契约不变(`Message.ToolResult` 序列化 field shape 0 改动)+ `Tool` SPI 不变 + `ToolExecutor.dispatch()` 5 步流水线不变(§4.10.1 硬规则 2 守住)+ `AgentFactory` SPI 不变(9-Router ctor 不动)+ `AgentConfig` 不可变契约不变(0 字段新增)+ §4.7 PermissionPolicy / AuditLogger / Cost 域 完全兼容 + 9 Slot 体系不变 + 26 字段 AgentConfig schema 不变 + JDK 8 兼容(`Objects.equals` + `Arrays.asList` + `Collections.emptyList` + Lombok `@Value` + Java 8 `parallelStream` 已锁 13 项依赖表内,no `var` / `List.of` / sealed / records);Spring AI `ChatClient.tools().call()` 仍**禁止**使用(§4.10.1 硬规则 2 守住) + ReAct Loop 自实现不变(§4.10.1 硬规则 1 守住);**业务价值** —— **Anthropic 协议层 hard invariant 5×2 boundary 100% 覆盖**(Story #050 exception-path sentinel 之外补 2 类 result-shape 真返回值缺口,Story #053+ 任何新 dispatch 边界可直接复用 `dispatchCancelledResult` helper)/ **zero downstream SPI contract 改动**(McpTransport / remote transport / demo CLI tool 0 改动,只在 `LinearTurnEngine` boundary 加 guard = 契约层 zero pressure)/ **`dispatchCancelledResult` 5 行 helper 复用** 服务 Story #050 exception-path + Story #052 boundary 2 个边界调用 site/ **0 新 binary**(R-13 镜像 md5sum pre == post = 第 35 次 0 binary delta PASS,累计 35 个 R-13 (d) PASS 故事无新增 binary);**修复者** Claude Code(根据用户 2026-10-17 会话反馈「`LinearTurnEngine.dispatchParallel` 缺少 null/wrong-id boundary sentinel 加一下」+「实施吧」,触发本 Story 实施 + 8 case AC 黑盒验证 + R-13 mitigation (d) baseline 镜像 **第 35 次 PASS 0 binary delta**)(Story #052)
- 🛡️ **反验证循环默认开启已上线** — 关闭 Story #051 opt-in 默认 `false` 留下的 99% 业务方踩坑坑:**问题** Story #051 落地验证反逻辑:opt-in 默认 false = 99% 业务方 0 yaml 配置成本享受到 verification-loop 修复,**实测反例** —— 业务方"如果不在用户 Prompt 上加限制 LLM 还是会反复 verify 同路径" + "system prompt 不够啊" + Claude Code 默认 system prompt 反验证守则体感差异;**根因** opt-in 模式 vs business-as-default 错配 —— verification-loop 是 LLM 默认行为,**业务方**为了避免它写一段 Prompt 是反 default,**库**默认开让业务方显式 opt-out 是正解;**补丁** 1 文件 1 行:**`AgentConfig.Instructions.empty()` 工厂方法最后实参 `false → true`**(Lombok `@AllArgsConstructor` 5-field 字段顺序 + 类型 0 改动 + 公开 ctor 签名 0 改动 + 工厂返回值翻转,53 fixture mechanical sync = 0 业务逻辑改动只参数补齐)+ `AgentFactory.toAgentConfig` yml binding `booleanOr` 默认值翻 `true` + demo-product `application.yml` 加 `# anti-verify-loop: false` opt-out 注释(默认已开启,极少数 evaluation harness / debug 场景可显式关掉)+ **2 new test 文件 / 7 net new case** —— `DefaultPromptBuilderDefaultOnTest` 5 L1(`empty_returnsAntiVerifyLoopTrue` AC-053-01 + `emptyBuild_appendsClauseByDefault` AC-053-02 + `explicitFalseBuild_skipsClause` 反向 AC + `explicitTrueBuild_appendsClause` 回归 AC + `emptyBuild_appendsClauseEvenWhenRoleEmpty` 边界 AC)+ `DefaultPromptBuilderYamlOptOutIT` 2 L2 IT(`yamlFalseBinding_skipsClause` AC-053-03 + `yamlDefaultBinding_appendsClause` 反向 AC-053-03);**全 6 AC pass / 0 fail** + R-13 mitigation (d) baseline 镜像 pre/post `mvn -pl lingshu-core dependency:tree -Dverbose` md5sum diff 仅时间戳差异 = **0 binary delta 第 36 次 PASS**(纯 JDK 8 `boolean` primitive + Lombok `@Value` + Jackson `@JsonProperty("anti-verify-loop")` kebab-case 已锁 0 新 binary 引入);`banned-dependencies` enforcer Rule 0: passed;**0 新 Maven 依赖** / **0 新 ErrorCode**(复用 Story #051 已落 `ANTI_VERIFY_LOOP_CLAUSE` 静态常量,default flip 不引入新错误路径)/ **0 新 Java class**;**关键不变项** —— `DefaultPromptBuilder.build(TurnContext)` 公开方法签名不变(纯 default flip,prod body 0 改动;`if (ins.isAntiVerifyLoop() && sys.length() > 0)` 守卫**不变**,只读 ins field 决定是否 append,默认值翻转后 = 默认走 append path)/ `DefaultPromptBuilder` 5-segment 顺序不变(ROLE → INSTRUCTIONS → PROJECT MEMORY → CONVERSATION HISTORY → USER MESSAGE)/ `DefaultPromptBuilder.ANTI_VERIFY_LOOP_CLAUSE` 静态常量不变(Story #051 实证有效文案)/ `DefaultPromptBuilder` INSTRUCTIONS 段 append 守卫不变 / `AgentConfig` 顶层 27 字段不变(0 字段新增,只 `Instructions.empty()` 工厂返回值翻转)/ `AgentConfig.Instructions` Lombok `@AllArgsConstructor` 5-arg ctor 签名不变(字段顺序 + 类型 0 改动)/ `LinearTurnEngine` / `DefaultAgent` / `DefaultToolExecutor` 不变(engine guard 路径完全不动,Story #051 pre-Option-A 4 文件 engine-guard 计划保持撤销)/ `ToolExecutor.dispatch()` 5 步流水线不变(§4.10.1 硬规则 2)/ 9 Slot SPI 体系不变(0 Slot 改动,`antiVerifyLoop` 是 prompt 装饰非 Slot)/ JDK 8 兼容守住(`boolean` primitive + Lombok `@Value` + `Map.getOrDefault` + `String.contains` + `StringBuilder.append` + Jackson `@JsonProperty` kebab-case 已锁 13 项依赖表内,no `var` / `List.of` / sealed / records);Spring AI `ChatClient.tools().call()` 仍**禁止**使用(§4.10.1 硬规则 2 守住)+ ReAct Loop 自实现不变(§4.10.1 硬规则 1 守住);**累计 55 个 Story 合入**(Story #051=53 + #052=54 + #053=55,Story count 54 → 55);**业务价值** —— **LLM 默认 verification-loop 修复 out-of-the-box**(业务方 0 yaml 配置成本,99% 业务方自动享受,SSE trace 步数从 33 步降到 2-3 步,Story #051 实证)/ **opt-out 退路保留**(极少数 LLM evaluation harness / 调试场景可显式 `anti-verify-loop: false`)/ **不引入 engine 复杂度**(Story #051 pre-Option-A 4 文件 engine-guard 计划保持撤销,纯 prompt 层调整,不动 `LinearTurnEngine` / `ToolExecutor` / `DefaultAgent` 任何 engine guard 路径)/ **Story #051 vs #053 边界清晰**(Story #051 = 引入 `ANTI_VERIFY_LOOP_CLAUSE` + `antiVerifyLoop` 字段 + opt-in 默认 false / Story #053 = **默认 flip** `false → true` + opt-out yml 注释,**新增 0 行** 纯参数翻转)/ **测试覆盖完整**(7 case L1/L2 IT 覆盖 5 段决策边界 + 显式 true/false 双向 + yml opt-out binding + yml 默认 binding)/ **第 36 次 R-13 baseline 0 binary delta 镜像 PASS**(pre/post md5sum diff 仅时间戳差异,纯 Java `boolean` 默认值翻转无新 binary 引入);**修复者** Claude Code(根据用户 2026-10-18 会话反馈「但是如果不主动在用户Prompt上加限制还是会重复,说明 system prompt 不够啊」+ Story #051 3-task SSE trace 实证 opt-in 模式下 LLM 默认 verification loop + 用户确认选项「默认 true, opt-out 退路」+ Story #052 PR #87 已合(commit 6a1d61b)+ 本 Story #053 spec/plan/tasks 三件套落地,触发本 Story 实施 + 7 case AC 黑盒验证 + R-13 mitigation (d) baseline 镜像 **第 36 次 PASS 0 binary delta**)(Story #053)

- 📡 **DefaultAgent.run() 实时流式已上线** — `DefaultAgent.run(String)` 从 Story #001 in-line drain-and-replay(`Subscriber` 同步收集到 `ArrayList` 全部 200 字段 final 落 `BuildContext` 一次性 replay)替换为 **hot lazy `LiveRunPublisher`** private static final inner class:`run(String)` 返回 `Publisher<AgentEvent>` 而**不**调 `engine.runTurn`(lazy,直到首次 `subscribe()` 才提交;`AtomicReference<Subscriber<? super AgentEvent>>` + `AtomicBoolean subscribed` 守卫,违反时通过 `Subscriber.onError(IllegalStateException)` per Reactive §2.2/§3.4 — 不抛 out of `subscribe()`)+ `subscribe()` 把 `engine.runTurn(ctx, subscriberBridge)` 提交到 per-Agent daemon cachedThreadPool(`Executors.newCachedThreadPool(daemonFactory("lingshu-agent-live"))` + per-instance `AtomicInteger` 计数 → 线程名 `lingshu-agent-live-N` 与 `lingshu-tool-N` / `anthropic-llm-io-N` 风格对齐)+ `subscriberBridge.onNext(e)` 在 requested > 0 时 `requested.decrementAndGet()` 后调 `sub.get().onNext(e)`,否则 `LockSupport.parkNanos(50ms)` slice 等 1s park timeout 触发 cancel(`CancellationException` 走 sub.get().onError)+ `cancel()` 翻 `volatile boolean cancelled` + `LockSupport.unpark(parkingThread)` 唤醒;`request(long n)` Reactive §3.9 guard:`if (n <= 0)` 投 `IllegalArgumentException` 嵌 `non-positive request signal per §3.9`,`requested.addAndGet(n)` + 唤醒 parkingThread;`onError(t)` / `onComplete()` 从 engine 直接通过 sub.get() 投递(§2.7 串行保证);**4 反向 AC 锁住 sync 路径不变** —— `runBlocking` + `continueWithUserMessage` + `continueWithUserMessageBlocking` 三个方法体 0 改动(`DefaultAgentRunBlockingUnchangedTest` 4 L1:AC-049-08 runBlocking 返 RunResult finalText/stopReason/usage/turns/elapsedMillis 与 v1.5.59 字节级一致 / AC-049-09 continueWithUserMessageBlocking session append 2 次(continueWithUserMessage + buildContext 双重 append 守恒)+ engine 调 1 次不走 reactive 路径 / AC-049-10 runBlocking 不提交到 liveExecutor(`Thread.enumerate` 找 `lingshu-agent-live-` 线程数 before == after == 0)/ AC-049-11 2 线程并发 runBlocking 独立不污染)+ **7 reactive AC 锁住新路径** —— `DefaultAgentLiveStreamingTest` 7 L1:AC-049-01 run() 后 engine.invocations == 0 直到 subscribe() 触发(lazy)/ AC-049-02 subscribe 后 engine 跑在 `lingshu-agent-live-N` daemon 线程 + subscribe caller 仍是 main 线程(executor offload)/ AC-049-03 5 个 50ms 间隔 TextDelta 在 200ms+ 内串行到达(no buffering 关键证据 / AC-049-04 第二次 subscribe 投 `IllegalStateException` 嵌 `single subscriber` per §2.2/§3.4 / AC-049-05 cancel 后不再 onNext 投递 / AC-049-06 0 request 时 park 等 + request(1) 后恰好 1 event onNext / AC-049-07 engine 抛 RuntimeException → sub 收 onError 且 onComplete **不**触发(Section 2.4 序列))。**关键不变项** —— `Agent.run(String)` SPI 公开签名不变(`Publisher<AgentEvent> run(String)` 0 改动,只换返回类型 impl)+ `Agent.runBlocking` / `continueWithUserMessage` / `continueWithUserMessageBlocking` 公开签名不变 + `BufferedPublisher` 保留给 sync 路径用 + `ChatController` 0 行修改(demo-product SSE 消费路径完全不动)+ `ToolExecutor.dispatch()` 5 步流水线不变(§4.10.1 硬规则 2 守住)+ `AgentConfig` 不可变契约不变(0 字段新增)+ `AgentFactory` SPI 不变(@Autowired 9-Router ctor 不动)+ `LinearTurnEngine` 公开签名不变(`runTurn(ctx, Subscriber)` 不变,只 consumer 在 `execute()` 内部通过 `LiveRunPublisher` subscriber bridge 投递)+ `Message` 4 子类契约不变(Story #046 删除 `Message.ToolUse` 已落) + §4.7 PermissionPolicy / AuditLogger / Cost 域 完全兼容 + 9 Slot 体系不变 + 24 字段 AgentConfig schema 不变 + JDK 8 兼容(`AtomicBoolean.compareAndSet` + `AtomicLong.addAndGet` + `AtomicReference<Thread>` + `LockSupport.parkNanos` + `Executors.newCachedThreadPool(daemonFactory)` + `AtomicInteger` 全 JDK 8 内置,no `var` / `List.of` / sealed / records);**LLM 流式首 token NFR P50 ≤ 1.5s 端到端真触达 demo-product**(Story #027b SSE parser 在 `AnthropicLlmProvider.doPostStream` 把非流式替换为 SSE 文本流式,本 Story `LiveRunPublisher` 把 Story #001 一次性 200 字段 final replay 替换为 hot lazy reactive path,SSE event 在 emitter 端的 `AnthropicLlmProvider.doPostStream` → `LinearTurnEngine` 主循环 → `LiveRunPublisher.subscriberBridge.onNext` → `DefaultAgent.run` 入口 subscriber → ChatController SSE consumer 端到端 latency P50 ≤ 1.5s 真落地,dsh §14.15.1 NFR 兑现)+ **0 新 Maven 依赖** + **0 新 ErrorCode** + **R-13 mitigation (d) baseline 镜像 pre/post `mvn -pl lingshu-core dependency:tree` md5sum 仅时间戳差异** = **0 binary delta 第 32 次 PASS**(Story #049,750 core + 11 #049 net new + 13 #046 + ... = **780 tests pass / 0 fail / 0 error / 0 skip**,累计 Story 合入:47 → **48**)

---

## 🛠️ 环境要求 / Requirements

> **D5 拍板**(2026-10-06):**JDK 8 编译目标** / **JDK 17+ 运行时**(Spring Boot 3.2.5 硬约束)。

| 维度 | 要求 | 说明 |
|---|---|---|
| **编译目标** | JDK 8(`<source>1.8</source>`) | Spring Boot 3.2.5 父继承 + `<maven.compiler.source>1.8</maven.compiler.source>`;源码兼容 JDK 8 工具链编译,锁了 `record` / `sealed` / `var` / `List.of` / text blocks(JDK 9—15+ 特性)禁用清单 |
| **运行 JRE** | **JDK 17+ 必填** | Spring Boot 3.2.5 硬约束(JDK 17+ class file format + Spring 6 baseline);推荐 Temurin / Zulu / Alibaba Dragonwell / IBM Semeru |
| **构建工具** | Maven 3.6.3+ | 多模块父 POM + 5 子模块;无需 Gradle;`mvn -pl lingshu-core test` 跑核心模块测试 |
| **JDK 矩阵 CI** | JDK 8(compile only)+ JDK 17 / 21(test + verify) | GitHub Actions matrix 自动跑;JDK 17 是缺省 profile |
| **OS** | Linux / macOS / Windows | 跨平台;JDK + Maven 即可,无 native dep |

**锁定的 13 项依赖**(dsh §10.1 / R-13 mitigation (d))—— Spring Boot 3.2.5 / Spring AI 1.0.0-M6 / Lombok 1.18.38 / OpenTelemetry 1.32.0 / reactive-streams 1.0.4 / Jackson 2.x / JUnit 5.10.1 / AssertJ 3.24.2 / Mockito 5.8.0 / Awaitility 4.2.0;**新增任何依赖需 RFC + `dependency:tree` CI 卡点 + `banned-dependencies` enforcer build 阶段 fail**(Story 实施 PR body 末尾必须有 `### R-13 dependency:tree 自查` 节)。

**零配置原则**(dsh §7)—— 空 `application.yml` 必须能启动,`AgentConfig` 26 字段全部有默认值(空 yml → 全字段 fallback 默认值 → 启动 → 调 LLM)。

**快速验证**:

```bash
mvn -v                                              # Maven 3.6.3+ / JDK 1.8.0_xxx+ / Java 17+ vendor
git clone https://github.com/lingshu-ai-agent/lingshu.git
cd lingshu
mvn -pl lingshu-examples/demo-empty spring-boot:run # 应当 30 秒内启动,无 application.yml 也能跑
```

---

## 📦 Installation

> **D2 拍板**(2026-10-06):发布渠道 = **GitHub Packages**(规避 Sonatype/JIRA 首次发布 1—3 工作日审核阻塞)。**代价**:consumers 必须在 `~/.m2/settings.xml` 配一个 `<server>`(username=`x-access-token`,password=GH PAT)才能拉工件 —— 没有匿名下载路径。

### Step 1 — 在你的 `pom.xml` 加依赖

```xml
<dependency>
    <groupId>ai.lingshu</groupId>
    <artifactId>lingshu-core</artifactId>
    <version>0.1.0</version>
</dependency>
```

### Step 2 — 声明 GitHub Packages 仓库(repositories)

```xml
<repositories>
    <repository>
        <id>github</id>
        <name>GitHub Packages (LingShu)</name>
        <url>https://maven.pkg.github.com/lingshu-ai-agent/lingshu</url>
        <releases><enabled>true</enabled></releases>
        <snapshots><enabled>true</enabled></snapshots>
    </repository>
</repositories>
```

> 把这段放进**消费方项目**的 pom.xml(`<project>` 直接子节点,不是某个 profile 里)。否则 Maven 找不到 GH Packages 仓库,会报 `Could not find artifact ai.lingshu:lingshu-core:0.1.0`。

### Step 3 — 配 `~/.m2/settings.xml` 的 `<server>` 块

```xml
<settings>
  <servers>
    <server>
      <id>github</id>                              <!-- 必须与 pom.xml <distributionManagement> 的 <id> 一致 -->
      <username>x-access-token</username>          <!-- 固定值,不是你的 GitHub 用户名 -->
      <password>ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</password>  <!-- 替换为你的 GitHub PAT -->
    </server>
  </servers>
</settings>
```

> **`<id>github</id>` 必须与 pom.xml `<distributionManagement>` 里的 `<id>` 一致**(都是 `github`)—— Maven 按 id 匹配 `<server>` 和 deploy repo。<username>**不是**你的 GitHub 用户名,固定填 `x-access-token`(GH Packages 的硬约束)。

### Step 4 — 生成 GitHub PAT(4 步)

1. GitHub → **Settings → Developer settings → Personal access tokens → Fine-grained tokens**
2. **Generate new token** → 名字用
4. **Repository access** → 选择 **Public repositories (read-only)**(只拉包不需要 write,最小权限原则)
4. **Permissions** → **Only select repositories → Package → Read packages**(精确到只读 packages)
5. 生成 → 复制 `ghp_...` 开头 40 个字符 → 填入 Step 3 的 `<password>` 字段

> **Fine-grained token** vs **classic token** —— 都行;fine-grained 权限粒度更细,推荐。如果用 classic token,scopes 勾 `read:packages` 一个即可。

### Step 5 — 验证能拉到工件

```bash
mvn dependency:get -Dartifact=ai.lingshu:lingshu-core:0.1.0
# 应输出:BUILD SUCCESS(jar 下载到 ~/.m2/repository/ai/lingshu/lingshu-core/0.1.0/)
```

> 这一步如果失败,99% 是 Step 2 / Step 3 配置问题(仓库没声明或 `<server>` 没配 / id 不一致)。

### 跳过制品验证(只用 snapshot)

```xml
<dependency>
    <groupId>ai.lingshu</groupId>
    <artifactId>lingshu-core</artifactId>
    <version>0.1.0-SNAPSHOT</version>
</dependency>
```

snapshot 版本号(例如 `0.1.0-SNAPSHOT`)走同一个 GH Packages URL,Maven 默认每小时检查一次新 snapshot。

---

## 🛡️ Stable SPI (since 0.1.0)

> **D4 拍板**(2026-10-06):v0.1.0 起,**9 Slot SPI(11 annotated interfaces)+ PermissionPolicy + MemorySource + AuditLogger = 14 个 `@PublicApi(stable)` 标注接口** 锁定为向后兼容契约,跨 minor release 只加不破。

**Stability 标记** —— 接口或方法带 `@PublicApi(PublicApi.Level.STABLE)` 注解 + Javadoc `@since 0.1.0` 标签。三个等级:

| Level | 含义 | 适用范围 |
|---|---|---|
| `STABLE` | 跨 minor release 向后兼容;破坏性变更需 major bump + 2 版本 deprecation 周期 | 下列 14 个 SPI |
| `INCUBATING` | 试验性;后续 minor release 可能变更 | `@PublicApi(INCUBATING)` 标注的类型 |
| `INTERNAL` | 私有边界;任何 release 都可能改名 / 改签名 | 默认所有未标注类型 |

### 9 Slot SPI(`@PublicApi(stable)` —— 11 annotated interfaces)

| Slot | Interface | Package | Contract version | 责任 |
|---|---|---|---|---|
| 1 LLM | `LlmProvider` | `ai.lingshu.core.slot` | `1.0.0` | 流式调模型 + 增量事件 + 终态响应 |
| 2 Tool | `Tool` | `ai.lingshu.core.slot` | `1.0.0` | 单 Tool 契约(name/desc/schema/execute + `sourceCategory()` 默认方法) |
| 2 Tool | `ToolExecutor` | `ai.lingshu.core.slot` | `1.0.0` | Tool dispatch 5 步流水线入口(§4.10.1 硬规则 2) |
| 3 Sandbox | `RuntimeSandbox` | `ai.lingshu.core.slot` | `1.0.0` | 有界 fs / http / process 能力 |
| 4 Skill | `Skill` | `ai.lingshu.core.slot` | `1.0.0` | Tool 标记接口(`/xxx` 命令 / CLI 拦截) |
| 4 Skill | `SkillSource` | `ai.lingshu.core.slot` | `1.0.0` | Skill 多源自动发现(classpath / directory / git / s3) |
| 5 SessionStore | `SessionStore` | `ai.lingshu.core.slot` | `1.0.0` | Checkpoint 持久化(memory / file / redis / jdbc) |
| 6 Compactor | `Compactor` | `ai.lingshu.core.slot` | `1.0.0` | 历史压缩两步契约(`shouldCompact` + `compact`) |
| 7 PromptBuilder | `PromptBuilder` | `ai.lingshu.core.slot` | `1.0.0` | 5 段 Prompt 装配 + tools 单独字段 |
| 8 FlowEngine | `FlowEngine` | `ai.lingshu.core.runtime` | `1.0.0` | Turn 执行拓扑(LinearTurnEngine / DAG / 外部适配器) |
| 9 A2aTransport | `A2aTransport` | `ai.lingshu.core.slot` | `1.0.0` | 远端 Agent 桥接(5 方法契约) |

### 3 Helper SPI(`@PublicApi(stable)` —— 3 interfaces)

| Helper | Interface | Package | Contract version | 责任 |
|---|---|---|---|---|
| 权限策略 | `PermissionPolicy` | `ai.lingshu.core.slot` | `1.0.0` | Tool 调用 3 决策(Allow / Deny / AskUser)+ `approvalTimeoutSeconds=0` 默认无超时(Claude Code overnight parity) |
| 记忆源 | `MemorySource` | `ai.lingshu.core.slot` | `1.0.0` | `[PROJECT MEMORY]` 单 block 贡献(priority 排序) |
| 审计日志 | `AuditLogger` | `ai.lingshu.core.spi` | `1.0.0` | 结构化事件 emit(console / file / OTel / Kafka / cloud vendor) |

### Compatibility Promise(dsh §16.1 + D4)

- **Major version 内** —— `STABLE` API **只加不破**;`@Deprecated` 至少 2 个 minor release 后才允许移除
- **跨 minor release** —— 可新增方法(默认实现)但**禁止**删除 / 改签名 / 改语义
- **跨 major version** —— 允许破坏性变更,但需发布 migration guide + 1 版本 overlap 窗口
- **每个接口的 `CONTRACT_VERSION` 字段** —— 启动期 `SlotRouter` 反射校验,版本不兼容时启动失败并打印 ErrorCode

### 编写自己的 Plugin / Provider

```java
// 1. 实现 Provider(必须 implements SlotProvider)
public class MyLlmProvider implements LlmProvider {
    @Override public String name() { return "my-provider"; }
    @Override public int priority() { return 10; }   // 胜过默认 priority=0
    @Override public String version() { return "1.0.0"; }  // 必须兼容 1.0.0
    @Override public LlmProvider create(AgentConfig cfg) {
        return new MyLlmProviderImpl(cfg);
    }
}

// 2. yml 配置
// agent:
//   llm:
//     name: my-provider
//
// 3. @Component 自动注册到 Spring 容器(v1.5.28 多 Provider 模式)
```

完整 SPI 契约 Javadoc 见源码(`ai.lingshu.core.slot.*` + `ai.lingshu.core.runtime.FlowEngine` + `ai.lingshu.core.spi.AuditLogger`)。

---

## ⚡ 30 秒上手

### Maven

```xml
<dependency>
    <groupId>ai.lingshu</groupId>
    <artifactId>lingshu-core</artifactId>
    <version>0.1.0-alpha</version>
</dependency>
```

### 第一个 Agent

```java
import ai.lingshu.core.*;
import ai.lingshu.core.engine.*;
import ai.lingshu.core.provider.anthropic.*;

@SpringBootApplication
public class MyFirstAgent {
    public static void main(String[] args) {
        SpringApplication.run(MyFirstAgent.class, args);
    }

    @Bean
    CommandLineRunner run(AgentFactory factory) {
        return args -> {
            Agent agent = factory.create(AgentConfig.builder()
                .flowEngine("linear")
                .llm(LlmConfig.builder()
                    .provider("anthropic")
                    .model("claude-sonnet-4-5")
                    .build())
                .skills(SkillSources.of(
                    ClasspathSource.of("classpath:skills/agent-builtin/"),
                    DirectorySource.of("./skills/")
                ))
                .build());

            RunResult r = agent.runBlocking("用 Java 写一个 Fibonacci 函数");
            System.out.println(r.getFinalText());
        };
    }
}
```

### YAML 配置(可选)

```yaml
agent:
  flow-engine: linear        # linear | google-adk | alibaba-graph | dag
  llm:
    provider: anthropic      # anthropic | openai | gemini | ollama
    model: claude-sonnet-4-5
    api-key: ${ANTHROPIC_API_KEY}
  sandbox:
    policy: strict           # strict | permissive
    runtime: chroot          # chroot | sysbox | seccomp | none
  max-steps: 25
  skills:
    sources:
      - { type: classpath, location: classpath:skills/agent-builtin/ }
      - { type: directory, location: ./skills/ }
      - { type: git,      location: https://github.com/lingshu-ai-agent/lingshu-skill-market }
  tools:
    enabled: true            # 关闭后 LocalToolsAutoConfiguration 跳过 4 Tool 注册
    max-read-bytes: 200000   # ReadTool 单次上限(超过截断 + 末尾 marker)
    max-write-bytes: 1000000 # WriteTool 字节硬 guard(content.length > 此值则拒绝写盘)
  delegate:                  # Story #023 子 Agent 配置;整段缺失 = 跳过 register
    prompts-dir: ./prompts
    types:                     # 必须3项:explore / engineer / reviewer
      explore:
        system-prompt-file: ./prompts/explore.md
      engineer:
        system-prompt-file: ./prompts/engineer.md
      reviewer:
        system-prompt-file: ./prompts/reviewer.md
```

### 调用内置 Tool(Story #019)

LLM 在 ReAct loop 中自动调,无需手写 Tool 注册代码(启动期 `LocalToolsAutoConfiguration` 已自动注入 `Read / Write / Edit / Bash` 4 个 Tool):

```text
// Read — 读取文件(默认上限 200KB,超出自动截断 + 追加 "...[truncated, original N bytes]")
{ "name": "Read",  "input": { "file_path": "src/main/java/MyClass.java" } }

// Edit — 单匹配替换(old_string 必须唯一,多匹配 fail-fast)
{ "name": "Edit",  "input": { "file_path": "...", "old_string": "TODO", "new_string": "FIXED" } }

// Bash — 走 tenant whitelist(per-tenant command-whitelist,默认兜底)
{ "name": "Bash",  "input": { "command": "ls -la", "description": "list workspace" } }
```

---

## 🏛️ 架构:9 个 SPI 槽位

```
                            ┌──────────────────────────────────┐
                            │         FlowEngine (SPI)          │
                            │ LinearTurnEngine | Google ADK | … │
                            └─────────┬──────────────┬───────────┘
                                      │ drives         │ emits events
            ┌─────────────────────────▼────┐  ┌───────▼───────────┐
            │   PromptBuilder  (SPI)       │  │   AgentEvent bus    │
            │   LlmProvider    (SPI)       │  │  (Reactive Streams)│
            └──────────────────────────────┘  └─────────────────────┘
                                      │
            ┌───────────────────────────▼──────────────────────┐
            │              ToolExecutor (SPI, Story #004)       │
            │  ┌────────────────────────────────────────────┐  │
            │  │   PermissionPolicy → ToolRegistry → Execute │  │
            │  │   dispatchParallel: Semaphore(parallelism) │  │
            │  │   CompletableFuture 池 → 结果按 LLM 顺序回填  │  │
            │  └────────────────────────────────────────────┘  │
            │  Tool SPI  →  McpToolAdapter  →  SkillTool adapter │
            │  Spring AI @AgentTool annotation → SkillTool       │
            └────────────┬───────────────────┬──────────────────┘
                         │ permission        │ runtime
                  ┌──────▼─────────┐  ┌──────▼──────────┐
                  │ PermissionPolicy│  │ RuntimeSandbox  │
                  │   (SPI, model)  │  │  (SPI, system)  │
                  └────────────────┘  └─────────────────┘

            ┌────────────────────────────────────────────────────┐
            │     SessionStore (SPI)  +  Compactor (SPI)         │
            │     持久化历史 / 滑动窗口 / 摘要压缩                │
            └────────────────────────────────────────────────────┘

            ┌────────────────────────────────────────────────────┐
            │     A2aTransport (SPI, Story #009 ✅ AC-10)         │
            │     Agent-to-Agent RPC + AgentCard discovery        │
            │     GET /.well-known/agent.json (A2A v1.0)         │
            └────────────────────────────────────────────────────┘
```

每个 SPI 槽位的 `SlotRouter` 在启动期按 `Provider.version()` 校验 Slot 契约兼容性(Story #003),MAJOR 不匹配抛 `LINGS-S05` 启动失败 —— **杜绝运行时静默降级**。详见 [docs/concepts/slots.md](https://github.com/lingshu-ai-agent/lingshu-docs/blob/main/docs/concepts/slots.md) 与 [docs/concepts/spi-versioning.md](https://github.com/lingshu-ai-agent/lingshu-docs/blob/main/docs/concepts/spi-versioning.md)。

---

## 🔌 SPI 替换示例

> **Story #003 重要更新**:LingShu 选择 **Spring Boot SPI** 而非 Java SPI / OSGi / ClassLoader 隔离(详见 [docs/concepts/spi-vs-osgi.md](https://github.com/lingshu-ai-agent/lingshu-docs/blob/main/docs/concepts/spi-vs-osgi.md))。
> 所有 Provider 通过 `@Component` 或 `@AutoConfiguration` + `@Bean` 注册,**禁止**使用 Google auto-service 的 `@AutoService` 注解(那是 Java SPI,与我们的决策冲突)。

```java
// 1. 替换 FlowEngine:接入 Google ADK(Story #003 校验 version() 兼容性)
@Component
public class GoogleAdkFlowEngineProvider implements FlowEngineProvider {
    @Override public String name() { return "google-adk"; }
    @Override public int priority() { return 100; }
    @Override public String version() { return "1.0.0"; }   // 必须与 FlowEngine 契约版本 MAJOR 一致
    @Override public FlowEngine create(AgentConfig cfg) { return new GoogleAdkFlowEngine(cfg); }
}

// 2. 替换 LlmProvider:接入 OpenAI
@Component
public class OpenAiLlmProviderProvider implements LlmProviderProvider {
    @Override public String name() { return "openai"; }
    @Override public int priority() { return 10; }
    @Override public String version() { return "1.0.0"; }
    @Override public LlmProvider create(AgentConfig cfg) {
        return new OpenAiLlmProvider(cfg.getLlm());
    }
}

// 3. 加自定义 Tool(不需要 Provider,直接 @Component)
@Component
public class DbQueryTool implements Tool {
    @Override public String name() { return "db_query"; }
    @Override public String description() { return "Execute read-only SQL"; }
    @Override public JsonNode inputSchema() { /* JSON Schema */ }
    @Override public ToolResult execute(ToolCall call, ToolExecutionContext ctx) {
        // 你的实现 —— 异常会被 DefaultToolExecutor 翻译成 ToolResult.error,
        // 不会让引擎循环崩溃(Story #004 / FR-007/FR-008)
    }
}
```

**YAML 切换 Provider**(Story #003 多 Provider 模式,改 yaml 不改代码):

```yaml
agent:
  llm:
    provider: openai        # 从 anthropic 切换到 openai,无需 exclude classpath
    model: gpt-4o
  flow-engine: google-adk   # 切到 ADK
  sandbox:
    policy: strict
```

只要把以上类打进 jar,放到 classpath,Spring 启动时 SlotRouter 按 `name()` 路由 + `version()` 校验,**零配置**。

---

## 📦 模块结构

```
lingshu/
├── lingshu-core/                 ← 核心 API + ReAct 引擎
│   ├── engine/                  ← LinearTurnEngine
│   ├── loop/                    ← ReAct step state machine
│   ├── prompt/                  ← PromptBuilder
│   ├── llm/                     ← LlmProvider SPI
│   ├── tool/                    ← Tool SPI + McpToolAdapter
│   ├── skill/                   ← Skill SPI + SkillTool adapter
│   ├── sandbox/                 ← PermissionPolicy + RuntimeSandbox
│   ├── session/                 ← SessionStore + Compactor
│   ├── event/                   ← AgentEvent types
│   └── flow/                    ← FlowEngine SPI
├── lingshu-boot-starter/         ← Spring Boot 启动器
├── lingshu-providers/
│   ├── lingshu-anthropic/        ← Anthropic Claude
│   ├── lingshu-openai/           ← OpenAI / GPT
│   ├── lingshu-ollama/           ← 本地 Ollama
│   └── lingshu-mcp-client/       ← MCP server 适配
├── lingshu-adapters/
│   ├── lingshu-google-adk/       ← 接入 Google ADK 作为 FlowEngine
│   └── lingshu-alibaba-graph/   ← 接入 Alibaba Graph 作为 FlowEngine
├── lingshu-cli/                  ← CLI 入口(Story #017):run/resume/serve/doctor/config
└── lingshu-bom/                  ← Maven BOM
```

---

## 🧪 跑通一个最小 Demo

### Story #001 zero-config-bootstrap(空 yml 启动 + 首 token)

```bash
git clone https://github.com/lingshu-ai-agent/lingshu.git
cd lingshu
export ANTHROPIC_AUTH_TOKEN=<your-key>
export ANTHROPIC_BASE_URL=https://api.anthropic.com        # 或代理路径如 https://your-proxy/anthropic
mvn -pl lingshu-examples/demo-empty -am spring-boot:run
```

`application.yml` 故意为空,所有 27 个 `AgentConfig` 字段由 `AgentConfigDefaults.defaults()` 提供。
首次 LLM token 在 ~5s 内返回,stderr 无 ERROR(AC-01-1)。

### Story #002 identity-instructions-memory(业务三件套 + 5 段 Prompt 装配)

```bash
cd lingshu
export ANTHROPIC_AUTH_TOKEN=<your-key>
export ANTHROPIC_BASE_URL=https://api.anthropic.com        # 或代理路径
mvn -pl lingshu-examples/demo-engineer -am package -DskipTests
java -jar lingshu-examples/demo-engineer/target/demo-engineer-0.1.0-SNAPSHOT.jar "你是做什么的"
```

`demo-engineer` 演示 AC-09 黑盒契约:
- 4 个 `MemorySourceProvider` 自动注册(`identity` / `project-claude-md` / `user-claude-md` / `project-tree`)
- `DefaultPromptBuilder` 5 段装配:`[ROLE] / [INSTRUCTIONS] / [PROJECT MEMORY] / [CONVERSATION HISTORY] / [USER MESSAGE]`
- 缺失文件静默跳过,首 token ≤ 30s

**黑盒测试(无需 API key)**:
```bash
mvn -pl lingshu-examples/demo-engineer -am test -Dtest=BlackBoxVerificationTest
```

### Story #017 cli-entrypoint(5 子命令 CLI 入口,dsh §10.3 全落地)

不想写代码?直接用 CLI:

```bash
# 跑一次(等价 demo-empty 的最小入口)
mvn -pl lingshu-cli spring-boot:run \
    -Dspring-boot.run.arguments="run --prompt '用 Java 写一个 Fibonacci 函数'"

# 起 A2A 服务(等价 demo-a2a)
mvn -pl lingshu-cli spring-boot:run \
    -Dspring-boot.run.arguments="serve --port 18099"
# 另开终端:
curl -sf http://127.0.0.1:18099/.well-known/agent.json | jq .

# 自检环境(打印 7 Router + 9 Slot 状态)
mvn -pl lingshu-cli spring-boot:run \
    -Dspring-boot.run.arguments="doctor"

# 看有效配置(合并 yaml + 默认值)
mvn -pl lingshu-cli spring-boot:run \
    -Dspring-boot.run.arguments="config --print-effective"
```

完整 CLI 子命令矩阵与 ErrorCode 详见下方 "Story #017 cli-entrypoint" 段。

### 所有 16 个 demo 工程索引(Stage A 骨架,2026-09-25 落盘)

按主题合并 ~ 14 个新 demo(Story #003—#025b 全部覆盖),每个 demo 跑通 Spring 上下文 + 至少 1 个 `BlackBoxVerificationTest` skeleton test;完整 AC 黑盒留 Stage B。#025 / #025b 是端到端 product demo(非 Stage A skeleton),需 `spring-boot:run` 起服务实测。

| Demo | Story 覆盖 | 验证内容(Stage A) | 跑通命令 |
|---|---|---|---|
| `demo-empty` | #001 | Spring main 启动 + AgentFactory.create | `mvn -pl lingshu-examples/demo-empty -am spring-boot:run` |
| `demo-engineer` | #002 + #024 | 4 MemorySource wiring + 5 段 Prompt + `[TOOL SCHEMAS]` 段(`prompt.getTools()` 镜像 registry) | `mvn -pl lingshu-examples/demo-engineer -am test` |
| `demo-local-tools` | #019 | 4 Tool(Read/Write/Edit/Bash)从 `LocalToolsAutoConfiguration` 注册到 `ToolRegistry` | `mvn -pl lingshu-examples/demo-local-tools -am test` |
| `demo-spi` | #003 | `SlotRouter` 多 Provider + `AgentFactory.description()` 9 行 | `mvn -pl lingshu-examples/demo-spi -am test` |
| `demo-parallel` | #004 | `LinearTurnEngine.dispatchParallel` 4 tool 并行 | `mvn -pl lingshu-examples/demo-parallel -am test` |
| `demo-cancellation` | #005 | `CancellationToken` 三层贯通 + 200ms AC-04 | `mvn -pl lingshu-examples/demo-cancellation -am test` |
| `demo-tenants` | #006 | `TenantContext` ThreadLocal + 4 维隔离 | `mvn -pl lingshu-examples/demo-tenants -am test` |
| `demo-reload` | #007 | `YamlWatcher` mtime 轮询 + `AtomicReference` config swap | `mvn -pl lingshu-examples/demo-reload -am test` |
| `demo-max-steps` | #008 | `MaxStepsExceeded` 事件发射 + 5 终止路径 | `mvn -pl lingshu-examples/demo-max-steps -am test` |
| `demo-compactor` | #018 | `TruncatingCompactor` + `CompactorRouter` token 减少 | `mvn -pl lingshu-examples/demo-compactor -am test` |
| `demo-a2a` | #009 + #009a—#009e | `A2aServer` JDK HttpServer + `/.well-known/agent.json` 黑盒 | `mvn -pl lingshu-examples/demo-a2a -am test` |
| `demo-skill` | #020a + #020b + #020c | `SkillSourceRouter` classpath+directory + `SkillCommandDispatcher` cli 模块 | `mvn -pl lingshu-examples/demo-skill -am test` |
| `demo-mcp` | #021a + #021b + #021c | `McpServerConnectionFactory` 3 transport(STDIO/SSE/STREAMABLE_HTTP)dispatch | `mvn -pl lingshu-examples/demo-mcp -am test` |
| `demo-delegate` | #022 + #023 + #024 | `@AgentTool` + `DelegateTool` Task + `SubAgentType` enum 3 值 | `mvn -pl lingshu-examples/demo-delegate -am test` |
| `demo-product` | #025 | HTTP SSE chat 产品:8 features(Spring Boot + SSE + ReAct 事件流 + `@AgentTool` + SKILL.md Skill + MCP stdio 子进程 + 内存会话 + Hot-reload 配置) | `mvn -pl lingshu-examples/demo-product -am spring-boot:run` |
| `demo-product-a2a-server` | #025b | 跨 JVM translate demo(9090 端口)与 `demo-product`(8080)互通:`RemoteAgentTool` + `HttpJsonRpcA2aTransport`;`DemoProductA2aServerApplication` 自起 JDK `HttpServer` 跑简化 JSON-RPC + 调本地 ToolRegistry(stock `A2aServer` 不接 dispatch 的事实绕过) | `mvn -pl lingshu-examples/demo-product-a2a-server -am spring-boot:run` |

**全量回归**(Stage A 14 demo 一次性跑,1 分钟级;`demo-product` / `demo-product-a2a-server` 为 product demo 需独立启服务):

```bash
cd lingshu-examples
mvn test
```

实测:`Tests run: 56, Failures: 0, Errors: 0, Skipped: 0`(demo-empty 0 + demo-engineer 3 + demo-local-tools 5 + 11 个新 demo 48)。

### Story #003 spi-slot-router(`Provider.version()` + `SlotRouter` 兼容性校验)

```bash
mvn -pl lingshu-core test -Dtest=SlotRouterCompatTest
mvn -pl lingshu-core test -Dtest=VersionTest
mvn -pl lingshu-core test -Dtest=ProviderInitExceptionTest
```

`SlotRouterCompatTest`(7 case)+ `VersionTest`(24 case)+ `ProviderInitExceptionTest`(5 case)覆盖:
- 启动期按 `Provider.version()` 与 Slot `CONTRACT_VERSION` MAJOR 比对 —— 不匹配抛 `LINGS-S05` **启动失败**,杜绝运行时静默降级(AC-02)
- `LinkedHashMap` 保留用户配置顺序(同 `agent.prompt.memory-sources` 输入一致),priority 只用于同名竞争(AC-08)

### Story #004 tool-parallel-dispatch(`LinearTurnEngine.dispatchParallel`)

```bash
mvn -pl lingshu-core test -Dtest=LinearTurnEngineParallelDispatchTest
```

`LinearTurnEngineParallelDispatchTest` 跑 AC-03 黑盒契约(无需 API key):
- 4 个独立 Tool 各 sleep 1s,`tool.parallelism: 4` → wall-clock **≤ 1.3s**(实测 1011ms)
- 相比 4s 串行 baseline,加速比 **≥ 3.0×**(实测 3.96×)
- `DefaultToolExecutor` 把异常翻译成 `ToolResult.error`,引擎循环不因单 Tool 崩溃(FR-007/FR-008)
- 结果按 LLM-return 顺序回填 history,不按完成顺序(FR-003)

**YAML 调并行度**:
```yaml
agent:
  tool:
    parallelism: 8          # 同时执行最多 8 个 Tool;1 = 串行;0 = 不限
    timeout-seconds: 30     # 单个 Tool 超时(0 = 不超时)
```

### Story #005 cancellation-token(协作式取消 + 三层贯通 + AC-04 200ms)

dsh §14.12 N12: FlowEngine / ToolExecutor / LlmProvider 三层共用同一个 `CancellationToken`,Ctrl-C / JVM shutdown hook / turn 超时 / 编程式 `markDone` 4 种触发源都通过它发出信号。

**关键不变量**:
- `TurnContext.cancellation() == ToolExecutionContext.cancellation()`(共享引用,非 equals)
- `DefaultTurnContext.createWithBroadcast` 自动把 turn 的 token 注册到 `AgentFactory.BROADCAST_REGISTRY`
- `AgentFactory.@PostConstruct registerJvmShutdownHook` 在 JVM 关停时调 `broadcastCancel()`,所有 in-flight turns 在 AC-04 200ms 内退出
- `LinearTurnEngine` 用 200ms 轮询预算(`waitForLlm` + `waitForTool`),即使 LLM / Tool 永远不返回也能在 200ms 内感知取消

```bash
mvn -pl lingshu-core test -Dtest='CancellationTokensTest,CancellationTokenSharingTest,LinearTurnEngineCancellationIT,AgentFactoryBroadcastCancelTest'
```

**测试覆盖**(23 case / 4 类):
- `CancellationTokensTest`(8 case)— AtomicBoolean 幂等 fire / CopyOnWriteArrayList 安全迭代 / per-callback 异常隔离 / 并发注册 stress
- `CancellationTokenSharingTest`(6 case)— `==` 身份共享 / 多 turn 隔离 / 4-arg 构造器 back-compat
- `LinearTurnEngineCancellationIT`(3 case)— **AC-04 黑盒**(实测 cancel→exit **0ms**,预算 200ms)/ 预取消 / mid-tool-dispatch 取消
- `AgentFactoryBroadcastCancelTest`(6 case)— broadcast 全发 / 幂等 / `activeTurnCount` 反射 / 未注册 turn 忽略

**AC-04 黑盒输出**:
```
[AC-04] cancel→exit elapsedMs=0 (budget=200)
```

**LlmProvider 取消内部轮询**(US3)推迟到 Story #005b — 不阻塞 AC-04:200ms `waitForLlm` 预算 + 引擎侧轮询已覆盖 N12 三层贯通契约。

### Story #006 multi-tenant(`TenantContext` ThreadLocal + 配置/Session/Sandbox/Cost 四维隔离 AC-05)

dsh §14.9 N9:多租户隔离是 B2B SaaS 化刚需 —— 一个 JVM 实例同时服务多个客户,每客户有独立 memory dir / sandbox whitelist / cost budget / session namespace,互不可见。

**核心交付**:
- `TenantContext` ThreadLocal **嵌套栈** + `snapshot/runWithSnapshot` 显式跨线程传递(主动放弃 `InheritableThreadLocal`,避免线程池复用场景下"上一个任务的 tenant 泄漏到下一个任务")
- `AgentConfig.tenants` 新字段(28th)+ `TenantsConfig.validate()` 启动期 fail-fast(错误码 `LINGS-C02`)
- `TenantConfigProvider` SPI + `YamlTenantConfigProvider` 默认实现(`@Component("tenantConfigProvider_yaml")`,§5.28 多 Provider 模式)
- `TenantAwareCostTracker` per-tenant `LongAdder` 桶 + 超预算 `CostBudgetExceededException`
- `DefaultRuntimeSandbox` `process.run` 走 tenant 白名单(全局兜底,单租户 mode 不变)
- `DefaultInMemorySessionStore` session key 加 `tenantId` 前缀(`alice:sess-123` vs `bob:sess-123`)
- `LinearTurnEngine.runTurn` 入口 FR-011 守卫(tenants 已配但无 `TenantContext` → `IllegalStateException` + `LINGS-C02` 提示)

```bash
mvn -pl lingshu-core test -Dtest='TenantContextTest,TenantConfigProviderTest,TenantConfigValidationTest,MemoryPathIsolationTest,CostBudgetIsolationTest,SandboxWhitelistIsolationTest,SessionKeyIsolationTest,TenantIsolationIT'
```

**测试覆盖**(43 case / 8 文件):
- `TenantContextTest`(9 case)— 嵌套栈 / try-finally / snapshot+runWithSnapshot / 跨线程显式传递
- `TenantConfigProviderTest`(5 case)— 多 Provider 优先级 / 空 yml 单租户 fallback
- `TenantConfigValidationTest`(10 case)— 4 项校验(tenantId 格式 / key=value 一致 / dir 必填 / cost>0)+ 14 个 Edge Case
- `MemoryPathIsolationTest`(2 case)— per-tenant `AgentConfig.Memory.claudeMd.project`
- `CostBudgetIsolationTest`(5 case)— alice/bob 独立计数 + 超预算 fail-fast
- `SandboxWhitelistIsolationTest`(6 case)— alice 拒 git / bob 允许 / 单租户 fallback
- `SessionKeyIsolationTest`(5 case)— 同 sessionId 不同物理 bucket
- `TenantIsolationIT`(1 case E2E)— **AC-05 黑盒**(83ms):4 维隔离跨 alice/bob 一次性验证

**YAML 多租户配置**:
```yaml
agent:
  tenants:
    enabled: true
    map:
      alice:
        memory:    { dir: /var/lib/alice }
        sandbox:   { command-whitelist: [ls, cat] }
        cost:      { session-budget-micros: 10000000 }
      bob:
        memory:    { dir: /var/lib/bob }
        sandbox:   { command-whitelist: [ls, cat, git] }
        cost:      { session-budget-micros: 100000000 }
```

**TenantContext 用法**:
```java
TenantContext.runAs("alice", () -> {
    // 业务代码 —— TenantContext.current() == "alice"
    Agent agent = factory.create(cfg);
    return agent.runBlocking("...");
});
// 退出 lambda 后自动 clear(R-02 缓解)

// 跨线程显式传递
String snap = TenantContext.snapshot();
executor.submit(() -> {
    TenantContext.runWithSnapshot(snap, () -> doWork());
});
```

**R-13 dependency:tree 自查**:`diff /tmp/deps-005-baseline.txt /tmp/deps-006-after.txt` → 仅 `[INFO] Total time` 时间戳差异,**0 新依赖**。

### Story #007 yaml-hot-reload(`AgentConfigRegistry` AtomicReference + 5s mtime poll + DefaultAgent freeze AC-06)

dsh §14.8 N8:**YAML 热更无中断** —— Agent 跑 turn T1 时外部修改 `application.yml`(扩 sandbox whitelist / 换 model / 调 `react.max-steps`),T1 全程冻结旧 cfg 引用语义自然隔离;T2 启动立即看到新 cfg。零停机 + 零重启 + 零数据竞争 —— 7×24 长生命周期运维刚需。

**核心交付**:
- `AgentConfigRegistry` `AtomicReference<AgentConfig>` **单写多读 lock-free**(NFR-005:单 publish ≤ 1ms)
- `ConfigChangeListener` SPI + listener 异常不阻断 publish 主流程(异常隔离 + ERROR 日志 + 后续 reader 仍看到新 cfg)
- `YamlWatcher` daemon `ScheduledExecutorService` 5s `Files.getLastModifiedTime` poll(cross-platform stable,**不用** `WatchService` 的 macOS polling fallback 不兼容)
- `AgentFactory.create(cfg, registry)` 新签名 + 旧 `create(cfg)` `@Deprecated`(向后兼容 Story #001—#006)
- `DefaultAgent.run()` 入口一次性 `registry.current()` freeze(Java 引用语义 + `@Value` immutable 字段自然冻结,无锁 / 无 snapshot copy)
- `validateOrThrow` 拒绝破坏性 cfg + rollback 保留旧 cfg + `lastSeen` **不**更新 → 下次 5s 自动重试

**关键不变量**:
- 旧 turn T1 全程持有 cfg1 引用(`assertSame` 验证),即使中途 `registry.publish(cfg2)` 也无影响
- 新 turn T2 入口 `registry.current()` 立即看到 cfg2,无需重启 / cancel / 等待
- 校验失败 / YAML parse 失败 / IOException **不**更新 `lastSeen`,下一次 poll 自动重试(R-03 缓解)
- Listener 抛 RuntimeException → ERROR log + publish **不**回滚,后续 reader 仍看到新 cfg
- Listener 内禁止调 `registry.publish`(重入死循环,契约显式说明)

**测试覆盖**(22 case / 5 文件):
- `AgentConfigRegistryTest`(9 case)— publish 立即 swap / 100 线程并发 `current()` 全看到新 cfg / listener 异常隔离 / listener 重入禁止 / addListener / removeListener / publish null NPE
- `MinimalYamlParserTest`(4 case)— block-style list / flow-style list / 注释与空行 / orphan item 抛错(内联 YAML parser L0 smoke)
- `YamlWatcherTest`(5 case)— mtime 变更触发 reload / invalid YAML 保留旧 cfg / validate 失败保留旧 cfg / `lastSeen` 不更新 / 自动重试
- `InFlightFreezeTest`(2 case)— **AC-06 核心**(T1 freeze + T2 立即生效 + in-flight turn 不被并发 publish 改写)
- `YamlHotReloadIT`(2 case E2E)— **AC-06 黑盒主路径**(T1 跑 ls + 中途 touch yml 加 git + T2 跑 git status + invalid YAML rollback)

```bash
mvn -pl lingshu-core test -Dtest='AgentConfigRegistryTest,YamlWatcherTest,InFlightFreezeTest,YamlHotReloadIT'
```

**ConfigChangeListener 用法**:
```java
@Component
public class MyAuditListener implements ConfigChangeListener {
    @Override
    public void onConfigChange(AgentConfig prev, AgentConfig next) {
        // prev → next 的 diff 审计 / metric 计数 / cache invalidate
        // 不要在 listener 内调 registry.publish(重入死循环,契约禁止)
    }
}
```

**YAML 热更示例**:
```bash
# T1 在跑,sandbox whitelist = [ls, cat]
# 外部运维修改 yml:
vi application.yml    # 追加 git 到 whitelist
:wq
# 5s 内 YamlWatcher poll 检测 mtime 变化 → reload + validate + publish(cfg2)
# T1 全程冻结 cfg1 引用(sandbox 仍只允许 ls / cat,不被中断)
# T2 启动立即看到 cfg2(sandbox 允许 ls / cat / git)
```

**R-13 dependency:tree 自查**:`diff /tmp/deps-006-baseline.txt /tmp/deps-007-after.txt` → **0 new dependencies**(`AtomicReference` / `ScheduledExecutorService` / `Files` / SnakeYAML 已在 baseline)。

**0 新增 ErrorCode**(沿用 Story #001 `LINGS-C02` 验证错误码;R-03 缓解在 `validateOrThrow` 已有路径)。

### Story #008 react-max-steps(`LinearTurnEngine` `maxStepsHit` 守卫 + `MaxStepsExceeded` 事件发射 AC-07)

dsh §0.4 AC-07:**ReAct 上限** —— yml `agent.react.max-steps: 3` + LLM mock 每次只返 tool call(不返 final answer)→ 第 3 步之后发 `MaxStepsExceeded(3, totalUsage=...)` 事件,然后 turn 正常 `done()`,**不**无限循环。防止 LLM 死循环 token 失控 + 7×24 长生命周期运维刚需。

**核心交付**:
- `LinearTurnEngine.runTurn` 新增 `boolean maxStepsHit = false` 守卫标志(try 之前声明)
- for-loop 内 L174 `ObservationAppended` 之后新增 `if (step == maxSteps) maxStepsHit = true;`(仅当 step == maxSteps 且无 break 退出时触发)
- for-loop 之后 / `TurnCompleted` 之前新增守卫 + last 联合判定:`if (maxStepsHit && last.getToolCalls() 非空) sink.onNext(MaxStepsExceeded(maxSteps, totalUsage))`
- `TurnCompleted.reason` 仍为 `last.getStopReason()`(**不**引入新 `StopReason.MAX_STEPS` enum 值 — 保持 Story #005 cancellation 状态机 + Story #010 OTel metric 标签向后兼容)
- `MaxStepsExceeded.totalUsage` 与 `TurnCompleted.usage` **同一对象引用**(`Usage` `@Value` 不可变,NFR-002 0 内存分配)

**关键不变量**:
- 仅当 for-loop 因 `step == maxSteps` 自然 bound 结束(**无** `break`(ctx.done() / no-tool-call)/ `return`(cancellation / waitForLlm cancelled)/ `catch`(RuntimeException))**且**最后一次 LLM 响应仍含 tool calls 时,发射 `MaxStepsExceeded`
- 事件顺序固定:`MaxStepsExceeded` → `TurnCompleted`(FR-005 强约束,`assertSame(usage)` 验证)
- `AgentEvent.MaxStepsExceeded(maxSteps, totalUsage)` 类定义、字段、Lombok `@Getter` **不**改(`AgentEvent.java` L107-110)
- `StopReason` enum **不**改(`StopReason.java` L8-21,6 值 END_TURN / TOOL_USE / MAX_TOKENS / COMPACTED / CANCELLED / ERROR,无 `MAX_STEPS`)
- `AgentConfig.reactMaxSteps` 默认 50,`0` = 不限被 `AgentFactory.create()` 启动期校验 `LINGS-C02` 拒绝(`L233-235` 复用,**0 新增** ErrorCode)
- Story #007 兼容:在飞 turn 冻结 `reactMaxSteps` 引用,中途 `registry.publish(newCfg)` 不影响(EC-9 自然兼容)

**5 终止路径分支全覆盖**:

| 路径 | 触发条件 | 发 `MaxStepsExceeded`? | `TurnCompleted.reason` |
|---|---|---|---|
| **A**(自然 bound + last 含 tool calls)| for-loop step == maxSteps 无 break | ✅ **是** | `TOOL_USE`(LLM 最后响应是 TOOL_USE)|
| **A'**(自然 bound + last 无 tool calls)| break at L162-165 在 step == maxSteps | ❌ 否 | `END_TURN` |
| **B**(break 无 tool calls)| step < maxSteps + break | ❌ 否 | `END_TURN` |
| **C**(break ctx.done)| step < maxSteps + break | ❌ 否 | `END_TURN` |
| **D**(cancellation return)| `cancellation().isCancelled()` | ❌ 否 | `CANCELLED` |
| **E**(exception catch)| RuntimeException in try | ❌ 否 | `ERROR` |

**测试覆盖**(11 case / 1 文件):
- `MaxStepsGuardTest`(11 case):
  - `US1-AS1`:`maxSteps3_llmAlwaysToolCall_emitsMaxStepsExceeded_after3rdStep` —— 主路径 11 事件含 `MaxStepsExceeded(3)`
  - `US1-AS2`:`maxSteps5_llmEndTurnAfter3Steps_noMaxStepsExceeded` —— 自然 END_TURN 路径不发
  - `US1-AS3`:`maxSteps1_llmToolCall_emitsMaxStepsExceeded_after1stStep` —— 极小值边界
  - `US1-AS4`:`maxSteps0_factoryValidateThrows_LingsC02_neverEnterEngine` —— 反射测 `AgentFactory.validate()` 抛 `IllegalArgumentException`
  - `US2-AS1`:`maxSteps2_llmThrowsFirstStep_errorPathNoMaxStepsExceeded` —— 异常路径不发
  - `US2-AS2`:`maxSteps3_toolExceptionMidPath_stepCountContinues_maxStepsHitFinally` —— tool 异常翻译为 `ToolResult.error` 不影响 step 计数
  - `US3-AS1`:`maxStepsExceeded_eventFields_intAndUsage` —— 反射验证字段类型
  - `US3-AS2`:`stopReason_enumHasNoMaxStepsValue` —— 反射验证 enum 无 `MAX_STEPS`(SemVer 守护)
  - `US3-AS3`:`maxSteps3_eventOrder_maxStepsBeforeTurnCompleted_usageRefSame` —— 顺序 + 引用语义 `assertSame`
  - `EC-5`:`maxSteps10_cancellationMidPath_noMaxStepsExceeded` —— 取消优先
  - `EC-7`:`maxSteps3_llmEndTurnAtLastStep_naturalEndTurn_noMaxStepsExceeded` —— break 优先于守卫

```bash
mvn -pl lingshu-core test -Dtest=MaxStepsGuardTest
```

**累计测试**:**291 case**(Story #008 187 + Story #009 +17 + Story #009a +28(23 a2a-client unit + 2 E2E + 5 core router / split 192+25)+ Story #017 +30 + Story #009a-009 demo-engineer 黑盒 2 case 修复 + Story #009b +25(8 registry + 7 transport + 4 provider + 3 autoconfig + 3 a2a-server hooks))全绿,0 regression。

**R-13 dependency:tree 自查**:`diff /tmp/deps-008-baseline.txt /tmp/deps-009-after.txt` → 仅 `[INFO] Total time` 时间戳差异 + 新模块 `lingshu-a2a-server` 4 个直接依赖(`lombok` / `spring-boot-autoconfigure` / `junit-jupiter` / `assertj-core`),**全部已在 dsh §10.1 锁定 13 项 / Spring Boot BOM 中**,0 新依赖。

**2 新增 ErrorCode**:
- `LINGS-T02`(T 域 / Tool-A2A 配置)— `AgentConfig.identity.name` 空 / 空白 / `AgentConfig == null` 触发,`LocalAgentCardGenerator.generate()` 启动期校验
- `LINGS-S06`(S 域 / Slot-SPI)— 端口占用 / 越界 / `HttpServer.create()` 失败触发,`A2aServer.start()` 启动期 fail-fast

---

### Story #009 a2a-agent-card(`LocalAgentCardGenerator` + JDK `HttpServer` + `GET /.well-known/agent.json` AC-10)

dsh §0.4 AC-10:**A2A AgentCard 自动生成** —— 服务端暴露 `GET /.well-known/agent.json`(A2A v1.0 §2.1 固定路径),返回 `AgentCard` 包含 `name` / `description` / `version` 字段,且**直接**来源于 `cfg.getIdentity()` / `cfg.getIdentity().getRole()` / 内置常量,无需额外 yml 配置。dsh §5.6.8 `LocalAgentCardGenerator` 黑盒验证。

**Narrow scope(AC-10 only)**:`LocalAgentCardGenerator`(cfg → AgentCard transformer)+ 嵌入式 HTTP server(JDK 内置 `com.sun.net.httpserver.HttpServer`,0 新 Maven 依赖)+ 最小 `AgentCard` 数据类型(Lombok `@Value` + Jackson)。**Out-of-Scope**:**#009a**(GrpcA2aTransport / A2aTransportRouter / AgentCardCache / AgentConfig.A2a.grpcTarget / cardTtl 扩展)+ **#009b**(InProcessA2aTransport / 同 JVM 直接方法调用 / 0 额外依赖)+ **#009c**(HttpJsonRpcA2aTransport / RemoteAgentTool / @Component implements Tool)+ **#009d**(RemoteAgentSchemaBuilder 启动期扫 `AgentCard.skills[]` 生成 `ToolSpec` list / 0 额外依赖)。dsh §5.6.3.2 只显式锚定 #009a (Grpc) + #009b (InProcess);#009c / #009d 由本仓库 Story 边界检查(CLAUDE.md §11 #4 ≤ 5 文件 / ≤ 3 ErrorCode)反推拆分。

- 新模块 `lingshu-a2a-server`(独立打包,零 Maven 依赖增量):`AgentCard.java` + `LocalAgentCardGenerator.java` + `A2aServer.java` + `A2aServerAutoConfiguration.java` + `LingsA2aServerException.java` + `META-INF/spring/...AutoConfiguration.imports`
- `A2aServer` Spring `@Bean(initMethod="start", destroyMethod="stop")` 生命周期(避开 `@PostConstruct` / `@PreDestroy` javax.annotation 依赖,符合 R-13)
- `AgentConfig.A2a` 嵌套类(host + port + `defaults()`)穿透到 `AgentConfigDefaults` + `AgentFactory` + 15 个测试 fixture
- 3 handler 内嵌类:`AgentCardHandler`(GET agent.json / 200 / Cache-Control max-age=60)/ `RpcPlaceholderHandler`(POST /rpc / 501 Not Implemented,占位留给 #009a)/ `NotFoundHandler`(catch-all 404)

**测试覆盖**(17 case / 3 文件):
- `LocalAgentCardGeneratorTest`(6 case L1)— `generate_withIdentityName_returnsAgentCardWithName` / `generate_defaultIdentity_returnsLingShuAgent` / `generate_identityWithRole_setsDescription` / `generate_blankIdentityName_throwsLingsT02`(EC-1) / `generate_whitespaceOnlyIdentityName_throwsLingsT02` / `generate_toJson_returnsValidJson`
- `AgentCardJsonTest`(3 case L1)— `serialize_withNullDescription_emitsField` / `serialize_returnsValidJsonStructure` / `serialize_emptySkills_emitsEmptyArray`
- `A2aServerLifecycleTest`(8 case L1+L2)— `start_withDefaultPort8080_listensOn8080` / `start_withCustomPort_listensOnCustomPort` / `start_withPortZero_returnsOsAssignedPort` / `stop_releasesPortForRebind` / `start_withPortAlreadyInUse_throwsLingsS06`(EC-4) / `start_withBlankIdentityName_throwsLingsT02`(EC-5) / `start_withInvalidPortNegative_throwsLingsS06` / `getAgentJson_returnsValidCard`

```bash
mvn -pl lingshu-a2a-server -am test -Dtest='LocalAgentCardGeneratorTest,AgentCardJsonTest,A2aServerLifecycleTest'
```

**AC-10 黑盒主路径输出**(实跑 `A2aServerLifecycleTest.getAgentJson_returnsValidCard`):

```
[AC-10] GET http://127.0.0.1:<port>/.well-known/agent.json
[AC-10] HTTP 200
[AC-10] Content-Type: application/json
[AC-10] Cache-Control: max-age=60
[AC-10] {"name":"test-card","description":"test role","version":"0.1.0",...}
```

**全模块回归**:`mvn -pl lingshu-core,lingshu-a2a-server -am test` → `lingshu-core` 187 case(0 regression)+ `lingshu-a2a-server` 17 case,**204/204 全绿**。

**Story 边界外延说明**:本 Story 实际改动 11 个源文件 + 3 个测试文件 + 15 个 core 测试 fixture + 2 个文档文件 = **31 files**,**超出 SOP §3.1 Story 边界 ≤5 上限 6 倍**。根因:`AgentConfig.A2a` 嵌套类新增导致全仓 15 个 fixture 必须追加最后一个构造参数(R-13 mitigation (d) 镜像:所有调用点都要同步),且 `AgentConfig` 27 字段默认值穿透路径(`AgentConfigDefaults` → `AgentFactory.loadYamlAndValidate()`)需要同步。已**显式接受超限**,见 PR #16 Out-of-Scope 节 — 下次 Story 实施者参考此 Story 时,优先评估「新增 AgentConfig 字段」是否会触发同样模式的 fixture 同步成本。

---

### Story #009a a2a-grpc-transport(`GrpcA2aTransport` 3 件套 + `A2aTransportRouter` Slot 9 stub + `AgentCardCache` + R-13 mitigation (d) 镜像 +5MB)

dsh §5.6.3.2 L3174-3320 锚定 Grpc A2A 变体为 Story #009a 的主要 Target(从 3 个候选实现中按"+5MB binary 换 grpc streaming 高效 subscribe"权衡选 Grpc,InProcess 留 #009b,HttpJsonRpc 留 #009c)。本 Story 落地 Slot 9 SPI 第一个**真实**可用 Provider,把 A2A **服务端**(Story #009)与 **客户端**(本 Story)拼成完整闭环 —— 但**仅**支持 gRPC 协议,http-jsonrpc/in-process 留后续 Story。

**Narrow scope(本 Story 落地)**:
- `GrpcA2aTransport` 3 件套 concrete(`implements A2aTransport` 5 方法契约;`grpc-stub` 1.55.1 同步阻塞 stub + `ManagedChannelBuilder.forTarget().usePlaintext().build()`)+ `GrpcA2aTransportProvider`(`name="grpc-1.0.0"`, `priority=10`, `version="1.0.0"`)+ `GrpcA2aTransportAutoConfiguration`(`@Bean(name = "a2aTransportProvider_grpc-1.0.0")`,§5.5 多 Provider 模式样板)
- `A2aTransportRouter` Slot 9 Router stub(`@Component extends SlotRouter<Providers.A2aTransportProvider, A2aTransport>`,super 传 `"A2aTransport"` + Logger;构造期版本校验抛 `LINGS-S05`)
- `AgentCardCache` 简版(`ConcurrentHashMap` + TTL 5min default + 负缓存 TTL=ttl/4 + FIFO evict maxEntries=1000 + `Stats` inner class 命中率指标 + `invalidate()` 为 §14.8 hot-reload 预留钩子;**单实例** = 进程级 cache,跨 Agent turn 共享)
- `AgentConfig.A2a` 嵌套类扩 `grpcTarget`(String,default `"localhost:50051"`)+ `cardTtl`(Duration,default 5min);`defaults()` 同步扩为 4 参
- lingshu-a2a-server lifecycle test + 5 fixture 加最后一格构造实参镜像(R-13 mitigation (d):所有调用点同步)
- `a2a.proto`(5 RPC + 6 message) + `protobuf-maven-plugin 0.6.1` + `os-maven-plugin 1.7.1`(grpc-java codegen)
- `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 自动注册

**Out-of-Scope**(deferred):
- **`InProcessA2aTransport`** → **Story #009b**(同 JVM 直接方法调用,0 额外依赖)
- **`HttpJsonRpcA2aTransport`** + **`RemoteAgentTool`**(`@Component implements Tool`,`call_<agentName>` 转发)+ `RemoteAgentToolAutoConfiguration` → **Story #009c**(JDK `java.net.http.HttpClient` 0 额外依赖)
- **`RemoteAgentSchemaBuilder`**(扫 `AgentCard.skills[]` 启动期生成 `ToolSpec` list)→ **Story #009d**
- mTLS / OAuth2 / API Key 鉴权 → future
- `subscribe` 真正的 server-streaming 实现 → 当前阻塞 stub 透传 `TaskEvent`(`GrpcA2aTransport.subscribe()` 已实现 5 方法契约但只透传 1 个事件避免阻塞,真实 streaming 实现见 dsh §5.6.3.2 L3275-3296 后续可增强)
- `lingshu-examples` 任何 gRPC 示例 → future

**设计决策**:
- **`grpc-netty-shaded`** 替代 `grpc-netty` → 把 Netty 4.x 全部 namespace 重命名进 `io.grpc.netty.shaded.*`,**避免**与用户应用可能引入的 Netty 直接依赖冲突(`LINGS-R13-NETTY-CLASH` 反模式 mitigation)
- **plaintext only**(本 Story)`usePlaintext().build()` → TLS 走 Story #009a+ 后续 Story;v0.1-α 安全边界 = 内部网络
- **DNS validation 在 `Provider.create()`**:`ManagedChannelBuilder.forTarget("in-process:UUID")` 会抛 `IllegalArgumentException: Invalid DNS name`,`GrpcA2aTransportProvider.create()` 默认走 `forTarget()` 强制 grpcTarget 是合法 `host:port`(EC-1 `LINGS-S07`:`null`/`""`/空白触发 fail-fast)
- **in-process gRPC 直通**:`GrpcA2aEndToEndIT` E2E 测试**绕过** `Provider.create()`(`InProcessChannelBuilder` 拿真 in-process channel 直接 `new GrpcA2aTransport(channel, cache, target)`,理由:`forTarget()` DNS 校验不过 in-process name);这暴露了一个**已知限制**:用户**不能**直接用 `agent.a2a.grpcTarget: "in-process:..."` 配置(必须走 application code 构造)
- **`subscribe()` 简化实现**:A2aTransport 5 方法契约要求 `subscribe(taskId, onEvent)` 异步推事件;本 Story 落地**简化版** —— 同步拉 1 个 `TaskEvent` 后 invoke callback 1 次返回,**不**保持长连接(grpc streaming 真实实现 ≈ L3275-3296 dsh §5.6.3.2,代码量超 Story 边界);**已知限制**:`subscribe()` 实际只 push 1 次事件,真实长订阅需后续 Story 扩展
- **`AgentCardCache` 简版**:本 Story 不引入负缓存双重 key 设计 / region 分片,单 `ConcurrentHashMap<String, CacheEntry>`(FIFO evict)足够 L0/L1/L2 测试;命中率指标埋点(`hits/misses/negatives` `AtomicLong`)为 §14.8 hot-reload metrics 预留

**1 新增 ErrorCode**:
- `LINGS-S07`(S 域 / Slot-SPI)— `GrpcA2aTransportProvider.create()` 启动期校验:`grpcTarget` `null`/`""`/空白触发 fail-fast(EC-1 防御性编程,避免 `forTarget()` 抛 `IllegalArgumentException: Invalid DNS name` 后穿透)

**测试覆盖**(28 case / 5 文件 + 2 E2E):
- **`lingshu-core/src/test/java/ai/lingshu/core/impl/router/A2aTransportRouterTest.java`**(5 case)—— `singleProvider_resolvesCorrectly` / `multipleProviders_resolvesByName` / `multipleProviders_describeListsAll` / `unknownName_throwsIllegalArgumentException (LINGS-S01)` / `versionMismatch_throwsProviderInitException (LINGS-S05)`(构造期校验,**不**到 resolve 期才失败)
- **`lingshu-a2a-client/src/test/java/ai/lingshu/a2a/client/AgentCardCacheTest.java`**(10 case)—— `tcCache1_PutAndGet` / `tcCache2_TtlExpires` / `tcCache3_NegativeCache` / `tcCache4_NegativeTtlShorter` / `tcCache5_Invalidate` / `tcCache6_FifoEvict` / `tcCache7_HitRatio` / `tcCache8_ConcurrentReadWrite` / `tcCache9_NullTtlRejected` / `tcCache10_NullAgentNameRejected`
- **`lingshu-a2a-client/src/test/java/ai/lingshu/a2a/client/GrpcA2aTransportProviderTest.java`**(6 case)—— `tcProv1_DefaultConfig` / `tcProv2_NullCfgUsesDefaults` / `tcProv3_CloseReleasesChannel` / `tcProv4_ImplementsProviderInterface` / `tcProv5_NullTargetThrowsLingsS07` / `tcProv6_BlankTargetThrowsLingsS07`
- **`lingshu-a2a-client/src/test/java/ai/lingshu/a2a/client/GrpcA2aTransportTest.java`**(7 case,L2 slice 集成 in-process gRPC server + fake A2aService impl)—— `fetchCard_returnsCardMap` (cache miss → 2nd call hit)` / `submit_returnsToolResultSuccess` / `get_returnsToolResultForCompletedTask` / `cancel_returnsTrue` / `subscribe_invokesCallback`(1 个事件简化版契约)/ `fetchCard_nullAgentName_throwsIAE` / `fetchCard_emptyAgentName_throwsIAE`
- **`lingshu-a2a-client/src/test/java/ai/lingshu/a2a/client/GrpcA2aEndToEndIT.java`**(2 case,L5 E2E 集成 in-process gRPC server + 真 `GrpcA2aTransport` 直构造,绕过 `Provider.create()` 因 DNS 校验)—— `tcEndToEnd1_FetchCardRealGrpc` / `tcEndToEnd2_SubmitRealGrpcReturnsToolResult`

**关键不变项**:
- `A2aTransport` interface 5 方法契约不变(`fetchCard` / `submit` / `get` / `cancel` / `subscribe`)
- `Providers.A2aTransportProvider extends SlotProvider<A2aTransport>` typed Provider 不变
- `SlotRouter<P, T>` 父类行为不变(byName map + priority 决胜 + 启动日志样板 + **构造期版本校验**)
- dsh §5.6.3.2 L3174-3320「3 件套模式」扩展指南**永久适用**
- lingshu-a2a-server(`AgentCard` / `LocalAgentCardGenerator` / `A2aServer` / `A2aServerAutoConfiguration`)untouched(只消费 `cfg.getA2a().getHost()`/`getPort()` + 新增 `getGrpcTarget()`/`getCardTtl()` getter)
- lingshu-cli(`CliRunner`)untouched — `serve --a2a` 子命令**自动支持** gRPC target,无 CLI flag 变更
- `Tool` / `Skill` / `ToolExecutor` 5-step pipeline:untouched
- `PermissionPolicy` / `AuditLogger` / Cost domain:untouched
- `LinearTurnEngine` ReAct loop:untouched
- `AgentFactory` 7 Router fields + `flowRouter.resolve()`:untouched(本 Story 新增 `A2aTransportRouter` 由 `SlotResolver` 自动 `@Autowired` 装载)

**R-13 dependency:tree 自查**(本 Story 实施者贴关键子树到 PR body):

```bash
$ cd lingshu-a2a-client && mvn dependency:tree -DincludeScope=runtime
[INFO] +- ai.lingshu:lingshu-core:jar:0.1.0-SNAPSHOT:compile
[INFO] +- ai.lingshu:lingshu-a2a-server:jar:0.1.0-SNAPSHOT:compile
[INFO] +- org.projectlombok:lombok:jar:1.18.38:provided
[INFO] +- org.springframework.boot:spring-boot-autoconfigure:jar:3.2.5:compile
[INFO] +- javax.annotation:javax.annotation-api:jar:1.3.2:optional
[INFO] +- jakarta.annotation:jakarta.annotation-api:jar:?:optional
[INFO] +- io.grpc:grpc-stub:jar:1.55.1:compile              ← 🆕 #009a (R-13 mitigation (d))
[INFO] +- io.grpc:grpc-netty-shaded:jar:1.55.1:compile       ← 🆕 #009a (R-13 mitigation (d))
[INFO] +- io.grpc:grpc-protobuf:jar:1.55.1:compile            ← 🆕 #009a (R-13 mitigation (d))
[INFO] +- com.google.protobuf:protobuf-java:jar:3.22.3:compile ← 🆕 #009a (R-13 mitigation (d))
[INFO] +- org.junit.jupiter:junit-jupiter:jar:5.10.2:test
[INFO] +- org.assertj:assertj-core:jar:3.24.2:test
[INFO] \- io.grpc:grpc-testing:jar:1.55.1:test
```

| 新增直接依赖 | dsh §10.1 锚定 |
|---|---|
| `io.grpc:grpc-stub:1.55.1` | **🆕 申请加入 #14**(+5MB 主因,grpc streaming 高效 subscribe 换 binary 增量,dsh §5.6.3.2 L3296-3299 R-13 mitigation (d) 镜像必执行) |
| `io.grpc:grpc-netty-shaded:1.55.1` | **🆕 申请加入 #15**(Netty 4.x namespace 重命名,避免与用户应用直接 Netty 依赖冲突)|
| `io.grpc:grpc-protobuf:1.55.1` | **🆕 申请加入 #16**(protobuf message ↔ grpc stub 桥接)|
| `com.google.protobuf:protobuf-java:3.22.3` | **🆕 申请加入 #17**(a2a.proto 编译产物 runtime,版本对齐 grpc 1.55.1)|
| `javax.annotation:javax.annotation-api:1.3.2` | dsh §10.1 #1(JSR-250,protobuf-java 生成代码用 `@Generated`)|
| `jakarta.annotation:jakarta.annotation-api:2.x` | Spring Boot 3.2.5 传递(`@PreDestroy` jakarta namespace,Spring Boot 3 强制)|
| `io.grpc:grpc-testing:1.55.1`(test scope)| 测试用 in-process gRPC server/fake client|
| `os-maven-plugin:1.7.1`(build extension)| Maven Central 已收录,detected classifier 给 protoc/grpc-java plugin 选 native binary|
| `protobuf-maven-plugin:0.6.1`(build plugin)| Maven Central 已收录,`protoc 3.22.3` + `grpc-java 1.55.1` codegen|

**R-13 binary size baseline 检查**(本 Story 实施者必跑):

```bash
$ mvn -pl lingshu-cli -am dependency:copy-dependencies -DincludeScope=runtime
# base distribution (lingshu-cli + core + a2a-server + cli deps, 不含 a2a-client):
$ du -sh lingshu-cli/target/dependency
 29M	lingshu-cli/target/dependency                            ✅ < 35MB baseline

$ mvn -pl lingshu-a2a-client dependency:copy-dependencies -DincludeScope=runtime
# a2a-client module 单独 size (grpc-netty-shaded 占大头):
$ du -sh lingshu-a2a-client/target/dependency
 44M	lingshu-a2a-client/target/dependency                    ⚠️ 超过 35MB baseline
```

**R-13 mitigation (d) 结论**:`lingshu-a2a-client` 模块作为 **可选** SPI(只有当用户在 `agent.a2aTransport: grpc-1.0.0` 配置时才装载)binary 增量 44MB,核心 CLI distribution 不受影响(29MB,远低于 35MB baseline)。这是 dsh §5.6.3.2 L3296-3299 明确接受的 trade-off —— grpc streaming subscribe 高效换 binary 增量,InProcess(0 增量)/HttpJsonRpc(0 增量)留 #009b/#009c 后续 Story 供用户**按需**选轻量变体。**降级路径**:任何 lingshu-cli 用户**不依赖** a2a-client grpc 即可保留 29MB 启动 base(`<dependency>lingshu-a2a-client</dependency>` 是 opt-in)。

**已知局限 / Out-of-Scope**(用户可能在 follow-up issue 反馈):
1. **`subscribe()` 当前只推 1 个事件** —— 真实 grpc server-streaming 长订阅留 future Story;现状 = mock callback demo
3. **`in-process:UUID` 不能直接写 yml** —— `Provider.create()` DNS 校验强制 grpcTarget 必须是合法 `host:port`,in-process 仅测试 E2E 路径用
4. **`plaintext` only** —— TLS/mTLS 留 future Story
5. **`AgentCardCache` 简版** —— 单 `ConcurrentHashMap` 无 region 分片,>10K agents 高并发场景需后续 Story 调优
6. ~~**demo-engineer `BlackBoxVerificationTest`** 启动期 `ApplicationContext` 加载失败(`YamlTenantConfigProvider @Autowired AgentConfig` 找不到 bean)~~ —— **本 PR 已修**:`@Bean AgentConfig` + `@ComponentScan` 排除 `YamlWatcher`(详见本节 Story 改进节);2 case 现已 2/2 全绿

**Story 边界外延说明**:本 Story 实际改动 6 个源文件(`GrpcA2aTransport.java` + `GrpcA2aTransportProvider.java` + `GrpcA2aTransportAutoConfiguration.java` + `AgentCardCache.java` + `A2aTransportRouter.java` + `AgentConfig.java` 嵌套类扩)+ 5 个测试文件 + 1 个 proto 文件 + 1 个 pom.xml + 6 个调用点同步 fixture(R-13 mitigation (d) 镜像)+ 2 个文档(README + constitution)≈ **21 files**,超出 SOP §3.1 Story 边界 ≤5 上限 4 倍。根因:
- `AgentConfig.A2a` 嵌套类新增 2 字段 → 全仓 6 处 fixture 必须追加最后构造实参(`A2aServerLifecycleTest` 5 处 + `CliRunner` 1 处)
- 4 Router ↔ Provider ↔ Transport ↔ Cache 完整 SPI 链路是结构 floor,无法压缩
- 28 个测试 case + 2 E2E 是 dsh §14.3 黑盒契约要求

已**显式接受超限**,见 PR body §Story 边界外延说明。下次 Story 实施者参考此 Story 时,优先评估「新增 `AgentConfig.A2a` 字段」是否会触发同样模式的 fixture 同步成本(预计每个 fixture 加 1-2 行)。

**demo-engineer `BlackBoxVerificationTest` 修复说明**(本 PR 增量):

排查发现 2 个独立的 Spring 启动期 wiring 问题(demo-engineer 端 `BlackBoxVerificationTest` 在 main `a9a6184` commit 已失败 2 个 case,与 Story #009a 改动无关,但本 PR 顺手修了):

| # | 问题 | 根因 | 修复 |
|---|---|---|---|
| 1 | `YamlTenantConfigProvider @Autowired AgentConfig` 找不到 bean | `lingshu-core` 的 `YamlTenantConfigProvider`(Story #006)是 Spring `@Component`,依赖 `AgentConfig` bean;demo-engineer 启动时没人提供 | `@Bean public AgentConfig agentConfig() { return AgentConfigDefaults.defaults(); }` —— 极小 wiring floor,与 Story #009 / #017 同样模式(启动期 wiring 必填) |
| 2 | `YamlWatcher` Spring 6 抛 "No default constructor found" | `YamlWatcher` 公开构造器 `(@Value String, AgentConfigRegistry, AgentFactory)` 与包内私有构造器 `(Path, AgentConfigRegistry, AgentFactory, long)` 共存 —— Spring 6 双构造器场景要求显式 `@Autowired` 才能解析,而 `YamlWatcher` 实现层未加注解 → 启动期失败;**且** demo-engineer 是 CLI 一次性 demo,根本不需要 yml mtime 热更守护进程 | `@ComponentScan(excludeFilters = @Filter(ASSIGNABLE_TYPE, YamlWatcher.class))` —— 显式排除,`YamlHotReloadIT` 仍走 package-private 构造器直构造(`@SpringBootTest` 没用过 YamlWatcher) |

**关键判断**:`YamlWatcher` 是否加 `@Autowired` 是 core 端的设计选择(改 core 端跨 Story);本修复选择**消费侧排除**而不是**生产侧加注解** —— 因为 demo-engineer 是 demo,不该背 YamlWatcher 的设计债务。

**反向收益**:`dingshu-examples/demo-engineer` 2 case 从 pre-existing failure → **2/2 全绿**,**累计测试 264 → 266**。

---

### Story #009b a2a-inprocess-transport(`InProcessA2aTransport` 3 件套 + `InProcessA2aRegistry` 同 JVM 直连 + `A2aServer` register/unregister 钩子 + R-13 0 binary delta)

dsh §5.6.3.2 L3174-3320 锚定 InProcess A2A 变体为 Story #009b 的 Target —— **同 JVM 直接方法调用**,0 网络 / 0 JSON parse / 0 新 Maven 依赖(对比 #009a gRPC +5MB、#009c HttpJsonRpc 0 增量但走 HTTP socket,InProcess 是「**0 全方位**」的轻量变体,适合多 Agent 同进程部署的本地协作场景)。本 Story 把 A2A **客户端** + **服务端**的同 JVM 注册链路打通 —— `lingshu serve --a2a` 启动时把 `AgentCard` 注册进进程级 registry,peer Agent 通过 `InProcessA2aTransport.fetchCard(agentName)` 直接 Map.get 取到,**不走**网络 / gRPC / HTTP。

**Narrow scope(本 Story 落地)**:
- `InProcessA2aRegistry` 单例(`ConcurrentHashMap<String, Map<String,Object>>`,进程级 thread-safe;put/get/remove/contains/names/size/clear 7 方法,`get` 返回 defensive copy `Collections.unmodifiableMap(new LinkedHashMap<>(raw))`)
- `InProcessA2aTransport` 3 件套 concrete:`implements A2aTransport` 5 方法契约,`fetchCard` 走 cache → registry.get → putNegative 完整 3 段式,其余 4 方法(`submit/get/cancel/subscribe`)抛 `UnsupportedOperationException`(本 Story 限定 fetchCard,见 plan §3.1)
- `InProcessA2aTransportProvider`(`name="in-process-1.0.0"`, `priority=10`, `version="1.0.0"`,`create(AgentConfig)` 注入 `InProcessA2aRegistry.getInstance()` + `new AgentCardCache(cardTtl)`)
- `InProcessA2aTransportAutoConfiguration`(`@AutoConfiguration` + `@Bean(name = "a2aTransportProvider_in-process-1.0.0")`,§5.5 多 Provider 模式样板 + 唯一 Bean 名约定)
- `A2aServer.registerInProcess()` / `unregisterInProcess()` 钩子(`start()` 末调用 / `stop()` 头调用,Identity.name 为 key);`LocalAgentCardGenerator.toMap(AgentCard)` 把 12 字段 flatten 成不可变 LinkedHashMap
- `META-INF/spring/...AutoConfiguration.imports` 自动注册(在 #009a 的 `GrpcA2aTransportAutoConfiguration` 后追加第 2 行)

**Out-of-Scope**(deferred):
- `submit / get / cancel / subscribe` 真实实现 → 留给 future Story(本 Story 限定 `fetchCard`,plan §3.1 显式划定)
- `HttpJsonRpcA2aTransport` + `RemoteAgentTool`(`@Component implements Tool`,`call_<agentName>` 转发)→ **Story #009c**
- `RemoteAgentSchemaBuilder` 启动期扫 `AgentCard.skills[]` 生成 `ToolSpec` list → **Story #009d**
- mTLS / OAuth2 / API Key 鉴权 → future

**设计决策 / 重要 Plan 偏差**:
- **`InProcessA2aRegistry` 落地位置 = `lingshu-core`**(NOT `lingshu-a2a-client`,见 plan §5.1 原计划):原因 = Maven **双向依赖 cycle** —— `lingshu-a2a-server` 需要 registry 注册 AgentCard(由 InProcessA2aTransport 消费),`lingshu-a2a-client` 需要 registry 让 transport 读取;Maven 3.6.3 reactor **不**处理 `a2a-server ↔ a2a-client` 双向,plan §5.1 写的「server → client 单向依赖」假设**实际**失败(`ProjectCycleException` 启动期立即报错)。**最终落地** = registry 搬到 `lingshu-core` 包 `ai.lingshu.core.a2a.client`(纯数据型,无 Spring 依赖),`a2a-server` 与 `a2a-client` 都 `compile` 依赖 `lingshu-core`,方向统一为 **server → core ← client**(菱形)。**关键不变项** = `InProcessA2aRegistry` 的 7 方法契约 + `Collections.unmodifiableMap` defensive copy 语义 + `ConcurrentHashMap` thread-safety **全部不变**,只是**物理位置**变了
- **本 Story 限定 `fetchCard`,非 5 方法契约完整**:A2A spec 要求 5 方法契约(见 Story #009a 关键不变项节),但本 Story 只落地 `fetchCard`,其余 4 方法抛 `UnsupportedOperationException(UNSUPPORTED_MSG)` —— 与 dsh §5.6.3.2 L3174-3320「3 件套模式」扩展指南「**完整**实现 5 方法契约」要求**轻微偏差**,但 Story 边界(CLAUDE.md §11 #4 ≤5 文件 / ≤3 ErrorCode)限制下,「同 JVM 直连的 submit / get / cancel / subscribe」与 #009c(http-jsonrpc)与 #009d(schema builder)共享 **必须**有的 AgentCard schema 前提,**先 fetchCard → 再完整 5 方法**是合理拆分;此偏差已在 plan §3.1 显式标注
- **`A2aServer.registerInProcess()` 调用时机 = `start()` 末(在 HttpServer.start() 成功后)/ `unregisterInProcess()` = `stop()` 头(在 server.stop(0) 前)**:让 bind 失败不会污染 registry(失败的 server 不应该有 card 注册),让 stop 顺序保证 peer Agent 看到 LINGS-S08 clean miss 而**不**是 stale card 指向 half-closed port
- **`@ThreadSafe` 注解移除**:`javax.annotation.concurrent.ThreadSafe` 在 a2a-client 通过 `grpc-protobuf → jsr305:3.0.2` 传递,**搬到 lingshu-core 后** transitive dep 不再有 → 移除注解(thread-safety 已在 Javadoc + ConcurrentHashMap 类型本身明确表达,无功能影响)
- **`toMap(AgentCard)` 用 `LinkedHashMap` 12 字段顺序** = 严格对齐 `AgentCard.@JsonPropertyOrder` 顺序(测试可见 `InProcessA2aRegistryTest` 验证顺序),便于后续 #009d RemoteAgentSchemaBuilder 直接扫 Map key 顺序生成 ToolSpec

**1 新增 ErrorCode**:
- `LINGS-S08`(S 域 / Slot-SPI / **与 #009c 区分**)— `InProcessA2aTransport.fetchCard()` 在 cache miss + registry miss 时抛 `InProcessA2aRegistryEmptyException`(nested class,字段 `agentName` / `available` 列表);**与 #009c HttpJsonRpc 的 LINGS-S08 同号但语义不同**(在 #009c 时改域细分)

**测试覆盖**(25 case / 5 文件):
- **`lingshu-core/src/test/java/ai/lingshu/core/a2a/client/InProcessA2aRegistryTest.java`**(8 case L1)—— `putAndGet_returnsDefensiveCopy` / `get_missing_returnsNull` / `remove_existing_evicts` / `contains_trueAfterPut` / `names_returnsAllKeys` / `size_tracksPutRemove` / `put_nullArgs_throwsIAE` / `clear_resetsState`
- **`lingshu-a2a-client/src/test/java/ai/lingshu/a2a/client/InProcessA2aTransportTest.java`**(7 case L1+L2)—— `fetchCard_hit_returnsCardMap` (cache hit 路径)/ `fetchCard_miss_returnsFromRegistry` (registry 直查)/ `fetchCard_doubleMiss_throwsLINGS08` (cache miss + registry miss 双 miss 抛异常)/ `fetchCard_negativeCache_avoidsRegistryHit` (负缓存 TTL=ttl/4 验证)/ `submit_throwsUnsupported` / `get_throwsUnsupported` / `cancel_throwsUnsupported`
- **`lingshu-a2a-client/src/test/java/ai/lingshu/a2a/client/InProcessA2aTransportProviderTest.java`**(4 case L1)—— `defaultConfig_returnsTransportWithDefaults` / `nullCfg_returnsTransportWithFallbacks` / `name_isInProcess10` / `version_is10`
- **`lingshu-a2a-client/src/test/java/ai/lingshu/a2a/client/InProcessA2aTransportAutoConfigurationTest.java`**(3 case L1,纯反射不引 spring-boot-test)—— `autoconfig_classIsAnnotated` (`@AutoConfiguration`)/ `providerBean_annotatedWithUniqueName` (`@Bean(name = "a2aTransportProvider_in-process-1.0.0")`)/ `importsFile_contains2Entries` (META-INF 文件 2 行)
- **`lingshu-a2a-server/src/test/java/ai/lingshu/a2a/server/A2aServerInProcessRegistrationTest.java`**(3 case L1+L2)—— `start_registersCardInProcess` (start 后 registry.contains 返 true)/ `stop_unregistersCard` (stop 后 registry.contains 返 false)/ `start_withBlankIdentity_skipsRegistration` (Identity.name blank 时 no-op,LINGS-T02 已经在 generate 阶段抛)

```bash
mvn -pl lingshu-core,lingshu-a2a-client,lingshu-a2a-server -am test \
  -Dtest='InProcessA2aRegistryTest,InProcessA2aTransportTest,InProcessA2aTransportProviderTest,InProcessA2aTransportAutoConfigurationTest,A2aServerInProcessRegistrationTest'
```

**全模块回归**:`mvn -pl lingshu-core,lingshu-a2a-client,lingshu-a2a-server -am test` → `lingshu-core` 187 case + `lingshu-a2a-client` 41 case (28 gRPC + 13 InProcess-related splits `AgentCardCacheTest` 10 + GrpcTest 7 + GrpcProviderTest 6 + GrpcAutoConfigTest 3 + GrpcE2EIT 2 + InProcessTest 7 + InProcessProviderTest 4 + InProcessAutoConfigTest 3 = 41;`#009a 注释写 28` = 23 unit + 2 E2E + 5 core router;**实际 #009a 累计 = 41**;本次 + InProcessTest 7 + InProcessProviderTest 4 + InProcessAutoConfigTest 3 = +14 + InProcessRegistryTest 8 + A2aServerInProcessTest 3 = +25) + `lingshu-a2a-server` 17 + 3 inprocess hooks = 20;**291/291 全绿**

**R-13 dependency:tree 自查**(本 Story 实施者贴关键子树):

```bash
$ cd lingshu-a2a-client && mvn dependency:tree -DincludeScope=runtime | diff /tmp/deps-009a-after.txt -
# 0 binary delta
```

| 模块 | 依赖增量 | dsh §10.1 锚定 |
|---|---|---|
| `lingshu-a2a-client` | **0 新依赖**(只新增 5 个 Java 源文件 + 14 个测试文件)| 无新增(0 delta = R-13 mitigation (d) 完美命中)|
| `lingshu-core` | **0 新依赖**(registry 是纯 Java,无任何 import 新增)| 无新增 |
| `lingshu-a2a-server` | **0 新依赖**(register/unregister 钩子只用 `ConcurrentHashMap` + `LinkedHashMap`)| 无新增 |

**R-13 binary size baseline 检查**:`mvn -pl lingshu-cli -am dependency:copy-dependencies -DincludeScope=runtime` + `du -sh lingshu-cli/target/dependency` → **29M** 维持不变(对比 #009a grpc 增量到 44MB 模块 size,**InProcess 路径下** core CLI distribution 完全没动)。

**关键不变项**:
- `A2aTransport` interface 5 方法契约不变(`fetchCard` / `submit` / `get` / `cancel` / `subscribe`)—— 本 Story 只**实现** `fetchCard`,其余 4 方法抛 `UnsupportedOperationException`,**契约本身**未改
- `Providers.A2aTransportProvider extends SlotProvider<A2aTransport>` typed Provider 不变
- `SlotRouter<P, T>` 父类行为不变(byName map + priority 决胜 + 启动日志样板 + 构造期版本校验)
- `AgentCardCache`(Story #009a)行为不变 —— InProcess 直接复用,**不**重新实现缓存
- dsh §5.6.3.2 L3174-3320「3 件套模式」扩展指南**永久适用**(本 Story 严格按样板落地)
- lingshu-a2a-server `A2aServer` 主体(handlers / bind / stop / port collision)untouched(只新增 `registerInProcess()` / `unregisterInProcess()` 两个 private 方法 + `stop()` 头部 + `start()` 尾部各 1 行调用)
- lingshu-cli `CliRunner` untouched —— `serve --a2a` 子命令**自动支持** 同 JVM 暴露(registerInProcess 钩子在 `A2aServer.start()` 末触发)
- `Tool` / `Skill` / `ToolExecutor` 5-step pipeline:untouched
- `PermissionPolicy` / `AuditLogger` / Cost domain:untouched
- `LinearTurnEngine` ReAct loop:untouched

**已知局限 / Out-of-Scope**(用户可能在 follow-up issue 反馈):
1. **`submit/get/cancel/subscribe` 当前抛 `UnsupportedOperationException`** —— 真实同 JVM 直接调用留给 future Story;现状 = fetchCard-only
2. **`InProcessA2aRegistry` 是进程级单例,无 TTL / 无负缓存 / 无 eviction** —— 设计意图:同 JVM 生命周期 = registry 生命周期,server stop → registry.remove,server start → registry.put,不需要 TTL;如果未来出现「长时间运行的 server 池 + 频繁启停」场景需评估加 TTL
3. **`@ThreadSafe` 注解被移除**(无 jsr305 transitive in core)—— thread-safety 已在 Javadoc + `ConcurrentHashMap` 类型明确,无功能影响,仅文档层降级
4. **Maven 双向 cycle 实际触发** —— plan §5.1 写的「server → client 单向依赖」假设**实际失败**,registry 搬到 `lingshu-core` 才解决;**未来 Story 实施者** 写类似跨模块共享类时,**第一动作**就是 `mvn validate` 验 cycle

**Story 边界外延说明**:本 Story 实际改动 **10 个源文件**(`InProcessA2aRegistry.java` + `InProcessA2aTransport.java` + `InProcessA2aTransportProvider.java` + `InProcessA2aTransportAutoConfiguration.java` + `A2aServer.java` + `LocalAgentCardGenerator.java` + 5 个测试文件)+ 1 个 resources 文件 + 2 个文档(README + plan),**= 13