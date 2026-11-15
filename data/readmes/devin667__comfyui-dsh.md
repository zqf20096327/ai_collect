# ComfyUI + DSH 本地生图（Windows / RTX 50 系显卡）

一套能落地的本地生图方案：**ComfyUI 独立进程**跑在本机 8188 端口，**DSH 插件**
`dsh-image-gen` 通过 HTTP 调用它。生图链路全程在本机完成，能有效避开云端审核，
不消耗生图 token，产出直接落在自己硬盘上。

配套一个自制的 **Denoise 滑杆页面**（8189 端口）：上传一张图，拖动滑杆就能从「微调」
到「基本重画」，实时对比源图与结果，历史记录可一键回填参数。

---

## 这套东西解决什么问题

云端生图服务（DashScope / OpenAI / Seedream）在服务端有内容审核，触发后请求被直接拒绝：

```
DashScope image generation failed (400):
{"code":"DataInspectionFailed","message":"Green net check rejected image (output)"}
```

`(input)` 是文字层拦截，改措辞还有机会过；`(output)` 是**图生成出来后送审被拒**，
判定对象是像素，提示词怎么写都没用。

本地部署把整条生成链路搬到自己机器上：请求不出本机，也就没有服务端审核这一环。
这就是常说的**生图破甲**——不是绕规则，而是换一条根本不经过审核环节的链路。

细节、代价对比和 8 GB 显存能跑什么，见 [docs/why-local.md](docs/why-local.md)。

---

## 装了什么 / 没装什么

| 内容 | 位置 | 说明 |
|---|---|---|
| ComfyUI 源码 | `ComfyUI-0.45.0/` | 从上游 GitHub 取 v0.45.0，不改一行 |
| Python 运行时 | `python-base/` | 独立 3.12 副本，不污染系统 Python |
| Python 环境 | `venv/` | torch 2.9.0+cu130 + 86 个包 |
| SDXL 模型 | `models/checkpoints/` | Illustrious-XL v1.1，6.46 GB |
| Denoise 滑杆 | `slider/` | 零依赖 Node 服务，8189 端口 |
| DSH 接入配置 | `dsh/` | workflow JSON + 补丁片段 + 应用脚本 |

**仓库里不含**（体积太大，安装脚本按需下载）：

- 模型权重 6.46 GB — 从 HF 镜像拉
- `venv/` 4.3 GB — 本地生成
- `python-base/` 381 MB — 从官方便携版复制
- ComfyUI 源码 — 按 tag 下载

装完约占 **11 GB 磁盘**。

---

## 三步装完

**方式一：下 Release（不用装 git）**

