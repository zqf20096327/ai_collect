# Antigravity Suite

**简体中文** · [English](docs/README.en.md) · [日本語](docs/README.ja.md) · [한국어](docs/README.ko.md) · [Español](docs/README.es.md)

> **给 Google Antigravity 桌面端（macOS）加装实用增强套件——纯外挂运行，绝不修改官方安装包与系统签名，不影响官方升级，随时可关。**

装好后，你的 Antigravity 会多出下面 **8 样实用功能**：

1. **🇨🇳 全中文界面 + 思考自动中译**：本地缓存翻译不耗额度，右上角 `⚙️` 秒切中英。
2. **🔔 macOS Dock 未读与状态提醒**：切走窗口时，Dock 图标实时显示未读角标与状态胶囊，切回自动消点。
3. **📱 手机 / 电脑远程控制（比官方快得多）**：同网毫秒级直连、扫码即用，跨网对话、发图、审批不转圈。
4. **⚡ 快捷提示词与一键优化**：内置与热门模板一键填入或直发，支持润色与下一步推荐。
5. **🧰 桌面顺手小工具**：`⌘1`～`⌘9` 秒切对话、文档原地编辑保存（`⌘S`）与一键开终端。
6. **📊 记忆容量看板与额度预警**：实时盯紧记忆余量与 **Gemini 4 / Claude** 额度，提前自动瘦身防卡顿。
7. **🛡️ 危险命令红框拦截**：`rm -rf`、`git reset --hard`、`sudo` 等高危操作强制人工放行。
8. **🔄 自动检测更新 & 一键升级**：有新版时 `⚙️` 亮红点，点一下立即生效。

<p align="center">
  <img src="assets/mac-preview.png" alt="Antigravity Suite macOS 桌面端真实全景效果" width="100%">
</p>
<p align="center"><sub>图注：左栏 <code>⌘1</code>～<code>⌘9</code> 对话秒切、右上角状态栏、底部进度条与快捷提示词、右下悬浮导航条</sub></p>

