# Blackwell llama.cpp Inference Container

[STATUS]: STABLE_RELEASE | [TARGET]: NVIDIA RTX 50 SERIES

[English](#overview) | [中文](#简介)

---

## Overview

A ready-to-run llama.cpp inference container for NVIDIA Blackwell GPUs (RTX 50 series). The image removes the need for manual compilation or CUDA environment setup.

- Pre-compiled llama.cpp with sm_120 support (`-DCMAKE_CUDA_ARCHITECTURES=120`)
- CUDA 12.8 toolchain and all system libraries baked in
- NVFP4 support compiled in (`-DGGML_CUDA_NVFP4=ON`)
- Built-in `llama-chat` wrapper script (readline support, thinking disabled in this build)

> This image is for inference only. Load the image, run the container, and use `llama-chat`.

---

## 简介

为 NVIDIA Blackwell GPU（RTX 50 系列）预构建的 llama.cpp 推理容器。镜像内已内置编译产物与 CUDA 12.8 运行库，无需手动编译或配置环境。

- 预编译 llama.cpp，启用 sm_120 指令集（`-DCMAKE_CUDA_ARCHITECTURES=120`）
- 内置 CUDA 12.8 工具链及全部动态库
- 已开启 NVFP4 编译支持（`-DGGML_CUDA_NVFP4=ON`）
- 内置 `llama-chat` 包装脚本（readline 支持，本构建默认关闭思考）

> 本镜像仅用于推理。加载镜像、启动容器、使用 `llama-chat` 即可。

---

## Quick Start / 快速开始

1. Download and merge / 下载并合并

从 [Releases](https://github.com/LianHe-BI/Blackwell-optimized-llama.cpp-Docker-image/releases) 下载 v5.0-final 的全部分卷（`blackwell-v5.0-final.tar.gz.part-00` 至 `part-04`），合并并校验：

```bash
cat blackwell-v5.0-final.tar.gz.part-* > blackwell-v5.0-final.tar.gz
sha256sum -c SHA256SUMS
```

2. Load the image / 加载镜像

```bash
docker load < blackwell-v5.0-final.tar.gz
```

3. Run the container / 启动容器

```bash
docker run -it --rm --gpus all -v /your/model/dir:/data g312-workstation:v5.0-b9334-thinking-off bash
```

将 `/your/model/dir` 替换为存放 .gguf 模型的实际路径。

4. Chat / 开始对话

```bash
llama-chat /data/your-model.gguf
```

---

## Performance / 性能

测试平台：RTX 5070 Ti Laptop 12GB，Ubuntu 24.04，驱动 590.48.01

| Model | Quantization | Prompt Processing | Generation |
| --- | --- | --- | --- |
| 4B | F16 | 250+ tok/s | 70+ tok/s |
| 14B | Q4_K_M | - | 30+ tok/s |

---

## Advanced Usage / 高级用法

HTTP server / 启动 HTTP 服务

```bash
llama-server -m /data/your-model.gguf -ngl 99 --host 0.0.0.0 --port 8080
```

Quantize a model / 量化模型

```bash
llama-quantize /data/model.gguf /data/model-q4.gguf Q4_K_M
```

Convert HuggingFace model to GGUF / 转换模型格式

```bash
python /opt/llama.cpp/convert_hf_to_gguf.py /path/to/hf_model --outfile /data/output.gguf --outtype f16
```

---

## Image Contents / 镜像内容

| Component | Version / Description |
| --- | --- |
| Base OS | Ubuntu 24.04.4 LTS |
| CUDA | 12.8.93 (nvcc) |
| llama.cpp | b9334 (thinking-off), sm_120 optimized, qwen3_nonthinking.jinja |
| Python | 3.12.3 + PyTorch 2.10.0+cu128 + Transformers 5.3.0 |
| Tools | rlwrap, git, cmake, build-essential |
| Scripts | /usr/local/bin/llama-chat |
| Work Dir | /opt/llama.cpp/build/bin |

---

## Requirements / 环境要求

| Item | Requirement |
| --- | --- |
| GPU | RTX 5070 Ti / 5080 / 5090 (also works on 30/40 series) |
| Host OS | Ubuntu 24.04 / 26.04 (other distros need driver >= 570) |
| Docker | installed, supports `--gpus all` |
| NVIDIA Driver | >= 570 (590 recommended) |

WSL2 is untested; native Ubuntu is recommended.

---

## License / 协议

- Open Source: MIT License (see LICENSE)
- The image contains NVIDIA proprietary driver components; please comply with applicable laws.

---

## Release Notes / 版本历史

- v5.0-final (2026-08-06)
  - llama.cpp b9334, thinking-off (reasoning disabled, qwen3_nonthinking.jinja)
  - llama-chat v5.0 production script (`--reasoning-budget 0` + rlwrap)
  - Parts + SHA256SUMS integrity verification
- v4.1-final (2026-03-28) [superseded]
  - Initial release, Blackwell + NVFP4-ready
  - llama-chat script, LD_LIBRARY_PATH fixed