到 [Releases](https://github.com/devin667/comfyui-dsh/releases/latest) 下 `comfyui-dsh.zip`，
解压到 `D:\ComfyUI`，然后：

```powershell
cd D:\ComfyUI
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

**方式二：git clone**

```powershell
git clone https://github.com/devin667/comfyui-dsh.git D:\ComfyUI
cd D:\ComfyUI
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

两者内容一致。`install.ps1` 分 7 步、全程幂等，中断了直接重跑：

1. 下载 Python 3.12 便携版 → `python-base\`（不动系统 Python）
2. 建 venv，`pyvenv.cfg` 重指当前目录（整个文件夹可搬移）
3. 装 **torch 2.9.0+cu130**（RTX 50 系必须 cu130，cu126/cu128 会报
   `You need pytorch with cu130 or higher to use optimized CUDA operations`）
4. 下载 ComfyUI v0.45.0 源码
5. 装其余依赖（Torch 已就位，不会被顶成 CPU 版）
6. 下载 Illustrious-XL 模型（走 hf-mirror，比 HF 官方快两个数量级）
7. 冒烟测试：`cuda True` / 显卡型号 / 显存 / `matmul ok`

装完双击 `启动ComfyUI.bat`，再跑一次 `node .\dsh\apply-workflows.mjs` 接到 DSH。
逐步骤说明和排错见 **[docs/INSTALL-QUICK.md](docs/INSTALL-QUICK.md)**。

想让 AI 帮你装？把 **[docs/AGENT-PROMPT.md](docs/AGENT-PROMPT.md)** 里的整段话
复制给 DSH（或任何能跑命令的 agent），它自己会走完全程并自查。

---

## 硬件要求

| 项 | 最低 | 我这台实测 |
|---|---|---|
| 显卡 | 6 GB 显存，支持 CUDA | RTX 5060 Laptop，8 GB |
| 内存 | 16 GB | 16 GB |
| 磁盘 | 15 GB 空闲 | — |
| 系统 | Windows 10/11 x64 | — |

8 GB 显存跑 SDXL 1024×1024 刚好够，但**实际可用显存要看当时占用**：浏览器 + 微信 +
NVIDIA Overlay 能吃掉 2 GB。实测空闲 5.7 GB 也能跑，只是慢一些。

**不支持 4 GB 显存 / 纯 CPU 跑 SDXL**——能启动，但一张图要 20 分钟以上，没有实用价值。

---

## 出图速度（RTX 5060 Laptop 实测）

| 配置 | 1024×1024 / 20-24 步 |
|---|---|
| 默认（`--cache-none`，dpmpp_2m/karras） | **56–68 秒** |
| 首张（模型未缓存） | 160 秒左右 |
| `--disable-fast-disk` | 更慢（19-21 s/it，内存装不下权重） |
| `--highvram` | 更慢（180 s/it，8 GB 显存顶不住 4.9 GB 权重反复换出） |

那个 `--cache-none` 是关键。默认配置下 ComfyUI 把中间结果缓存进内存，16 GB 机器只剩
1.2 GB 可用时，SDXL 的 4.9 GB 权重会反复从磁盘重读，一张图跑到 200 秒以上。
关掉缓存反而快 3-4 倍。

---

## Denoise 滑杆怎么用

双击 `启动Denoise滑杆.bat`，浏览器开 `http://127.0.0.1:8189`。

滑杆范围 0.05–1.00，语义对照：

| denoise | 效果 |
|---|---|
| 0.05–0.20 | 几乎不动，只补细节 |
| 0.20–0.40 | 轻微改动（换表情、加配饰） |
| 0.40–0.55 | 保守改动，人物身份稳 |
| 0.55–0.75 | 中幅改动（**0.55 是默认档**） |
| 0.75–0.88 | 大幅改动（明显重绘的上限大约 0.8） |
| 0.88–0.97 | 激进，脸开始漂 |
| 0.97–1.00 | 基本等于只用源图定构图 |

**提示词必须用英文，而且要用 Danbooru 标签式**，不是自然语言句子。同一张图、同 seed、
同 denoise 下实测：

```
中文： 就这个姿势，画风不变，人物样貌不变，把背景换成白天的海边   → 背景基本没动
英文： same pose, same art style, same girl, identical face,
       identical long silver hair, sunny beach background,
       bright daylight, clear sky                                 → 改到位
```

原因是 SDXL 的文本编码器按英文标签训练，中文进去基本等于噪声。要写「状态标签」
（`sunny beach`、`bright daylight`）而不是「动作指令」（`change the background to`），
后者模型响应很弱。

---

## 接到 DSH 上

前提：DSH 已装 `dsh-image-gen` 插件（0.11.x）。

```powershell
# 把 workflow 写进 profile 配置（脚本会先备份再改）
node .\dsh\apply-workflows.mjs
```

然后重启 DSH，设置 → 插件 → 图像生成：

- Provider 选 `comfyui`
- Base URL 填 `http://127.0.0.1:8188`

之后 `generate_image` / `edit_image` 工具调用全部走本地。

**注意一个坑**：`dsh-image-gen` 的**图像生成工作台（Studio）不支持 ComfyUI**。
`CLOUD_IMAGE_PROVIDERS` 这个列表里没有 `comfyui`，所以工作台会回落到第一个配了 key 的
云端 provider（比如 DashScope → qwen-image-3.0）。工作台里出图仍然是云端出的。

不受影响的是 Agent 工具链路——`generate_image`、`generate_images`、`edit_image` 三个
工具在 `generateSingle` / `editComfyUIImage` 分支里对 comfyui 是完整支持的。所以聊天里
让 Agent 生图走本地，工作台里动手点还是走云端。

---

## 安全与卸载

- **不写注册表**、**不装系统服务**、**不加开机启动**
- 不动显卡驱动，不装内核驱动（这点和 Nmap 那种带 Npcap 的安装不同）
- 不跑的时候：0 进程、0 显存、0 CPU
- 卸载：结束 python 进程，删掉整个目录

端口只绑 `127.0.0.1`，局域网内其他机器访问不到。

---

## 目录结构

```
ComfyUI-0.45.0/           ComfyUI 源码（v0.45.0，未改动）
  models/checkpoints/     Illustrious-XL-v1.1.safetensors
  input/                  上传的源图落这里
  output/                 生成的图落这里
  main.py
python-base/              独立 Python 3.12（可整目录搬移）
venv/                     Python 环境
slider/
  server.mjs              零依赖 HTTP 服务
  index.html              滑杆页面
  cli.mjs                 命令行入口
  启动滑杆.bat
dsh/
  workflows/              workflow JSON（文生图 + 图生图）
  apply-workflows.mjs     写进 cordis.patch.yml
docs/
  INSTALL-QUICK.md        逐步骤安装说明 + 排错
  AGENT-PROMPT.md         复制给 AI 让它自己装的 prompt
  why-local.md            为什么本地跑 / 代价对比
启动ComfyUI.bat           启动 ComfyUI（已在跑就提示）
启动Denoise滑杆.bat       启动滑杆页（已在跑就打开浏览器）
install.ps1               一键安装
```

---

## 常见问题

**Q: 报 `Could not connect to ComfyUI at http://127.0.0.1:8188`**
ComfyUI 没启动。`dsh-image-gen` 没有 provider 回退逻辑，连不上就直接抛错，不会静默切到
云端。双击 `启动ComfyUI.bat`。

**Q: 报 `You need pytorch with cu130 or higher`**
torch 版本不对。RTX 50 系（Blackwell / sm_120）必须 cu130：
```powershell
.\venv\Scripts\pip.exe install --no-deps --force-reinstall "https://mirrors.aliyun.com/pytorch-wheels/cu130/torch-2.9.0%2Bcu130-cp312-cp312-win_amd64.whl"
```

**Q: 装依赖时 `pip` 把 torch 降级成 CPU 版**
`pip install -r requirements.txt` 会重装 torch。装完必须检查：
```powershell
.\venv\Scripts\python.exe -c "import torch;print(torch.__version__, torch.cuda.is_available())"
```
应当输出 `2.9.0+cu130 True`。不是的话用 `--no-deps --force-reinstall` 重装 torch。

**Q: 出图 200 秒以上**
检查启动参数有没有 `--cache-none`，以及任务管理器里可用内存有没有低于 2 GB。

**Q: 想换模型**
任何 SDXL 系 checkpoint 都能用，丢进 `models/checkpoints/` 即可。改
`dsh/workflows/*.json` 里的 `ckpt_name` 字段。Flux（12B）/ Qwen-Image（20B）在 8 GB
显存上跑不动。

---

## 许可

本仓库的脚本与滑杆页面：MIT。

ComfyUI 源码：GPL-3.0，来自 [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)。
Illustrious-XL 模型：见 [OnomaAIResearch/Illustrious-XL-v1.1](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v1.1)
的许可条款（非商用）。仓库里不包含模型权重，安装脚本仅提供下载指引。
