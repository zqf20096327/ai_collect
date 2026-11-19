# Antigravity Suite

> **给 Google Antigravity 桌面端（macOS）加实用功能的小工具——不修改官方安装包，不影响官方升级，随时可关。**

装好后，你的 Antigravity 会多出下面 **6 样实用功能**：

1. **📱 手机/电脑远程控制（四通道融合配对）**：在手机或另一台电脑上扫码就能聊、传图、批命令，支持 `局域网` / `Tailscale` / `Bonjour` / `Cloudflare 隧道`（免登录 4G/5G 外网直连或自有固定域名）启停门禁，还能看到几台设备连着你。
2. **🇨🇳 全中文界面 + 思考过程自动中译**：装好即变中文，英文思考与会话标题本地自动翻译，可在 `⚙️` 里免重启秒切中英。
3. **📊 上下文与额度看板**：右上角直接看这次对话用了多少上下文，以及 Gemini / Claude 5 小时与每周额度还剩多少。
4. **🔄 自动检测更新 & 一键升级**：有新版时右上角 `⚙️` 会亮小红点，点一下 **「立即更新」**，免重启立刻生效。
5. **⚡ 顺手小工具**：按 **`⌘1`～`⌘9`** 快速切换左侧对话、右侧预览直接改文件并 `⌘S` 保存、`Tab` 一键补全下一步建议、右上角 `>_ CLI` 一键开本地终端。
6. **🛡️ 危险命令红框提醒**：AI 准备运行 `rm -rf`、`git reset --hard`、`sudo` 等高危命令时自动亮红框拦截，必须你亲手确认。

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
     - 未检测到：提醒用户完全退出 Antigravity 并以 `open -a Antigravity --args --remote-debugging-port=9222` 启动（或开启调试端口后重启客户端）。
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

> 可选参数：加 `--no-auto` 只在当前窗口启用，以后打开 Antigravity 时不会自动加载；加 `--no-remote` 关闭手机/电脑远程控制端口。

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
| **右上角 `📱远程`**（有时带数字 `· 1`） | 弹出四通道配对二维码与复选控制（`局域网` / `Tailscale` / `Bonjour` / `Cloudflare 隧道`），支持外网直连、停用通道后端拦截及查看在线关联设备 |
| **右上角 `⚙️`**（有新版本时带小红点） | 换主题配色、切换中英文、配置终端 CLI（含多路复用器目标主机）、管理套餐订阅，以及在有新版本时一键升级 |
| **右上角 `>_ CLI`** | 一键在你常用的 Mac 终端里打开 `agy` 命令行会话（支持 Rex / WezTerm / tmux 指定主机名） |
| **右上角圆环 + `G4` / `C`** | 圆环看这次对话用了多少上下文及 Token 账单图表；`G4` / `C` 看 Gemini 与 Claude 的 5 小时和每周配额 |
| **输入框上方小按钮 & 底部细条** | 上方按钮快速发 `/compact`、`/plan`、导出对话或开关自动确认；底部细条用双比例图标实时看上下文占用率、生成速度与缓存命中率 |
| **输入框右侧导航条 & 右侧 `✏️ 编辑`** | 右侧细条一键跳到顶部/上一轮/下一轮/底部；预览文件时点 **`✏️ 编辑`** 就地修改，按 `⌘S` 直接保存 |

> 💡 **快速切换对话快捷键**：按 **`⌘1`～`⌘9`** 快速切换左侧前 9 个对话（按住 **`⌘`** 键自动浮现序号角标），按 **`⌘⇧[`** / **`⌘⇧]`**（或 **`⌃Tab`**）切换上/下一个对话。

---

## 三、核心功能怎么用？

### 1. 📱 手机 / 电脑远程控制（四通道启停门禁 + Cloudflare 公网隧道）

> **一句话**：一个二维码里同时装了 **多条连接路线**，弹窗支持按行复选启停通道并直连 **Cloudflare 隧道**（4G/5G 免装 Tailscale 也能扫码秒进）；手机端打开后会自动并发测速并切到最快路线，点击顶栏状态也可随时查看延迟并手动测速切换。

1. 在电脑右上角点 **`📱远程`**，弹出配对二维码。
2. 手机用系统相机扫码并在 Safari 打开。
3. 点 Safari 底部 **「分享」→「添加到主屏幕」**——以后从手机桌面图标点开，就是全屏独立体验，支持在对话区向右轻滑切换会话、`+` 号选图或拍照压缩发送。

