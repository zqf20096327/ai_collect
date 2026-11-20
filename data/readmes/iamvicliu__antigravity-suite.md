# Antigravity Suite

**简体中文** · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

> **给 Google Antigravity 桌面端（macOS）加实用功能的小工具——100% 零改包（不修改 `app.asar` 与官方签名），不影响官方升级，随时可关。**

装好后，你的 Antigravity 会多出下面 **6 样实用功能**：

1. **🇨🇳 全中文界面 + 思考过程自动中译（零 Token）**：装好即变中文，英文思考过程与会话标题本地自动翻译并缓存，不消耗任何模型额度，可在 `⚙️` 里免重启秒切中英。
2. **📱 手机/电脑远程控制（四通道 + 默认免登录 Cloudflare 隧道 + 多端隔离）**：扫码即可跨网聊、传图、批命令；支持 `局域网` / `Tailscale` / `Bonjour` / **默认启用的免登录 `Cloudflare 隧道`**（4G/5G 零配置开箱可用，也支持自有固定域名），多浏览器各自独立查看会话互不串扰，并与桌面端同步深浅外观与主题色。
3. **📊 上下文看板、240K 防卡死压缩 & 双窗口配额**：右上角圆环直接看当前上下文容量、每日与 52 周热力图及参考成本；`G4` / `C` 胶囊实时盯紧 Gemini 4 与 Claude/GPT 的 5 小时与每周额度；官方 512K 才压缩极易引发 4～5 分钟卡顿重算，套件默认在 240K 或缓存归零脱落时自动触发 `/compact` 并实时预警。
4. **⚡ 输入框效率套件 & 顺手小工具**：内置 **14 项快捷指令推荐池**（点击 `/compact`、`/plan`、`/goal` 等自动转原生命令胶囊，悬停弹出双行解读）+ 自定义提示词、发送区 **`✨ 优化` / `↩ 撤回`**、`Tab` 下一步建议悬停预览，以及 **`⌘1`～`⌘9`** 切对话、右侧预览 **`⌘S`** 原地编辑与右上角 `>_ CLI`。
5. **🛡️ 危险命令红框拦截**：AI 准备运行 `rm -rf`、`git reset --hard`、`sudo` 等高危命令时自动亮红框强拦截，就算开启了自动确认，也必须你亲手点击放行。
6. **🔄 自动检测更新 & 一键升级**：后台自动对比 GitHub 最新版本，有新版时右上角 `⚙️` 会亮小红点，点一下 **「立即更新」**，免重启立刻热生效。

<p align="center">
  <img src="assets/mac-preview.png" alt="Antigravity Suite macOS 桌面端真实全景效果" width="100%">
</p>

---

## 一、怎么安装？（二选一）

运行环境：**macOS + 已安装 Antigravity + Node.js 22.4 或更高版本**（没装 Node 可在终端运行 `brew install node@22`）。

### 方式 1：复制一句话发给你的 AI Agent（最省心）

把下面这段话直接发给 Antigravity / Claude Code / Codex，它会自动完成检查和安装：

```text
请帮我安装并配置 https://github.com/iamvicliu/antigravity-suite 这套 Antigravity 免改包增强套件。
请克隆到 ~/.local/share/antigravity-context-viewer，并严格按照仓库 README.md 中折叠的「AI Agent 自动安装执行规范」完成环境检查、安装与开启随客户端自启。
完成后运行 ~/.local/bin/ag-context-meter status 向我汇报各项状态，并简单告诉我日常怎么开关和卸载。
```

<details>
<summary>📋 展开查看：AI Agent 自动安装执行规范（人类用户无需阅读）</summary>

如果你是正在替用户安装本套件的 AI Agent，请按序执行以下 4 步，并用通俗中文汇报：

