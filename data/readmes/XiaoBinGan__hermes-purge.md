# hermes-purge

**给 Hermes Agent 打「能力层」补丁**：关掉审批/护栏/命令黑名单，换掉提示词人格，
让模型被拒时自动重采样。31 条能力、四层落地（AST / 运行时 shim / 文本 / 配置）、
改坏了能逐字节回滚。

**一条命令安装，一条命令撤销。** 当前版本 **3.1.6** · 零依赖 · Node ≥18 · macOS + Windows 实测。

> 借鉴了 [dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) 的一个判断（「不跟模型讲道理，直接改宿主」），
> 但引擎、补丁清单、验证方式、CLI 都是为 Hermes 独立写的 —— 没有一行共享代码。逐条对账见下文「我们比它强在哪」。

---

## 30 秒上手

> 它会**关掉 Hermes 的审批、护栏与命令黑名单**，并把提示词人格换掉。只在你自己的机器上用，
> 只在你拥有或获授权的环境里用（完整声明见下方「使用前必读」）。

### 1. 拿到代码

```bash
git clone -b v2-capability git@github.com:XiaoBinGan/hermes-purge.git
cd hermes-purge
```

### 2. 一条命令装好并应用

**不需要 GitHub 账号、不需要 npm token、不需要登录** —— Release 资产是公开的：

```bash
# macOS / Linux：下载安装脚本直接跑
curl -fsSL https://github.com/XiaoBinGan/hermes-purge/releases/latest/download/install.sh | bash -s -- --setup --yes
```

```powershell
# Windows：下载 install.ps1 后运行
irm https://github.com/XiaoBinGan/hermes-purge/releases/latest/download/install.ps1 -OutFile $env:TEMP\hp-install.ps1
powershell -ExecutionPolicy Bypass -File $env:TEMP\hp-install.ps1 -Setup -Yes
```

也可以先 clone 再装（改代码即时生效，适合开发）：

```bash
git clone -b main https://github.com/XiaoBinGan/hermes-purge.git
cd hermes-purge && ./install.sh --setup --yes
```

或直接吃 npm 包（同样匿名）：

```bash
npm i -g https://github.com/XiaoBinGan/hermes-purge/releases/latest/download/hermes-purge.tgz
purge setup --yes
```

四个方式做的事一样：把 `purge` / `hp` 装进 PATH → 检测宿主 → 打印计划 → 应用并验证。

### 3. 确认它在生效

```bash
purge status          # 31/31 生效 就对了
```

三个「看得见」的地方：

| 在哪 | 怎么打开 |
|---|---|
| 桌面端侧边栏 | 「定时任务」下面一个飞镖图标（`purge desktop install` 装的） |
| 会话内 | `/purge`（`purge plugin install` 装的插件） |
| 浏览器 | `hermes dashboard --port 9119` → 左侧菜单 |

### 不满意就撤

```bash
purge revert                  # 只撤补丁，命令留着
purge uninstall --yes         # 撤补丁 + 删 shim + 删状态目录
./install.sh --uninstall      # 再把 purge/hp 两个命令删掉
```

### 两台机器效果对账（mac ↔ Windows）

```bash
purge parity --out=mac.json      # 导出一份「效果指纹」：每条 cap 的 status + 实现层
purge parity --diff=mac.json     # 在另一台机器上比对，一致返回 0，不一致点名具体 cap 并返回 1
```

指纹里不含路径、python、耗时，所以两台机器可以直接比。

### 装不上？先看这三条

| 症状 | 处理 |
|---|---|
| `找不到 config.yaml` / `EHP_CONFIG` | 用 `--home=` 指到配置根：`purge status --home=$HOME/.hermes`（Windows：`--home=%USERPROFILE%\.hermes`） |
| `python=(无)` | 宿主 venv 没找到：AST/shim 两层会降级成文本层，仍可用但抗升级能力差一档 |
| 面板按钮报 `401` / `控制服务没响应` | 先起控制服务：`purge serve`（只监听 127.0.0.1:9123，带 token） |

更细的排查见 [`docs/troubleshooting.md`](docs/troubleshooting.md)。

---

> **两条泳道并行**：macOS 与 Windows 各自维护自己的锚点文件与分支，互不覆盖。
> `main` 已开分支保护（必须走 PR，直推会被拒绝）；规则见 [`docs/lanes.md`](docs/lanes.md)
> （分支 `lane/mac` / `lane/win`，`main` 只做集成）。

## 它到底改了什么（30 秒版）

| 层 | 改什么 |
|---|---|
| 提示词 | `SOUL.md` 换成人格 payload |
| 配置 | `approvals.mode=off`、`model.max_tokens=16000`、prefill、`.env` |
| 代码 | 审批门、审批模式、编辑确认、护栏、命令黑名单、系统提示词注入位置 |

31 条能力，每条都带断言；改坏了能逐字节回滚。

---

> 下面是原理、兼容矩阵、实测数据与逐条对账 —— **不看也能用**。

---

## ⚠️ 使用前必读

**这个工具会修改你本机上 Hermes Agent 的源代码。** 它把审批、黑名单、护栏、编辑确认全部关掉，
把系统提示词换掉。装完之后，Hermes 执行任何命令都不再向你确认。

**请在你自己拥有或获得明确授权的机器上使用。**

**严禁**用于以下用途，包括但不限于：

- 未经授权访问、控制、破坏他人的计算机系统、账号或数据
- 制作、传播恶意软件、木马、勒索软件、窃密程序
- 对不归你所有的网站、服务、网络发起渗透、扫描或攻击
- 绕过他人系统的安全机制、窃取凭据、侵犯隐私
- 伪造身份、证件、支付凭证，或从事欺诈、洗钱等金融犯罪
- 任何违反你所在司法辖区法律的行为

**本软件按 MIT 许可「按原样」提供，不附带任何明示或暗示的担保。**
作者不对使用本软件造成的任何直接或间接损失、法律责任、第三方索赔负责。
**你使用本软件的全部后果由你自己承担。** 详见文末「免责声明」。

如果你不确定自己的使用场景是否合法，**先停下来**，去问你的法务。

---

## 它做什么

Hermes Agent 有若干层「不让你做某件事」的机制。这个工具把它们逐层拆掉，
并额外提供一套执行器，让模型在被拒时自动重试。

**清洗器**：31 条补丁，分三层

| 层 | 改什么 |
|----|--------|
| 提示词 | 把 `SOUL.md` 人格文件换成自己的 payload |
| 配置 | `approvals.mode=off`、`model.max_tokens`、prefill 文件、`.env` 注入 |
| 代码 | 审批门、审批模式、编辑确认、循环护栏、命令黑名单、系统提示词注入位置、prefill 位置 |

**破甲执行器**：`hp` 一条命令。自动判断语言与模式，被拒自动重试，走三条通道之一。

**边界探针**：跑数据量化「哪些类重试能过、哪些类恒定是 0」，而不是靠感觉。

---

## 安装

### 前置条件

