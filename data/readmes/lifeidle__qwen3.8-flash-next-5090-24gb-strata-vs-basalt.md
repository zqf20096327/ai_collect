# Qwen3.8-Flash-Next · RTX 5090 Laptop 24GB · Strata vs Basalt

> 同一台 **24GB 笔记本**，同一个 **177B MoE**，只换推理引擎：
> 单路 **96.1 → 143.3 tok/s（+49%）**，双路聚合 **67.5 → 163.9 tok/s（+143%）**，
> 并且把"3 路 × 96K 长上下文同时跑"从会崩变成可用；8 路 × 13 万 token 也能一次跑通。
>
> 全部数字来自本机实测（同一台机器、同一批模型文件、可复现命令在文末）。
> 中英双语 · 迭代记录见 [docs/](docs/) · 模型文件来自 Unsloth / ISTA-DASLab 的公开 GGUF 重打包。

---

## 最终选择（TL;DR）

| 场景 | 引擎 / 模型 / 并发 | 实测 |
|---|---|---|
| **两个窗口日常聊** | Basalt · UD-IQ1_S · 双路 256K · spec 2 | **每路 ~110 tok/s**（短请求），长上下文 114-144 |
| **三窗口读长文档** | Basalt · UD-IQ1_S · 3 路 · spec 9 | 每路 ~50 tok/s，Σ 178（96K 热态） |
| **批量短请求** | Basalt · UD-IQ1_S · 8 路 · spec 8 | Σ **279 tok/s** |
| **追质量（top-1 88.7%）** | Basalt · UD-IQ3_XXS · 单路/短上下文 | 每路 96（200K 双路），注意 RAM 余量 |
| **不再使用** | Strata 0.1.55（Windows） | 双路 67.5，串行抢占 |

![Strata vs Basalt](assets/figs/fig1-strata-vs-basalt.svg)

---

## 硬件与环境

| 项 | 值 |
|---|---|
| GPU | RTX 5090 Laptop **24 GB**（GDDR7，WDDM） |
| 内存 | 63.4 GB（DDR5，双通道） |
| 存储 | NVMe（模型盘 D:，读 ~2 GB/s） |
| CPU | 无 AVX-512（引擎全程走 AVX-2 内核，日志有 warning） |
| 系统 | Windows 11 原生（非 WSL2、非容器） |
| 引擎 | Basalt 0.3.3（Windows x64 原生）；对照 Strata 0.1.44→0.1.55 |
| 模型 | Qwen3.8-Flash-Next 177B MoE · `.basalt` 官方包（Unsloth UD-IQ1_S / UD-IQ3_XXS / ISTA-DASLab IQ3_S） |

**为什么能跑**：专家权重按热度分层——显存放得下的部分常驻，其余放**锁页内存**，SSD 上只留 n-gram 查找表按需读。三个量化在该机上 SSD 常驻专家都是 **0%**（见第七节）。

---

## 一、Strata 时代：96 → 67 的"双路悖论"

Strata 在这台机器上跑了 5 个版本（0.1.44.1 → 0.1.55）。可用、但双路是个悖论：

| 版本 | 单路 | 双路聚合 | 说明 |
|---|---:|---:|---|
| 0.1.44.1 | 97.7 | — | 双路被守卫强制降级到 2×128K |
| 0.1.50 | 93.1 | 67.0 | 真 2×256K 解锁，但聚合低于单路 |
| 0.1.52 | 96.1 | — | 单路基线 |
| **0.1.55** | 96.1 | **67.5** | Windows 上无变化（1.45x 并发提升是 Linux 专属） |

**双路为什么比单路还慢**：batch2 时 expert cache 被压到 2161 槽 / 4.15 GB（KV 窗口挤占显存），两个请求实为**串行抢占**——各自接近全速（66.6），但时间不重叠，聚合锁死在 67。满仓双灌（245K/槽、46.9 万 token 在线）时两路 decode 63/81，同样受限于缓存。

---

## 二、Basalt 登场：单路 143 / 双路 164

`Basalt 0.3.3` Windows 原生，官方 `.basalt` 包（一个文件装权重 + tokenizer + MTP 起草器 + hc8 + 视觉投影器）。