**4 条连接路线与安全门禁**：
- **整行复选启停 & 后端 `403` 拦截**：点击通道行即可启用/停用对应路线；未勾选的方式不仅从二维码移除，服务端也会直接拒绝该通道来源的调用（返回 `403`）。
- **局域网（Wi-Fi）**：手机和电脑连同一个路由器时速度最快。
- **Tailscale（私网跨网）**：电脑和手机登录同一 Tailscale 账号即可跨网互通。
- **Bonjour（`*.local` 域名）**：路由器重新分配内网 IP 时仍可通过 `电脑名.local` 找到电脑。
- **Cloudflare 隧道（公网 HTTPS）**：勾选开启后支持两种模式（均启用 `--edge-ip-version 4 --protocol http2` 提升稳定性，并内置 3s 快速故障切换）：
  - **免登录临时隧道（默认）**：无需 Cloudflare 账号，自动通过本机 `cloudflared` 在约 3～8 秒内分配 `https://*.trycloudflare.com` 公网入口；开启或从固定域名切换时按钮显示旋转状态与实时提示，并自动屏蔽切换期间的旧固定域名。
  - **自有域名固定隧道**：点行尾 **`固定域名 ▾`**（内置 **`获取 Token ↗`** 一键跳转 Cloudflare Zero Trust 控制台），填入你在 Cloudflare 托管并在 Tunnel **Public Hostname** 绑定到 `http://127.0.0.1:18765` 的自有域名（请勿填写 `*.cloudflareaccess.com` 登录门户，系统会自动拦截并提示），再粘贴保留完整 Base64（`+ / =`）的 `eyJ...`（校验 `{ a, t, s }` / JWT 结构）或完整 `cloudflared service install <token>` 命令即可固定访问。

**自动切最快路线 & 测速切换弹窗**：
- 手机扫码打开或跨通道访问时，客户端会自动并发测试各开启路线的真实延迟，优先切换到更快通道（如同一 Wi-Fi 下从公网隧道自动切回低延迟局域网或 Tailscale），同时在「切换连接方式」弹窗展示**最近一次测速耗时（`ms`）与测速时间**，并提供 **`⚡ 测速`** 按钮供随时重测。

**查看连了多少设备 & 一键踢出旧设备**：
- 右上角按钮会实时显示已配对数量（例如 **`📱远程 · 1`**），点开弹窗就能看到 **`已关联 N 台设备（M 台在线）`** 和具体设备（如 `iPhone`、`iPad`、`Mac`）；同一台设备在 `局域网` / `Tailscale` / `Cloudflare` 间切换时会自动跨通道识别并合并为一台。
- 发现陌生设备或链接不小心发给了别人，点弹窗里的 **「重置密钥」**（或终端运行 `ag-context-meter remote --reset-token`），立刻踢出全部旧设备并作废旧二维码。

**用另一台电脑远程（比如用 MacBook 控制家里 Mac mini）**：
- 在另一台电脑浏览器打开弹窗复制出来的链接（或扫码），宽屏窗口会自动变成**左边常驻会话列表（可收起）、右边居中聊天与宽屏输入框**的双栏界面，直接把图片拖进窗口或按 `⌘V` 粘贴截图就能发给 AI，按 `Esc` 可顺次收起弹层。

<p align="center">
  <img src="assets/mobile-preview.jpg" alt="手机极速 PWA 遥控真机效果（主对话界面与全屏右滑抽屉）" width="88%">
</p>

### 2. 🔄 自动检测更新 & 一键升级

- **不用自己记着检查**：后台会自动对比 GitHub 最新版本；有新版本时，右上角 **`⚙️` 按钮会自动亮起小红点**。
- **怎么升级**：点开 **`⚙️`**，在面板最顶部看到版本对比提示后直接点 **`「立即更新」`**（或在终端运行 `ag-context-meter update`），后台会自动拉取代码并热刷新当前窗口，无需重启 Antigravity。
- **前提注意**：一键更新要求你是通过 **`git clone` 安装**，且**没有自己修改过仓库里的文件**（避免覆盖你的改动）；如果你是下载 zip 压缩包安装的，请重新下载新版覆盖，或改用 `git clone` 安装。

### 3. 🇨🇳 全中文界面 & 中英文秒切

- 装好后菜单、设置弹窗、报错和权限提示会自动变中文；AI 的英文思考过程（Thought）与左侧英文会话标题会自动翻译为中文并缓存在本地，**不消耗任何 AI 模型额度**。
- 正在展开阅读某段思考时，新消息进来也不会突然帮你折叠回去；手动重命名过的会话标题也会自动保留。
- 想临时切换回英文：点右上角 **`⚙️`** → 语言选择 **`English`**，立刻全部切回英文，无需重启。

