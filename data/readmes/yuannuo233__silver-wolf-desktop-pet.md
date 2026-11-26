# Silver Wolf Desktop Pet 银狼桌宠

> “Hack into your desktop.” —— 银狼钻进你的电脑里啦

A Silver Wolf inspired desktop companion for Windows: **a clean main app**
(sidebar + home/chat/settings) **plus a floating desktop pet**.
AI chat with any OpenAI-compatible API; standalone exe, or run from source
with just `Pillow` (`pip install -r requirements.txt`).

致敬《崩坏：星穹铁道》「银狼」的桌面伴侣（非官方粉丝作品，免费、非商业）：
**正经主程序窗口** + 桌面浮窗桌宠，双箭齐发。

## ✨ Features 功能

- 🖥️ **完整主界面**：侧边栏导航（主页 / 聊天 / 设置），自绘一体化标题栏（无系统白边），浅 / 深 / 赛博蓝三主题
- 🐺 **桌面浮窗宠物**：永远置顶、单击说话、双击快问快答、右键菜单（动作 / 尺寸 / 主题开关）
- 🏃 **拖拽 = 瞄准，松手 = 她自己跑过去**：按住拖动时窗口不动、她原地转身面朝方向，松手后以固定速度跑向落点，跑到停回待机
- 🎬 **11 组帧动画**：待机（含眨眼）/ 左右跑 / 转身过渡 / 挥手 / 打盹 / 伸懒腰 / 吃棒棒糖 / 敲键盘 / 玩掌机
- ⌨️ **跟着你做事**：你在编辑器里打字她跟着敲键盘，前台是游戏她掏掌机自己玩（右键可关）
- 💬 **AI 聊天**：任意 OpenAI 兼容接口——DeepSeek / 智谱 / 通义 / Kimi / 豆包方舟 / OpenAI / 本地 Ollama，预设一键填
- 🎭 **高度还原人设**：三档系统提示词（完整版 / 平衡版 / 省token版）自由编辑实时生效
- 📏 **尺寸五档**：迷你 100px → 特大 400px，记住偏好
- 📦 独立 exe（无需 Python）；源码仅依赖 Pillow

## 💻 系统与环境要求（实测数据，非推测）

### 用现成 exe（大多数人）

| 项 | 要求 |
| --- | --- |
| 系统 | **Windows 10 / 11（64 位）** |
| Python | **不需要**（已打包进 exe） |
| 磁盘 | 约 40MB（单文件 exe） |

### 从源码运行（开发者）

| 项 | 要求 | 实测结论 |
| --- | --- | --- |
| Python | **3.10 及以上** | 3.10.11 / 3.12 / 3.13.17 / 3.14 全部编译+导入通过；3.10.11 与 3.13.17 **实测能正常起窗口** |
| tkinter | 随 Python 自带（Tk 8.6） | 3.10.11 = Tk 8.6，3.13.17 = Tk 8.6.15，都正常 |
| Pillow | **≥ 10.0**（必需，不是可选） | 3.10 装 12.3.0、3.13 装 13.0.0 均正常 |
| 架构 | **64 位**（AMD64） | 大量 Win32 结构体按 64 位指针声明，32 位下会出错 |
| 其他依赖 | **无** | AI 聊天走标准库 `urllib`，不需要 `requests` |

> ⚠️ **Pillow 不是可选项**：缺了它程序仍能启动，但帧动画会退化成单帧浮动
> （`HAS_PIL` 降级分支）。这种"能开但不对"的情况比直接报错更难排查。

### 版本下限是怎么定的

- 代码里**没有任何 3.10 专属语法**（无 `match` 语句、无 `X | Y` 类型注解），
  理论上 3.8 也能跑；
- 但 **3.10 是本项目实测过的最低版本**（那只放行"实测能起窗口"的版本，
  没测过的不写进要求）。**低于 3.10 未经验证，请自行评估。**

### 平台限制

