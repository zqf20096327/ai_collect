# ComfyUI-GPU-Tuning

对 ComfyUI 的模型推理实现进行全方位测量和调优：int8 linear、注意力、VAE、
文本编码器与单 token 解码。**不改 ComfyUI 源码**，全部以运行时包装安装，
`COMFY_GPU_TUNE=off` 可整体关闭。启用哪些优化由实测数据决定，没测过的卡保持通用路径。

## 实测效果（MI50 32 GB）：

| 模型 | 参数 | 关闭节点 | 开启节点 |
|---|---|---|---|
| Qwen-Image 2.1 | 1024²              | 19.73 s/it | 3.55 s/it |
| Qwen3.5-9B     | 4096 context       | 1.27 it/s  | 37 it/s   |
| SDXL           | 1024² batch_size 4 | 4.85 s/it  | 3.49 s/it |

## 安装

1. 克隆仓库到 ComfyUI 自定义节点目录
```bash
git clone https://github.com/LaoBro/ComfyUI-GPU-Tuning custom_nodes/ComfyUI-GPU-Tuning
```
2. 参考 [docs/PORTING.md](docs/PORTING.md) 进行测量与调优，可交由 agent 自动完成

## 两个节点

| 节点 | 位置 | 作用 |
|---|---|---|
| **GPU Tuning Model Settings** | 模型链（加载器 → 采样器之间） | 注意力模式、布局与 fp16 策略、int8 tile、QKV、VAE、GEMV、profiler 等 |
| **GPU Tuning CLIP Settings** | CLIP 链（加载器 → 编码） | 文本编码器 int8、TE GEMV、4-bit w4a8、文本生成补丁组 |

设置节点改动下一次执行就生效，不用重启。开关与环境变量全表见 [docs/CONFIG.md](docs/CONFIG.md)。

## 文档

移植与进一步调优 [PORTING.md](docs/PORTING.md) · 补丁与文本生成实现 [PATCHES.md](docs/PATCHES.md) ·
gfx906 实测边界 [GFX906.md](docs/GFX906.md) · 写 HIP 内核 [HIP_KERNELS.md](docs/HIP_KERNELS.md)

## 许可

MIT。补丁只改动运行时行为，不附带任何模型权重。
