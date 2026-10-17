# VeriVLA

一个我自己从零搭到跑通的多模态工具调用 Agent 后训练项目：给 Qwen3-VL-4B 喂自己造的图表问答数据，
走完 SFT → RM/PPO → DPO → GRPO → 合并量化 → vLLM 部署 → 独立评测 的整条链路，最后把评测结果反过来
再喂给训练，做第二轮。

写这个仓库的初衷很简单：网上讲 RLHF 的文章很多，但基本都停在公式和概念，真正自己在 4 张 3090 上
跑一遍，会发现坑全在工程细节里——显存怎么抠、奖励怎么防止被话术 hack、评测怎么才算公平。
这些我都写进 [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) 了，20 多个真实报错，每条都留了原始日志。

> 想快速看我踩了什么坑、怎么解决的，直接翻那份文档就行；想看整体设计和结果，往下读。

## 它做了什么

```
造数据 → SFT → RM → PPO → DPO → GRPO → 三重合并校验 → 五模型同口径评测
                                                          ↓
                                  AWQ 量化 + vLLM 部署 ← 评测反哺第二轮 GRPO
```

- **模型**：Qwen3-VL-4B-Instruct 为主，2B / SmolVLM2-2.2B 当 debug 用的便宜替身
- **训练方式**：QLoRA（r=64，视觉塔保持 bf16 不量化，不然读图直接掉点）
- **任务**：图表问答 + 工具调用。模型要看图、调计算器/查表工具、再给出带读数依据的答案
- **奖励**：不训奖励模型，全部程序化规则打分（后面细说）
- **部署**：AWQ W4A16 量化到 3.3GB，vLLM 直接加载压测

## 三个我觉得值得说的设计

**1. 逐步工具合法性奖励。** 每生成一步就校验一次工具名、参数 JSON Schema，还真的在只读沙箱里执行一遍。
好处是信用分配能落到具体某一步，而且没有额外模型要训、也没法靠话术把分骗出来。
（对比一下：只看最终结果的奖励，模型很容易学会"看起来在调工具"。）

**2. 跨模态接地奖励。** 图像题必须把 `<readings>` 里的读数和图像真值逐项对上，且答案要建立在读数之上
才能拿满分。这条专门堵"不看图、靠文本先验蒙答案"的路。

**3. 评测反哺课程。** 五模型 13 维评测找出最弱的维度 → 自动生成针对性数据 → 从 GRPO 的 adapter
续训第二轮 → 再用 McNemar + 配对 bootstrap 量化有没有提升。机制整条跑通了（诚实地说，小数据下
增益测不出来，见文末的局限）。

## 结果

24 道题、13 个能力维度、贪心解码，五个模型同基座同口径：

| 模型 | 准确率 |
| --- | --- |
| base | 0.333 |
| SFT / DPO / GRPO / GRPO+课程 | **0.583** |
| PPO（最小 rollout 配置） | 0.250 |

- `GRPO vs base`：Δ=+0.250，配对 bootstrap 置信区间不跨 0，McNemar p=0.0703（24 题的样本量就这水平，我认）
- `GRPO vs PPO`：p=0.0078，差得很显著——PPO 我只跑通了最低配，不是调优过的配置
- 提升最集中的几个维度：`error_recovery` 0 → 1.0，`tool_choice` 0.031 → 0.39，`tool_format` 0.417 → 0.792

顺带一提，中间我把一个欠拟合的 SFT（3 epoch，loss 卡在 3.73）当成有效权重往下训了一整条链，
最后才发现问题、重训了 SFT。这个教训和排查过程也留在仓库里了，属于"复盘证据"，没删。

## 目录结构

```
├── configs/        # 各阶段超参快照
├── scripts/        # 00~10 一键串联脚本，从体检到评测
├── src/verivla/
│   ├── tools/      # 工具沙箱：calculator / kb_lookup / sql_query，只读 + 白名单 AST
│   ├── data/       # 图表生成、7 类真实场景轨迹、一键造数
│   ├── sft/        # QLoRA SFT
│   ├── rlhf/       # reward model + PPO
│   ├── dpo/        # DPO / IPO / SimPO / ORPO / KTO 一个入口
│   ├── grpo/       # 五个规则奖励 + 训练循环
│   ├── deploy/     # AWQ 量化、vLLM 服务、吞吐压测
│   └── eval/       # 三层判定、13 维评测、显著性检验、课程
├── docs/           # 详细版设计文档 + 踩坑档案（强推）
├── logs/           # 原始训练日志，出问题时对照用
└── reports/        # 评测报告
```

## 快速开始

```bash
git clone <repo>
cd <repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt          # flash-attn / vllm 的坑写在文件注释里了

bash scripts/00_check_env.sh             # 环境体检，全 PASS 再往下
bash scripts/01_prepare_data.sh          # 造数 + 生成图表，笔记本也能跑，约 30 秒

bash scripts/02_sft.sh debug             # 单卡小模型 smoke test，先确认链路通
bash scripts/02_sft.sh 4                 # 正式 4 卡
bash scripts/06_grpo.sh 4

bash scripts/07_awq.sh                   # 量化，建议单独一个 venv
bash scripts/08_serve_vllm.sh ckpt/qwen3vl_4b_awq 2 8000
bash scripts/09_eval_all.sh              # 五模型顺序评测 + 显著性报告
```

两套环境（训练栈 / 部署栈）**不要混装**——vLLM 会 pin 自己的 torch，混了会打坏 bitsandbytes 的
CUDA 扩展 ABI，QLoRA 当场报废。具体的版本组合在 `requirements.txt` 里。

## 老实说的局限

- 数据是玩具规模：37 条 SFT。机制都是通的，扩数据属于线性工程活
- PPO 是"跑通"的配置，不是调优过的
- 课程反哺链路全通，但小数据下对评测集测不出增益（p=1.0）
- 在线压测的质量分和离线评测不可比（线上为了快没执行工具）

## 文档

- [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) —— 20+ 个真实报错：现象、报错原文、根因、修法、验证
- [docs/README_full.md](docs/README_full.md) —— 更细的设计文档（21 项交付对照）
- [INTERVIEW.md](INTERVIEW.md) —— 我自己准备面试时写的问答梳理
- [STATUS.md](STATUS.md) —— 当前各阶段产物和复跑入口
