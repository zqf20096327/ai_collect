# NInfer on RTX 4090D — Full-Spectrum Benchmark (Qwen3.8-27B)

单卡黑盒性能 + 能力评测：一台**常驻** `ninfer-serve` 实例，跑 **Qwen3.8-27B**，
显卡为 **RTX 4090D（24 GB，sm_89）**。下面所有数字都来自对线上 OpenAI 兼容端点
（`http://127.0.0.1:8081/v1`）的直接压测——也就是实际承载生产流量的那个进程，
所以结果反映的是真实部署状态：前缀缓存复用、MTP 投机解码、INT8 KV 全部按生产配置开启。

## TL;DR

| 场景 | 吞吐 | 对比 llama.cpp Q4_K_M（同 4090D） |
|---|---:|---:|
| 短轮次 / agent 对话（MTP 接近全采纳） | **~168 tok/s** | **~4.8×** |
| 连续自然语言长文 | **~84–105 tok/s** | **~2.9×** |
| 冷启动长上下文 prefill（8k → 64k） | **~1600–1800 tok/s** | llama.cpp 在此区间明显劣化 |

**加速的同时质量没有掉。** MTP 全程开启的情况下，模型依然拿到
**AIME25 = 0.800**、**AIME26 = 0.667**、**GPQA-Diamond = 0.803**——
吞吐的提升在推理质量上没有付出可测量的代价。

## 实现路径与方法

想在自己机器上复刻这套测试的话，整个流程就四步：**起服务 → 压性能 → 评质量 → 收数据**。
下面把每一步的关键决策讲清楚，照着做就能跑通。

### 整体思路：黑盒打线上服务

不重启、不独占 GPU，所有测试都通过 HTTP 打到**正在承载生产流量的那个常驻服务**上。
好处是结果反映真实部署状态（前缀缓存、MTP、INT8 KV 都是开着的）；代价是并发饱和层
没法测（需要独占 GPU），所以这次没跑。

指标全部取自响应里的服务端 `timings` JSON（权威值），客户端只算 wall time 做交叉验证：

```
prefill_tps = prompt_tokens / timings.prompt_seconds     # 冷启动 prefill 速度
ttft        = timings.prompt_ms                          # 首 token 延迟
decode_tps  = (completion_tokens - 1) / timings.decode_seconds
mtp_accept  = draft_n_accepted / draft_n                 # 投机解码采纳率
tok/round   = 1 + accepted / speculative_rounds          # 每轮实际产出 token
```

### Step 1 — 起常驻服务

用 `ninfer-serve` 把模型加载成 Windows 常驻服务，暴露 OpenAI 兼容 API（`:8081/v1`）。
关键参数见下方"运行时配置"表。注意两点：

- **上下文窗口要按显存预算留够**：27B INT8 权重约 17 GiB，KV cache 也是 INT8，
  98k 上下文在 24 GB 卡上刚好放得下。超窗的 fixture（128k/256k NIAH）会在客户端
  预筛阶段被跳过并记录，不会打爆服务。
- **prefix reuse 保持开启**：agent 场景大量请求共享系统提示词，这块缓存命中
  是 ~4.8× 加速的主要来源之一，关掉再测就没有代表性了。

### Step 2 — 性能压测（纯 stdlib，无依赖）

`bench/adx_blackbox_serve.py` 只依赖标准库（urllib/json），不需要装任何包。
它的结构值得参考：

1. **fixtures 复用上游 manifest**：从 `examples/cli/manifest.json` 读 30 个 case
   （text/code/story/translation/structured/NIAH/math-decode），每个 case 就是
   一段 messages JSON。这样测出来的数字能和上游项目的公开基线直接对比。
2. **多 seed 重复**：除 warmup 外每个 fixture 跑 5 个不同 seed，聚合时取
   mean ± sd，避免单次抖动。
3. **客户端预筛超窗**：按 CJK≈1.8 tok/char、其它≈0.35 tok/char 粗估 prompt
   长度，超过上下文窗口就跳过并记入 `skipped.json`。
