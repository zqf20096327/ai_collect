<p align="center">
  <img src="docs/title_banner.png" alt="LoRA-CosyVoice123 Chanting 艺术字标题和阿拉斯加小狗吉祥物" width="1000">
</p>

<p align="center">
  <sub>🦇 <em>"Why do we fall, sir? So that we can learn to pick ourselves up."</em></sub>
</p>

<p align="center">
  <strong>面向中文古诗词吟诵的 CosyVoice 1/2/3 LoRA 微调实验框架</strong><br>
  <em>把三代论文读进代码里：架构差异、token 布局、prompt 边界、吟诵评估</em>
</p>

<p align="center">
  <a href="README.en.md">English</a> |
  <a href="#这个项目真正想回答什么">项目问题</a> |
  <a href="#使用的-hugging-face-基座模型">基座模型</a> |
  <a href="#论文阅读给出的五个微调判断">论文判断</a> |
  <a href="#三代-cosyvoice-为什么不能一套经验打天下">三代差异</a> |
  <a href="#代码如何适配三代架构">代码适配</a> |
  <a href="#吟诵专用评估公式">评估公式</a> |
  <a href="#试听演示">试听演示</a> |
  <a href="#快速开始">快速开始</a>
</p>

---

## 这个项目真正想回答什么

这个仓库关心的是：**当 CosyVoice 从第一代走到第二代、第三代以后，微调的有效位置、错误形态和评估方式为什么都会变？**

中文古诗词吟诵有长时值拖腔、滑音、慢起音、类颤音 F0 起伏和强音色保持需求，与普通朗读不同。普通 TTS 微调里常见的”听起来像不像””字准不准”不够用；要判断模型是否学会吟诵，必须同时看 speech token 长度、prompt 边界、Flow/DiT 声学建模、F0 轨迹和试听内容覆盖。

本项目的价值在于：**同一份吟诵数据、同一套 LoRA 框架，横向比较 CosyVoice 1、CosyVoice 2、CosyVoice 3 三代，并把论文中的架构差异落实成可运行的训练、推理和诊断代码。**

<p align="center">
  <img src="docs/cosyvoice123_architecture_poster.png" alt="LoRA-CosyVoice123 Chanting 工程架构海报" width="1000">
</p>

---

## 使用的 Hugging Face 基座模型

本项目的 LoRA 在三代 CosyVoice 官方 Hugging Face 权重之上做轻量微调。三代模型对应关系如下：

