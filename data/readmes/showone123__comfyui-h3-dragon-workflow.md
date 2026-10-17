# MiniMax H3 竖屏「奶龙」工作流（ComfyUI）

一个本地运行的 **MiniMax H3 R2V（参考生视频 / Reference-to-Video）** 竖屏工作流。
用一张参考图 + 一段提示词，生成 9:16 的短镜头视频。已针对 **8G 显存 / 24G 内存** 的 Windows 设备调优。

成品效果：一张「桌面上趴着一只黄色奶龙」的参考图 → 生成一段奶龙跳起来求抚摸、手轻轻摸头的 5 秒竖屏视频，带环境音。

---

## 硬件要求

| 项目 | 最低 | 说明 |
|---|---|---|
| 显存 | 8 GB | int8 量化版权重 + Turbo 4step，可跑 480×864 |
| 内存 | 16 GB | 推荐 24 GB |
| 磁盘 | ~60 GB | 模型权重体积大（见下） |
| 系统 | Windows（便携版 ComfyUI 已验证） | Linux / macOS 理论上可行 |

> 提示：8G 显存下不建议在工作流内做超分。先低分辨率生成，再用剪映「画质增强」/ Topaz 后期超分更稳。

---

## 依赖

### 1. ComfyUI 自定义节点

- **MiniMax H3 节点**（提供 `MiniMaxH3ReferenceToVideo`、`MiniMaxH3SigmaShift`、`MiniMaxH3TeaCache` 等）
- **ComfyUI-SolAttn_triton**（稀疏注意力加速 `SolAttnPatch`，需 Triton）

### 2. 模型权重（**不随本仓库提供，需自行下载**）

把以下文件放到 ComfyUI 的 `models/` 对应目录：

| 节点 | 文件名 | 目录 |
|---|---|---|
| UNET | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | `models/unet/` |
| CLIP | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `models/text_encoders/` |
| VAE (video) | `minimax_h3_video_vae_fp16.safetensors` | `models/vae/` |
| VAE (audio) | `minimax_h3_audio_vae_fp32.safetensors` | `models/vae/` |
| Turbo LoRA | `minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors` | `models/loras/` |

> 权重请从 MiniMax 官方发布渠道 / HuggingFace 获取，遵守其许可协议。

---

## 使用方法

1. **载入工作流**：在 ComfyUI 菜单 `Workflow → Open` 打开 `dragon_anime_ui_turbo.json`。
2. **放参考图**：双击 `LoadImage` 节点，选择你的参考图（建议一张清晰、背景简单的「奶龙趴桌上」照片或图）。
3. **关于 `<Picture 1>` 标签（重要）**：
   - 提示词里的 `<Picture 1>` 指的就是你接在 `ref_image_0` 槽位的那张参考图。
   - 节点槽位名 `ref_image_0`（0-based）和提示词标签 `<Picture 1>`（1-based）是**两套命名**，由 H3 节点自动对应，不要改成别的写法，否则参考图会失效。
   - 序号只数「实际连了线」的图；空槽不占位。
4. **运行**：`Queue Prompt`。输出视频在 `output/video/dragon_shot_*.mp4`。

### 可调参数（在 `MiniMaxH3ReferenceToVideo` 节点上）

| 参数 | 当前值 | 说明 |
|---|---|---|
| width × height | 480 × 864 | 32 倍数；8G 显存上限约 576×1024 |
| length | 124 | 帧数 @ 24fps ≈ 5 秒 |
| ref_image_size | match | `match`=缩到生成画面尺寸；`max`=2048 短边保真但更吃显存 |

---

## 提示词约定

- 中文提示词完全可用（底层是 Qwen3-VL-32B），且比英文更准。
- 必须显式写 `<Picture 1>` 来绑定参考图身份，否则模型会自由发挥、与参考图脱节。
- 未约束的维度（镜头运动 / 景别 / 时间节奏 / 画质）模型会自动补，建议写明「镜头固定不动」等约束。
- H3 是音视频联合生成，音频段请写具体的环境音（如"安静的室内氛围，温柔的轻音乐"），不要写"无"。
- 参考图里没有的新元素（如"手拿块肉"）必须显式描述，否则形态失控。

---

## 已知限制

- 本工作流**不含超分节点**，依赖后期处理提升分辨率。
- 需自行准备模型权重与自定义节点，仓库仅提供工作流与说明。
- Turbo LoRA 为 4 步蒸馏，过多步数反而可能劣化；当前 `BasicScheduler` 设 4 步。

---

## License

[MIT](./LICENSE)。工作流 JSON 与文档可自由使用、修改、再分发；模型权重遵循其各自的许可协议。