| | Strata 0.1.55 | **Basalt 0.3.3** | 变化 |
|---|---:|---:|---:|
| 单路 | 96.1 | **143.3**（141.4/152.8/143.3） | **+49%** |
| 双路聚合 | 67.5 | **163.9**（84.9/路） | **+143%** |
| 双路 > 单路？ | ❌（67.5 < 96.1） | ✅（163.9 > 143.3） | 真批处理 |
| 130K 长文 prefill | ~2700 tok/s | **3716 tok/s** | +38% |
| 短请求 TTFT | 30 s（WSL2）/ 0.1 s | **0.1 s** | — |

关键机制差异：Basalt 用**自适应专家分层**（VRAM ↔ 锁页 RAM 之间按热度交换，日志 `0 blob reads from the file`），Strata 在 Windows 上把专家缓存压得很小。双路不再是"串行"，而是真正的 batch 解码。

---

## 三、三个量化的真实差距

双路、每路灌满 20~26 万 token、vision 开、int8 KV、spec 8：

![三个量化对比](assets/figs/fig2-models-long-context.svg)

| 模型 | 文件 | 专家总量 | 每路 tok/s | 聚合 | 接受率 | 质量 top-1 | 结论 |
|---|---:|---:|---:|---:|---:|---:|---|
| **UD-IQ1_S** | 65.6 GiB | 31.1 GiB | **104.8** | **167.9** | 72.4% | 82.76% | 最快、内存余量大、可撑 8 并发 |
| **UD-IQ3_XXS** | 81.6 GiB | 46.8 GiB | 96.4 | 137.2 | 59.8% | **88.67%** | 质量最高，但 RAM 吃紧 |
| **IQ3_S** | 81.6 GiB | 46.8 GiB | 89.0 | 136.1 | 57.1% | 87.56% | 被 IQ3_XXS 全面压制 |

**结论**：`UD-IQ3_XXS` 是 `IQ3_S` 的直接替代（同专家量、质量更高、略快）；`UD-IQ1_S` 是速度档，比质量档快 10~25%，代价是 top-1 低 6 个百分点。

---

## 四、并发：短请求与长上下文是两条相反的曲线

### 短请求（71 token 提示、800 token 生成）

![短请求并发阶梯](assets/figs/fig3-concurrency-short.svg)

| 路数 | 1 | 2 | 3 | 4 | 8 |
|---|---:|---:|---:|---:|---:|
| 每路 tok/s | **171.5** | 102.3 | 71.6 | 54.3 | 35.6 |
| 聚合 tok/s | 171.5 | 194.6 | 210.4 | 206.8 | **278.9** |

- 聚合随并发上升，每路单调下降
- **3 路（210.4）> 4 路（206.8）**：4 路是 24GB 显存账上的坏点（KV 15.2GiB 把专家挤到内存），要并发就跳过 4

### 长上下文（每路 96K，热态真并发）

| 路数 | 每路 | 聚合 | 评价 |
|---:|---:|---:|---|
| **3** | **42.0** | **132.9** | 🏆 长上下文甜点 |
| 4 | 31.5 | 130.1 | 吞吐持平、每路慢 25% |
| 8 | 11.8 | 101.9 | 最差：KV 挤爆显存 |

**与短请求完全相反**：短请求 8 路聚合最高（279），96K 长上下文 8 路反而最差（102），3 路最优（133）。原因：96K × 8 路要 15.2 GiB KV，显存里的专家被全挤到内存，每路都在走 PCIe。

### 容量上限（能不能跑通）

| 组合 | 结果 |
|---|---|
| 双路 × 258,772 token | ✅ 稳定 |
| **8 路 × 254,699 token** | ✅ 8/8 一次成功（各槽实读 25.5 万） |
| 4 路 × 240K | ✅ 成功（读入 77-360 s） |
| 3 路 × 260K / 200K / 128K | ❌ **引擎静默崩溃**（200K 与 128K 同样崩） |

> 3 路长上下文崩溃是 Basalt 0.3.3 在该配置下的稳定性问题；双路与 8 路反而稳定——不是单调关系，`parallel` 的 `batch` 校验路径有差异。

---

## 五、冷态 vs 热态：之前的数字为什么虚高

![冷态 vs 热态](assets/figs/fig4-cold-vs-hot.svg)

| 路数 | 冷态 Σ | 热态 Σ | 虚高 |
|---|---:|---:|---:|
| 3 | 209.4 | **132.9** | −37% |
| 4 | 236.9 | **130.1** | −45% |
| 8 | 210.8 | **101.9** | −52% |

