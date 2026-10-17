<p align="center">
  <b style="font-size: 2em;">MoXin（墨心）</b>
</p>

<p align="center">
  从零实现的中文大语言模型 & 多模态视觉语言模型 & 视觉语言动作模型
</p>

<p align="center">
  <a href="#模型架构">架构</a> •
  <a href="#训练流程">训练</a> •
  <a href="#效果展示">效果</a> •
  <a href="#评测与推理">评测</a> •
  <a href="https://huggingface.co/mozihe/moxin">模型权重</a> •
  <a href="LICENSE">License</a>
</p>

---

## 简介

MoXin（墨心）是一个完全从零构建的中文语言模型项目，覆盖从 Tokenizer 训练、语言模型预训练、多阶段 SFT、LoRA 微调到多模态视觉语言扩展的完整流程，并进一步扩展至视觉语言动作（VLA）模型，实现端到端的机器人操控。项目不依赖任何第三方训练框架，所有组件均基于 PyTorch 原生实现。

### 核心特性

- **从零构建** — Tokenizer、模型架构、训练管线全部从头实现
- **混合专家架构（MoE）** — 底层 Dense Block 学习基础表示，顶层 MoE Block 实现专家分工
- **多模态视觉理解** — 冻结 CLIP ViT-B/16 + 可学习投影层，支持图文对话
- **视觉语言动作（VLA）** — π₀ 风格 Flow Matching + Action Expert，端到端机器人控制
- **LoRA 微调** — 基于 forward hook 的非侵入式实现，支持动态 attach / detach / merge
- **分布式训练** — 原生 PyTorch DDP，兼容多 GPU 与 CPU 训练
- **WebUI** — Flask + SSE 流式推理界面，支持 LLM 对话与 VLM 看图

### 模型权重

