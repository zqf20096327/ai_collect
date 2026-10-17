# Claude Pet 🐾

**[English README](README.en.md)**

<p align="center"><img src="docs/pet-walk.gif" width="190" alt="宠物在桌面上遛弯"/></p>

> A macOS desktop pet that lives above all your windows — feed it, walk it, turn your own
> pet's photos/videos into its skin via fully-offline AI matting (Apple Vision framework),
> and watch it react to your Claude Code and Codex sessions. PySide6 + QML + three.js in QtWebEngine.
>
> **Not affiliated with or endorsed by Anthropic.** "Claude" is a trademark of Anthropic PBC;
> this is a community project that merely talks to your locally installed Claude Code CLI.
> 本项目为社区作品,与 Anthropic 无关联;宠物本体功能不依赖 Claude、完全离线。

## ✨ 能干什么

| 🐶 你家宠物本尊上桌面 | 🍗 养成互动 | 🤖 Claude Code + Codex 联动 |
|---|---|---|
| 拍照/拍段视频 → **本地 AI 抠图**(系统 Vision 框架,离线、免费、不排队)→ 变成会呼吸、走路、吃饭、睡觉的桌宠 | 投喂 / 摸摸 / 玩球 / 睡觉 / 🚶遛弯,攒经验升级;饿了会喊你 | 统一管理 Claude/Codex 会话与模型;在跑时头顶转 ⚙️,干完活撒花,**等你回复时蹦跶 + 系统通知**;识别 App / VS Code / 终端并直达原会话 |

<p align="center">
  <img src="docs/menu.png" width="330" alt="喂养菜单"/><br/>
  <sub>右键宠物 → 喂养菜单:投喂 / 互动 / 换形象;「我的模型」区 <b>➕ 上传 3D 模型(.glb/.gltf)</b> 或 <b>🎬 创建动画宠物</b>,左右滑动挑选、长按拖动排序</sub>
</p>

<table align="center">
  <tr>
    <td align="center"><img src="docs/panel.png" width="330" alt="Claude 会话面板"/></td>
    <td align="center"><img src="docs/slots.png" width="330" alt="动画宠物活动槽编辑器"/></td>
  </tr>
  <tr>
    <td align="center" width="360"><sub><b>点宠物 → AI 会话</b>:Claude/Codex 按来源筛选,模型、状态和打开渠道一眼可见;点击卡片直达 App / VS Code / 终端中的原会话</sub></td>
    <td align="center" width="360"><sub><b>🎬 动画宠物 · 活动槽编辑器</b>:六个动作逐槽上传照片/视频,本地 AI 抠图自动透明,✅ 实时标记进度</sub></td>
  </tr>
</table>

<p align="center">
  <img src="docs/matting-demo.png" width="540" alt="AI 抠图:照片进,透明宠物出"/>
</p>
<p align="center">
  <img src="docs/hero.png" width="230" alt="睡觉槽示例"/><br/>
  <sub>「睡觉」槽 = 你家狗睡觉的照片,连地板反光都保留 —— 六个活动槽(待机/走路/吃饭/睡觉/玩耍/开心)逐槽上传,宠物按状态自动切换</sub>
</p>

## 📦 下载安装

1. 到 **[Releases](../../releases)** 下载最新 `ClaudePet-*.dmg`(约 130MB,QtWebEngine 占主要体积)
2. 把 `Claude Pet.app` 拖进「应用程序」
3. **首次打开提示「已损坏,无法打开」?** 这是 macOS 对未公证应用的拦截(个人项目没买 $99/年的开发者账号),App 本身没坏:
   - **双击 DMG 里附带的 `修复「已损坏」提示.command`** 即可(如果它也被拦,右键它 → 打开)
   - 或终端执行:`xattr -cr "/Applications/Claude Pet.app"`
   - 注意:Apple 芯片 (M1/M2/M3) 上**右键 App → 打开 是绕不过去的**,必须用上面两种方式之一