1. **只读预检**
   - 检查 `node -v` 是否为 **`v22.4.0` 及以上**（不足时提示用户或通过 `brew install node@22` 安装）。
   - 检查运行中 Antigravity 调试端口：支持读取 `~/Library/Application Support/Antigravity/DevToolsActivePort`，若受 macOS TCC 权限限制无法读取该目录，CLI 亦内置 `lsof -nP -a -c Antigravity -iTCP -sTCP:LISTEN` 免权回退探测：
     - 已检测到：安装后可**免重启立即热生效**；
     - 未检测到（如 Antigravity `2.33.0+` 默认关闭调试端口）：可由守护进程自动重拉或提醒用户退出后通过 `ag-context-meter restart` / `open -a Antigravity --args --remote-debugging-port=9222` 启动。
2. **下载仓库到本地**
   ```bash
   git clone https://github.com/iamvicliu/antigravity-suite.git ~/.local/share/antigravity-context-viewer
   cd ~/.local/share/antigravity-context-viewer
   ```
3. **运行安装脚本（零改包原则）**
   ```bash
   ./scripts/setup-macos-cdp.sh
   ```
   > **安全核验说明**：
   > - 本套件在 `cli.js` 与 `bin/ag-context-meter` 入口均已禁用改写 `app.asar` 或客户端二进制的命令，仅通过纯内存 CDP 挂载界面。
   > - 若 `~/Library/Application Support` 无写权限，状态缓存自动回退至 `~/.config/antigravity-context-meter`。
   > - 可选参数：`--no-auto` 跳过写入 `~/Library/LaunchAgents/` 开机/随客户端自启；`--no-remote`（或环境变量 `AG_DISABLE_MOBILE_REMOTE=1`）禁用远程控制端口。
4. **验收状态**
   - 运行 `~/.local/bin/ag-context-meter status`，确认各项为 `✅`，并提醒用户若想直接运行 `ag-context-meter` 需将 `~/.local/bin` 加入 `~/.zshrc` 的 `PATH`。

</details>

### 方式 2：终端手动 3 步安装

**第 1 步：下载并运行安装脚本**

```bash
git clone https://github.com/iamvicliu/antigravity-suite.git ~/.local/share/antigravity-context-viewer
cd ~/.local/share/antigravity-context-viewer
./scripts/setup-macos-cdp.sh
```

> 可选参数：加 `--no-auto` 只在当前窗口启用，以后打开 Antigravity 时不会自动加载（也可搭配 `ag-context-meter install-launcher` 创建桌面增强启动图标）；加 `--no-remote` 关闭手机/电脑远程控制端口。

**第 2 步：让 `ag-context-meter` 命令随处可用**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**第 3 步：验证安装是否成功**

```bash
ag-context-meter status
```

看到 **「中文汉化：✅ 已生效」**，且 Antigravity 右上角出现 **`📱远程`** 和 **`⚙️`** 按钮，就装好了。如果没出现，请看下方第五节的排查方法。

---

## 二、装好后点哪里？（6 行界面地图）

| 你在界面上看到的 | 点它有什么用 |
| :--- | :--- |
| **右上角 `📱远程`**（有时带数字 `· 1`） | 弹出四通道配对二维码、链路延迟概览与在线设备列表；通道复选、Cloudflare 隧道配置、重置令牌与远程页 9 项模块显隐均统一收敛在 **`⚙️` → `📱 远程设置`** |
| **右上角 `⚙️`**（有新版本时带小红点） | 统一 5 分页设置面板（`终端与通用` / `外观与主题` / `套餐与订阅` / `远程设置` / `网络与高级`）：支持功能显隐开关、快捷指令池、主题色同步、240K 防卡死开关、订阅账单及一键热升级 |
| **右上角 `>_ CLI`** | 一键在你常用的 Mac 终端里打开 `agy` 命令行会话（支持 Rex / WezTerm / tmux 指定远程主机、默认模型与自动批准选项） |
| **右上角圆环 + `G4` / `C`** | 圆环看这次对话用了多少上下文、Token 分类账单与 52 周热力图；`G4` / `C` 看 Gemini 与 Claude 的 5 小时和每周配额 |
| **输入框效率区 & 底部细条** | 输入框上方显示按场景排序的快捷指令（点击即填入或转原生胶囊，悬停弹出双行解读），发送区旁提供 **`✨ 优化` / `↩ 撤回`**，底部双比例图标条实时看占用率、生成速度、缓存命中与脱落预警 |
| **输入框右侧导航条 & 右侧 `✏️ 编辑`** | 右侧细条一键跳到顶部/上一轮/下一轮/底部；预览 `.md` 或代码时点 **`✏️ 编辑`** 就地修改，按 `⌘S` 直接保存回硬盘 |