**冷态时**：N 个请求里有几个还在 prefill（几乎不占解码算力），剩下的在 decode 时**独占 GPU**——所以能冒出 142 tok/s 那种漂亮数字，但无法复现（8 路两次冷测 164.7 vs 256.9，相差 56%）。

**热态时**：所有路同时 decode，才是窗口同时生成的真实体验。热态 5 轮波动仅 ±5-10%。

**这条教训比任何单个数字都重要**：长上下文并发必须用热态测量，冷态只能回答"能不能跑通"。

---

## 六、spec 精调：3 路 × 96K 全档

![spec 全档](assets/figs/fig5-spec-3lane.svg)

| spec | 2 | 3 | 4 | 5 | 6 | 7 | 8（默认） | **9** | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Σ tok/s | 155.4 | 145.4 | 162.5 | 173.4→157.3 | 160.1 | 154.7 | 156.6 | **170.6→177.6** | 73.0→151.4 | 154.5 | 163.1 |
| 接受率 | 67.7% | **74.6%** | 72.8% | 65.0% | 63.1% | 60.6% | 63.9% | 66.3→73.1% | 62.9% | 65.7% | 63.0% |

- **最优：`--spec 9`**（两次 170.6 / 177.6，范围 ±11%）
- **最稳：`--spec 4`**（162.5，范围 ±8%，接受率 72.8%）
- **接受率最高：`--spec 3`**（74.6%，但每路只有 45）
- 官方默认 `spec 8` 只是中游（156.6）
- `spec 10` 首测 73.0 是**环境异常**（冷态建 KV 的 Σ 只有 87.7，正常 200-270），复测 151.4 恢复正常

---

## 七、专家分层：显存 / 内存 / SSD

![专家分布](assets/figs/fig6-expert-placement.svg)

| 模型 | 专家总量 | VRAM | RAM（走 PCIe） | SSD | 日志证据 |
|---|---:|---:|---:|---:|---|
| IQ1_S | 31.1 GiB | 15.9 GiB (51%) | 15.2 GiB (49%) | **0** | `0 blob reads from the file` |
| IQ3_XXS | 46.8 GiB | 15.8 GiB (34%) | 31.1 GiB (66%) | **0** | 同上 |
| IQ3_S | 46.8 GiB | 16.0 GiB (34%) | 30.8 GiB (66%) | **0** | 同上 |

**这是全篇最重要的机制解释**：
- 三个量化都**没有专家落 SSD**，SSD 上只有 28.8 GiB 的 n-gram 查找表（按需读几行）
- 差距在"多少专家留在内存、每 token 走一遍 PCIe"：IQ1_S 只 49%，IQ3_XXS/IQ3_S 有 66%
- 这也解释了 `IQ3_XXS` 的 500 错误：它需要 31.1 GiB 常驻 RAM，63.4 GB 机器上 pin 满就没有缓冲，任何后台程序吃掉 1.5 GB 就会撞上引擎的 RAM 守卫：

```
error: engine reported RAM low (1948 MiB free < 2048 MiB guard):
request stopped; other programs took 1543 MiB since the engine was ready
```

- 调低守卫会更糟：`--ram-reserve-mib 512` → auto 贪心 pin 47.1 GB 直接 OOM；`resident-budget 30` → 544 个专家落 SSD，96K prefill 卡死 6 分钟

---

## 八、KV 格式与视觉

### KV 精度（官方标定 + 本机实测）

| 格式 | dKLD [95% CI] | top-1 | 官方判定 | 本机可用性 |
|---|---|---:|---|---|
| **int8**（现用） | **+0.0000** [−0.0010, +0.0010] | **+0.15** | **lossless** | 多路唯一支持，单路最快（171.5） |
| k8v4 | +0.0056 [+0.0038, +0.0073] | −0.20 | measurable | **batch 不支持** |
| q4_0 | +0.0093 [+0.0074, +0.0112] | −0.38 | measurable | batch 不支持；单路 154.7（比 int8 慢 10%） |

- `q4_0` / `k8v4` 在 ≥2 路时引擎直接拒绝：`batch windows need INT8 K/V without rotation`
- int8 相对 fp16 是**无损压缩**（KV 显存减半），这个便宜已经占到了

### 视觉

`.basalt` 单文件自带视觉投影器，配置写 `"vision": "dynamic"`（在 `models[]` 条目内，写 `server` 块会报错）：

