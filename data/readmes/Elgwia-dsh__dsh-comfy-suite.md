# dsh-comfy-suite

> **个人整合项目，不是任何上游插件的官方版本。**
>
> 本仓库把三个 MIT 许可的 DSH 插件合并成一个：一个 Loader 条目、一个设置入口、一份代码，
> 并附上一组真机修复与本地功能。三个上游才是各自能力的维护方：
>
> - [dsh-comfyui](https://github.com/fandc520/dsh-comfyui) 0.5.5 —— 工作流库 / `comfyui_*`
> - [dsh-qwen-paint](https://github.com/yanfei0725/dsh-qwen-paint) 0.17.13 —— 出图 / 修图 / 捏人
>   （原作者 [@奇迹与你](https://github.com/wonderandyou)）
> - `dsh-comfyui-launcher` 1.0.0 —— 本仓库作者自建，未单独发布
>
> **只想用其中一个功能，就直接装上游**，不要装这个整合包。本包定位是「合并实验 + 修复集」，
> 锁定 2026-11-13 快照，不承诺跟进上游更新。第三方许可与逐条修改见
> [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。

把三个 DSH 插件合成**一个**插件：一个 Loader 条目、一个设置入口、一份代码。

| 原插件 | 在本包里的位置 | 能力 |
| --- | --- | --- |
| `dsh-comfyui` 0.5.5 | `vendor/comfyui/` | 工作流库、`comfyui_workflow` / `comfyui_skill` / `comfyui_object_info` / `comfyui_run`、媒体代理、技能包 |
| `dsh-comfyui-launcher` 1.0.0 | `vendor/launcher/` | `comfyui_server`：启停配置里指定的便携版 ComfyUI |
| `dsh-qwen-paint` 0.17.13 | `vendor/qwen-paint/` | `draw_image` / `inpaint_image` / `outpaint_image` / `character_image` / `upscale_image` / `list_available_models` / `check_acceleration` |

对外只有一个 Loader 条目（`comfy-suite`）、一个包、一个设置入口。
合并后模型侧应看到 **14 个工具**；`boot.log` 里的 `tools audit` 行会逐次核对。

> 2026-11-05：借鉴 [`dsh-image-gen`](https://github.com/shanliuling/dsh-image-gen) 补了两件事——
> **作品库**（图库：检索 / 收藏 / 复用参数 / 回收站）与**风格库**（62 条提示词积木，
> 外加给模型用的 `image_presets` 工具）。详见下方「作品库与风格库」。
>
> 2026-11-12：借鉴一套 9 步整合画布（Qwen2.1-Turbo-9步-编辑&扩图&移除&重绘&生图）——
> **采样换成显式 9 步 sigma 表**（`ManualSigmas` + `SamplerCustomAdvanced`），
> 局部重绘同步升级，并新增 **`outpaint_image`（扩图）**。详见下方「9 步采样与扩图」。
>
> 2026-11-13（1.6.0）：**面板实时进度** + 一轮宿主侧审计修复。详见下节。
>
> 2026-11-17（1.6.2）：面板离线体验修复——ComfyUI 没启动时点开面板不再弹报错。见下节。

## 1.6.2：ComfyUI 没启动时，点开面板不再报错

**症状**：ComfyUI 没运行（最常见的情况）时点标题栏的「ComfyUI 面板」，整个面板刚打开就被关掉，
页面顶部弹出一条通栏错误：「后端未能连上 ComfyUI（fetch failed（探测地址 http://127.0.0.1:8188））……」。
用户看到的是"插件坏了"，而不是"服务没开"。

**根因**：`connection` 探测把"连不上"当成致命错误处理——`panelStore.close()` 关面板，
再渲染一条页面级 toast；`fetch failed` 是 Node `fetch` 的传输层文案，被原样搬上了界面。
可面板里的工作流库、作品库、设置页都是本地数据，后端离线完全不影响它们。

**修复**：

- **面板不再关**：探测失败只改状态，不碰 `panelStore`。离线时面板照常打开、照常能看能导工作流。
- **错误条换成面板内提示**：标题栏下面多一条 `ComfyUI 未启动` 的横幅（工作流/资产/队列哪一页都在），
  带 **启动服务**（POST `/comfyui-launcher/start`，就绪后横幅自动消失）和 **重新检测** 两个按钮；
  不再是页面顶部那条通栏报错，也不再出现 `fetch failed` 字样。
- **宿主侧分级**（`vendor/comfyui/lib/routes.js`）：`POST /comfyui/test` 现在一并返回
  `offline`（`ECONNREFUSED`/`ETIMEDOUT` 等套接字层判定）、`code`、`reason`、`baseUrl`；
  客户端据此把"没启动"和"地址/鉴权配错"分开说。老客户端/老宿主都兼容（客户端也会自己识别 `fetch failed`）。
- **面板块里的原始报错一起收口**：工作流页的「ComfyUI 工作流」、队列页、标题栏状态条在离线时
  分别显示「ComfyUI 未启动，启动后这里会列出服务端保存的工作流」「ComfyUI 未启动，队列里还没有任务」
  「ComfyUI 未启动」，不再把 `fetch failed` 当下发给用户。设置页的「测试连接」同样改成
  「连接失败：<地址> 没有响应（ComfyUI 可能未启动）」。

**回归**：`test-client.mjs` 新增离线场景（探测失败后面板必须仍打开、横幅文案正确、不外泄 `fetch failed`）；
`test-routes.mjs` 新增 `/comfyui/test` 的离线分类断言（把 baseUrl 指到必然关闭的 65530 端口）。

## 1.6.0：实时进度、效率与一批真 bug

### 面板：任务实时进度监测

- **标题栏状态条**（新增）：面板标题下面那行常驻显示 `正在生成 · 工作流名 · 3/9 步 · 约 42s 后完成 · 队列 1`，
  空闲时显示「空闲」，进度通道没连上时明确写「进度通道未连接」（生成照常，只是没有实时数字）。
  右侧是百分比，下面是 3px 进度条；还没拿到第一步时走不确定态动画。
- **「任务」页大进度卡**：正在生成的任务单独一张卡，显示步数 / 节点号 / 已用 / 预计剩余，
  带中断按钮；列表里的运行中任务也有秒级走时（不再是「耗时 0s」）。
- **工具卡片**：`comfyui_workflow run` / `comfyui_run` 的卡片改为读 `/comfyui/live`，
  带步数与 ETA，且不再每 2 秒往 ComfyUI 打一次 `/queue`。
- **数据来源**：宿主新增 `GET /comfyui/live`，完全由已连接的 ComfyUI WebSocket 事件
  （`status` / `execution_start` / `executing` / `progress` / `execution_error` /
  `execution_success` / `execution_interrupted`）与内存里的运行表算出，**不产生任何上游请求**，
  所以可以按 0.9 秒轮询；页面不可见时自动降频，空闲时 2.5 秒一次。
- **布局与渲染**：面板默认宽度 420（可拉到 720），标题栏更紧凑；标签页带「运行中」圆点；
  拖动固定位置后**自动补高度**（旧实现会把面板变成内容高度、正文不再滚动）；
  Esc 关闭面板（输入框内不抢）；资产页每 8 秒自刷新；加载区失败/降级现在会显示原因，
  不再把「服务器离线」显示成「一个素材都没有」。

### 出图 / 出视频效率

- **`/object_info` 缓存从 60 秒提到 30 分钟**，并补到 6 个此前绕过缓存的调用点
  （识别参数、下拉选项、刷新参数、加载区、`comfyui_object_info`、图→API 提取）。
  装了自定义节点的机器上这张表是 5–20 MB，过去「隔一分钟再出图」就要先整份下载+解析，
  而且串在提交之前。
- **提交前三次读盘并行化**（object_info / 加载区槽位 / 素材尺寸）。
- **完成检测改为事件驱动**：WebSocket 在就绪时是权威信号，`/history` 轮询从每秒一次降到每 5 秒一次
  （10 分钟的视频约 600 次请求 → 120 次），任务结束那一刻立即收图；单次轮询抖动不再判整次生成失败。
- **超时不再丢结果**：等待预算用完时任务仍在 ComfyUI 里跑，现在保持 tracked，
  媒体落地后照样进资产索引/作品库，工具返回「仍在运行」而不是「失败」。
- **队列扫描**：历史读取并发 4 路（过去串行，资产页有 N 个待归档任务就 N 个来回），
  归档后立刻从跟踪表移除，永不出现的 run 连续 10 次拉不到就丢弃（过去会永远重拉）。
- qwen-paint：节点 schema 加 120 秒缓存（局部重绘每次少 3–7 次 `/object_info`），
  每 5 秒一条的诊断日志不再无条件写（与已节流的状态日志重复），
  加速自检定时器并入 `ctx.effect`（热重载不再叠加多份并发）。

**本机实测（2026-11-13，ComfyUI 0.42.3 / RX 9060 XT）**

| 项 | 数字 |
| --- | --- |
| `/object_info` 体积 | 4.62 MB（这就是过去"隔一分钟再出图"要先下载解析的那份） |
| `/comfyui/live` 响应 | 1–2 ms（冷启 59 ms） |
| `/comfyui/loadarea` | 冷 529 ms（含一次 object_info 下载）→ 热 **2 ms** |
| `/comfyui/jobs` | **3 ms**（资产名改成内存映射，过去每次重解析整份 assets.json） |
| 视频实测 | MiniMax-H3 int4、56 帧、4 步：**438 s** 出片（含约 150 s 权重装载，每步 ≈87 s），进度条与 ETA 全程跟随 |
| 图片实测 | 544²、9 步、seed 固定：**51.7 s** |

### 修掉的真 bug（每条都有触发条件）

| # | 位置 | 症状 |
| --- | --- | --- |
| 1 | `comfy-ui/store.js` | 所有 JSON 都是**就地整文件重写**且无串行化：崩溃/断电留下半截文件，下次读取当成「没有」返回空列表，再保存一次就把整个工作流库清空；面板保存与 Agent 刷新并发时后写覆盖前写。现在 temp+rename 原子写、按文件串行、坏文件转存 `.corrupt-<ts>` 并写回执 |
| 2 | `vendor/qwen-paint/comfy-accel.js` | 跨模块给 `export let SAGE_READY` 赋值 → ESM 抛 `TypeError`，加速自检**每次都在装包前中止**，`--use-sage-attention` 永不生效。改为 `setSageReady()` |
| 3 | `vendor/qwen-paint/index.js` | 权重下拉的闸门参数写成 `unet/lora/controlnet`，面板发的是 `mainmodel/lorapick/cnetpick` → 三个下拉**静默无效**（端点照回 ok） |
| 4 | `vendor/qwen-paint/index.js` | `freeComfyModels` 里 `log?.()` 引用未声明标识符，**照样抛 ReferenceError**，把「卸载失败不影响后续」变成 upsell/修复流程整体失败 |
| 5 | `vendor/qwen-paint/index.js` | 中断的任务不认识 `execution_interrupted`，对已结束的任务按 400ms 轮询满 300 秒，最后报「超时」 |
| 6 | `vendor/comfyui/progress.js` | WebSocket 只处理 `progress`：Map 无界增长、终态事件全丢、attach 不幂等、重连固定 3 秒无退避 |
| 7 | `vendor/comfyui/comfyui.js` | 路由前缀靠「404 再发一次」学习：合法 404（已删的预览/被清的历史）**永远双倍请求**，POST 还可能被执行两次 |
| 8 | `vendor/comfyui/params.js` | 选项校验把「调用方没传、用的保存默认值」也当非法：音色/模型文件一变，工作流**完全跑不了**，错误还把整份选项列表塞进上下文 |
| 9 | `vendor/comfyui/params.js` | 宽高参数按节点 id 先到先得，可能被缩放节点抢走 → 面板设 1920×1080 实际改的是 resize 节点 |
| 10 | `lib/gallery.js` | 删除用 `rename` 到 E: 的回收站，图在 C: → **EXDEV，删除从来没成功过**；且回收站目录被拼两次（`trash/trash/`） |
| 11 | `lib/gallery.js` | 墓碑永不失效：从回收站放回来的图仍然隐形，与「放回来就等于撤销」的注释相反 |
| 12 | `lib/presets.js` | 检索上限硬夹到 50：62 条风格里最后 12 条在面板里永远没有入口，`total` 却写 62 |
| 13 | `lib/hidden-launch.js` | `void runPowerShell(...)` 没挂 catch：一次隐藏窗口失败 = 未处理 rejection = **Node 直接终止 DSH 主进程** |
| 14 | `vendor/comfyui/http.js` | 请求体无上限，`/comfyui/upload` 与预设导入都是先全量缓冲再检查 → 一个大文件打爆宿主堆 |
| 15 | `vendor/comfyui/routes.js` | `object_info` 失败被吞成 `ok:true`，面板拿到「成功」的降级参数并保存进库；加载区选「已生成」找不到文件时静默成功 |

## 结构

```
dsh-comfy-suite/
  package.json            dsh.bundle.patch + dsh.client + scripts
  cordis.patch.yml        唯一的条目与三块配置（comfyui / launcher / qwenPaint）
  lib/
    index.js              聚合宿主：挂三个子插件、转发配置写入、写启动回执
    config.js             嵌套 schema（comfyui 用原 schema，另两块透传）
    bridge.js             子插件 ↔ 条目的配置写入 / 刷新 / 回执通道
    hidden-launch.js      ComfyUI 的零窗口 + 脱离宿主启动（wscript/SW_HIDE）
    gallery.js            作品库的扫描/索引/回收站（纯函数，可单测）
    gallery-routes.js     作品库与风格库的 7 个 HTTP 端点
    presets.js            风格库的加载/检索/拼句
    presets/qwen-presets.json  62 条提示词积木（纯数据，改文案不用碰代码）
    wardrobe.js           提示词衣柜引擎（档位闸门/三层权重/可复现/自检）
    presets/qwen-wardrobe.json 衣柜词库（层/字段/选项/场景，人写数据）
    tools.js              给模型用的 image_presets / prompt_wardrobe 工具
  vendor/                 三份原插件代码（已打合并补丁）
  client/
    client.js             四份 client bundle 拼成的唯一 factory（产物）
    _parts/               拼接源：head + 三份 vendor client + suite_gallery + tail
  scripts/build-client.mjs  client.js 的可复现构建（--check 校验）
  test-host.mjs           宿主冒烟测试（工具集、失败隔离、回执、设置写入）
  test-gallery.mjs        作品库/风格库单元测试（文件头解析、越界、检索、回收站）
  test-sampling.mjs       采样引擎回归（9 步 sigma 表 / 重采样 / 两种档位的节点形状）
  test-outpaint.mjs       扩图回归（留白计算 / 8 对齐 / 上限收敛 / 尺寸读取）
  test-library.mjs        GHIL 图库回归（索引 / 检索 / id 解析 / 尺寸 / 默认提示词）
  test-routes.mjs         端点集成测试（真喂请求，含同源/方法/类型守卫）
  test-client.mjs         客户端冒烟测试（私有模块表、五个 tab、组件物化、面板实时进度渲染）
  test-comfyui.mjs        宿主纯函数测试（校验错误渲染、媒体判定、content-type）
  test-wardrobe.mjs       衣柜引擎单元测试（闸门 / 权重 / 复现 / 场景 / 裁剪）
  install.sh              安装 / 重装（默认 link）
  rollback.sh             恢复最近一次 package.json / cordis.patch.yml 备份
  node_modules/           自带的 schemastery + cosmokit + fflate（见下）
```

### 为什么不是一个文件堆在一起

三个子插件仍然各自是**独立的 cordis fiber**（`ctx.plugin()`），各自的 `inject`、
`ctx.effect` 清理、工具注册、REST 路由都保持原样。合并只发生在三个边界上：

1. **Loader 条目**：从三条变一条，`cordis.patch.yml` 里只有 `id: comfy-suite`。
2. **配置**：一个条目下三块 `comfyui` / `launcher` / `qwenPaint`。`comfyui` 块沿用
   原 Schemastery schema，`.volatile()` 字段照旧由 Loader 提交进运行引用；另两块
   原样透传（子插件自己合并 DEFAULTS）。
3. **客户端**：三个 bundle 不再各自向 `window.__ModuleLoader__` 注册新包 id，而是
   收进 `window.__DSH_SUITE_MODULES__` 私有表，由唯一的 `dsh-comfy-suite` factory
   物化。设置页合并成一个 section、五个 tab：「工作流与生成」「作品库」「风格库」
   「提示词衣柜」「服务启停」。

### 配置保存怎么走

原 `dsh-comfyui` 的设置页保存走 `settings.update('comfyui', patch)`，按条目 id 定位；
合并后条目 id 是 `comfy-suite`，所以那一处改成 `suiteBridge.update(...)`，由聚合层
转成 `settings.update('comfy-suite', { comfyui: patch })`。Loader 提交 volatile 值后
只通知条目 fiber，子 fiber 收不到 `loader/volatile-update`；`bridge.register/refresh`
负责把刷新扇出给子插件，`bridge.report` 负责把子插件的注册结果写进启动回执。

`dsh-qwen-paint` 的界面偏好写自己的 `qwen-paint-ui.json`，与条目 id 无关，未改动。
启动器的设置页只有启停/日志，没有配置写入。

## 安装 / 重装

### 前置条件

- **DSH** `>=0.2.1-rc.5 <0.3.0-0`（`engines.dsh` 会强制校验）
- **Node** `>=22.19`
- **平台**：Windows（零窗口启动走 `wscript.exe` + VBS；其他平台未验证，`install.sh` 是
  bash，Git Bash / WSL 可用）
- **ComfyUI**：一套能跑的安装（便携版或源码版都行），并在下面「必改配置」里填对路径

### 装法

```bash
# 1) 克隆或解压到任意目录，例如 ~/dsh-comfy-suite
# 2) 改 profile 配置（见下一节）
# 3) 安装（Git Bash 示例）
PROFILE=/c/Users/you/.dsh/profiles/desktop bash install.sh
```

`install.sh` 的目标是 `$PROFILE/node_modules/dsh-comfy-suite`；`PROFILE` 不传时按
`$DSH_HOME/profiles/desktop` → `~/.dsh/profiles/desktop` 的顺序取默认值。

- 默认 **link** 安装：改本目录的代码即刻生效（热重载后）。
- `--copy` 物理复制：改本目录不再直接影响运行副本。
- 脚本顺序是「校验 → 备份 → 再动目标」：缺 `package.json` / `lib/index.js` /
  `client/client.js` / `cordis.patch.yml` 直接中止、不删任何东西；覆盖前把 profile 的
  `package.json`、`cordis.patch.yml` 和现有运行副本备份成带时间戳的文件；
  最后 `import()` 一次做装后自检。
- 装完给 `<profile>/cordis.patch.yml` 末尾追加一行注释即可触发热重载，不必重启宿主。

### 必改配置

`cordis.patch.yml` 三块路径默认指向作者本机的便携版布局（`D:/dsh-video/a/...`），
**换成你自己的 ComfyUI 安装目录**，否则启停与出图都会找不到文件：

| 配置块 | 字段 | 指向 |
| --- | --- | --- |
| `comfyui` | `comfyuiDirs` / `outputDir` | ComfyUI 根目录与其 `output/` |
| `launcher` | `comfyuiDir` / `pythonPath` | ComfyUI 根目录与它自带的 python |
| `qwenPaint` | `comfyPython` / `comfyMainPy` / `comfyWorkdir` | Python、`main.py`、工作目录 |

主模型默认是 `Qwen-Image-2.1-Turbo-AD-Q6_K.gguf`，要跟你的 `models/` 里的文件名一致；
换模型就改 `qwenPaint.unet`（GGUF 走 `UnetLoaderGGUF`）。

### 自带依赖

`node_modules/` 里 vendored 了三份东西，所以 **link 安装和物理复制都能解析**：

- `@deepseek-ai/schemastery`（配置 schema）+ 它缺的运行时依赖 `@deepseek-ai/cosmokit`
- `fflate`（`vendor/comfyui/lib/transfer.js` 用它解压上传）

旧版只 vendored 了 schemastery，是从 link 形态（Node 保留 profile 前缀解析）跑通的；
一旦按 `install.sh` 物理复制，`import '@deepseek-ai/cosmokit'` 立刻报
`Cannot find package`——本包现在不靠宿主 flag，两种形态实测都能 `import()`。

## 诊断：`boot.log`

每次激活都会往 `$DSH_HOME/data/dsh-comfy-suite/boot.log` 追加回执（超过 256 KB 自动
只留最近 300 行）。正常一次激活长这样：

```
apply pid=17212 blocks=comfyui,launcher,qwenPaint
comfyui: apply start
launcher: apply start
qwenPaint: apply start
children mounted
qwenPaint: apply settled in 184ms
launcher: apply settled in 103ms
comfyui: apply settled in 438ms
comfyui: tools 4/4
tools audit: 10/10 present
```

出问题时就多了能直接定位的行：

| 回执行 | 含义 |
| --- | --- |
| `xxx: apply still pending after 15000ms` | 子插件 `apply()` 卡住，工具不会注册 |
| `xxx: apply rejected … — <msg> @<frame>` | 子插件初始化抛错，附第一处插件代码栈帧 |
| `comfyui: tools 3/4, failed — comfyui_workflow: duplicate …` | 单个工具注册失败，其余照常 |
| `tools audit: 9/10 — MISSING comfyui_workflow` | 模型侧真的少了一个工具 |

**为什么加这些**：2026-11-04 合并后出现过一次「界面正常、`draw_image` 正常，但 4 个
`comfyui_*` 工具从模型工具表里消失」。原因是合并窗口里新旧插件可能同时注册同名工具，
一个 `register()` 抛错就把整批工具带走，而当时的回执只写了 `children mounted`，
没有任何地方能看出少了什么。现在：四个工具逐个注册、互不连坐，失败原因和
`tools audit` 都落盘；`test-host.mjs` 里有对应的回归用例。

## 作品库与风格库（2026-11-05，借鉴 dsh-image-gen）

`dsh-image-gen` 最值得抄的不是云端多模型，而是它把「出过的图」和「会用的风格」
都变成了**可复用的资产**。本套件补上了这两块，同时刻意避开了它的复杂度。

### 作品库：文件系统就是索引

| 事实 | 做法 |
| --- | --- |
| 图在哪 | `draw_image` 等的出图目录（默认 `<桌面>/千问1生图`，可用 `qwenPaint.outputDir` 改） |
| 怎么列 | 扫目录（3 层、最多 4000 张），读 PNG/JPEG/WebP **文件头**拿宽高，不装任何图像库 |
| 提示词哪来 | 复用 qwen-paint 早就在写的 `.qwen-paint-memory.jsonl`：先按整路径匹配，失败再按文件名 |
| 收藏存哪 | `$DSH_HOME/data/dsh-comfy-suite/gallery-state.json`（原子写，坏文件不炸） |
| 删除 | **移进 `…/dsh-comfy-suite/trash/`**，不是 `unlink`；误删可捞回 |
| 工作流产物 | 默认**不扫** ComfyUI 的 output（那里有千问图的中间副本，会重复显示）；面板勾选后才并入 |

界面在 **设置 → ComfyUI 套件 → 作品库**：搜索（提示词/文件名/种子）、全部/收藏切换、
时间排序、点开看大图与参数、复制提示词/路径、**换一颗种子再画 / 同种子复现**、删除。

「再画一张」不是前端拼参数：它把出图日志里的 prompt / negative / seed / 宽高
原样交给已经注册的 `draw_image.execute()`（与 qwen-paint 自己的圈选重绘端点同一条路），
所以画幅会按像素反算回 `1:1 / 3:4 / 4:3 / 2:3 / 3:2 / 16:9 / 9:16` 里最近的一档。

### 风格库：62 条提示词积木

`lib/presets/qwen-presets.json`：画风（水彩/国风/像素/赛博朋克…）、光效（体积光/伦勃朗光/霓虹…）、
构图（三分法/对称/俯拍…）、画质、负面词、海报版式。界面里可以检索、勾选、拼成一整句。

模型侧对应一个 **`image_presets`** 工具（`search` / `get` / `compose` / `kinds`）。
它的描述里写清了触发条件（用户点名某种风格、或说"没灵感"），这样 Agent 会自己去查、
再 `draw_image` —— 这正是 image-gen「Agent 自动套用 500+ Prompt」的机制，只是规模小一号、
全部本地。负面词条目会单独返回 `negative` 字段，不会被混进正向提示词。

### 端点（全部只服务同源页面）

```
GET  /api/comfy-suite/gallery?q=&scope=&sort=&limit=&workflow=1
GET  /api/comfy-suite/gallery/file?id=
GET  /api/comfy-suite/wardrobe
POST /api/comfy-suite/wardrobe/roll
POST /api/comfy-suite/wardrobe/draw
GET  /api/comfy-suite/presets?q=&kind=
POST /api/comfy-suite/gallery/favorite   {id, favorite}
POST /api/comfy-suite/gallery/delete     {id}
POST /api/comfy-suite/gallery/regenerate {id, seed: 'same'|'random'}
POST /api/comfy-suite/presets/compose    {ids, base}
```

安全边界：`id` 是绝对路径的 base64url，**解码后必须仍落在扫描根内**（`resolve` 后再比较，
`..` 折叠不掉）；跨站 `Origin` → 403，非 POST → 405，非 JSON → 415，正文上限 64 KB。
读图上限 48 MB。这些都有 `test-routes.mjs` 的用例兜着。

## 提示词衣柜（2026-11-12）

风格库是**查表**：你自己挑几条拼一句。衣柜是**抽签**：给档位、权重、种子，它给你一整段，
可复现、可审计。参考对象是
[`Comfyui-Anima-Wardrobe-V5`](https://github.com/lingdongbudong/Comfyui-Anima-Wardrobe-V5)
（灵冻不冻，GPL-3.0）。**移植的是引擎设计，不是它的词库**：那边是 danbooru 英文标签，
服务 Anima 底模；这边出图走 Qwen-Image，吃中文自然语言。所以词条按 Qwen 重写，
代码也是新写的（没有复制 GPL 代码或数据），本包仍是 MIT。

| 原项目点明的缺口 | 本套件的做法 |
| --- | --- |
| 盲抽后补锅：先按概率抽，抽完再给高档内容打补丁 | **先按档位收窄候选池，再抽**。`candidatesOf()` 是唯一准入点，权重再大也拉不回超档项 |
| 权重不可调 | **三层权重**：段 / 字段 / 选项。`0`=关闭，`1`=常态，`3`=必现；权重**不参与**档位判定 |
| 结果出不去 | STRING 直出：`PROMPT` / `NEGATIVE` 两行直接喂 `draw_image`，也能在面板里一键画 |
| 不可复现 | 同 `seed` 同设置逐字一致；种子是 crc32/整数，不是按进程加盐的 hash |
| 没法审计 | 每次自带 `report`：档位是否被抬、种子、哪些字段被闸门/权重/互斥/上限让路，逐条写明 |

### 词库长什么样

`lib/presets/qwen-wardrobe.json` 是**人写数据**，加载时完整校验（场景引用了不存在的选项、
锁定项高于场景档位，都会让那条场景停用并写进 `boot.log`，而不是静默缺一块）。

| 段 | 字段 | 选项 | 最高档 | 说明 |
| --- | --- | --- | --- | --- |
| subject 主体 | who | 8 | L0 | 用户给了 `subject` 就整段跳过 |
| identity 人物特征 | age/face/hair/eyes/skin/body/expression | 42 | L3 | 抽到 `who` 后才知道性别，后续按性别收窄 |
| outfit 服装 | top/bottom/shoes/wrapper/accessory/state | 46 | L3 | 连体款（长裙/浴衣/床单）带 `omit`，选中后压掉下装 |
| pose 动作姿态 | stance/action/gaze/mood | 27 | L2 | |
| scene 场景 | place/weather/time/detail/crowd | 41 | L1 | |
| camera 镜头 | shot/angle/lens/dof | 21 | L0 | 七分身/胸部以上只在 person 模式出现 |
| style / lighting / composition / quality / negative | preset | 36/8/6/4/2 | L0 | **直接用 `qwen-presets.json`**，不重复维护 |

另有 **16 条场景搭配**（跨字段固定组合）：锁住的字段不参与随机，其余照常抽 ——
所以同一个"雨夜霓虹·回眸"每次的头发、表情、衣着都不同，但地点/天气/光线/机位是稳的。
场景声明的档位必须 ≥ 它锁定的每个选项的档位，这条在加载时强制（否则就是低档场景夹带高档词的漏洞）。

### 怎么调

```
prompt_wardrobe action=roll level=1 seed=2026 scene=sc-rain-neon
prompt_wardrobe action=roll level=2 weights={"outfit.top":3, "style.preset":0} forced={"identity.hair":"高马尾"}
prompt_wardrobe action=scenes level=0 query=雨
prompt_wardrobe action=meta
```

几条容易踩的语义，都是刻意这么定的：

- **显式指定会抬档**：`forced` 点了 L2 的项、或 `scene` 指了 L2 的场景，整张图按 L2 抽，
  报告第一行会写 `L0 → L2`。随机抽样**永远**不抬档。
- **必现项不裁**：`tagCap` 裁的是随机项；`req` 字段、场景锁定、被权重点名"必现"的项一律不裁
  —— 裁掉它们等于把"必现"变成"通常出现"。显式项本身就超过上限时，报告会说明为什么没裁到 cap。
- **权重 3 会把字段也变成必抽**：否则"必现的选项"会因为字段整体没被抽中而消失。
- **性别只在明确时收窄**：`who` 抽到"一位男性"后，后续不会再抽"低盘发/比基尼"；
  用户自带 `subject` 且没给 `gender` 时**不过滤** —— 猜错性别比不猜更糟。

### 端点

```
GET  /api/comfy-suite/wardrobe          全量词库（层/字段/选项/场景/档位）
POST /api/comfy-suite/wardrobe/roll     抽一版或多版（与工具同一个引擎）
POST /api/comfy-suite/wardrobe/draw     把抽到的 prompt 交给 draw_image（面板「画一张」）
```

面板在 **设置 → ComfyUI 套件 → 提示词衣柜**：档位、模式、主体、场景、种子，
抽完可以复制，也可以直接出图。客户端 bundle 改了要刷新窗口（Ctrl+R）。

## 9 步采样与扩图（2026-11-12，借鉴 9 步整合画布）

来源：`▶▷Qwen2.1-Turbo-9步-编辑&扩图&移除&重绘&生图（整合）.json`（ComfyUI 画布，154 节点 /
5 个独立流程）。**移植的是做法，不是它的连线**：那张画布依赖 `孤海`/`GH`/`Goohai` 三个
第三方节点包和 5 个 LoRA（`Qwen-功能2.1/*`），本机都没有；这里只用 ComfyUI 自带节点
+ 本机已有模型，把那五个流程的**工作点**搬过来。

### 采样：把 `scheduler:simple` 换成显式 sigma 表

画布 5 个流程都用同一套：`ManualSigmas` + `SamplerCustomAdvanced` + `KSamplerSelect(euler)` +
`CFGGuider(cfg=1)`（扩图/移除两支用 `BasicGuider`，cfg=1 时两者出图逐像素一致）。表长这样：

```
1.0, 0.978453, 0.954180, 0.926626, 0.895080, 0.845148, 0.704534, 0.414568, 0.150000, 0
```

它不是"随便一串数"：`simple` 调度器是按 sigma 分布现场推导的通用调度，而这串数是
**针对 turbo 蒸馏模型调过的步序**（前 5 步几乎等高、后半段陡降）。本机实测（1024²，同 seed）：

| 链路 | 耗时 | 锐度（拉普拉斯方差） | 备注 |
| --- | --- | --- | --- |
| 旧：KSampler 8 步 + simple（含 TE-Speed/Speedup） | 20.9 s | 135.9 | 基准 |
| **新：ManualSigmas 9 步** | 20.9–24.1 s | **140.6** | **不比原来慢，细节略好** |
| 画布的 8 步变体（表尾截到 0.414568） | 21.1 s | 106.5 | 明显发糊 —— 那是截断表，**不用** |

局部重绘更明显（同图同蒙版，denoise 1.0）：

| 链路 | 结果 |
| --- | --- |
| 旧：无 turbo LoRA、4 步、`ModelSamplingAuraFlow(shift 3.1)` | 蒙版区留一条**发白的雾带**（没收敛） |
| **新：turbo LoRA + 9 步表** | 干净、与周围光影自然融合，接缝不可见 |

> 4 步是"8 步蒸馏 LoRA 再砍一半"的工作点；**缺了 LoRA 还跑 4 步**才是那条雾带的根源。
> 所以这次把重绘/扩图一并接到同一条 turbo9 链上。

三个实现细节：

- **不接 `ModelSamplingFlux`**。表的数值是在模型原生 shift 下标定的，再叠一层 flux 位移会把
  sigma→timestep 的映射挪走（画布本身也没有这个节点）。`ksimple` 档保持原样。
- **`denoise` 变成"从第几档起跑"**：`SamplerCustomAdvanced` 没有 denoise 参数，它体现在
  sigma 表被切掉开头几项。`denoise=0.7` ⇒ 从 0.845148 起。
- **工具里的 `steps` 是对同一张表重采样**（线性插值、末尾恒 0），不是换调度器。

开关在 `qwenPaint.samplingProfile`：`turbo9`（默认）/ `ksimple`（老链路，留作对照）。
没有 turbo LoRA 的机器会被自动忽略（那种情况本来就走 25 步 / CFG 2.5 的原生链路）。

实现落在 `vendor/qwen-paint/lib/sampling.js`（表 + 重采样/截档函数）：
`config.js` 已经 249 KB，逼近 DSH STORE 的单文件 262144 字节上限，所以这张表单独一个文件。
（顺带一条实测结论：`TextEncodeQwenImage21` 的 `resolution` 在**已经给定 latent** 时影响极小 ——
同 seed 下 1024 与 1376 两档的新增区锐度完全一致（75.7 / 246.2），肉眼也看不出；
文件不是逐字节相同，但那是数值噪声级别。所以传画布长边或固定 1024 都行。）

### 扩图：`outpaint_image`

画布的「图像扩展」支路靠 `孤海外补画板可视化` + 一堆数学节点算留白；这里换成
**ComfyUI 自带的 `ImagePadForOutpaint`**（它直接输出"补好的图 + 新增区域蒙版"），
再把蒙版挂到 latent 的 `noise_mask` 上 —— 于是**新边是生成的、原图像素一个不动**。

```
outpaint_image image=D:\a.png aspect=16:9
outpaint_image image=D:\a.png expand=0.25
outpaint_image image=D:\a.png sides={"right":0.5,"top":256}
outpaint_image image=D:\b.png aspect=3:4 prompt="上边补出天空与屋檐，延续原有透视"
```

- `aspect` 按目标画幅算（方图 → 16:9 只补左右；→ 3:4 只补上下）。
- `expand`/`sides`：**≤4 当比例**（0.25 = 各边 25%），**>4 当像素**（256 = 各边 256 px）。
- 四边一律**对齐 8 的倍数**（潜空间 1/8 分辨率，不对齐会留半格毛边）。
- **羽化默认 96 px**，不是拍脑袋定的：同图同种子，量"接缝处相邻列的差分 / 全图中位数"
  —— 0 px（硬边）7.8 倍、48 px 4.4 倍、**96 px 2.5 倍**（与"本来就没有接缝"的那张参考图同档）。
  羽化会自动收敛到「最小留白的一半」，小图不会被过渡带吃光留白。
- 成图上限 = `max(maxEdge=2048, 原图 1.5 倍)`，超了**只收敛留白**（原图不缩），并回报 `clamped`。
- **画布超过 1.15 MP 自动把步数加到 16**：1024² → 1024×1360 竖扩实测，新增区锐度
  9 步 57.9 / 12 步 70.8 / **16 步 90.9**（拉普拉斯方差；原图那一带三次都是 39.4，说明被保护的
  像素一个没动），用时只多约 10%。不做这一步，扩出来的边会明显发软、像蒙了层薄雾。
- 读尺寸支持 PNG / JPEG / WebP；读不出来就报错，不猜（猜错 = 扩歪）。

真机验证：1024² → 1824×1024（左右各 400 px），46 s（新尺寸首次要重载模型），
接缝不可见、光线与景深延续，中心区域逐像素保留。

### 和画布的差距（如实记）

| 画布里的东西 | 本机状况 |
| --- | --- |
| `qwen_image_2.1_turbo_int8_convrot`（已蒸馏主模型） | 没有；用 `qwen_image_2.1_int8_convrot` + `turbo8_lora_step2500` 等效替代 |
| `qwen3vl_8b_int8_convrot`（CLIP） | 没有；用 `qwen3vl_8b_w4a8` |
| 扩图 / 万物移除 / 一致性 三个功能 LoRA | **都没有** —— 所以移除只能走"蒙版 + 指令"的通用重绘，没有专用权重 |
| `QwenImagePromptOptimizer` + `Qwen-Image-2.1-PE-*.gguf`（LLM 改写提示词） | 没有权重；`TextGenerate` 节点在，但没有对应的 PE 模型，暂不接 |
| `孤海` / `GH` / `Goohai` 节点包（裁切-还原、绿幕蒙版、画板） | 未安装；扩图/重绘改用自带节点实现同一效果 |
| 3 张参考图的编辑（`<image1>/<image2>/<image3>`） | `draw_image` 目前只接 1 张参考图（编码器支持到 4 张，工具层还没放开） |

把上面这些补上（放模型 + 装节点包）之后，画布的 5 条流程可以原样作为 API 工作流导入，
但**本包的默认链路不依赖它们**。

## 捏人 / 换装：`character_image`（2026-11-12，GHIL 素材库）

这个工具把两样东西接了起来：

| 资源 | 在哪 | 干什么 |
| --- | --- | --- |
| `Goohaitools-comfyui`（98 个节点） | `custom_nodes/` | 提供 `TextEncodeQwenImage21GH`——**支持 10 张参考图**的 Qwen 2.1 编码器（官方那个只有 1 个图槽） |
| `GoohaiImageLibrary-Comfyui` + `GHIL.7z`（6.68 GB / 13 984 文件） | `models/GHIL/` | 人像 1499 / 服装 1407 / 姿势 1439 / 发型 893 条，每条带 id + 原图 + 中文标签 |

工具做的事：从图库里挑「人像 + 服装（+ 发型 + 姿势）」→ 多参考图送进 GH 编码器 → 出图。
参考图按 **人像 → 服装 → 发型 → 姿势** 的顺序变成「图1/图2/图3/图4」，提示词里可以这么指代。

```
character_image action=list kind=人像 query=短发           # 先查 id
character_image portrait=f71f980dde3 costume=SPR-0001 size=3:4
character_image portrait="ghil:人像/f71f980dde3" costume="D:\assets\外套.jpg" prompt="..."
```

- 参考图三种写法都认：纯 id（按参数名推类型）、`ghil:人像/<id>`、本地绝对路径。
- 图库根目录 `qwenPaint.ghilRoot`，留空则从 `comfyMainPy` 推 `<ComfyUI>/models/GHIL`。
- 提示词不填就自动拼一句（影棚全身像 + 逐条点名"保持图N的面部特征/穿上图N的服装"）。

**实测**（本机 RX 9060 XT，864×1152，两张参考图，turbo9 采样）：

| `ref_image_size` | 执行耗时 | 成图锐度 |
| --- | --- | --- |
| 自动（默认） | 98 s | **127.4** |
| 1024 | 105 s | 121.1 |
| 768 | **80 s** | 111.0 |

参考图分辨率直接决定耗时（编码器要把它们变成几十 k 个 token 再进注意力），
768 省 20% 但锐度掉 13%；所以默认 `自动`，嫌慢就配 `characterRefSize: '768'`。
`test-library.mjs`（14 条）盯着索引读取、检索、id→文件解析、尺寸计算这几件容易悄悄错的事。

> ⚠ 这个工具**依赖 `Goohaitools-comfyui`**（`TextEncodeQwenImage21GH`）。
> 那包没装时工具仍在工具表里，但一提交就会被 ComfyUI 以"节点不存在"拒收——
> 报错原文会指出是哪个节点，按提示装包即可；`draw_image` / `inpaint_image` 不受影响。

## turbo GGUF 主模型（2026-11-12）

Qwen-Image-2.1-Turbo-AD-Q6_K.gguf 是**自带蒸馏**的 turbo 主模型，现在作为默认主模型。
它有两个坑，都已实测解决：

**① 文件缺元数据。** 这个 GGUF 的 metadata_kv_count 是 0（没有 general.architecture），
ComfyUI-GGUF 因此退回 detect_arch() 猜架构，猜不出直接抛
This model is not currently supported - (Unknown model architecture!)。
修法：往表头插一条 general.architecture = qwen_image（数据区整体后移 64 字节，张量 offset 不变）。
原始文件未改动，改的是 models\diffusion_models 里那份副本。

**② 反量化精度决定速度。** 同一文件、同 seed、1024²、9 步表：

| 加载器 / 精度 | 执行耗时 | 锐度 |
| --- | --- | --- |
| UnetLoaderGGUF（默认 dequant，fp32） | 82–155 s | 336.9 |
| UnetLoaderGGUFAdvanced(target) | **37.6 s** | 333.3 |
| UnetLoaderGGUFAdvanced(bfloat16) | 38.7 s | 333.3 |
| 对照：int8 底模 + turbo8 LoRA | 26.7 s | 140.5 |

所以插件默认 ggufLoader: advanced + ggufDequantDtype: target。
**别叠 turbo8 LoRA**：拿它去叠蒸馏模型会压暗压黑（暗部占比 0.2%→1.3%），
配置项 turboBakedModel: true 就是干这个的——保留 turbo9 采样，但跳过 LoRA 节点。

同时装好的配套资源（都在 models\ 下）：loras\Qwen-功能2.1\ 五个功能 LoRA
（扩图 / 万物移除 / 一致性 / 换头 / 换身）、LLM\ 两个 PE 提示词优化 GGUF + mmproj
（QwenImagePromptOptimizer 节点用它，尚需 llama-cpp-python 才能真跑）。

### 1.3.1 / 1.3.2 真机修复（2026-11-12 晚）

**① 局部重绘第二次必崩。** --gpu-only 的 ComfyUI 会把蒙版留在显存；同一张蒙版第二次使用时
LoadImageMask 命中缓存，下游 GrowMask 抛
can't convert cuda:0 device type tensor to numpy。现改为纯 torch 的 GrowMaskWithBlur
（外扩+羽化一体），备用链 MaskToImage → ImageBlur → ImageToMask，**绝不**再回 GrowMask。
test-inpaint.mjs 直接盯源码，防止有人把它加回来。

**② 三个辅助工具在叠 turbo LoRA。** 主模型已是蒸馏版（turboBakedModel: true）时，
inpaint_image / outpaint_image / character_image 仍在挂 turbo8 LoRA —— 双重蒸馏，
既压暗又慢。统一收敛到一个 turboBakedOrLora(cfg, workflow, loraName)，三处调用点共用。
实测同一张图同一蒙版：**120 s → 27 s**。

## 从上游 dsh-qwen-paint 移植（2026-11-12，0.18/0.19）

上游已到 0.19.2（我们 vendor 的是 0.17.13 + 大量本地补丁），没有整体替换，而是挑了三处
**我们确实缺的**移植过来：

| 来源 | 内容 | 为什么需要 |
| --- | --- | --- |
| 0.19.0 §3 | 参考图上传按序号加前缀 dshqp-ref-<序号>-<原名> | 上传用 overwrite=true + 文件名，
efs/1/ref.png 与 
efs/2/ref.png 会**静默**变成同一张 |
| 0.18.0 §1 | 主模型文件名带 turbo 就自动跳过 turbo8 LoRA | 我们原来是手工开 turboBakedModel，配置一丢就退回 25 步 / CFG 2.5（实测 126 s 且画面过冲） |
| 0.19.0 §1 | draw_image 多参考图 1–6 张（第 N 张 → images.image_N） | 换装 / 角色融合 / 多主体摆拍都需要；上游上限 16，我们取 6（再多编码器吃显存） |

用法：

\draw_image prompt="把图1的人物放进图2的场景，保持图1脸型与图2光照" references=["D:\a.png", "D:\b.png"]
\
判定统一收敛到 isTurboBakedModel(cfg, unetName)（配置 > 文件名兜底），
test-upstream.mjs 10 条回归盯着这三件事。

## 2026-11-12 优化批次（1.5.0：修 7 个真 bug + 一轮效率清理）

这一轮**不改采样链路、不改模型、不换节点**，只做三件事：把会**静默失败**的地方修好、
把**白干的活**去掉、把**重复 IO** 收敛。全部改动都有 `test-fixes.mjs` 的 16 条回归盯着。

### 修掉的 bug

| # | 症状 | 根因 | 修法 |
| --- | --- | --- | --- |
| 1 | 空闲关停后第一次**图生图**必失败（原生 `fetch failed`），而且不会自动拉起后端 | 只要传了 `reference` 就整段跳过探活（旧假设"要上传图说明后端在跑"）；而本套件默认 5 分钟就关后端 | `runDraw` 先用一次 `/queue` 判活，离线才 `ensureComfyUp`；图生图 / 多参考图 / ControlNet 全走同一条路 |
| 2 | **"空闲 5 分钟自动关停"从来没生效**（后端一直在线，`shutdowns:0`），显存白占 | 进程识别要求命令行同时含 `comfy` 与 `main.py`；但启动器用 `cwd + 相对路径 main.py` 拉起，命令行里**一个 comfy 都没有** | 身份判定改成"命令行含 `main.py`" **且**（含 `comfy` **或** 可执行文件 == 配置的 `comfyPython`）；端口监听 + `/system_stats` 已有两道前置闸，不会误杀 |
| 3 | 配置的 `outputDir` 不可写时，日志说"已退回默认目录"，但默认目录同样不可写 → 每次出图都在写盘那一步失败 | 兜底目标恒等于 `defaultOutputDir()`，等于没有第二选择 | 兜底链：配置目录 → 桌面默认 → `<DSH_HOME>/data/dsh-comfy-suite/output` → 系统临时目录，每个都做**真写测试**；原配置为什么不可用会如实回报 |
| 4 | `character_image` 的参考图同名时，后传的覆盖先传的 —— 提示词里的「图1/图2」指向同一张 | 上传没带序号前缀（`draw_image` 早就带了） | 统一成 `dshqp-ref-<序号>-<原名>`，并改成并发上传 |
| 5 | 日志/记忆里 `steps=undefined cfg=undefined`；turbo9 的步数一直没写进 `.qwen-paint-memory.jsonl` | turbo9 档把 KSampler 换成了 `ManualSigmas`，**节点 8 不存在**，旧代码却只从 `workflow[8]` 读步数 | 新增 `effectiveSampling()`：按节点类型读（KSampler 读 inputs；turbo9 用 sigma 个数 - 1） |
| 6 | 容量探测把"自带蒸馏"的主模型判成 `basic`，面板写"回退到 25 步 / CFG 2.5"，与实跑的 9 步 turbo9 **矛盾** | 档位只看"有没有 turbo8 LoRA"，没看 `isTurboBakedModel` | 探测阶段就认 `bakedTurbo`：档位记为 turbo（有 TE/Speedup 时 full），并写一条说明 |
| 7 | `comfyUrl` 配成非默认端口（如 8189）时，**自动拉起后端会等满 240 秒后报"没就绪"** | `ensureComfyUp` 的启动参数里**不带 `--port`**，ComfyUI 永远只听默认 8188；启动器那条路径却一直传 | 抽出纯函数 `buildComfyArgs()`：端口/监听地址从 `comfyUrl` 推、并剥掉手写参数里过期的 `--port/--listen` |

顺带修的文档/小项：`check_acceleration` 的 `action=repair` 与 `confirm` 补进工具描述；
7 处被误写成制表符的 `t`（`turboBakedModel`、`test-inpaint.mjs` …）修回。

### 效率（每条都能从代码里看出省了什么）

- **状态轮询 2 个请求 → 1 个**：`/system_stats` + `/queue` 合并成一次 `/queue`
  （`status.probeBusy()`）。面板每 5 秒轮询一次，约合每天少发 1.7 万个请求。
- **诊断/状态日志不再"读全文件 → 写全文件"**：`diag()` 改 append-only + 512 KB 轮转；
  状态日志从"每 5 秒重写 200 行"改成"状态变化或每 60 秒追加一行"。
  旧写法在默认路径下每分钟约 34 KB 写放大，而且落在**用户的出图目录**里。
- **调试日志移出出图目录**：`qwen-paint-diag.log` / `qwen-paint-status.log` 落到
  `<DSH_HOME>/data/dsh-comfy-suite/`，不再混进成品图。需要改位置用 `DSHQP_DIAG_FILE`。
- **作品库扫描**：图片尺寸（文件头）按 `mtime+size` 缓存、`stat`/读头改成 8 路并发；
  第二次打开面板不再对每张图重读 64 KB。出图日志的 JSON 解析同样按 `mtime+size` 缓存。
- **放大不白卸主模型**：`upscale_image` 以前一进门就 `/free` 卸主模型、再去探引擎 ——
  引擎缺失或图读不到时，6.5 GB 的主模型白卸一次，下次出图要重新加载。
  现在**先探引擎、先上传，最后才卸**（`test-fixes.mjs` 断言"引擎缺失时 `/free` 一次都不发"）。
- **一次多张不再逐张取图**：N 张改为并行 `/view` + 落盘（`Promise.all` 保序）。
- **首轮轮询立即查**：`waitForResult` 不再固定先睡 `pollIntervalMs`（默认 1.2 s）；
  同 prompt+seed 命中 ComfyUI 缓存时可以立即返回。
- **参考图不再读两遍**：扩图/重绘本来就要读整张图算尺寸，现在把字节直接交给上传函数。
- **`config.js` 拆出 `output-dir.js`**：改完兜底链之后它到了 261999 字节 —— 离 DSH STORE 的
  单文件 262144 上限只剩 **145 字节**，下一次改动必顶爆。把出图目录解析拆走后是 256608，
  留出约 5.4 KB 余量；`index.js`（255 KB）也接近上限，后续再加功能要同样先拆文件。

### 实测：为什么同一张 992² 有时 16 秒、有时 140 秒

这不是插件参数变了，是**硬件资源被挤**。同一次 ComfyUI 会话（日志 `user/comfyui_8188.log`）：

| 时间 | 尺寸 | 采样 | 每步 | 说明 |
| --- | --- | --- | --- | --- |
| 22:08 | 992² | 9 步 **16 s** | 1.86 s/it | 刚启动，CLIP + UNET 都在显存里 |
| 22:26 | 992² | 9 步 34 s | 3.84 s/it | 常驻后一般水平 |
| 22:37 | 992² | 9 步 **120 s** | 13.35 s/it | 同一台机器、同一模型，单步慢 7 倍 |

原因是测试机 **16 GB 显存要和桌面（dwm ≈2.1 GB）+ Edge GPU 进程（≈0.8 GB）分**，
系统内存也只有 16 GB：
- 16.3 GB 显存里 ComfyUI 实际能用约 13 GB，装不下 CLIP(6 GB) + UNET(6.5 GB) + 激活，
  于是每个 prompt 前都要卸掉 CLIP、再重载 UNET（日志里的 `Unloaded partially` / `loaded completely`，约 8–20 s）；
- 显存一紧，Windows 会把权重换页到系统内存/页面文件；GGUF Q6_K 每步都要读权重，
  单步就从 1.9 s 掉到 13 s。

**插件侧能做的**：已经做了（不重复卸模型、不重复探测、不重复读文件、轮询减半）。
**需要人做的**：出图时关掉占显存的程序（浏览器硬件加速、播放器、别的 AI 工具），
或把 `--reserve-vram` 调小给模型让位。这不是改代码能绕开的。

## 构建与测试

```bash
node scripts/build-client.mjs          # 从 client/_parts 重新拼 client.js
node scripts/build-client.mjs --check  # 产物是否与源一致（CI/装前用）
node test-host.mjs                     # 宿主：14 个工具、失败隔离、回执、设置写入
node test-gallery.mjs                  # 作品库/风格库：文件头、越界、检索、回收站
node test-wardrobe.mjs                 # 衣柜引擎：闸门/权重/复现/场景/裁剪
node test-sampling.mjs                 # 采样引擎：sigma 表/重采样/两种档位的节点形状
node test-outpaint.mjs                 # 扩图：留白计算/对齐/上限/尺寸读取
node test-library.mjs                  # GHIL 图库：索引/检索/id 解析/尺寸
node test-routes.mjs                   # 端点：列表/原图/收藏/重画/删除/同源守卫
node test-fixes.mjs                    # 2026-11-12 优化批次：兜底目录/日志轮转/缓存/单请求判活/首轮立即查/放大顺序
node test-comfyui.mjs                  # 宿主纯函数：校验错误渲染 / 预检 / 媒体判定 / 进度状态机
node test-launch.mjs                   # 零窗口启动：批处理编码/引号/环境变量、VBS 语义
node test-client.mjs                   # 客户端：私有模块表、五个 tab、组件物化、面板实时进度与介绍块
npm test                               # 以上全部 + 构建一致性
```

改 UI 的路径：改 `client/_parts/vendor_*/...`（或 `_head.js` / `suite_gallery.js` / `_tail.js`），再跑
`build-client.mjs`，最后热重载（往 `profiles/desktop/cordis.patch.yml` 末尾追加一行注释即可触发）。
不要再手拼 `client.js`。

`test-client.mjs` 会对**面板本身**做一次离线渲染（`window.__DSH_SUITE_UI__.comfyui.__internal`）：
实时进度条、运行中任务卡、任务行、插件介绍块各渲染一次并断言关键文案。改面板时先跑它——
它抓的是「渲染期就崩」那类错误，不需要开浏览器。

## 0.2.2-rc.1 适配（2026-11-06）

本包的外部依赖只有 `@deepseek-ai/schemastery` 与 `fflate`（都随包 vendored），**没有** import
任何宿主的 `@deepseek-ai/dsh-*` 包——这一点在 0.2.2 里变成了硬要求：profile 不再装宿主的那套
`@deepseek-ai/*`，link: 安装的插件按 Node 语义向上查找会 `MODULE_NOT_FOUND`。核对过的接口面：

| 用到的宿主接口 | 0.2.2 现状 |
| --- | --- |
| `ctx.tools.register(definition)` | 要求 `output { schema, render }`，参数即 JSON Schema；本包的 12 个工具全部满足 |
| `ctx.slots.inject/register` | `settings.section` / `tool.call.toolview` / `shell.overlay` / `conversation.session.header.actions` / `conversation.input.right` 均仍在 |
| `ctx.locale.register(ns, dict)` / `bind(ns)` | 签名未变 |
| `settings.update(entryId, patch)` | 0.2.2 多了可选的 `expectedRevision`，两参调用兼容 |
| `window.__ModuleLoader__.load({id, factory})` | 契约未变，单 row 注册仍然正确 |

新增声明：`engines.dsh = ">=0.2.1-rc.5 <0.3.0-0"`、`dsh.manifestVersion = 1`
（0.2.2 起启动和安装都会按 `semver.satisfies(..., {includePrerelease:true})` 校验）。
验证：`npm test`（宿主 11 工具 / 作品库 / 端点 / 启动 / 客户端 / 构建一致性）全绿。

## 启动行为（2026-11-05 修订）

- **零窗口启动**：Windows 上由 `wscript.exe`（GUI 子系统，自身没有控制台）执行
  `.dshqp-hidden.vbs`，再以 `SW_HIDE` 拉起 `.dshqp-launch.cmd` → python。
  控制台从创建那一刻就是隐藏的，桌面上不会再出现 `DSHQP-ComfyUI`，任务栏也
  没有条目；不再依赖"先弹窗、再最小化"的两套补丁。实现见 `lib/hidden-launch.js`。
  批处理以 CRLF + UTF-8 写入、首行 `chcp 65001`，安装路径带中文/空格也能跑。
  极端情况下（组策略禁用 wscript.exe）自动退回旧的 cmd + 事后隐藏方案：
  会闪一下窗口，但**不会起不来**。
- **DSH 启动预热（默认开启，延迟 10 秒）**：宿主起来 10 秒后在后台把后端拉起
  （`qwenPaint.warmupDelayMs`），等真正要画时通常已经就绪，不用再等约 45 秒冷启动。
  2026-11-04 曾因"预热会弹 DSHQP 窗口"关掉它；零窗口之后恢复。
  不想预热：`qwenPaint.warmupOnStart: false`。
- **后端不随 DSH 退出**：ComfyUI 由 WMI 派生，进程树不在 DSH 的作业对象里；
  DSH 重启/升级不会带走它。下次宿主启动直接探到在线 —— 这是"启动快"的关键。
  测试机冷启动约 45 秒：torch/ROCm 初始化约 27 秒 + 自定义节点约 10 秒 +
  ComfyUI-Manager 预启动约 7 秒。
- 启动日志与脚本都在 ComfyUI 安装目录：`.dshqp-launch.log`、
  `.dshqp-launch.cmd`、`.dshqp-hidden.vbs`。
- `qwen-paint` 在 5 分钟无出图时自动关停（`idleShutdownMs`，可在界面里改），
  关停后进程与日志句柄一起释放。
- 就绪检测轮询为 1 秒（原 3 秒），端口一通最多 1 秒内就显示"在线"。

## 已知限制

- **锁死在上游当前版本**：不再跟这三个插件的上游更新，
  上游修 bug 需要手动重放，或重新 vendor 这三份代码。
- 客户端是拼接产物，没有 sourcemap（有可复现构建脚本，但仍是几份 bundle 的拼接）。
- 合并后 `dsh-comfyui` 的收编副本多了三处补丁：`lib/index.js` 顶部 import
  `suiteBridge`、`runtime.updateConfig` 走 bridge、`lib/tools.js` 逐个注册工具并上报
  结果；`client/client.js` 是合并产物。其余字节与原包一致（`diff -r` 可复核）。
- `draw_image` 与 `comfyui_server` 各自都有启动/关停 ComfyUI 的代码路径：前者按需
  拉起、空闲 5 分钟关停；后者是手动启停。2026-11-05 起两者都走
  `lib/hidden-launch.js`（零窗口、脱离宿主），但仍是两套参数/状态机：同开时以后端
  实际在跑的那一份为准（先启动者赢）。彻底收敛成一个 supervisor 是后续工作。
- **作品库靠扫目录**，因此：文件名不是本插件起的图（手动丢进目录的）没有提示词；
  `_` 开头的文件（如 `_正在生成图片.webp`）和隐藏文件会被跳过；超过 3 层子目录不扫；
  超过 4000 张只取前 4000。这批限制是刻意的 —— 面板要能秒开，就不能在渲染路径上遍历整个磁盘。
- 作品库的"再画一张"依赖**那条出图日志**。日志被清理、或图不是本插件生成的，
  按钮会明确告诉你"无法复现参数"，而不是用错的参数硬画一张。
- 回收站不会自动清理。`$DSH_HOME/data/dsh-comfy-suite/trash/` 攒多了要自己删。
- **实时进度依赖 ComfyUI 的 WebSocket**（`/ws?clientId=…`）。事件是**按提交它的
  client 广播**的，所以：① 别人在 ComfyUI 网页里跑的任务，插件这边看不到步数
  （队列深度能看）；② 需要在认证代理后面的远程 ComfyUI 上，Node 的 `WebSocket`
  没法带 Authorization 头，进度通道连不上 —— 这时标题栏会明确写「进度通道未连接」，
  生成、结果与资产索引都不受影响，只是没有实时数字。
- 进度百分比是**当前节点**的步数进度，不是整张工作流的加权进度：多采样器的工作流
  里，第二个采样器开始时百分比会从头再走一遍（`.dsc-progress-fill` 是节点内进度）。
  ETA 用的是**采样步速**（第一步之后的实测速度），所以模型加载那 2–3 分钟不计入；
  这也意味着刚起步时（<2 步）只显示「已用」，不瞎猜剩余。