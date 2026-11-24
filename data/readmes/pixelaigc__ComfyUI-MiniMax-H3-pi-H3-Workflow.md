# ComfyUI MiniMax H3 · pi-H3 Workflow

<div align="center">

**MiniMax H3 首尾帧视频生成工作流｜FL2VA · 同步音频 · 2/4 步加速**

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Workflow-2ea44f?style=flat-square)](https://github.com/comfyanonymous/ComfyUI)
[![MiniMax H3](https://img.shields.io/badge/MiniMax-H3-7c3aed?style=flat-square)](https://huggingface.co/Comfy-Org/MiniMax-H3)
[![pi-H3](https://img.shields.io/badge/pi--H3-2%20%7C%204%20Steps-06b6d4?style=flat-square)](https://huggingface.co/Lakonik/pi-H3)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078d4?style=flat-square)](#windows-注意事项)

[中文](#中文说明) · [English](#english-summary)

</div>

![pi-H3 workflow overview](assets/pi-H3-Workflow.png)

## 中文说明

这是一个面向 **MiniMax H3** 的 ComfyUI **FL2VA（First/Last Frame to Video and Audio）** 工作流。它可以根据提示词与首帧、尾帧生成带同步音频的视频，并通过 pi-H3 Adapter 将采样压缩到 **2 步或 4 步**。

### 工作流亮点

- 支持首帧、尾帧或首尾帧联合约束
- 视频与音频同步生成
- pi-H3 2-step / 4-step Adapter 可切换
- 使用 Sol Block Sparse Attention 加速采样
- 使用 DWD Decode 降低长视频解码压力
- 内置画幅、分辨率、时长和提示词控制
- 针对 Windows + RTX 3060 12GB 做过实测

### 3060 12GB 实测

| 设置 | 耗时 / 能力 |
|---|---:|
| 768P · 8 秒 · 4 步 | 约 404 秒 |
| 768P · 8 秒 · 2 步 | 约 262 秒 |
| 480P · 2 步 | 可直接生成约 30 秒 |

> 实际速度和显存占用会受到 ComfyUI 版本、显卡驱动、显存状态、注意力实现与输出参数影响。

## 快速开始

### 1. 获取工作流

下载仓库中的工作流文件：

[`pi-H3-DWD-3060-2.json`](pi-H3-DWD-3060-2.json)

也可以克隆仓库：

```bash
git clone https://github.com/pixelaigc/ComfyUI-MiniMax-H3-pi-H3-Workflow.git
```

### 2. 导入 ComfyUI

1. 启动并更新到较新的 ComfyUI 版本。
2. 将 `pi-H3-DWD-3060-2.json` 拖入 ComfyUI 画布。
3. 如果出现缺失节点，使用 ComfyUI Manager 安装缺失的自定义节点，然后重启 ComfyUI。
4. 按下方目录放置模型文件，并刷新模型列表。

### 3. 安装必需节点

本工作流需要安装 **[ComfyUI-piFlow](https://github.com/Lakonik/ComfyUI-piFlow)**。

推荐通过 ComfyUI Manager 搜索 `ComfyUI-piFlow` 并安装；也可以进入 ComfyUI 的 `custom_nodes` 目录手动安装：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Lakonik/ComfyUI-piFlow.git
```

安装完成后请重启 ComfyUI。如果导入工作流后仍有红色节点，再通过 ComfyUI Manager 安装提示的其他缺失节点。

### 4. 下载模型

| 类型 | 模型 | 保存位置 |
|---|---|---|
| Base model | [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | `models/diffusion_models/` |
| pi-H3 2-step | [pi_h3_2step_dwd_adapter_int8_convrot.safetensors](https://huggingface.co/Lakonik/pi-H3/resolve/main/pi_h3_2step_dwd_adapter_int8_convrot.safetensors) | `models/loras/` |
| pi-H3 4-step | [pi_h3_4step_dwd_adapter_int8_convrot.safetensors](https://huggingface.co/Lakonik/pi-H3/resolve/main/pi_h3_4step_dwd_adapter_int8_convrot.safetensors) | `models/loras/` |
| Text encoder | [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | `models/text_encoders/` |
| Video VAE | [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | `models/vae/` |
| Audio VAE | [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | `models/vae/` |

模型目录结构：

```text
ComfyUI/
└── models/
    ├── diffusion_models/
    │   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors
    ├── loras/
    │   ├── pi_h3_2step_dwd_adapter_int8_convrot.safetensors
    │   └── pi_h3_4step_dwd_adapter_int8_convrot.safetensors
    ├── text_encoders/
    │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    └── vae/
        ├── minimax_h3_video_vae_int8_convrot.safetensors
        └── minimax_h3_audio_vae_fp32.safetensors
```

完整精度的 Adapter 也可以使用：

- [2-step full precision](https://huggingface.co/Lakonik/pi-H3/resolve/main/pi_h3_2step_dwd_adapter/diffusion_pytorch_model.safetensors)，保存为 `models/loras/pi_h3_2step_dwd_adapter.safetensors`
- [4-step full precision](https://huggingface.co/Lakonik/pi-H3/resolve/main/pi_h3_4step_dwd_adapter/diffusion_pytorch_model.safetensors)，保存为 `models/loras/pi_h3_4step_dwd_adapter.safetensors`

## 使用方法

1. 在 **First frame** 节点加载首帧。
2. 在 **Last frame** 节点加载尾帧。
3. 在 pi-H3 生成节点中设置：
   - `steps`：选择 2 步或 4 步模式；
   - `aspect_ratio`：输出画幅；
   - `megapixels`：目标分辨率；
   - `seconds`：视频时长；
   - `prompt`：画面、动作、对白与声音描述。
4. 运行工作流，在预览节点检查画面、声音和时长。
5. 在 **保存视频** 节点设置文件名前缀、格式与编码器。

### 2 步与 4 步

`steps` 会选择对应的 pi-H3 Adapter 与推荐参数：

| 模式 | 推荐 `max_raw_t` | 特点 |
|---|---:|---|
| 2 steps | `0.93` | 更快，适合快速测试和长时长输出 |
| 4 steps | `0.96` | 采样更充分，耗时更长 |

工作流中的 `final_step_size_scale` 为 `0.6`；`ModelSamplingMiniMaxH3` 默认使用视频 shift `12`、音频 shift `3`。

## Windows 注意事项

> [!IMPORTANT]
> Windows 推荐使用 **Sol-Attn + DWD** 路线。Spark-Attn 节点在 Windows 环境中可能报错，请勿启用。

- `Model Sparse Attention (Sol)` 用于加速采样；如果环境不兼容，可以绕过该节点改用 Dense Attention。
- DWD 用于视频解码路径，尤其适合显存有限或较长视频的场景。
- 首次运行前请确保模型名称与工作流中选择的名称一致。

## 提示词建议

建议在提示词中明确写出：

- 输出时长、画幅、帧率与清晰度
- 人物、场景、动作和镜头运动
- 分镜时间段与对白
- 环境声、对白音色和背景音乐
- 首尾帧之间需要保持一致的主体特征

> 提示词中的规格描述不会替代工作流参数。最终画幅、分辨率和时长仍应以节点设置为准。

## English Summary

This repository provides a ComfyUI FL2VA workflow for **MiniMax H3 + pi-H3**. It generates synchronized video and audio from a text prompt, optionally conditioned on a first frame, a last frame, or both.

Key features:

- First/last-frame conditioning
- Synchronized video and audio generation
- Switchable pi-H3 2-step and 4-step adapters
- Sol block-sparse attention for faster sampling
- DWD decoding for memory-conscious video output
- Tested on Windows with an RTX 3060 12GB

Import [`pi-H3-DWD-3060-2.json`](pi-H3-DWD-3060-2.json) into ComfyUI, install any missing custom nodes, download the models listed above, select your input frames, and run the workflow.

## Related Projects

- [ComfyUI-MiniMax-H3-Workflow](https://github.com/pixelaigc/ComfyUI-MiniMax-H3-Workflow)
- [ComfyUI-MiniMax-H3-Studio](https://github.com/pixelaigc/ComfyUI-MiniMax-H3-Studio)
- X / Twitter: [@PixelAigc](https://x.com/PixelAigc)
- Contact: [ai@pixelaigc.cc](mailto:ai@pixelaigc.cc)

## Credits & License Notice

- MiniMax H3 models: [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)
- pi-H3 adapters: [Lakonik/pi-H3](https://huggingface.co/Lakonik/pi-H3)
- ComfyUI: [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

模型文件不包含在本仓库中。请分别遵守 ComfyUI、MiniMax H3、pi-H3 及相关模型和自定义节点的许可证与使用条款。