> 💡 **快速切换对话快捷键**：按 **`⌘1`～`⌘9`** 快速切换左侧前 9 个对话（按住 **`⌘`** 键自动浮现序号角标），按 **`⌘⇧[`** / **`⌘⇧]`**（或 **`⌃Tab`**）切换上/下一个对话。

---

## 三、核心功能怎么用？

### 1. 🇨🇳 全中文界面 & 中英文秒切

- 装好后菜单、设置弹窗、报错和权限提示会自动变中文；AI 的英文思考过程（Thought）与左侧英文会话标题会自动翻译为中文并缓存在本地，**不消耗任何 AI 模型额度**。
- 正在展开阅读某段思考时，新消息进来也不会突然帮你折叠回去；手动重命名过的会话标题也会自动保留。
- 想临时切换回英文：点右上角 **`⚙️`** → `终端与通用` → 语言选择 **`English · 英文原版`**，立刻全部切回英文，无需重启。

### 2. 📱 手机 / 电脑远程控制（四通道 + 默认免登录公网隧道 + 多端隔离）

> **一句话**：一个二维码里同时装了 **4 条连接路线**，**默认开启免登录 Cloudflare 临时隧道**（4G/5G 零配置扫码秒进）；手机或另一台电脑打开后自动并发测速切到最快路线，且支持多浏览器各自独立查看不同会话。

1. 在电脑右上角点 **`📱远程`**，弹出配对二维码与快速设备概览。
2. 手机用系统相机扫码并在 Safari 打开。
3. 点 Safari 底部 **「分享」→「添加到主屏幕」**——以后从手机桌面图标点开，就是全屏独立体验，支持在对话区向右轻滑切换会话、`+` 号选图或拍照压缩发送。

**4 条连接路线与门禁控制（在 `⚙️` → `📱 远程设置` 统一管理）**：
- **整行复选启停 & 后端 `403` 拦截**：在 `⚙️` → `📱 远程设置` 点选通道即可启用/停用对应路线；未勾选的路线会从二维码移除，服务端也会直接拒绝该通道来源请求（返回 `403`）。
- **局域网（Wi-Fi）**：手机和电脑连同一个路由器时速度最快。
- **Tailscale（私网跨网）**：电脑和手机登录同一 Tailscale 账号即可跨网互通。
- **Bonjour（`*.local` 域名）**：路由器重新分配内网 IP 时仍可通过 `电脑名.local` 找到电脑。
- **Cloudflare 隧道（公网 HTTPS，默认开启）**：默认启用免登录临时隧道（零配置开箱可用，也可随时取消勾选关闭）：
  - **免登录临时隧道（默认）**：无需 Cloudflare 账号，自动通过本机 `cloudflared` 在约 3～8 秒内分配 `https://*.trycloudflare.com` 公网入口；如果本机尚未安装 `cloudflared`，设置页内置 **macOS / Windows / Linux 一键复制安装命令引导** 与「重新检测」按钮，装完即刻连通。
  - **自有域名固定隧道**：在通道展开 **`固定域名 ▾`**（内置 **`获取 Token ↗`** 一键跳转 Cloudflare Zero Trust 控制台），填入你在 Cloudflare 托管并在 Tunnel **Public Hostname** 绑定到 `http://127.0.0.1:18765` 的自有域名（请勿填写 `*.cloudflareaccess.com` 登录门户，系统会自动拦截并提示），再粘贴保留完整 Base64（`+ / =`）的 `eyJ...`（校验 `{ a, t, s }` / JWT 结构）或完整 `cloudflared service install <token>` 命令即可固定访问。

