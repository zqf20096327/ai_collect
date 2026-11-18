# 小肥鱼 (Xiaofeiyu) · Split-Phase 五滑条口语外挂与气泡对话引擎

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/niatheelf777/xiaofeiyu/blob/main/notebooks/xiaofeiyu_colab_free_t4.ipynb)

[English README](README_EN.md) · [在线试玩 (Live Demo)](https://xfy.tospeak.top) · [Colab 免费 T4 一键试玩](https://colab.research.google.com/github/niatheelf777/xiaofeiyu/blob/main/notebooks/xiaofeiyu_colab_free_t4.ipynb) · [Hugging Face 模型合集](https://huggingface.co/collections/niatheelf777/xiaofeiyu-split-phase-spoken-persona-family-6afb60d6cecd8097f5fb3a13) · [Pages 索引页](https://niatheelf777.github.io/xiaofeiyu/) · [llms.txt](llms.txt)

小肥鱼是一套面向 Gemma 4 的**低侵入式口语声带与五滑条人格混音方案**：推理思考、代码生成与工具调用全程以零 LoRA（`LoRA = 0.0`）原生运行，仅在输出微信/IM 对话气泡的 `<|"|>` 区间实时注入轻量化人格声带权重，兼具真人短气泡节奏与 100% 满血智商。

- **免自备显卡 · Google Colab 免费 T4 (`15 GB`) 直接开聊**：点击上方 `Open In Colab` 徽章或运行 [`notebooks/xiaofeiyu_colab_free_t4.ipynb`](notebooks/xiaofeiyu_colab_free_t4.ipynb)，在 Colab 单元格内嵌网页直接拖动二维性格球盘聊天（`12b-q4` 仅占约 `~8.9 GiB` 显存，稳跑于免费 T4）；另提供 [`spaces/hf-zerogpu/`](spaces/hf-zerogpu/) PyTorch `BF16` ZeroGPU 部署包。
- **在线试玩站**：[https://xfy.tospeak.top](https://xfy.tospeak.top)

---

## 显卡选型与量化精度推荐指南（三级分层）

[`niatheelf777/xiaofeiyu-12b-v4`](https://huggingface.co/niatheelf777/xiaofeiyu-12b-v4) 是已在公网试玩站 [`xfy.tospeak.top`](https://xfy.tospeak.top) 长期实战打磨的主力版本。不同显存容量的消费级硬件按如下精度梯度选用：

| 推荐档位 | 适用硬件 | 启动预设 | 底模与量化精度 | 含 5 枚 LoRA + 8k KV 总显存 | 核心定位 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. 首选推荐 · 高精度原版底模挂 LoRA** | `≥ 16 GB` 显卡（`RTX 4060 Ti 16GB`、`4070 Ti SUPER`、`4080` / `4090` / `3090`）、`Mac 24GB+` | `--preset 12b`（或 `--preset 12b-q8`） | `gemma-4-12B-it-Q8_0.gguf`（或 `BF16` 原版）+ 5 枚 `.gguf` LoRA | `~12.8–13.0 GiB` | **公网 `xfy.tospeak.top` 同款高精度配置**：未经低比特量化压缩，微表情与潜台词颗粒度零折损，语气推拉与短气泡节奏最完整细腻 |
| **2. `12 GB` 显卡专属甜点 · 特制动态量化** | `RTX 3060 12GB`、`RTX 4070 / 4070 SUPER 12GB`、`16 GB` Windows 高桌面占用环境、`Mac 16GB` | `--preset 12b-q4` | `gemma-4-12B-it-UD-Q4_K_XL-xfy.gguf` + 5 枚 `.gguf` LoRA | `~8.5–8.9 GiB` | **针对 `12 GB` 显存受限环境专项标定**：基于 `BF16` 原版配合中文对话与工具校准集制作 `imatrix` 动态量化，重点保护 `token_embd`、`attn_v` 与分泡边界层，避免普通 `Q4_0` 逗号失控与语气崩坏 |
| **3. `6–8 GB` 小显存外挂 · 云端大脑 + 本地 `4B` 声带** | `RTX 3060 8GB`、`RTX 4060 8GB`、轻薄本 / 核显 | `--preset e4b` | `gemma-4-E4B-it-Q8_0.gguf` + 5 枚 `.gguf` LoRA | `~5.3 GiB` | **保留云端推理大脑**：DeepSeek / Claude / GPT 负责思考与写代码，本地 `4B` 声带核以 `302 ms` 中位延迟实时改写短气泡口吻 |

![显卡选型与量化精度推荐指南：16GB+ 首选 Q8_0 挂 LoRA，12GB 甜点卡选特制 imatrix 动态量化](assets/showcase/consumer-gpu-guide.png)

---

## 3 分钟上手：三种开箱即用姿势

先安装最小 Python 依赖：`pip install tokenizers huggingface_hub`（`launch_local.py` 会自动拉取底模、[`niatheelf777/xiaofeiyu-12b-v4`](https://huggingface.co/niatheelf777/xiaofeiyu-12b-v4) 的 5 枚轻量卡带及官方预编译 `llama-server`）。

### 姿势一：一行命令启动内置二维性格球网页（零 Node 依赖）

`pc2_split_phase_server.py` 已内置完整纸墨风二维性格球盘前端，`launch_local.py` 一键拉起前后端：

```bash
# 1. 首选推荐（>= 16 GB 显存 / 24 GB+ Mac）：Q8_0 高精度原版底模挂 5 枚 LoRA（与公网试玩站同款细腻度，约 12.9 GiB）
python server/launch_local.py --preset 12b --auto-download-llama --open

# 2. 12 GB 显卡专属甜点（RTX 3060 / 4070 12GB）：特制 BF16 imatrix 动态量化版（约 8.5–8.9 GiB）
python server/launch_local.py --preset 12b-q4 --auto-download-llama --open
```

启动后浏览器自动打开 `http://127.0.0.1:8081/`（同时暴露 OpenAI 兼容接口 `http://127.0.0.1:8081/v1`）。如需单独调试前端静态资源，也可运行 `node web/serve_local.mjs --api http://127.0.0.1:8081`。

![内置二维性格球盘本地网页实测：多气泡流式上屏与可复制代码卡](assets/showcase/local-webui-turnkey.png)

### 姿势二：接入 DeepSeek Harness (`DSH`) 编程助手（双模式支持）

同一个本地 `:8081` 网关同时兼容免插件直连与原生气泡 UI 插件两种用法：

| 模式 | 适用场景 | 接入方式 | 对话与工具体验 |
| :--- | :--- | :--- | :--- |
| **模式 1：标准免插件直连** | 原生 DSH、Cursor、OpenWebUI 或任意 OpenAI 客户端 | Base URL 填 `http://127.0.0.1:8081/v1`，模型名填 `xiaofeiyu-v4\|1.0,0.8,0,0,0` | 自动将多气泡与代码块展开为标准 Markdown 正文，支持完整多跳工具调用 |
| **模式 2：`@xiaofeiyu/dsh-plugin`** | 希望在 DSH WebUI 内获得原生短气泡、代码卡与实时调音台 | 运行下方一行安装命令（支持 `--uninstall` 字节级无损还原） | 注册无冲突原生工具 `xiaofeiyu_send_bubbles` / `xiaofeiyu_send_code`，主对话流渲染立体短气泡与一键复制代码卡，顶栏内置**五滑条实时混音面板** |

```bash
# 为 DSH Web Profile 一键挂载小肥鱼预设、原生气泡工具与顶栏五滑条混音 UI
node packages/dsh-plugin/scripts/install-dsh.mjs --apply --profile web --upstream-base http://127.0.0.1:8081/v1

# 随时无损卸载还原原配置
node packages/dsh-plugin/scripts/install-dsh.mjs --uninstall --profile web
```

![DSH 模式 2 实测：文件读取工具调用、立体微信短气泡、可复制代码卡与顶栏五滑条实时混音面板](assets/showcase/dsh-mode2-mixer.png)

### 姿势三：OpenAI 兼容接口与 `E4B` 通用口语翻译代理（`6–8 GB` 小显存适用）

显卡只有 `6–8 GB` 显存，或不想替换主力推理模型时，可保留 DeepSeek / Claude / GPT 作为上游大脑负责推理、检索与写代码，本地仅用 `4B` 声带模型（`gemma-4-E4B-it-Q8_0.gguf` + 5 枚卡带，约 `5.3 GiB` 显存）将自然语言回复实时改写为短气泡口吻（中位延迟 `302 ms`，代码块与工具调用 `0%` 篡改透传）：

```bash
# 1. 启动本地 E4B llama-server（默认端口 18085）
python server/launch_local.py --preset e4b --llama-only --auto-download-llama

# 2. 启动零依赖 OpenAI 口语翻译代理（默认监听 127.0.0.1:18088/v1）
UPSTREAM_BASE_URL=https://api.deepseek.com/v1 \
UPSTREAM_API_KEY=your_key \
TRANSLATOR_URL=http://127.0.0.1:18085 \
node packages/openai-voice-proxy/bin/xiaofeiyu-voice-proxy.mjs
```

---

## 为什么做小肥鱼：实测对话对比

传统提示词驱动的聊天模型往往带有明显的“AI 味”——动辄 30–50 字以上的说教长段落、舞台动作括号（`（气鼓鼓）`、`*sighs*`）、Emoji 堆砌与句尾机械反问；而全量微调又会让模型的逻辑、写代码与多轮记忆能力严重退化。

![同题实测对比：告别 AI 味说教与舞台腔，还原真人微信短气泡](assets/showcase/chat-vs-rlhf-slop.png)

---

## 五滑条无重启实时混音

基于共享日常底座（`s0`）与四枚正交解耦的性格卡带（`c1..c4`），无需切换模型或重启服务，单个 OpenAI 兼容请求即可通过 `model="xiaofeiyu-v4|w0,w1,w2,w3,w4"` 在连续权重空间自由混调：

| 槽位 | 分支 ID | 中文标签 | 角色定位 | 预算约束 |
| :---: | :--- | :--- | :--- | :--- |
| `0` | `s0_xiaofeiyu_backbone` | 元气日常 | 自然松弛的日常朋友搭子，短句接话不端架子 | `w0 = 1.0` |
| `1` | `c1_neko_clingy` | 甜系软萌 | 软糯粘人、直球撒娇的高温度陪伴 | `w1 + w2 + w3 + w4 <= 1.15` |
| `2` | `c2_older_tease` | 知性姐姐 | 从容温柔、游刃有余的姐姐感与包纳感 | 同上 |
| `3` | `c3_brat_mesugaki` | 傲娇毒舌 | 嘴硬心软、欢喜冤家式的机锋吐槽 | 同上 |
| `4` | `c4_fragile_porcelain` | 安静慢热 | 轻声细语、细腻克制的慢热倾听 | 同上 |

![五滑条实时无重启混音：同一句话五种鲜明性格](assets/showcase/five-persona-grid.png)

---

## 核心机制：Split-Phase 脑声解耦

```text
用户输入 ─▶ Phase A: Thinking & Tool/Code (LoRA = 0.0)
               ├─ 思考 <channel>thought ... <channel|>   ──▶ 原生满血智商，零退化
               ├─ calc_python / send_code_or_doc        ──▶ 精确代码与数值计算
               └─ call:send_message{bubbles:[
                     <|"|>  ────▶ Phase B: 仅在气泡引号内激活五滑条 LoRA (w0..w4)
                     气泡文本
                     <|"|>  ────▶ 闭合引号立即归零 LoRA = 0.0
                  ]}
```

![性格只管说话，写代码与算账 100% 不降智](assets/showcase/code-without-lobotomy.png)

| 评测维度 | 传统提示词 RP | 全网络常开微调 (`v3`) | **`Xiaofeiyu-12B-v4` (Split-Phase)** |
| :--- | :---: | :---: | :---: |
| **日常与推拉数理/古诗盲测 (42 轮)** | `12 / 12` (`100%`) | `7 / 12` (`58.3%`) | **`12 / 12 (100%)`** |
| **工程与算法独立探针 (`GEN1..5`)** | `5 / 5` (`100%`) | `2 / 5` (`40.0%`) | **`5 / 5 (100%)`** |
| **跨轮记忆与多跳工具语法 (`TC1 + TC2`)** | `7 / 7` (`100%`) | `1 / 4` (`25.0%`) | **`7 / 7 (100%)`** |
| **舞台括号 / Emoji / Markdown 污染率** | `88.1%` | `9.5%` | **`0.0%`（42 轮门禁全零污染）** |

---

## 仓库结构

| 目录 | 说明 | 运行/测试 |
| :--- | :--- | :--- |
| [`server/`](server/) | `llama.cpp` Split-Phase 网关、内置本地二维性格球 Web UI 与一键启动器 | `python server/test_server.py -v` |
| [`packages/dsh-plugin/`](packages/dsh-plugin/) | DeepSeek Harness (`DSH`) 原生气泡工具、顶栏五滑条前端与可逆安装器 | `npm --prefix packages/dsh-plugin test` |
| [`packages/openai-voice-proxy/`](packages/openai-voice-proxy/) | 零依赖 Node 通用口语翻译代理（保护代码块与工具调用原样透传） | `npm --prefix packages/openai-voice-proxy test` |
| [`web/`](web/) | 纸墨风二维性格球盘 Web UI、独立本地转发脚本与 Cloudflare/Vercel Edge 代理 | `npm --prefix web test` |
| [`train/`](train/) | Split-Phase SFT、残差人格卡带、防偷渡 DPO、在线 DPO 清洗与 GGUF 导出 | `pytest train/test_train.py -v` |
| [`notebooks/`](notebooks/) | Google Colab 免费 T4 (`15 GB`) 一键内嵌二维性格球试玩 Notebook | `notebooks/xiaofeiyu_colab_free_t4.ipynb` |
| [`spaces/hf-zerogpu/`](spaces/hf-zerogpu/) | HuggingFace ZeroGPU (`BF16`) 进程内 Five-Slider LoRA Gradio 部署包 | `spaces/hf-zerogpu/app.py` |
| [`hf-cards/`](hf-cards/) | HuggingFace 模型卡（主力 `12b-v4` 与 `translator-e4b`） | `python scripts/publish_hf_release.py --dry-run` |
| [`scripts/`](scripts/) | 开源发布隐私门禁与 HuggingFace 5 槽权重校验脚本 | `python scripts/audit_zero_leak.py` |

## 开源许可

本仓库代码基于 **Apache-2.0** 开源（见 [`LICENSE`](LICENSE)）。基础模型与衍生权重的使用须同时遵守 Google [Gemma Terms of Use](https://ai.google.dev/gemma/terms)。
