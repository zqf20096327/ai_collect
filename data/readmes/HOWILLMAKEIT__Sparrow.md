<div align="center">

# 麻雀 (Sparrow) - 轻量级大语言模型

麻雀虽小，五脏俱全。

![DeepSpeed](https://img.shields.io/badge/DeepSpeed-ZeRO%201%2F2%2F3-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange)
![MoE](https://img.shields.io/badge/Architecture-MoE-green)
![Model Size](https://img.shields.io/badge/Params-196M%20(%20106M%20active)-brightgreen)
![Training](https://img.shields.io/badge/Training-Pretrain--SFT--DPO-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

</div>

---

## 📑 目录

- [📌 项目简介](#-项目简介)
- [🌟 项目亮点](#-项目亮点)
- [🏗️ 模型架构](#️-模型架构)
- [🚀 快速开始](#-快速开始)
- [🔥 训练流程](#-训练流程)
  - [1. 预训练（Pretrain）](#1-预训练pretrain)
  - [2. 监督微调（SFT）](#2-监督微调sft)
  - [3. 强化学习对齐（DPO）](#3-强化学习对齐dpo)
  - [恢复训练](#恢复训练)
  - [DeepSpeed Checkpoint 转换](#deepspeed-checkpoint-转换)
- [📝 DPO 数据增强](#-dpo-数据增强)
- [📊 模型评测](#-模型评测)
- [🎓 训练技巧](#-训练技巧)
- [🔧 推理](#-推理)
- [📁 项目结构](#-项目结构)
- [📄 开源协议](#-开源协议)
- [🤝 贡献](#-贡献)

---

## 📌 项目简介

**麻雀 (Sparrow)** 是一个基于 [MiniMind](https://github.com/jingyaogong/minimind) 衍生而来的轻量级大语言模型实验项目。本项目旨在探索和实践大模型的完整训练流程，从预训练到强化学习对齐，全部采用原生 PyTorch 实现。

### 训练阶段与实测数据

| 阶段 | 设备配置 | Batch Size | 时间/Epoch | 总时间 | 显存占用 | 效果提升 |
|------|----------|------------|------------|--------|----------|----------|
| **Pretrain** | 单卡 RTX 4090 | 32 | ~100min | 2 epochs | ~18GB | 基准 |
| **SFT** | 3× RTX 2080Ti | 8 | ~580min | 2 epochs | ~7GB/卡 | - |
| **SFT** | 2× RTX 4090 | 32 | ~77min | 2 epochs | ~17GB/卡 | **+72.18%** ✅ |
| **DPO** | 2× RTX 4090 | 8 | ~5min | 1 epoch | ~16GB/卡 | -5.02% ⚠️ |

**性能对比**：双 4090 相比三卡 2080Ti，SFT 训练速度提升约 **7.5 倍**（每 epoch 77min vs 580min）。

### 实验内容

- **完整三阶段训练**：Pretrain → SFT → DPO，记录各阶段训练时间和资源消耗
- **DPO 数据合成探索**：实现基于 Reward Model 的自动化 DPO 数据生成与筛选方案
- **Reward Model 评测**：使用 Skywork-Reward-V2-Qwen3-8B 对各阶段模型进行量化评估


### 模型规格

- **架构**：Decoder-only Transformer + MoE（Mixture of Experts）
- **总参数**：~196M
- **激活参数**：~106M（4个专家，top-2路由）
- **位置编码**：RoPE（Rotary Position Embedding）
- **注意力机制**：GQA（Grouped Query Attention，8头查询/2头KV）


---

## 🌟 项目亮点

- **轻量级 MoE 架构**：总参数 196M，激活参数 106M（4个专家，top-2路由）
- **完整训练流程**：覆盖 Pretrain → SFT → DPO 全流程
- **原生实现**：所有算法均用 PyTorch 原生实现，无第三方框架封装
- **DeepSpeed 支持**：支持 DeepSpeed ZeRO-2 分布式训练，优化通信配置
- **自动化评测**：基于 **Skywork-Reward-V2-Qwen3-8B** 的自动化评测体系，量化模型对齐质量
- **数据增强探索**：实现基于 Reward Model 的 DPO 数据自动合成方法

---

## 🏗️ 模型架构

### 模型配置

| 配置项 | 值 |
|--------|-----|
| Hidden Size | 768 |
| Layers | 8 |
| Attention Heads | 8 |
| KV Heads (GQA) | 2 |
| Experts | 4 (top-2 路由) |
| 总参数 | ~196M |
| 激活参数 | ~106M |

### MoE 架构特点

- **4个专家**：每个token激活top-2专家
- **参数效率**：总参数196M，但每次前向传播只激活106M参数
- **负载均衡**：自动平衡专家使用频率，避免专家塌陷

---

## 🚀 快速开始

### 环境要求

```bash
# Python >= 3.10
# CUDA >= 12.1 (如果使用 GPU)
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 数据准备

从 [MiniMind 数据集](https://www.modelscope.cn/datasets/gongjy/minimind_dataset/files) 下载以下文件到 `dataset/` 目录：

```
dataset/
├── pretrain_t2t_mini.jsonl    # 预训练数据
├── sft_t2t_mini.jsonl         # SFT 数据
└── dpo.jsonl                   # DPO 数据
```

---

## 🔥 训练流程

### 选择训练模式

| 模式 | 适用场景 | 启动方式 |
|------|----------|----------|
| **单卡训练** | 只有一张显卡，或显存充足 | `python xxx.py` |
| **多卡数据并行** | 多张显卡，显存充足 | `torchrun --nproc_per_node=N` |
| **DeepSpeed** | 多张显卡，显存有限 | `torchrun --nproc_per_node=N --use_deepspeed 1` |

**说明**：以下命令假设系统有 2 张显卡。如果您只有 1 张显卡，请使用单卡训练命令；如果有更多显卡，请将 `--nproc_per_node=2` 修改为对应的显卡数量。

**指定显卡**：
```bash
# 使用特定显卡（如显卡1）
CUDA_VISIBLE_DEVICES=1 python trainer/train_full_sft.py ...

# 使用多张特定显卡（如显卡1和2）
CUDA_VISIBLE_DEVICES=1,2 torchrun --nproc_per_node=2 trainer/train_full_sft.py ...
```

### 1. 预训练（Pretrain）

**实测性能数据**：

| 设备配置 | Batch Size | 每Epoch时间 | 显存占用 |
|---------|-----------|------------|---------|
| 单卡 RTX 4090 | 32 | ~90分钟 | ~18GB |

**单卡训练**（单GPU用户）：
```bash
python trainer/train_pretrain.py \
    --hidden_size 768 \
    --num_hidden_layers 8 \
    --use_moe 1 \
    --epochs 2 \
    --max_seq_len 340 \
    --data_path dataset/pretrain_t2t_mini.jsonl \
    --dtype bfloat16 \
    --save_dir out \
    --save_weight pretrain
```

**多卡数据并行**（多GPU用户）：
```bash
torchrun --nproc_per_node=2 trainer/train_pretrain.py \
    --hidden_size 768 \
    --num_hidden_layers 8 \
    --use_moe 1 \
    --epochs 2 \
    --max_seq_len 340 \
    --data_path dataset/pretrain_t2t_mini.jsonl \
    --dtype bfloat16 \
    --save_dir out \
    --save_weight pretrain
```

**多卡 DeepSpeed**（显存不足时）：
```bash
torchrun --nproc_per_node=2 trainer/train_pretrain.py \
    --hidden_size 768 \
    --num_hidden_layers 8 \
    --use_moe 1 \
    --epochs 2 \
    --max_seq_len 340 \
    --data_path dataset/pretrain_t2t_mini.jsonl \
    --dtype bfloat16 \
    --use_deepspeed 1 \
    --zero_stage 2 \
    --save_dir out \
    --save_weight pretrain
```

### 2. 监督微调（SFT）

**实测性能数据**：

| 设备配置 | Batch Size | 每Epoch时间 | 显存占用 | DeepSpeed |
|---------|-----------|------------|---------|-----------|
| 3× RTX 2080Ti | 8 (每卡) | ~580分钟 | ~7GB/卡 | ZeRO-2 |
| 2× RTX 4090 | 32 (每卡) | ~77分钟 | ~17GB/卡 | ZeRO-2 |

**性能对比**：双4090相比三卡2080Ti，训练速度提升约 **7.5 倍**。

**单卡训练**（单GPU用户）：
```bash
python trainer/train_full_sft.py \
    --hidden_size 768 \
    --num_hidden_layers 8 \
    --use_moe 1 \
    --epochs 2 \
    --learning_rate 1e-5 \
    --data_path dataset/sft_t2t_mini.jsonl \
    --dtype bfloat16 \
    --save_dir out \
    --from_weight pretrain
```

**多卡数据并行**（多GPU用户）：
```bash
torchrun --nproc_per_node=2 trainer/train_full_sft.py \
    --hidden_size 768 \
    --num_hidden_layers 8 \
    --use_moe 1 \
    --epochs 2 \
    --batch_size 32 \
    --learning_rate 1e-5 \
    --data_path dataset/sft_t2t_mini.jsonl \
    --dtype bfloat16 \
    --save_dir out \
    --from_weight pretrain
```

**多卡 DeepSpeed**（显存不足时）：
```bash
torchrun --nproc_per_node=2 trainer/train_full_sft.py \
    --hidden_size 768 \
    --num_hidden_layers 8 \
    --use_moe 1 \
    --epochs 2 \
    --batch_size 32 \
    --learning_rate 1e-5 \
    --data_path dataset/sft_t2t_mini.jsonl \
    --dtype bfloat16 \
    --save_dir out \
    --use_deepspeed 1 \
    --zero_stage 2 \
    --from_weight pretrain
```

### 3. 强化学习对齐（DPO）

**实测性能数据**：

| 设备配置 | Batch Size | 每Epoch时间 | 显存占用 | DeepSpeed |
|---------|-----------|------------|---------|-----------|
| 2× RTX 4090 | 8 (每卡) | ~5分钟 | ~16GB/卡 | 不需要 |

**单卡训练**（单GPU用户）：
```bash
python trainer/train_dpo.py \
    --use_moe 1 \
    --data_path dataset/dpo.jsonl \
    --save_dir out \
    --from_weight full_sft
```

**多卡数据并行**（多GPU用户）：
```bash
torchrun --nproc_per_node=2 trainer/train_dpo.py \
    --use_moe 1 \
    --batch_size 8 \
    --data_path dataset/dpo.jsonl \
    --save_dir out \
    --from_weight full_sft
```

**多卡 DeepSpeed**（显存不足时）：
```bash
torchrun --nproc_per_node=2 trainer/train_dpo.py \
    --use_moe 1 \
    --batch_size 8 \
    --data_path dataset/dpo.jsonl \
    --save_dir out \
    --from_weight full_sft \
    --use_deepspeed 1 \
    --zero_stage 2
```

### 恢复训练

所有训练阶段都支持从 checkpoint 恢复：

```bash
# 预训练恢复
python trainer/train_pretrain.py --from_resume 1

# SFT 恢复
python trainer/train_full_sft.py --from_resume 1

# DPO 恢复
python trainer/train_dpo.py --from_resume 1
```

**说明**：`--from_resume 1` 会自动检测并从最新 checkpoint 恢复训练。

### DeepSpeed Checkpoint 转换

使用 DeepSpeed ZeRO 训练时，训练脚本会**自动将 checkpoint 转换为标准 PyTorch 权重文件**并保存到 `out/` 目录。

如果自动转换失败或需要手动转换，可以使用以下命令：

```bash
python zero_to_fp32.py \
    checkpoints/ds_ckpt_full_sft_768_moe \
    out/full_sft_768_moe_fp32.pth \
    fp32
```

**说明**：
- `zero_to_fp32.py` 脚本会在 DeepSpeed 训练时自动生成在 checkpoint 目录中
- 一般情况下不需要手动转换，训练脚本会自动处理
- 如果 `out/` 目录中没有生成 `.pth` 文件，再使用上述命令手动转换

---

## 📝 DPO 数据增强

本项目实现了一种基于Reward Model的DPO数据增强方法，通过生成多个候选答案并自动筛选最优解来提升数据集质量。

### 方法原理

参考论文：[What Matters for DPO? The Quality of Chosen Matters Most](https://arxiv.org/abs/2508.18312)

**核心思想**（来自论文）：

> **"The quality of chosen responses plays a dominant role in DPO performance, while the quality of rejected responses has a more limited impact."**

论文的关键发现：
1. **Chosen答案的质量起主导作用**：高质量的正样本能显著提升DPO性能
2. **Rejected答案质量影响有限**：即使负样本质量一般，对整体性能影响较小
3. **增加对比度的本质是提升Chosen质量**：单纯的对比不如直接提高正样本质量有效
4. **Online数据的混合效应**：在高质量离线数据中混入10%的online模型生成数据，能显著提升性能

基于这些发现，本项目实现了以下增强策略：

1. **候选生成**：使用SFT模型为每个问题生成多个候选答案（如8个）
2. **自动评分**：使用Reward Model对所有候选答案进行打分
3. **智能筛选**：选择评分最高的候选答案，如果高于原始chosen答案则替换

### 架构设计

采用**双GPU流水线并行**架构，充分利用硬件资源：

```
GPU0 (生成)          GPU1 (评分)
    ↓                    ↓
生成候选答案 → 队列 → Reward Model评分
    ↓                    ↓
8个候选           批量forward pass
                   (原始答案+候选)
```

**优化特性**：
- ✅ 真正的双GPU异步流水线并行
- ✅ 预处理所有prompt，避免重复tokenize
- ✅ 批量评分，减少forward pass次数
- ✅ Generator对象池（1024个预创建）
- ✅ TF32/cuDNN优化（409D原生支持）

### 使用方法

```bash
# 运行DPO数据增强脚本（需要双GPU）
python synthesize_dpo.py
```

**单GPU用户**：如果只有一张显卡，需要修改脚本：
```python
# 在 synthesize_dpo.py 中修改设备配置
gen_device, rm_device = "cuda:0", "cuda:0"  # 都改为cuda:0
```

或者分步运行（先生成，再评分）：
```bash
# 先生成候选答案
python synthesize_dpo.py --mode generate_only

# 再进行评分
python synthesize_dpo.py --mode score_only
```

### 实验结果

**实验配置**：
- 模型：Sparrow-768-MoE（~106M激活参数）
- Reward Model：Skywork-Reward-V2-Qwen3-8B
- 候选数量：8个/问题
- 测试样本：1716个（10%抽样）

**筛选示例**：

```
📝 问题:
   Please add punctuation to this: What it is all about or where we are going I cant be sure of But I know Id like to take the same journey

📚 数据集答案:
   What is it is all about, or where are we going? I can't be sure of. But I know, I'd like to take the same journey.
   ⭐ 评分: 6.0938

🤖 模型生成的8个候选答案:
   候选 #1 ✗ 较差 | 评分: -16.5000 (vs 原始: -22.5938)
   候选 #2 ✗ 较差 | 评分: -14.5625 (vs 原始: -20.6562)
   候选 #3 ✗ 较差 | 评分: -7.8750 (vs 原始: -13.9688)
   ... (所有候选评分均低于原始答案)

⏭️ 决策: 保留数据集原答案
```

**实验结论**：

受限于模型规模（~100M参数 vs 主流模型7B+），当前SFT模型生成的答案质量普遍低于原始数据集：

| 指标 | 结果 |
|------|------|
| 处理速度 | ~0.11 样本/秒（双4090 24GB） |
| 改进率 | ~1% (100样本中) |

**分析与展望**：

1. **方法有效性**：该合成方法在理论上是可行的，在大参数模型上已有成功案例
2. **模型限制**：小参数模型（<1B）在生成质量上难以超越人工标注的高质量数据
3. **改进方向**：
   - 使用更大规模的SFT模型（如7B+）
   - 增加候选数量（如16个或32个）
   - 结合多种生成策略（不同temperature、top_p等）
   - 引入人工校验环节

**代码位置**：`synthesize_dpo.py`

---

## 📊 模型评测

本项目提供了基于Reward Model的自动化评测脚本，用于量化模型在训练各阶段的对齐质量。

### 评测方法

使用 **Skywork-Reward-V2-Qwen3-8B** 作为Reward Model，对模型生成的回答进行自动评分，对比Pretrain、SFT、DPO各阶段的性能。

### 运行评测

```bash
# 运行评测（会自动下载Reward Model）
python eval_with_reward.py
```

**脚本功能**：
- 自动下载Reward Model（首次运行，约16GB）
- 评测Pretrain、SFT、DPO三个阶段的模型
- 使用100个覆盖多领域的评测问题
- 生成详细的评测报告（JSON格式）

**输出内容**：
```json
{
  "num_questions": 100,
  "models": {
    "Pretrain": {"avg_score": -2.3456, "total_score": -234.56},
    "SFT": {"avg_score": 1.2345, "total_score": 123.45},
    "DPO": {"avg_score": 2.4567, "total_score": 245.67}
  },
  "summary": {
    "sft_vs_pretrain_improvement": "+152.67%",
    "dpo_vs_sft_improvement": "+99.02%"
  }
}
```

**单卡用户注意事项**：

如果只有一张显卡，需要修改脚本使用单GPU：

1. **修改设备配置**：
```python
# 在 eval_with_reward.py 中修改
REWARD_DEVICE = "cuda:0"  # 改为cuda:0
```

2. **或者分步评测**（显存不足时）：
```bash
# 先评测Pretrain
python eval_with_reward.py --model pretrain

# 再评测SFT（需要先注释掉Pretrain部分）
# ... 手动修改脚本中的models_to_eval列表
```

**查看结果**：
```bash
cat eval_results.json
```

### 评测问题集

评测问题包含100个精心设计的问题，覆盖以下10个领域：

1. **模型认知**（1-10）：自我介绍、能力范围、局限性等
2. **AI概念**（11-20）：人工智能、机器学习、深度学习等基础知识
3. **编程能力**（21-30）：算法实现、数据结构、设计模式等
4. **科学知识**（31-40）：生物、物理、化学等基础科学
5. **常识问答**（41-50）：日常生活、地理、基础事实等
6. **生活建议**（51-60）：学习方法、健康、时间管理等
7. **语言表达**（61-70）：英语理解、描述能力、写作等
8. **翻译能力**（71-80）：中英互译，覆盖日常用语
9. **文学知识**（81-90）：中外文学作品、文学流派等
10. **健康常识**（91-100）：疾病预防、健康生活等

完整问题列表见 [eval_questions.txt](eval_questions.txt)。

### 实测评档结果

**评测配置**：
- Reward Model：Skywork-Reward-V2-Qwen3-8B
- 评测问题：101个（覆盖多领域）
- 评测时间：2024年4月9日

**评测结果**：

| 模型阶段 | 平均分 | 总分 | 相对变化 |
|---------|--------|------|----------|
| **Pretrain** | -15.75 | -1590.52 | 基准 |
| **SFT** | -4.38 | -442.52 | **+72.18%** ✅ |
| **DPO** | -4.60 | -464.43 | **-5.02%** ⚠️ |

**结果分析**：

1. **SFT 显著提升模型质量**：从 Pretrain 到 SFT，评分提升 **72.18%**
   - Pretrain 模型只能完成基础的文本续写
   - SFT 模型学会了指令跟随，能够生成符合要求的回答

2. **DPO 后性能略有下降**：从 SFT 到 DPO，评分下降 **5.02%**

   这可能是**小模型的参数空间限制**导致的：DPO 在强行降低 rejected 样本概率时，会误伤周围相似的 token，使模型失去解题多样性。


---

## 🎓 训练技巧

### 混合精度训练

推荐使用 `bfloat16` 进行训练（A100/RTX 3090/4090）：

```bash
python train_full_sft.py \
    --dtype bfloat16 \
    ...
```

对于不支持 bfloat16 的硬件（如 RTX 2080），使用 `float32`：

```bash
python train_full_sft.py \
    --dtype float32 \
    ...
```

### 梯度累积

如果显存不足以使用大 batch size，可以使用梯度累积：

```bash
python train_full_sft.py \
    --batch_size 8 \
    --accumulation_steps 4 \
    ...
```

### 断点续训

所有训练脚本都支持自动断点续训：

```bash
python train_full_sft.py --from_resume 1
```

训练会自动从最新的 checkpoint 恢复。

---

## 🔧 推理

### 命令行推理

```bash
python eval_llm.py --weight full_sft
```

### 推理性能优化

**KV Cache 加速**：

| 模式 | 生成速度 | 加速比 |
|------|----------|--------|
| 不使用 KV Cache | 4.59 tokens/s | 基准 |
| 使用 KV Cache | 167.50 tokens/s | **36.5x** ⚡ |

**什么是 KV Cache？**

LLM 推理分为两个阶段：

1. **Prefill（处理阶段）**：一次性处理输入 prompt，计算所有 token 的 Key/Value 并缓存
2. **Decode（生成阶段）**：逐个生成输出 token，每次只需计算新 token 的 Key/Value，历史 KV 直接复用

**加速原理**：

```
# 不使用 KV Cache
Token 1: 计算 attention [1]                              → 1 个 token
Token 2: 计算 attention [1, 2]                          → 2 个 token
Token 3: 计算 attention [1, 2, 3]                       → 3 个 token
...
Token N: 计算 attention [1, 2, ..., N]                  → N 个 token
总计：O(N²) 次计算

# 使用 KV Cache
Prefill:  计算 attention [1, 2, ..., L]，缓存所有 KV    → L 个 token（输入长度）
Decode 1: 计算 attention [新1] + 复用缓存               → 1 个 token
Decode 2: 计算 attention [新2] + 复用缓存               → 1 个 token
...
Decode N: 计算 attention [新N] + 复用缓存               → 1 个 token
总计：O(L) + O(N) 次计算
```

**效果**：生成长度越长，加速越明显。实测 **36.5 倍** 加速（167.5 vs 4.59 tokens/s）。

---

## 📁 项目结构

```
minimind/
├── model/                 # 模型架构
│   └── model.py           # Sparrow 模型定义
├── trainer/               # 训练脚本
│   ├── train_pretrain.py  # 预训练
│   ├── train_full_sft.py  # SFT
│   ├── train_dpo.py       # DPO
│   └── trainer_utils.py   # 训练工具函数
├── dataset/               # 数据集
│   └── lm_dataset.py      # 数据加载器
├── eval_llm.py            # 模型评测脚本
├── eval_with_reward.py    # Reward Model 评测
├── synthesize_dpo.py      # DPO 数据合成
├── checkpoints/           # checkpoint 保存目录
└── out/                   # 最终模型输出
```

---

## 📄 开源协议

本项目采用 [Apache License 2.0](LICENSE) 开源协议。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

<div align="center">

**再次感谢 [MiniMind](https://github.com/jingyaogong/minimind) 项目的开源！**

Made with ❤️ by HOWILLMAKEIT

</div>