**只能跑 Windows。** 透明桌宠窗口、任务栏按钮、键盘钩子、控制台隐藏全部依赖
Win32 API，换成 macOS / Linux 会在 import 阶段就失败。
详细原因与可移植部分见 **[LIMITATIONS.md](LIMITATIONS.md)**。

## 🚀 立即使用（无需编程 / No coding needed）

1. 前往 [Releases 页面](../../releases)（已发布 v0.6.30）
2. 下载 `SilverWolfPet-v0.6.30-win64.zip`（或 Releases 里最新版本）
3. 解压到任意文件夹（路径带中文也行），**双击 `SilverWolfPet.exe`**
4. 主界面弹出（主页 / 聊天 / 设置），同时银狼出现在屏幕右下角！
5. **想在桌面放图标**：双击包内的 `创建桌面快捷方式.bat`，
   就会在桌面生成同款「银狼桌宠」图标（带银狼图标，不是白板）

> zip 里**不带**现成的 `.lnk` 快捷方式，因为快捷方式记录的是**绝对路径**——
> 别人解压到别的目录后，那个 lnk 会指向不存在的旧地址。
> 所以改成"在你解压的位置现场生成"的脚本，搬目录也不会失效。

- ✅ 无需安装 Python，解压即用
- ✅ 系统：Windows 10 / 11（64 位）
- ✅ 包内 创建桌面快捷方式.bat 一键在桌面生成同款图标
- ✅ 从源码跑也不会弹出黑控制台（只隐藏属于她自己的那个控制台）

> **首次运行弹蓝色警告「Windows 已保护你的电脑」？**
> 这是对未付费签名程序的统一提示。点 **更多信息 → 仍要运行** 即可。
> 杀毒软件误报同理，添加信任即可。程序完全开源，可自行审阅源码。
> 首次启动若"没反应"，多为安全软件在扫描新 exe（本机实测 30~45s），等一会儿或加信任后再开。

## 🤖 给 AI 助手 / Agent 的安装说明

如果你是被派来安装本项目的 AI 助手，直接照做即可：

```text
目标：安装银狼桌宠（SilverWolfPet）
步骤：
1. 下载最新 Release 的 zip：
   https://github.com/yuannuo233/silver-wolf-desktop-pet/releases/latest
   （资产名形如 SilverWolfPet-v0.6.30-win64.zip）
2. 解压 zip 到任意目录（如 C:\Tools\SilverWolfPet）
3. 运行 SilverWolfPet.exe；如遇 SmartScreen 蓝色警告，
   点击"更多信息"→"仍要运行"
4. 验证：弹出"银狼桌宠"主窗口 + 屏幕右下角出现 Q 版银狼即成功
5. 关闭主窗口 = 退出程序；桌宠右键菜单也有"退出程序"
6. 可选：在主窗口「设置」页填 AI 供应商 API Key 启用聊天
备选（机器已有 Python 3.10+ 时）：git clone 本仓库 → `pip install -r requirements.txt` → `python main.py`
```

## 💬 AI 聊天配置（可选，两分钟搞定）

不配置 AI 也完全可用（她说离线台词）。想跟她真聊，只需要一个 API 密钥：

1. 主界面 → **设置** 页（或桌宠右键 → 设置…）
2. 选**厂商预设**（推荐智谱 GLM 的 `glm-4-flash`：有免费额度）
3. 到该厂商官网注册并创建 API Key，粘贴进密钥框
4. 点 **保存** → 「聊天」页或双击桌宠开聊！

| 预设 | 接口地址 | 默认模型 | 备注 |
| --- | --- | --- | --- |
| DeepSeek | `https://api.deepseek.com/v1` | deepseek-chat | 便宜量大 |
| 智谱 GLM | `https://open.bigmodel.cn/api/paas/v4` | glm-4-flash | **有免费额度** |
| 通义千问 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | qwen-turbo | 阿里云 |
| Kimi | `https://api.moonshot.cn/v1` | moonshot-v1-8k | 长文本 |
| 豆包·火山方舟 | `https://ark.cn-beijing.volces.com/api/v3` | 填接入点 ID | 控制台创建接入点 |
| OpenAI | `https://api.openai.com/v1` | gpt-4o-mini | 国际 |
| Ollama 本地 | `http://127.0.0.1:11434/v1` | 本机模型名 | 完全免费、离线 |