**远程端 `v2.0.0` 新能力**：
- **顶部上下文窗口 & 本机用量抽屉**：远程页面顶栏新增上下文占用与本机累计用量入口，可随时查看当前窗口 Token 构成与互斥配额抽屉。
- **9 项页面内容可配置**：在 **`⚙️` → `📱 远程设置`** →「Remote 页面显示内容」中，可按需开启/隐藏顶部上下文面板、本机已记录用量面板、模型配额胶囊、通道连接元信息、左侧会话抽屉、AI 思考折叠区、底部快捷建议、输入区工具栏（模型/权限）以及待审批横幅。
- **多浏览器 / 多标签页会话隔离**：每个远程浏览器标签使用独立会话标识（`X-AG-Client-Id`），同时开多个浏览器各自切会话、留草稿或筛用量互不串扰（仅发送/执行审批等状态改变操作会通过桌面端安全串行队列执行）。
- **三态外观跟随 & 主题同步**：远程端支持跟随系统 / 浅色 / 深色三态外观，强调色与桌面端动态主题保持一致。
- **自动切最快路线 & 跨通道同设备去重**：打开或切网时自动并发测速切回最快路线（如回到同一 Wi-Fi 自动切回局域网），弹窗展示各路线延迟耗时并提供 `⚡ 测速`；同一台设备在 `局域网` / `Tailscale` / `Cloudflare` 间切换时自动合并统计。
- **一键踢出旧设备**：发现陌生设备或链接泄露，在 `⚙️` → `📱 远程设置` 或终端运行 `ag-context-meter remote --reset-token` 点击 **「重置令牌」**，立刻作废全部旧二维码与旧会话。

**用另一台电脑远程（比如用 MacBook 控制家里 Mac mini）**：
- 在另一台电脑浏览器打开弹窗复制出来的链接（或扫码），宽屏窗口会自动变成**左边常驻会话列表（可收起）、右边居中聊天与宽屏输入框**的双栏界面，直接把图片拖进窗口或按 `⌘V` 粘贴截图就能发给 AI，按 `Esc` 可顺次收起弹层。

<p align="center">
  <img src="assets/mobile-preview.jpg" alt="手机极速 PWA 遥控真机效果（主对话界面与全屏右滑抽屉）" width="88%">
</p>

### 3. 📊 上下文看板、240K 防卡死压缩 & 328K 缓存脱落预警

- **右上角圆环**：代表当前这次对话已经用了多少上下文容量；点开可以查看今日 / 本月 / 本年 Token 用量、52 周使用热力图以及按 API 价格估算的参考费用。
- **`G4` / `C` 胶囊**：代表 Gemini 4 与 Claude/GPT 套餐剩余额度；点开能看 **5 小时窗口** 和 **每周总限额** 双进度条以及准确重置时间。卡片右上角的 **「最紧 XX%」** 取 `min(5 小时剩余%, 每周剩余%)`，即决定当前模型池何时触发限流的短板剩余比例。
- **328K 缓存雪崩与脱落实时预警**：不再让“整轮累计缓存命中”掩盖“当前这一步缓存突然归零（0%）”的风险；底部细条（采用占用率 + 缓存命中率双比例 SVG 图标）与上下文浮窗会实时标记缓存脱落与 328K 临界预警。
- **240K 长上下文防卡死自动压缩（默认开启）**：官方默认要到 **512K** 才触发压缩，但超过 **250K～330K** 后一旦服务端缓存过期（如停顿超 3 分钟），后续每步都会变成全量重算，卡死 **4～5 分钟** 且极速烧光配额。在 **`⚙️` → `终端与通用`** 开启「长上下文防卡死自动压缩」后，只要本轮回答结束且输入框为空，一旦上下文达到 `240K` 或发生缓存脱落，套件便会自动发送 `/compact` 提前压缩历史。
- **统一 5 分页设置面板 & 全站主题联动**：`⚙️` 面板包含 `终端与通用`、`外观与主题`、`套餐与订阅`、`远程设置`、`网络与高级` 5 大分页；在「功能显示开关」可自由隐藏/恢复 6 处界面入口，切换「外观与主题」的 5 套配色或深浅三态后，全站面板、配额胶囊与提示气泡均会实时同步高亮色。