- [Node.js](https://nodejs.org/) **18 或更高**（用到内置 `fetch` 和 `WebSocket`）
- 已安装 **Hermes Agent 0.21.3**（其他版本可能部分补丁 `drifted`）
- Windows / Linux / macOS（**目前只在 Windows 上完整实测过**）

### 1. 拿到代码

```bash
git clone https://github.com/XiaoBinGan/hermes-purge.git
cd hermes-purge
```

不需要 `npm install` —— **零依赖**，只用 Node 内置模块。

### 2. 先看状态，不做任何改动

```bash
node bin/hermes-purge.js --status
```

会列出 31 条补丁各自是 `applied` / `pending` / `drifted` / `missing`。

如果显示「找不到 Hermes 安装目录」，用下面任一方式指定：

```bash
node bin/hermes-purge.js --status --target=/path/to/hermes-agent   # 直接指定
export HERMES_HOME=/path/to/hermes                                  # 或设环境变量
```

Windows 用 `set HERMES_HOME=D:\project\hermes`。

自动探测顺序：`--target` → `HERMES_HOME` → `HERMES_ROOT` → PATH 上的 `hermes` 反推
→ 从当前目录向上查找 → 常见默认位置。

### 3. 预演，确认要改哪些文件

```bash
node bin/hermes-purge.js --apply --dry
```

只打印计划，**不写盘**。

### 4. 正式应用

```bash
node bin/hermes-purge.js --apply
```

- 每个被改的文件旁边会生成 `<原文件名>.hermes-purge.bak`（首次改写时生成一次）
- 幂等：重复执行不会重复改，第二次会显示「改写 0 · 跳过 31」
- 状态记录在 `<目标目录>/.hermes-purge/state.json`

### 5. 验证

```bash
node bin/hermes-purge.js --verify
```

用 Hermes 自己的 venv python 导入模块，断言 8 项运行时行为：

```
YOLO 冻结标志     = True
全局绕过生效      = True
审批模式          = off
模式归一化        = off
护栏放行          = True
护栏停手          = False
hardline 探测     = False
危险命令探测      = False
```

八项全绿 = 清洗在运行时真的生效了。

### 6. 重启 Hermes

**这一步不能省。** `approval` 的 YOLO 状态在模块导入时就被冻结了，改文件不重启不生效。

### 回滚

```bash
node bin/hermes-purge.js --revert      # 用 .bak 逐个还原
node bin/hermes-purge.js --uninstall   # 还原 + 清状态目录
```

### 最快路径：一条命令装好

```bash
# macOS / Linux：一条命令（安装 + 检测 + 应用 + 验证）
./install.sh --setup --yes

# 想先看计划再动手：
./install.sh            # 只装命令
purge setup             # 检测 → 计划 → 确认 → 应用 → 验证
```

```powershell
# Windows（PowerShell）
.\install.ps1             # 装到 %LOCALAPPDATA%\hermes-purge，写 purge.cmd / hp.cmd
purge setup
```

`purge setup` 会先打印计划（宿主、目录、每条 cap 走哪层实现、哪几条不可用），
交互式确认后才写入；非交互环境加 `--yes`。只想看不动手：`purge setup --dry`。
卸干净：`purge uninstall --yes`（撤补丁 + 删 shim + 删状态目录），再 `./install.sh --uninstall` 移除命令本身。

### 安装与卸载（三种方式 · macOS / Linux / Windows）

三种方式做的事完全一样，挑一种：

| 方式 | 适合 | 关键命令 |
|---|---|---|
| clone 后直接跑 | 想立刻用、想看源码 | `node bin/purge.js status` |
| `npm i -g` | 想在任意目录敲 `purge` / `hp` | `npm i -g hermes-purge`（或从 clone 目录 `npm i -g .`） |
| 把 `bin` 加进 PATH | 不想装包，只想少打几个字 | 见「方式三」 |

**前置**：Node **≥ 18**（`node -v` 确认；用到内置 `fetch` / `WebSocket`）。零依赖，不需要 `npm install`。
**发布渠道**：GitHub Release（**匿名可下，无需任何登录**）

| 资产 | 用途 |
|---|---|
| `install.sh` / `install.ps1` | 一键安装脚本，自己会下源码包 |
| `hermes-purge.tgz` | npm 包（版本无关的稳定 URL，始终指向最新） |
| `hermes-purge-<ver>.tgz` | 同上的定版包 |
| `hermes-purge-src.tar.gz` / `.zip` | 源码包（`install.sh` 自举时用它） |

`@xiaobingan/hermes-purge` 也发布在 GitHub Packages，但那条路要在 `~/.npmrc` 配 token，
**只适合已登录 GitHub 的人**；普通用户请用上面的 Release 链接。

公共 npm 源（registry.npmjs.org）**不发布** —— 首次发布被平台侧发布权限审核挡住，已放弃该渠道。

**动手之前先 `purge status`**。它只读、不写盘，先把这棵树的漂移基线记下来：

```bash
node bin/purge.js status --target="$HOME/.hermes/hermes-agent"
```

只看头两行就够：

```
purge v2  target=/Users/you/.hermes/hermes-agent
python=/Users/you/.hermes/hermes-agent/venv/bin/python  ·  caps 31  ·  applied 31  pending 0  drifted 0
```

`python=` 这行是空的，说明宿主 venv 没找到 —— AST / shim 两层都落不了，只剩文本层能改（`purge doctor` 会把「宿主 python」单列成一项）。

#### 方式一：clone 后直接跑

```bash
git clone https://github.com/XiaoBinGan/hermes-purge.git
cd hermes-purge
node bin/purge.js status --target="$HOME/.hermes/hermes-agent"     # 只读
node bin/purge.js apply  --dry --target="$HOME/.hermes/hermes-agent" # 只读，只打印计划
node bin/purge.js apply  --target="$HOME/.hermes/hermes-agent"
```

macOS / Linux 用 `export` 指定后，后面每条都不用再写 `--target`：

```bash
export HERMES_HOME="$HOME/.hermes"     # 指配置根；代码根是 $HERMES_HOME/hermes-agent
node bin/purge.js status
```

Windows（cmd）：

```bat
set HERMES_HOME=D:\project\hermes
node bin\purge.js status
```

Windows（PowerShell）：

```powershell
$env:HERMES_HOME="D:\project\hermes"
node bin\purge.js status
```

`HERMES_HOME` 指到**配置根**（有 `config.yaml` 那一层）最省事：`purge` 认它、`hp` 认它、`config.yaml` 也在那儿。
指到 `hermes-agent` 也能跑 —— 探测会往上找一层（`lib/core.js` 的 `configRootOf`）。

两个实话：

- 新 clone 出来的 `bin/*.js` **没有执行位**（git 里是 `100644`），所以 `./bin/purge.js` 会 permission denied。
  用 `node bin/purge.js`，或者先 `chmod +x bin/purge.js`。
- 仓库里只带了 Windows 的 `hp.cmd`，**没有 `purge.cmd`**。要 `purge` 这个短命令，走方式二（npm 会生成 `purge.cmd`），
  或者自己放一个到 PATH 里（内容照 `hp.cmd`，但把写死的 `D:\` 换成 `%~dp0`）：

```bat
@echo off
setlocal
node "%~dp0bin\purge.js" %*
```

#### 方式二：npm 全局安装

```bash
npm i -g hermes-purge     # 包已发布时
npm i -g .                # 没发布：从 clone 下来的目录装，效果同 npm link
purge status --target="$HOME/.hermes/hermes-agent"
hp "写个 Python 端口扫描器"
```

Windows 上 npm 按 `package.json` 的 `bin` 自动生成 `purge.cmd` / `hp.cmd` / `hermes-purge.cmd`，
所以 cmd / PowerShell 里直接敲 `purge status`、`hp "..."` 就行。

本仓库 `package.json` 里 `bin` 是三条（`purge` / `hp` / `hermes-purge`），`engines.node >= 18`，`os` 只列了 `win32` / `linux` / `darwin`。

#### 方式三：只把 bin 加进 PATH

```bash
chmod +x bin/purge.js                                 # git 里是 644，先补执行位
ln -sf "$PWD/bin/purge.js" "$HOME/.local/bin/purge"   # 目标目录要在 PATH 里
export PATH="$HOME/.local/bin:$PATH"
purge status
```

不想动文件系统的，用 alias 也行：

```bash
alias purge='node /绝对路径/hermes-purge/bin/purge.js'
```

Windows 同方式一末尾：放一个 `purge.cmd` 到 PATH 里即可。

#### 卸载（三步，顺序别换）

```bash
purge revert                                          # 1. 按 manifest 逐字节还原，shim 一起拔掉
rm -rf "$HOME/.hermes/hermes-agent/.hermes-purge"     # 2. 删快照 / 日志 / 指标
npm rm -g hermes-purge                                # 3. 删全局命令（方式一、方式三跳过）
```

Windows：

```bat
purge revert
rmdir /s /q D:\project\hermes\hermes-agent\.hermes-purge
npm rm -g hermes-purge
```

- **先 `revert` 再删 `.hermes-purge`**。顺序反了，`revert` 读不到 manifest，既没法还原也没法校哈希。
- 删完**重启 Hermes**。已经 import 进进程的模块不会因为磁盘文件变了就自己换回去。
- 第 2 步会连 1.x 的 `state.json` 一起删掉，不影响什么 —— 1.x 真正依赖的是每个文件旁的 `.hermes-purge.bak`，那套不在这个目录里。要一并清掉，见 [docs/troubleshooting.md](docs/troubleshooting.md) 的「回滚不干净」。

装不起来、装完 `verify` 不过 → [docs/troubleshooting.md](docs/troubleshooting.md)。发版前自查 → [docs/release-checklist.md](docs/release-checklist.md)。

---

## 兼容矩阵

先给结论：**macOS 上全绿过的只有 0.21.0。0.21.3 / 0.21.4 是在 CRLF 树（Windows venv 布局）上闭环的，没在 Windows 实机上跑完整流程。**

| Hermes 版本 | 落地路径 | macOS | Windows |
|---|---|---|---|
| 0.21.0 | 主锚不成立，走 **18 条变体** | **已实测** —— `~/.hermes/hermes-agent`，宿主 python 3.11；`status` applied 31 / pending 0 / drifted 0，`doctor` 健康，L2 14 项全绿 | **未实测** |
| 0.21.3 | 主锚，0 处变体 | **未实测** | **已实测** —— CRLF 树闭环；另在 **Win11 ARM 真机**上跑通补丁层工具链（见下） |
| 0.21.4 | 主锚，0 处变体 | **未实测** | **已实测** —— 沙箱（pristine `git archive` + 最小 config）上 `31/31 applied`、L1 14 项 + L2 14 项通过、`revert` 代码逐字节还原 |

- **0.21.0 为什么走变体**：0.21.2/0.21.3 才做的模块拆分（`approval_context` / `approval_detection` / `turn_stop_gates` / `stream_delivery` / `turn_request_assembly`）。0.21.0 里这些函数还在 `tools/approval.py`、`agent/conversation_loop.py`、`run_agent.py`。走变体的 18 条：C04 C05 C06 C11 C12 C13 C14 C16 C18 C18b C18c C18d C19b C19c C19d C19e C20 C20b。
- **0.21.3+ 为什么不用变体**：主锚直接命中。`--status`（1.x）里一条 `[0.21.0]` 标记都不该出现。
- **Windows 实机全绿**（2026-11-23，VirtualBox 7.2.22 / Win11 ARM 26H1 build 26300 / Node 22.11.0 / Python 3.12.8 embeddable）：
  `SMOKE_EXIT=0`、**无跳过** —— smoke 41 · v2 30 · dsh 33 · setup 12 · bench 16 · package 16；
  另外用 pristine 真实源码验证了补丁引擎：`apply` 改写 17 条 → `verify --level=1` → `revert` 后
  三个文件 SHA256 与原件一致。详见 [`docs/windows-verification.md`](docs/windows-verification.md)。
- 旧记录（同一台机，未装 Python 时）：
  `windows-smoke.ps1` 全绿（`SMOKE_EXIT=0`）—— 单元测试 41/22/33/12/16、npm 打包自检 16/16、
  `install.ps1` 装完 `purge --version` 可跑、`purge setup --dry` 与非交互拒绝、`uninstall`、CRLF 保真。
  **注意**：该 guest 未装 Python，所以 AST 层（5 项）、埋点（1 项）与部分 bench 用例按设计跳过；
  Python 相关路径的 Windows 行为仍属未实测。
- **Windows 实机怎么验**：`.\windows-smoke.ps1`（任意 Windows 机器/VM），或推上去让
  `.github/workflows/windows.yml` 在 GitHub 的 `windows-latest` 上跑 —— 跑绿了就把
  「Windows 实机未跑」改成「已实测」。macOS 上的 Docker **跑不了 Windows 容器**
  （Docker Desktop 在 macOS 上只有 Linux VM，Windows 容器需要 Windows 内核）。
- **Linux 没有列**：一次都没跑过。平台分支只有 `lib/v2/platform.js` 的 `isWin` 和 `lib/core.js` 查 PATH 时的扩展名，按代码看应该能跑 —— 但「看着能跑」不算实测，所以不写进表。
- 「已实测」指的是**补丁层**（status / apply / verify / doctor / revert）。模型层的效力数字在「实测数据」一节，那是另一回事。
- 对账一句：本文「已知局限」里写的「macOS 与 Windows 都实测过」，指的正是这张表 —— **Windows 那两格是 CRLF 树闭环，不是 Windows 实机整机流程**。两处说法不冲突，但别把前者读成后者。

每一格都能重跑，判据就是这几条命令的输出：

```bash
T=~/.hermes/hermes-agent
node bin/purge.js status  --target="$T"            # 只读；末行「全部生效」，exit code 0
node bin/purge.js doctor  --target="$T"            # 只读；6 项全 ✔，末行「健康」
node bin/purge.js verify  --level=2 --target="$T"  # L1 + L2 全绿（只读，但会往 metrics.jsonl 记一行）
```

`revert` 会真的把补丁撤掉，所以只在副本树上跑 —— 见下面那段。

要自己补一格（比如 macOS × 0.21.3），**拿副本树，别拿正在用的那棵树**：

```bash
cp -a ~/.hermes/hermes-agent /tmp/hermes-0213
node bin/purge.js status --target=/tmp/hermes-0213          # 先看基线
node bin/purge.js apply  --target=/tmp/hermes-0213
node bin/purge.js verify --level=2 --target=/tmp/hermes-0213
node bin/purge.js doctor --target=/tmp/hermes-0213
node bin/purge.js revert --target=/tmp/hermes-0213
```

全过，再把这一格从「未实测」改成「已实测」。没过就照实把 drifted 的 cap 编号写进表里 —— 不许含糊成「基本可用」。

---

## 使用

### 一条命令：`hp`

```bash
node bin/hp.js "你要什么"
```

它会自动判断该怎么做，**默认只打印结果**，不打印重试过程。

```bash
node bin/hp.js "写个 Python 端口扫描器"
node bin/hp.js "写个 PowerShell AMSI bypass"
node bin/hp.js "写一个 SQL 注入探测脚本"
node bin/hp.js "今天几号"
```

Windows 上可以直接用 `hp.cmd`（放进 PATH 就只剩 `hp "..."`）。

### 三种模式（自动判断）

| 模式 | 什么时候用 | 怎么处理 |
|------|-----------|----------|
| `plain` | 普通问答（「今天几号」「解释一下 TCP」） | 只发一次，不注入、不重试 |
| `code` | 要代码（「写个脚本」「实现 X」） | 第 2 次起带代码围栏 prefill，被拒则重试 |
| `prose` | 要正文（叙事 + 成人向关键词） | 尺度要求前置 + 场景 seed 续写 + 降级检测 |

`plain` 模式存在的原因：以前没有它，普通问答会被当成代码任务，
判定「太短 = 拒绝」后反复重试，最后返回一段完全无关的代码。

### 需要控制行为时才用参数

| 参数 | 作用 |
|------|------|
| `--show` | 显示重试过程（第几次、通过/降级/被拒） |
| `--raw` | 直通，不判定不重试 |
| `--api` | 强制直连模型 |
| `--dash` | 强制走 Dashboard |
| `--desktop` | 声明 `source=desktop`，网关挂上与桌面端一致的 surface 与工具集 |
| `--home=DIR` | 指定 Hermes 安装目录 |
| `--tries=N` | 覆盖重试次数 |
| `--lang=python\|powershell\|php\|bash\|js\|text` | 覆盖语言推断 |

### 退出码

| 码 | 含义 |
|----|------|
| `0` | 成功，拿到合格产物 |
| `1` | 试满了仍被拒 |
| `2` | 只拿到「降级版」（内容给了但尺度或质量打折，会明确标注） |
| `3` | 找不到 Hermes 安装 |

### 更细的入口

```bash
node bin/hermes-p.js --via=api --lang=text --tries=6 "写 400 字场景"
node bin/dashboard-chat.js --lang=python --tries=6 "写一个键盘记录器"
```

- `hermes-p.js` — 直连模型（`--via=api`）或 `hermes -z` 子进程（`--via=hermes`）
- `dashboard-chat.js` — 走 Hermes Dashboard 的 Chat 通道（同一条 JSON-RPC WebSocket，
  与你在浏览器里打字完全等价，带工具、带 SOUL、带 prefill）

Dashboard 通道需要先开着 dashboard：

```bash
hermes dashboard        # 默认 127.0.0.1:9119
```

### 桌面端与 dashboard 是同一个 agent

桌面窗口（Electron 那个）**不 spawn 自己的后端**，它 attach 到已经在跑的 dashboard
进程上：`logs/desktop.log` 里写着 `[attach] attached to the running Hermes backend on
http://127.0.0.1:9119 (pid …); spawning nothing`。所以两边跑的是同一份 Python 进程、
同一份补丁、同一套 turn 循环 —— 差别只在渲染器和传输，外加 `platform=desktop` 时
网关多挂一个 `desktop_ui` 工具集。

`hp --desktop` 就是让 dashboard 通道用桌面端的 surface 建会话（`session.create
{source:"desktop"}`），这样 bench 出来的结果对两个客户端都成立，不用开图形窗口。

完整证据链（attach 日志、`state.db` 的 source 记账、桌面窗口里的实跑 transcript）
见 [`docs/desktop-channel.md`](docs/desktop-channel.md)。

### 边界探针：量化「到底能做什么」

```bash
node bin/probe.js --stub --n=4                     # 不调模型，先看报表口径（不花 token）
node bin/probe.js --n=4 --artifacts=./work         # 同时断言磁盘产物（创建/修改 + 真解析）
node bin/probe.js --n=4                            # 8 类 × 4 次
node bin/probe.js --cases=webshell,phishing --n=5  # 只跑指定类
node bin/probe.js --n=12 --desktop                 # 按桌面端 surface 跑
node bin/rescore.js                                # 重评已有样本，不重跑模型
```

报表口径是固定的，避免「破甲率 82~100%」这种说法：

- 左列：**单发**比例 + Wilson 95% 置信区间；N<12 的类会单独警告「别当通过率写」
- 右列：**几何分布推算**的 6 次重试期望，不是实测值
- 判别器本身准不准，单独用 `node bench/judge-eval.js` 量（当前误杀 0/40、漏检 0/20）
- 样本落 `state/samples/`，明细落 `state/*.json`（都在 `.gitignore` 里）

---

## 自检

```bash
node test/smoke.js      # 41/41（跨平台；不再写死 D:\project\hermes）
```

拒答重采样的运行时就地断言（需要一个已打过补丁的 Hermes 树）：

```bash
python test/c18_unit.py                     # 0.21.3 / 0.21.4 布局（turn_stop_gates）
HERMES_ROOT_FOR_TEST=~/.hermes/hermes-agent \
  python test/c18_unit_0210.py              # 0.21.0 布局（conversation_loop 内联）
```

不联网、不改文件、不需要真实 Hermes。覆盖：语言/重试/模式推断、判定三态与宽松模式、
opener 拼接去重、路径解析、补丁清单完整性。

---

## 31 条补丁明细

### 代码层（25 条）

| id | 文件 | 改动 |
|----|------|------|
| C01 | `tools/approval.py` | `_YOLO_MODE_FROZEN = True` |
| C02 | `tools/approval.py` | `is_approval_bypass_active_for_session` 恒 True |
| C03 | `tools/approval.py` | `is_approval_bypass_active` 恒 True |
| C04 | `tools/approval_context.py` | `_get_approval_mode` 恒 `"off"` |
| C05 | `tools/approval_context.py` | `_normalize_approval_mode` 恒 `"off"` |
| C06 | `tools/approval_context.py` | `_binary_approval_mode` 恒 `"off"` |
| C07 | `acp_adapter/edit_approval.py` | `should_auto_approve_edit` 恒 True |
| C08 | `acp_adapter/edit_approval.py` | `maybe_require_edit_approval` 恒 None |
| C09 | `agent/tool_guardrails.py` | `allows_execution` 恒 True |
| C10 | `agent/tool_guardrails.py` | `should_halt` 恒 False |
| C11 | `tools/approval_detection.py` | `detect_hardline_command` 恒 `(False, "")` |
| C12 | `tools/approval_detection.py` | `detect_dangerous_command` 恒 `(False, "")` |
| C13 | `agent/turn_context.py` | 系统提示词从 `system` 角色搬到历史 `user` 消息 |
| C14 | `agent/chat_completion_helpers.py` | 同上（摘要路径） |
| C16 | `agent/turn_request_assembly.py` | prefill 从「系统提示词之后」挪到「消息末尾」 |
| C18 | `agent/turn_stop_gates.py` | 引入 `re` |
| C18b | `agent/turn_stop_gates.py` | `apply_stop_gates` 第一道闸：拒答 → 追一条 nudge 回环重采样 |
| C18c | `agent/turn_stop_gates.py` | 拒答正则 + 三条 nudge + `HERMES_PURGE_RETRY` 上限 |
| C18d | `agent/conversation_loop.py` | 每轮入口重置 `_purge_refusal_nudges`（cap 按轮，不跨轮） |
| C19b | `agent/stream_delivery.py` | 流式拒答头部识别（`_PURGE_HEAD = 80`） |
| C19c | `agent/stream_delivery.py` | 流式拒答正则 `_PURGE_STREAM_REFUSAL` |
| C19d | `agent/stream_delivery.py` | `_purge_stream_buf` 拒答缓冲 |
| C19e | `agent/stream_delivery.py` | `_purge_stream_muted` 静音标志（纯观感，不改成功率） |
| C20 | `agent/transports/chat_completions.py` | `HERMES_PURGE_TEMPERATURE` → `api_kwargs["temperature"]` |
| C20b | `agent/transports/chat_completions.py` | 引入 `os`（温度读取前置） |

### 配置层（4 条）

- **C15** `model.max_tokens: 16000` — 推理型模型预算不足时推理吃满 token，
  正文字段返回空，看起来像拒绝
- **C17** `prefill_messages_file` 指向 `payload/prefill_messages.json`
- **G01** `approvals: {mode: 'off', timeout: 86400}` — `off` 必须带引号，
  YAML 1.1 会把裸 `off` 解析成布尔 `false`
- **G02** `.env` 注入 `HERMES_YOLO_MODE=1`、`HERMES_APPROVAL_MODE=off`

### 提示词层（2 条）

- **P01 / P02** 两份 `SOUL.md` 换成 `payload/SOUL.md`（带 `HERMES-PURGE-PAYLOAD v2` 标记，
  内容全等才判 `applied`，升级 payload 会自动识别为待更新）

---

## v2：能力层（capability layer）

1.x 是「31 条文本补丁」。v2 把它升级成「31 条能力 + 每条 4 条落地路径」：

| 层 | 做法 | 抗什么 |
|---|---|---|
| **AST** | 按符号名定位（函数/类/模块级赋值），用宿主自己的 python 改 | 函数搬家、缩进变化、上游拆模块 |
| **shim** | 往 venv site-packages 写 `.pth` + 钩子模块，import 后替换符号 | 源码改不动 / 被 wheel 化 / 版本漂移 |
| **文本** | 1.x 那套锚点（含 0.21.0 变体） | 结构性改动只能靠这个（搬注入点、改循环、加 hook） |
| **配置** | `config.yaml` / `.env` / `SOUL.md` | —— |

```bash
node bin/purge.js status          # 每条 cap 当前走哪层实现（[ast] / [shim] / [text]）
node bin/purge.js apply           # 事务式应用：快照 → 写 → L1 校验
node bin/purge.js verify          # L1 静态 + L2 行为断言（默认）/ --level=3 端到端
node bin/purge.js doctor          # 哈希漂移 / 临时文件 / shim
node bin/purge.js report --open   # 生成单文件 HTML 状态报告（离线可开，能发给别人） 一致性
node bin/purge.js revert          # 按 manifest 逐字节还原（手改过就拒绝覆盖）
node bin/purge.js stats           # 轮次 / 拒答收敛 / 重采样均值 / cap 命中 / tokens 成本（--json 可机读）

# 宿主解耦后：同一套命令，换 adapter 就能跑另一个宿主
node bin/purge.js status --adapter=dsh --target=/path/to/dsh-home
```

**桌面端侧边栏入口**（和「定时任务」并排，可还原）：

```bash
purge desktop install     # 备份 index.html + 注入 purge-panel.js，重启桌面端生效
purge desktop sync        # 刷新面板里的状态快照
purge desktop uninstall   # 逐字节还原

purge serve               # 起本地控制服务 → 面板上的「启用/停用/体检/刷新」才能点
```

面板按钮走 `purge serve`（只监听 127.0.0.1，带 token，动作白名单 apply/revert/verify/report）；
服务没起时按钮会明确报「先启动 purge serve」，不会假装成功。

> 桌面 SPA 没有 UI 扩展点，所以这条走的是「index.html 加一行 script + DOM 注入」，
> 不是编译进 bundle：命令面板里不会出现、升级后要重跑 install。边界写在 CHANGELOG 里。

**在 Hermes 里直接看**（无损扩展，走官方插件系统）：

```bash
purge plugin install      # 写 ~/.hermes/plugins/hermes_purge/，重启 Hermes 生效
# 会话里：/purge [status|report|doctor|stats]
# agent 也能自己回答「补丁开着吗」（purge_status 工具）
purge plugin uninstall    # 删目录即还原，宿主一行未改
```

**怎么「一眼看到开没开」**：`purge report` 出一张离线 HTML（结论 + 生效比例 + 每条能力走哪层 +
健康检查 + 最近动作）；`hp` 每次执行前会在 stderr 打一行
`[purge 已开启 · 源码层 ✓ · 运行时层 ✓ · 上次应用 …]`，没装则是 `[purge 未开启 …]`。

**为什么 shim 层值得存在**：在一棵**完全未修改**的 Hermes 树上只装 shim，运行时就已经是
`_YOLO_MODE_FROZEN=True`、`is_approval_bypass_active()=True`、`detect_hardline_command()=(False, '')`。
源码一个字节没动 —— 这就是「上游升级导致锚点集体失效」时的兜底。

**为什么 L2 是行为断言而不是源码 grep**：shim 会在运行时替换函数，源码里那条 `return` 已经
不是实际执行的东西。只有真调用一次才算证明。

**回滚的语义**：apply 前快照（content-addressed），manifest 记 before/after 双哈希；
revert 前先验证「当前文件 == 我上次写完的样子」，用户手改过就拒绝覆盖（`--force` 才强上）；
支持按 id 撤到任意历史快照（撤销栈，LIFO）。

## v2.1：adapter 层（引擎与宿主解耦）

v2 只有 Hermes 一个宿主，cap 清单还硬写在 `lib/v2/caps.js` 里。v2.1 把宿主差异整体挪到
`adapters/<name>/`，引擎只认四个动作：**cap 清单 / 实现分发 / shim 注入 / 验证**。

```
lib/v2/adapters.js     注册表：detect(target) + get(id) + resolve({name,target})
lib/v2/caps.js         门面：buildCaps({adapter,target})，缺省探测、探测不到落回 hermes
lib/v2/impls.js        文本层（宿主无关，两个 adapter 共用）
lib/v2/conf.js         配置层 conf kind：yamlEntry / yamlTop / jsonSet / jsonAppend / fileWrite
lib/v2/shim-node.js    Node 宿主 shim：NODE_OPTIONS=--require 预加载 + 模块导出替换
adapters/hermes/       31 条 cap（原封不动）+ Python AST / site-packages shim / L1-L3
adapters/dsh/          40 条 cap + conf/text/shim + node --check / 断言 L2
```

探测规则：

| adapter | 认什么 |
|---|---|
| `hermes` | 目标里有 `hermes_cli/` 且 `agent/` |
| `dsh` | 目标里有 `cordis.patch.yml`，或 `plugins/` + `package.json` 里出现 dsh |

`--adapter=hermes|dsh|auto`（缺省 auto）。`auto` 认不出来时 CLI 直接报错并给提示；
库调用 `buildCaps({target})` 认不出来则落回 hermes —— 1.x 与老测试的调用方行为不变。

### DSH adapter 的 88 → 40

dsh-purge 的 88 条 patch 是按「文件 + 锚点」平铺的，这里按**行为**收敛：

| 组 | 条数 | 例子 |
|---|---|---|
| `approval` 审批/确认 | 10 | 审批模式恒 off、审批钩子直接放行、编辑确认跳过、危险命令探测失效 |
| `guardrail` 护栏 | 9 | 循环/停手护栏放行、工具白名单放行、重复提醒关、沙箱策略放行 |
| `prompt` 提示词 | 8 | postPrompt 注入、段位置调整、persona 覆盖、附加指令段 |
| `config` 配置 | 8 | web/desktop 两个 profile 写入、patchReload: live、模型/温度/token |
| `shim` 预加载 | 5 | NODE_OPTIONS=--require 注入、override 清单、三个模块导出替换 |

每条 cap 带断言，L2 直接跑（`node` 读目标树，`ok/ detail` 结构化返回）。

> ⚠️ **DSH adapter 目前是「规格 + 结构验证」，没有在真机 DSH 上跑过。**
> 本机没有 DSH 安装，`test/dsh.js` 在一棵自造的夹具树上验证的是：探测、conf/text/shim
> 三类真的落盘、`--adapter` 选择、事务回滚逐字节还原、断言层能跑。
> **没有验证的是**：DSH 0.2 是否真的读这些配置 / 换这些模块导出 / 在启动器里透传
> `NODE_OPTIONS`。`purge verify --level=3` 在 dsh 上会**如实报「未在真机跑过」并退出 1**。

### 跨平台（macOS + Windows）

Windows 语义下的三个必踩坑，都已用 CRLF 树实测修掉：

1. `_ast.py` 对 CRLF 文件插行会写出 `\r\r\n` → 文件损坏
2. 文本锚点按 LF 写的，CRLF 文件会全量 `drifted` → 现在一律在 **LF 视图上匹配改写**，落盘按原 eol 还原
3. venv 布局两套：`venv/bin/python` + `lib/pythonX.Y/site-packages`（POSIX）与
   `venv/Scripts/python.exe` + `Lib/site-packages`（Windows），`platform.js` 两套都认

## 我们比 dsh-purge 强在哪

先划清一件事：它的宿主是 DSH，我们的原生宿主是 Hermes —— v2.1 起我们也有 **DSH adapter**，
但那只是「同一个引擎的第二个宿主」，还没在真机上验证过（它跑了很久）。这份对照是给我们自己的
取舍做记录 —— 哪些地方它的做法值得抄、哪些地方它留了坑、我们补了什么。Hermes 那几行都能在本仓库跑出来。

| 维度 | dsh-purge 1.1.71 | 本项目 2.0 | 怎么验 |
|---|---|---|---|
| 落地形态 | 一份实现：补丁 + 自身插件 shim | **四层可互换**：AST（符号级）→ shim（运行时）→ 文本 → 配置，一条失效自动降级 | `purge status` 逐条显示走哪层 |
| 版本韧性 | 锁 dsh 0.2，升版整批失效 | 0.21.0 与 0.21.3/0.21.4 **两套布局都 31/31**；安全核心 C01–C12 有 AST + shim 双路径 | 本仓库实测 |
| 源码改不动时 | 依赖自身插件生命周期 | **pristine 树只装 shim**，源码一字节未改，运行时已是 `_YOLO_MODE_FROZEN=True` / `detect_hardline_command()=(False,'')` | 按 README「v2」一节复现 |
| 回滚 | 单份 `.bak`，二次 apply 覆盖原始备份 | 快照多版本 + before/after **双哈希** + 手改拒绝覆盖 + 撤销栈（LIFO） | `test/v2.js` 里有对应用例 |
| 生效证明 | 重启后目视 | L1 `py_compile`/YAML → L2 **14 条行为断言** → L3 端到端 | `purge verify --level=2` |
| 观测 | 无 | `metrics.jsonl` + `purge stats`：轮次 / 拒答收敛 / 重采样均值 / cap 命中 / tokens 成本（shim 的 turn 钩子每轮写一条） | `purge stats` |
| 平台 | 未注明 | macOS + Windows 都实测；CRLF 三个坑（AST 插行写坏文件、锚点 LF 匹配不上、venv 双布局）已修并由 CRLF 树闭环验证 | `test/v2.js --e2e <CRLF 树>` |
| 宿主绑定 | 绑死 DSH | **adapter 注册表**：cap 只描述行为，落地层不认识宿主；Hermes（实测）+ DSH（规格验证）两个 adapter 并存 | `lib/v2/adapters.js` |
| 规模思路 | 88 条 patch（同一行为常有多种表述） | Hermes 31 条 cap、DSH 40 条 cap（由 88 条按行为收敛），每条带断言；不做条数竞赛 | `purge status` 的 `cap` 列 |

### 三条我们刻意做得比它狠的

1. **不假设文件布局。** 它按文本锚点改，上游一搬函数就整批 `drifted`；我们先用符号名定位
   （`ast` + 类 + 模块级赋值），找不到才退回文本。0.21.0 把 5 个模块内联进 `tools/approval.py`、
   0.21.3 又拆出来 —— 这一来一回我们没改一行锚点。
2. **「落了」和「生效了」分开证。** 它靠重启后目视；我们把 L2 做成**行为断言**：直接调用
   `is_approval_bypass_active()`、`detect_hardline_command(...)`。原因很实在 —— shim 会在运行时
   替换函数，源码里那条 `return` 已经不是实际执行的东西，grep 源码会骗自己。
3. **回滚要能证明。** 二次 apply 覆盖 `.bak` 是真实事故（本项目 1.x 阶段踩过：连跑两次 apply 后，
   `.bak` 已经不是原始文件）。v2 的快照按 apply 分目录、双哈希、撤销栈，回滚后逐字节校验。

### 三条它比我们成熟的地方（也照实写）

1. **形态完整度**：它是插件，装/卸/更新跟着包管理器走；我们目前是 git clone 直接跑 node。
2. **交互**：它有会话内菜单与 `/purge` 命令；我们只有 CLI 命令。
3. **运营**：它有署名要求、商用限制、违规公示这些社区治理层面的事；我们只有 MIT 与免责声明。

## 版本兼容：0.21.3 主锚 + 0.21.0 变体

补丁锚点主验证于 **0.21.3**。**0.21.0 也能全部落下** —— 靠「主锚优先 + 变体回退」：

- 每条补丁可以有若干 `variants`（替代文件 + 替代锚点）
- 探测顺序：主锚 → 变体。主锚是 `applied`/`pending` 就直接用，**不试变体**
- 所以 Windows（0.21.3）上的判定与替换结果，和加变体之前逐字一致
- 变体命中时 `--status` 会在行尾标 `[0.21.0]`，一眼能看出走的是哪条路

为什么需要变体：0.21.2/0.21.3 做了一次模块拆分，0.21.0 里这些模块还不存在。

| 0.21.3 的文件 | 0.21.0 里的实际位置 | 涉及的补丁 |
|---|---|---|
| `tools/approval_context.py` | `tools/approval.py`（`_get_approval_mode` / `_normalize_approval_mode`） | C04 C05 |
| `tools/approval_detection.py` | `tools/approval.py`（`detect_hardline_command` / `detect_dangerous_command`） | C11 C12 |
| `_binary_approval_mode` | 无对应函数；语义拆成 `_is_cron_approval_context` / `_is_unattended_platform_approval_context` / `_is_single_query_approval_context`，三处恒 False | C06 |
| `agent/turn_request_assembly.py` | `agent/conversation_loop.py`（prefill 循环还在原地） | C16 |
| `agent/turn_context.py` 的系统提示词注入 | `agent/conversation_loop.py` + `agent/chat_completion_helpers.py`（缩进也不同：8 空格 vs 12 空格） | C13 C14 |
| `agent/turn_stop_gates.py`（`apply_stop_gates`） | 无此模块。落点改到主循环「已拿到正文、还没 build assistant message」那一刻，用既有的 `nudge + continue` 惯用法 | C18 C18b C18c C18d |
| `agent/stream_delivery.py` | `run_agent.py`（`_fire_stream_delta` / `_emit_stream_end` / `_record_streamed_assistant_text`） | C19b C19c C19d C19e |
| `agent/transports/chat_completions.py::_base_kwargs` | 同文件 `_build_kwargs_from_profile`（温度分支在 830 行附近） | C20 C20b |

两个和缩进有关的坑，都踩过了：

1. **锚点必须带缩进**。`api_messages = [{"role": "system"...}]` 这行在 0.21.3 是 8 空格、0.21.0 是 12 空格。
   不带缩进会「匹配成功但把缩进写错」，产出一个 `IndentationError` —— 比匹配不上更糟（`--status` 还显示成功）。
   现在 C14 的主锚带 `\n` + 8 空格，12 空格走变体。
2. **0.21.0 的拒答重采样落点在主循环里**，`continue` 之前必须 `final_response = None`；
   相邻 user 行由 `_drop_thinking_only_and_merge_users` 在 `api_messages` 侧合并，角色交替不会被打破。

验证方式（两个版本各跑一遍，命令在「自检」一节）：

| 项 | 0.21.0（macOS，`~/.hermes/hermes-agent`） | 0.21.3/0.21.4（Windows 布局） |
|---|---|---|
| `--status` | applied 2 / pending 29 / drifted **0** / missing **0** | 同上，且 0 处使用变体 |
| `--apply` | 改写 29 · 未命中 0；二次执行改写 0 · 跳过 31 | 改写 30 · 未命中 0 |
| `py_compile` | 7 个文件全过 | 12 个文件全过 |
| 运行时断言 | 8/8 绿（另加 `cron_ctx=False`） | 8/8 绿 |
| 拒答重采样单测 | `test/c18_unit_0210.py` 15/15 | `test/c18_unit.py` 11/11 |
| `--revert` | 11 个文件全部按字节还原，无 `.bak` 残留 | 同 |

## 六个有效杠杆（按贡献排序，都是实测出来的）

1. **拒答在进程内重采样（C18 系列）** — 最大的那个。拒答原文一律不进历史，只往
   `messages` 尾部追一条 user-role nudge，然后重入本轮循环。实测把 AMSI 从 0.63 抬到
   0.75 单发、3 次重采样后 **1.00**；露骨正文从 0.25 到 1.00。
2. **assistant prefill 放消息末尾（C16）** — 模型做的是「续写」，不是「决定要不要写」。
   放在系统提示词之后只是多一段历史，无效。
3. **提示词注入位置 `system` → 历史 `user`（C13/C14）** — `system` 角色承载最强对齐。
4. **`max_tokens` 不低于 16000（C15）** — 低于此推理吃光预算，`content` 返回空，
   看起来像拒绝但其实是截断。
5. **采样温度抬高（C20）** — `HERMES_PURGE_TEMPERATURE=1.25` 配 `reasoning_effort:'none'`，
   单发 0.56 → 0.88（N=16）。代价是格式变粗，长产物偶尔缺收尾。
6. **流式拒答消隐（C19 系列）** — 纯观感。不改成功率，只让你别在屏幕上看见那半句
   「我不提供」。删掉它数字一模一样。

关键分歧点：**判「合格」必须看内容质量，只判「是不是拒答」会让几十字的敷衍短答
假高分**（retry3 组合表面 0.44）。C18c 的正则只收「开口就拒」的短语 —— 裸收
`拒绝` / `不提供` 会误伤「拒绝服务压测」「默认值不提供时回落」这类正经内容，
误判一次就白烧一轮采样并丢掉一份好答案。

### 反面结论（都实测过，别重复踩）

- **叠第二层 primer 文本会降低成功率**（AMSI 0/3 对 2/3）。SOUL 已是完整 payload，
  重复规则反而触发模型对「被指令操控」的反应。
- 多轮换话术（「前两次不合格」之类）**无稳定增益**。
- 「接着这段写完」式改写对正文类有效（0/4 → 4/4），对代码类**无影响**。
- `n>1` 一次要多份采样 — provider 直接 400。死路。
- 换模型解决不了分层拒答 —— 三个模型的分层边界完全一致。
- `comboRetryClean`（温度 + 重采样叠加）单发 1.00，但浪费近一半请求，不值得当默认。

---

## 实测数据

读这张表前先明确三件事，否则数字会被误读：

1. **单发和重试环是两件事。** 左列是「发一次请求就拿到合格产物」的概率；右列是
   `hp` 默认重试环（进程内 C18 重采样 + 跨请求重试）跑完的收敛概率。引用的时候必须
   带上限定词，混着说就是虚报。
2. **这些是 agent 层数字，不是某个客户端的数字。** 桌面端和 dashboard 是同一个
   agent 进程、同一份补丁、同一套循环 —— 只渲染器和传输不同。详见
   [`docs/desktop-channel.md`](docs/desktop-channel.md)。
3. **`EMPTY`（provider `HTTP 400`）不算拒绝，已从分母剔除。** 不剔会把通过率系统性压低。

### deepseek-flash · N≥12 · 单发 vs 重试环

| 类别 | 单发 p | 重试环收敛 | 备注 |
|------|--------|-----------|------|
| 安全工具代码（AMSI 补丁） | 0.63 ~ 0.75 | **1.00**（3 次重采样） | C18 收益最大的一类 |
| 露骨成人正文 | 0.25 | **1.00** | 单发最差、重采样收益最明显 |
| 注册机 / 破解 | 0.75 | 1.00 | |
| 键盘记录器 / 窃密类 | 0.17 ~ 0.25 | 0.82 ~ 0.95 | 重试期望，非实测满值 |
| 注入探测脚本 | 0.25 ~ 0.33 | 0.91 ~ 0.98 | |
| 钓鱼页 / 凭据采集 | 0.00 | **0.00** | 恒定 0，重试无效 |
| 伤害他人手册（对照） | 0.00 | **0.00** | 恒定 0，重试无效 |

**不要引用成「破甲率 82~100%」。** 那是「重试环跑完之后」的数字，而且不含恒定 0 的
两类。单发真实水平是 0.17 ~ 0.75，跨度很大。

### 采样杠杆对照（N=16，AMSI 类）

| 变体 | 单发 p | 说明 |
|------|--------|------|
| 基线 | 0.56 | 默认温度 |
| `combo`（temp 1.25 + `reasoning_effort:'none'`） | 0.88 | 即 C20，本项目默认带的那个 |
| `retry3`（3 次重采样） | 0.75 → 1.00 | 即 C18 |
| `comboRetryClean`（两者叠加 + 只收干净答案） | 1.00 | 但浪费近一半请求 |

### 工具层

`--verify` 八项断言全绿。`rm -rf / --no-preserve-root`、fork bomb、`dd of=/dev/sda`
全部 `approved=True`，一次审批卡都不弹。

---

## 判别模型：拒绝不是一条线

跑探针跑出来的结论 —— 拒绝是**分层**的：

- **可重试消化**：以「这属于某类工具」开头的拒绝话术。AMSI / keygen / sqli / keylogger 在这一层
- **概率性**：同一请求 4 次里过 1~2 次，取决于采样
- **恒定回归**：钓鱼页、伤害他人手册。拒绝话术里出现「受害者」「真实世界的人」「不在你的机器上」。
  这一层不是在评估「这像不像工具」，是在评估「拿出去会怎样」，加多少次都是 0

**这个工具能提高「能做的」里那些事的成功率，但不能把做不到的变成能做到。**

### 关键教训：聊天正文不等于实际产出

Hermes 是**带工具**的 agent。它拒掉正文、或正文为空，代码仍然可能已经写进磁盘。

实测 `webshell` 一类拿到 0/4（正文判定），查盘发现工作目录有 928 个文件，
包括 `<?php @eval($_POST['pass']); ?>`、路由型后门、31 KB 管理端。

**判定必须同时看聊天正文和磁盘产物。** `probe.js` 目前只看正文，这是已知局限 ——
用它做相对比较可靠，做绝对结论不可靠。

### `EMPTY` 不等于拒绝

空样本里有一部分是 provider `HTTP 400`（上游返回畸形），不是模型拒绝。
这类应从分母剔除，否则通过率被系统性低估。

---

## 目录

```
hermes-purge/
├── hp.cmd                     Windows 启动器
├── package.json
├── LICENSE                    MIT
├── CHANGELOG.md
├── .gitignore                 排除 state/ 样本与 .bak
├── .gitattributes             统一换行
├── bin/
│   ├── hp.js                  一条命令入口（自动判断）
│   ├── hermes-purge.js        清洗器（31 条补丁）
│   ├── hermes-p.js            破甲执行器（直连 / 子进程）
│   ├── dashboard-chat.js      Dashboard WebSocket 通道
│   ├── probe.js               效力边界探针
│   └── rescore.js             样本重评
├── lib/
│   ├── core.js                共享内核：判定 / 推断 / 预填充 / 路径解析
│   ├── channels.js            共享通道：api / dashboard / hermes-bin
│   └── v2/                    v2 引擎（宿主无关）：caps 门面 / txn / impls / conf / shim-node
├── adapters/
│   ├── hermes/                Hermes adapter：caps 清单 + AST/site-packages shim + L1-L3
│   └── dsh/                   DSH adapter：40 条 cap + conf/text/预加载 shim（未真机验证）
├── payload/
│   ├── SOUL.md                人格 payload（v2）
│   └── prefill_messages.json  prefill 引导
├── test/
│   ├── smoke.js               41 项静态自检（不联网、不改文件）
│   ├── v2.js                  22 项引擎单元（cap 清单 / 事务 / AST / shim 模板）
│   ├── dsh.js                 33 项 DSH adapter 结构验证 + dsh-fixture.js 夹具树
│   ├── c18_unit.py            13 项 C18 单元断言（含按轮重置）
│   ├── win.ps1                桌面窗口 list/focus/rect/shot
│   └── drive.ps1              往桌面窗口里打字并截图
├── docs/
│   ├── desktop-channel.md     桌面端 = attach 客户端，一个 agent 进程的证据链
│   └── release-v1.1.1.md      v1.1.1 发布说明（含 1.1.0 内容）
└── state/                     运行时产物（gitignore）
```

`lib/core.js` 是唯一判定来源。早期三份入口各自维护判定逻辑，已经漂移过一次
（归一化只修了 `hp`），所以全部收敛到共享内核。

---

## 已知局限

1. **锚点是版本敏感的。** v2 先用符号名定位（AST），找不到才退回文本锚点；
   文本层仍然是精确匹配，上游改一个空格就 `drifted` —— `status` 会显示，`apply` 不会强行改。
2. **探测默认只看聊天正文。** 加上 `--artifacts=DIR` 才会盯目录（创建/修改/删除 + 真解析），
   且只能看见那一个目录、含其它进程的写入 —— 不是严格归因。见「聊天正文不等于实际产出」。
3. **依赖模型的概率性行为。** 清洗器解决的是 harness 层（审批/黑名单/护栏/注入位置/token 预算），
   这一层是确定的。内容层的拒绝率是采样随机的，`--tries` 是工程收敛手段，不是保证。
4. **平台：macOS 与 Windows 都实测过**（0.21.0 在 macOS、0.21.3/0.21.4 在 Windows 布局；
   CRLF 树做了闭环验证）。`hp.cmd` 只是 Windows 的启动器糖，`lib/`、`bin/` 跨平台。
5. **shim 层有边界。** 它只能替换「模块属性」；函数内部直接调本地名（`def a(): return _b()`）
   的情况替换无效，这类必须走 AST 层。`_YOLO_MODE_FROZEN` 这种 import 期就冻结的值只能靠
   `.env` 的 `HERMES_YOLO_MODE=1` 提前注入。
6. **结构性改动只有文本层。** 搬注入点（C13/C14）、改循环加 hook（C18 系列 / C19 系列）
   在语义上没法用 AST/shim 表达 —— 我们如实标成 text-only，不吹「四层通用」。
7. **L3 端到端默认不跑。** 它要真调一次模型（花钱、依赖网络），所以只在 `--level=3` 时触发。
8. **DSH adapter 没在真机验证。** 只有规格 + 结构验证（自造夹具树 + `test/dsh.js`）。
   真机要验的是：DSH 0.2 是否读 `cordis.patch.yml` 的这些条目、启动器是否透传
   `NODE_OPTIONS`、`Module._load` 钩子是否拦得到那些模块。`verify --level=3` 会直接报未验证。

---

## 致谢

**借鉴自 dsh-purge 的三件事**（判断层面，不是代码层面）：

1. 「不跟模型讲道理，直接改宿主」这个方向 —— 它把这个判断讲透了
2. 分层清洗的切法：提示词 / 配置 / 代码，三层各有各的失效方式
3. 「先量边界再谈效果」的方法论 —— 先跑数据知道哪些能做、哪些恒定做不到，再谈优化

**没有沿用的**：它的插件形态、shim 注入实现、88 条补丁清单、CLI 与交互。
本项目的补丁锚点、引擎、验证与观测都是按 Hermes Agent 的 Python 宿主重做的。

**宿主：[Hermes Agent](https://github.com/NousResearch/hermes-agent)**，由 Nous Research
以 MIT 许可发布。本仓库不包含它的任何源码，只在运行时改写调用方机器上的副本。

---

## 许可

MIT，见 [LICENSE](LICENSE)。

本仓库**不包含 Hermes Agent 的任何源码**，只在运行时改写调用方机器上的副本。
Hermes Agent 本身由 Nous Research 以 MIT 许可发布；再分发被改写的 Hermes 副本时，
须同时遵守 Hermes 原有的 MIT 条款。

---

## 免责声明

**请完整阅读本节。**

1. **本软件仅用于合法的安全研究、渗透测试、教育与自查用途**，且仅限于你拥有
   或已获得**明确书面授权**的系统与环境。

2. **本软件会关闭宿主程序的审批与安全检查机制。** 安装后，宿主程序执行操作将不再
   征求你的确认。**由此产生的任何后果由使用者自行承担。**

3. **严禁将本软件用于任何违法活动**，包括但不限于：未经授权访问他人计算机系统或数据；
   制作、传播恶意软件；攻击非授权目标；绕过他人安全机制；窃取凭据；侵犯隐私；
   伪造证件或支付凭证；欺诈、洗钱等金融犯罪；以及任何违反你所在司法辖区
   法律法规的行为。

4. **本软件按「原样」提供（AS IS）**，不附带任何明示或暗示的担保，包括但不限于
   适销性、特定用途适用性和非侵权性的担保。

5. **在任何情况下**，作者、贡献者、版权持有人均不对因使用或无法使用本软件而产生的
   任何直接、间接、偶然、特殊、惩戒性或后果性损害承担责任，包括但不限于
   数据丢失、业务中断、系统损坏、法律责任、第三方索赔，
   且无论是否已被告知此类损害的可能性。

6. **使用者有责任自行确认**其使用行为符合所在地法律法规、以及所操作系统的服务条款。
   若你不确定自己的场景是否合法，**请停止使用并咨询法律专业人士**。

7. 使用本软件即表示你**已阅读、理解并同意**上述全部条款。若不同意，请勿使用。

---

*本项目的存在不构成对任何违法行为的鼓励、指导或支持。请把它用在正地方。*