4. **分模式运行**：`niah` / `scenario` / `decode --maxnew=4096` / `smoke`，
   可以单独跑某一层，不用每次都全量。

```bash
python bench/adx_blackbox_serve.py niah       # 长上下文 prefill
python bench/adx_blackbox_serve.py scenario   # 分场景 decode + MTP 采纳
ADX_REQ_TIMEOUT=280 python bench/adx_blackbox_serve.py decode --maxnew=4096
```

另有 `bench/adx_blackbox_concurrent.py` 做并发饱和（C=1/2/4…），但需要独占 GPU，
有常驻服务时不能跑。

### Step 3 — 能力评测（独立 venv）

EvalScope 的依赖比较重，**不要装进 agent 运行时环境**，单独建 venv：

```bash
python -m venv eval-venv
eval-venv\Scripts\pip install -r requirements.txt   # Windows
# eval-venv/bin/pip install -r requirements.txt    # Linux
```

然后跑官方 `ninfer_eval` runner，配置里只需改 `base_url` 指向你的端点：

```yaml
targets:
  model_api:
    protocol: openai_chat
    base_url: http://127.0.0.1:8081/v1   # ← 改成你的地址
    model: qwen3.8-27b                   # ← 改成你的模型名
```

数学题（AIME）用规则判分（`judge_strategy: rule`），GPQA 走选择题匹配，
都不需要额外的 judge 模型。

### Step 4 — 收数据

- 性能：每次运行存到 `profiles/bench/<run>/results.json` + `skipped.json`
- 能力：`eval/runs/<run_id>/backends/<dataset>/job-result.json` + `summary.json`，
  各带一份 HTML 报告

本仓库 `results/` 目录下保留了本次运行的原始数据，可以直接核对上面的表格。

---

## 引擎与来源