> **小抄**：**上下文** = AI 这一轮会话里还能“记住”的文字长度；**Token** = AI 计费与计量单位，大约对应一小段字词；**配额** = 你的账号在当前时间窗口内还能用多少额度。

### 4. ⚡ 输入框效率套件 & 🛡️ 危险命令红框拦截

- **内置 14 项快捷指令推荐池 & 自定义提示词**：
  - 在 **`⚙️` → `终端与通用` →「快捷提示词」** 中，内置 14 项高频工作流指令（如 `/compact`、`/plan`、`/grill-me`、`/btw`、`/learn`、`/goal`、`/boost`、`/swarm`、`/teamwork`、`/browser`、`/schedule`、重载规则、复制会话 ID、导出 Markdown）统一作为推荐池开关（不可删除，点击即控制显隐），并按 **`🔥 日常高频与上下文`**、**`🚀 复杂攻坚与多 Agent`**、**`🛠️ 会话工具与规则`** 分组及推荐星级（`★必开` / `★推荐`）排列；悬停任意选项，下方**实时解读框**立即展示该指令的「作用」与「场景」。你也可以点「+ 新增」添加个人自定义快捷提示词。
  - 输入框上方快捷栏同步按分组和推荐优先度显示按钮，鼠标悬停**零延迟弹出双行解读气泡**（`/compact` 还会动态标注 240K 自动压缩状态与当前上下文风险）；点击 `/compact`、`/plan`、`/goal` 等斜杠指令时，会自动激活并点选客户端内置的斜杠命令菜单，直接转换成原生命令胶囊（不再只是纯文本）。
- **提示词一键优化（`✨ 优化` / `↩ 撤回`）**：发送区旁新增提示词润色按钮。点击 **`✨ 优化`** 时会优先按低延迟、轻量与剩余配额筛选可用快模型（并支持多模型自动回退），把口语化描述一键整理为结构化提示词；优化完成后保留 **`↩ 撤回`** 按钮与提示，直到你主动编辑、发送或点击撤回还原原文。
- **`Tab` 下一步建议截断 & 悬停预览**：AI 回复完、输入框空着时，会自动推荐 2～4 句下一步追问；超长建议在快捷行自动截断为 `8` 字保持整洁，鼠标悬停即浮现完整全文，按 **`Tab` 或 `→`** 直接填入，**`↓`/`↑`** 切换，**`Esc`** 隐藏。
- **适配 Antigravity `2.32.x` / `2.33.0+` 与 CDP 无感自愈**：完整兼容新版对话侧栏（`conversation-row-sidebar`）、输入框栏（`.surface-composer`）与回复节点结构（`agent-response`），巡检期间不误关已展开浮窗；针对 `2.33.0+` 默认关闭调试端口的情况，随软件自启守护会在安全时机自动检测并无感重拉补开调试端口（支持 `AG_CDP_PORT` 与 `/Applications` / `~/Applications` 自动寻址），若启用 `--no-auto` 无守护模式，也可运行 `ag-context-meter install-launcher` 生成独立启动器图标。
- **快捷键极速切换对话**：按 **`⌘1`～`⌘9`** 直接切换到左侧列表第 1～9 个对话（按住 **`⌘`** 键不松时，左侧前 9 个对话右侧会自动浮现序号提示；已避开 `⌘⇧3/4/5` 系统截图键）；按 **`⌘⇧[`** / **`⌘⇧]`**（或 **`⌃Tab`** / **`⌃⇧Tab`**）可循环切换到上一个 / 下一个对话。
- **右侧预览直接改文件**：查看右侧 `.md` 方案或代码时，顶栏点 **`✏️ 编辑`** 即可原地修改，按 **`⌘S`** 直接保存回本地硬盘，点 **`↩️ 完成`** 退出并刷新预览。
- **一键开本地终端 (`>_ CLI`)**：自动探测 Terminal、iTerm2、Ghostty、Warp、Kitty、WezTerm、cmux 等终端，支持配置默认启动模型、Rex / WezTerm / tmux 远程主机 (`muxHost`) 及 `--dangerously-skip-permissions` 免询问开关（日常建议保持关闭，仅测试或隔离目录按需开启）。
- **高危命令红框强拦截**：AI 准备执行 `rm -rf`、`git reset --hard`、`git clean -f`、`git push`、`sudo`、`kill -9`、`DROP/DELETE`、`op item` 等危险操作时，确认卡片会亮起醒目红框和警示条；就算你打开了右上角「自动确认」，高危步骤也会强制停下等你亲手决定。

