# Antigravity Suite

**简体中文** · [English](docs/README.en.md) · [日本語](docs/README.ja.md) · [한국어](docs/README.ko.md) · [Español](docs/README.es.md)

> **给 Google Antigravity 桌面端（macOS）加装实用增强套件——纯外挂运行，绝不修改官方安装包与系统签名，不影响官方升级，随时可关。**

装好后，你的 Antigravity 会多出下面 **7 样实用功能**：

1. **🇨🇳 全中文界面 + 思考自动中译**：不耗额度本地翻译缓存，可在 `⚙️` 免重启秒切中英。
2. **📱 手机 / 电脑远程遥控（比官方快得多）**：同网毫秒级直连、扫码即用，跨网聊、传图、批命令不转圈。
3. **⚡ 快捷指令与提示词优化**：常用口令一键发送（`填入` / `⚡直发`），支持一键润色与下一步推荐。
4. **🧰 桌面顺手小工具**：`⌘1`～`⌘9` 秒切对话、原地改文档保存（`⌘S`）与一键开本地终端。
5. **📊 容量看板与防卡死压缩**：实时盯紧记忆余量与 `G4`/`C` 额度，快满时自动整理防卡顿。
6. **🛡️ 危险命令红框拦截**：`rm -rf`、`git reset --hard`、`sudo` 等高危操作强制人工放行。
7. **🔄 自动检测更新 & 一键升级**：有新版时右上角 `⚙️` 亮红点，点一下免重启热生效。

<p align="center">
  <img src="assets/mac-preview.png" alt="Antigravity Suite macOS 桌面端真实全景效果" width="100%">
</p>
<p align="center"><sub>图注：左栏 <code>⌘1</code>～<code>⌘9</code>、右上角状态栏、底部快捷胶囊与右下悬浮导航条均为本套件增强区域</sub></p>