4. 打开后宠物出现在屏幕右下角,菜单栏会有 🐱 图标。**看不到菜单栏图标?** 刘海屏 MacBook 菜单栏满了会把新图标挤掉——不影响使用,所有操作(大小/形象/退出)右键宠物都有;想找回图标就清理几个菜单栏项或用 [Ice](https://github.com/jordanbaird/Ice)/Bartender
5. 以后有新版会**自动提示更新**(每天静默检查一次 GitHub Releases,一键下载换包重启);也可托盘「⬆️ 检查更新」手动查

系统要求:macOS 14+(AI 抠图依赖系统 Vision"提取主体"能力;13 可运行但照片/视频抠图不可用)。当前发布包为 **Apple 芯片 (arm64)** 构建,Intel Mac 需自行从源码打包。会话联动按需识别本机的 [Claude Code](https://claude.com/claude-code) 和/或 Codex CLI(都可选,不装不影响桌宠本体)。

### 从旧版升级到 v1.5.2

1. 在托盘选择 **检查更新**，或下载 [v1.5.2 安装包](https://github.com/Sabrina-creater/claude-pet/releases/tag/v1.5.2)，退出旧桌宠后将新 App 拖入“应用程序”覆盖。无需删除本机设置、已导入素材或唤醒队列。
2. 打开桌宠 → **唤醒** → **安装 / 修复**，为已安装的 Claude Code 接入对应桥接。本版支持 **2.1.270**，同时保留 **2.1.263**；其他版本需桌宠提供对应适配。
3. 等原 VS Code 窗口中的请求结束并保存草稿后，执行 **Developer: Reload Window（开发人员：重新加载窗口）**。保留原 Claude 标签页，在桌宠中点 **检查原页**，再按需开启自动唤醒。

如果之前为临时回退关闭了 Claude Code 的 **Auto Update**，可重新开启；无需长期固定或降级插件。新版兼容性由桌宠适配。[更新内容与验证范围](https://github.com/Sabrina-creater/claude-pet/releases/tag/v1.5.2)

## 🚀 三步上手

1. **右键宠物** → 喂养菜单(单击 = 会话面板,双击 = 摸摸,拖动 = 挪位置)
2. 「我的模型」→ **🎬 动画宠物** → 按提示给各活动槽上传你家宠物的照片/视频(jpg/heic/mp4/mov/gif 都行,自动抠图秒级生效;方向不对点 ↻)
3. 开着 **🚶 遛弯**,它会自己在屏幕上散步;写代码时它同时盯着你的 Claude Code / Codex 会话

---

住在你桌面上的 **3D 宠物**:18 种形象可换、可喂养、会对 Claude Code / Codex 会话有反应。

## 它会干什么

- **3D 本体**:Three.js 渲染的卡通宠物,转头看你的鼠标、呼吸、眨眼、随机东张西望;翅膀/触手等部件有各自的小动作
- **看会话**:Claude 活会话 + Codex 最近 48 小时未归档会话统一显示,可按来源筛选并查看实际模型和 App / VS Code / 终端渠道;点击卡片会先定位所属 VS Code 工作空间再回到原会话,「记录」按钮留在宠物内看只读历史;AI 在干活时它头顶转 ⚙️ 陪你"上班",干完活会跳起来转圈撒彩带(还涨经验),有会话等你时它会蹦跶提醒(角标变红)
- **能喂养**:饱食🍗 / 心情💗 / 精力⚡ 三条状态随时间衰减(关掉 App 也在掉,封顶 24h),喂食、抚摸、玩毛线球、睡觉都会影响数值;攒经验升级
- **会说话**:吃饱了、饿了、被摸了、干完活了……头顶冒中文气泡

## 操作

| 动作 | 效果 |
|---|---|
| 单击宠物 | 会话面板(状态/Todo 进度/渠道识别/原会话跳转) |
| **右键宠物** | **喂养菜单**:状态条、投喂(小鱼干/苹果/蛋糕/咖啡)、摸摸/玩球/睡觉/**🚶遛弯**、形象切换、**➕ 上传 .glb 模型**、**🎬 创建动画宠物** |
| 双击宠物 | 摸摸(冒爱心,心情+) |
| 拖动 | 移动位置(自动记住) |
| Esc | 关面板/菜单 |

21 形象:🐱小猫 👻幽灵 🦫卡皮巴拉 🦉猫头鹰 🦆小鸭 🪿大鹅 🫧泡泡 🐉小龙 🐙章鱼 🐧企鹅 🐢乌龟 🐌蜗牛 🦎六角恐龙 🌵仙人掌 🤖机器人 🐰兔兔 🍄蘑菇 😺胖墩,以及三只**真模型**:
- 🐈 高级猫(Sketchfab,带骨骼,坐姿/理毛/哈欠/甩尾;睡觉定格在闭眼蜷缩帧)
- 🦊 高级狐狸(Khronos 官方样例 Fox,CC0 by PixelMannen / rig CC-BY tomkranis,Survey 待机)
- 🦜 高级鹦鹉(three.js 官方样例 Parrot,CC-BY mirada/rome,形变飞行动画,悬浮)

**上传自己的模型**:右键菜单"➕ 上传模型"选一个 `.glb`/`.gltf`,自动归一化(居中/缩放/贴地)成新形象。带骨骼动画的会播动画;没动画的(如 Tripo 图生 3D)走全程序化(呼吸/看鼠标/吃饭/蹦跳),保持模型自身姿态。模型存 `~/Library/Application Support/claude-pet/models/`,悬停模型格按 ✕ 删除。建议先把模型简化到 <5MB(`npx @gltf-transform/cli optimize`),太大(几十万面)会卡。

**🎬 动画宠物(不会建模也能养)**:右键菜单点"🎬 动画宠物"创建,自动初始化 6 个**活动槽**(待机/走路/吃饭/睡觉/玩耍/开心),槽位编辑器逐槽引导上传。**素材自动路由**:
- **真实照片(jpg/heic)/ 视频(mp4/mov)→ 本地 AI 抠图**(matting.py):Vision 框架(系统"提取主体"同源,Apple 芯片硬件加速)逐帧抠出主体 → 透明动画 WebP,视频 1-5 秒出结果,全程离线不排队——顺带绕开 WebEngine 没有 H.264 解码器的限制
- GIF/WebM → 纯色背景自动色键成透明(边框取样 + 自适应容差,GIF 抖动调色板也能识别);自带透明的素材原样用

至少上传「待机」;缺的动作自动回退到待机。宠物按状态切槽播放,上传/重传立刻热生效(文件名带时间戳)。拍你家宠物不同动作的短视频逐槽上传,桌宠就是它本狗/本猫;单张照片也行(呼吸/蹦跳/转向由渲染层实时加)。素材存 `models/<key>/` 子目录,索引损坏可从子目录自愈重建。

**🚶 桌面遛弯**:宠物会自己在屏幕上走动(默认开,互动区可关):歇几秒挑个目标点走过去,走路时播「走路」槽动画并自动转向。拖动宠物、开面板/菜单、睡觉时自动暂停。

养成数值:喂食 +饱食/+心情/+5xp(>95 拒食),抚摸 +心情/+2xp,玩球 +心情/-精力/+8xp(精力<15 玩不动),睡觉回精力(太困会自己睡,睡饱自己醒);Claude 每干完一轮活 +15xp。每 100xp 升一级。

## 额度恢复后自动唤醒（v1.5.2 实验功能）

默认关闭。点宠物打开会话面板 → **唤醒** → 开启自动唤醒，单个会话可独立暂停。Claude VS Code 点击 **安装 / 修复** 接入后台通道，然后在原 VS Code 窗口执行 **开发人员: 重新加载窗口**，保留原 Claude 标签页。看到后台连接状态后，可用 **检查原页** 验证具体会话。

检测到会话最新一轮明确的额度错误后，宠物保存原渠道和会话 ID，等待恢复时间再提交继续消息。Claude VS Code 使用原页面的发送函数和原 Claude 通道，核对页面及进程回执，无需前台焦点或辅助功能权限，支持锁屏期间发送。不会购买额度重置，不会新开 CLI 执行器。Codex 显示账户额度；Claude 根据真实错误记录显示恢复时间，未知时间最多尝试三次。

原页有草稿、附件、权限弹窗、运行中的任务或页面身份不明确时等待；用户已经手动继续则撤销旧动作。发送后以原会话日志中的消息标记确认，结果不明时需要核对，不能直接反复点重试。**检查原页**只检查，不发送消息。

保持宠物、原客户端和原标签页运行，并让电脑保持唤醒；锁屏与睡眠不同，睡眠时不能处理请求。本机桥接会修改已安装 Claude 插件的两个文件并保存原文件。桌宠 v1.5.2 按插件版本选择适配配置，支持文件校验通过的 **2.1.270**，并保留 **2.1.263** 的兼容。

Claude Code 可正常升级，再更新桌宠、点击 **安装 / 修复** 并重新加载原 VS Code 窗口；无需固定或回退到旧版插件。若插件版本尚未适配，需等待桌宠补充适配；安装器不会猜测私有接口或覆盖未知文件，也不保证任意未来版本自动兼容。Claude App、Codex App 和 Codex VS Code 仍使用辅助功能，需要授权 **Claude Pet** 并保持桌面解锁；终端尚未接入。

2026-09-09，桌宠 v1.5.1 与 Claude 插件 2.1.263 已通过真实锁屏验收：锁屏期间在同一页面、同一通道提交，并在约 5 秒后收到回复，session ID 保持一致。该记录是既有版本的验证结果，详见[实现与验证说明](docs/ai-quota-wakeup-design.md)。

队列与记录在 `~/Library/Application Support/claude-pet/wake-queue.json`、`wake.log`，后台连接和回执在同目录的 `bridge/`；不要将这些私人会话记录提交到 GitHub。

## 运行

```bash
./run.sh                        # 首次自动建 .venv 并装 PySide6-Essentials + Addons(WebEngine)
.venv/bin/python pet.py --dump  # 不开窗口,纯打印会话扫描结果
.venv/bin/python pet.py --demo  # 自动演示一轮喂食/摸摸/玩球/睡觉,21s 后退出
.venv/bin/python pet.py --probe # 每 2s 打印窗口几何/可见性,15s 后退出(诊断用)
.venv/bin/python pet.py --animdemo idle.gif walk.gif eat.gif
                                # 动画宠物全链路冒烟:创建→逐槽导入→喂食→遛弯,40s 自动清理退出
```

没装上 PySide6-Addons(WebEngine)时自动退回旧版 2D 小猫,功能不缺。

## 打包成独立 App(分发给别人)

打成 macOS `.app` + `.dmg`,对方无需装 Python,双击即用:

```bash
./packaging/build-mac.sh        # 一键:PyInstaller 出 .app,再打 dist/ClaudePet.dmg
```

要点:
- 成品约 **515MB**(QtWebEngine 固有体量),`.app` 内含 qml/web/cat.glb 与完整 Qt 运行时
- **只能在 macOS 上构建 macOS 包,在 Windows 上构建 Windows 包**(PyInstaller 不能跨系统);本仓库当前只配了 Mac
- 产物是 **arm64**(Apple 芯片)。Intel Mac 需在 Intel 机器上重跑构建
- **未签名** → 对方首次打开会被 Gatekeeper 拦(Apple 芯片上直接提示「已损坏」,右键打开也无效)。DMG 里已附带 `修复「已损坏」提示.command` 双击即修;或终端 `xattr -cr "/Applications/Claude Pet.app"`
- 打包后仍是后台型(无 Dock 图标);退出用面板里的"退出宠物"或 `pkill -f "Claude Pet"`
- 宠物本体(养成/3D)不依赖任何 AI CLI;只有终端来源的恢复需要对应 CLI,App / VS Code 来源走客户端深链

资源定位:`pet.py` 的 `resource_dir()` 在打包后走 `sys._MEIPASS`,直跑时走脚本目录;打包配置见 `claude-pet.spec`。

## 架构

```
pet.py                  PySide6:Claude/Codex 会话扫描、养成状态机、原渠道跳转
qml/Main.qml            悬浮窗 + 气泡 + 面板/菜单窗口管理
qml/Pet3DBody.qml       透明 WebEngineView + 鼠标交互(单击/双击/右键/拖动)
qml/PetMenu.qml         喂养菜单(右键)
qml/PanelContent.qml    多 AI 会话筛选 + 渠道标签 + 历史 / 原会话跳转
qml/PetBody.qml         2D 后备小猫(无 WebEngine 时)
web/index.html          Three.js 宿主页(透明背景)
web/js/pet3d.js         渲染层:18 宠物加载归一化、IBL 三点光、看鼠标转头、
                        呼吸/眨眼、吃饭/摸摸/玩球/庆祝状态机、emoji 粒子
web/js/buddies.js       18 个程序化宠物模型(来自 claude-buddy-desktop)
web/js/GLTFLoader.js    GLB 加载器(高级猫用;import 路径改成了同目录)
web/assets/cat.glb      高级猫模型(Sketchfab,带骨骼 + 10.8s sit_A 动画)
web/js/three.module.js  Three.js(本地,离线可用)
```

GLB 模型接入要点(再加新模型时照抄):
- **防"公转"**:cat.glb 根节点自带 ~30 单位枢轴偏移,直接旋转会绕大圆;
  加载后按**蒙皮采样的真实包围盒**(`getVertexPosition`,蒙皮/morph 都覆盖)把内容中心平移回原点再缩放
- 绑定姿态的 bbox 不可信(猫尾伸直),要先 `mixer.update()` 推进到动画姿态再量
- 待机动画整段循环,**不要切片**(旧项目硬切 5 段导致接缝闪烁);多段动画用 `idleClip` 按名挑
- 毛发壳材质用半透明混合(`opacity 0.26 + alphaTest 0.04 + depthWrite false`),
  目标观感:体表干净色块、毛只在剪影边缘积累(两层毛壳叠加,单层要压很低);
  纯 cutout 会"一茬一茬",透明度过高整身蒙霜
- `sleepPoseT`: 睡觉时把待机动画定格在闭眼帧的时间点(cat.glb 是 5.0s)
- **Chromium 节流**:透明悬浮窗会被判成"被遮挡",rAF 掉到 ~6fps 动画慢放;
  必须带 `--disable-backgrounding-occluded-windows` 等三个 flag(pet.py 已设)

Python ↔ JS 走 QWebChannel:`petJson` 属性(状态)+ `petEvent` 信号(互动事件)+ `cursorMoved` 信号(视线)+ `walkChanged` 信号(遛弯走/停/方向)+ `userModelsJson` 属性(用户模型,anim 类型带 `slots` 槽位表);宠物状态存 `~/Library/Preferences` 的 `pet.state`。

动画宠物渲染要点:素材帧(ImageDecoder 解 GIF/WebP,`<video>` 解 MP4/WebM)画进 canvas → `CanvasTexture` 贴在竖立平面上挂进 body 组,呼吸/跳跃/影子/粒子全部复用 3D 管线;`toneMapped=false` 保原色;走路用 `mesh.scale.x=-1` 翻转。抠图见 `detectBg`/`keyInPlace`(边框众数桶做种子 → 色距<120 收内点 → 内点均值当背景色,按离散度自适应容差)。

浏览器单独调试渲染层:直接开 `web/index.html?demo=1`(需关 CORS 或本地 server),`window.PET.do('eat',{food:'fish'})` 手动触发动画。

## 数据从哪来(全部只读)

| 来源 | 用途 |
|---|---|
| `~/.claude/projects/*/*.jsonl` | 会话 transcript → 状态 / 标题 / Todo 进度 / 聊天历史 |
| `~/.claude/sessions/<pid>.json` | 活着的 claude 进程 → 哪些会话"开着"、来源是 Claude App / VS Code / 终端 |
| `~/Library/Application Support/Claude/claude-code-sessions/` | Claude App 本地会话 ID 映射 → 精确打开 App 原会话 |
| `~/.codex/state_*.sqlite` | Codex 官方本地会话索引 → 标题 / 项目 / 模型 / 分支 / 最近活动(只读连接) |
| `~/.codex/sessions/**/*.jsonl` | Codex rollout → 运行状态 / 最终回复 / 历史(只读) |

状态判定规则:
- transcript 15 秒内有写入 → **正在干活**
- 进程活着但没在写 → **开着 · 等你**(最后停在工具调用上则提示**可能等授权**)
- 进程已退出:最后一条是 Claude 的回复 → **等你回复**;停在工具调用/你的消息上 → **已中断**
- 超过 2 小时没动静 → **空闲**
- Codex 以 `task_started/task_complete` 判定运行/完成;已结束会话按索引真实时间降级为空闲,不受迁移任务批量 touch 干扰

## 聊天页注意

- 续聊走 `claude -p --resume <id> --output-format stream-json`,在会话原目录执行
- "正在干活"的会话禁止插话(避免并发写 transcript)
- 在桌面端/终端开着的会话可以发,但对方界面不会实时刷新(会有黄条提醒)
- "自动同意文件编辑" = `--permission-mode acceptEdits`;不开的话,需要权限的操作会被拒绝
- 某些情况下续聊会 fork 出新 session id,宠物会自动跟过去
- 会话卡片按真实来源显示 **Claude App / Codex App / VS Code / 终端**;点击后用各客户端会话深链直达,终端来源执行对应 CLI 的 resume
- Codex 历史在面板内只读;点卡片旁的「记录」查看,不会写入 Codex 数据

## 窗口行为

悬浮在状态栏层级(level 25):所有空间可见、**全屏 App 上方也显示**;accessory 模式无 Dock 图标。退出靠面板里的"退出宠物"或 `pkill -f pet.py`。

白影防护(v1.4.3 起多层):默认**软件合成**(`--disable-gpu-compositing`,从机制上消灭"旧 GPU 表面残留成白影",CPU 约 +7%,`CLAUDE_PET_GPU=1` 可换回)+ macOS 15 窗口属性互斥修复(NSPanel 不抢焦点)+ 锁屏自动藏窗/解锁重建 + 关面板重建表面 + WebGL 上下文丢失即藏画布。

## 开机自启(可选)

`~/Library/LaunchAgents/com.claude-pet.plist` 指向 `run.sh` 即可,或加到"登录项"。

## 卸载

`rm -rf` 本目录即可,没有任何系统级改动(只有 `~/Library/Preferences` 里位置和宠物状态两条记录)。

## 许可与致谢

代码 MIT(见 [LICENSE](LICENSE));三方模型/库的许可与"仓库不含哪些模型、如何自备"见
[NOTICE.md](NOTICE.md) 与 [web/assets/README.md](web/assets/README.md)。
高级猫/我的狗两个模型因许可与隐私不入库,缺失时自动退回程序化形象,不影响运行。

隐私:会话扫描只读 `~/.claude` / `~/.codex` 本地文件(含 Codex SQLite 的只读连接)，抠图走 macOS 系统框架。额度读取通过本机 Codex CLI 查询账户；开启自动唤醒后，续跑消息由原客户端发送给对应 AI 服务。等待队列和运行记录保存在本机，无遥测。