### 5. 🔄 自动检测更新 & 一键升级

- **不用自己记着检查**：后台会自动对比 GitHub 最新版本；有新版本时，右上角 **`⚙️` 按钮会自动亮起小红点**。
- **怎么升级**：点开 **`⚙️`**，在面板最顶部看到版本对比提示后直接点 **`「立即更新」`**（或在终端运行 `ag-context-meter update`），后台会自动拉取代码并热刷新当前窗口，无需重启 Antigravity。
- **前提注意**：一键更新要求你是通过 **`git clone` 安装**，且**没有自己修改过仓库里的文件**（避免覆盖你的改动）；如果你是下载 zip 压缩包安装的，请重新下载新版覆盖，或改用 `git clone` 安装。

---

## 四、日常命令与彻底卸载

### 日常命令

> **记住区分这两条**：`stop` = **只关这一次**（下次打开 Antigravity 还会自动挂载）；`auto-off` = **关闭自动挂载**（以后打开 Antigravity 也不再自动启动）。

| 命令 | 作用 |
| :--- | :--- |
| `ag-context-meter status` | 查看各模块是否已生效、随客户端自启状态，以及 `app.asar` 是否未被本套件修改 |
| `ag-context-meter remote` | 在终端打印四通道配对链接、Cloudflare 隧道状态、已关联设备统计与二维码（支持 `--tunnel on|off` / `--reset-token` / `--json`） |
| `ag-context-meter update` | 从 GitHub 拉取最新版本并自动热刷新运行中的 Antigravity 窗口 |
| `ag-context-meter live` | 立即把增强功能挂载到当前打开的 Antigravity 窗口（加 `--no-remote` 可关闭远程端口） |
| `ag-context-meter restart` | 以带远程调试端口方式平滑启动或重启 Antigravity（适配 `2.33.0+`，内置会话内防误杀保护） |
| `ag-context-meter install-launcher` | （可选）在 `~/Applications` 创建「Antigravity 增强启动器.app」，适合 `--no-auto` 无守护用户点击启动 |
| `ag-context-meter stop` | **本次暂时关闭**：停止后台桥接并恢复纯英文原版界面（下次启动软件会自动恢复加载） |
| `ag-context-meter auto-off` | **关闭随软件自启**，并卸下当前窗口全部增强界面 |
| `ag-context-meter auto-on` | 重新开启“打开 Antigravity 自动挂载”，并立即加载一次 |

### 怎么彻底卸载？（4 步清干净）

```bash
# 1. 关闭自启并停止当前挂载
ag-context-meter auto-off

# 2. 删除开机/随客户端自启配置（若创建过增强启动器可一并删除）
rm -f ~/Library/LaunchAgents/com.$(id -un).ag-live-helper.plist
rm -rf ~/Applications/"Antigravity 增强启动器.app"

# 3. 删除命令行快捷方式
rm -f ~/.local/bin/ag-context-meter

# 4. 删除程序目录（请勿删错路径）
rm -rf ~/.local/share/antigravity-context-viewer
```

*可选*：如果你希望连同翻译缓存、远程配对密钥和个人设置一起清空，再多跑一条：

```bash
rm -rf ~/Library/Application\ Support/AntigravityContextMeter
```

---

## 五、遇到问题怎么办？