- 空闲时 0 显存、约 0.85 GiB 锁页内存；用图时借专家缓存槽位
- 实测：48 KB JPEG → **2.1 s** 端到端、847 prompt tokens、prefill 5381 tok/s，描述准确
- 视频需 FFmpeg 6/7/8 DLL（`avformat-62/61/60.dll`），缺则 `video off`（不影响图片）

---

## 九、最终配置矩阵与启动器

| 用途 | 配置文件 | 命令 |
|---|---|---|
| 日常双窗口 | `basalt_config_iq1s_dual_vis.v2.json` | `serve --config ... --spec 2` |
| 三窗口长文档 | `cfg_iq1s_p3_96k.v2.json` | `serve --config ... --spec 9` |
| 八路批量 | `cfg_iq1s_cap8.v2.json` | `serve --config ... --spec 8` |

桌面启动器（双击即用，自动清端口 → 起服务 → 等加载 → 开浏览器）：

```
IQ1S-3路-256K-spec9 启动.bat
```

---

## 十、测量方法论（踩过的坑，按代价排序）

1. **冷态会骗人**：长上下文并发必须热态测量（缓存命中、纯 decode）。冷态虚高 37-52%，且不可复现。
2. **单轮不可信**：同一配置同一轮次可差 ±27%。至少 5 轮取中位，同时记录范围。
3. **先看 coldΣ 再信结果**：如果冷态建 KV 的 Σ 只有正常值 30-40%，说明启动环境异常（显存残留），该轮作废。
4. **别信"接受率最高"**：接受率高 ≠ 吞吐高。spec 2/3 接受率最高，但每窗口产出 token 少，总吞吐反而低 5-10%。
5. **`timings.prompt_ms` 在 8 路长 prompt 下会失真**（曾报出 220 万 tok/s），用端到端 wall 算。
6. **强杀进程会让 profile/缓存不落盘**：`taskkill /F` 不给引擎优雅退出机会；`expert-profile-save` 需 ≥1 分钟周期才写盘。
7. **仓库改名后 PUT 走 ID**：GitHub contents API 对新名字 PUT 会 307，用 `repositories/{id}/contents/...`。
8. **中文 Windows 的 netstat 是 GBK**：Python `text=True` 会 UnicodeDecodeError，要 `bytes.decode('gbk')`。

---

## 复现

```powershell
# 1) 下载 Basalt 0.3.3 Windows x64 与官方 .basalt 包（见 docs/）
# 2) 双路日常
cd D:\Strata\basalt-win\basalt-v0.3.3-windows-x64
.\bin\basalt.exe serve --config basalt_config_iq1s_dual_vis.v2.json `
  --python "D:\Strata\app\.venv\Scripts\python.exe" --api-key <KEY> --spec 2

# 3) 三窗口长文档（本仓库推荐的长上下文配置）
.\bin\basalt.exe serve --config cfg_iq1s_p3_96k.v2.json `
  --python "D:\Strata\app\.venv\Scripts\python.exe" --api-key <KEY> --spec 9
```

配置要点（v2 格式）：

```json
{ "version": 2,
  "engine": { "expert-cache": "auto", "prefill": "auto", "resident-experts": true },
  "models": [{ "model": "…/Qwen3.8-FN-UD-IQ1_S.basalt", "kv": "int8",
               "max-context": 262144, "parallel": 3, "slot-full-context": true,
               "vision": "dynamic" }],
  "server": { "host": "0.0.0.0", "port": 8080 } }
```

---

## 历史记录

本仓库 2026-09-11 → 11-13 的完整迭代（llama.cpp 时代 27 tok/s → Strata 双路 256K 解锁 → 引入 Basalt）见 [docs/history-legacy.md](docs/history-legacy.md)。

## 致谢与声明

- 模型：Qwen3.8-Flash-Next（阿里通义千问）· GGUF 量化来自 Unsloth（UD 系列）与 ISTA-DASLab（IQ3_S）
- 引擎：[Basalt](https://github.com/jesdga95/basalt) 0.3.3 · [Strata](https://github.com/Niko1221/Strata) 0.1.44→0.1.55
- 所有数字为本机实测；官方标定数据（KV 精度、质量 top-1/KLD）引自 Basalt 与 Unsloth 文档，已注明
- 未测量声明：Windows 画质/质量门未跑（官方声明 Windows 不测质量）；3 路长上下文崩溃未定位到具体栈
