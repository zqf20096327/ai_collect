# DSH Loomy Connect

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

简体中文 | [English](README.en.md)

> **派生声明**：本项目是 [gdrpzym/dsh-loomy-connect](https://github.com/gdrpzym/dsh-loomy-connect) 的衍生版本，上游基线 `0.2.0`（MIT，原始版权归 `gdrpzym` 所有），本仓库将其适配到 DSH 0.2.1。改动范围与许可说明见 [FORK.md](FORK.md)。

用 Loomy 账号登录，把它内置的文本模型接入 [DeepSeek Harness](https://github.com/deepseek-ai)（DSH），无需 API Key。

**不需要安装 Loomy 桌面应用**：在插件页输入手机号、填一次短信验证码即可，登录态由插件自己持有，14 天有效。

插件也兼容已装桌面端的机器——此时可直接复用桌面端已有的登录态，无需再登录一次。

> **注意**：与上游 [gdrpzym/dsh-loomy-connect](https://github.com/gdrpzym/dsh-loomy-connect) 注册的是同一个 `loomy` provider，**两者不能同时安装**。从上游迁移时先卸载再装本分支。

| 能力 | 位置 | 说明 |
|---|---|---|
| 模型 Provider | 宿主端 | 注册 `loomy` provider，模型列表在启动时从 Loomy 发现 |
| 设置卡片 | 浏览器端 | **设置 → 插件配置** 下分「账户」「模型」两个标签页：账户展示登录态、脱敏手机号与积分余额；模型以表格列出名称、上下文窗口与倍率，图像模型排在最后 |
| 登录表单 | 浏览器端 | 未登录或使用桌面端登录态时，卡片下方显示「登录 Loomy 账号」：手机号 → 短信验证码 → 完成 |

## 目录

- [派生说明（FORK.md）](FORK.md)
- [功能](#功能)
- [安装](#安装)
- [登录](#登录)
- [配置](#配置)
- [安全边界](#安全边界)
- [已知限制](#已知限制)
- [故障排查](#故障排查)
- [深入文档](#深入文档)
- [许可](#许可)
- [免责声明](#免责声明)
- [致谢](#致谢)

## 功能

- **零配置**：安装启用后，Loomy 的模型直接出现在 DSH 的模型选择器里。
- **短信登录**：手机号 + 验证码即可，不需要密码，也不需要桌面端。用 `POST /login/phone/sendMsgCode` 与 `/login/phone/checkCode` 换取会话，会话有效期 14 天。
- **实时积分**：登录后积分取自 Loomy 的正式账本接口（`/points/records`），点「刷新」立即向 Loomy 重新拉取；与桌面端本地缓存相比不再滞后。
- **模型自动发现**：启动时拉取当前账号可用的模型清单，只纳入支持文本输出的模型。
- **倍率与优惠**：插件页的「模型」标签页列出全部模型及各自的积分倍率（如 `x3.0`、限时免费），数据随 Loomy 侧调整而变化。
- **账号与积分**：插件页顶部状态行显示当前登录账号（脱敏手机号），「积分」标签页显示永久积分与每日赠送积分。
- **模型明细**：插件页的「模型」标签页以三列表格列出每个模型的名称、上下文窗口大小（若 Loomy 的清单提供了该字段）与积分倍率，图像模型排在文本模型之后。
- **模型页状态条**：「设置 → 模型」的 Loomy 卡片内直接显示登录态与永久积分。
- **逐模型开关**：在 `llm-loomy` 行配置页可逐个启用或禁用模型；被禁用的模型不再出现在 DSH 的模型选择器中，改动即时生效、无需重启。
- **图片输入**：支持向模型发送图片，由宿主的 attachment 服务转成请求内的图像内容。
- **工具调用**：模型可正常返回 `tool_calls`，DSH 的工具链不受影响。
- **中英双语**：界面文案跟随 DSH 界面语言。

## 界面位置（DSH 0.2.1）

| 位置 | 内容 |
|---|---|
| 设置 → 插件 → **DSH Loomy Connect** | 账号、积分、模型表、登录表单、退出登录、手动刷新 |
| 该插件的 **llm-loomy** 行 → 配置页 | `authFile` / `configFile` 路径覆盖；页面下方为「禁用的模型」开关，可保存并立即生效 |
| 设置 → 模型 → **Loomy** 卡片 | 精简状态条（登录态、永久积分、刷新） |

## 安装

| | |
|---|---|
| **Loomy 账号** | 一个能收短信的手机号即可 |
| **Loomy 桌面应用** | **可选**。装有且登录过时，插件可直接复用其登录态，无需再登录一次 |
| **DeepSeek Harness** | `>= 0.2.1-rc.2 < 0.3.0` |
| **Node.js** | `>= 22.19` |
| **pnpm** | 必需。`dsh plugin` 内部通过 pnpm 管理 profile 依赖，只装有 npm 不够 |

### 从插件市场安装（推荐）

DSH 的 **插件 → 插件市场** 里搜索 `loomy`，或直接打开条目页：

```
https://awesome-dsh-plugin.com/p/2239058652/dsh-loomy-connect/
```

本仓库已收录进 [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) 精选列表，市场会自动同步。

### 从 GitHub 安装

```sh
dsh plugin --profile web add github:2239058652/dsh-loomy-connect
dsh web
```

本仓库已提交构建产物 `lib/`，安装时**不会**触发构建，无需 tsdown 或 TypeScript。

没有全局 `dsh` 时，把 `dsh` 换成以下任一即可（两者都只是下载 dsh 本身，插件安装仍走 pnpm）：

```sh
npx @deepseek-ai/dsh plugin --profile web add github:2239058652/dsh-loomy-connect
pnpm dlx @deepseek-ai/dsh plugin --profile web add github:2239058652/dsh-loomy-connect
```

### 从本地目录安装（改代码时）

```sh
git clone https://github.com/2239058652/dsh-loomy-connect.git
cd dsh-loomy-connect
pnpm install
pnpm run build          # 仅改了 src/ 时需要，产物在 lib/
dsh plugin --profile web add /绝对路径/dsh-loomy-connect
dsh web
```

验证：

```sh
dsh --profile web --dump-config     # 应出现 llm-loomy 条目
```

`--dump-config` 只组合配置树，不实例化插件。确认插件能否真正启动，需运行 `dsh web` 后检查模型选择器中是否出现 **Loomy**。

## 登录

打开 **设置 → 插件 → DSH Loomy Connect**：

1. 状态行若显示「未登录」，卡片下方会出现「登录 Loomy 账号」。
2. 填手机号，点「发送验证码」。
3. 填入收到的 6 位验证码，点「登录」。

登入后：

| 状态行标签 | 含义 |
|---|---|
| `Loomy 账号` | 插件持有自己的账号登录态，积分为实时数据，右上角有「退出登录」 |
| `桌面 App` | 正在复用 Loomy 桌面端的登录态，积分读自本地缓存 |

**用桌面端登录态时会同时显示登录表单**——登录一次即可切换到账号模式，积分随之变成实时。两种模式都能正常对话，区别只在积分新鲜度。

### 凭证优先级

```
插件自身账号登录态  →  Loomy 桌面端登录态  →  未登录（对话请求返回 502）
```

账号登录态保存在 `~/.dsh/loomy-account.json`（可用 `DSH_HOME` 改变父目录）。该文件只含 session 与账号 id，权限 `0600`。

### 会话有效期

Loomy 的会话 **14 天后失效，且没有 refresh token**。到期后界面上会显示未登录，重新走一次短信登录即可。

## 配置

路径按平台自动探测，一般无需配置。**只有在使用桌面端登录态时**，下面的覆盖项才有意义；账号登录模式不读任何本地文件。

以下覆盖项面向非标准安装。

| 变量 | 覆盖对象 |
|---|---|
| `LOOMY_AUTH_FILE` | 登录态 `auth-session.json` 路径 |
| `LOOMY_CONFIG_FILE` | 模型清单 `opencode.json` 路径 |
| `LOOMY_LOCAL_STORAGE_DIR` | 积分缓存 `Local Storage/leveldb` 目录 |
| `DSH_HOME` | 账号登录态的父目录（默认 `~/.dsh`） |
| `LOOMY_AK_ID` / `LOOMY_AK_SECRET` | 账号服务的签名密钥对（仅当官方客户端换了常量时才需要） |

每项查找的优先级：**插件配置（`authFile` / `configFile`）→ 环境变量 → 探测到的默认值**。

默认路径按 macOS / Windows 顺序探测，取第一个存在的：

| 平台 | 登录态 | 模型清单 | 积分缓存 |
|---|---|---|---|
| Windows | `%APPDATA%/loomy/auth-session.json` | `%APPDATA%/loomy-opencode/opencode.json` | `%APPDATA%/loomy/Local Storage/leveldb` |

## 安全边界

| 边界 | 机制 |
|---|---|
| 网络暴露面 | 网关仅绑定 `127.0.0.1` |
| 客户端鉴权 | 进程内随机密钥，`timingSafeEqual` 比较 |
| DNS 重绑定 | `Host` 必须为 loopback |
| 跨站简单请求 | 携带 `Origin` 时须为 loopback；请求体须为 `application/json` |
| Token 保管 | Loomy session token 只在宿主侧持有：账号模式存于 `~/.dsh/loomy-account.json`（`0600`），桌面模式仅在网关内按需从磁盘读取。两种模式都不会把 token 交给浏览器 |
| 登录表单 | 验证码与 session 不经过页面：浏览器只发手机号/验证码，宿主换取 session 并落盘，回给页面仅「成功/失败」与脱敏手机号 |

威胁模型：防御本机其他进程与浏览器中运行的网页；**不**防御以同一用户身份运行的代码——其可读取插件所读的同样文件。

## 已知限制

- 依赖 Loomy 与讯飞账号服务的非公开接口，Loomy 更新后插件可能需要随之调整。
- 会话 14 天到期且无 refresh token，到期需重新短信登录；插件不会替用户保存密码。
- 只实现短信登录，未实现密码登录（需账号在讯飞账号中心单独设置密码，无法从插件引导完成）。
- 模型清单与倍率取自 Loomy 的接口；接口不可达时回落到 Loomy 生成的配置文件，两者都不可用时才使用内置快照。
- 使用桌面端登录态时积分读自 Loomy 的本地缓存，会滞后；改用账号登录后积分走实时账本接口。
- 模型清单在启动时读取，Loomy 侧增删模型后点一次「刷新」或重启 DSH 即可同步。
- 图片输入需要宿主提供 attachment 服务（`@deepseek-ai/dsh-attachment` 的默认组合已内置）；未挂载该服务的 headless 组合下，含图片的请求会被拒绝。
- 与上游 [gdrpzym/dsh-loomy-connect](https://github.com/gdrpzym/dsh-loomy-connect) 注册同一个 `loomy` provider，**不能同时安装**；两者切换时需先卸载再装。
- Windows 下若桌面端登录态路径未被探测到，需通过 `LOOMY_AUTH_FILE` 手动指定（仅影响桌面模式）。

## 故障排查

| 现象 | 原因 |
|---|---|
| 「插件配置」下始终无卡片 | 宿主端未注册命名空间，见 [docs/internals.md](docs/internals.md#浏览器端) 第 4 项 |
| 插件列表有条目但无卡片 | 同上——「插件」tab 反映已安装条目，非已提供命名空间 |
| 启动时报 `Cannot read properties of undefined (reading 'authFile')` | 缺少运行时 `Config` 导出，见 [docs/internals.md](docs/internals.md#cordis-config-schema) |
| 发验证码报「手机号格式不正确」 | 只接受 11 位大陆手机号，不带 `+86` |
| 填了验证码仍提示未登录 | 会话已写入但 DSH 未重读；刷新页面或重启 DSH |
| 登录后提示「登录态没能写入磁盘」 | `~/.dsh` 不可写；会话仅本次进程有效，重启后需重新登录 |
| 卡片显示未登录（明明刚登录过） | 会话已超过 14 天，重新走一次短信登录 |
| 每次对话请求均 `502` | 两种模式下都没有有效会话：先登录，或检查桌面端是否登录过 |
| 模型列表陈旧 | 点「刷新」或重启 DSH |
| 积分为空 | 桌面模式下 Loomy 尚未缓存积分摘要，或 `LOOMY_LOCAL_STORAGE_DIR` 配置有误；账号模式下多为会话失效 |

## 深入文档

架构、网关、浏览器卡片的实现约束与踩坑记录见 [docs/internals.md](docs/internals.md)（英文版 [docs/internals.en.md](docs/internals.en.md)）。

## 许可

[MIT](LICENSE)

## 免责声明

- 本项目**仅供个人学习和研究使用**，仅驱动使用者本人的 Loomy 账号在本机调用，请勿用于商业用途或超出个人合理使用的场景。
- 使用者须遵守 Loomy 服务条款；因使用本项目产生的一切后果（包括但不限于账号被限制、额度被清空、服务中断）由使用者自行承担。
- 作者不对因使用或滥用本项目导致的任何直接或间接损失负责。
- 本项目与 Loomy、讯飞（iFlytek）、DeepSeek 均无关联，未获其授权或认可；文中名称仅用于描述兼容关系，商标权利归各自所有者。

## 致谢

- [gdrpzym/dsh-loomy-connect](https://github.com/gdrpzym/dsh-loomy-connect)（MIT）：本项目的上游基线 `0.2.0`，provider 注册、回环网关、登录态解析、模型目录与积分读取的实现来源。
- [Patrick130306/loomy2api](https://github.com/Patrick130306/loomy2api)：讯飞账号服务的 HMAC-SHA1 签名规则与登录接口（`getPuKey` / `sendMsgCode` / `checkCode`）的协议参考。本项目只移植了短信登录与积分账本两条调用，未引入其代码或依赖。
- DSH provider 架构参考 [dsh-workbuddy-connect](https://github.com/corrinehu/dsh-workbuddy-connect)（MIT）。
