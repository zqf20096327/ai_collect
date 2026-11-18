# comfyui-dsh — 本地生图，ComfyUI + DeepSeek Harness

[![DSH target](https://img.shields.io/badge/DeepSeek%20Harness-0.2.2--rc.3-4f46e5)](docs/COMPATIBILITY.md)
[![version](https://img.shields.io/badge/version-1.4.1-16a34a)](https://github.com/devin667/comfyui-dsh/releases/tag/v1.4.1)
[![checkpoints](https://img.shields.io/badge/checkpoints-4-0ea5e9)](docs/MODELS.md)
[![workflows](https://img.shields.io/badge/workflows-15-8b5cf6)](dsh/workflows)
[![license](https://img.shields.io/badge/license-MIT-a3a3a3)](LICENSE)
[![platform](https://img.shields.io/badge/platform-Windows%20%2F%20RTX%2050-f97316)](docs/COMPATIBILITY.md)

中文 · [English](README.en.md) · [变更日志](CHANGELOG.md) · [适配说明](docs/COMPATIBILITY.md) · [保脸换装](docs/IPADAPTER.md)

![banner](docs/banner.svg)

---

## 中文

ComfyUI 跑在本机 8188，DSH 的 `dsh-image-gen` 插件通过 HTTP 调它。生成链路全程不出本机，
产出落在自己硬盘上，可换底模、可拖 denoise、可一句话切模型。

一个 8 GB 的 RTX 5060 Laptop 上实测：SDXL 832×1216 热态 **26–33 秒**，HiRes 1.5× 58 秒。

### 四个底模，一张图看清差别

![四底模同场景对比](docs/preview/checkpoints-4way.jpg)

同一段 prompt（`RAW photo, amateur snapshot taken on iPhone, woman in a cluttered
kitchen making coffee, morning backlight, unedited`）、同一场景：

| 底模 | 体积 | 热态单图 | 定位 |
|---|---|---|---|
| **RealVisXL V5.0 fp16** | 6.5 GB | **26–31 s** | 写实默认档。纪实/生活感最准 |
| Juggernaut XI v11 | 6.6 GB | 24–30 s | 商业/电影感，手部结构更稳，但过度精致 |
| Illustrious-XL v1.1 | 6.5 GB | 26–33 s | 二次元插画。左上那张是用写实 prompt 强扭的结果 |
| FLUX.1 Krea dev Q2_K | 3.7 GB | 82 s | 场景理解最强，慢 3–4 倍，皮肤有量化色斑 |

六场景对拍、FLUX 四档量化的实测数据、提示词四风格、参数甜点，见
**[docs/MODELS.md](docs/MODELS.md)**。

### 白净皮肤

默认负向里那串 `freckles, moles, birthmark, blemishes, skin spots, acne, large pores...`
不是装饰。写实模型出的图满脸雀斑，八成是因为提示词里写了 `freckles` 这个词。

![白净皮肤](docs/preview/clean-skin.jpg)

### 图内文字，别指望

同一段 prompt，三家写法各不相同：

![图内文字对比](docs/preview/text-rendering.jpg)

`KRA COFFEE` / `KREA. COFFEE` / `KIRE A`。要准确文字请后期加。

### 锁住同一个人

![IPAdapter FaceID 真人换装](docs/preview/ipadapter-faceid-real.jpg)

同一张真人参考照，四套衣服四个场景，脸不动。走的是 IPAdapter **FaceID PLUS V2**：
insightface 先算 512 维身份向量，只把向量送进 cross-attention，所以换装不会跟衣服打架、
背景色调也不会渗。

别用 `PLUS (high strength)`——它把整图特征一起灌进去，在 Illustrious 上还会出横向彩虹条。
两种 preset 的差别、参数甜点、五个坑见 **[docs/IPADAPTER.md](docs/IPADAPTER.md)**。

### Denoise 滑杆

![滑杆页](docs/preview/slider.jpg)

`启动Denoise滑杆.bat` → `http://127.0.0.1:8189`。上传图、拖滑杆、实时对比源图与结果，
历史记录点一下就回填参数。

滑杆范围 0.05–1.00，`0.55` 是默认档 —— 保守改动、人物身份稳。0.75 以上开始大幅重绘，
0.97 基本等于只用源图定构图。

**提示词必须英文、标签式**。同一张图、同 seed、同 denoise：

```
中文： 就这个姿势，画风不变，人物样貌不变，把背景换成白天的海边   → 背景基本没动
英文： same pose, same art style, same girl, identical face,
       identical long silver hair, sunny beach background,
       bright daylight, clear sky                                 → 改到位
```

写**状态标签**（`sunny beach`、`bright daylight`）而不是**动作指令**
（`change the background to`），后者模型响应很弱。

### 装

两种方式内容一致：

```powershell
# 方式一：下 Release（不用装 git）
# 从 Releases 下 comfyui-dsh.zip，解压到 D:\ComfyUI

# 方式二：git clone
git clone https://github.com/devin667/comfyui-dsh.git D:\ComfyUI

cd D:\ComfyUI
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

`install.ps1` 分 9 步、全程幂等，中断了直接重跑。第 7、8 步是可选的写实底模与 FLUX：

```powershell
.\install.ps1                                 # 只装动漫底模（15 GB）
.\install.ps1 -WithRealistic                  # + RealVisXL V5（推荐，21.5 GB）
.\install.ps1 -WithRealistic -WithJuggernaut  # 两个写实底模（28 GB）
.\install.ps1 -WithRealistic -WithFlux        # + FLUX 四件套与 GGUF 节点（24 GB）
```

装完双击 `启动ComfyUI.bat`，再跑 `node .\dsh\apply-workflows.mjs` 接到 DSH。
逐步说明与排错见 **[docs/INSTALL-QUICK.md](docs/INSTALL-QUICK.md)**。

想让 AI 帮你装？把 **[docs/AGENT-PROMPT.md](docs/AGENT-PROMPT.md)** 整段复制给 DSH
（或任何能跑命令的 agent），它自己走完全程并自查。

### 速度

条件：`832×1216`，SDXL 30 步 / cfg 5 / dpmpp_2m karras，RTX 5060 Laptop 8 GB。

| 底模 | 热态单图 | 首图（含加载） | HiRes 1.5×（1248×1824） |
|---|---|---|---|
| Illustrious-XL | 26–33 s | 150 s | 62 s |
| **RealVisXL V5** | **26–31 s** | 150 s | **58 s** |
| Juggernaut XI v11 | 24–30 s | 150 s | 58 s |
| FLUX Krea Q2_K（24 步） | 82 s | 240 s | — |

#### 启动参数

```bat
main.py --listen 127.0.0.1 --port 8188 --cache-lru 8 --reserve-vram 0.3
```

就这四个，别的都别加。

| 参数 | 为什么 |
|---|---|
| `--cache-lru 8` | 缓存节点结果。**必须加**：默认 `--cache-none` 会让每个节点每次重算 |
| `--reserve-vram 0.3` | 给系统留 300 MB。0.5 太保守会触发 dynamic VRAM loading，0 又会在跑 FLUX 时爆 |
| ~~`--fast cublas_ops`~~ | **别加**。显存干净时反而慢 3.5 倍（115 s vs 32 s） |
| ~~`--fast fp16_accumulation`~~ | **别加**。单独使用慢 3.5 倍（72–87 s） |
| ~~`--enable-triton-backend`~~ | **别加**。装了 triton 3.5.1 反而灾难性变慢（FLUX 每步 178–295 s） |
| ~~`--highvram`~~ | 别加，8 GB 顶不住 4.9 GB 权重反复换出 |

**一条最实用的经验**：出图变慢先看 `nvidia-smi` 的 `memory.free`。剩 3.4 GB 和剩 6.2 GB
的差距是 142 秒 vs 32 秒 —— 比换任何参数都有效。浏览器 + 微信 + NVIDIA Overlay 能吃掉 2 GB。

踩坑全过程见 **[docs/PERFORMANCE.md](docs/PERFORMANCE.md)**。

### 接到 DSH

前提：已装 `dsh-image-gen` 插件（0.11.x）。

```powershell
node .\dsh\apply-workflows.mjs      # 写进 profile 配置，脚本会先备份
```

重启 DSH → 设置 → 插件 → 图像生成 → Provider 选 `comfyui`，Base URL 填
`http://127.0.0.1:8188`。之后 `generate_image` / `edit_image` 全部走本地。

**注意一个坑**：`dsh-image-gen` 的**图像生成工作台（Studio）不支持 ComfyUI**。
`CLOUD_IMAGE_PROVIDERS` 里没有 `comfyui`，工作台会回落到第一个配了 key 的云端 provider。
不受影响的是 Agent 工具链路 —— 聊天里让 Agent 出图走本地，工作台里动手点还是云端。

### 切换底模：`dsh-comfy-models`

`dsh-image-gen` 自己只能选工作流，改模型要手改 YAML + 重启。这个插件补上这一段。

```powershell
powershell -ExecutionPolicy Bypass -File .\dsh\install-plugin.ps1
```

| 工具 | 作用 |
|---|---|
| `comfy_models_list` | 列出 ComfyUI 里所有底模 + 当前工作流 + 当前激活项 |
| `comfy_models_sync` | 扫到新底模就自动生成 文生图 / 改图 / HiRes 三条工作流 |
| `comfy_models_switch` | 一句话切模型：`juggernaut` / `flux` / `realvis` 都能命中 |

匹配优先级：全等 → 忽略大小写全等 → 前缀 → 包含，同级取名字最短的
（所以 `juggernaut` 命中 `Juggernaut-XI` 而不是 `Juggernaut-XI-Edit`）。

改的是 profile 的 `cordis.patch.yml`，该文件被 HMR 监听，**改完十几秒自动生效，不用重启 DSH**。
细节见 [plugin/README.md](plugin/README.md)。

### 选错工作流不会白跑

`dsh-image-gen` 原版有个硬行为：工具调用里传了 `workflow: "..."` 就用它，
形状不对（文生图撞上带 `{{image}}` 的、改图撞上不带 `{{image}}` 的）直接抛错，
这几十秒就白跑了。卡片上又只写 `API workflow`，事后无法对账。

`scripts/patch-dsh-image-gen.py` 改掉这几件事（幂等，`--revert` 可还原）：

| 改动 | 效果 |
|---|---|
| 自动选对工作流 | 传的不合适就按「显式请求 → 同底模兄弟 → 同族兄弟 → 胶囊 → 其余」换成能干的，结果里带一句中文 notice 说明换成了哪条、为什么；一条能干的都没有才报错 |
| 底模上卡 | 从工作流 JSON 里读 `CheckpointLoaderSimple.ckpt_name` / `UnetLoaderGGUF.unet_name`，卡片标题旁显示真实底模 |
| 尺寸上卡 | 卡片显示生成图的**真实像素**，不再对非 `import` 来源留空 |

改图工作流现在也都吃尺寸：每条 `-Edit` / `-Rework` 在 `LoadImage` 与 `VAEEncode` 之间
插了一个 `ImageScale`（`lanczos` + `crop: center`），`edit_image` 传 `size` / `aspect_ratio`
会真的生效；比例与原图不同时按目标比例裁边，想保原构图就不传。

举例：`generate_image` 传了 `workflow: "RealVisXL-V5-Edit"`，自动改用 `RealVisXL-V5`，
notice 写「请求的「RealVisXL-V5-Edit」有 1 个 `{{image}}` 输入（文生图要求 0 个），做不了这次调用，已自动改用「RealVisXL-V5」。」
反过来 `edit_image` 传 `workflow: "RealVisXL-V5"` 会落到 `RealVisXL-V5-Edit` ——
**同底模优先**，不会跳到 FLUX 或 Juggernaut 去。

```powershell
python .\scripts\patch-dsh-image-gen.py --check   # 先看会改哪几处
python .\scripts\patch-dsh-image-gen.py           # 打补丁
python .\scripts\test-dsh-image-gen-pin.py        # 15 条断言，不碰 DSH 运行时
```

**改完必须重载插件**（`plugin_manager` 里关掉 `dsh-image-gen` 再打开），光改文件不生效 ——
文本层面已经换掉了，运行时还是旧代码，报错还是旧的英文串。

**插件升级会静默覆盖补丁**（`node_modules` 被重装），升级后发现行为回退就重跑一次。

### 事后对账：这张图到底是谁画的

ComfyUI 把整张工作流写进 PNG 的 `tEXt` 块，所以不用信任何界面上的字：

```powershell
python .\scripts\which_workflow.py                                  # 最近 8 张 dsh-*
python .\scripts\which_workflow.py ..\ComfyUI-0.45.0\output\a.png   # 指定文件
```

输出底模文件名、每段采样的步数/cfg/采样器/denoise、FaceID preset 与 LoRA 强度、文件名前缀。
HiRes 那种两段采样的会列出两行（`30步 ... | 18步 ... denoise0.35`）。

### 装了什么

| 内容 | 位置 | 说明 |
|---|---|---|
| ComfyUI 源码 | `ComfyUI-0.45.0/` | 上游 v0.45.0，不改一行 |
| Python 运行时 | `python-base/` | 独立 3.12 副本，不污染系统 Python |
| Python 环境 | `venv/` | torch 2.9.0+cu130 + 90 个包 |
| SDXL 动漫底模 | `models/checkpoints/` | Illustrious-XL v1.1，6.5 GB |
| SDXL 写实底模 | `models/checkpoints/` | RealVisXL V5.0 fp16（默认）、Juggernaut XI v11 |
| FLUX 底模 | `models/diffusion_models/` | flux1-krea-dev-Q2_K.gguf，3.7 GB |
| FLUX 文本编码器 | `models/text_encoders/` | t5-v1_1-xxl-Q4_K_S（2.55 GB）+ clip_l（235 MB） |
| FLUX VAE | `models/vae/` | flux_ae.safetensors，320 MB |
| GGUF 加载节点 | `custom_nodes/ComfyUI-GGUF/` | 读 FLUX 量化权重 |
| Denoise 滑杆 | `slider/` | 零依赖 Node 服务，8189 端口 |
| DSH 接入配置 | `dsh/` | workflow JSON + 补丁片段 + 应用脚本 |
| DSH 底模切换插件 | `plugin/` | `dsh-comfy-models`，三个工具 |
| 辅助脚本 | `scripts/` | 断点续传下载器、测速脚本、打包脚本 |

**仓库里不含**（体积太大，安装脚本按需下载）：模型权重 ≈ 19 GB、`venv/` 4.3 GB、
`python-base/` 381 MB、ComfyUI 源码。装完约占 **33 GB**（只装 SDXL 一个底模约 15 GB）。

### 硬件要求

| 项 | 最低 | 我这台实测 |
|---|---|---|
| 显卡 | 6 GB 显存，支持 CUDA | RTX 5060 Laptop，8 GB |
| 内存 | 16 GB | 16 GB |
| 磁盘 | 15 GB 空闲（四底模全装 33 GB） | 552 GB |
| 系统 | Windows 10/11 x64 | Windows 11 26100 |
| 驱动 | ≥ 570（cu130） | 617.42 |

**不支持 4 GB 显存 / 纯 CPU 跑 SDXL** —— 能启动，但一张图要 20 分钟以上。

各档显存、CUDA 版本、操作系统、Python 与 ComfyUI 版本、端口冲突的完整矩阵，见
**[docs/COMPATIBILITY.md](docs/COMPATIBILITY.md)**。最后一节叫「不适配就不适配，别硬凑」，
列的是物理限制：4 GB 跑 SDXL 1024×1024、8 GB 跑 FLUX 全精度、纯 CPU 跑 SDXL。
这些调参数解决不了，路径是换硬件到 16 GB 显存起步。

### 为什么本地跑

云端生图服务在服务端有内容审核，触发后请求被直接拒绝：

```
DashScope image generation failed (400):
{"code":"DataInspectionFailed","message":"Green net check rejected image (output)"}
```

`(input)` 是文字层拦截，改措辞还有机会过；`(output)` 是**图生成出来后送审被拒**，
判定对象是像素，提示词怎么写都没用。本地部署把整条链路搬到自己机器上，没有服务端审核这一环。

代价对比见 **[docs/why-local.md](docs/why-local.md)**。

### 安全与卸载

- **不写注册表**、**不装系统服务**、**不加开机启动**
- 不动显卡驱动，不装内核驱动
- 不跑的时候：0 进程、0 显存、0 CPU
- 卸载：结束 python 进程，删掉整个目录

端口只绑 `127.0.0.1`，局域网内其他机器访问不到。

### 从脚本里起服务

`serve_comfy.py` 用 `CREATE_BREAKAWAY_FROM_JOB` 起进程，脱离调用方的 Job Object：

```powershell
python D:\ComfyUI\serve_comfy.py      # 静默，脱会话
```

`Start-Process` 不够 —— agent shell 跑在 Windows Job 里，杀掉 job 会带走整棵进程树。
手动用还是双击 `启动ComfyUI.bat`（有控制台窗口能看进度）。

**默认只起服务，不开浏览器。** 双击之后控制台刷日志，你要看图就自己在浏览器里开
`http://127.0.0.1:8188`（收藏一次，以后点收藏夹就行）。这样后台常驻也不会有窗口突然弹出来打断你。

想要「起来就自动开」就带参数：

```bat
启动ComfyUI.bat -open        :: 或 --open，服务就绪后自动开浏览器
启动ComfyUI.bat              :: 默认，只起服务
启动ComfyUI.bat --no-browser :: 显式不出浏览器，跟默认一样
```

三种情况下都不会再出现 `Port 8188 is already in use`：探测到 8188 在听就只打印一行
`ComfyUI is already running.` 然后退出（带 `-open` 时才额外开浏览器）。

`start.bat` 是同一套逻辑的纯 ASCII 副本。之所以要两份：`.bat` 里写中文文件名在非 936
代码页的控制台下会被解成乱码路径，`call "%~dp0启动ComfyUI.bat"` 直接报
`is not recognized as an internal or external command`。中文名的给资源管理器双击用，
ASCII 的给任何自动化/终端调用用。

### 目录结构

```
ComfyUI-0.45.0/           ComfyUI 源码（v0.45.0，未改动）
  models/checkpoints/     Illustrious-XL / RealVisXL-V5.0 / Juggernaut-XI-v11
  models/diffusion_models/ flux1-krea-dev-Q2_K.gguf
  models/text_encoders/   t5-v1_1-xxl-Q4_K_S.gguf + clip_l.safetensors
  models/vae/             flux_ae.safetensors
  custom_nodes/ComfyUI-GGUF/   FLUX GGUF 加载节点
python-base/              独立 Python 3.12（可整目录搬移）
venv/                     Python 环境
slider/                   Denoise 滑杆（server.mjs / index.html / cli.mjs）
dsh/
  workflows/              13 条 workflow JSON（4 底模 × 文生图/改图 + 3 条 HiRes + 3 条 FaceID）
  workflows.manifest.json 工作流元数据 + 预设提示词
  apply-workflows.mjs     写进 cordis.patch.yml
  export-from-profile.mjs 从 profile 反向导出
  install-plugin.ps1      装底模切换插件
plugin/                   dsh-comfy-models（catalog / index / yaml-store + 负向脚本）
scripts/
  fetch_parts.sh          断点续传下载器（校验 206 + 字节数 + 魔数）
  bench_final.py          测速脚本
  which_workflow.py       读 PNG 里嵌的工作流，反查这张图是哪条工作流哪个底模出的
  patch-dsh-image-gen.py  选错工作流时自动改道 + 底模上卡（幂等，可 --revert）
  test-dsh-image-gen-pin.py  上面那个补丁的单元测试（14 条断言，不需要 DSH 运行时）
  pack-release.ps1        git archive 打包发行版
  make-release.py         建 GitHub release 并上传 zip + SHA256SUMS
docs/
  INSTALL-QUICK.md        逐步骤安装 + 排错
  AGENT-PROMPT.md         复制给 AI 让它自己装
  why-local.md            为什么本地跑 / 代价对比
  MODELS.md               四个底模横向实测
  PERFORMANCE.md          启动参数调优与显存争用
  COMPATIBILITY.md        显卡/驱动/系统/版本适配矩阵
  IPADAPTER.md            FaceID 保脸换装：两种 preset 差别、参数、五个坑
  preview/                README 用的截图
启动ComfyUI.bat           启动 ComfyUI（默认不开浏览器，-open 才开）
start.bat                 ASCII 版启动器，功能同上，中文路径炸掉时的备胎
open_when_ready.bat       轮询 8188，服务起来后开浏览器（仅 -open 时被调用）
启动Denoise滑杆.bat       启动滑杆页
install.ps1               一键安装
CHANGELOG.md              变更日志
README.en.md              英文说明
```

### 常见问题

**Q: 报 `Could not connect to ComfyUI at http://127.0.0.1:8188`**
ComfyUI 没启动。`dsh-image-gen` 没有 provider 回退逻辑，连不上就直接抛错。双击 `启动ComfyUI.bat`。

**Q: 报 `You need pytorch with cu130 or higher`**
```powershell
.\venv\Scripts\pip.exe install --no-deps --force-reinstall "https://mirrors.aliyun.com/pytorch-wheels/cu130/torch-2.9.0%2Bcu130-cp312-cp312-win_amd64.whl"
```

**Q: 装依赖后 torch 变成 CPU 版**
`pip install -r requirements.txt` 会重装 torch。查：
```powershell
.\venv\Scripts\python.exe -c "import torch;print(torch.__version__, torch.cuda.is_available())"
```
应当输出 `2.9.0+cu130 True`。

**Q: 出图 200 秒以上**
先看 `nvidia-smi` 的 `memory.free`。低于 4 GB 就是被别的程序占了。再确认启动参数**只有**
`--cache-lru 8 --reserve-vram 0.3`。详见 [docs/PERFORMANCE.md](docs/PERFORMANCE.md)。

**Q: 出的图满脸雀斑斑点**
提示词里写了 `freckles`。去掉它，负向加斑点类词（清单见 [docs/MODELS.md](docs/MODELS.md)）。

**Q: 写实模型出的图像棚拍、不像真人**
`masterpiece, best quality, 8k` 会把写实模型拉向影楼美化。要日常感就写
`amateur snapshot, taken on iPhone, unedited, grain`。cfg 用 5，别用 7。

**Q: 想换模型**
任何 SDXL 系 checkpoint 丢进 `models/checkpoints/`，跑一次 `comfy_models_sync` 自动生成工作流。
FLUX 系需要 GGUF 量化 + ComfyUI-GGUF 节点。

**Q: 模型文件大小对但加载报 `GGUF magic invalid`**
hf-mirror 被限流时会把报错页当正文写进文件，大小完全吻合。用 `scripts/fetch_parts.sh` 下载，
它校验 HTTP 206 + 每段字节数 + 文件魔数。

### 版本

| 版本 | 底模 | 启动参数 | 磁盘 |
|---|---|---|---|
| v1.0.0（2026-11-15） | Illustrious-XL（动漫） | `--cache-none` | 11 GB |
| v1.1.0（2026-11-16） | + RealVisXL V5 / Juggernaut XI / FLUX Krea | `--cache-lru 8 --reserve-vram 0.3` | 15–33 GB |
| v1.1.1（2026-11-16） | 同上（纯文档：英文说明、变更日志、适配矩阵） | 同上 | 同上 |
| v1.2.0（2026-11-16） | 同上（README 图文改版：banner + 四张实测截图） | 同上 | 同上 |
| v1.2.1（2026-11-17） | 同上（启动器重写：不再撞端口、就绪自动开页、ASCII 备胎） | 同上 | 同上 |
| v1.2.2（2026-11-17） | 同上（默认不开浏览器，`-open` 才开） | 同上 | 同上 |
| **v1.3.0（2026-11-17）** | 同上（新增 IPAdapter FaceID 保脸换装 + 2 条工作流） | 同上 | 同上 |
| **v1.3.1（2026-11-18）** | 同上（胶囊优先补丁、底模上卡、13 条工作流、对账脚本） | 同上 | 同上 |
| **v1.4.0（2026-11-19）** | 同上（选错工作流自动改道、FaceID 权重修正、Rework 工作流、Undress 提示词去冲突） | 同上 | 同上 |
| **v1.4.1（2026-11-19）** | 同上（五条改图工作流补上 `size` / `aspect_ratio` 支持，15 条全部吃尺寸） | 同上 | 同上 |

逐条变更见 **[CHANGELOG.md](CHANGELOG.md)**。

---

## English

A local image generation stack for Windows: **ComfyUI** runs on `127.0.0.1:8188` and the
DSH **`dsh-image-gen`** plugin calls it over HTTP. Four checkpoints (anime + three
photoreal), a denoise slider, and a plugin that switches checkpoints with one sentence.
Measured on an 8 GB RTX 5060 Laptop: **26–33 s** per 832×1216 SDXL image.

Full English documentation: **[README.en.md](README.en.md)**.

---

## 许可

本仓库的脚本与滑杆页面：MIT。

ComfyUI 源码：GPL-3.0，来自 [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)。

模型权重许可见各自仓库：Illustrious-XL v1.1（非商用）、RealVisXL V5.0、Juggernaut XI v11、
FLUX.1 Krea dev（非商用）。仓库里不包含模型权重，安装脚本仅提供下载指引。