| 实验代际 | 本项目本地权重目录 | Hugging Face 模型 | 说明 |
|---|---|---|---|
| CosyVoice 1 | `cosy1_weight/` | [`FunAudioLLM/CosyVoice-300M`](https://huggingface.co/FunAudioLLM/CosyVoice-300M) | 第一代 300M 基座，项目中的 `Cosy1-LoRA` 在此基础上挂载 LLM/Flow LoRA |
| CosyVoice 2 | `cosy2_weight/` | [`FunAudioLLM/CosyVoice2-0.5B`](https://huggingface.co/FunAudioLLM/CosyVoice2-0.5B) | 第二代 0.5B 基座，使用 Qwen/FSQ 相关结构，项目中的 `Cosy2-LoRA` 在此基础上微调 |
| CosyVoice 3 | `cosy3_weight/` | [`FunAudioLLM/Fun-CosyVoice3-0.5B-2512`](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512) | 第三代 0.5B 基座，包含 Cosy3 的 DiT-CFM 声学骨干；`Cosy3-LoRA`、`Ablation-LLM`、`Ablation-DiT` 都来自这一代 |

此外，官方 CosyVoice 运行链路还依赖文本前端/资源包 [`FunAudioLLM/CosyVoice-ttsfrd`](https://huggingface.co/FunAudioLLM/CosyVoice-ttsfrd)。如果读者要从零复现权重下载，可以优先参考这四个 Hugging Face 仓库与本项目的本地目录对应关系。

---

## 论文阅读给出的五个微调判断

### 1. Cosy1 到 Cosy3 是声学骨干换代

CosyVoice 第一代采用“text-to-token LM + token-to-speech conditional flow matching”的两阶段框架。这个思想非常重要：LLM 负责把文本变成语义 speech tokens，Flow 再把 tokens 渲染成 Mel/波形。

<p align="center">
  <img src="docs/paper_figures/cosy1_fig1_page.png" alt="CosyVoice 第一代论文 Figure 1 页面截图" width="720">
</p>

但是第一代的 Flow 侧主要还是卷积/U-Net 风格的局部声学建模。早期我微调 Cosy1 时总觉得 LoRA 改变有限，一个重要原因就是：**如果主要可塑空间落在局部 CNN/局部窗口里，LoRA 对全局拖腔、长句节奏和整句吟诵走向的影响天然受限。**

到了 CosyVoice3，论文明确把 CFM 骨干升级为 Diffusion Transformer，也就是 DiT。DiT 的全局注意力更适合让 LoRA 影响整句声学结构，而不只是局部纹理。

<p align="center">
  <img src="docs/paper_figures/cosy3_fig2_detail_page.png" alt="CosyVoice3 论文训练流程与 DiT 页面截图" width="720">
</p>

因此本项目的一个核心判断是：**Cosy3 的 DiT-CFM 比 Cosy1/2 的局部 Flow 更适合吟诵风格 LoRA，尤其是拖腔、滑音、句内能量走向这种需要全局建模的特征。**

### 2. Cosy2 的 streaming/non-streaming token 布局会直接影响 prompt leakage

CosyVoice2 论文 Figure 2 讨论 unified streaming / non-streaming text-speech LM。它的关键是：**text tokens 和 speech tokens 在 LM 输入序列中如何摆放。**

<p align="center">
  <img src="docs/paper_figures/cosy2_fig2_page.png" alt="CosyVoice2 unified streaming and non-streaming LM 页面截图" width="720">
</p>

论文给出的逻辑可以简化成：

```text
Non-streaming:
S, all text tokens, T, all speech tokens, E

Streaming:
S, text chunk N, speech chunk M, fill, text chunk N, speech chunk M, ..., T, remaining speech, E

CosyVoice2 paper setting:
N:M = 5:15
```

这解释了本项目 debug 中遇到的 prompt leakage：如果只截取 prompt 音频前 3 秒，却给完整 prompt 文本，那么 LM 看到的实际上下文是”音频只覆盖了前半截，但文本还剩后半截”的错配状态。在 streaming 或续写式布局下，模型很容易先把 prompt 剩余文本补成 speech tokens，再把这些 tokens 接到上下文里传给 Flow/CFM，于是目标音频开头会听到 prompt 后半句残留。

更严谨地说：**streaming 的交错式 text/speech token 布局会放大”截断 prompt audio + 完整 prompt text”这种不一致条件的风险，这是 prompt leakage 的重要成因。**

所以本项目推理路径采用：

```text
安全策略:
完整 cross-sample prompt audio
+ 与该 prompt audio 完全匹配的 prompt text
+ target text 单独输入

避免:
截断 prompt audio
+ 完整 prompt text
```

如果不追求超低延迟，吟诵任务更适合优先采用 non-streaming / unistream 思路：让模型先看到更完整的文本和 prompt 边界，再生成目标 speech tokens。吟诵比口语更依赖长程节奏，长程建模优先于低延迟。

### 3. 25 Hz speech tokens、50 Hz Mel 和 5:15 chunk ratio 不能混为一谈

这里需要特别严谨。CosyVoice2/3 论文都写到 speech tokenizer 的 token rate 是 **25 Hz**，也就是每秒约 25 个 speech tokens；Mel 特征是 **50 Hz**，所以 Flow/CFM 里通常需要把 speech token 表示上采样到 Mel 帧率。

```text
论文中的物理速率:
speech token rate ~= 25 tokens/s
mel frame rate    ~= 50 frames/s
=> 1 speech token ~= 2 mel frames
```

而 streaming LM 里的 `N:M = 5:15` 描述的是”每 N 个 text tokens 后面交错 M 个 speech tokens”的训练/推理序列布局，与 text token 到 Mel frame 的采样率无关。

吟诵的困难在于：一行很短的文本可能对应很长的声学展开。我的数据分析发现，Cosy3 吟诵样本的 `speech_token_len / text_token_len` 中位数约为 14.5。也就是说，一个文本 token 附近可能对应远多于普通朗读的 speech token 空间。

```text
普通流式假设:
5 text tokens -> 15 speech tokens
约等于每个 text token 分到 3 个 speech tokens

吟诵数据观测:
median speech/text ratio ~= 14.5
长拖腔样本甚至更高
```

所以我后来把 Cosy3 LLM 训练改成 unistream-only：官方 `5:15` 针对普通流式语音很合理，但对”短文本、长声学跨度”的吟诵小样本 LoRA 来说，交错式布局会增加跳字、漏字、提前结束和补读风险。

### 4. Cosy2 相比 Cosy1 的 tokenizer 与 LM 结构变化很大，不能复用一套矩阵假设

CosyVoice2 把第一代的 VQ 思路升级为 FSQ，并改用 Qwen2.5-0.5B 作为 text-speech LM 骨干。论文里 Table 4/7 说明 FSQ 更充分利用 codebook，并显著改善内容一致性。

<p align="center">
  <img src="docs/paper_figures/cosy2_fig1_2_page.png" alt="CosyVoice2 Figure 1 和 FSQ/LM 结构页面截图" width="720">
</p>

这直接影响工程实现：Cosy1、Cosy2、Cosy3 的 text tokenizer、speech token size、LLM hidden size、Flow 输入帧率、STFT 参数、LoRA pattern 都不同，不能仅靠更换 checkpoint 路径来适配。

```python
# experiments/features.py
if model_type == "cosy1":
    sample_rate=22050, n_fft=1024, hop=256, win=1024
elif model_type == "cosy2":
    sample_rate=24000, n_fft=1920, hop=480, win=1920
else:
    sample_rate=24000, n_fft=1920, hop=480, win=1920
```

```python
# experiments/models/base.py 的核心差异
Cosy1:
  speech_token_size = 4096
  LLM hidden        = 1024
  Flow input rate   = 50
  LoRA targets      = Transformer/Conformer + CNN Flow

Cosy2:
  speech_token_size = 6561
  LLM hidden        = 896
  mix_ratio         = [5, 15]
  Flow token rate   = 25, token_mel_ratio = 2

Cosy3:
  speech_token_size = 6561
  LLM hidden        = 896
  mix_ratio         = [5, 15]
  Flow backbone     = DiT-CFM
  LoRA targets      = Qwen LM + DiT linear blocks
```

这也是本项目开源价值比较突出的地方：它把三代架构都接入同一个 LoRA 实验框架，并为每一代写了不同的矩阵形状、特征参数和 LoRA 注入规则。

这些参数是三代模型的”结构契约”。如果其中一个契约错了，轻则音色变差，重则直接出现维度错误、token/Mel 对不齐、生成音频过短或 prompt 泄露。

**特征参数为什么三代不同**

| 参数 | 在结构中的功能 | Cosy1 设置 | Cosy2/3 设置 | 为什么不能混用 |
|---|---|---:|---:|---|
| `sample_rate` | Mel、F0、vocoder 保存音频时使用的采样率 | 22050 | 24000 | 官方权重训练时的声学前端不同；采样率错会让 Mel 帧时间和 vocoder 输出都错位 |
| `n_fft` | STFT 频谱分析窗口对应的 FFT 点数 | 1024 | 1920 | Cosy2/3 的 24 kHz 前端使用更长窗口；沿用 Cosy1 的 1024 会触发 window/FFT 不匹配或频谱分辨率错误 |
| `hop_size` | 相邻 Mel 帧之间的采样点间隔 | 256 | 480 | `256/22050≈11.6ms`，`480/24000=20ms`；它决定 Mel 帧率和 Flow 训练目标长度 |
| `win_size` | STFT Hann window 长度 | 1024 | 1920 | 必须与官方 Matcha/CosyVoice 前端一致，否则会出现 `expected window size` 类错误 |
| `num_mels` | Mel 频带数，也是 Flow/DiT 输出通道数 | 80 | 80 | 三代都输出 80 维 Mel，因此 Flow 输出层和 vocoder 都围绕 80 维构建 |
| `fmax` | Mel 滤波器最高频率 | 8000 | Cosy2 为 8000，Cosy3 为 None | Cosy3 本地配置允许使用完整高频范围；硬套 Cosy2 的 `fmax=8000` 可能改变高频音色 |

这就是为什么 `features.py` 按权重目录自动判断版本，不使用全局采样率和 STFT 参数。最初 Cosy2 报过 `n_fft=1920` 但 window 还是 `[1024]` 的错误，本质就是跨代复用了 Cosy1 的前端缓存。

**LLM 与 speech token 参数是什么意思**

| 参数 | 结构功能 | Cosy1 | Cosy2 | Cosy3 | 微调含义 |
|---|---|---:|---:|---:|---|
| `speech_token_size` / `vocab_size` | 离散 speech token 词表大小，也是 LM 输出分类空间和 Flow token embedding 输入空间 | 4096 | 6561 | 6561 | Cosy1 的 VQ codebook 是 4096；Cosy2/3 的 FSQ codebook 是 6561。LoRA checkpoint 不能跨词表加载 |
| `llm_input_size` / `llm_output_size` | text-speech LM 内部 hidden size | 1024 | 896 | 896 | 决定注意力层、MLP 层和 LoRA A/B 矩阵形状；Cosy1 的 LoRA 权重不可能直接加载到 Cosy2/3 |
| `text_token_size` | 文本 token 词表大小 | 51866 | Qwen tokenizer 管理 | Qwen tokenizer 管理 | Cosy1 走 Whisper/text encoder 风格，Cosy2/3 依赖 `CosyVoice-BlankEN` 的 Qwen tokenizer |
| `mix_ratio=[5,15]` | streaming LM 中 text chunk 与 speech chunk 的交错比例 | 无 | 有 | 有 | 这是 Cosy2/3 unified streaming/non-streaming LM 的核心布局参数；吟诵长拖腔会让默认比例变得紧张 |
| `length_normalized_loss=True` | CE loss 是否按长度归一化 | True | True | True | 避免长音频样本因为 token 更多而在 loss 中天然权重过大 |
| `lsm_weight=0` | label smoothing 权重 | 0 | 0 | 0 | 这里保持官方权重加载契约，不额外改变目标分布 |

这里最重要的是 `speech_token_size` 和 `llm_input_size`。LoRA 的低秩矩阵本质上挂在 Linear 层上，Linear 层输入输出维度一变，LoRA 的 `A/B` 形状就变。因此三代 checkpoint 不能互相复用，甚至同一代里 rank/alpha 不一致也会加载失败。

**Flow / CFM 参数在做什么**

| 参数 | 结构功能 | Cosy1 | Cosy2 | Cosy3 | 为什么重要 |
|---|---|---:|---:|---:|---|
| `input_frame_rate` | Flow 侧接收 speech tokens 的时间速率 | 50 | 25 | 25 | Cosy1 token 侧约 50 Hz；Cosy2/3 tokenizer 论文明确是 25 Hz |
| `token_mel_ratio` | 一个 speech token 对应多少个 Mel 帧 | 无显式设置 | 2 | 2 | Cosy2/3 是 25 Hz token 到 50 Hz Mel，所以需要 2 倍上采样 |
| `pre_lookahead_len` | causal 模式下提前看的未来 token 数 | 无 | 3 | 3 | 给流式/因果模块一点未来信息，减少 chunk 边界断裂 |
| `static_chunk_size` | 流式 chunk 的固定窗口大小 | Cosy1 非主线 | encoder 25 / decoder 50 | DiT 50 | 对齐 25 Hz token 和 50 Hz Mel 的 chunk 处理；太小会破坏长程上下文，太大增加延迟/显存 |
| `spk_embed_dim` | speaker embedding 维度 | 192 | 192 | 192 | CAM++ embedding 的维度契约，speaker conditioning 必须匹配 |
| `in_channels=240` | CFM 条件输入通道组合 | 240 | 240 | 240 | 通常来自 Mel、mask/condition 等 80 维通道组合，错了会直接维度不匹配 |

Cosy2 和 Cosy3 都是 25 Hz speech token、50 Hz Mel，但它们的 Flow 骨干不同：Cosy2 是 causal CNN/Transformer 风格的 chunk-aware Flow，Cosy3 换成 DiT-CFM。这个差异决定了 LoRA 策略：Cosy2 主要挂 Flow CNN/局部模块，Cosy3 可以挂 DiT transformer blocks，让风格微调影响更全局的声学轨迹。

**DiT 参数为什么适合吟诵 LoRA**

```python
estimator = DiT(
    dim=1024,
    depth=22,
    heads=16,
    dim_head=64,
    ff_mult=2,
    mel_dim=80,
    mu_dim=80,
    spk_dim=80,
    out_channels=80,
)
```

| 参数 | 结构功能 | 吟诵微调意义 |
|---|---|---|
| `dim=1024` | DiT 主干 hidden width | 决定声学表示容量，LoRA 在这些大 Linear 层上能影响更丰富的风格维度 |
| `depth=22` | Transformer block 层数 | 层数越深，越能建模长程声学依赖；吟诵拖腔和整句走势需要这种深层建模 |
| `heads=16` / `dim_head=64` | 多头注意力结构 | 允许模型在不同注意力头中关注音色、节奏、局部发音和长程旋律 |
| `ff_mult=2` | FFN 扩张倍率 | 控制每层非线性变换容量，LoRA 挂在 FFN/Linear 上时会影响声学细节生成 |
| `mel_dim=80` / `out_channels=80` | 输入/输出 Mel 维度 | 与声学前端和 vocoder 的 80 维 Mel 契约保持一致 |
| `mu_dim=80` | 条件均值/语义条件维度 | 连接 speech token 条件与 CFM 生成路径 |
| `spk_dim=80` | speaker 条件投影维度 | 把 192 维 speaker embedding 投影到 DiT 可用的声学条件空间 |

这就是我认为 Cosy3 值得单独强调的原因：Cosy1/2 的 Flow LoRA 更偏局部声学修补，Cosy3 的 DiT LoRA 更可能改变整句级别的韵律、拖腔和能量走向。

**LoRA pattern 为什么要分三套**

```python
LLM_V1_PATTERNS  -> text_encoder / TransformerLM 的 ESPnet-style Linear
LLM_V23_PATTERNS -> Qwen2.5 的 q_proj/k_proj/v_proj/o_proj 和 MLP
FLOW_CNN         -> Cosy1/2 的局部 Flow/CNN/decoder 模块
FLOW_DIT_V3      -> Cosy3 的 DiT transformer_blocks / final_proj
```

LoRA 只能注入到实际存在的 `nn.Linear` 或可替换线性层里。Cosy1 的模块名像 `self_attn.linear_q`，Cosy2/3 的 Qwen 模块名像 `self_attn.q_proj`，Cosy3 DiT 又有自己的 `transformer_blocks`。如果 pattern 写错，最好的情况是 LoRA 没挂上，最坏的情况是只训练了不该训练的层，最后看起来“训练正常”，但音频完全没有学到目标风格。

### 5. 吟诵不能只看 CER/WER，需要专门的声学评估公式

吟诵里“字对了”不等于“吟诵风味对了”。一句诗可以字准，但拖腔、滑音、颤音、起声方式完全不像。因此本项目把评估重点转移到 F0 轨迹、长音、频谱和起声边界。

这些指标把”听起来哪里不对”拆成可解释的声学证据。

---

## 三代 CosyVoice 为什么不能一套经验打天下

| 版本 | 论文里的核心变化 | 微调时最容易踩的坑 | 本项目处理方式 |
|---|---|---|---|
| CosyVoice1 | supervised semantic token + text-to-token LM + CFM | Flow 局部建模限制，LoRA 对整句拖腔影响有限 | LLM + Flow-CNN LoRA，作为第一代基线 |
| CosyVoice2 | FSQ、Qwen LM、unified streaming/non-streaming、causal Flow | prompt 截断会造成续写式泄露，5:15 交错布局不适合所有吟诵 | 完整 prompt audio/text 配对，区分 25 Hz token 与 50 Hz Mel |
| CosyVoice3 | MinMo-FSQ tokenizer、DiT-CFM、DiffRO/post-training、百万小时扩展 | 小数据 LLM-LoRA 容易跳字、漏字、提前 EOS | Cosy3 LLM 采用 unistream-only 训练补丁，DiT 侧单独做 LoRA |

### Ablation-LLM 与 Ablation-DiT 的对比价值

最新试听样例里，`Ablation-LLM` 的质量明显弱于 `Ablation-DiT`：前者更容易时长偏短、内容覆盖不足、吟诵味不稳定；后者反而更容易保持完整文本，同时呈现更接近吟诵的声学风格。这个现象说明 Cosy3 微调时 **LLM 侧和 DiT-CFM 侧承担的是两种不同风险**。

```text
LLM side:
text -> speech tokens
决定说什么、token 序列多长、是否过早 EOS、是否跳字漏字

DiT-CFM side:
speech tokens -> Mel / acoustic realization
决定拖腔、滑音、起声、音色纹理、能量走势
```

`Ablation-LLM` 只微调上游 text-to-speech-token LM。吟诵里一个字可能对应很多 speech tokens，小数据 LoRA 很容易扰动原本稳定的文本到 token 对齐。一旦 LLM 生成的 speech tokens 数量偏少，或者提前采到 EOS/stop token，后面的 CFM/DiT 再强也只能渲染一段短音频。因此它的短时长和”不对味”是因为上游 token 序列本身已经不够完整，而非 vocoder 的问题。

`Ablation-DiT` 则保留 base LLM，只微调 DiT-CFM。这等于保留大规模预训练/后训练得到的内容稳定性，同时让声学渲染器学习吟诵的拖腔、滑音和能量形态。因此它的主观质量更好，说明对当前小样本吟诵任务来说，**DiT 侧 LoRA 是比 LLM 侧 LoRA 更稳健的风格迁移入口**。

这组消融的价值在于，它把“内容稳定性”和“声学风格迁移”拆开了：如果只改 LLM，容易破坏内容和时长；如果只改 DiT，反而更可能在不破坏文本覆盖的前提下学到吟诵味。后续更合理的方向是优先强化 DiT 侧，或者降低 LLM-LoRA 学习率、减少 LLM 可训练层数，把 LLM 作为内容稳定器。

---

## 代码如何适配三代架构

### LoRA 挂载按代际区分

```text
Group 1: Cosy1-LoRA     = CosyVoice1 + LLM LoRA + Flow-CNN LoRA
Group 2: Cosy2-LoRA     = CosyVoice2 + Qwen LLM LoRA + Flow-CNN LoRA
Group 3: Cosy3-LoRA     = CosyVoice3 + Qwen LLM LoRA + DiT LoRA
Group 4: Ablation-LLM   = CosyVoice3 + only LLM LoRA
Group 5: Ablation-DiT   = CosyVoice3 + only DiT LoRA
```

```python
# experiments/models/base.py
LLM_V1_PATTERNS = [
    "text_encoder.encoders.*.self_attn.linear_q",
    "llm.encoders.*.self_attn.linear_q",
    "llm.encoders.*.feed_forward.w_1",
]

LLM_V23_PATTERNS = [
    "llm.model.model.layers.*.self_attn.q_proj",
    "llm.model.model.layers.*.mlp.up_proj",
    "llm.model.model.layers.*.mlp.down_proj",
]

FLOW_DIT_V3_PATTERNS = [
    "decoder.estimator.transformer_blocks",
    "decoder.estimator.final_proj",
]
```

### Cosy3 的 unistream-only 训练补丁

Cosy3 官方 LM target 会混合 unistream 与 bistream。我的吟诵数据里 speech/text ratio 明显偏高，因此主流程默认打开 unistream-only patch：

```python
# experiments/train.py
if objective_plan.train_llm and detect_model_type(weight_dir) == "cosy3":
    patch_cosy3_lm_unistream_only()
```

它的核心目标是让 Cosy3 LLM 先看完整文本，再预测 speech tokens：

```text
unistream target:
SOS + instruction + full text + task id + full speech tokens + EOS

why:
吟诵一字多 token，交错式 chunk target 容易让小数据 LoRA 学到跳读/补读
```

### Prompt 边界作为推理契约

```text
safe prompt contract:
prompt_audio = another complete chanting utterance
prompt_text  = transcript of that complete prompt_audio
target_text  = text to synthesize

unsafe:
prompt_audio = first 3 seconds only
prompt_text  = full transcript
```

这条规则来自论文中的 in-context / streaming sequence construction，也来自本项目实际 debug：截断 prompt audio 配完整 prompt text 时，生成开头会残留 prompt 后半句。

---

## 吟诵专用评估公式

本项目的指标实现主要在 [`experiments/metrics/chanting.py`](experiments/metrics/chanting.py)。核心原则是：吟诵生成和参考录音不可能逐帧等长，因此大多数曲线/频谱比较都先做 DTW 对齐。

| 指标 | 方向 | 关注点 |
|---|---:|---|
| `F0-DTW-RMSE` | 越低越好 | DTW 对齐后的基频曲线误差 |
| `TCC` | 越高越好 | F0 一阶变化连续性，近似衡量滑音平滑度 |
| `GDE` | 越低越好 | 平滑 F0 趋势误差 |
| `VRE` | 越低越好 | 颤音速率误差 |
| `VDE` | 越低越好 | 颤音幅度误差 |
| `SS` | 越高越好 | CAM++ speaker embedding 余弦相似度 |
| `DTW-LMD` | 越低越好 | DTW 对齐后的 log-Mel L1 距离 |
| `NBE` | 越低越好 | 首个有声起点附近的归一化能量突变 |

几个关键公式可以这样理解：

```text
F0-DTW-RMSE:
先用 DTW 找到预测 F0 与参考 F0 的时间对齐路径 P
再计算路径上的 RMSE

sqrt( mean_{(i,j) in P} (F0_pred[i] - F0_ref[j])^2 )
```

```text
GDE:
先对 F0 做移动平均，得到更像“吟诵旋律走向”的平滑曲线
再做 DTW-RMSE

RMSE( smooth(F0_pred), smooth(F0_ref) )
```

```text
VRE / VDE:
F0 - smooth(F0) 得到局部周期性残差
VRE 比较残差过零率对应的颤音频率
VDE 比较残差标准差对应的颤音幅度
```

```text
NBE:
找到首个有声 onset
取 onset 附近短窗口能量
除以全局平均能量做归一化
计算局部能量斜率最大值

它比固定前 100ms 能量跳变更适合慢起音和前置静音的吟诵录音。
```

`CER/WER` 仍然重要，但需要可靠 ASR 后端。没有 ASR 时，本项目不会伪造这些结果。

### 当前客观评估结果

本次评估直接读取 `outputs/listening_samples/` 中已经生成的 5 组试听音频，不重新推理。完整 JSON 见 [`outputs/evaluation_results.json`](outputs/evaluation_results.json)，英文表见 [`outputs/evaluation_table.md`](outputs/evaluation_table.md)，中文表见 [`outputs/evaluation_table.zh-CN.md`](outputs/evaluation_table.zh-CN.md)。

<p align="center">
  <img src="outputs/figures/metrics_radar.png" alt="LoRA-CosyVoice123 chanting objective metrics radar plot" width="760">
</p>

| 指标 | 含义 | Cosy1-LoRA | Cosy2-LoRA | Cosy3-LoRA | Ablation-LLM | Ablation-DiT | 最优 |
|---|---|---:|---:|---:|---:|---:|---|
| **CER** | ASR 字错误率，越低越好 | - | - | - | - | - | - |
| **WER** | ASR 词错误率，越低越好 | - | - | - | - | - | - |
| **F0-DTW-RMSE** | DTW 对齐后的 F0 曲线误差，越低越好 | 47.73 | 55.06 | 56.18 | 61.77 | 65.45 | **Cosy1-LoRA** |
| **TCC** | F0 一阶差分连续性，越高表示滑音更平滑 | 0.1645 | 0.1238 | 0.2035 | 0.2566 | 0.1539 | **Ablation-LLM** |
| **LNDE** | 长有声片段相对时长误差，越低越好 | - | - | - | - | - | - |
| **GDE** | 平滑 F0 趋势误差，越低越好 | 40.15 | 47.39 | 48.14 | 55.53 | 58.58 | **Cosy1-LoRA** |
| **VRE** | 颤音速率误差，越低越好 | 0.54 | 0.91 | 0.42 | 1.15 | 0.71 | **Cosy3-LoRA** |
| **VDE** | 颤音深度误差，越低越好 | 9.57 | 6.66 | 9.17 | 9.78 | 11.66 | **Cosy2-LoRA** |
| **SS** | CAM++ 说话人相似度，越高越好 | 0.795 | 0.796 | 0.763 | 0.724 | 0.727 | **Cosy2-LoRA** |
| **DTW-LMD** | DTW 对齐后的 log-Mel L1 距离，越低越好 | 1.94 | 1.86 | 1.97 | 2.13 | 1.92 | **Cosy2-LoRA** |
| **PLR** | Prompt 泄露率，依赖 ASR/检索后端 | - | - | - | - | - | - |
| **NBE** | 起声边界能量斜率，越低越平滑 | 0.31 | 0.19 | 0.12 | 0.20 | 0.17 | **Cosy3-LoRA** |
| **Legacy-RCR** | 旧版 Mel 表征诊断，仅作历史对比 | 0.9551 | 0.9457 | 0.9549 | 0.9329 | 0.9515 | **Ablation-LLM** |
| **Legacy-BEJ** | 旧版前 100ms 能量跳变，仅作历史对比 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | **Ablation-LLM** |
| **Legacy-F0-RMSE** | 未经 DTW 的旧版逐帧 F0 RMSE | 94.92 | 91.52 | 101.11 | 120.64 | 117.52 | **Cosy2-LoRA** |

**如何解读这张表**

- `Cosy1-LoRA` 在 `F0-DTW-RMSE` 和 `GDE` 上最好，说明它和参考吟诵的 F0 轮廓更接近。不过 Cosy1 的声学骨干更局部，主观听感中的拖腔质感、音色和内容完整度仍要结合试听判断。
- `Cosy2-LoRA` 在 `DTW-LMD`、`SS` 和 `VDE` 上表现最好，说明它的频谱距离、说话人相似度和颤音深度更接近参考。这和 Cosy2 的 FSQ tokenizer、Qwen LM 以及更稳定的 token/Mel 对齐有关。
- `Cosy3-LoRA` 在 `VRE` 和 `NBE` 上最好，说明它在颤音速率和起声边界平滑性上更有优势。这个结果符合 DiT-CFM 更擅长建模全局声学形态的直觉。
- `Ablation-LLM` 的 `TCC` 最高，需要注意短音频或内容不完整的音频也可能产生更平滑的 F0 差分曲线，因此 TCC 必须和时长、内容覆盖、试听一起看。
- `Ablation-DiT` 的主观听感明显优于 `Ablation-LLM`，部分客观指标也未排第一。这提示当前指标能描述 F0、Mel、speaker similarity、onset 等局部维度，但”是否把整句诗完整、自然、有吟诵味地唱/诵出来”仍需人工判断。

**本次评估给出的实验结论**

这组结果支持一个重要消融判断：在小样本吟诵风格迁移中，`Ablation-DiT` 比 `Ablation-LLM` 更稳，因为它保留 base LLM 的文本到 speech token 稳定性，只让 DiT-CFM 学声学风格；而 `Ablation-LLM` 直接扰动上游 text-to-token LM，更容易带来短时长、漏字、提前停止和吟诵味不足。换句话说，本项目当前最有价值的方向是优先研究 DiT 侧 LoRA 如何学习拖腔、滑音、起声和音色纹理。

---

## 工程架构树

```text
吟诵 WAV + TXT 成对数据
        |
        v
特征前端
        |-- Whisper log-mel -> speech tokenizer
        |-- speech tokens -> LLM 监督学习
        |-- CAM++ embedding -> speaker identity
        |-- Matcha-style Mel -> Flow/DiT 训练与评估
        |
        v
三代 CosyVoice LoRA 通道
        |-- Cosy1-LoRA: LLM + Flow-CNN
        |-- Cosy2-LoRA: Qwen LLM + Flow-CNN
        |-- Cosy3-LoRA: Qwen LLM + DiT
        |-- Ablation-LLM: only Cosy3 LLM
        |-- Ablation-DiT: only Cosy3 DiT
        |
        v
训练 / 推理 / 诊断
        |-- outputs/<group>/<group>_lora.pt
        |-- outputs/listening_samples/*.wav
        |-- outputs/evaluation_results.json
        |-- debug/duration + debug/cosy3_llm
```

---

## 试听演示

下表链接 `outputs/listening_samples/` 中的试听样例。GitHub README 有时不会内嵌播放器，但点击链接可以打开或下载音频。

<sub>说明：不同样例时长不同是正常现象。CosyVoice 先自回归生成可变长度 speech tokens，再由 Flow/DiT 和 vocoder 转成波形。LoRA 挂载位置、prompt 条件、EOS/stop token 和解码长度都会影响最终时长。</sub>

<sub>如果你已经删除 RAG 组并重新生成试听样例，当前推荐文件编号是：`01_Cosy1`、`02_Cosy2`、`03_Cosy3`、`04_Ablation-LLM`、`05_Ablation-DiT`。</sub>

<div style="overflow-x: auto; width: 100%; padding-bottom: 0.5rem;">
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>目标文本</th>
      <th>Prompt 文本</th>
      <th>Cosy1-LoRA</th>
      <th>Cosy2-LoRA</th>
      <th>Cosy3-LoRA</th>
      <th>Ablation-LLM</th>
      <th>Ablation-DiT</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>01</td><td>一之日于貉，取彼狐狸，为公子裘</td><td>月明星稀乌鹊南飞绕树三匝何枝可依</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample01.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample01.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample01.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample01.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample01.wav">音频</a></td></tr>
    <tr><td>02</td><td>一水护田将绿绕，两山排闼送青来</td><td>月有盈亏花有开谢，想人生最苦离别</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample02.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample02.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample02.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample02.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample02.wav">音频</a></td></tr>
    <tr><td>03</td><td>一道残阳铺水中，半江瑟瑟半江红</td><td>月未到诚斋，先到万花川谷</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample03.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample03.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample03.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample03.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample03.wav">音频</a></td></tr>
    <tr><td>04</td><td>七月流火，九月授衣</td><td>有女怀春，吉士诱之</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample04.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample04.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample04.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample04.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample04.wav">音频</a></td></tr>
    <tr><td>05</td><td>上之回，大旗喜。悬虹彗，挞凤尾。剑匣破，舞蛟龙</td><td>朝为越溪女，暮作吴宫妃</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample05.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample05.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample05.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample05.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample05.wav">音频</a></td></tr>
    <tr><td>06</td><td>上穷碧落下黄泉，两处茫茫皆不见</td><td>朱户黏鸡，金盘簇燕，空叹时序侵寻</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample06.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample06.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample06.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample06.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample06.wav">音频</a></td></tr>
    <tr><td>07</td><td>不是诚斋无月，隔一林修竹</td><td>来往不逢人，长歌楚天碧。</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample07.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample07.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample07.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample07.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample07.wav">音频</a></td></tr>
    <tr><td>08</td><td>不畏浮云遮望眼</td><td>来疑沧海尽成空，万面鼓声中</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample08.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample08.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample08.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample08.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample08.wav">音频</a></td></tr>
    <tr><td>09</td><td>不闻爷娘唤女声，但闻黄河流水鸣溅溅</td><td>杨家有女初长成，养在深闺人未识</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample09.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample09.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample09.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample09.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample09.wav">音频</a></td></tr>
    <tr><td>10</td><td>不露文章世已惊，未辞翦伐谁能送</td><td>杨柳青青江水准，闻郎江上唱歌声</td><td><a href="outputs/listening_samples/01_Cosy1-LoRA_sample10.wav">音频</a></td><td><a href="outputs/listening_samples/02_Cosy2-LoRA_sample10.wav">音频</a></td><td><a href="outputs/listening_samples/03_Cosy3-LoRA_sample10.wav">音频</a></td><td><a href="outputs/listening_samples/04_Ablation-LLM_sample10.wav">音频</a></td><td><a href="outputs/listening_samples/05_Ablation-DiT_sample10.wav">音频</a></td></tr>
  </tbody>
</table>
</div>

---

## 快速开始

### 1. 创建环境

```powershell
conda create -n ragcosy python=3.10 -y
conda activate ragcosy
pip install -r requirements.txt
```

### 2. 准备官方权重

请分别下载 CosyVoice 1/2/3 官方权重，并放到：

```text
cosy1_weight/
cosy2_weight/
cosy3_weight/
```

### 3. 准备数据

```text
data/chanting/example_001.wav
data/chanting/example_001.txt
```

### 4. 训练或推理

训练 Cosy3、Ablation-LLM、Ablation-DiT 三组：

```powershell
python -u -B -m experiments.run --groups 3,4,5 --epochs 50 --train-only --output outputs
```

单独推理 Ablation-LLM 并保存试听音频：

```powershell
python -u -B -m experiments.run --eval-only --eval-group 4 --eval-samples 10 --save-audio --output outputs
```

训练并推理单组：

```powershell
python -u -B -m experiments.run --group 4 --epochs 50 --eval-group 4 --eval-samples 10 --save-audio --output outputs
```

---

## 调试工具

```powershell
python -m debug.duration.analyze_outputs --listening-dir outputs/listening_samples
python -m debug.duration.probe_inference_lengths --group 3 --sample-index 0 --prompt-index 100 --output outputs
python -m debug.cosy3_llm.analyze_dataset_ratios --group 3 --limit 200 --output-json outputs\debug\cosy3_llm\ratios_g3_full.json
python -m debug.cosy3_llm.inspect_lm_targets --sample-index 0 --prompt-index 100
```

---

## 文件结构

```text
lora-cosyvoice123-chanting/
|-- README.md                 # 中文默认首页
|-- README.en.md              # 英文文档
|-- experiments/              # 训练、推理、评估主流程
|-- debug/                    # duration 与 Cosy3 LM 诊断工具
|-- docs/                     # 论文、图示、指标说明
|-- data/chanting/            # 本地吟诵数据，不提交
|-- cosy1_weight/             # 官方权重，不提交
|-- cosy2_weight/
|-- cosy3_weight/
|-- outputs/                  # 指标、图表、试听样例
`-- daily_log.md              # 工程调试时间线
```

---

## 重要说明

- 官方 CosyVoice 权重不随仓库分发，请遵守上游许可证。
- 本地吟诵数据不随仓库分发。
- LoRA checkpoints、训练日志、大型报告和临时 debug 产物默认不提交。
- 本项目已移除 RAG 实验组，当前重点是 LoRA-CosyVoice 1/2/3 的三代架构对照。

---

## 文档

- [Quick Start](docs/QUICKSTART.md)
- [Metrics](docs/METRICS.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [工程调试日志](daily_log.md)

---

<p align="center">
  <strong>如果这个项目能帮你少踩一点 CosyVoice 微调的坑，欢迎 star。</strong>
</p>