快速跳转：[一、核心功能](#一核心功能) · [二、怎么安装](#二怎么安装二选一) · [三、日常命令与卸载](#三日常命令与彻底卸载) · [四、常见问题](#四常见问题) · [五、安全与致谢](#五安全说明与致谢)

---

## 一、核心功能

### 1. 🇨🇳 全中文界面 & 中英文秒切

- 菜单、设置弹窗、报错和权限提示自动变中文；AI 的英文思考过程与左侧英文会话标题会自动翻译并缓存在本地，**不消耗模型额度**。
- 正在展开阅读某段思考时，新消息不会突然折叠；手动重命名过的标题会自动保留。
- 想切回英文：点右上角 **`⚙️`** → `🌐 语言与外观` → 语言选 **`English · 英文原版`**，立刻生效。

### 2. 🔔 macOS Dock 未读与状态提醒

> **切出去看网页、回消息时，不用反复切回软件猜 AI 跑完了没——瞄一眼桌面 Dock 图标就知道全部状态。**

<p align="center">
  <img src="assets/dock-preview.jpg" alt="macOS Dock 未读角标与状态胶囊真机效果" width="86%">
</p>
<p align="center"><sub>图注：右上角蓝/红未读数字 + 底部磨砂状态胶囊（平滑跟随 Dock 悬停放大）</sub></p>

- **四种状态一目了然**（默认开启「**带状态胶囊（推荐）**」）：

  | 当前会话状态 | 右上角角标 | 底部状态胶囊 | 说明 |
  | :--- | :--- | :--- | :--- |
  | AI 正在生成、无新未读 | — | 🔵 `生成中` | 让后台继续跑，不用守在窗口前 |
  | 有已完成的新回复待查看 | 🔵 蓝底未读总数 | 🔵 `新回复` | 与侧边栏未读同步，多窗口自动去重 |
  | 有普通确认卡等待点击 | 🔴 红底审批数 | 🔴 `待审批` | 提示需人工放行（混合时显示 `3新·2批`） |
  | 命中高危命令等待确认 | 🔴 红底告警数 | 🚨 `高危待批` | 最高优先级常驻，处理后才消 |

- **切回自动消点、审批不漏**：回到窗口后自动清除蓝色未读，红色待审批会保留到处理完毕；若喜欢极简风，可在 **`⚙️` → `🌐 语言与外观`** 切为 **「仅显示角标」**。
- **30 秒启用**：首次在 **`⚙️` → `🌐 语言与外观`** 点击 **「前往开启权限」** 放行 macOS「辅助功能」即可生效，点 **「测试提醒」** 可当场预览。

### 3. 📱 手机 / 电脑远程控制（比官方快得多）

- **本地直连、极速流畅**：手机点电脑右上角 **`📱远程`** 扫码，Safari **「分享」→「添加到主屏幕」** 即可全屏使用（支持右滑切会话、`+` 发图或传文件）；另一台电脑打开同链接自动适配宽屏。同 Wi-Fi 毫秒级直连，出门自动并行测速选最快通道（默认**免登录外网通道**，也支持 **Tailscale** 加密私网，可在 **`⚙️` → `📱 远程设置`** 开关，未勾选通道一律拒绝）。切会话不打断后台 AI，长历史按需加载 + 压缩传输，翻几百轮也不卡。
- **完整工作区**：按项目分组查看全部历史，可在你的个人目录（`$HOME`）和已登记项目内新建项目、浏览代码与修改对比；输入框上方配横向快捷提示词栏，默认 `Enter` 换行、`Cmd/Ctrl + Enter` 发送（带中文输入法防误触）。
- **排队消息与后台推送**：可查看并**立即发送 / 编辑 / 撤回**排队中的待发消息，实时审批确认卡（含高危二次放行）；添加到主屏幕后支持系统后台推送与图标未读角标。
- **多端独立与口令安全**：多个浏览器标签页互不串草稿，深浅外观同步桌面端；可在 **`⚙️` → `📱 远程设置`** 随时点击「重置配对口令」，旧链接立即失效。

<p align="center">
  <img src="assets/mobile-preview.jpg" alt="手机极速 PWA 遥控真机效果" width="88%">
</p>

### 4. ⚡ 快捷提示词与一键优化

- **14 个内置指令 + 10 条热门模板**：在 **`⚙️` → `⚡ 对话与效率`** 按场景分组选用或自由新增，点一下直接进输入框。
- **区分 `填入` 与 `⚡直发`**：**`填入`** 只把文字放进输入框（方便继续贴报错或截图，如 `修复这个报错`）；**`⚡直发`**（带 `↵`）一点即发（如 `直接实现`、`继续`、`用中文回答`）。已有草稿时自动只填入防误发，按 **`⌘/Ctrl + 点击`** 可临时切换。
- **一键优化 & 下一句推荐**：点输入框旁 **`✨ 优化`** 可让轻量快模型整理你的口语描述（带 **`↩ 撤回`**）；AI 回复完且输入框为空时，右侧会自动给出 2～4 句应景短句（按 **`Tab` / `→`** 填入、**`↑/↓`** 切换）。

<p align="center">
  <img src="assets/composer-preview.png" alt="输入框快捷提示词、场景补全与一键优化特写" width="96%">
</p>

### 5. 🧰 桌面顺手小工具

| 工具 | 快捷操作 / 入口 | 用途 |
| :--- | :--- | :--- |
| **对话秒切** | `⌘1`～`⌘9` / `⌘⇧[` / `⌘⇧]` / `⌃Tab` | 长按 `⌘` 显示序号角标瞬切左侧前 9 个对话，或前后切会话 |
| **悬浮消息导航** | 对话区右侧悬浮条 | 一键跳回顶部、底部或上一轮 / 下一轮消息 |
| **原地改文档** | 右侧预览栏 `编辑` + `⌘S` | 看 `.md` 方案或代码时就地编辑保存，点 **`完成`** 刷新预览 |
| **一键开终端** | 右上角 `>_ CLI`（`⚙️` → `🧰 终端与网络`） | 自动识别常用 macOS 终端，一键打开 `agy`（同页面可配置 CLI 与更新用的本地代理地址） |
| **统一设置中心** | 右上角 `⚙️` | 整合全部功能开关与 5 套主题配色（浅色/深色自动联动手机端） |

<p align="center">
  <img src="assets/shortcuts-preview.png" alt="⌘1～⌘9 对话秒切与悬浮消息导航特写" width="58%">
</p>

### 6. 📊 记忆容量看板、240K 自动瘦身与额度追踪

- **容量圆环与用时统计**：右上角实时显示当前对话占了多少记忆容量；点开可看今日 / 本月 / 本年 Token 统计、52 周热力图和 API 参考费用。
- **`G4` / `C` 额度胶囊**：实时追踪 Gemini 4 与 Claude/GPT 的 **5 小时窗口** 和 **每周总限额** 双进度条与重置倒计时，直观标出最紧余量；套餐、币种与实付金额可在 **`⚙️` → `📊 套餐与订阅`** 设置。
- **提前自动瘦身防卡死**：官方快装满（512K）才压缩，很容易因为前文缓存过期而卡顿 4～5 分钟。输入区底部能量条会实时盯紧缓存失效风险，并在达到 **240K** 且你空闲时自动发一次 `/compact` 减负（可在 **`⚙️` → `⚡ 对话与效率`** 开关）。

<p align="center">
  <img src="assets/quota-preview.png" alt="右上角上下文圆环、配额胶囊与底部能量条特写" width="84%">
</p>

### 7. 🛡️ 危险命令红框拦截

- 当 AI 准备执行 `rm -rf`、`git reset --hard`、`git clean -f`、`git push`、`sudo`、`kill -9`、`DROP/DELETE`、`op item` 等高危命令时，确认卡片会强制亮起醒目红框并拦停。
- 即使开启了「自动确认安全操作」，高危命令依然必须由你亲手点击放行。

### 8. 🔄 自动检测更新 & 一键升级

- 后台自动对比 GitHub 最新版，有更新时右上角 **`⚙️`** 亮起小红点，点开点击 **「立即更新」**（或终端运行 `ag-context-meter update`）即可原地更新生效，无需重启软件。
- **前提**：通过 **`git clone`** 安装且仓库无本地未提交改动。

---

## 二、怎么安装？（二选一）

运行环境：**macOS + Google Antigravity（兼容 `2.32.x ～ 2.34.0`）+ Node.js `22.4.0+`**（未装 Node 可运行 `brew install node@22`，常见 Node 版本管理器均兼容）。

### 方式 1：复制一句话发给你的 AI Agent（最省心）

把下面这段话直接发给 Antigravity / Claude Code / Codex，它会自动完成检查和安装：

```text
请帮我安装并配置 https://github.com/iamvicliu/antigravity-suite 这套 Antigravity 增强套件。
请克隆到 ~/.local/share/antigravity-suite，并严格按照仓库 README.md 中折叠的「AI Agent 自动安装执行规范」完成环境检查、安装与开启随客户端自启。
完成后运行 ~/.local/bin/ag-context-meter status 向我汇报各项状态，并简单告诉我日常怎么开关和卸载。
```

<details>
<summary>📋 展开查看：AI Agent 自动安装执行规范（人类用户无需阅读）</summary>

请按序执行以下 4 步，并用通俗中文汇报结果：

1. **只读预检**：检查 `node -v >= v22.4.0`；探测 Antigravity 调试端口（`~/Library/Application Support/Antigravity/DevToolsActivePort` 或 `lsof -nP -a -c Antigravity -iTCP -sTCP:LISTEN`），如未开启（`2.33.0+` 默认关闭）则提醒用户装完执行 `ag-context-meter restart` 或 `⌘Q` 重开。
2. **下载仓库**：
   ```bash
   git clone https://github.com/iamvicliu/antigravity-suite.git ~/.local/share/antigravity-suite
   cd ~/.local/share/antigravity-suite
   ```
3. **运行安装脚本**（`cli.js` 与 `bin/ag-context-meter` 已默认禁用改包命令；可选 `--no-auto` 不写入 `LaunchAgents`，`--no-remote` 关闭远程端口）：
   ```bash
   ./scripts/setup-macos-cdp.sh
   ```
4. **验收状态**：运行 `~/.local/bin/ag-context-meter status` 确认各项生效，并提示用户把 `~/.local/bin` 加入 `~/.zshrc` 的 `PATH`。

</details>

### 方式 2：终端手动 3 步安装

**第 1 步：下载并运行安装脚本**

```bash
git clone https://github.com/iamvicliu/antigravity-suite.git ~/.local/share/antigravity-suite
cd ~/.local/share/antigravity-suite
./scripts/setup-macos-cdp.sh
```

> 可选参数：`--no-auto` 仅当前窗口启用（可配合 `ag-context-meter install-launcher` 生成桌面启动器）；`--no-remote` 关闭远程端口。

**第 2 步：把命令加入终端 `PATH`**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**第 3 步：验证安装**

```bash
ag-context-meter status
```

看到 **「中文汉化：✅ 已生效」** 且右上角出现 **`📱远程`** 和 **`⚙️`** 就装好了。如果界面暂未变化（Antigravity `2.33.0+` 默认关闭调试端口），**请先按 `⌘Q` 彻底退出再重开一次 Antigravity**（或运行 `ag-context-meter restart`）。

---

## 三、日常命令与彻底卸载

> **记住区分这两条**：`stop` = **只关这一次**（下次打开自动恢复）；`auto-off` = **关闭自动加载**（以后打开也不再启动）。

| 命令 | 作用 |
| :--- | :--- |
| `ag-context-meter status` | 查看增强状态、自动加载与官方软件未改动校验 |
| `ag-context-meter remote` | 在终端查看手机扫码链接、通道状态与二维码 |
| `ag-context-meter update` | 拉取最新版并免重启刷新当前窗口 |
| `ag-context-meter stop` | **临时关闭这一次**：立刻还原英文原版界面 |
| `ag-context-meter auto-off` / `auto-on` | 关闭或恢复「打开 Antigravity 自动加载」 |
| `ag-context-meter restart` | 重启 Antigravity 并加载增强（`2.33.0+` 常用） |
| `ag-context-meter live` | 立即挂载到当前已打开的窗口 |
| `ag-context-meter install-launcher` | 在 `~/Applications` 生成独立的增强启动器图标 |

### 怎么彻底卸载？（4 步清干净）

```bash
ag-context-meter auto-off
rm -f ~/Library/LaunchAgents/com.$(id -un).ag-live-helper.plist
rm -rf ~/Applications/"Antigravity 增强启动器.app" ~/.local/bin/ag-context-meter ~/.local/share/antigravity-suite ~/.local/share/antigravity-context-viewer
```

*可选*（连同本地缓存与个人设置一起清空）：

```bash
rm -rf ~/Library/Application\ Support/AntigravityContextMeter ~/.config/antigravity-context-meter
```

---

## 四、常见问题

| 遇到的情况 | 先做什么 |
| :--- | :--- |
| **装完右上角没出现 `📱远程` 和 `⚙️`** | 按 `⌘Q` 彻底退出再重开软件（或跑一次 `ag-context-meter restart`）；仍未出现请跑 `ag-context-meter status` 查看原因。 |
| **Dock 图标没有出现未读或审批提醒** | 1. 打开 **`⚙️` → `🌐 语言与外观`**，点击 **「前往开启权限」** 在系统设置「辅助功能」勾选 Antigravity（终端启动需一并勾选终端）；<br>2. 如提示缺编译工具，在终端运行 `xcode-select --install` 后重试；<br>3. 点 **「测试提醒」** 可当场预览 5 秒。 |
| **终端提示 `ag-context-meter: command not found`** | 运行 `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc`。 |
| **手机扫码打不开页面** | 打开 **`⚙️` → `📱 远程设置`** 确认对应通道已勾选；确认在同 Wi-Fi，或外网已开启外网隧道；必要时检查系统防火墙放行 `18765` 端口。 |

---

## 五、安全说明与致谢

### 安全原则

1. **绝不改写官方软件**：仅在运行时外挂加载界面增强，不修改 `Antigravity.app` 安装包文件与苹果签名。
2. **通道门禁与 48 位随机口令**：所有远程请求都校验 48 位随机配对口令，可在 **`⚙️` → `📱 远程设置`** 一键重设（旧链接立刻作废），不需要远程功能时可随时关掉外网通道或禁用远程服务。
3. **数据与目录严格限权**：翻译缓存和设置仅存在本机；远程文件浏览和在线编辑严格锁定在个人主目录（`$HOME`）与已登记项目目录内，绝不触碰系统目录与各类密码/密钥文件夹（重要项目仍建议配合 Git 使用）。

<details>
<summary>🔧 展开查看：进阶配置与开发者说明（自建固定域名、Windows/Linux、上游对比）</summary>

- **自建固定域名隧道与 `/#/NoAuth` 排错**：有自有域名时，请在 Cloudflare Zero Trust Tunnels 的 **Public Hostname** 绑定子域名指向 `http://127.0.0.1:18765`（若扫码停在 `*.cloudflareaccess.com` 或 `/#/NoAuth`，说明填成了 Access 登录地址，切回「免登录临时隧道」即可）。输入 Token 框旁提供直达入口，Token 仅加密/限权存放在本地，接口永不回显。
- **Windows / Linux 手动用法**：自动挂载与 Dock 提醒为 macOS 专属；Windows / Linux 用户安装 Node.js `22.4.0+` 并以 `--remote-debugging-port=9222` 启动 Antigravity 后，在仓库目录运行 `node cli.js live` 也可加载核心功能。
- **检查上游参考仓库**：运行 `ag-context-meter upstreams` 与 [`scripts/upstreams.json`](scripts/upstreams.json) 比对；仓库亦附带 [`docs/fast-io-AGENTS.md`](docs/fast-io-AGENTS.md) 提速规则可按需合并。

</details>

### 核心协作者与上游致谢

- **核心协作者**：感谢 **[@hubo1989](https://github.com/hubo1989)**（深度打磨扫码配对、远程通道控制、设置整合与 `v2.32+` 兼容）和 **[@Shens](https://github.com/Shens)**（深度打磨远程交互性能、多项目全历史滚动、排队消息审批、Mac 自启守护与非 Homebrew Node 兼容）。

| 参考项目 | 作者 / 贡献者 | 参考与吸收内容 |
| :--- | :--- | :--- |
| **[elviscjn-cjn/antigravity-context-viewer](https://github.com/elviscjn-cjn/antigravity-context-viewer)** | [@elviscjn-cjn](https://github.com/elviscjn-cjn)、[@Jia131313](https://github.com/Jia131313)、[@Azreal2021](https://github.com/Azreal2021)、[@MoiraToki](https://github.com/MoiraToki)、[@nocoo](https://github.com/nocoo) | 基础框架、顶部上下文圆环看板、Token 与热力图统计、费用估算与双周期配额 |
| **[akelabs/antigravity-pulse](https://github.com/akelabs/antigravity-pulse)** | [@akelabs](https://github.com/akelabs) | 输入框底部能量条：输出速率、缓存命中与窗口倒计时 |
| **[n2ns/antigravity-panel](https://github.com/n2ns/antigravity-panel)** | [@n2ns](https://github.com/n2ns) | 模型额度监控、安全自动确认与缓存体积监控思路 |
| **[yiheng8023/antigravity-chinese](https://github.com/yiheng8023/antigravity-chinese)** | [@yiheng8023](https://github.com/yiheng8023) | 适配 `2.32+ ～ 2.34.0` 的中文词条与动态翻译规则 |
| **[wycocoyu/agy-context-dashboard](https://github.com/wycocoyu/agy-context-dashboard)** | [@wycocoyu](https://github.com/wycocoyu) | 轻量状态栏排布与 `local-api` 存活进程凭证校验思路 |
| **[oil-oil/agy-fast-io](https://github.com/oil-oil/agy-fast-io)** | [@oil-oil](https://github.com/oil-oil) | 桌面端 Fast IO 提速规则规范 |

---

基于 [MIT License](LICENSE) 开源，所有参考或引入的第三方组件均完整保留其原始版权与开源协议。