### 4. 📊 看懂上下文与配额看板

- **右上角圆环**：代表当前这次对话已经用了多少上下文容量；点开可以查看今日 / 本月 / 本年 Token 用量、52 周使用热力图以及按 API 价格估算的参考费用。
- **`G4` / `C` 胶囊**：代表 Gemini 4 与 Claude/GPT 套餐剩余额度；点开能看 **5 小时窗口** 和 **每周总限额** 双进度条以及准确重置时间。卡片右上角的 **「最紧 XX%」** 取 `min(5 小时剩余%, 每周剩余%)`，即决定当前模型池何时触发限流的短板剩余比例。
- **输入框底部细条**：采用占用率 + 缓存命中率双比例 SVG 图标，实时显示当前模型窗口上限（如 `1M` / `512k` / `128k`）、上下文占用率、每秒生成速度（`tok/s`）与缓存命中率。
- **统一设置与订阅面板**：`⚙️` 面板内置主题配色、中英文秒切、`>_ CLI` 终端多路复用配置及账号套餐订阅信息表单（所有输入框与下拉框已统一为 `28px` 高度对齐）。

> **小抄**：**上下文** = AI 这一轮会话里还能“记住”的文字长度；**Token** = AI 计费与计量单位，大约对应一小段字词；**配额** = 你的账号在当前时间窗口内还能用多少额度。

### 5. ⚡ 顺手小工具 & 🛡️ 危险命令红框拦截

- **适配 Antigravity `2.32.x` / `2.33.0` 与防抖浮窗**：完整兼容新版桌面端对话侧栏（`conversation-row-sidebar`）、输入框栏（`.surface-composer`）与回复节点结构（`agent-response`），并在后台健康巡检期间保持已展开浮窗稳定不误关。
- **快捷键极速切换对话**：按 **`⌘1`～`⌘9`** 直接切换到左侧列表第 1～9 个对话（按住 **`⌘`** 键不松时，左侧前 9 个对话右侧会自动浮现序号提示；已避开 `⌘⇧3/4/5` 系统截图键）；按 **`⌘⇧[`** / **`⌘⇧]`**（或 **`⌃Tab`** / **`⌃⇧Tab`**）可循环切换到上一个 / 下一个对话。
- **右侧预览直接改文件**：查看右侧 `.md` 方案或代码时，顶栏点 **`✏️ 编辑`** 即可原地修改，按 **`⌘S`** 直接保存回本地硬盘，点 **`↩️ 完成`** 退出并刷新预览。
- **`Tab` 补全下一步建议**：AI 回复完、输入框空着时，会自动推荐 2～4 句下一步可以怎么接；按 **`Tab` 或 `→`** 直接填入，**`↓`/`↑`** 切换，**`Esc`** 隐藏。
- **一键开本地终端 (`>_ CLI`)**：自动探测 Terminal、iTerm2、Ghostty、Warp、Kitty、WezTerm、cmux 等终端并支持指定 Rex / WezTerm / tmux 多路复用器目标主机 (`muxHost`) 拉起 CLI。*（提示：设置里的 `--dangerously-skip-permissions` 免审核开关打开后命令行执行不再逐条询问，日常建议保持关闭，仅在测试或隔离目录使用。）*
- **高危命令红框强拦截**：AI 准备执行 `rm -rf`、`git reset --hard`、`git clean -f`、`git push`、`sudo`、`kill -9`、`DROP/DELETE`、`op item` 等危险操作时，确认卡片会亮起醒目红框和警示条；就算你打开了右上角「自动确认」，高危步骤也会强制停下等你亲手决定。

---

## 四、日常命令与彻底卸载

### 日常命令

> **记住区分这两条**：`stop` = **只关这一次**（下次打开 Antigravity 还会自动挂载）；`auto-off` = **关闭自动挂载**（以后打开 Antigravity 也不再自动启动）。