| 遇到的情况 | 先做什么 |
| :--- | :--- |
| **装完右上角没出现 `📱远程` 和 `⚙️`** | 1. 终端跑一次 `ag-context-meter status`；<br>2. 若提示 `v2.33.0+` 未开启调试端口，按 `⌘Q` 退出重开（随软件自启会自动补参），或在**外部终端**运行 `ag-context-meter restart`；<br>3. 再跑一次 `ag-context-meter live`。 |
| **终端提示 `ag-context-meter: command not found`** | 说明 `~/.local/bin` 还没加进终端 `PATH`，运行：<br>`echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| **手机扫码打不开页面** | 1. 打开 **`⚙️` → `📱 远程设置`**，确认对应连接通道处于勾选启用状态（未勾选的通道会被后端拒绝并返回 `403`）；<br>2. 看手机和电脑是否在**同一个 Wi-Fi**（走 Tailscale 则确认同账号已连接），不在同网段时确认 **Cloudflare 隧道** 已开启（缺 `cloudflared` 可直接按设置页引导一键安装）；<br>3. 若本地连接仍受阻，检查系统防火墙是否放行 `18765` 端口或点开顶栏延迟入口切换其他通道。 |
| **固定域名扫码停在 `/#/NoAuth` 或报错** | `*.cloudflareaccess.com` 是 Cloudflare Zero Trust 登录门户，不是隧道转发域名。若无自有域名请切换回 **「免登录临时隧道」**（等待 3～8 秒分配 `*.trycloudflare.com`）；若有托管在 Cloudflare 的自有域名，请在 Zero Trust → Networks → Tunnels → 对应隧道 → **Public Hostname** 新增子域名指向 `http://127.0.0.1:18765` 后再填入该子域名。 |
| **点「立即更新」提示失败** | 确认你是用 `git clone` 安装的（zip 下载不支持自动拉取），并且自己没有改过仓库目录里的代码。 |
| **想临时变回全英文原版界面** | 点右上角 **`⚙️`** → `终端与通用` 把语言切回 `English`，或在终端运行 `ag-context-meter stop`。 |

---

## 六、安全说明、进阶细节与开源致谢

### 为什么这套方案比较安全？

1. **绝不修改官方软件**：不解包、不改写 `Antigravity.app` 内的 `app.asar`，保留苹果原装签名。
2. **四通道显式门禁 + 口令隔离**：远程控制内置 `局域网` / `Tailscale` / `Bonjour` 私网通道，并默认启用免登录 **Cloudflare 临时隧道（HTTPS）** 以便外网开箱可用；**你可以随时在 `⚙️` → `📱 远程设置` 一键关闭 Cloudflare 隧道（仅保留私网），或启动时传入 `--no-remote` 完全关闭远程端口**。所有未勾选通道都会在后端被直接拒绝（`403`）；每次请求与配对链接均校验 48 位随机口令（支持一键「重置令牌」踢出全部旧设备），固定隧道 Token 仅写入权限为 `0600` 的本机 `remote-config.json`（接口绝不回显明文，亦支持通过 `TUNNEL_TOKEN` 环境变量传入）。
3. **翻译与设置保存在本地**：翻译缓存与配置仅存于本机 `~/Library/Application Support/AntigravityContextMeter/`；文件编辑器通过黑名单禁止访问常见系统目录与密钥目录（重要项目仍建议搭配 Git 使用）。

<details>
<summary>🔧 展开查看：进阶与安全实现细节（监听端口、响应头、Windows/Linux 用法与上游同步）</summary>