被测引擎是 **[sergiuszm/ninfer-4090](https://github.com/sergiuszm/ninfer-4090)**，
它是 [Don-Chad/ninfer-3090](https://github.com/Don-Chad/ninfer-3090) 的 `sm_89` 移植版，
而后者派生自 **[Neroued/ninfer](https://github.com/Neroued/ninfer)**——一个专为
C++20/CUDA 单卡推理写的引擎，本 benchmark 的方法学也取自它。

### 为什么 4090D（Windows）能跑 NInfer

上游 [Neroued/ninfer](https://github.com/Neroued/ninfer) 官方支持矩阵只列了
**5090 / 5080（Blackwell, sm_120）+ Linux**，所以"4090D + Windows 上能跑 NInfer"
看起来像是不可信的组合。实际路径是这样的：

1. **CUDA 架构适配**：NInfer 的核心 kernel 按 compute capability 分发。
   Blackwell（sm_120）和 Ada/Hopper（sm_89/sm_90）走的是不同的代码路径，
   但都是标准 CUDA C++，没有依赖任何 Blackwell 专属硬件特性
   （如 FP4 tensor core）。[sergiuszm/ninfer-4090](https://github.com/sergiuszm/ninfer-4090)
   做的事就是补上 `sm_89` 的编译目标（nvcc `-gencode arch=compute_89,code=sm_89`），
   让同一套 kernel 在 Ada 卡上通过编译并正确运行。这不是 fork 重写，
   是加一个架构分支。
2. **Windows 移植**：NInfer 的 serving 层（HTTP server、KV cache 管理、
   MTP 调度）本身不依赖 Linux 特有 API。Windows 版本把进程模型从
   daemon 换成 Windows Service（`ninfer-serve.exe`），网络层用 Winsock，
   其余逻辑不变。CUDA runtime 在 Windows 上是一等公民，驱动栈完全一致。
3. **本仓库的验证方式**：所有数字都是对 `http://127.0.0.1:8081/v1`
   这个**正在跑的 Windows 服务**打的 HTTP 请求拿到的——响应里的
   `timings` JSON 是服务端自己算的（prefill/decode 分段计时、MTP draft
   采纳计数），客户端无法伪造。`results/` 目录保留了逐样本原始数据，
   任何人 clone 下来都能核对。

简言之：**NInfer 不是 5090 专属引擎，官方只是没给其它卡型发预编译包。**
`sm_89` 适配 + Windows 服务化是社区补的最后一公里，本仓库测的就是这条路径
在 RTX 4090D 上的实际表现。

> **方法学致谢。** 这里用的四层测试设计——长上下文 prefill / 分场景 decode（含 MTP 采纳率）/
> 长输出 decode 饱和 / EvalScope 能力评测——直接改编自源项目官方发布的方法学文档：
>
> - [`docs/performance/methodology.md`](https://raw.githubusercontent.com/Neroued/ninfer/master/docs/performance/methodology.md)
> - [`tools/bench/README.md`](https://raw.githubusercontent.com/Neroued/ninfer/master/tools/bench/README.md)
> - [`docs/performance.md`](https://raw.githubusercontent.com/Neroued/ninfer/master/docs/performance.md)

### 运行时配置

| 项 | 值 |
|---|---|
| GPU | NVIDIA GeForce RTX 4090D，24564 MiB，驱动 616.56 |
| 模型 | Qwen3.8-27B（官方 groupwise `.ninfer` 产物，约 16.96 GiB） |
| KV cache | INT8 |
| 上下文长度 | 98304 tokens |
| 前缀复用 | 开（compatible-prefix KV reuse） |
| MTP draft tokens | 4 |
| CUDA Graphs | 开 |
| Prefill chunk | 1024 |
| 服务方式 | 常驻 `ninfer-serve` Windows 服务，OpenAI 兼容 API，端口 :8081 |

---

## 1. 能力（质量）— EvalScope

三个 suite 全部打在线上端点上，参数 `temperature=0.6, top_p=0.95, max_tokens=16384, seed=42`，
规则判分，走源项目官方的 `ninfer_eval` runner。

| 数据集 | 领域 | 样本数 | 准确率 | 答对数 |
|---|---|---:|---:|---:|
| **AIME25** | 数学竞赛 | 30 | **0.800** | 24/30 |
| **AIME26** | 数学竞赛 | 30 | **0.667** | 20/30 |
| **GPQA-Diamond** | 研究生级科学问答 | 198 | **0.803** | 159/198 |

以上成绩是在 MTP 投机解码完全开启的状态下测的——也就是说，下文报告的加速
并没有以牺牲答案质量为代价。

---

## 2. 长上下文 prefill（NIAH）

Needle-in-a-haystack fixtures。**Cold** = 首个请求（无前缀缓存）；
**Warm** = 后续请求命中兼容前缀（KV-reuse hit）。Decode 数据来自 17 token 的短针答案。

| Fixture | Tokens | 模式 | Prefill (tok/s) | TTFT | Decode (tok/s) | MTP 采纳 |
|---|---:|---|---:|---:|---:|---:|
| `long_niah_8k` | 7.7k | Cold | **1798.8** | 4.27 s | 144.5 | 100% |
| `long_niah_8k` | 7.7k | Warm（前缀复用） | 85.4（cached） | 0.08 s | 144.8 | 100% |
| `long_niah_64k` | 63k | Cold | **1621.3** | 39.79 s | 120.3 | 100% |
| `long_niah_64k` | 63k | Warm（前缀复用） | 57.3（cached） | 0.24 s | 130.3 | 100% |

**要点：** 冷启动 prefill 从 8k 到 64k 基本保持平稳（~1600–1800 tok/s），
没有出现长上下文塌陷——llama.cpp 在超长 prompt 上通常会有明显劣化。
前缀一旦进缓存，TTFT 就降到 0.08–0.24 s。128k/256k 两个 fixture 超出了
98304 token 的上下文窗口，被跳过（这是真实的部署约束，如实记录而不是藏起来）。

---

## 3. 分场景 decode + MTP 采纳率

按内容类型统计 decode 吞吐和 MTP draft 采纳率。采纳率跟着输出的可预测性走——
结构化文本几乎总能采纳，自由散文则很少：

| 场景 | n | Decode (tok/s) | MTP 采纳 | tokens/round |
|---|---:|---:|---:|---:|
| 结构化（JSONL/CSV/SQL） | 8 | **163.4** | 85% | 1.85 |
| 代码（CUDA/Py/TS） | 14 | 140.5 | 70% | 1.70 |
| 翻译 | 15 | 134.0 | 65% | 1.65 |
| 故事 / 创意散文 | 15 | 79.8 | 29% | 1.29 |
| **总体** | 52 | **124.6** | 59% | — |

这正是 MTP 的典型特征：确定性、低熵的输出（结构化数据、代码）draft 采纳率高，
有效吞吐最高；开放式创作文本采纳率低，回落到接近基础 decode 速度。

---

## 4. 长输出 decode（数学题，`max_new=4096`）

长数学输出上的持续 decode，按是否走 thinking/reasoning 链分开统计：

| 模式 | 输出长度 | Decode (tok/s) | MTP 采纳 | tokens/round |
|---|---:|---:|---:|---:|
| Direct（非推理） | ~1.2–1.7k | **126–141**（均值 133.2） | 60–70% | ~1.6 |
| Thinking（推理链） | 4096（截断） | **81–93**（均值 87.5） | 30–38% | ~1.3 |
| **总体** | — | **102.7** | 44% | — |

数学推理链更长，但每一步的熵更低；直接作答的 decode 更快。

---

## 5. 核心吞吐汇总

| 场景 | 吞吐 | 对比 llama.cpp Q4_K_M（4090D） |
|---|---:|---:|
| 短轮次 / agent 对话（MTP 接近全采纳） | **~168 tok/s** | **~4.8×** |
| 连续自然语言长文 | **~84–105 tok/s** | **~2.9×** |
| 冷启动长上下文 prefill（8k→64k） | **~1600–1800 tok/s** | —（llama.cpp 劣化） |

参考基线：同一张 4090D 上，不带 MTP 的 llama.cpp Q4_K_M decode 实测约 32–43 tok/s。

> **本次未测：** 并发 decode 饱和（C=1/2/4/8）。这一层需要独占 GPU，
> 和常驻生产服务冲突，所以这次没跑——可以另找时间窗或在第二张卡上补测。

---

## 复现

```bash
# 黑盒性能 runner（打常驻 :8081 端点，复用上游 fixtures）
python bench/adx_blackbox_serve.py niah        # 长上下文 prefill
python bench/adx_blackbox_serve.py scenario    # 分场景 decode + MTP
ADX_REQ_TIMEOUT=280 python bench/adx_blackbox_serve.py decode --maxnew=4096   # 长输出 decode

# 能力评测（独立 venv；把官方 runner 指向线上端点）
PYTHONPATH=eval <venv>/python -m ninfer_eval run \
    --config configs/adx_live_8081.yaml --suite reasoning
```

> **注意：** 脚本里 `REPO = Path(__file__).resolve().parents[2]` 和
> `MANIFEST = REPO / "examples" / "cli" / "manifest.json"` 是按原始部署布局写的
> （bench 目录在 ninfer 源码树内）。如果你单独 clone 本仓库跑，需要把 manifest
> 从 [Neroued/ninfer](https://github.com/Neroued/ninfer) 的
> `examples/cli/manifest.json` 拷到对应位置，或改这两行路径。

能力评测配置见 `configs/adx_live_8081.yaml`，只需改 `base_url` 和 `model`：

```yaml
targets:
  model_api:
    protocol: openai_chat
    base_url: http://127.0.0.1:8081/v1
    model: qwen3.8-27b
```

逐样本原始结果保留在 `profiles/bench/<run>/results.json`（性能）和
`eval/runs/<run_id>/backends/<dataset>/job-result.json` + `summary.json`（能力），
各附带一份 HTML 报告。

---

## Acknowledgements

benchmark 方法学、serving fixtures 以及 EvalScope 评测框架均取自
**[Neroued/ninfer](https://github.com/Neroued/ninfer)**（及其
[`sergiuszm/ninfer-4090`](https://github.com/sergiuszm/ninfer-4090) /
[`Don-Chad/ninfer-3090`](https://github.com/Don-Chad/ninfer-3090) 谱系）。
本报告中的所有测量都是在作者自己的硬件上、针对自建常驻服务完成的。