模型权重托管在 HuggingFace：[mozihe/moxin](https://huggingface.co/mozihe/moxin)

| 权重文件 | 说明 |
|---|---|
| `pretrain.pth` | 文本预训练 |
| `sft01.pth` | SFT 第一阶段 (seq_len=512) |
| `sft02.pth` | SFT 第二阶段 (seq_len=1024) |
| `moxin-lora.pt` | LoRA 微调权重 |
| `pretrain_vlm.pth` | VLM 预训练 |
| `sft_vlm.pth` | VLM SFT |
| `vla_lift.pth` | VLA — Lift 单任务 |
| `vla_libero_spatial.pth` | VLA — LIBERO-Spatial 多任务 |
| `norm_stats_lift.pt` | VLA — Lift 归一化统计量 |
| `norm_stats_libero_spatial.pt` | VLA — LIBERO-Spatial 归一化统计量 |

## 模型架构

### LLM (~270M)

```
Embedding (9600 vocab, dim=768, 权重与输出层共享)
├── 2 × Dense Block (Attention + SwiGLU FFN)
├── 10 × MoE Block (Attention + MoE FFN)
│   ├── 4 个路由专家, top-2 激活
│   ├── 1 个共享专家
│   └── 负载均衡辅助损失
├── RMSNorm
└── LM Head (tied weights)
```

### VLM (基于 LLM 扩展)

```
CLIP ViT-B/16 视觉编码器 (冻结, ~86M)
├── VisionProj (Linear → GELU → Linear, 768 → 768)
└── 196 个图像 patch token 注入文本序列
```

### VLA (基于 VLM 扩展, ~292M)

<p align="center">
  <img src="assets/vla_architecture.png" width="600">
</p>

```
Multi-Layer Feature Fusion (后 4 层 softmax 加权融合 + RMSNorm)
├── Action Expert (~22M)
│   ├── 3 × Action Expert Layer
│   │   ├── CrossAttention (VLM features → action tokens)
│   │   └── SelfAttention (action tokens 间时序建模)
│   ├── Sinusoidal Timestep Embedding
│   └── Proprio / Action 投影层
└── Flow Matching
    ├── Midpoint ODE Solver (二阶)
    ├── Classifier-Free Guidance (训练 5% drop)
    └── Proprioceptive Dropout (可选)
```

### 超参数

| 配置项 | LLM / VLM | VLA Action Expert |
|---|---|---|
| 隐藏维度 | 768 | 768 |
| Q 头数 / KV 头数 | 8 / 2 (GQA) | 8 / 8 |
| Transformer 层数 | 2 Dense + 10 MoE | 3 |
| FFN 隐藏维度 | 2048 | — |
| 专家数 / 激活数 / 共享 | 4 / 2 / 1 | — |
| 词表大小 | 9600 (BPE) | — |
| 动作维度 / Chunk 大小 | — | 7 / 16 |
| 位置编码 | RoPE (θ=1e6) | Sinusoidal |
| 归一化 | RMSNorm | RMSNorm |

## 项目结构

```
moxin_vlm/
├── config/
│   └── moxin_config.py              # 模型超参数配置
├── model/
│   ├── moxin_model.py               # LLM 主模型
│   ├── moxin_vlm_model.py           # VLM 多模态模型
│   ├── moxin_vla_model.py           # VLA 动作模型
│   ├── lora.py                      # LoRA 适配器与注入器
│   ├── utils.py                     # RoPE、GQA repeat_kv、image2tensor
│   └── nn/
│       ├── attention.py             # GQA 注意力 (RoPE + SDPA)
│       ├── block.py                 # Dense Transformer Block
│       ├── moe_block.py             # MoE Transformer Block
│       ├── feed_forward.py          # SwiGLU 前馈网络
│       ├── moe_feed_forward.py      # MoE 路由 + 共享专家
│       ├── moe_gate.py              # Top-K 专家门控 + 辅助损失
│       ├── rms_normal.py            # RMSNorm
│       ├── vision_proj.py           # 视觉投影层
│       ├── action_expert.py         # Action Expert 主模块
│       ├── action_block.py          # Action Expert Layer (CA + SA)
│       ├── action_attention.py      # Cross / Self Attention for actions
│       └── flow_matching.py         # Flow Matching (训练 + 采样)
├── envs/
│   ├── data_collector.py            # 数据采集 / 转换 (Lift + LIBERO)
│   └── wrapper/
│       ├── robosuite.py             # Robosuite 环境封装
│       └── libero.py                # LIBERO 环境封装
├── tokenizer/
│   ├── train_tokenizer.py           # BPE Tokenizer 训练脚本
│   └── moxin_tokenizer/             # 训练好的 Tokenizer 文件
├── dataset/script/
│   ├── pretrain_dataset.py          # 预训练数据集 (JSONL)
│   ├── sft_dataset.py               # SFT 数据集 (对话格式)
│   ├── vlm_dataset.py               # VLM 数据集 (Parquet, 图文)
│   └── vla_dataset.py               # VLA 数据集 (HDF5, 示教轨迹)
├── train/
│   ├── base_trainer.py              # 训练器基类 (DDP、AMP、checkpoint)
│   ├── pretrain.py                  # 文本预训练
│   ├── sft_train.py                 # 文本 SFT
│   ├── lora_train.py                # LoRA 微调
│   ├── vlm_pretrain.py              # VLM 预训练
│   ├── vlm_sft.py                   # VLM SFT
│   ├── vla_train.py                 # VLA 训练
│   └── utils.py                     # 学习率调度、训练循环、EMA
├── test/
│   ├── sft_test.py                  # SFT 对话
│   ├── lora_test.py                 # LoRA 对话
│   ├── vlm_sft_test.py              # VLM 看图对话
│   ├── vla_test.py                  # VLA 闭环评估
│   ├── vla_demo.py                  # VLA 交互式可视化
│   ├── lang_bench.py                # 中文能力评测
│   ├── ceval_bench.py               # C-Eval 评测
│   └── vlm_bench.py                 # VLM 生成质量评测
├── webui/
│   ├── app.py                       # Flask 后端 (SSE 流式推理)
│   └── templates/index.html         # 聊天界面
├── requirements.txt
└── LICENSE
```

## 环境安装

- Python >= 3.10
- PyTorch >= 2.0

```bash
pip install -r requirements.txt
git submodule update --init --recursive   # CLIP 视觉编码器
```

## 训练流程

<p align="center">
  <img src="assets/train_pipeline.png" width="600">
</p>

### 1. Tokenizer

```bash
python -m tokenizer.train_tokenizer
```

在 `dataset/data/tokenizer_data.jsonl` 上训练 BPE Tokenizer（词表 9600），Chat 模板：

```
<|start|><|system|>你是 墨心，是一个人工智能助手。<|end|>
<|start|><|user|>用户消息<|end|>
<|start|><|assistant|>助手回复<|end|>
```

### 2. 文本预训练

```bash
python -m train.pretrain
torchrun --nproc_per_node=4 -m train.pretrain   # 多卡
```

数据：`dataset/data/pretrain_data.jsonl`，格式 `{"text": "..."}`

输出：`out/pretrain.pth`

### 3. 文本 SFT（两阶段）

| 阶段 | 输入权重 | 序列长度 | 输出 |
|---|---|---|---|
| SFT-1 | `pretrain.pth` | 512 | `sft01.pth` |
| SFT-2 | `sft01.pth` | 1024 | `sft02.pth` |

```bash
python -m train.sft_train
```

数据格式：`{"conversations": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}`

### 4. LoRA 微调（可选）

```bash
python -m train.lora_train
```

冻结基础模型，仅训练 LoRA 低秩适配器。输出：`out/moxin-lora.pt`

### 5. VLM 预训练 → SFT

```bash
python -m train.vlm_pretrain    # 冻结 CLIP + LLM，仅训练 VisionProj
python -m train.vlm_sft         # 全参数微调
```

VLM 数据（Parquet）：`conversations`（JSON，`<image>` 标记图像位置）+ `image_bytes`

输出：`out/pretrain_vlm.pth` → `out/sft_vlm.pth`

### 6. VLA 训练

在 VLM SFT 权重基础上，冻结前 8 层 Transformer，训练 Action Expert + Feature Fusion + 后 4 层。

**数据准备：**

```bash
# Lift: 采集 500 条 scripted 示教
python -m envs.data_collector --task lift

# LIBERO-Spatial: 下载并转换官方示教 (含中文翻译)
python -m envs.data_collector --task libero_spatial --download
```

数据保存至 `dataset/data/{task}.hdf5`。

**训练：**

```bash
# Lift 单任务
python -m train.vla_train --task lift --proprio_drop_rate 0.0

# LIBERO-Spatial 多任务
python -m train.vla_train --task libero_spatial --epochs 25 --proprio_drop_rate 0.1
```

输出：`out/vla_{task}.pth` + `out/norm_stats_{task}.pt`（动作与本体感觉归一化统计量）

## 效果展示

### WebUI 对话

<p align="center">
  <img src="assets/demo_webui.gif" width="640">
</p>

### LLM 对话

> **user**: 你是谁？你叫什么名字？
>
> **moxin**: 您好，我是 moxin，由 mozihe 开发。我是 moxin，一个由 mozihe 开发的人工智能助手。

---

> **user**: 请用简洁的语言解释一下什么是Transformer架构。
>
> **moxin**: Transformer架构是一种基于自注意力机制的机器学习模型，它可以在大规模数据集上进行训练，以捕捉输入序列中的上下文信息，从而实现对文本、图像、音频等不同形式的信息的理解和处理。

---

> **user**: 用Python写一个快速排序算法。
>
> **moxin**: 快速排序是一种高效的排序算法，采用分治法策略。以下是使用Python实现的快速排序算法：
>
> ```python
> def quick_sort(arr):
>     if len(arr) <= 1:
>         return arr
>     pivot = arr[len(arr) // 2]
>     left = [x for x in arr if x < pivot]
>     middle = [x for x in arr if x == pivot]
>     right = [x for x in arr if x > pivot]
>     return quick_sort(left) + middle + quick_sort(right)
> ```
>
> 这段代码首先检查输入数组的长度，如果长度小于等于1，则直接返回数组。然后选择一个基准值（这里选择数组中间的元素），将数组分为三部分：小于基准值的元素、等于基准值的元素和大于基准值的元素。接着递归地对小于和大于基准值的元素进行快速排序，并将结果合并。

---

> **user**: 请推荐三本值得阅读的中国古典名著，并简要说明推荐理由。
>
> **moxin**: 推荐三本中国古典名著，它们不仅在文学艺术上有着极高的成就，而且在历史、哲学、社会学等多个领域都有着深远的影响。
>
> 1. **《红楼梦》**：作者曹雪芹，是中国古代小说的巅峰之作。这部小说以贾、王、史、薛四大家族的兴衰为背景，通过贾宝玉与林黛玉、薛宝钗的爱情故事，展现了封建社会的种种矛盾和人性的复杂。
>
> 2. **《西游记》**：作者吴承恩，讲述了唐僧师徒四人西天取经的传奇故事，融合了神话、宗教、历史、地理等多种元素，充满了奇幻色彩和深刻的寓意。
>
> 3. **《水浒传》**：作者施耐庵，讲述了宋江领导的一百零八位好汉在梁山泊聚义的故事，反映了当时社会的黑暗与人民的苦难。

---

> **user**: 如果地球停止自转会发生什么？
>
> **moxin**: 如果地球突然停止自转，将会发生一系列极其严重和灾难性的事件：
>
> 1. **极端温度变化**：地球的自转导致了日夜的交替。如果地球停止自转，极端的温度变化将非常剧烈，可能导致极地冰盖和高山冰川融化，引发海平面上升。
> 2. **生态系统崩溃**：极端的温度变化将导致生态系统的崩溃。许多物种将无法适应这种极端环境，导致物种灭绝。
> 3. **自然灾害**：如果地球停止自转，自然灾害的频率和强度可能会增加。
> 4. **人类社会的挑战**：人类社会将面临前所未有的挑战，包括食物、水和能源的获取。

---

> **user**: 春天来了，描写一下你眼中的春天。
>
> **moxin**: 春天，这个季节总是充满了生机与希望，它以它独有的方式，唤醒了沉睡的大地，带来了温暖的阳光、清新的空气和各种生命的活力。在春天，天空呈现出一种深邃而清澈的蓝色，偶尔飘过几朵白云，如同轻盈的羽毛。树木开始抽出嫩绿的新芽，花朵竞相开放，红的、黄的、紫的、白的，五彩斑斓，如同大自然的调色盘，将大地装扮得五彩斑斓。田野里，农民们忙碌着，播种希望，期待着秋天的丰收。

### VLM 图文对话

<table>
<tr>
<td width="160"><img src="assets/demo_vlm_0.jpg" width="160"></td>
<td>

**user**: 当这个人盯着苹果时，他可能在想些什么呢？

**moxin**: 当这个男人盯着苹果的时候，他可能在思考苹果的外观、味道和质地。他也许会考虑苹果的颜色、大小、形状、质地和整体外观，或者只是单纯地欣赏苹果的外观。此外，他还可能在思考苹果的新鲜度，因为这表明它已经准备好被食用了。

</td>
</tr>
</table>

<table>
<tr>
<td width="160"><img src="assets/demo_vlm_beach.jpg" width="160"></td>
<td>

**user**: 写一个详细的描述给定的图像。

**moxin**: 这幅图片描绘了一个美丽的海滩场景，人们在那里享受着阳光明媚的一天。可以看到许多人在海边散步、玩耍和放松。有些人站在水边，而其他人则坐在沙滩上。海滩上散布着几把遮阳伞，为游人提供遮阴和舒适。沙滩上还摆放着几把椅子，供人们休息和欣赏海景时使用。

</td>
</tr>
</table>

<table>
<tr>
<td width="160"><img src="assets/demo_vlm_2.jpg" width="160"></td>
<td>

**user**: 在这个滑板场景中可能会出现什么问题？

**moxin**: 在图中，一名男子正骑着滑板沿着金属栏杆滑行。这个场景中可能出现的问题是滑板运动员失去平衡而跌倒。由于滑板运动员正在表演特技，因此有可能失去控制而导致跌倒或受伤。为了避免这些问题，滑板运动员应该确保他们有足够的技能和经验来安全地完成这些特技动作，并且在尝试这些特技之前应该穿戴保护装备。

</td>
</tr>
</table>

<table>
<tr>
<td width="160"><img src="assets/demo_vlm_5.jpg" width="160"></td>
<td>

**user**: 在这样的环境下放个钟有什么用？

**moxin**: 在这样的环境下，时钟有很多用途。首先，它为路人提供了一个容易看到和阅读的时间参照物，使他们能够掌握时间并安排日常活动。其次，时钟可作为地标，帮助人们在城市中找到方向。此外，它还能成为一个装饰元素，提升整个空间的美感，营造出一种吸引人的气氛。

</td>
</tr>
</table>

<table>
<tr>
<td width="160"><img src="assets/demo_vlm_7.jpg" width="160"></td>
<td>

**user**: 现场发生了什么？

**moxin**: 图中是一个穿着尿布的小女孩，她坐在一堆毛绒玩具上。这些玩具包括泰迪熊和填充动物，它们被摆放在一起，占据了整个画面。女孩似乎正全神贯注地看着这些玩具，可能是在玩耍或看着它们。

</td>
</tr>
</table>

<table>
<tr>
<td width="160"><img src="assets/demo_vlm_8.jpg" width="160"></td>
<td>

**user**: 描述下列图像。

**moxin**: 图中是一张摆满各种食物和饮料的餐桌，桌上有几个碗、杯子和蛋糕。其中一个碗里盛着一束鲜花，为整个场景增添了一丝自然之美。除了食物和饮料，桌子上还摆放着一些餐具，如叉子、刀子和勺子等。桌上还放着一个花瓶，为餐桌增添了一丝优雅气息。在背景中，可以看到一个人，可能正在享受他们的食物或与他人交谈。

</td>
</tr>
</table>

### VLA 机器人操控

<table>
<tr>
<td width="340">
<img src="assets/vla_lift.gif" width="320">
</td>
<td width="340">
<img src="assets/vla_libero.gif" width="320">
</td>
</tr>
<tr>
<td align="center"><b>Lift — 单任务 (100%)</b></td>
<td align="center"><b>LIBERO-Spatial — 多任务 (70%)</b></td>
</tr>
</table>

## 评测与推理

### LLM 中文语言能力

```bash
python -m test.lang_bench --ckpt_name sft02.pth --show_responses
```

| 指标 | MoXin SFT (270M) |
|---|---|
| Perplexity ↓ | 147.36 |
| Avg Length | 138.7 |
| Distinct-1 ↑ | 0.492 |
| Distinct-2 ↑ | 0.864 |
| Distinct-3 ↑ | 0.943 |
| Repetition ↓ | 0.009 |
| Empty Rate ↓ | 0.0% |

### LLM C-Eval（52 科目）

```bash
python -m test.ceval_bench --ckpt_name sft02.pth
```

| 类别 | 正确 / 总数 | 准确率 |
|---|---|---|
| STEM | 96 / 393 | 24.4% |
| Social Science | 129 / 516 | 25.0% |
| Humanities | 29 / 117 | 24.8% |
| Other | 54 / 245 | 22.0% |
| **Overall** | **308 / 1271** | **24.2%** |

### VLM 图文理解

```bash
python -m test.vlm_bench --ckpt_name sft_vlm.pth --num_samples 50 --show_responses
```

| 指标 | 值 |
|---|---|
| CharOverlap ↑ | 0.410 |
| BLEU-1 ↑ | 0.305 |
| Avg Length | 120.6 |
| Distinct-1 ↑ | 0.274 |
| Distinct-2 ↑ | 0.714 |
| Distinct-3 ↑ | 0.872 |
| Repetition ↓ | 0.036 |
| Empty Rate ↓ | 0.0% |

### VLA 机器人操控

| 任务 | 参数量 | 训练数据 | 成功率 | GPU |
|---|---|---|---|---|
| **Lift** | ~292M | 500 demos | **100%** | 1× A100 |
| **LIBERO-Spatial** | ~292M | 50 demos/task × 10 | **70%** | 1× A100 |

**横向对比（LIBERO-Spatial）：**

| 模型 | 参数量 | 成功率 | 硬件 |
|---|---|---|---|
| **MoXin VLA** | **292M** | **70%** | **1× A100** |
| SmolVLA | 450M | 90% | 1× consumer GPU |
| OpenVLA | 7B | 96% | 8× A100 |
| π₀.₅ | 3B | 97% | 8× H100 |

VLA 推理参数：

| 参数 | 默认值 | 说明 |
|---|---|---|
| `--inference_steps` | 10 | ODE 积分步数，越大越精确越慢 |
| `--guidance_scale` | 1.5 | CFG 引导强度，多任务建议 1.5~2.0 |
| `--execute_horizon` | 4 | 每次重规划间执行的步数 |
| `--blend_decay` | 0.1 | Temporal ensemble 衰减率 |

### 推理命令

```bash
# LLM
python -m test.sft_test                                    # SFT 对话
python -m test.lora_test --lora_path out/moxin-lora.pt     # LoRA 对话

# VLM
python -m test.vlm_sft_test                                # VLM 看图对话
python -m webui.app --port 7860                            # WebUI

# VLA
python -m test.vla_test --task lift                        # 闭环评估
python -m test.vla_test --task libero_spatial
python -m test.vla_demo --task lift                        # 交互式可视化
python -m test.vla_demo --task libero_spatial --inference_steps 20 --guidance_scale 2.0
```

## 致谢

- [MiniMind](https://github.com/jingyaogong/minimind) — 项目灵感来源
- [OpenAI CLIP](https://github.com/openai/CLIP) — 视觉编码器
- [HuggingFace Transformers](https://github.com/huggingface/transformers) — Tokenizer 与模型基类
- [π₀ (Physical Intelligence)](https://www.physicalintelligence.company/blog/pi0) — VLA 架构参考
- [SmolVLA](https://huggingface.co/blog/smolvla) — 小参数量 VLA 实践参考
- [Robosuite](https://robosuite.ai/) — 机器人仿真平台
- [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO) — 多任务操控 benchmark
- [C-Eval](https://cevalbenchmark.com/) — 中文评测基准

## License

本项目采用 [MIT License](LICENSE) 开源。
