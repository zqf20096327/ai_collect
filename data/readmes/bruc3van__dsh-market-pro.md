# DSH Market Pro

<img src="https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/logo.svg" alt="DSH Market Pro Logo" width="96" height="96" />

[![Website](https://img.shields.io/badge/Website-dsh--market--pro.com-0f172a?style=flat-square)](https://dsh-market-pro.com)
[![npm version](https://img.shields.io/npm/v/dsh-market-pro?style=flat-square)](https://www.npmjs.com/package/dsh-market-pro)
[![npm downloads](https://img.shields.io/npm/dw/dsh-market-pro?style=flat-square)](https://www.npmjs.com/package/dsh-market-pro)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://github.com/bruc3van/dsh-market-pro/blob/master/LICENSE)

**面向 Agent 的 DSH 插件、技能与 MCP 市场：30,000+ 已核实插件、100 个精选技能与 100 个精选 MCP 目录，内置 `/market-pro` AI 选型助手、一键批量更新与安装后安全审查。**

中文 | [English](https://github.com/bruc3van/dsh-market-pro/blob/master/README_EN.md) | [官网与全量目录](https://dsh-market-pro.com) | [GitHub](https://github.com/bruc3van/dsh-market-pro) | [npm](https://www.npmjs.com/package/dsh-market-pro)

> **DSH Market Pro** is an AI-native plugin, Agent Skills, and MCP marketplace for **DeepSeek Harness (DSH)** — featuring 30,000+ verified plugins, 100 curated skills, 100 curated MCP servers, and the built-in `/market-pro` AI discovery assistant. Browse the full directory online at [dsh-market-pro.com](https://dsh-market-pro.com/en/) or read the [English README](https://github.com/bruc3van/dsh-market-pro/blob/master/README_EN.md).

DeepSeek Harness（DSH）的 AI 原生第三方插件市场（官网与在线目录：[dsh-market-pro.com](https://dsh-market-pro.com)）。基于每日核实的社区目录 [awesome-dsh-plugin-pro](https://github.com/bruc3van/awesome-dsh-plugin-pro)（覆盖 30,000+ 社区插件）、内置 100 个精选 Agent 技能与 100 个精选 MCP 目录，不仅让你在一个界面里完成插件浏览与安装、版本更新、精选技能零依赖直装与删除管理、精选 MCP 一键添加、MCP 服务器托管配置与测试连接弹窗诊断、安装后 AI 审查，更直接赋予 **DSH Agent 对话内查市场、选插件、挑技能、配 MCP、给方案与安全安装** 的原生能力——告别人工翻找。

![插件市场主界面](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace.png)

## 主要功能

- **面向 Agent 的 AI 原生选型、直装与批量更新（统一内置 Skill `/market-pro` + 插件 · 技能 · MCP 三大工具）**：
  - 安装并启用 `dsh-market-pro` 后，默认自动向当前 DSH 会话注册统一内置技能 **`market-pro`** 以及三大底层工具 **`dsh_market_pro`**（插件选型、兼容性检查、`install_plugin` 安全直装与批量更新）、**`dsh_skills_pro`**（100 精选技能检索、盘点与原生审批直装）、**`dsh_mcp_pro`**（精选与自定义 MCP 托管安装），无需手工配置，卸载或停用插件时自动清理。
  - **直接对话即可挑插件、装插件、选技能、配 MCP、一键更插件**：在任意会话中自然语言描述需求，或输入 **`/market-pro`** 显式唤起（支持跨插件/技能/MCP 联合选型与去重）；也可以在市场顶部点击 **「AI 帮我选插件」**、**「AI 帮我选技能」** 或 **「AI 帮我选 MCP」** 一键发起对话。
  - **精准检索、环境盘点与兼容性诊断**：支持中文分词回退、中英多同义词并查、已装/已配项过滤与批量详情核对，直接读取本地缓存的编辑精选、30,000+ 全量插件目录、100 个精选技能与内置 100 个精选 MCP 目录；联合盘点当前环境已安装的插件、技能与 MCP 避免重复推荐，并在检索、详情与更新前自动识别插件与当前 DSH 版本的双向兼容性及多版本自动回退版本。
  - **纵深防注入、原生审批与零明文密钥**：所有检索与更新探测严格只读，对第三方元数据执行隐形 Unicode 剥离、尖括号中和与 `<untrusted_market_data>` / `<untrusted_mcp_data>` / `<untrusted_skill_data>` 协议边界隔离；插件安装经你确认后直接通过 `dsh_market_pro` 的 `install_plugin` 发起 DSH 原生审批与构建脚本（`pendingBuilds`）显式授权（标准模式即可直接使用；仅在 API 不可用或安装本地/非 GitHub·Gitee 来源时回退至 `plugin_manager`），插件批量更新（`update_plugins`）严格绑定你确认过的精确包名与版本、强制走 DSH 原生审批（fail-closed）并完整列出每一项，技能直装（`install_featured`）与 MCP 安装/启停（`install_featured` / `install_custom` / `set_enabled`）同样强制走原生审批，拒绝一切明文密钥并自动绑定 `${credential:REF}` 凭据模板。
  - **随时可控，兼顾零 Token 偏好**：在市场顶部的 **设置** 页签中可随时一键关闭或开启 **AI 选型助手（插件 · 技能 · MCP）**，关闭后立即撤回内置技能与全部工具、回归零常驻 Token；同时也支持一键开关社区目录联网加载、查看/关闭匿名统计，并在设置页内置永久 GitHub Star 支持入口，修改即时生效并随当前 profile 持久化。顶部操作栏直接展示 **刷新** 与 **仓库**，并在检测到任意已安装插件有新版时展示 **一键更新 (N)**。
- **精选、官方实验性与全量目录**：剔除蹭标签与非插件项目。打开即展示编辑精选，提供 **官方实验性** 子页签与宿主实时同步管理 DSH 内置可选/实验性插件（支持按启用状态筛选、按需安装并启用、版本更新与卸载进度反馈），同时提供完整社区目录，支持按分类筛选、关键词与包名搜索、「全部」目录按**活跃热门 / Star 最多 / 最近更新**排序，以及在局部视图搜不到时的**跨范围一键引导**。
- **一键安装与手动添加插件**：已收录安装信息的插件可直接点击安装并启用；未提供直接安装信息的仓库，可一键生成提示词交由 AI 核实后完成安装。右上角提供 **添加插件** 弹窗，支持输入 npm 包名（可指定版本）、GitHub / Git 仓库地址（支持 `#分支` 与 `#path:子目录`）或本地目录路径，内置可折叠安装引导示例、多安装源切换（默认源 / npm 官方源 / 中国大陆镜像 / 自定义私服）与检查/未知状态恢复机制。
- **双向 DSH 版本兼容性校验与多版本自动回退**：
  - **双向识别与方向性提示**：不仅拦截「插件要求更高版本 DSH」（**需升级 DSH**），也能识别「插件仅支持旧版宿主、已被当前 DSH 拒绝加载」（**插件版本过旧** / **版本不兼容**），以及 Monorepo 半安装兼容性问题，在卡片、安装弹窗、已安装/官方实验性卡片、更新列表与 AI 工具返回中统一呈现具体版本要求与修复指引（引导升级 DSH 或更新插件，并禁用无效启用按钮）。
  - **订阅多版本自动兼容回退**：当订阅插件最新版需要更高版本 DSH 时，自动从多版本索引中选用适配当前 DSH 的最新兼容稳定版，并在安装弹窗中给出内联说明；若安装包仍因版本不兼容被宿主拦截，则本地化展示失败详情并隐藏无效重试按钮。
- **已安装管理、筛选与一键批量更新**：已安装插件卡片与精选/技能/MCP 统一卡片几何与视觉层次，读取本地插件 `locale/*.json` 多语言名称/简介与包内本地图标（去除头像圆角裁切）并关联目录品牌 Logo，支持随时启用/停用（立即生效，无需重启）、卸载（慢清理时实时显示耗时安抚与状态刷新）、按**全部状态 / 有新版**筛选，以及单插件多版本选择升级（对不兼容历史/新版给出方向性禁用原因）与**一键批量更新**（先弹窗确认清单、可勾选、依次更新、失败项自动跳过并支持重试、本插件自动最后更新）；无论哪个已安装插件有新版，主面板右上角都会直接显示 **一键更新 (N)** 快捷按钮。
- **安装后 AI 审查**：支持对已安装插件生成审查草稿并填入对话框（由你确认发送），让 AI 协助排查本地插件代码中的联网请求、凭据读取或脚本执行等潜在风险。
- **精选技能零依赖直装、来源校验与分组管理**：
  - **100 个精选 Agent 技能（源自 skills.sh All Time）**：与插件统一采用 7 大功能分类（顶栏提供分类 + 来源双下拉筛选），全量展示对应开源组织/作者的真实品牌 Logo；
  - **免 `npx`、免终端交互一键直装与来源证明**：在详情弹窗中直接从 GitHub 拉取经核实的技能子路径，若 GitHub 不可达自动回退至官方 jsDelivr 镜像，无需本机预装 CLI 或手动交互确认；默认安装到 **DSH 全局目录 `~/.dsh/skills`**，也可选 **通用 Agent 目录 `~/.agents/skills`** 或通过目录选择器安装到指定 **项目级 `.dsh/skills`**；写入前强制校验根目录 `SKILL.md` 与路径边界，并在包含脚本时给出提示；安装时自动写入 `.dsh-market-pro.json` 来源标记（同时兼容识别 `npx skills` 的 `.skill-lock.json`），严格按来源证明关联精选目录元数据，避免手动拷贝的同名本地技能被误认领；同样保留「交由 AI 核实」与原生审批直装；
  - **已安装技能分组视图与弹窗安全删除**：在「已安装」视图及对话内技能页按来源（**用户 / 项目 / 随包提供**）分组展示统一卡片，已验证来源的精选技能自动展示品牌 Logo、仓库与中文简介（并支持直接按展示文案搜索），支持通过提示气泡查看完整路径与 `SKILL.md` 额外说明、打开目录，以及通过**独立确认弹窗**安全删除本地用户/项目技能（Host 侧校验技能目录与 `SKILL.md`、禁止符号链接越界，并保护随包内置的 `market-pro` 技能）。
- **MCP 精选目录、JSON 粘贴导入、托管管理与弹窗诊断**：基于 DSH 官方 MCP 管理器（DSH ≥ 0.2.2-rc.2），分为 **精选** 与 **已配置** 两个子页签，页签工具栏右侧统一提供 **打开设置文件**、**AI 帮我选 MCP** 与 **添加 MCP** 快捷入口：
  - **内置 100 个精选 MCP 目录**：与插件统一按功能划分为开发者工具、知识与研究、网页与浏览器、设计与视觉、集成与分享、实用工具、Agent 工作流 7 大分类（含 Context7、DeepWiki、arXiv、Zotero、AWS Docs、Playwright、Chrome DevTools、Scrapling、Browser Use、GitHub、GitLab、Supabase、Stripe、Sentry、Azure、Firebase、腾讯云开发、DBHub、Serena、Codebase Memory、Kubernetes、MongoDB、ClickHouse、Neo4j、DuckDB、Exa、AIHOT、高德/百度地图、12306、Home Assistant、AKTools、飞书、钉钉、语雀、Notion、Excel、Airtable、AntV 图表、draw.io、GitDiagram、tldraw、MiniMax、Figma、Qdrant、Basic Memory 等）；支持顶栏分类 + 接入方式（免密钥 / HTTP / npx / uvx）双下拉筛选、关键词/包名搜索、自动识别已配置状态与实时连接状态，以及一键添加或弹窗配置（支持密钥获取页一键直达、密钥显隐切换、命令复制、原生状态点与流光实时展示启动连接进度与失败重试）；
  - **JSON 粘贴导入与本地备注**：在「添加 MCP」弹窗中支持直接粘贴 Claude / Cursor / DSH 风格的 `mcpServers` JSON（自动剥离 Markdown 代码块、支持多服务器切换填入并识别明文密钥一键转为加密凭据）；支持为自定义服务器填写仅保存在本地的**描述备注**（不写入宿主设置、修改描述无需重启服务），新建服务器默认保存后立即启用并实时展示连接进度；
  - **统一卡片、状态芯片工具弹窗与测试连接弹窗**：在「已配置」视图按状态筛选并支持按名称、命令、工具名、本地备注与精选文案搜索；匹配精选目录的服务器自动展示品牌 Logo、发布者与双语简介；点击右上角 **已连接 · N 个工具** 状态芯片即可直接打开**工具弹窗**浏览与搜索全部工具；点击 **测试连接** 弹出独立诊断弹窗实时反馈握手耗时、服务器版本、发现的工具列表与错误原因（支持一键重新测试或跳转编辑配置）；
  - **完整生命周期与凭据安全**：支持添加、编辑、启停、重启，配置**断线自动重连策略**与**关闭超时**；展示凭据来源（凭据库 / 环境变量），支持明文密钥一键转存为凭据、更新或**清除凭据**；
  - **静态 MCP 启动详情与一键转托管**：直接写入 profile 的静态 `dsh-mcp-client` 服务器提供可点击/键盘聚焦的 **启动详情** 提示徽章、风险提示与启停开关，并支持一键**转为托管**（Host 侧自动将明文密钥安全迁入凭据库并停用原静态行）。

## 方案对比

与其他常见插件发现与管理方式相比，DSH Market Pro 将**严选数据源、精选 MCP 目录、全栈管理界面**与**可随时开关的 Agent 原生选型能力**整合在一个插件中：

| 对比维度 | DSH Market Pro（本插件） | DSH 官方发现页 (`dsh-plugin-market`) | 常见纯 UI / 泛收录社区市场 | 独立发现型 Skill / MCP 服务 |
|---|---|---|---|---|
| **数据源与筛选质量** | **严选真插件 + 精选技能 + 精选 MCP**：每日核验并剔除蹭标签、空仓与非插件项目；提供**编辑精选 + 30,000+ 全量插件目录 + 100 个精选技能 + 100 个精选 MCP**，内置国内镜像容灾（含技能 jsDelivr 回退）与本地持久化缓存 | 仅读取用户手动添加的 format-1 订阅索引，自身不内置社区目录 | 部分目录按 GitHub topic 泛抓取，容易混入非插件或无法安装的仓库，需人工甄别 | 依赖第三方聚合 API 或外部 CLI，对 DSH 插件结构与安装目标覆盖有限 |
| **对话内 AI 选型与配置** | **安装即默认开启，标准模式可用**：统一内置 `/market-pro` 技能与 `dsh_market_pro` + `dsh_skills_pro` + `dsh_mcp_pro` 工具，支持跨形态选型、兼容性诊断、`install_plugin` 原生审批直装与一键批量更新插件，以及安全安装/启停 MCP | 提供 `plugin_market` 工具，但**默认仅在 Creator 模式启用**，无配套选型技能与 MCP 安装能力 | 多数侧重界面点击浏览，不提供对话内 Agent 自主查库选型 | 可在对话中检索，但需额外配置独立 MCP 子进程或外部 CLI，缺少可视化管理界面 |
| **环境感知与去重** | 自动联合盘点当前 profile **已安装插件 + 托管/静态 MCP 与工具组**，自动过滤已装项并检查双向 DSH 版本兼容性与兼容替代版本 | 标注订阅条目的安装状态，不含 MCP/技能联合盘点 | 多以卡片已安装徽章为主，不参与对话级能力规划 | 通常无法直接读取当前 DSH profile 的已安装插件与托管 MCP 状态 |
| **一站式管理范围** | **插件（精选/官方实验性/全量/手动添加）+ 技能 + 精选与托管 MCP + 市场设置**四合一（支持热启停、有新版筛选与右上角 `一键更新 (N)`、精选 MCP 一键添加、转托管、凭据管理与工具弹窗） | 聚焦插件发现与管理，不含技能页和 MCP 托管界面 | 侧重插件浏览、评分或社区讨论，通常需另装插件管理 MCP 与技能 | 仅聚焦单一类型（只搜 Skill 或只搜 MCP），不含宿主插件管理 |
| **安全与防注入** | **纵深防注入**（剥离隐形 Unicode + 尖括号中和 + 数据边界隔离）+ `install_plugin` / 原生审批（含脚本 `pendingBuilds` 授权）+ **零明文密钥凭据模板** + **安装后只读 AI 审查** | 工具描述声明不可信数据，安装走官方 `plugin_manager` 审批 | 各方案策略不一，以页面提示或安装时校验为主 | 多依赖提示词提醒先确认，较少提供协议级数据隔离与零明文密钥强校验 |
| **Token 开销控制** | 紧凑单语输出 + 批量查询省轮次；可在 **设置页一键关闭**，立即撤回全部技能与工具，回归**零常驻 Token** | 仅在启用该工具的预设中占用工具声明 | 被动 UI 运行，无常驻对话开销 | 外部 MCP 常驻子进程并持续注入工具 schema |

> 以上对比基于各方案公开形态与典型定位，不同工具各有侧重（例如纯 UI 市场适合偏好社区评论与截图浏览的用户）。如果你希望在 DSH 中同时获得**经过核实的真插件数据源、内置精选 MCP 目录、插件/技能/MCP 一体化管理**以及**开箱即用、随时可关的 Agent 原生选型闭环**，DSH Market Pro 会更省心。

## 安装方式

1. 打开 DSH 左侧导航栏的 **插件** 页面。
2. 在官方插件安装界面中输入 **`dsh-market-pro`** 进行安装并启用。
3. 安装完成后，即可从左侧导航栏的 **插件市场Pro**、插件页顶部标签或会话右侧边栏打开市场，也可以直接在对话中向 DSH 提问或使用 **`/market-pro`** 让 Agent 帮你选插件、挑技能、配 MCP。

## 对话内 AI 选型与安装示例

截图中的对话由本地演示模型驱动。DSH 实际执行工具并生成审批卡片。

### 1. 选插件与跨形态推荐（`/market-pro`）

安装后默认开启，在 DSH 对话框中直接输入：

```text
我想让 DSH 帮我做文档导出和图表绘制，先看看我目前装了哪些插件，再从市场里推荐几个活跃的方案
```

或者使用斜杠命令显式调用统一内置技能：

```text
/market-pro 帮我找适合前端研发和接口联调的插件、技能与 MCP 组合
```

Agent 会通过 `dsh_market_pro` 自动完成以下流程：

1. **环境盘点**（`environment`）：了解当前 profile 已安装的插件和 MCP，避免重复推荐。
2. **精选与全量检索**（`featured` / `search` / `detail`）：优先检索编辑精选与可直装插件，按需扩展至数万社区仓库并核对安装目标、前置依赖及与当前 DSH 版本的双向兼容性（存在多版本索引时自动选择最新兼容版本）。
3. **对比建议与安全安装**：给出 2–4 个候选对比；在你确认后，直接调用 `dsh_market_pro` 的 `install_plugin` 发起 DSH 原生审批（标准模式可用，若触发 `pendingBuilds` 需你显式授权构建脚本；本地路径或 API 不可用时回退至 `plugin_manager`），并可继续执行只读安全审查。

![对话内 AI 原生选插件](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-ai-chat.png)

### 2. 检查与一键批量更新插件（`/market-pro`）

在对话中直接输入：

```text
/market-pro 帮我检查已安装插件有没有新版本，确认后一键更新到最新版
```

Agent 会通过 `dsh_market_pro` 执行安全更新闭环：

1. **只读检查更新**（`check_updates`）：同时检查 npm registry 与已配置的 Git 订阅源，列出每个可更新插件的当前版本与最新兼容稳定版。
2. **锁定版本 + 原生审批更新**（`update_plugins`）：经你确认后仅提交已确认的精确 `{ packageName, version }` 列表，触发 DSH 原生审批完整列出全部更新项；执行时自动将 `dsh-market-pro` 排在最后，失败项自动跳过并保留回滚提示，最后汇总成功、需重启与失败详情。

### 3. 选配与安全安装 MCP（`/market-pro`）

在对话中直接输入 `/market-pro` 或点击 MCP 页右上角的 **「AI 帮我选 MCP」**：

```text
/market-pro 先盘点我当前已配置的 MCP，再推荐适合查最新框架文档和画图表的精选 MCP，确认后帮我安全安装
```

Agent 会通过 `dsh_mcp_pro` 完成端到端安全闭环：

1. **只读盘点与筛选**（`list_configured` / `search_featured` / `detail`）：自动跳过已配置的同类 MCP，对比连接方式（`HTTP` / `npx` / `uvx`）与凭据需求。
2. **宿主原生审批写入**（`install_featured` / `install_custom` / `set_enabled`）：经你在对话确认后发起 DSH 原生审批，完整展示实际命令、端点、工作目录、环境变量与请求头，拒绝即止。
3. **全程零明文密钥**：需要 API Key 的服务器自动绑定 `${credential:REF}` 凭据模板，不要求在对话中粘贴密钥；保存后直接引导你前往 **插件市场Pro → MCP → 已配置** 点击 **填写** 安全存入凭据库。

![对话内 AI 原生选配与安全安装 MCP](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-ai-mcp-chat.png)

### 4. 选配与原生审批直装 Agent 技能（`/market-pro`）

在对话中直接输入 `/market-pro` 或点击技能页右上角的 **「AI 帮我选技能」**：

```text
/market-pro 先盘点我当前可用的技能，再推荐适合前端界面设计或代码审查的精选技能，确认后直接帮我安装到 ~/.dsh/skills
```

Agent 会通过 `dsh_skills_pro` 完成安全闭环：

1. **盘点与检索**（`list_installed` / `search_featured` / `detail`）：跳过已有同类技能，核对精选技能的来源仓库、子路径与适用场景。
2. **原生审批直装**（`install_featured`）：经你确认后发起 DSH 原生审批，直接从已核实仓库（支持国内 jsDelivr 自动回退）下载并写入目标目录（`~/.dsh/skills` / `~/.agents/skills` / 项目 `.dsh/skills`），无需调用交互式 `npx skills` 命令。

> 如需关闭或重新开启该能力，打开 **插件市场Pro → 设置**，切换 **AI 选型助手（插件 · 技能 · MCP）** 即可实时生效。

## 界面预览

### 市场设置（AI 助手、数据源与支持入口）

在 **设置** 页签中一键管理 **AI 选型助手（插件 · 技能 · MCP）**、**社区插件目录** 与 **匿名使用统计**（内联隐私说明链接），即时生效并随当前 profile 持久化，也可以直接点击按钮在对话中试用 AI 选型或前往 GitHub 点亮 Star。

![市场设置页](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-settings.png)

### 官方实验性插件

切换到 **官方实验性** 与当前宿主实时同步管理 DSH 内置可选与实验性插件，支持按启用状态筛选、按需安装并启用、版本更新及卸载反馈；对不兼容当前 DSH 版本的异常插件也会给出方向性提示并保护性禁用开关。

![官方实验性插件](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-official.png)

### 手动添加插件与多安装源

点击右上角 **添加插件**，直接通过 npm 包名（可指定版本）、GitHub / Git 仓库地址（支持 `#分支` / `#path:子目录`）或本地目录路径安装插件，内置可折叠安装引导示例、多安装源切换（默认安装源 / npm 官方源 / 中国大陆镜像 / 自定义地址）与兼容性诊断。

![手动添加插件弹窗](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-manual-install.png)

### 全量目录与排序

切换到 **全部** 浏览完整收录目录，按分类筛选并自由切换 **活跃热门**、**Star 最多**、**最近更新** 排序方式。

![全量目录与排序](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-all.png)

### MCP 精选目录、JSON 粘贴导入、托管管理与弹窗诊断

在 **MCP** 页签的页签工具栏右侧即可一键 **打开设置文件**、唤起 **AI 帮我选 MCP** 或 **添加 MCP**；先通过 **精选** 子页签浏览内置的 100 个精选 MCP 服务器（与插件统一按功能分类，支持分类与接入方式双下拉筛选、关键词检索、已添加与实时状态识别，以及弹窗内直达密钥获取页与原生状态点实时跟踪安装连接），再切至 **已配置** 集中管理托管与静态 MCP 服务器：卡片自动匹配精选 Logo、发布者与简介并支持自定义本地备注，点击右上角状态芯片即可打开 **工具弹窗** 搜索全部工具，点击 **测试连接** 弹出独立诊断弹窗实时反馈握手与工具列表，在 **添加 MCP** 弹窗中还支持直接粘贴 Claude / Cursor 风格的 `mcpServers` JSON 一键解析填入。

![MCP 精选目录](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-mcp-featured.png)

![MCP 已配置与托管管理](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-mcp.png)

![添加 MCP 与 JSON 粘贴导入](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-mcp-add.png)

![MCP 测试连接诊断弹窗](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-mcp-probe.png)

![MCP 工具列表弹窗](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-mcp-tools.png)

### 侧边栏快捷入口

除了左侧主导航外，也可以在任意对话中展开右侧边栏，快速打开 **插件市场Pro**。

![右侧栏入口](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-sidebar.png)

### 已安装管理、筛选与一键更新

在 **已安装** 页面管理当前环境中的插件，自动读取本地 `locale/*.json` 名称简介与包内图标，支持按 **全部状态 / 有新版** 筛选、随时启停或卸载（慢清理时显示耗时提示与状态刷新）、单插件多版本选择升级（对需升级 DSH 或仅支持旧版宿主的版本分别给出禁用原因），以及当任意已安装插件有新版时直接点击右上角 **一键更新 (N)** 确认清单后按顺序批量升级（失败自动跳过并支持重试失败项）。

![已安装面板](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-installed.png)

![批量更新确认清单](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-batch-update.png)

### 安装后 AI 安全审查

在安装完成弹窗或已安装插件卡片上点击 **AI 审查**，自动在会话输入框中准备审查提示词草稿，由你发送给 AI 进行只读检查。

![AI 审查草稿](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-sec-check.png)

### 技能页、精选直装与分组管理

在市场顶部的 **技能** 页签中，可先通过 **精选** 子页签浏览内置的 100 个 skills.sh All Time 精选技能（展示真实品牌 Logo，支持功能分类与来源下拉筛选、查看仓库子路径，以及在弹窗中免 `npx` 一键直装到 **DSH 全局目录 `~/.dsh/skills`**、**通用 Agent 目录 `~/.agents/skills`** 或 **指定项目级 `.dsh/skills` 目录**，并自动支持国内 jsDelivr 回退与「交由 AI 核实」）；切换至 **已安装** 或打开对话标题下方的 **技能** 入口，可按来源分组（**用户 / 项目 / 随包提供**）查看当前会话可用的全部技能、打开目录或通过确认弹窗安全删除本地用户/项目技能。

![全局技能精选页](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-skills.png)

![精选技能直装弹窗](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-skills-install.png)

![已安装技能分组与管理](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/marketplace-skills-installed.png)

![对话内技能页](https://raw.githubusercontent.com/bruc3van/dsh-market-pro/master/assets/screenshots/conversation-skills.png)

## 使用提示

- **安全提醒**：目录收录仅核实项目是否为 DSH 插件，不代表安全背书。安装前请留意插件来源与权限要求。
- **关于 AI 审查**：AI 审查是在插件安装后对本地文件进行的辅助检查，供你评估风险参考，无法阻止或撤销插件安装时已经发生的执行。
- **匿名使用统计**：默认开启，每天向 [dsh-market-pro.com](https://dsh-market-pro.com) 发送活跃心跳（本地随机安装 ID、插件与 DSH 版本、运行形态、操作系统与语言）以及官方公开目录插件、内置精选技能与内置精选 MCP 的安装成功或失败结果（失败原因仅映射为脱敏闭集错误码），用于统计安装规模与改进兼容性。绝不采集对话、文件路径、密钥、原始错误堆栈、私有插件、自定义技能或自定义 MCP（非公开目标直接丢弃不上报）；可在市场 **设置 → 匿名使用统计** 一键关闭（立即停发并清除本地 ID），或设置环境变量 `DO_NOT_TRACK=1` / `DSH_MARKET_TELEMETRY=0` / `DSH_TELEMETRY_DISABLED=1` / `CI=true`。详情与报文样例见 [PRIVACY.md](https://github.com/bruc3van/dsh-market-pro/blob/master/PRIVACY.md)。

## 相关项目

- **[DSH Market Pro 官网与全量目录](https://dsh-market-pro.com)**：在线浏览全部 30,000+ DSH 社区插件、100 个精选 MCP 与官方发现页订阅源。

- **[DSH Desktop Pro](https://github.com/bruc3van/dsh-desktop-pro)**：让 Agent 安全常驻桌面的独立 DeepSeek Harness 客户端。
- **[awesome-dsh-plugin-pro](https://github.com/bruc3van/awesome-dsh-plugin-pro)**：经过每日核实的 DSH 社区插件目录，也是本市场的数据来源。
- **[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)**：DeepSeek Harness 官方仓库。

## 许可证

[MIT](https://github.com/bruc3van/dsh-market-pro/blob/master/LICENSE)
