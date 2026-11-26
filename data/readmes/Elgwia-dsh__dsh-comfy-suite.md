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
> **只想用其中一个功能，就直接装上游**，不要装这个整合包。本包定位是「合并 + 修复 + 本地增强」，
> vendor 代码锁定 2026-11-13 快照，不承诺跟进上游更新。第三方许可与逐条修改见
> [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。

把 ComfyUI 接进 DSH：**14 个工具**管工作流、出图、修图、捏人、放大与服务启停，
**一个设置页**管配置与素材，**标题栏一条实时进度条**告诉你这一步跑到哪、还剩多久。

**更新记录不在本文档**：版本变化、修掉的 bug、回归测试都在 [CHANGELOG.md](CHANGELOG.md)。

---

## 效果图

下面每一张都是**这个插件在测试机上实际生成/处理的结果**，不是示意图；参数与种子写在图注里，
可以照着复现。测试机：RX 9060 XT 16 GB，ComfyUI 0.42.3，Qwen-Image 2.1 int8_convrot，原生 25 步链路。

### 文生图

`draw_image` 走本机 ComfyUI：主模型、步数、CFG、画幅、参考图全部由配置与参数决定。

![雨夜街头，穿米色风衣的女性双手插兜回望](docs/images/hero-street-night.jpg)

*16:9 · 1472×832 · 25 步 / CFG 3 · seed 20261131 ·「雨夜的城市街头，湿润的柏油路面倒映着红蓝霓虹招牌……」*

| 影棚人像 | 风光 |
| :---: | :---: |
| ![影棚半身人像，米白高领毛衣，伦勃朗光](docs/images/portrait-studio.jpg) | ![清晨薄雾中的江南水乡，白墙黛瓦与石拱桥](docs/images/scene-jiangnan.jpg) |
| 3:4 · 960×1280 · seed 20261129 | 4:3 · 1280×960 · seed 20261127 |

**100% 裁切（520×520，不缩放）** —— 皮肤、发丝、耳环这些细节是原图就有的，不是放大补的：

![人像面部 100% 细节裁切](docs/images/detail-crop.jpg)

### 提示词衣柜

`prompt_wardrobe` 按档位收窄候选池、按三层权重抽一整段 prompt（同 seed 逐字可复现），
再交给 `draw_image`。这张用的是 `level=0`、`scene=sc-autumn-street`、`seed=20261125` 抽出的那段：

![秋日人行道，穿风衣行走的女性，暖金色逆光](docs/images/wardrobe-autumn.jpg)

*3:4 · 960×1280 · 衣柜抽题 + `draw_image` 出图*

### 捏人 / 换装

`character_image` 直接从 GHIL 素材库挑「人像 + 服装」（可再加发型、姿势），
拼成多参考图送进 GH 编码器。这张是 `portrait=f71f980dde3` + `costume=SPR-0005`：

![影棚全身像，短发女性穿米色碎花连衣裙](docs/images/character-ghil.jpg)

*3:4 · 960×1280 · GHIL 人像 + 春装连衣裙*

### 局部重绘

`inpaint_image` 只重画蒙版区域，蒙版外**逐像素保持原样**。这张把天空换成傍晚（蒙版由脚本按天空亮度和
饱和度自动生成，不是手画）：

| 原图 | 蒙版区重绘后 |
| :---: | :---: |
| ![清晨的水乡原图](docs/images/inpaint-before.jpg) | ![同一条河，天空换成橙粉色晚霞](docs/images/inpaint-after.jpg) |
| 1280×960 | 同尺寸 · `denoise 1.0` · `feather 28` · 指令「傍晚的天空，柔和的橙粉色晚霞……」 |

### 扩图

`outpaint_image` 原图像素一个不动，只往画面外补。这张把 3:4 的影棚人像扩成宽幅：

| 原图（3:4） | 扩图后 |
| :---: | :---: |
| ![影棚人像 3:4](docs/images/portrait-studio.jpg) | ![同一张人像的宽幅版本，两侧补出影棚背景](docs/images/outpaint-after.jpg) |
| 960×1280 | `aspect=16:9` → 2048×1280（成图上限 `maxEdge 2048`，宽度收敛）· `feather 96` |

---

## 界面

插件在 DSH 里只有一个设置入口：**设置 → ComfyUI 套件**，下面五个标签页；
生成时标题栏还有一条常驻状态条。

| 位置 | 内容 |
| --- | --- |
| **标题栏状态条** | `正在生成 · 工作流名 · 3/9 步 · 约 42s 后完成 · 队列 1`；空闲显示「空闲」，进度通道没连上时写「进度通道未连接」。右侧百分比 + 3px 进度条，第一步之前走不确定态动画 |
| **ComfyUI 面板**（标题栏按钮） | 工作流库 / 资产 / 队列三页。ComfyUI 没启动时面板照常打开，顶部给一条「ComfyUI 未启动」横幅 + 「启动服务」「重新检测」两个按钮，不在页面顶部弹通栏报错 |
| **工作流与生成** | ComfyUI 地址与鉴权、工作流目录、加载区槽位、主模型与采样档位、出图目录、空闲关停 |
| **作品库** | 扫描出图目录得到的图库：搜索（提示词/文件名/种子）、收藏、时间排序、看大图与参数、复制提示词/路径、换种子再画 / 同种子复现、删除进回收站 |
| **风格库** | 62 条提示词积木（画风 / 光效 / 构图 / 画质 / 负面词 / 海报版式），可检索、勾选、拼成整句 |
| **提示词衣柜** | 档位、模式、主体、场景、种子 → 抽一整段 prompt，带自检报告，可复制或直接出图 |
| **服务启停** | ComfyUI 启停、端口、日志尾部；零窗口启动，不弹控制台 |

---

## 工具一览

模型侧一共 **14 个工具**，`boot.log` 里的 `tools audit` 行会逐次核对：

| 工具 | 做什么 |
| --- | --- |
| `draw_image` | 文生图 / 图生图。画幅 7 档，可给 1–6 张参考图（「图1/图2…」），可选 ControlNet |
| `inpaint_image` | 局部重绘：给图 + 蒙版 + 一句编辑指令，蒙版外严格保持原样 |
| `outpaint_image` | 扩图：按目标画幅或四边比例往外补，原图像素不动 |
| `character_image` | 捏人 / 换装：从 GHIL 素材库挑人像 + 服装（+ 发型 + 姿势）生成 |
| `upscale_image` | 放大 / 超分：VOSR2 分块放大（2–16 倍），可切 RealESRGAN |
| `list_available_models` | 列出本机 ComfyUI 的 UNET / CLIP / VAE / LoRA / Checkpoint 文件 |
| `check_acceleration` | 检查 GPU 与加速环境，安装/修复加速包 |
| `image_presets` | 风格库检索/取详情/拼句（`search` / `get` / `compose` / `kinds`） |
| `prompt_wardrobe` | 提示词衣柜：按档位随机组合一整段 prompt（`roll` / `scenes` / `meta`） |
| `comfyui_workflow` | 工作流库：列、跑、看、刷新参数、提取图工作流、上传素材 |
| `comfyui_skill` | 工作流技能包：读/写 SKILL.md 与引用文件 |
| `comfyui_object_info` | 查当前 ComfyUI 支持的节点定义与可选模型文件名 |
| `comfyui_run` | 直接提交手写的 API 工作流（调试用） |
| `comfyui_server` | ComfyUI 服务启停、状态、日志 |

---

## 安装

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

`cordis.patch.yml` 三块路径默认是占位的 `D:/ComfyUI` 布局，
**换成你自己的 ComfyUI 安装目录**，否则启停与出图都会找不到文件：

| 配置块 | 字段 | 指向 |
| --- | --- | --- |
| `comfyui` | `comfyuiDirs` / `outputDir` | ComfyUI 根目录与其 `output/` |
| `launcher` | `comfyuiDir` / `pythonPath` | ComfyUI 根目录与它自带的 python |
| `qwenPaint` | `comfyPython` / `comfyMainPy` / `comfyWorkdir` | Python、`main.py`、工作目录 |

主模型默认是 `qwen_image_2.1_int8_convrot.safetensors`（**完整版，非蒸馏**），
要跟你的 `models/` 里的文件名一致；换模型就改 `qwenPaint.unet`。
加载器按扩展名自动选：`.safetensors` → 原生 `UNETLoader`，`.gguf` → `UnetLoaderGGUF*`。

> 换模型时**必须同步改** `turboBakedModel` / `turbo8Enabled`，否则插件会继续按
> 9 步 / CFG 1 的蒸馏工作点跑完整版（欠采样，画面发糊）。详见「主模型与工作点」。

### 自带依赖

`node_modules/` 里 vendored 了三份东西，所以 **link 安装和物理复制都能解析**：

- `@deepseek-ai/schemastery`（配置 schema）+ 它缺的运行时依赖 `@deepseek-ai/cosmokit`
- `fflate`（`vendor/comfyui/lib/transfer.js` 用它解压上传）

旧版只 vendored 了 schemastery，是从 link 形态（Node 保留 profile 前缀解析）跑通的；
一旦按 `install.sh` 物理复制，`import '@deepseek-ai/cosmokit'` 立刻报
`Cannot find package`——本包现在不靠宿主 flag，两种形态实测都能 `import()`。

---

## 用法

### 出图与修图

```
draw_image prompt="雨后霓虹街头，穿风衣的女性回头" size=16:9 seed=42
draw_image prompt="把图1的人物放进图2的场景，保持图1脸型与图2光照" references=["D:\\a.png", "D:\\b.png"]
inpaint_image image=D:\\a.png mask=D:\\m.png prompt="把帽子换成红色针织帽"
outpaint_image image=D:\\a.png aspect=16:9
outpaint_image image=D:\\a.png sides={"right":0.5,"top":256}
character_image portrait=f71f980dde3 costume=SPR-0001 size=3:4
upscale_image image=D:\\a.png scale=4
```

- 画幅：`1:1 / 3:4 / 4:3 / 2:3 / 3:2 / 16:9 / 9:16`，`megapixels` 控总像素。
- `steps` / `negative` 的说明按**当前配置**生成：原生链路（CFG 3）里两者都真正生效；
  turbo 8 步蒸馏链路里 `steps` 会被忽略、`negative` 基本无效。
- 参考图三种写法都认：`draw_image` 的 `references` 路径数组；`character_image` 的纯 id
  （按参数名推类型）、`ghil:人像/<id>`、本地绝对路径。

### 工作流

```
comfyui_workflow action=list
comfyui_workflow action=run id=<workflow> parameters={"prompt": "…"}
comfyui_object_info filter=KSampler
comfyui_server status / start / stop / logs
```

- 「运行主题」是 API 工作流，「衍生主题」是 ComfyUI 端保存的画布；画布要先「提取」成
  API 工作流才能跑（面板里按分量提取，或 `action=extract`）。
- 工作流列表带 `filter` 时会同时报「全库 N 个，命中 M 个」，并按顶层目录聚合；
  目录一多就用 `filter: "目录名"` 收窄，比加大 `limit` 省 token。

### 服务启停

- `comfyui_server` 手动启停；`draw_image` 等工具需要时会自动拉起，空闲 5 分钟自动关停
  （`qwenPaint.idleShutdownMs`，可在界面里改）。
- 端口不可用时（Windows `WinError 10013` 系统保留、`10048` 被占用）启动前会先真的 bind 一次，
  能给出原因并在激活时把三块配置对齐到同一个可用端口；换端口只影响运行期，不写回配置。
- 启动是零窗口的（`wscript.exe` + `SW_HIDE`），日志与脚本落在 ComfyUI 安装目录：
  `.dshqp-launch.log`、`.dshqp-launch.cmd`、`.dshqp-hidden.vbs`。

---

## 主模型与工作点

同一 prompt、同一 seed（20261124）、同一尺寸 1024×1376，只换模型 / 加载路径 / 工作点：

| 主模型 | 加载器 | 采样 | 平坦区噪声 | 暗部噪声 | 细节能量 | 耗时 |
| --- | --- | --- | --- | --- | --- | --- |
| `Qwen-Image-2.1-Turbo-AD-Q6_K.gguf` | UnetLoaderGGUFAdvanced(target) | 9 步表 / CFG 1 | 1.127 | 3.159 | 207.0 | 109.8 s |
| `qwen_image_2.1_turbo_int8_convrot` | UNETLoader | 9 步表 / CFG 1 | 1.116 | 3.108 | 202.8 | **26.2 s** |
| `qwen_image_2.1_int8_convrot`（完整版） | UNETLoader | 25 步 / CFG 3 | **0.957** | **1.946** | 136.5 | 94.7 s |

（噪声 = 归一化到 1024 宽后、平坦区/暗部的亮度高频标准差，越低越干净；
细节能量 = 拉普拉斯方差，太低说明被磨平。）

三条结论：

1. **量化格式只影响速度，不影响画质。** GGUF Q6_K 与 int8_convrot 的指标几乎相同
   （1.127 vs 1.116），但 int8_convrot 走 ROCm 原生 convrot 内核，**快约 4 倍**（26 s vs 110 s）。
   GGUF 只能 torch 现场反量化，是纯损耗 —— 能用 safetensors 就别用 GGUF。
2. **蒸馏模型不能加步数。** 同一个 turbo 主模型按 25 步跑时，暗部噪声反而从 3.11 涨到
   4.49（+44%）—— 蒸馏工作点固定在 8~9 步，多跑只是把细节反复叠成砂。
3. **完整版更干净，但要用纹理换。** 换成非蒸馏完整版 + 25 步 + CFG 3：暗部噪声降 37%、
   平坦区降 15%，代价是细节能量掉 33%（皮肤更平、发丝更软）。

当前默认取完整版（干净优先）。配置：

```yaml
qwenPaint:
  unet: 'qwen_image_2.1_int8_convrot.safetensors'
  turboBakedModel: false
  turbo8Enabled: false     # 必须显式关：level 探测成 full 时插件仍会判「turbo 可用」，
                           # 那样完整版会被按 9 步 / CFG 1 跑（实测明显欠采样）
  baseSteps: 25
  baseCfg: 3               # 官方推荐 2.5~4，实测 3.0 比默认 2.5 更稳
  steps: 25
  forceTurbo8Steps: false
```

想换回蒸馏快档：unet 指回 `qwen_image_2.1_turbo_int8_convrot.safetensors`，
`turboBakedModel` / `turbo8Enabled` 置 true，采样会自动回到 9 步表 / CFG 1。

> ⚠ 改完这些配置**必须重启 DSH**。`qwen-paint` 的 cfg 在 `apply()` 时合并并被工具闭包捕获，
> 改 patch 文件不会热重建 —— 实测等两轮热重载（40 s）仍是旧值，只有重启宿主才生效。
> 症状：`draw_image` 报 `unet_name ... not in []`（拿旧文件名去问一个已经不存在的加载器）。

---

## 结构

```
dsh-comfy-suite/
  package.json            dsh.bundle.patch + dsh.client + scripts
  cordis.patch.yml        唯一的条目与三块配置（comfyui / launcher / qwenPaint）
  README.md               本文件：插件说明与效果图
  CHANGELOG.md            更新记录（版本变化 / 修掉的 bug / 回归测试）
  LICENSE                 MIT
  THIRD-PARTY-NOTICES.md  三个上游的许可与逐条修改
  docs/images/            README 用的样张与界面截图
  lib/
    index.js              聚合宿主：挂三个子插件、转发配置写入、写启动回执
    config.js             嵌套 schema（comfyui 用原 schema，另两块透传）
    bridge.js             子插件 ↔ 条目的配置写入 / 刷新 / 回执通道
    hidden-launch.js      ComfyUI 的零窗口 + 脱离宿主启动（wscript/SW_HIDE）
    ports.js              ComfyUI 端口体检、换端口与失败归因（10013 / 10048）
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
  test-wardrobe.mjs       衣柜引擎单元测试（闸门 / 权重 / 复现 / 场景 / 裁剪）
  test-sampling.mjs       采样引擎回归（9 步 sigma 表 / 重采样 / 两种档位的节点形状）
  test-outpaint.mjs       扩图回归（留白计算 / 8 对齐 / 上限收敛 / 尺寸读取）
  test-library.mjs        GHIL 图库回归（索引 / 检索 / id 解析 / 尺寸 / 默认提示词）
  test-inpaint.mjs        局部重绘回归（蒙版链、绝不回 GrowMask）
  test-upstream.mjs       上游移植回归（多参考图前缀、turbo 判定）
  test-fixes.mjs          兜底目录 / 日志轮转 / 缓存 / 单请求判活 / 放大顺序
  test-routes.mjs         端点集成测试（真喂请求，含同源/方法/类型守卫）
  test-client.mjs         客户端冒烟测试（私有模块表、五个 tab、面板实时进度渲染）
  test-comfyui.mjs        宿主纯函数测试（校验错误渲染、预检、媒体判定、进度状态机）
  test-launch.mjs         零窗口启动与端口预检回归
  install.sh              安装 / 重装（默认 link）
  rollback.sh             恢复最近一次 package.json / cordis.patch.yml 备份
  node_modules/           自带的 schemastery + cosmokit + fflate（见上）
```

> 发布仓另有 `market/`（自托管插件索引），不属于插件包本身。

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

---

## 作品库与风格库

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

---

## 提示词衣柜

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

---

## 9 步采样与扩图

采样引擎来自一套 9 步整合画布（154 节点 / 5 个独立流程）。**移植的是做法，不是它的连线**：
那张画布依赖 `孤海`/`GH`/`Goohai` 三个第三方节点包和 5 个 LoRA（`Qwen-功能2.1/*`），
测试机都没有；这里只用 ComfyUI 自带节点 + 已有模型，把五个流程的**工作点**搬过来。

### 采样：把 `scheduler:simple` 换成显式 sigma 表

画布 5 个流程都用同一套：`ManualSigmas` + `SamplerCustomAdvanced` + `KSamplerSelect(euler)` +
`CFGGuider(cfg=1)`（扩图/移除两支用 `BasicGuider`，cfg=1 时两者出图逐像素一致）。表长这样：

```
1.0, 0.978453, 0.954180, 0.926626, 0.895080, 0.845148, 0.704534, 0.414568, 0.150000, 0
```

它不是"随便一串数"：`simple` 调度器是按 sigma 分布现场推导的通用调度，而这串数是
**针对 turbo 蒸馏模型调过的步序**（前 5 步几乎等高、后半段陡降）。测试机实测（1024²，同 seed）：

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
`plan.useTurbo === false` 时这个开关整个被忽略，直接走原生链路（`baseSteps` / `baseCfg`）。
当前默认是原生链路：主模型为完整版 int8_convrot，CFG 3（见「主模型与工作点」）。

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
outpaint_image image=D:\\a.png aspect=16:9
outpaint_image image=D:\\a.png expand=0.25
outpaint_image image=D:\\a.png sides={"right":0.5,"top":256}
outpaint_image image=D:\\b.png aspect=3:4 prompt="上边补出天空与屋檐，延续原有透视"
```

- `aspect` 按目标画幅算（方图 → 16:9 只补左右；→ 3:4 只补上下）。
- `expand`/`sides`：**≤4 当比例**（0.25 = 各边 25%），**>4 当像素**（256 = 各边 256 px）。
- 四边一律**对齐 8 的倍数**（潜空间 1/8 分辨率，不对齐会留半格毛边）。
- **羽化默认 96 px**，不是拍脑袋定的：同图同种子，量"接缝处相邻列的差分 / 全图中位数"
  —— 0 px（硬边）7.8 倍、48 px 4.4 倍、**96 px 2.5 倍**（与"本来就没有接缝"的那张参考图同档）。
  羽化会自动收敛到「最小留白的一半」，小图不会被过渡带吃光留白。
- 成图上限 = `max(maxEdge=2048, 原图 1.5 倍)`，超了**只收敛留白**（原图不缩），并回报 `clamped`。
  所以 3:4 扩到 `16:9` 时，宽会收敛到 2048（结果 2048×1280），不是严格的 1.777 比例。
- **画布超过 1.15 MP 自动把步数加到 16**：1024² → 1024×1360 竖扩实测，新增区锐度
  9 步 57.9 / 12 步 70.8 / **16 步 90.9**（拉普拉斯方差；原图那一带三次都是 39.4，说明被保护的
  像素一个没动），用时只多约 10%。不做这一步，扩出来的边会明显发软、像蒙了层薄雾。
- 读尺寸支持 PNG / JPEG / WebP；读不出来就报错，不猜（猜错 = 扩歪）。

真机验证：1024² → 1824×1024（左右各 400 px），46 s（新尺寸首次要重载模型），
接缝不可见、光线与景深延续，中心区域逐像素保留。

---

## 捏人 / 换装：`character_image`

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
character_image portrait="ghil:人像/f71f980dde3" costume="D:\\assets\\外套.jpg" prompt="..."
```

- 参考图三种写法都认：纯 id（按参数名推类型）、`ghil:人像/<id>`、本地绝对路径。
- 图库根目录 `qwenPaint.ghilRoot`，留空则从 `comfyMainPy` 推 `<ComfyUI>/models/GHIL`。
- 提示词不填就自动拼一句（影棚全身像 + 逐条点名"保持图N的面部特征/穿上图N的服装"）。

**实测**（测试机 RX 9060 XT，864×1152，两张参考图，turbo9 采样）：

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

---

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
tools audit: 14/14 present
```

出问题时就多了能直接定位的行：

| 回执行 | 含义 |
| --- | --- |
| `xxx: apply still pending after 15000ms` | 子插件 `apply()` 卡住，工具不会注册 |
| `xxx: apply rejected … — <msg> @<frame>` | 子插件初始化抛错，附第一处插件代码栈帧 |
| `comfyui: tools 3/4, failed — comfyui_workflow: duplicate …` | 单个工具注册失败，其余照常 |
| `tools audit: 13/14 — MISSING comfyui_workflow` | 模型侧真的少了一个工具 |
| `ports: 8188 → 8189 — …` | 端口被系统保留/占用，激活时换到了下一个能绑的端口 |

**为什么加这些**：合并后出现过一次「界面正常、`draw_image` 正常，但 4 个
`comfyui_*` 工具从模型工具表里消失」。原因是合并窗口里新旧插件可能同时注册同名工具，
一个 `register()` 抛错就把整批工具带走，而当时的回执只写了 `children mounted`，
没有任何地方能看出少了什么。现在：四个工具逐个注册、互不连坐，失败原因和
`tools audit` 都落盘；`test-host.mjs` 里有对应的回归用例。

---

## 构建与测试

```bash
node scripts/build-client.mjs          # 从 client/_parts 重新拼 client.js
node scripts/build-client.mjs --check  # 产物是否与源一致（CI/装前用）
npm test                               # 下面全部 + 构建一致性
```

| 测试 | 盯什么 |
| --- | --- |
| `test-host.mjs` | 宿主：14 个工具、失败隔离、回执、设置写入 |
| `test-gallery.mjs` | 作品库/风格库：文件头解析、越界、检索、回收站 |
| `test-wardrobe.mjs` | 衣柜引擎：闸门 / 权重 / 复现 / 场景 / 裁剪 |
| `test-sampling.mjs` | 采样引擎：sigma 表 / 重采样 / 两种档位的节点形状 / 参数说明按配置生成 |
| `test-outpaint.mjs` | 扩图：留白计算 / 8 对齐 / 上限收敛 / 尺寸读取 |
| `test-library.mjs` | GHIL 图库：索引 / 检索 / id 解析 / 尺寸 |
| `test-inpaint.mjs` | 局部重绘：蒙版链，绝不再回 `GrowMask` |
| `test-upstream.mjs` | 上游移植：参考图序号前缀 / turbo 判定 |
| `test-fixes.mjs` | 兜底目录 / 日志轮转 / 缓存 / 单请求判活 / 放大顺序 |
| `test-routes.mjs` | 端点：列表 / 原图 / 收藏 / 重画 / 删除 / 同源守卫 |
| `test-client.mjs` | 客户端：私有模块表、五个 tab、组件物化、面板实时进度与介绍块 |
| `test-comfyui.mjs` | 宿主纯函数：校验错误渲染 / 预检 / 媒体判定 / 进度状态机 |
| `test-launch.mjs` | 零窗口启动：批处理编码 / 引号 / 环境变量、VBS 语义、端口预检 |

改 UI 的路径：改 `client/_parts/vendor_*/...`（或 `_head.js` / `suite_gallery.js` / `_tail.js`），再跑
`build-client.mjs`，最后热重载（往 `profiles/desktop/cordis.patch.yml` 末尾追加一行注释即可触发）。
不要再手拼 `client.js`。

`test-client.mjs` 会对**面板本身**做一次离线渲染（`window.__DSH_SUITE_UI__.comfyui.__internal`）：
实时进度条、运行中任务卡、任务行、插件介绍块各渲染一次并断言关键文案。改面板时先跑它——
它抓的是「渲染期就崩」那类错误，不需要开浏览器。

---

## 启动行为

- **零窗口启动**：Windows 上由 `wscript.exe`（GUI 子系统，自身没有控制台）执行
  `.dshqp-hidden.vbs`，再以 `SW_HIDE` 拉起 `.dshqp-launch.cmd` → python。
  控制台从创建那一刻就是隐藏的，桌面上不会再出现 `DSHQP-ComfyUI`，任务栏也
  没有条目；不再依赖"先弹窗、再最小化"的两套补丁。实现见 `lib/hidden-launch.js`。
  批处理以 CRLF + UTF-8 写入、首行 `chcp 65001`，安装路径带中文/空格也能跑。
  极端情况下（组策略禁用 wscript.exe）自动退回旧的 cmd + 事后隐藏方案：
  会闪一下窗口，但**不会起不来**。
- **DSH 启动预热（默认开启，延迟 10 秒）**：宿主起来 10 秒后在后台把后端拉起
  （`qwenPaint.warmupDelayMs`），等真正要画时通常已经就绪，不用再等约 45 秒冷启动。
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

---

## 已知限制

- **锁死在上游当前版本**：不再跟这三个插件的上游更新，
  上游修 bug 需要手动重放，或重新 vendor 这三份代码。
- 客户端是拼接产物，没有 sourcemap（有可复现构建脚本，但仍是几份 bundle 的拼接）。
- 合并后 `dsh-comfyui` 的收编副本多了三处补丁：`lib/index.js` 顶部 import
  `suiteBridge`、`runtime.updateConfig` 走 bridge、`lib/tools.js` 逐个注册工具并上报
  结果；`client/client.js` 是合并产物。其余字节与原包一致（`diff -r` 可复核）。
- `draw_image` 与 `comfyui_server` 各自都有启动/关停 ComfyUI 的代码路径：前者按需
  拉起、空闲 5 分钟关停；后者是手动启停。两者都走 `lib/hidden-launch.js`
  （零窗口、脱离宿主），但仍是两套参数/状态机：同开时以后端实际在跑的那一份为准
  （先启动者赢）。彻底收敛成一个 supervisor 是后续工作。
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
- **扩图受 `maxEdge` 约束**：成图长边上限 2048（或原图 1.5 倍），超出时只收敛留白、
  不缩原图，所以 3:4 扩 16:9 的结果会是 2048×1280 而不是严格的 16:9。

---

## 许可

MIT，见 [LICENSE](LICENSE)。三个上游的许可与逐条修改见
[THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。

- [dsh-comfyui](https://github.com/fandc520/dsh-comfyui)（MIT）
- [dsh-qwen-paint](https://github.com/yanfei0725/dsh-qwen-paint)（MIT，原作者
  [@奇迹与你](https://github.com/wonderandyou)）
- `dsh-comfyui-launcher`（本仓库作者自建，随本包 MIT 发布）

更新记录：[CHANGELOG.md](CHANGELOG.md)。