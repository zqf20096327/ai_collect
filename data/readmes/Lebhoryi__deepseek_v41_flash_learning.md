# DeepSeek-V4.1-Flash 源码研读仓库

> 官方 HuggingFace 仓库 [`deepseek-ai/DeepSeek-V4.1-Flash`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) 的本地镜像 + 学习笔记。
> 不含模型权重（全量约 510 GB / 48 分片，仅保留 `index.json` 索引），用于**静态读源码**研习 V4.1-Flash 的网络结构与创新点。

- **模型**：DeepSeek-V4.1-Flash（2026-09 发布，MIT License）
- **架构**：552B 主干 + 196B Engram；激活 8B(prefill) / 16B(decode)；40 层 CED（20 编码器 + 20 解码器）
- **创新点**：CED 因果编解码器 / CSA2 压缩稀疏注意力 2 / 分层稀疏索引器 / Single-Pass mHC / Engram 条件记忆 / DSpark 投机解码 / FP4 主 KV 缓存（890 B/token）
- **官方技术报告**：`DeepSeek_V41_Tech_Report.pdf`（51 页，文本版见 `docs/Tech_Report.txt`）

## 仓库结构

目录结构已按官方仓库还原（下载时被打平，导致内部导入失效；2026-09-11 还原修复）。

```
dsv41-flash-learning/
├── README_hf.md                    # 官方模型卡（英文原版，含评测对比表与采样参数）
├── config.json                     # HF 权重配置（architectures=DeepseekV41ForCausalLM）
├── index.json                      # 48 片 safetensors 权重索引（96085 张量 / 510 GB）
├── DeepSeek_V41_Tech_Report.pdf    # 官方技术报告
├── pyrightconfig.json              # 编辑器补全用 extraPaths=["inference"]
├── encoding/                       # Prompt 编码参考实现（无推理依赖）
│   ├── encoding.py                 #   编解码：encode_messages / parse_message_from_completion_text
│   ├── test_encoding.py            #   21 个测试 = V4.1 格式契约（DSML 前导空格 / effort 1-100 / 中途 System 消息）
│   └── README.md
├── inference/                      # 最小可读推理实现（可读参考，非生产引擎）
│   ├── model.py                    #   核心前向 1333 行（已提交版 1328）：CED / CSA2 三模式 / Engram / mHC / DSpark
│   ├── kernel.py                   #   TileLang kernel：dense-fp8 / MoE-fp4 GEMM、sparse_attn、hc_split_sinkhorn
│   ├── convert.py                  #   HF 权重 → TP 分片转换（含 FP4 反量化 cast_e2m1fn_to_e4m3fn）
│   ├── engram.py                   #   n-gram 哈希查表（素数表 / 压缩 token map / NgramHashState）
│   ├── image_processor.py          #   图像网格规划（resize 比例 / token 约束）
│   ├── vision.py                   #   DeepSeek-ViT + Aligner
│   ├── generate.py                 #   生成入口（torchrun TP 并行）
│   ├── config.json                 #   推理侧配置（generate.py 实际读取）
│   ├── run.sh / requirements.txt / README.md
└── docs/                                    # 学习笔记与图表
    ├── Tech_Report.txt                      #   技术报告文本提取版（2879 行，可全文检索）
    ├── dsv41-ch2-architecture-mindmap.html  #   第二章 Architecture 交互式思维导图（可折叠）
    ├── dsv41-attention-arch.drawio          #   Attention（CSA2 + SWA）架构图（Draw.io）
    ├── dsv41-block-mhc.drawio               #   Block.forward · Single-Pass mHC 结构图（Draw.io）
    ├── dsv41-engram.drawio                  #   Engram n-gram 查表数据流图（Draw.io）
    ├── csa2-dataflow.html / .json           #   CSA2 单层数据流与跨层复用图（signal-flow）
    ├── dsv41-ch2-mHC-dataflow.json          #   mHC 数据流 spec（系数错位一拍 / 视角切换）
    ├── dsv41-ch2-CED-学习笔记.md            #   2.2 CED 自测 8 题 + replay 概念 + YoCo 对比
    ├── dsv41-ch2-CSA2-SWA-学习笔记.md       #   2.3 CSA2/SWA 自测 10 题 + 3 专题澄清
    └── dsv41-ch2-CSA2-Indexer-学习笔记.md   #   2.3 Indexer.forward 逐行 + 分层候选池 + 自测 6 题
```

## 快速开始

```bash
# 参考实现自测（小模型，走真实 dense-fp8 / MoE-fp4 kernel，验证形状与管道，无需权重）
python inference/model.py

# Prompt 编码契约测试（无需 torch）
pytest encoding/test_encoding.py

# 完整推理流程：先转权重，再生成（需要 510GB 权重 + 多卡）
export HF_CKPT_PATH=<权重目录> SAVE_PATH=<输出目录> MP=8
python inference/convert.py --hf-ckpt-path $HF_CKPT_PATH --save-path $SAVE_PATH \
  --model-parallel 8 --expert-dtype fp4 --tokenizer-path $HF_CKPT_PATH
./inference/run.sh $SAVE_PATH        # 默认 MP=8，可 MP=4 覆盖
```