快速跳转：[一、核心功能](#一核心功能) · [二、怎么安装](#二怎么安装二选一) · [三、日常命令与卸载](#三日常命令与彻底卸载) · [四、常见问题](#四遇到问题怎么办) · [五、安全与致谢](#五安全说明进阶细节与开源致谢)

---

## 一、核心功能

### 1. 🇨🇳 全中文界面 & 中英文秒切

- 装好后菜单、设置弹窗、报错和权限提示会自动变中文；AI 的英文思考过程与左侧英文会话标题会自动翻译并缓存在本地，**不消耗任何模型额度**。
- 正在展开阅读某段思考时，新消息进来不会突然帮你折叠回去；手动重命名过的会话标题也会自动保留。
- 想切回英文原版：点右上角 **`⚙️`** → `终端与通用` → 语言选 **`English · 英文原版`**，无需重启立刻生效。

### 2. 📱 极速手机 / 电脑远程控制（比官方快得多）

> **为什么比官方快很多？**
> - **本地直连不绕远路**：同 Wi-Fi 局域网毫秒级直连，外出自动并发测速挑最快路线（Tailscale 私网 / 免登录 Cloudflare 隧道），告别官方云端中转反复转圈。
> - **超轻量网页秒开秒切**：专为手机与远程浏览器精简，切会话时仅取消旧页面未加载完的数据读取（不打断后台 AI 运行），长对话按需加载与流量压缩，翻几百轮全量历史依然顺滑跟手。
> - **扫一次码即用**：点电脑右上角 **`📱远程`** 扫码并「添加到主屏幕」，点开就像原生 App 一样秒进，多端同开也互不卡顿。

- **怎么打开**：手机点桌面端右上角 **`📱远程`** 扫码，用 Safari **「分享」→「添加到主屏幕」** 即可全屏像原生 App 一样秒进（支持右滑切会话、`+` 传图或拍照压缩发送）；另一台电脑浏览器打开同一链接自动适配宽屏，支持直接拖图、`⌘V` 贴图与 `Esc` 收起弹层。
- **怎么选线路**（在 **`⚙️` → `📱 远程设置`** 勾选实时生效，未勾选的通道会自动拒绝访问）：
  - **同 Wi-Fi 下**：开 **局域网 Wi-Fi** 或 **Bonjour**（内网免记 IP），毫秒级直连。
  - **出门在外**：默认开启 **免登录 Cloudflare 临时隧道**（3～8 秒分配外网入口），也可连自己的 **Tailscale 私网**（*自有固定域名与 Token 进阶配置见文末折叠区*）。
- **远程端顺手体验**：按项目分组浏览与无损上翻全量历史，支持在 `$HOME`（`~`）安全边界内建新项目、浏览项目文件树与本会话变更/产物；输入框上方带**单行横滑快捷口令栏**（与桌面端自定义口令同步，支持 **`⚡直发 / ✎填入`** 一键切换与草稿防误发保护）；支持排队消息查看 / `⚡立即发送` / 单条撤回、通用文件与图片上传及直点预览、交互式单选/多选确认卡（含高危持久放行二次确认）以及侧栏未读红点与审批铃铛；顶栏查看容量与累计用量（支持 9 处界面开关）；多标签页独立切会话不串草稿，主题与深浅模式同步桌面端；默认 `Enter` 换行、`Cmd/Ctrl + Enter` 发送（带 Safari 中文输入法防误触），怀疑泄露可一键重置令牌作废全部旧链接。

<p align="center">
  <img src="assets/mobile-preview.jpg" alt="手机极速 PWA 遥控真机效果（主对话界面与全屏右滑抽屉）" width="88%">
</p>

### 3. ⚡ 输入框快捷指令与提示词优化

- **14 个内置常用指令**：在 **`⚙️` → `终端与通用` →「快捷提示词」** 按场景分组（**`🔥 日常高频`**、**`🚀 复杂攻坚`**、**`🛠️ 会话工具`**），鼠标悬停看中文说明，点一下自动填入输入框。
- **自定义快捷词 & 10 条热门模板（区分 `填入` 与 `⚡直发`）**：自定义区可一键添加 10 条高频口令或点 **`+ 新增`** 自由编写：

  | 模式 | 点击效果 | 适合场景 | 热门模板默认项 |
  | :--- | :--- | :--- | :--- |
  | **`填入`** | 只把文字放进输入框，不发送 | 需要继续粘贴报错日志、截图或补充细节 | `修复这个报错`、`按这个需求做` |
  | **`⚡直发`**（末尾带 `↵`） | 点一下直接发出去 | 无需补充参数的高频短口令 | `直接实现`、`用中文回答`、`继续`、`不要解释`、`跑一下`、`优化一下`、`为什么不行`、`再改一版` |

  > **防误发保护**：按住 **`⌘/Ctrl + 点击`** 可临时反转本次行为；输入框已有草稿时自动防吞跳过直发，并支持勾选「内置免参指令点击直接发送」；悬停清晰标明 `自定义 · 填入` 或 `自定义 · ⚡直发`。

- **提示词一键优化（`✨ 优化` / `↩ 撤回`）**：发送区旁点击 **`✨ 优化`**，会优先选用低延迟、轻量且有余量的快模型把口语整理为清晰结构；优化后保留 **`↩ 撤回`** 按钮，随时还原原文。
- **`Tab / →` 智能推荐下一句**：AI 回复完且输入框为空时，右侧自动浮现 2～4 句应景短句（例如 AI 写英文推 **`用中文回答`**，报错推 **`修复这个报错`** / **`为什么不行`**，改完未运行推 **`跑一下`**，对话快满时自动置顶 `/compact` 压缩）；按 **`Tab` / `→`** 填入、**`↓` / `↑`** 切换、**`Esc`** 隐藏。

<p align="center">
  <img src="assets/composer-preview.png" alt="输入框快捷指令、场景补全与一键优化特写" width="96%">
</p>

### 4. 🧰 桌面顺手小工具

| 工具 | 快捷操作 / 入口 | 干嘛用 |
| :--- | :--- | :--- |
| **对话秒切** | `⌘1`～`⌘9` / `⌘⇧[` / `⌘⇧]` / `⌃Tab` | 长按 `⌘` 显示序号角标瞬切左侧前 9 个对话（已避让截图键），或前后切会话 |
| **悬浮消息导航** | 对话区右侧悬浮条 | 一键跳回顶部、底部或上一轮 / 下一轮消息 |
| **原地改文档** | 右侧预览栏 `✏️ 编辑` + `⌘S` | 看 `.md` 方案或代码时就地编辑保存，点 **`↩️ 完成`** 刷新预览 |
| **一键开终端** | 右上角 `>_ CLI`（可在 `⚙️` 按需开启） | 自动识别 Terminal、iTerm2、Ghostty、Warp、Kitty、WezTerm、cmux 拉起 `agy` 会话 |
| **统一设置与主题联动** | 右上角 `⚙️` | 自由开关各处界面入口，切换 5 套配色或深浅三态（手机远程端同步联动） |

<p align="center">
  <img src="assets/shortcuts-preview.png" alt="⌘1～⌘9 对话秒切与悬浮消息导航特写" width="58%">
</p>

### 5. 📊 上下文看板、240K 防卡死压缩 & 328K 缓存脱落预警

> **30 秒看懂概念**：**上下文** = AI 这轮会话还能记住的内容容量（越满越慢）；**缓存命中** = AI 复用前文记忆的加速状态（归零时要重头慢读一遍）；**配额** = 你的账号当前周期还能用的额度。

- **右上角圆环看板**：一眼看当前对话占了多少上下文容量；点开查看今日 / 本月 / 本年 Token 统计、52 周热力图及参考费用。
- **`G4` / `C` 配额胶囊**：实时追踪 Gemini 4 与 Claude/GPT 的 **5 小时窗口** 和 **每周总限额** 双进度条与精确重置时间；卡片右上角 **「最紧 XX%」** 取两者最小值，直接反映最容易触发限流的短板余量。
- **防卡死能量条（输入框底部）**：双比例细条（占用率 + 缓存命中率）实时监测是否发生缓存归零（0%）或逼近 `328K` 缓存失效雪崩区，不被历史平均值误导。
- **240K 防卡死自动压缩（默认开启）**：官方默认快装满（**512K**）才整理，往往超过 250K～330K 后一旦缓存过期就要重头重算、卡顿 4～5 分钟。套件在达到 `240K` 或缓存失效且输入框为空时，自动发一次 `/compact` 提前减负（可在 **`⚙️` → `终端与通用`** 开关）。

<p align="center">
  <img src="assets/quota-preview.png" alt="右上角上下文圆环与 G4/C 配额胶囊、输入框底部缓存命中率能量条特写" width="84%">
</p>

### 6. 🛡️ 危险命令红框拦截

- 当 AI 准备执行 `rm -rf`、`git reset --hard`、`git clean -f`、`git push`、`sudo`、`kill -9`、`DROP/DELETE`、`op item` 等高危命令时，确认卡片会自动亮起醒目红框与警示条。
- 就算你打开了右上角「自动确认」，高危步骤依然会强制停下，必须由你亲手点击放行。

### 7. 🔄 自动检测更新 & 一键升级

- 后台自动对比 GitHub 最新版本，有更新时右上角 **`⚙️`** 会亮起小红点。
- 点开 **`⚙️`** 直接点顶部的 **「立即更新」**（或在终端跑 `ag-context-meter update`），即可自动拉取代码并热刷新当前窗口，无需重启 Antigravity。
- **前提**：一键更新需通过 **`git clone` 安装**，且本地未修改仓库代码（若通过 zip 下载，请改用 `git clone` 或重新覆盖安装）。

---

## 二、怎么安装？（二选一）

运行环境：**macOS + Google Antigravity（兼容 `2.32.x ～ 2.34.0`）+ Node.js `22.4.0+`**（选方式 1 可让 AI 自动检查补齐；手动安装若未装 Node，可先运行 `brew install node@22`，常见版本管理器均自动兼容）。

### 方式 1：复制一句话发给你的 AI Agent（最省心）

把下面这段话直接发给 Antigravity / Claude Code / Codex，它会自动完成检查和安装（新版 `2.33.0+` 装完按提示重启一次 Antigravity 即可生效）：

```text
请帮我安装并配置 https://github.com/iamvicliu/antigravity-suite 这套 Antigravity 免改包增强套件。
请克隆到 ~/.local/share/antigravity-suite，并严格按照仓库 README.md 中折叠的「AI Agent 自动安装执行规范」完成环境检查、安装与开启随客户端自启。
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
   git clone https://github.com/iamvicliu/antigravity-suite.git ~/.local/share/antigravity-suite
   cd ~/.local/share/antigravity-suite
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
git clone https://github.com/iamvicliu/antigravity-suite.git ~/.local/share/antigravity-suite
cd ~/.local/share/antigravity-suite
./scripts/setup-macos-cdp.sh
```

> 可选参数：`--no-auto` 只在当前窗口启用（以后不再自动加载，也可搭配 `ag-context-meter install-launcher` 生成桌面增强启动器）；`--no-remote` 关闭远程控制端口。

**第 2 步：把命令注册进终端**（否则下一步会提示找不到命令）

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**第 3 步：验证安装是否成功**

```bash
ag-context-meter status
```

看到 **「中文汉化：✅ 已生效」** 且右上角出现 **`📱远程`** 和 **`⚙️`** 就装好了。如果当前软件没变化（Antigravity `2.33.0+` 默认关闭调试端口），**请先按 `⌘Q` 彻底退出再重开一次 Antigravity**（或运行 `ag-context-meter restart`）即可生效；仍有问题请看下方第四节。

---

## 三、日常命令与彻底卸载

### 日常命令

> **记住区分这两条**：`stop` = **只关这一次**（下次打开 Antigravity 还会自动挂载）；`auto-off` = **关闭自动挂载**（以后打开 Antigravity 也不再自动启动）。

| 命令 | 作用 |
| :--- | :--- |
| `ag-context-meter status` | 查看各项增强是否生效、自动加载状态，以及官方软件未被修改 |
| `ag-context-meter remote` | 在终端打印扫码配对链接、隧道状态、已连设备与二维码（支持 `--tunnel on\|off` / `--reset-token` / `--json`） |
| `ag-context-meter update` | 从 GitHub 拉取最新版本，免重启刷新当前 Antigravity 窗口 |
| `ag-context-meter stop` | **临时关闭这一次**：立刻恢复纯英文原版界面（下次打开软件会自动恢复） |
| `ag-context-meter auto-off` | **关闭随软件自启**，并卸下当前窗口全部增强界面 |
| `ag-context-meter auto-on` | 重新开启“打开 Antigravity 自动挂载”，并立即加载一次 |
| `ag-context-meter restart` | 重启 Antigravity 并加载增强功能（装完界面没出来时用，适配 `2.33.0+`） |
| `ag-context-meter live` | 立即把增强功能加载到当前已打开的 Antigravity 窗口（加 `--no-remote` 可关闭远程端口） |
| `ag-context-meter install-launcher` | （可选）在 `~/Applications` 生成「Antigravity 增强启动器.app」，适合关闭自动加载的用户点击启动 |

### 怎么彻底卸载？（4 步清干净）

```bash
# 1. 关闭自启并停止当前挂载
ag-context-meter auto-off

# 2. 删除自动加载配置（LaunchAgents）与桌面启动器
rm -f ~/Library/LaunchAgents/com.$(id -un).ag-live-helper.plist
rm -rf ~/Applications/"Antigravity 增强启动器.app"

# 3. 删除命令行快捷方式
rm -f ~/.local/bin/ag-context-meter

# 4. 删除程序目录（请勿删错路径）
rm -rf ~/.local/share/antigravity-suite
# 如果你是从旧版本升级、装在旧目录，可一并清理 ~/.local/share/antigravity-context-viewer
```

*可选*：如果你希望连同翻译缓存、远程配对密钥和个人设置一起清空，再多跑一条：

```bash
rm -rf ~/Library/Application\ Support/AntigravityContextMeter
```

---

## 四、遇到问题怎么办？

| 遇到的情况 | 先做什么 |
| :--- | :--- |
| **装完右上角没出现 `📱远程` 和 `⚙️`** | 1. 先按 `⌘Q` 彻底退出并重开软件（新版需由自启程序带参拉起）；<br>2. 仍未出现时在终端跑 `ag-context-meter status` 按提示排查（老版本升级可执行 `ag-context-meter auto-on && ag-context-meter live`）。 |
| **终端提示 `ag-context-meter: command not found`** | 说明 `~/.local/bin` 还没加进终端 `PATH`，运行：<br>`echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| **手机扫码打不开页面** | 1. 打开 **`⚙️` → `📱 远程设置`**，确认对应连接通道已勾选启用；<br>2. 确认手机与电脑在**同一 Wi-Fi**（或已连同一 Tailscale），不在同网段时确认 **Cloudflare 隧道** 已开启（缺 `cloudflared` 可按设置页引导一键安装）；<br>3. 若仍受阻，检查系统防火墙是否放行 `18765` 端口或切换其他路线测速。 |
| **固定域名扫码停在 `/#/NoAuth` 或报错** | **仅自建固定域名用户**：误填了 `*.cloudflareaccess.com` 登录页。无自有域名请切回「免登录临时隧道」；有自有域名请在 Zero Trust Tunnels 的 **Public Hostname** 绑定子域名指向 `http://127.0.0.1:18765`（详见文末折叠区）。 |
| **点「立即更新」提示失败** | 确认是通过 `git clone` 安装的（zip 下载不支持自动拉取），且仓库目录没有本地未提交改动。 |
| **想临时变回全英文原版界面** | 点右上角 **`⚙️`** → `终端与通用` 把语言切回 `English`，或在终端运行 `ag-context-meter stop`。 |

---

## 五、安全说明、进阶细节与开源致谢

### 为什么这套方案比较安全？

1. **绝不修改官方软件**：不解包、不改写 `Antigravity.app` 内的 `app.asar`，完整保留苹果原装签名。
2. **通道门禁与 48 位随机口令**：默认仅放行已勾选通道（未选返回 `403`），所有请求均校验 48 位随机令牌并支持一键重置；不需要外网隧道时，可在 `⚙️` 随时关掉 Cloudflare 隧道或启动时传 `--no-remote` 关闭远程端口。
3. **数据与权限全留本地**：翻译缓存和设置仅存在本机；文件在线编辑与远程目录浏览均严格锁定在 `$HOME` 与已登记工作区范围内，并自动阻止访问系统目录与常见密钥凭据路径（重要项目仍建议搭配 Git 使用）。

<details>
<summary>🔧 展开查看：进阶与安全实现细节（端口与响应头、固定隧道 Token、交互与 CLI 参数、Windows/Linux 与上游同步）</summary>

- **远程服务监听与安全门禁**：默认监听 IPv4/IPv6 双栈 `[::]:18765`，按 `lan` / `tailscale` / `bonjour` / `tunnel` 识别来源并拦截未勾选通道（返回 `403`）；私网请求校验回环或 RFC1918/CGNAT 来源与 `Origin`，页面下发 `Content-Security-Policy` 与 `X-Content-Type-Options: nosniff`。
- **多端会话隔离与性能优化**：设备标识结合 `X-AG-Device-Hint` 与 `X-AG-Client-Id` 同时实现跨通道同设备合并与多浏览器页面隔离（状态改变操作经桌面端串行队列执行）；后台聚合主会话与 Subagent 状态并维护 `remote-session-catalog.json` 防缩水持久列表及权限模式图标联动，切会话时仅取消旧页面未完成的快照拉取（不影响后台 AI 运行），并用折叠思考惰性挂载、轨迹签名缓存与 `gzip` 响应压缩加速长历史加载。
- **固定隧道 Token 校验与落盘规范**：输入界面内置 `获取 Token ↗` 直达入口，保留完整 Base64（`+ / =`）并校验 `eyJ...` / `{ a, t, s }` 或 JWT 结构，兼容整条 `cloudflared service install <token>` 命令；Token 仅写入权限为 `0600` 的本机 `remote-config.json`（接口永不回显明文，亦支持通过 `TUNNEL_TOKEN` 环境变量传入）。
- **交互细节与 CLI 终端配置**：自定义直发内置 `800ms` 防连点锁；`Tab / →` 场景推荐短句超长自动截断为 8 字并支持悬停查看全文；右上角 `>_ CLI` 支持在设置中配置默认启动模型、Rex / WezTerm / tmux 远程主机与按需开启免询问参数。
- **桌面端兼容与守护自愈机制**：完整适配 Antigravity `2.32.x ～ 2.34.0` 的 `conversation-row-sidebar`、`.surface-composer`、`agent-response` 与 Lexical 命令胶囊，巡检期间不误关已展开浮窗；macOS LaunchAgent 采用 `SingletonSocket` + `StartInterval=5` 零 Node 快路径毫秒级巡检，支持 `nvm` / `fnm` / `volta` / `asdf` / `mise` 真实 Node 路径自动发现，并在 `RELAUNCH_LOCK_FILE` 写入两列 `"ts pid"` 防抖、避让 `ShipIt` 自动更新且跳过 30 秒老会话保护；一键更新前校验 `.git` 与洁净工作区再执行 `git pull --ff-only` 与热重载。
- **文件读写安全边界**：行内编辑与远程目录浏览均通过 `realpathSync` 校验路径规范化，强制限制在 `$HOME` 与已登记工作区边界内，阻止读写 `/System`、`/usr`、`/etc`、`Antigravity.app` 及 `.ssh` / `.gnupg` / `1Password` / `.gemini` 等凭据路径，并拦截 Symlink 逃逸与悬空软链。
- **Windows / Linux 手动使用**：`setup-macos-cdp.sh` 与 `~/Library/LaunchAgents/` 后台自启为 macOS 专属；Windows / Linux 用户安装 Node.js 22.4+ 并让 Antigravity 以远程调试端口启动后，进入仓库目录手动运行 `node cli.js live` 也可加载核心面板增强逻辑（`node cli.js status` 查看状态）。
- **检查 6 个上游参考仓库**：可运行 `ag-context-meter upstreams` 与本地基线 [`scripts/upstreams.json`](scripts/upstreams.json) 比对。如想让 AI Agent 帮你安全合入参考项目更新，可对 Agent 说：
  > `请运行 ag-context-meter upstreams --json，过滤掉改写 app.asar / 二进制解锁的提交，把安全可吸收的新词条、新模型价格或好用的交互移植进项目并更新 scripts/upstreams.json 基线。`
- **内置 Agent 提速规则**：仓库附带 [`docs/fast-io-AGENTS.md`](docs/fast-io-AGENTS.md)（源自 `oil-oil/agy-fast-io`），通过只读白名单命令、同轮并读文件与合并必审命令减少 AI 工具往返耗时，可按需合并到个人全局规则中。

</details>

### 参考与致谢（Credits & Acknowledgements）

#### 核心协作者（Core Contributors）

感谢两位核心协作者在扫码配对、远程控制与交互体验上的深度优化与持续打磨：

| 协作者 | 主要优化与增强 |
| :--- | :--- |
| **[@hubo1989](https://github.com/hubo1989)** | 深度优化扫码配对与远程通道控制（四通道门禁开关、默认免登录 Cloudflare 隧道与固定域名引导、多浏览器会话隔离），并优化设置中心分页整合、中英切换体验与 `v2.32+` 界面兼容 |
| **[@Shens](https://github.com/Shens)** | 深度优化远程控制交互与性能（全屏自适应、深浅三态外观、多项目分组会话与全量历史无损上翻、排队消息管理、通用文件上传与直点预览、交互式确认卡与状态红点/铃铛、安全边界内远程建项目、子 Agent 状态汇总与 `gzip` 压缩），并优化 macOS 自启守护与非 Homebrew Node 兼容 |

#### 上游参考项目（Upstream Projects）

本套件吸收并整合了社区多位作者与贡献者的开源成果，谨此致谢：

| 参考项目 | 作者 / 贡献者 | 参考与吸收内容 |
| :--- | :--- | :--- |
| **[elviscjn-cjn/antigravity-context-viewer](https://github.com/elviscjn-cjn/antigravity-context-viewer)** | [@elviscjn-cjn](https://github.com/elviscjn-cjn)、[@Jia131313](https://github.com/Jia131313)、[@Azreal2021](https://github.com/Azreal2021)、[@MoiraToki](https://github.com/MoiraToki)、[@nocoo](https://github.com/nocoo) | 基础框架、顶部上下文圆环看板 (`v0.8.9`)、Token 分类统计与 52 周热力图、API 费用估算、5h+Weekly 双窗口配额与 `0%` 修复 |
| **[akelabs/antigravity-pulse](https://github.com/akelabs/antigravity-pulse)** | [@akelabs](https://github.com/akelabs) | 输入框底部能量条 (`v1.3.2`)：输出速率、缓存命中与 5 小时窗口倒计时 |
| **[n2ns/antigravity-panel](https://github.com/n2ns/antigravity-panel)** | [@n2ns](https://github.com/n2ns) | 模型额度监控 (`v2.8.5`)、Auto-Accept 安全自动确认与 Brain 缓存体积监控思路 |
| **[yiheng8023/antigravity-chinese](https://github.com/yiheng8023/antigravity-chinese)** | [@yiheng8023](https://github.com/yiheng8023) | 适配 Antigravity `2.32+ ～ 2.34.0` (`v3.3.60`) 的中文界面精确词条与安全动态正则规则 |
| **[wycocoyu/agy-context-dashboard](https://github.com/wycocoyu/agy-context-dashboard)** | [@wycocoyu](https://github.com/wycocoyu) | 轻量状态栏排布与 `local-api` 优先存活 PID 凭证校验思路 (`v0.9.7`，已整合去重) |
| **[oil-oil/agy-fast-io](https://github.com/oil-oil/agy-fast-io)** | [@oil-oil](https://github.com/oil-oil) | 桌面端 Fast IO 提速规则 (`v0.2.1`)：免审白名单命令、同轮并读与回合压缩规范 |

---

基于 [MIT License](LICENSE) 开源，所有参考或引入的第三方组件均完整保留其原始版权与开源协议。