- **人设提示词**：三档一键填入（完整版 / 平衡版 / 省token版），自由编辑；AI 每次回复都按这份"角色说明书"来演。
- **隐私**：API 密钥只保存在 `%APPDATA%\SilverWolfPet\config.json`，不经过任何第三方服务器。
- **记忆**：带最近 6 句对话上下文，不无限膨胀（省 token）。

## 🛠️ 从源码运行（开发者）

```bash
git clone https://github.com/yuannuo233/silver-wolf-desktop-pet.git
cd silver-wolf-desktop-pet
pip install -r requirements.txt   # 只有 Pillow 一个依赖
python main.py
```

- Windows 下也可以直接双击 `启动银狼桌宠.bat`（自动优先用 pythonw 无控制台启动）
- **VSCode 用户**：直接"打开文件夹"选本仓库 → 装推荐扩展（Python + 中文语言包）→
  按 **F5** 即运行（`.vscode/launch.json` 已配好）；注释全中文，`files.encoding=utf8` 已锁，不会乱码
- 帧动画 / 平滑缩放 / 图标处理都依赖 Pillow；缺失时程序仍能启动但退化为单帧浮动模式

### 打包成 exe（维护者参考）

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --name SilverWolfPet --icon icon.ico ^
  --add-data "assets;assets" --add-data "icon.png;." main.py