> 注意：`inference/generate.py` 通过 `sys.path.insert(../encoding)` 引用仓库根的 `encoding/` 目录，**目录结构不可再扁平化**。

## 学习笔记

- **架构全景**：`docs/dsv41-ch2-architecture-mindmap.html`（第二章 Architecture 思维导图，可交互折叠；2026-09-22 扩写 2.3 / 2.4）
- **CED 学习记录**：`docs/dsv41-ch2-CED-学习笔记.md`（2.2 CED 自测 8 题 + replay 概念 + CED vs YoCo 两项改进）
- **CSA2 / SWA 学习记录**：`docs/dsv41-ch2-CSA2-SWA-学习笔记.md`（2.3 自测 10 题 + `_window_kv` 双返回值与 ring cache 机制 + 3 专题澄清：层间信息流动、多跳为何有损、win=128 vs Mistral 4096）
- **CSA2 Indexer 细读**：`docs/dsv41-ch2-CSA2-Indexer-学习笔记.md`（`Indexer.forward` 逐行：indexer K 发布 / Q 复用 / ReLU 打分 / `all_reduce`；两级 top-k 候选池；6 易错点 + 自测 6 题；含会话交接说明）
- **CSA2 三轴理解**（思维导图 2.3 + 对话沉淀）：`KV 字节 ≈ (bytes/entry) × (tokens/m) × L_own`；源码层分配 `kv_source_layers=[2,8,14,20]`（40 层仅 4 层自持 main KV）、`index_source_layers` 8 层产 Top-K
- **Single-Pass mHC 结构图**：`docs/dsv41-block-mhc.drawio`（两个子块各四步 `H → hc_pre 4→1 → F → hc_post 1→4`，B/C 就地写回、A 错位一拍交给下一子块；数据流 spec 见 `docs/dsv41-ch2-mHC-dataflow.json`）
- **Engram 数据流图**：`docs/dsv41-engram.drawio`（压缩词表 → 滚动 XOR 哈希 24 列 → 查 FP8 表 → wkv → gate → 写回残差流）
- **CSA2 数据流图**：`docs/csa2-dataflow.html`（2.3 单层数据流 + 跨层复用，spec 见 `docs/csa2-dataflow.json`）
- **创新点 → 源码坐标**（报告章节 → 代码位置）：

| 创新点 | 报告 | 源码 |
|---|---|---|
| CED 因果编解码器 | 2.2 | 仅技术报告 2.2（参考实现 `Transformer.forward` 未实现 CED；`kv_source_layers` 是 CSA2 层间复用，非 CED 投影） |
| CSA2 三模式（Full/Reindex/Reuse） | 2.3.1 | `inference/model.py` `Attention`(630，三模式判定 669–680) / `Indexer`(494) / `Compressor`(430) |
| 分层稀疏索引器 | 2.3.2 | `inference/model.py` `select_candidate_blocks`(599)；config candidate_* |
| Single-Pass mHC | 2.4.1 | `inference/model.py` `Block`(938) hc_mixes/pre/post；`kernel.py` hc_split_sinkhorn(469) |
| Engram 条件记忆（196B） | 2.4.2 | `inference/engram.py` `EngramLayout`(87) / `NgramHashState`(129)；`model.py` `Engram`(328) / `ParallelEngramEmbedding`(296) |
| DSpark 投机解码 | 2.4.3 | `inference/model.py` DSpark*（1064–1189）/ forward_spec(1309) |
| FP4 主 KV 缓存 | 2.4.4 | `inference/convert.py` cast_e2m1fn_to_e4m3fn(18)；`kernel.py` fp4 系列 |
| head-wise Muon / Sinkhorn 优化 | 2.5 | 报告 Algorithm 1（训练侧，代码不在仓库） |

> 上表行号按当前工作副本 `inference/model.py`（1333 行，含中文注释；已提交版 1328 行）核对；该文件若再增删行，需重新校准。

## 与官方仓库的差异

| 缺失项 | 说明 |
|---|---|
| `examples/` | 示例输入（example.txt / example_harmony.json），可从 HF 补 |
| `evaluation/` | DeepSWE v1.1 复现说明（dsh-minimal + Pier patch），可从 HF 补 |
| 模型权重 | 全量 510 GB / 48 分片，需自行下载 |
| `assets/` | README 中的两张对比图（README_hf.md 引用） |

其他说明：官方仓库有 `Tech_Report.pdf` 与 `DeepSeek_V41_Tech_Report.pdf` 两份同名内容（已校验文本一致），本仓库仅保留官方命名的后者；`LICENSE` 已按官方 MIT（Copyright (c) 2023 DeepSeek）补齐。

## 相关链接

- 模型仓库：[deepseek-ai/DeepSeek-V4.1-Flash · HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- Prompt 生产级编码库（Rust）：[deepseek-ai/deepseek-recipe](https://github.com/deepseek-ai/deepseek-recipe)
- 官方模型卡（英文）：[`README_hf.md`](./README_hf.md)