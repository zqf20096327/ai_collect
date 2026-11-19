<h1 align="center"><img src="docs/images/tinybrain.svg" alt="tinybrain" width="100%"></h1>

[![License: MIT](https://img.shields.io/badge/license-MIT-2140d6)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-2140d6)](pyproject.toml)
[![PyTorch 2.5+](https://img.shields.io/badge/PyTorch-2.5%2B-e9482b)](https://pytorch.org)
[![数据集 ModelScope](https://img.shields.io/badge/%E6%95%B0%E6%8D%AE%E9%9B%86-ModelScope-ffd21f)](https://www.modelscope.cn/datasets/caiwangzsnm/tinybrain-dataset)
[![视频 B 站](https://img.shields.io/badge/%E8%A7%86%E9%A2%91-B%20%E7%AB%99-fb7299)](https://www.bilibili.com/video/BV1kqsj6EEtT/)
[![模型 Chat RC1](https://img.shields.io/badge/ModelScope-Chat%20RC1-15965a)](#现状)
[![GitHub stars](https://img.shields.io/github/stars/logitcai/tinybrain?color=15965a)](https://github.com/logitcai/tinybrain/stargazers)

**从一个字开始，自己做一个中文大模型。**

60B token 开源中文数据 · 自己训的分词器 · 预训练到强化学习的全流程 · 专门为古文和诗词练过

[English](README.en.md) · [视频介绍（B 站）](https://www.bilibili.com/video/BV1kqsj6EEtT/) · [数据集（ModelScope）](https://www.modelscope.cn/datasets/caiwangzsnm/tinybrain-dataset)

tinybrain 是一个从零写起的中文小模型项目。和 [MiniMind](https://github.com/jingyaogong/minimind)、[nanochat](https://github.com/karpathy/nanochat) 一样，所有代码都是自己写的、能一行行读懂；不一样的是：

- **数据也从零做**：从 26 个公开来源下载、清洗、跨来源去重、按配比和质量分成四档（1B / 5B / 20B / 60B token），这套数据叫 **tinybrain dataset**，做数据的每一步代码都在 `dataset/` 里。
- **结构用新东西**：多流残差（mHC）、Engram 查表记忆、3:1 的滑动窗口注意力、可选的混合专家（MoE），优化器是 Muon。
- **后训练做全套**：SFT → 领域专家 → 多老师在线蒸馏（MOPD）→ 强化学习（RLVR、agent RL、RLAIF），10 种题型、各自的判分器。
- **以中文为主**：分词器、数据配比、评分细则都按中文定，另外专门放了古文、诗词、鲁迅全集。

## 现状

2026 年 11 月 19 日发布了 Small 和 Medium 的首批中文对话研究权重。两个模型都经过预训练、余弦退火、监督微调、专家蒸馏和强化学习，发布包使用 FP32 safetensors，并附带匹配的 TinyBrain 运行时。

| ModelScope 权重 | 参数量 | 权重文件大小 | 可用回答数 / 采样数 |
| --- | ---: | ---: | ---: |
| [Small Chat RC1](https://www.modelscope.cn/models/caiwangzsnm/TinyBrain-Small-Chat-20261119-RC1) | 1.67 亿 | 639 MiB | 13/180 |
| [Medium Chat RC1](https://www.modelscope.cn/models/caiwangzsnm/TinyBrain-Medium-Chat-20261119-RC1) | 4.99 亿 | 1.86 GiB | 29/180 |

两个模型回答同一组 90 道开发题，每题采样两次，温度为 1.0，随机种子相同。Qwen3.8-27B-FP8 对照参考答案逐条评分。

实际聊天仍有明显局限。Medium 在另一组 10 段三轮对话中，30 次都正常结束，达到 8/10 的回答为 0 次。例如问「50 元买 6 张 7 元的海报还剩多少」，它先算出了 42 元总价，最后却答 12 元。独立终评尚未完成。

### 直接试用 Small

需要 Python 3.11 或更高版本。以下命令下载 Small、安装配套运行时并打开交互式对话。

```bash
python -m pip install modelscope
modelscope download --model caiwangzsnm/TinyBrain-Small-Chat-20261119-RC1 --local_dir ./tinybrain-small
python -m pip install ./tinybrain-small/tinybrain-0.1.0-py3-none-any.whl safetensors
tinybrain chat ./tinybrain-small --device auto
```

Medium 的模型页提供对应命令。想从头训练，可以从下面的[快速开始](#快速开始)进入。

11 月 16 日的预训练记录中，Medium 在约 61 亿 token 时验证损失为 2.50，Small 在约 74 亿 token 时为 2.76。

---

## 目录

- [现状](#现状)
- [要花多少](#要花多少)
- [快速开始](#快速开始)
- [完整训一遍 small](#完整训一遍-small)
- [聊天网页](#聊天网页)
- [代码结构](#代码结构)
- [模型](#模型)
- [分词器](#分词器)
- [数据集：tinybrain dataset](#数据集tinybrain-dataset)
- [预训练](#预训练)
- [后训练](#后训练)
- [N 卡训练：加速、Windows、监控](#n-卡训练加速windows监控)
- [评测](#评测)
- [推理](#推理)
- [演示结果](#演示结果)
- [还没做的](#还没做的)
- [联系与赞助](#联系与赞助)
- [许可证](#许可证)
- [参考](#参考)

---

## 要花多少

| 硬件 | 模型 | 数据 | 预训练一遍 |
|---|---|---|---|
| RTX 5070 Ti 16GB | small（主干 6400 万参数，连词向量和记忆表共 1.67 亿） | nano（10 亿 token） | 约 4 小时 |
| RTX 5070 Ti 16GB | small | mini（50 亿 token） | 约 20 小时 |
| RTX 5070 Ti 16GB | small | base（202 亿 token） | 约 3.4 天 |
| M4 Max | 演示模型（2300 万参数） | 9000 万 token，加上整套后训练 | 共 198 分钟 |

5070 Ti 这几行是按实测的速度换算的：16 × 2048、约 7 万 token/秒（0.46–0.47 秒一步），显存峰值约 12.5 GiB，设置见[N 卡训练](#n-卡训练加速windows监控)。
后训练的时间还没在显卡上量过。

---

## 快速开始

**第 0 步：装好**

```bash
git clone https://github.com/logitcai/tinybrain && cd tinybrain
pip install -e ".[data]"          # 要 Python 3.11+、PyTorch 2.5+（用 PyTorch 自带的 Muon 要 2.9+）；装完就有 tinybrain 命令
pip install -e ".[cuda,fast]"     # 可选：N 卡训练加速（Liger）、快一个数量级的切词（gigatoken）；Windows 先看「N 卡训练」一节
```

**第 1 步：下数据**（[ModelScope](https://www.modelscope.cn/datasets/caiwangzsnm/tinybrain-dataset)）

```bash
modelscope download --dataset caiwangzsnm/tinybrain-dataset pretrain_nano.parquet posttrain/sft_small.parquet --local_dir data
mv data/posttrain/* data/
```

也可以自己从头做：`tinybrain data --check` 先看每一步要什么，再 `tinybrain data`。

**第 2 步：训练**。不用写路径：每个阶段写到 `out/small/<阶段>/`，下一个阶段自动从上一个阶段的存档出发；parquet 第一次用时自动切词。

```bash
tinybrain pretrain        # 预训练：data/pretrain_nano.parquet → out/small/pretrain
tinybrain sft             # SFT：data/sft_small.parquet，从上一步出发 → out/small/sft
```

**第 3 步：看效果**

```bash
tinybrain generate        # 预训练完：续写几个内置的开头
tinybrain chat --demo     # SFT 完：把内置的 8 个问题挨个问一遍
tinybrain chat            # 自己聊（--tools 打开计算器和 Python）
tinybrain serve           # 聊天网页：浏览器打开 http://127.0.0.1:8001/
```

- 换更大的数据：`--data data/pretrain_mini.parquet`；换尺寸：`--preset medium`（写到 `out/medium/`）。
- 显存不够：`--batch-size 8 --grad-accum 2`，等效的批大小不变；中断了加 `--resume` 接着跑。
- 日志每行都有损失、梯度范数、速度和剩余时间；想看曲线用 `tinybrain tensorboard`（见「N 卡训练」一节）。
- small 从预训练到评测按顺序怎么跑、要开几个终端，见[完整训一遍 small](#完整训一遍-small)；每个阶段的原理见[后训练](#后训练)。
- 只想看整条链能不能跑：`tinybrain demo` 在一个 2300 万参数的小模型上把所有阶段跑一遍（M4 Max 上约 3.3 小时）。
- 没装成命令也没关系：`tinybrain pretrain` 就是 `python -m training.train_pretrain`，每个命令对应的模块见 `tools/cli.py`。

**全部命令**（`tinybrain <命令> --help` 看全部参数）

```
tinybrain data         做数据：下载、清洗、去重分档、SFT 语料、RL 题目（--check 先看缺什么）
tinybrain prepare      切词；训练时给 parquet 会自动切，一般不用单独跑
tinybrain tokenizer    抽样本、训练、评测分词器，导出 HF 格式
tinybrain pretrain     预训练，也用来退火
tinybrain sft          SFT：通用和领域专家
tinybrain distill      MOPD：多老师在线蒸馏
tinybrain rl           强化学习（GRPO）：RLVR、agent RL、RLAIF
tinybrain generate     续写：看预训练模型学到了什么
tinybrain chat         命令行对话（--demo 把内置的问题问一遍）
tinybrain serve        聊天网页和 OpenAI 兼容的服务
tinybrain eval         评测：留出集损失、各题型正确率、评审打分
tinybrain benchmarks   C-Eval、CMMLU、GSM8K
tinybrain bench        测这张卡的训练速度和显存
tinybrain report       参数量报告
tinybrain overfit      过拟合检查：在一小批数据上把损失训到接近 0
tinybrain diagnose     诊断：生成重复、和损失对不上时，分清是数据、计算路径还是训练不够
tinybrain demo         在一个 2300 万参数的小模型上把整条链跑一遍
tinybrain tensorboard  把训练日志同步成 TensorBoard
tinybrain judge-check  检查评审模型打分靠不靠谱
```

---

## 完整训一遍 small

快速开始只跑了预训练和 SFT。下面是 small 的整条链：预训练 → 退火 → SFT → 强化学习 → 评测，按一张 RTX 5070 Ti 16GB 写。

**要开几个终端**

| 终端 | 跑什么 | 什么时候要开 |
|---|---|---|
| 1 | 主线：下面的命令按顺序一条条跑 | 一直 |
| 2 | 评审模型（给 RLAIF 和评测打分） | 第 4、5 步 |
| 3（可选） | `tinybrain tensorboard` 看曲线 | 想看的时候 |

**终端 1：主线**

```bash
# 0. 下数据
modelscope download --dataset caiwangzsnm/tinybrain-dataset pretrain_mini.parquet \
    posttrain/sft_small.parquet posttrain/rl_small.parquet posttrain/eval_tasks.parquet --local_dir data
mv data/posttrain/* data/
tinybrain benchmarks prepare      # 下载 C-Eval、CMMLU、GSM8K，只在本地评测用

# 1. 预训练：mini 档 50 亿词 → out/small/pretrain                    5070 Ti 上约 20 小时
tinybrain pretrain --data data/pretrain_mini.parquet

# 2. 退火 → out/small/anneal                                          约 2 小时
#    先把 SFT 语料切成「整段都算损失」的对话数据，再用九成预训练数据 + 一成对话数据训 0.1 轮
tinybrain prepare --chat --train-on all --input data/sft_small.parquet --out data/tokens/chat-all
tinybrain pretrain --init out/small/pretrain/ckpt.pt --data data/pretrain_mini.parquet:0.9,data/tokens/chat-all:0.1 \
    --epochs 0.1 --warmup-steps 0 --lr-mult 0.1 --final-lr-frac 0

# 3. SFT：从退火出发 → out/small/sft
tinybrain sft

# 4. 强化学习：agent RL + RLAIF，从 SFT 出发 → out/small/rl（先把终端 2 开起来）
tinybrain rl --judge-url http://<评审机地址>:8080/v1 --judge-workers 1 --judge-timeout 600

# 5. 评测：留出题 + C-Eval、CMMLU、GSM8K
tinybrain eval out/small/rl/ckpt.pt --tasks data/eval_tasks.parquet --bench ceval cmmlu gsm8k \
    --judge-url http://<评审机地址>:8080/v1 --judge-workers 1
```

第 3 到 5 步的时间还没在显卡上量过。每个阶段跑完都可以先看看效果：预训练和退火之后用 `tinybrain generate`，SFT 之后用 `tinybrain chat --demo`。

**终端 2：评审模型**

评审模型是 Qwen3.8-27B，16GB 的显卡装不下，要放在另一台机器上，终端 1 通过局域网访问它：

- **Apple 芯片的 Mac**（内存 32GB 以上）：4-bit 版约占 15GB。它一次只算一个请求，所以终端 1 里用 `--judge-workers 1`。`--host 0.0.0.0` 会让局域网里的其他机器都能访问，只在自己的网络里这样开。

  ```bash
  pip install mlx-lm
  python -m mlx_lm.server --model mlx-community/Qwen3.8-27B-4bit --host 0.0.0.0 --port 8080
  ```

- **40GB 以上的显卡**：用 vLLM 跑 FP8 版，能同时处理很多请求，终端 1 里的 `--judge-workers 1` 可以去掉（默认 16）。

**已经有预训练存档**

跳过第 1 步，从第 2 步开始：把 `--init` 换成你的存档，`--data` 里的预训练数据换成你预训练时用的那份。`--epochs 0.1` 是按整份数据算的，base 档就是 20 亿词；嫌长可以改成 `--steps 10000`（每步 16 × 2048 词，共约 3.3 亿词，5070 Ti 上一个多小时）。

---

## 聊天网页

```bash
tinybrain serve                                           # 用 out/small 里走得最远的存档
tinybrain serve out/medium/pretrain/ckpt.pt --port 8001   # 指定存档；浏览器打开 http://127.0.0.1:8001/
```

![聊天网页：2300 万参数演示模型的续写](docs/images/chat-demo.png)

<sub>截图里是 2300 万参数的演示模型，只为展示页面；这个尺寸只会复读。</sub>

- **续写**：写一个开头，模型接着往下写（黑字是你写的，蓝字是模型写的）。预训练、退火的存档还没学过对话，只能这样用，网页会默认打开续写，并在顶上说明。
- **对话**：多轮对话，前面说过的话会一起发给模型。SFT 之后的存档默认打开对话。
- 边生成边显示，可以随时停止；左边能调温度、候选词个数和最多写多少词，下面写着这次写了多少词、每秒多少词。
- 网页不加载任何外部资源，本机离线也能用。服务默认只在本机（127.0.0.1）上开，要让别的机器访问，加 `--host 0.0.0.0`。

---

## 代码结构

```
lm/                    模型的定义，只有模型（一个文件一个概念）
  config.py              所有尺寸和开关；small / medium / large 三档预设
  model.py               整个模型的组装和前向
  layers/
    attention.py           分组查询注意力 + QK 归一化 + 旋转位置编码 + 滑动窗口
    feedforward.py         ReLU² 前馈层
    moe.py                 混合专家（共享专家、sqrt(softplus) 打分、偏置均衡、可选 LatentMoE）
    hyper.py               多流残差连接（mHC，静态）
    engram.py              Engram：按 2、3 元词组查表的记忆
    streams.py             多条流的入口和出口（用注意力）
    block.py               一层 = 记忆注入 + 注意力 + 前馈
    norm.py / rotary.py    归一化、位置编码
  loss.py                输出层加交叉熵（CUDA 上用 Liger 的融合内核，否则分块算；不会塌缩的写法）
  checkpointing.py       逐层激活重计算
training/              训练；每个阶段一个脚本，从头读到尾就是这个阶段的全部，参数都在文件末尾的 parse_args 里
  train_pretrain.py      预训练（也用于退火：--init 从存档出发，--data 按比例混合几份数据；--schedule wsd、--cooldown-from 分支退火）
  train_sft.py           SFT：只在回答上算损失（通用 SFT 和领域专家都用它）
  train_distill.py       MOPD：多老师在线蒸馏，按领域路由到老师
  train_rl.py            GRPO（Dr. GRPO）：RLVR、agent RL、RLAIF 共用
  trainer_utils.py       共用的：设备和混合精度、学习率曲线、优化器、梯度裁剪、存档、运行目录（各阶段之间怎么衔接）
  cuda_graph.py          可选：把优化器的更新录成 CUDA graph
  dataset.py             训练数据的读写（预训练的长串、打包好的对话、按比例混合）
  muon.py                自己写的 Muon（另一条路径是 PyTorch 自带的，--optimizer native）
  rollout.py             采样一组回答、带工具的多轮对话
  rewards/               判分：数学、代码（沙箱）、选择题、阅读、填空、指令跟随、逻辑题、诗词格律、评审模型、工具环境
inference/             推理：分词器、对话格式、生成（CUDA 上走静态缓存 + CUDA graph）、命令行对话、OpenAI 兼容服务
eval/                  评测：留出集损失、题目正确率、评审打分、C-Eval / CMMLU / GSM8K
dataset/               数据流水线（tinybrain dataset）
  sources.py             所有来源一张表：出自哪里、许可证、怎么下载、怎么取正文
  download.py            下载原始数据
  clean.py               单篇文档的清洗规则（含切书）
  pretrain.py            按来源批量清洗预训练数据
  mix.py                 去重、配比、分四档写出、检查、生成数据集说明
  sft.py                 SFT 语料
  rl.py                  RL 题目、评测题、MOPD 提示
  build.py               总入口：按顺序跑各步，开跑前检查输入
tools/                 辅助工具：tinybrain 命令（cli.py）、参数量报告、测速、训练分词器、切词、过拟合检查、整条链演示、评审模型检查、TensorBoard 同步
tokenizer/             正式分词器（tokenizer.model、tokenizer.vocab；tokenizer.json 是逐词一致的 HF 格式，给 gigatoken 用）
docs/                  设计文档：post-training.md（后训练流程）、rlaif-rubric.md（评审的评分细则）
data/                  数据（不进仓库）：raw 原始下载、clean 洗好的、inputs 后训练原料、*.parquet 成品、tokens/ 切好的词
out/                   训练输出（不进仓库）：out/<尺寸>/<阶段>/ 下有 ckpt.pt、log.jsonl、config.json
```

---

## 模型

### 总览

```
词编号 ─┬─ 词向量 ────────────────┐
        └─ Engram 查表 ─┬─ 二元记忆 ┤  三份「来源」
                        └─ 三元记忆 ┘
                               │ 入口：每条流用注意力挑自己要的来源
                               ▼
                     n=4 条残差流 (B, T, 4, d)
                               │
        ┌──────── 第 i 层（重复 L 次）─────────┐
        │  [第 1、中间层] Engram 门控注入        │
        │  读(pre) → RMSNorm → 注意力 → 写(post)，流之间按 res 混合 │
        │  读(pre) → RMSNorm → 前馈/MoE → 写(post)，流之间按 res 混合 │
        └──────────────────────────────────────┘
                               │ 出口：注意力把 4 条流合成一条
                               ▼
                     RMSNorm → 输出层（和词向量不共享）→ logits
```

### 多流残差（mHC）

普通残差只有一条流：$`x \leftarrow x + F(x)`$。tinybrain 把残差拓宽成 $`n=4`$ 条流 $`X \in \mathbb{R}^{n \times d}`$，每个子层（注意力、前馈各算一个）有三组可学的系数：

```math
X \leftarrow H^{\text{res}} X + h^{\text{post}} \otimes F\!\left(\textstyle\sum_{s} h^{\text{pre}}_s X_s\right)
```

- **读** $`h^{\text{pre}} = \sigma(\cdot) \in (0,1)^n`$：把 4 条流加权合成这个子层的输入；
- **写** $`h^{\text{post}} = 2\sigma(\cdot) \in (0,2)^n`$：子层的输出按多大比例加回每条流；
- **混** $`H^{\text{res}} \in \mathbb{R}^{n\times n}`$：流和流之间互相搬运。它被约束成**双随机矩阵**（每行每列和为 1），所以信号总量在层与层之间不会被放大或缩小——这是 mHC 相对原始 Hyper-Connections 的改进，解决了深层训练不稳。

双随机用 Sinkhorn 迭代得到：对 $`\exp(\text{logits})`$ 交替按列、按行归一，在对数域里做 20 次：

```math
\log M \leftarrow \log M - \mathrm{logsumexp}_{\text{行}}(\log M),\qquad \log M \leftarrow \log M - \mathrm{logsumexp}_{\text{列}}(\log M)
```

这里用的是**静态**版：系数不看输入，整个模型所有子层的系数放在一起一次算完，几乎不花时间。初始化让它等价于普通残差（$`H^{\text{res}} \approx I`$，第 $`s`$ 个子层主要读第 $`s \bmod n`$ 条流）。代码：`lm/layers/hyper.py`。

### Engram：查表记忆

很多知识是「看到这几个字就该想起什么」，用矩阵乘去算有点浪费。Engram 直接按「前 $`n-1`$ 个词 + 当前词」查表：对阶数 $`n \in \{2, 3\}`$、每个哈希头 $`h`$（8 个），

```math
\text{row}_{n,h}(p) = \Big(\bigoplus_{j=0}^{n-1} t_{p-j}\cdot m_{n,h,j}\Big) \bmod P_{n,h} + \text{offset}_{n,h}
```

$`t_{p-j}`$ 是往前第 $`j`$ 个词的编号，$`m`$ 是固定的随机奇数乘数，$`\oplus`$ 是按位异或，$`P_{n,h}`$ 是互不相同的质数（不同哈希头的碰撞不会成对出现）。每个位置取回 $`2 \times 8`$ 行、每行宽 32（small）的向量，拼起来、归一化。

取回的记忆用两次：

1. **入口**：每个阶数投影成一份 $`d`$ 维的「来源」，和词向量一起交给流入口；
2. **门控注入**：在第 1 层（medium、large 再加中间一层）之前，每条流拿自己当前的状态和记忆的「键」比一比，决定收多少：

```math
g_s = \sigma\!\left(\frac{\langle \text{RMSNorm}(X_s),\ \text{RMSNorm}(K_s\,e)\rangle}{\sqrt{d}}\right),\qquad X_s \leftarrow X_s + g_s \cdot V e
```

记忆表查一次只取十几行，**不花算力，只占显存**。所以记忆表都做得很大：small、medium 占「主干 + 记忆表」参数的 45%（`ENGRAM_SHARE`）；large 是 MoE，按 Engram 论文的最优点，占「每个词用不到的参数」的 25%（`ENGRAM_SPARSE_SHARE`）。代码：`lm/layers/engram.py`。

### 流的入口和出口

- **入口**：一个位置有三份来源（词向量、二元记忆、三元记忆）。每条流 $`m`$ 有一个自己的查询向量 $`q_m`$，对来源打分、加权求和：$`X_m = \sum_s \mathrm{softmax}_s\!\big(q_m^\top k_s / \sqrt{d_k}\big)\, \text{src}_s`$。不同的流可以偏好不同的来源。
- **出口**：一个可学的查询向量对 4 条流打分、加权合成一份。查询从零开始，所以一开始就是 4 条流的平均。

代码：`lm/layers/streams.py`。

### 注意力

- **分组查询注意力（GQA）**：small 有 12 个查询头、3 组键值头，键值缓存小到四分之一；
- **QK 归一化**：查询和键先过 RMSNorm 再做点积，训练更稳；
- **旋转位置编码（RoPE）**，底数 10000，上下文 8192；
- **滑动窗口 3:1**：每 4 层里前 3 层只看最近 1024 个词，第 4 层（以及最后一层）看全文。CUDA 上用 FlexAttention：窗口和因果写成一条掩码规则，编成块稀疏的掩码，只算窗口里的那条带子，计算量从 $`T^2`$ 降到约 $`WT`$，原生支持分组查询；CPU、MPS 上用带掩码的 scaled_dot_product_attention，结果一样。

代码：`lm/layers/attention.py`。

### 前馈和混合专家

普通前馈层用 ReLU²：$`\text{FFN}(x) = W_2\,\text{ReLU}(W_1 x)^2`$，中间宽度 4d。

large 档换成混合专家：第 1 层仍是普通前馈；其余各层是 2 个**共享专家**（和路由专家同宽，合起来就是一个半宽的前馈层），加上从 48 个四分之一宽的路由专家里选 8 个。按宽度算，每个词用到全部专家的 20%：

```math
s = \sqrt{\mathrm{softplus}(W_r z)},\qquad \mathcal{K} = \mathrm{top\text{-}k}(s + b),\qquad y = \text{FFN}_{\text{shared}}(x) + \sum_{e \in \mathcal{K}} \frac{s_e}{\sum_{e' \in \mathcal{K}} s_{e'}}\,\text{FFN}_e(z)
```

负载均衡有两层：
- **偏置均衡**（不参与求导）：每个专家有一个偏置 $`b_e`$，只在「挑谁」时加上。每步按实际负载调整：$`b_e \leftarrow b_e + \gamma \cdot \mathrm{sign}(1/E - \text{load}_e)`$，$`\gamma = 10^{-3}`$。活儿多的专家偏置降一点，下次就少被挑。
- **很轻的均衡损失**：$`\mathcal{L}_{\text{bal}} = E \sum_e \text{load}_e \cdot \text{share}_e`$，权重 $`10^{-4}`$。$`\text{load}_e`$ 是专家实际接了多大比例的词，$`\text{share}_e`$ 是它平均拿到多大比例的分数。

可选 LatentMoE：先把输入压到更窄的宽度，路由和专家都在压缩后的空间里算，最后再升回来。代码：`lm/layers/moe.py`。

**为什么这么配**（对照了 20 个公开 MoE 的配置）：2024 年以后的 MoE 激活比例几乎都在 12.5% 以下，和我们尺寸接近的小 MoE 用 32–64 个专家（Granite-1B 是 32 选 8、OLMoE 是 64 选 8）；专家宽度多是模型宽度的 0.25–0.5 倍；DeepSeek、Kimi、GLM、Moonlight 让第 1 层保持普通前馈、配一两个窄的共享专家（Qwen3、OLMoE、Granite 不用共享专家，这一点没有共识）。蚂蚁的效率杠杆论文给出的最优粒度 $`2d/w`$ 在 8–12，我们是 8。记忆表的大小也跟着 MoE 走：Engram 论文发现，每个词用不到的参数（没选中的专家 + 记忆表）里，记忆表占 20–25% 最好，large 取 25%。

### 其他细节

- **RMSNorm 带可学系数**（PyTorch 的 `nn.RMSNorm`，CUDA 上是融合内核）；
- **词向量和输出层不共享**；
- **初始化**：每个子层往残差流里写的那个投影（注意力输出、前馈的第二个矩阵、记忆注入的值）都从零开始，所以刚初始化时每一层什么都不加；其余矩阵按输入宽度均匀分布。

### 三档预设（词表 32768）

| 档 | 宽 × 层 | 主干 | 记忆表 | 词向量 + 输出层 | 合计 |
|---|---|---|---|---|---|
| small | 768 × 10 | 64M | 53M（每个哈希约 10 万行 × 宽 32） | 50M | 167M |
| medium | 1152 × 16 | 233M | 190M（约 25 万行 × 宽 48） | 75M | 499M |
| large | 1280 × 20 | 889M（每个词用到 266M） | 207M（约 20 万行 × 宽 64，占每个词用不到的参数的 25%） | 84M | 1.18B |

large 的前馈层：第 1 层普通前馈，其余各层 48 选 8 的四分之一宽专家加 2 个同宽的共享专家。`tinybrain report large` 打印每个部件的参数量。

---

## 分词器

`tokenizer/tokenizer.model`：SentencePiece BPE，**32768 词**，在按配比抽出的约 3500 万 token 样本上训练。

- 不做任何归一化，字节兜底，数字逐位拆开，字符覆盖率 0.99995，**解码和原文一字不差**；
- 0–3 是未知、开头、结束、填充，另留 8 个控制符：`<|im_start|>`、`<|im_end|>` 给对话格式，两个给工具调用，其余备用。

在留出文档上一个词平均几个字（越大越省）：

| 中文文章 | 百科 | 古文 | 代码 | 数学 | 论文 | 英文网页 | 合计 |
|---|---|---|---|---|---|---|---|
| 1.70 | 2.16 | 1.11 | 2.84 | 3.09 | 3.40 | 4.16 | 2.38 |

```bash
tinybrain tokenizer sample --tokens 40000000      # 重新抽样本
tinybrain tokenizer train --vocab 32768           # 重新训练
tinybrain tokenizer eval tokenizer/tokenizer.model
```

---

## 数据集：tinybrain dataset

一份以中文为主的混合预训练集，分四档，大档包含小档（nano ⊂ mini ⊂ base ⊂ full）。token 数是用上面的分词器实测的。

| 档 | 真实 token | 篇数 | 文件大小 | 适合 |
|---|---|---|---|---|
| nano | 0.99B | 54 万 | 2.1 GB | 跑通流程、做小实验 |
| mini | 4.96B | 348 万 | 10.3 GB | small（167M） |
| base | 20.19B | 1319 万 | 40.6 GB | medium（499M） |
| full | 60.26B | 4298 万 | 117 GB | large（1.18B） |

每个文件都是完整的一档、内部打乱：要 mini 就只读 `pretrain_mini.parquet`。列：`text`、`source`、`category`、`license`、`quality`、`est_tokens`。

### 配比

nano、mini、base 严格按下面的配比挑（按真实 token 算）；full 是去重后的全部，各类别有多少放多少。

| 类别 | 配比 | 主要来源 |
|---|---|---|
| 中文文章 | 37% | Fineweb-Edu-Chinese-V2.2（教育质量 3–5 分） |
| 百科 | 15.5% | 中文维基、英文维基、百度百科 |
| 代码 | 12% | UltraData-Code、UltraData-Stack-v3 |
| 数学 | 10% | Nemotron 数学教材、IFM 数学改写、FineMath、UltraData-Math、NuminaMath |
| 论文 | 8% | arXiv、peS2o |
| 古文和公版书 | 6% | 维基文库、殆知阁古籍、greathangpt、shu、古腾堡中文书、诗词、鲁迅全集 |
| 英文网页 | 5% | Ultra-FineWeb |
| 英文书 | 4% | 古腾堡（排除 PG-19 的验证集和测试集） |
| 合成 | 2.25% | Chinese Cosmopedia |
| 法律 | 0.25% | 中国法律法规 |

26 个来源各自的出处、许可证、下载方式和取正文的方式都登记在 `dataset/sources.py`；生成的数据集说明（`python -m dataset.mix card`）列出每个来源在每档里的用量。

### 怎么做的

1. **清洗**（`dataset/clean.py`、`dataset/pretrain.py`）：修乱码，统一标点和空白，繁体转简体；去掉太短、不成句、语言不对、广告、重复太多、有屏蔽字的文档；手机号、身份证号、邮箱换成占位符；书和古籍按章节切成篇；维基去掉表格、模板残留和「参考文献」之后的部分。每篇算一个质量分（来源自带的分数，或者按语言、重复、成句、广告、长度、用字丰富度算的启发式分数）。法院裁判文书因为含有当事人的姓名、出生日期和住址，没有放进来。
2. **跨来源去重**（`dataset/mix.py index`）：每篇取最长的 3 句当指纹；一篇文档如果有 2 句（指纹不足两个的，全部指纹）在优先级更高的文档里出现过，就算重复。只撞一句不算——一条常见的法律条文会出现在很多不同的文章里。优先级是整理过的来源（法律、诗词、古籍、维基……）在前，网页抓取的在后。去重去掉了约四分之一。
3. **分档**（`mix.py plan`、`write`）：按配比算出每个来源每档取多少；来源内部按质量分从高到低取，最好的进 nano，往下依次进 mini、base。所以**越小的档单篇质量越高**，大档的价值在量。
4. **检查**（`mix.py verify`）：每个来源的 token 数和计划一致；文件内部没有重复（允许十万分之一以内：句子太短、取不出指纹的残篇会漏下，base 和 full 里有 41 篇）；小档完整包含在大档里；顺序是打乱的。

### 许可

混合数据集没有统一的许可证：每篇文档带着 `license` 列，写的是它所属来源的许可证。维基百科、维基文库是 CC BY-SA 3.0（署名、相同方式共享）；百度百科和 shu 的上游没写清楚许可证，标成「待确认」，商用前请自行确认，或者按 `source` 列去掉。

```bash
tinybrain data --check              # 每一步要什么、有没有、会产出什么
python -m dataset.download wiki_zh --list    # 某个来源会下哪些文件
python -m dataset.pretrain audit wiki_zh     # 抽查洗出来的结果：随机看几篇、最常重复的行、可疑痕迹
```

---

## 预训练

```bash
tinybrain pretrain                                        # 默认：small，data/pretrain_nano.parquet → out/small/pretrain
tinybrain pretrain --data data/pretrain_mini.parquet --seq-len 2048 --batch-size 16
tinybrain pretrain --help     # 全部参数：模型（--dim、--n-layers……）、各组学习率、梯度裁剪、记录和存档
```

### 损失

下一个词预测，所有位置都算交叉熵；有 MoE 时加上均衡损失：

```math
\mathcal{L} = -\frac{1}{T}\sum_{t=1}^{T} \log p_\theta(x_{t} \mid x_{\lt t}) + 10^{-4}\,\mathcal{L}_{\text{bal}}
```

**模型很有把握时的梯度（softmax 塌缩）。** Barron 等（Google DeepMind，[arXiv 2610.31642](https://arxiv.org/abs/2610.31642)，按 v3）指出：标准实现里正确词的梯度是 $`p_t - 1`$。设正确词领先其余所有词的间隔为

```math
m = z_t - \mathrm{LSE}_{j \neq t}\, z_j
```

$`m`$ 超过约 16.6（FP32；BF16 约 5.5）时，$`p_t`$ 舍入成 1，正确项的梯度变成 0，其余词的梯度却还是正的，整份梯度加起来不再是 0。`lm/loss.py` 换成数学上相等、但不会舍入掉的写法：

```math
\ell = \mathrm{softplus}(-m),\qquad \frac{\partial \ell}{\partial z_t} = -\sigma(-m)
```

$`m`$ 用 $`-\mathrm{LSE}_{j\neq t}(z_j - z_t)`$ 来算，其余词全是 $`-\infty`$ 时先截到 $`-10^4`$（v3 勘误里的 NaN）。CPU/MPS 的分块损失、要整张输出时的损失、强化学习里的对数概率都走这条路；CUDA 上的 Liger 融合内核还是标准写法。论文还给出：用 Adam 加权重衰减时，间隔会停在 $`\ln(1/\varepsilon)`$ 附近。我们的默认 $`\varepsilon = 10^{-10}`$ 对应约 23，已经越过 FP32 的临界值，所以验证时日志里多一列 `saturated`（第一行里间隔超过临界值的词占比，屏幕上显示为「塌缩」）。它在 CUDA 上明显不是 0 时，可以加 `--adam-eps 1e-7`（对应约 16.1）。

### 按轮数训

`--epochs`（可以是小数；也可以直接给 `--steps`）：数据切成不重叠的片段，每轮打乱一次依次取完，**一轮里每个片段恰好看一遍**。日志每一行都写着已经训了多少词、多少轮，开训时先打印「共 N 步 = 多少词 = 几轮」。第几批取哪些片段只由种子和批次序号决定，所以中断后 `--resume` 接着跑，和一口气跑完结果一样。

### 优化器：矩阵用 Muon，其余用 Adam

**Muon**（`training/muon.py`）管所有矩阵（注意力、前馈、专家、各种投影）。思路是：先做动量，再把更新量「正交化」——让它的奇异值都接近 1，这样每个方向走的步子一样大，不会被少数几个大方向主导：

```math
B \leftarrow \mu B + (1-\mu) G,\qquad U = (1-\mu) G + \mu B\ \ (\text{Nesterov}),\qquad O = \mathrm{NS}_5(U)
```

```math
W \leftarrow (1 - \eta\lambda)\,W - \eta \sqrt{\max(1,\ m/n)}\; O
```

$`\mathrm{NS}_5`$ 是 5 次 Newton–Schulz 迭代，不用做 SVD：

```math
X_0 = U / \lVert U \rVert,\qquad A = X X^\top,\qquad X \leftarrow aX + (bA + cA^2)\,X,\qquad (a, b, c) = (3.4445,\ -4.7750,\ 2.0315)
```

形状相同的矩阵叠在一起一次算完；CUDA 上用 bf16 算正交化。`--optimizer native` 换成 PyTorch 自带的 `torch.optim.Muon`（两条路径的更新结果几乎一样，有测试对照）。

**Adam** 管词向量、输出层、记忆表和零碎的系数（$`\beta = (0.8, 0.95)`$），学习率按 $`(d/768)^{-1/2}`$ 缩放：

| 参数组 | 起步学习率 | 命令行 |
|---|---|---|
| 矩阵（Muon） | 0.02 | `--matrix-lr` |
| 词向量 | 0.3 | `--embed-lr` |
| 输出层 | 0.004 | `--head-lr` |
| 记忆表（不做权重衰减） | 0.3 | `--engram-lr` |
| 归一化系数、多流残差系数、流入口出口的查询 | 0.01 | `--scalar-lr` |

这些都是起步值，还没在我们的数据上调过。

### 学习率曲线

先线性预热，再按余弦降到起步值的 $`f`$ 倍（`--final-lr-frac`，预训练默认 0.1）：

```math
\text{scale}(t) = \begin{cases} \dfrac{t+1}{T_w} & t < T_w \\[2mm] f + (1-f)\cdot\dfrac{1 + \cos(\pi p)}{2},\quad p = \dfrac{t - T_w}{T - T_w} & t \ge T_w \end{cases}
```

每组的学习率 = 起步值 × scale(t) × `--lr-mult`。

`--schedule wsd` 换成 WSD（预热、恒定、退火）：预热之后一直保持 1，最后 $`T_d`$ 步（`--decay-frac`，默认 0.2）按 $`1-\sqrt{p}`$ 降到 $`f`$：

```math
\text{scale}(t) = \begin{cases} \dfrac{t+1}{T_w} & t < T_w \\[2mm] 1 & T_w \le t < T - T_d \\[2mm] 1 - (1-f)\sqrt{p},\quad p = \dfrac{t - (T - T_d) + 1}{T_d} & t \ge T - T_d \end{cases}
```

余弦要在开始时定死总步数；WSD 的恒定段里，任何一个存档都能分出一支单独退火，主线接着训。这样训到一半就能拿到一个退过火、能用的模型，再决定要不要训满。短退火能达到和余弦相当的效果，见 Hägele 等 2024，*Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations*。

```bash
tinybrain pretrain --schedule wsd                                                  # 主线
tinybrain pretrain --cooldown-from out/small/pretrain/ckpt.pt --cooldown-steps 3000   # 分支 → out/small/cooldown-<步数>
```

退火分支连优化器状态一起接着主线走，数据也接着主线往后取；学习率从主线在这一步本来的值降到 `--final-lr-frac`（不写就和主线一样）。片段长度、批大小、优化器设置都取自存档。余弦训练的存档也能分支，可以用来量「现在退火能降多少」。和[退火](#退火)那一步的 `--init` 不同：`--init` 只取模型参数，优化器从头开始。

---

## 后训练

```
small        ：预训练(mini) → 退火 → SFT → agent RL（同时练指令跟随、中文阅读、诗词填空）→ RLAIF
medium/large ：预训练(base / full) → 退火 → SFT → 领域专家（数学、代码：SFT + RLVR；文学：SFT）
               → MOPD → RL（工具调用、科学选择题、指令跟随、阅读、填空）→ RLAIF
```

每档都能单独跑通，不依赖别的尺寸。完整的设计和取舍见 [docs/post-training.md](docs/post-training.md)。

```bash
tinybrain data sft rl       # 后训练数据：SFT 语料、RL 题目、评测题、MOPD 提示（也可以从 ModelScope 的 posttrain/ 下载）
```

各阶段都写到同一个运行目录（默认 `out/small`，换尺寸用 `--run out/medium`），不写 `--init` 时自动从上一个阶段的存档出发：

```bash
tinybrain sft                                            # SFT：从退火（没有就预训练）出发 → out/small/sft
tinybrain sft --data data/sft_expert_math.parquet        # 领域专家 → out/small/expert_math（代码、文学同理）
tinybrain distill                                        # MOPD：学生是 sft，老师是所有 expert_<领域> → out/small/mopd
tinybrain rl --judge-url http://localhost:8000/v1        # RL：从 sft 出发，data/rl_small.parquet → out/small/rl
```

### 退火

预训练最后一段（默认最后 10% 的步数）换数据接着训：九成预训练数据 + 一成对话格式的数据（整段都算损失），学习率从 0.1 倍降到 0。用的还是 `train_pretrain.py`：

```bash
tinybrain prepare --chat --train-on all --input data/sft_small.parquet --out data/tokens/chat-all    # 一成的对话数据：整段都算损失
tinybrain pretrain --init out/small/pretrain/ckpt.pt --data data/pretrain_mini.parquet:0.9,data/tokens/chat-all:0.1 \
    --epochs 0.1 --warmup-steps 0 --lr-mult 0.1 --final-lr-frac 0          # 给了 --init 默认写到 out/small/anneal
```

### SFT

对话格式（`<|im_start|>`、`<|im_end|>` 是分词器里预留的控制符，正文里写出同样的字符串也不会变成控制符）：

```
<|im_start|>system
你是 tinybrain……<|im_end|>
<|im_start|>user
床前明月光的下一句是什么？<|im_end|>
<|im_start|>assistant
疑是地上霜。<|im_end|>
```

**只在回答上算损失**：每个位置带一个遮罩 $`m_t \in \{0,1\}`$，只有助手的回答和它后面的 `<|im_end|>` 是 1：

```math
\mathcal{L}_{\text{SFT}} = -\frac{\sum_t m_t \log p_\theta(x_t \mid x_{\lt t})}{\sum_t m_t}
```

对话按长度打包成等长的行（一段对话不拆到两行，行尾用填充补齐），按轮数训（`--epochs`），学习率默认是预训练的 0.1 倍。

**SFT 语料**（`dataset/sft.py`）：18 个外部来源（smoltalk-chinese、COIG-CQIA、Chinese-Instruct、deepctrl、Infinity-Instruct、NuminaMath-CoT、OpenCoder SFT、ToolACE……，每个取前 10 万条），加上自己做的文学数据（按题写诗、文白互译、鲁迅续写）和自我认知。三档的区别：small 去掉推理过程、截到 2048 词，并且每个外部来源按回答的质量分只留好的一半；medium、large 保留 `<think>` 推理过程，截到 4096 / 8192 词，多几个推理和 agent 来源。每个来源留出 2% 的问题不进 SFT，给 RL 和评测出题。

**领域专家**（medium、large）：从通用 SFT 模型复制出三份，分别在数学、代码、文学数据上接着 SFT，数学和代码专家再做 RLVR。

### MOPD：多老师在线蒸馏

把几个专家的本事合回一个通用模型。做法是让**学生自己生成回答**，再让对应领域的专家逐位置给出它的概率分布，最小化学生对老师的**反向 KL**：

```math
\mathcal{L}_{\text{MOPD}} = \frac{1}{\sum_i |y_i|}\sum_i \sum_{t \in y_i} \sum_{v \in V} \pi_\theta(v \mid h_{i,t}) \Big[\log \pi_\theta(v \mid h_{i,t}) - \log \pi_{T(d_i)}(v \mid h_{i,t})\Big]
```

- $`y_i \sim \pi_\theta`$ 是学生自己写的回答，$`h_{i,t}`$ 是提示加上回答的前 $`t`$ 个词；
- $`T(d_i)`$ 是第 $`i`$ 道题的老师，按领域 $`d_i`$ 路由：数学、代码、文学各有专家；逻辑题交给数学专家，阅读、诗词、写作交给文学专家，指令跟随、科学、工具调用和通用题交给 SFT 模型自己（`training/train_distill.py` 的 `ROUTES`，`--route 领域=老师` 可以改）；
- 学生和老师用同一个分词器，所以 KL 在**整个词表上精确地算**，不是只靠采样出的那一个词去估。

**为什么是在线、为什么是反向 KL**：普通蒸馏让学生模仿老师写好的文本，学生训练时只见过「老师的前文」，自己生成时一旦写偏就没见过这种情况（暴露偏差）。在线蒸馏在学生自己的回答上纠错，正好覆盖它会犯的错。反向 KL $`\text{KL}(\pi_\theta \Vert \pi_T)`$ 是「寻峰」的：学生只需要把概率放在老师认可的地方，不用强行覆盖老师的所有可能——对容量小的学生更合适。

`--merge-init`：开始前先做任务算术，把学生换成 $`\theta \leftarrow \theta + \frac{1}{K}\sum_k (\theta_k - \theta)`$（各专家相对 SFT 模型的改动取平均）。

### RL：从 PPO 到 GRPO，再到我们的写法

**PPO** 的策略损失（每个位置 $`t`$）：

```math
\mathcal{L}^{\text{PPO}} = -\mathbb{E}_t\Big[\min\big(\rho_t A_t,\ \mathrm{clip}(\rho_t,\,1-\epsilon,\,1+\epsilon)\,A_t\big)\Big],\qquad \rho_t = \frac{\pi_\theta(y_t \mid h_t)}{\pi_{\theta_{\text{old}}}(y_t \mid h_t)}
```

- $`\rho_t`$ 是新旧策略的概率比：同一批回答要用来更新好几次，更新后的策略和采样时的不一样了，所以要按比例修正；
- $`\mathrm{clip}`$ 不让一次更新走太远；
- 优势 $`A_t`$ 要一个**价值模型**（critic）来估，和策略一样大，训练和显存都翻倍。

**GRPO**（DeepSeekMath）去掉了价值模型：每道题采一组 $`G`$ 个回答，用**组内比较**当优势：

```math
A_i = \frac{r_i - \mathrm{mean}(r_1, \dots, r_G)}{\mathrm{std}(r_1, \dots, r_G)}
```

并且每个回答的损失按它的长度 $`|y_i|`$ 平均。

**Dr. GRPO** 指出这两处会带偏：除以标准差，会让「几乎全对或全错」的简单题、难题权重过大；按长度平均，会让答错的长回答每个词受的惩罚变小，模型于是越答越长。改法是**不除标准差、用一个常数代替长度**。

**tinybrain 的写法**（`training/train_rl.py`）：在 Dr. GRPO 的基础上，每批回答**只更新一次**（完全在线）。这时 $`\theta = \theta_{\text{old}}`$，$`\rho_t = 1`$，clip 不起作用，min 里两项一样，PPO 的梯度正好退化成带组内基线的策略梯度。所以损失直接写成：

```math
\mathcal{L}_{\text{RL}} = -\frac{1}{N \cdot L_{\max}} \sum_{i=1}^{N} A_i \sum_{t \in y_i} \log \pi_\theta(y_{i,t} \mid h_{i,t}),\qquad A_i = r_i - \frac{1}{G}\sum_{j \in \text{组}(i)} r_j
```

$`N`$ 是这一步的回答总数（每步题数 × 每题回答数），$`L_{\max}`$ 是回答长度上限（`--max-new`），两个都是常数。整组奖励一样的题优势全是 0，不贡献梯度。agent 题里工具返回的内容不是模型写的，遮掉不算。没有价值模型，也没有参考模型的 KL 惩罚。

RLVR、agent RL、RLAIF 用的是同一个训练器，区别只在题目和奖励：

| 题型 | 奖励 $`r`$ | 题目来源 | 用在 |
|---|---|---|---|
| math | 最终答案（`\boxed{}` 或「答案是」）和标准答案相等（按数值比）→ 1，否则 0 | Big-Math-RL-Verified（挑 8B 模型解题率 0.2–0.95 的）、DeepScaleR、GSM8K_zh | medium、large |
| code | 在沙箱里跑测试用例，全过 → 1 | DeepCoder-Preview 训练集；评测用其中的 Codeforces | medium、large |
| logic | reasoning-gym 的判分函数（有的题允许多个对的答案） | reasoning-gym 现场生成：算术、数列、24 点、Countdown、骑士与无赖、小数独等 33 种 | medium、large |
| choice | 选项字母对 → 1 | ARC、OpenScience | medium、large |
| instruct | 满足的约束占比（字数、段落、编号、关键词、开头结尾、JSON、不用逗号……，程序检查） | RLVR-IFeval；给留出的中文问题加中文约束 | 三档 |
| reading | 和参考答案按字算 F1，取最好的参考 | CMRC2018 | 三档 |
| cloze | 去掉标点后和标准答案完全一样 → 1（回答不能长到把整首诗都写上） | 从诗词里出：给作者、题目、上句，写下句 | 三档 |
| agent | 答案对 → 1；工具调用格式坏一次 −0.1 | 程序生成：大数运算、百分比、取模、日期、在维基资料里检索 | 三档 |
| judge | 评审打分 $`s \in [1,10]`$，$`r = (s - 5.5)/4.5 \in [-1, 1]`$ | 留出的通用问题；鲁迅续写（附原文参考） | 三档 |
| poetry | $`r = 2\big(0.4\,r_{\text{格律}} + 0.6\,\tfrac{s-1}{9}\big) - 1`$；字数句数不对时评审分减半 | 真实诗题，五绝、七绝、五律、七律 | 三档 |

**格律分**（`training/rewards/poetry.py`）：句数、每句字数要对，否则 0；对了以后 $`r_{\text{格律}} = 0.3 + 0.35\,r_{\text{押韵}} + 0.35\,r_{\text{平仄}}`$。押韵看偶数句末字是否同韵且平声；平仄按「一三五不论，二四六分明」，在仄起、平起两种格式里取对得更好的。平仄和韵部用 pypinyin 按普通话近似，入声字会判错（这是已知的简化）。

**RLAIF 的评审模型**：Qwen3.8-27B（Apache-2.0），按中文评分细则（`docs/rlaif-rubric.md`：通用、写作、古文、诗词四个领域）打 1–10 分，不开思考模式。显卡上用 vLLM 跑 FP8 版，Mac 上用 `mlx_lm.server` 跑 4-bit 版（一次只算一个请求，要加 `--judge-workers 1`）。`tinybrain judge-check` 用好回答和故意弄坏的回答（截断、答非所问、车轱辘话、诗的字序打乱）检查评审分不分得清好坏。

题目和评测题由 `dataset/rl.py` 生成：每种题先留出一份当评测题，和 RL 题、SFT 都不重复。

---

## N 卡训练：加速、Windows、监控

在 RTX 5070 Ti 16GB 上验证过：small、2048 × 16，约 7 万 token/秒（0.46–0.47 秒一步），进程专用显存峰值约 12.5 GiB。CPU 和 MPS 上走普通的 PyTorch 实现，结果一样（有测试对照）。

CUDA 训练加速使用 **Liger Kernel 0.8.5+**（融合输出层交叉熵、静态 mHC 读写、RMSNorm、RoPE、ReLU²）和 **PyTorch FlexAttention**（原生 GQA、滑动窗口）。Linux 可安装 `pip install -e ".[data,cuda]"`；Windows 先准备匹配 PyTorch 的 `triton-windows`，再安装 `pip install --no-deps liger-kernel==0.8.5`，避免 pip 拉取不支持 Windows 的标准 Triton 包。CPU 保留普通 PyTorch 实现。

`tinybrain bench small --batch 16 --seq 2048` 测完整的前向、反向和优化器更新；CUDA 默认使用选择性激活重计算，可用 `--checkpoint-policy full` 改为整层重算，或 `--no-checkpoint` 关闭重算。主干逐层编译，Engram 查表、流入口、出口和 Sinkhorn 也参与编译。mHC 使用 Liger 原有内核直接写入输入精度的缓冲区，减少 FP32 临时张量；内核内仍用 FP32 计算。预训练和 SFT 使用同一套融合损失与加速算子。

预训练和 bench 可加 `--cuda-graph` 捕获融合 Adam 与自定义 Muon 的更新图，学习率保留在设备张量中逐步更新；检查点仍保存完整优化器状态。`--autotune` 搜索固定形状下的矩阵和注意力内核，首次编译较久。预训练默认每 50 步记录日志，可用 `--log-every` 修改。例如 `tinybrain pretrain --data data/tokens/base --out out/small/pretrain --preset small --seq-len 2048 --batch-size 16 --epochs 1 --cuda-graph --log-every 50`；从已有存档继续时加 `--resume`。

CUDA 训练时把 Q、K、V 投影合并成一次矩阵乘法，参数和检查点中仍分别保存三组权重。验证和带缓存的生成保留原来的投影路径。

medium 在 16GB 显卡上用微批 4、梯度累积 4，完整一步仍处理 16 × 2048 = 32,768 个词，实测约 2.59 万 token/秒（1.26 秒一步），专用显存峰值约 12.4 GiB。可以装 `pip install -e ".[cudnn]"`（`nvidia-cudnn-frontend>=1.32.3,<1.33`，要 PyTorch 2.13+），用 `--attention-backend cudnn` 换成 NVIDIA 原生的滑动窗口/GQA 前向和反向；默认仍是 FlexAttention。编译路径还把 mHC 读流和 RMSNorm 融在一起，并让 FFN 的矩阵乘法和 ReLU² 一起搜索融合方式；模型结构、词表和优化器状态的精度不变。`--gpu-memory-fraction` 在建模型之前给 PyTorch 设显存上限。验证的抽样批大小（`--eval-batch-size`）和实际前向的微批（`--eval-micro-batch-size`）分开指定：换了训练微批，验证片段仍和以前一样，历史损失可以直接比。

```bash
tinybrain pretrain --data data/tokens/base --out out/medium/pretrain --preset medium --seq-len 2048 --batch-size 4 --grad-accum 4 --epochs 1 --autotune --attention-backend cudnn --gpu-memory-fraction 0.85 --checkpoint-policy selective --eval-batch-size 16 --eval-micro-batch-size 4 --log-every 50
tinybrain bench medium --batch 4 --grad-accum 4 --seq 2048 --autotune --attention-backend cudnn --gpu-memory-fraction 0.85
```

**多卡（ZeRO-1）**：预训练用 torchrun 启动就是多卡，每张卡一个进程（NCCL），代码在 `training/distributed.py`。`--batch-size` 是每张卡的批大小，每步一共「批大小 × 累积 × 卡数」个片段。

```bash
torchrun --standalone --nproc-per-node 8 -m training.train_pretrain --preset medium --data data/tokens/base --batch-size 2 --grad-accum 1 \
    --seq-len 2048 --epochs 1 --eval-batch-size 16 --eval-micro-batch-size 4
```

- 每个参数归一张卡管（按大小贪心地分）：梯度只汇总到管它的卡上，这张卡用 Muon 或 Adam 更新它，再把新参数广播给其他卡。优化器状态（Adam 的两个矩、Muon 的动量）每张卡只存自己那份，约为单卡的 1/卡数；通信量和普通的数据并行一样。
- 第几步、第几个微批、第几张卡取哪些片段只由种子和序号决定，合起来正好是单卡同一步取的那些。所以每步的片段数一样时，多卡和单卡训出来的是同一个模型（有测试对照，只差浮点加法的顺序），存档也能在单卡和多卡之间互相 `--resume`。比如 5070 Ti 上用 `--batch-size 4 --grad-accum 4` 训到一半的 medium，换到 8 张卡上用 `--batch-size 2 --grad-accum 1` 接着训。每步的片段数和存档不一样时，`--resume` 会拒绝。
- 第一次给 parquet 时只有 0 号卡切词，其他卡等它切完。只有 0 号卡打印、写日志和存档；验证的几批分给各卡算。
- MoE 的路由偏置按各卡负载的平均来调。多卡时不能用 `--cuda-graph`、`--offload-adam`。
- 现在只有预训练（含退火）支持多卡，SFT、蒸馏、RL 还是单卡。

Windows 默认编码为 GBK 时，先设 `$env:PYTHONUTF8 = 1`（PowerShell）再运行 `tinybrain …`，或者用 `python -X utf8 -m tools.bench small --batch 8 --seq 4096`。如果 Triton 默认缓存目录报路径错误，可在 PowerShell 中先设置 `$env:TRITON_CACHE_DIR = "$PWD\.cache\triton"` 和 `$env:TORCHINDUCTOR_CACHE_DIR = "$PWD\.cache\inductor"`。

训练中也可以接入 TensorBoard：安装 `pip install -e ".[monitor]"`，运行 `tinybrain tensorboard --run out/small/pretrain`，再运行 `python -m tensorboard.main --logdir out/small/pretrain/tensorboard --host 127.0.0.1 --port 6006`，打开 `http://127.0.0.1:6006`。同步工具会补录已有 JSONL 指标并持续追加训练/验证损失、各参数组学习率、吞吐和进度；不需要重启训练。历史数据的横轴使用训练步数。

---

## 评测

```bash
tinybrain benchmarks prepare                                             # 下载 C-Eval、CMMLU、GSM8K（只在本地评测用）
tinybrain eval out/small/rl/ckpt.pt --tasks data/eval_tasks.parquet --bench ceval cmmlu gsm8k --judge-url …
tinybrain benchmarks run out/small/pretrain/ckpt.pt --shots 5            # 基座模型：不套对话格式，带例题
```

- **留出集损失**：按类别（中文、百科、代码、数学、古文……）看后训练有没有把预训练学到的东西训坏；
- **题目正确率**：每种 RL 题型留出的评测题，默认温度 0.8、前 50 名里采样作答（种子固定，可复现；`--temperature 0` 改回贪心），用同一套判分；
- **标准基准**：C-Eval（验证集）、CMMLU 比较「答案：」后面四个选项字母的概率（不用生成，基座模型也能测）；GSM8K 同样默认采样生成后对答案；
- **固定提问**：每个阶段对同一组问题作答，放在一起给人看。

C-Eval 是 CC BY-NC-SA 4.0、CMMLU 是 CC BY-NC 4.0，只下载到本地评测，不随仓库或数据集发布。

---

## 推理

```bash
tinybrain chat --tools                         # 命令行对话：默认用 out/small 里走得最远的存档；--tools 打开计算器和 Python
tinybrain serve out/small/rl/ckpt.pt --port 8001  # 聊天网页，以及 OpenAI 兼容的接口（见下）
```

`tinybrain serve` 的接口：`POST /v1/chat/completions`（对话，支持工具调用）、`POST /v1/completions`（续写，提示前面自动加文档结束符）、`GET /v1/models`、`GET /v1/info`（存档、阶段、步数、参数量）。请求里写 `"stream": true` 就按 OpenAI 的格式边生成边推送；读的一方断开，服务端就不再往下生成。

续写和生成式评测默认温度 0.8、只在概率最高的 50 个词里采样；`tinybrain generate`、`tinybrain eval`、`tinybrain benchmarks run` 都可以用 `--temperature`、`--top-k`、`--seed` 改，默认种子 0，评测结果里记下采样参数。`--temperature 0` 是每步取概率最大的词。预训练续写在提示前加文档结束符，生成出结束符就停。

CUDA 上生成走静态缓存：键值缓存按最大长度预先分配，每一步原地写入，形状完全固定，整步用 `torch.compile(mode="reduce-overhead")` 录成 CUDA graph（gpt-fast 的做法）。CPU、MPS 上走普通的带缓存生成，两条路径结果一样（有测试对照）。

---

## 演示结果

2300 万参数的演示模型（宽 256 × 4 层），用 nano 开头的 9000 万词预训练 1 轮，再用完整的后训练数据把每个阶段都跑一遍（M4 Max 上共 198 分钟）。**这一步只为确认整条链衔接无误，分数不代表能力**：这个尺寸只会复读（问「你好，请介绍一下你自己」，答「你好，你好，你好……」），选择题在随机水平附近（四选一随机是 25%，每个基准只评了 100 题）。

| 阶段 | 留出集损失 | C-Eval | CMMLU | GSM8K |
|---|---|---|---|---|
| 预训练 | 4.073 | 31% | 34% | 0% |
| 退火 | 4.057 | 27% | 36% | 0% |
| SFT | 4.206 | 24% | 25% | 1% |
| 工具调用 RL | 4.208 | 26% | 22% | 0% |
| 数学专家 | 4.445 | 25% | 26% | 1% |
| 代码专家 | 4.526 | 27% | 34% | 0% |
| MOPD | 4.207 | 25% | 24% | 0% |
| MOPD + 评审 RL | 4.207 | 26% | 28% | 1% |

能看出来的只是机制在起作用：退火后损失再降一点；两个专家在通用留出集上损失明显升高（往自己的领域偏了）；MOPD 把学生拉回 SFT 的水平，同时吸收了专家。

---

## 还没做的

- 完成 Small 和 Medium 的独立终评，覆盖多轮对话、算术和指令遵循。Large 尚未训练。
- 评分细则和人工打分对比校准；
- 古文、诗词的专门评测；MMLU、MATH-500、HumanEval、MBPP、IFEval 这些基准；
- large 接小米开源的 MiMo agent 环境（通过 `inference/serve.py` 的 OpenAI 兼容接口）；
- 诗词格律换成平水韵的字表。

---

## 联系与赞助

训练用的算力是我自己出钱租的。如果你愿意赞助算力，或者想合作，欢迎写信到 [3995756625@qq.com](mailto:3995756625@qq.com)；赞助方会写进 README 和之后的视频。提问和反馈请直接开 [issue](https://github.com/logitcai/tinybrain/issues)。

## 许可证

代码以 [MIT 许可证](LICENSE) 发布。数据集没有统一的许可证，每篇文档按所属来源的许可证，见[许可](#许可)。

---

## 参考

- MiniMind — https://github.com/jingyaogong/minimind ；nanochat — https://github.com/karpathy/nanochat
- Hyper-Connections（字节跳动）、mHC：Manifold-Constrained Hyper-Connections（DeepSeek）
- Engram：按 n 元词组查表的条件记忆（DeepSeek）
- Muon — https://kellerjordan.github.io/posts/muon/
- GRPO：DeepSeekMath — https://arxiv.org/abs/2402.03300
- Dr. GRPO：Understanding R1-Zero-Like Training — https://arxiv.org/abs/2503.20783
- MOPD: Multi-Teacher On-Policy Distillation — https://arxiv.org/abs/2606.30406 ；CA-MOPD — https://arxiv.org/abs/2610.26950
- reasoning-gym — https://github.com/open-thought/reasoning-gym
- 数据集的每个来源见 `dataset/sources.py`