| 命令 | 作用 |
| :--- | :--- |
| `ag-context-meter status` | 查看各模块是否已生效、随客户端自启状态，以及 `app.asar` 是否未被本套件修改 |
| `ag-context-meter remote` | 在终端打印四通道配对链接、Cloudflare 隧道状态、已关联设备统计与二维码（支持 `--tunnel on|off` / `--reset-token` / `--json`） |
| `ag-context-meter update` | 从 GitHub 拉取最新版本并自动热刷新运行中的 Antigravity 窗口 |
| `ag-context-meter live` | 立即把增强功能挂载到当前打开的 Antigravity 窗口 |
| `ag-context-meter stop` | **本次暂时关闭**：停止后台桥接并恢复纯英文原版界面（下次启动软件会自动恢复加载） |
| `ag-context-meter auto-off` | **关闭随软件自启**，并卸下当前窗口全部增强界面 |
| `ag-context-meter auto-on` | 重新开启“打开 Antigravity 自动挂载”，并立即加载一次 |

### 怎么彻底卸载？（4 步清干净）

```bash
# 1. 关闭自启并停止当前挂载
ag-context-meter auto-off

# 2. 删除开机/随客户端自启配置
rm -f ~/Library/LaunchAgents/com.$(id -un).ag-live-helper.plist

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
| **装完右上角没出现 `📱远程` 和 `⚙️`** | 1. 终端跑一次 `ag-context-meter status`；<br>2. 如果提示未连接，完全退出 Antigravity（`⌘Q`），用这条命令带调试端口重开：`open -a Antigravity --args --remote-debugging-port=9222`；<br>3. 再跑一次 `ag-context-meter live`。 |
| **终端提示 `ag-context-meter: command not found`** | 说明 `~/.local/bin` 还没加进终端 `PATH`，运行：<br>`echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| **手机扫码打不开页面** | 1. 打开电脑右上角 **`📱远程`**，确认当前使用的连接通道处于勾选启用状态（未勾选的通道会被后端拒绝并返回 `403`）；<br>2. 看手机和电脑是否在**同一个 Wi-Fi**（走 Tailscale 则确认同账号已连接），不在同网段时可勾选开启 **Cloudflare 隧道** 后扫码；<br>3. 若本地连接仍受阻，检查系统防火墙是否放行 `18765` 端口或切换通道直选入口。 |
| **固定域名扫码停在 `/#/NoAuth` 或报错** | `*.cloudflareaccess.com` 是 Cloudflare Zero Trust 登录门户，不是隧道转发域名。若无自有域名请点 **「改用免登录临时隧道」**（等待 3～8 秒分配 `*.trycloudflare.com`）；若有托管在 Cloudflare 的自有域名，请在 Zero Trust → Networks → Tunnels → 对应隧道 → **Public Hostname** 新增子域名指向 `http://127.0.0.1:18765` 后再填入该子域名。 |
| **点「立即更新」提示失败** | 确认你是用 `git clone` 安装的（zip 下载不支持自动拉取），并且自己没有改过仓库目录里的代码。 |
| **想临时变回全英文原版界面** | 点右上角 **`⚙️`** 把语言切回 `English`，或在终端运行 `ag-context-meter stop`。 |

---

## 六、安全说明、进阶细节与开源致谢

### 为什么这套方案比较安全？

1. **绝不修改官方软件**：不解包、不改写 `Antigravity.app` 内的 `app.asar`，保留苹果原装签名。
2. **远程控制默认私网隔离 + 四通道门禁与口令保护**：默认仅允许局域网 / Tailscale / Bonjour 私网访问；公网 **Cloudflare 隧道（HTTPS）** 仅在用户主动勾选后启用；所有未勾选通道都会在后端被直接拒绝（`403`）。每次请求与配对链接均校验 48 位随机口令（支持一键「重置密钥」），固定隧道 Token 仅写入权限为 `0600` 的本机 `remote-config.json`（接口绝不回显明文，亦支持通过 `TUNNEL_TOKEN` 环境变量传入）。
3. **翻译与设置保存在本地**：翻译缓存与配置仅存于本机 `~/Library/Application Support/AntigravityContextMeter/`；文件编辑器通过黑名单禁止访问常见系统目录与密钥目录（重要项目仍建议搭配 Git 使用）。

<details>
<summary>🔧 展开查看：进阶与安全实现细节（监听端口、响应头、Windows/Linux 用法与上游同步）</summary>

- **远程服务监听与安全响应头**：默认启用 IPv4/IPv6 双栈 `[::]:18765` 监听并按四通道（`lan` / `tailscale` / `bonjour` / `tunnel`）识别请求来源与强制门禁拦截（未启用通道返回 `403`）；私网入口严格校验本机回环或 RFC1918/CGNAT 来源并核验 `Origin`；页面下发 `Content-Security-Policy` 与 `X-Content-Type-Options: nosniff`，设备标识可结合 `X-AG-Device-Hint` 区分桌面端 UA 的现代 `iPad`。
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