- **远程服务监听与安全响应头**：默认启用 IPv4/IPv6 双栈 `[::]:18765` 监听并按四通道（`lan` / `tailscale` / `bonjour` / `tunnel`）识别请求来源与强制门禁拦截（未启用通道返回 `403`）；私网入口严格校验本机回环或 RFC1918/CGNAT 来源并核验 `Origin`；页面下发 `Content-Security-Policy` 与 `X-Content-Type-Options: nosniff`，设备标识结合 `X-AG-Device-Hint` 与 `X-AG-Client-Id` 同时实现跨通道同设备合并与多浏览器页面会话隔离。
- **更新实现细节**：右上角 `⚙️` 一键更新与 `ag-context-meter update` 仅在安装目录具备 `.git` 且工作区无未提交修改时，通过 `git pull --ff-only` 更新后热重载目标窗口；文件行内编辑通过前缀黑名单阻止读写 `/System`、`/usr`、`/etc`、`Antigravity.app` 及 `.ssh` / `.gnupg` / `1Password` 等凭据路径。
- **Windows / Linux 手动使用**：`setup-macos-cdp.sh` 与 `~/Library/LaunchAgents/` 后台自启为 macOS 专属；Windows / Linux 用户安装 Node.js 22.4+ 并让 Antigravity 以远程调试端口启动后，进入仓库目录手动运行 `node cli.js live` 也可加载核心面板增强逻辑（`node cli.js status` 查看状态）。
- **检查 6 个上游参考仓库**：可运行 `ag-context-meter upstreams` 与本地基线 [`upstreams.json`](upstreams.json) 比对。如想让 AI Agent 帮你安全合入参考项目更新，可对 Agent 说：
  > `请运行 ag-context-meter upstreams --json，过滤掉改写 app.asar / 二进制解锁的提交，把安全可吸收的新词条、新模型价格或好用的交互移植进项目并更新 upstreams.json 基线。`
- **内置 Agent 提速规则**：仓库附带 [`rules/fast-io-AGENTS.md`](rules/fast-io-AGENTS.md)（源自 `oil-oil/agy-fast-io`），通过只读白名单命令、同轮并读文件与合并必审命令减少 AI 工具往返耗时，可按需合并到个人全局规则中。

</details>

### 参考与致谢（Credits & Acknowledgements）

本套件吸收并整合了社区多位作者与贡献者的开源成果，谨此致谢：

| 参考项目 | 作者 / 贡献者 | 参考与吸收内容 |
| :--- | :--- | :--- |
| **[elviscjn-cjn/antigravity-context-viewer](https://github.com/elviscjn-cjn/antigravity-context-viewer)** | [@elviscjn-cjn](https://github.com/elviscjn-cjn)、[@Jia131313](https://github.com/Jia131313)、[@Azreal2021](https://github.com/Azreal2021)、[@MoiraToki](https://github.com/MoiraToki)、[@nocoo](https://github.com/nocoo) | 基础框架、顶部上下文圆环看板 (`v0.8.6`)、Token 分类统计与 52 周热力图、API 费用估算、5h+Weekly 双窗口配额与 `0%` 修复 |
| **[akelabs/antigravity-pulse](https://github.com/akelabs/antigravity-pulse)** | [@akelabs](https://github.com/akelabs) | 输入框底部能量条 (`v1.3.2`)：输出速率、缓存命中与 5 小时窗口倒计时 |
| **[n2ns/antigravity-panel](https://github.com/n2ns/antigravity-panel)** | [@n2ns](https://github.com/n2ns) | 模型额度监控 (`v2.8.5`)、Auto-Accept 安全自动确认与 Brain 缓存体积监控思路 |
| **[yiheng8023/antigravity-chinese](https://github.com/yiheng8023/antigravity-chinese)** | [@yiheng8023](https://github.com/yiheng8023) | 适配 Antigravity `2.32+ / 2.33.0` (`v3.3.52`) 的中文界面精确词条与安全动态正则规则 |
| **[wycocoyu/agy-context-dashboard](https://github.com/wycocoyu/agy-context-dashboard)** | [@wycocoyu](https://github.com/wycocoyu) | 轻量状态栏排布与指标展示思路 (`v0.8.16`，已整合去重) |
| **[oil-oil/agy-fast-io](https://github.com/oil-oil/agy-fast-io)** | [@oil-oil](https://github.com/oil-oil) | 桌面端 Fast IO 提速规则 (`v0.2.1`)：免审白名单命令、同轮并读与回合压缩规范 |

---

基于 [MIT License](LICENSE) 开源，所有参考或引入的第三方组件均完整保留其原始版权与开源协议。