```

（不要用 `--splash`：PyInstaller 闪屏在部分机器上会残留/挡住主窗口。）


## 📁 仓库里都有什么

```text
main.py / app.py / pet.py / ui.py / settings.py   程序本体
config.py / ai_client.py / lines.py / prompts.py
interop.py            跨宠物系统互通桥（协议见 PROTOCOL.md）
assets/               立绘 3 张 + banner
assets/stand/         11 组帧动画共 186 张 PNG + frames.json
scripts/              抠图工具 + .petpack 导出
icon.png / icon.ico   应用图标
启动银狼桌宠.bat        双击即用（优先 pythonw，无控制台）
```

## 📌 先看这两个文档

- **[LIMITATIONS.md](LIMITATIONS.md) —— 局限说明**：只能跑 Windows、为什么、哪些能移植；
  帧动画不是骨骼动画所以做不到什么；AI 聊天支持范围；打包与分发的坑。
  **下载前建议先读，免得把已知限制当 bug。**
- **[PROTOCOL.md](PROTOCOL.md) —— 桌宠互操作协议（草案）**：三级能力模型（素材包 / 行为包 /
  事件包），可以把银狼接入 LongCat 那类多宠物框架，也能让别的桌宠复用她的素材。
  协议已实现 L1 导出脚本与 L3 事件通道：

  ```bash
  python scripts/export_petpack.py --zip    # 导出 silver-wolf.petpack（任何引擎可读）
  ```

  L3 事件通道走文件，零依赖：外部往
  `%APPDATA%\SilverWolfPet\interop\inbox.jsonl` 追加一行 JSON 即可控制她，
  她的状态与聊天会写到同目录 `outbox.jsonl`。

## Replace the sprite 换成你自己的立绘

1. 准备一张 **透明背景 PNG**（推荐 chibi，高度 150–300px；大尺寸的存成 `silver_wolf_hd.png` 供缩放）
2. 覆盖 `assets/` 里的同名文件
3. 重新运行

背景不是透明的？用仓库自带的工具抠一下（需要 Pillow）：

```bash
python scripts/remove_background.py 你的图.png 输出.png 32
```

## Roadmap 路线图

- [x] v0.1 单帧立绘 + 浮动 + 台词气泡 + 拖拽 + 右键菜单
- [x] v0.2 AI 对话（OpenAI 兼容全通吃）+ 尺寸五档 + 三档可编辑人设提示词
- [x] v0.3 主程序界面（主页/聊天/设置）+ 双击聊天 + 桌宠与主界面联动
- [x] v0.4 多状态动画状态机（frames.json 规格）
- [x] v0.6 H3 素材帧动画全面接管：待机眨眼 / 跑动 / 转身过渡 / 右键动作 / 敲键盘 / 玩掌机
- [x] v0.6.13+ 自绘一体化标题栏 + 三主题 + 跟着你做事
- [x] v0.6.17 任务栏图标/按钮 + 黑控制台自隐藏 + 窗口轮廓 + 拖拽追光标（自己的速度）+ 转身动画
- [x] v0.6.17 互通协议 L1 素材包导出 + L3 事件通道；局限说明
- [x] v0.6.24 插件系统 + 插件市场（独立子进程、JSON 行协议、任何语言可写）
- [x] v0.6.26 多角色（银狼 / 银狼冷淡版）+ 页面滚动 + 窗口边缘拉伸
- [x] v0.6.27 公告栏、意见反馈邮箱
- [ ] 银狼 Lv999 素材（框架已就位，等帧图）
- [ ] L2 行为包（规则从代码里抽到 pack.json）
- [ ] macOS / Linux（靠 L3 把前台感知交给宿主）

## Disclaimer 免责声明

**三份文件共同构成完整条款，请都读一遍：**
[DISCLAIMER.md](DISCLAIMER.md)（非官方粉丝作品声明）·
**[TERMS.md](TERMS.md)（使用条款与责任边界）** · [LICENSE](LICENSE)（MIT + 附加条款）

要点：

- **非官方粉丝作品（Unofficial fan work）**，与 miHoYo / HoYoverse / COGNOSPHERE 无关，也未经其授权或认可。
- 未使用任何游戏拆包素材（立绘、语音、UI 图标），台词与提示词为原创，Q 版形象为粉丝向原创/AI 辅助二创。
- 代码 MIT 开源，但**不包含**任何对米哈游角色形象 / 名称 / 商标的授权；禁止商业用途。
- AI 回复由第三方大模型生成，不代表官方设定；API 密钥只存本机，请自行保管。
- 本项目完全免费、非商业用途；如权利方提出合理要求将配合修改或下架相关素材。

### ⚠️ 关于"别人拿去乱用"这件事

**本项目仅限桌面装饰与娱乐用途。** 说得直白些：

- **谁使用、谁负责。** 任何人用这份代码（无论原版还是改过的）去做的事，
  责任在那个做事的人身上，**不在原作者**。
- 原作者**没有能力也没有义务**监控代码被复制到了哪里、被改成了什么样 ——
  MIT 许可证允许任何人自由使用和修改，正因为如此，原作者不可能对下游行为负责。
- **TERMS.md 第 3 条**明确列出了禁止用途（违法、未授权入侵、恶意软件、窃取凭证、
  诈骗、侵权、商业用途等）。违反者是其**个人独立行为**，与原作者无关。
- **TERMS.md 第 4 条**是责任限制与赔偿条款：任何因使用者行为引发的索赔或诉讼，
  由使用者独自承担，并须使原作者免受损害。
- **再分发者注意**：请保留 `LICENSE`、`TERMS.md`、`DISCLAIMER.md` 三个文件。
  删掉它们再分发，等于把责任揽到自己身上。

> 这不是"甩锅式免责"，而是开源项目的标准做法（Linux、Kubernetes、任何 MIT 项目同理）：
> 作者提供的是**工具**，不是**行为的授权**。

## License

[MIT](LICENSE) + 附加条款（见 `LICENSE` 正文 ADDITIONAL TERMS）


## 意见反馈 / 联系作者

有建议、想法、bug，或者想一起做插件，欢迎写信给作者：

**邮箱：dafeiyutanchi@qq.com**

（这是非官方粉丝作品，作者是初中生，收到邮件不一定秒回，但都会看。）
