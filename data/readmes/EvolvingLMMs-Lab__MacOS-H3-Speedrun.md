<h1 align="center">MacOS H3 Speedrun</h1>

<p align="center">
  <b>中文</b> · <a href="README_EN.md">English</a>
</p>

<p align="center">
  在 Apple Silicon 上用 ComfyUI 创作原生音画同步短片。按内存自动选模型，从 Prompt 直接输出 MP4。
</p>

<p align="center">
  <a href="examples/cyber-480p-5s.mp4"><img src="assets/Teaser.jpg" width="100%" alt="MacOS H3 Speedrun"></a>
</p>

<p align="center">
  <b>点击封面播放</b> · 480p · 5.175 秒 · 生成耗时 <b>3min12s</b> · 原生音频
</p>

## 创作示例

以下示例使用 **MiniMax-H3 Turbo v4-600 + SolAttn 1.3** 生成，约15秒并包含原生音频。点击海报播放720p版本。

<table>
<tr>
<td align="center" width="50%">
<a href="examples/720p/cyber-v4-600-bf16merged.mp4"><img src="assets/posters/cyber.jpg" width="420" alt="Cyber showdown"></a><br>
<b>赛博对决</b><br>
<a href="examples/480p/cyber-v4-600-bf16merged.mp4">480p</a> · <a href="examples/720p/cyber-v4-600-bf16merged.mp4">720p</a> · <a href="examples/prompts/prompt_cyber">Prompt</a>
</td>
<td align="center" width="50%">
<a href="examples/720p/wuxia-v4-600-bf16merged.mp4"><img src="assets/posters/wuxia.jpg" width="420" alt="Wuxia bamboo forest"></a><br>
<b>竹林武侠</b><br>
<a href="examples/480p/wuxia-v4-600-bf16merged.mp4">480p</a> · <a href="examples/720p/wuxia-v4-600-bf16merged.mp4">720p</a> · <a href="examples/prompts/prompt_wuxia">Prompt</a>
</td>
</tr>
<tr>
<td align="center" width="50%">
<a href="examples/720p/product-v4-600-bf16merged.mp4"><img src="assets/posters/product.jpg" width="420" alt="Luxury perfume commercial"></a><br>
<b>香水广告</b><br>
<a href="examples/480p/product-v4-600-bf16merged.mp4">480p</a> · <a href="examples/720p/product-v4-600-bf16merged.mp4">720p</a> · <a href="examples/prompts/prompt_product">Prompt</a>
</td>
<td align="center" width="50%">
<a href="examples/720p/fps-v4-600-bf16merged.mp4"><img src="assets/posters/fps.jpg" width="420" alt="First-person shooter"></a><br>
<b>第一人称战场</b><br>
<a href="examples/480p/fps-v4-600-bf16merged.mp4">480p</a> · <a href="examples/720p/fps-v4-600-bf16merged.mp4">720p</a> · <a href="examples/prompts/prompt_fps">Prompt</a>
</td>
</tr>
</table>

> 示例实际为832×480与1280×736、24 fps、15.083秒；“480p / 720p”是便于理解的档位名称。

## 三步开始创作

```bash
git clone https://github.com/EvolvingLMMs-Lab/MacOS-H3-Speedrun
cd MacOS-H3-Speedrun
/path/to/ComfyUI/.venv/bin/python bootstrap.py --comfyui /path/to/ComfyUI --memory-tier auto
```

1. 安装器按统一内存下载所需节点、模型和工作流。
2. PyTorch工作流使用 `python main.py --use-pytorch-cross-attention` 重启ComfyUI。
3. 打开 `user/default/workflows` 中的Turbo4工作流，修改Prompt并Queue。

> PyTorch MiniMax-H3不要使用`--force-fp16`、`--fp16-unet`或`--fp16-text-enc`；保持checkpoint默认BF16/混合精度。`--bf16-vae`可以保留。错误配置会在第一步产生NaN/花屏，并可能最终显示为`SaveVideo: avcodec_send_frame() returned 22`。

## 选择你的 Mac

| 统一内存 | 默认工作流 | 峰值内存 |
| ---: | --- | ---: |
| **24 GB** | MLX Core4-pruned · offset stream2 | **16.36 GB** |
| **32 GB** | MLX Core4-pruned · resident | **24.70 GB** |
| **48 GB** | MLX Core8-pruned · resident | **32.21 GB** |
| **64 GB** | MLX Attention16 + MLP8 | **39.73 GB** |
| **96–128 GB** | **BF16-pruned标准ComfyUI图** | **63.35 GB**（同checkpoint strict-staged基线） |
| **192 GB+** | Full BF16标准ComfyUI图 | **159.99 GB** |

峰值来自512 GB M3 Ultra测试机的进程footprint。32/48 GB数据来自旧AdaLN8等价配置，属于保守测量。96–128 GB的63.35 GB来自同一BF16-pruned checkpoint在strict-staged Full20下的实测；当前标准ComfyUI图仍需同条件复测。24 GB尚未在物理24 GB Mac验证，并需要约110–120 GB临时磁盘空间。

48/64 GB的可选BF16-pruned stream5质量档真实API峰值为**42.56 GB**，三种生成模式均为0 swap。

## 选择生成模式

| 模式 | 适合场景 | 默认加速 |
| --- | --- | --- |
| **Turbo 4 Fast** | Prompt、镜头和声音草稿 | SolAttn开启 |
| **Turbo 8 Balanced** | 可选的第二条生成轨迹 | SolAttn开启 |
| **Full 20 Quality** | 不使用Turbo LoRA的最终比较 | Safe FBC + SolAttn开启 |

24 GB只安装经过验证的Turbo4；其他标准档包含Turbo4、Turbo8与Full20。建议先用480p / 5秒Turbo4确定主体、动作、镜头和声音，再提高分辨率或步数。

## 社区魔改与 LoRA

社区模型分为两条使用路径：

| 路径 | 适用工作流 | 使用方式 |
| --- | --- | --- |
| **直接在ComfyUI操作** | 48/64 GB BF16质量档、96–128 GB BF16-pruned、192 GB Full BF16 | 兼容的H3 checkpoint可直接选择；自定义图可用标准`MODEL` stream节点连接兼容LoRA |
| **先转换checkpoint/adapter** | 24–64 GB MLX快档 | 不能直接连接通用`Load LoRA`或加载ComfyUI checkpoint；需先转换为MLX H3格式，当前一次支持一个adapter |

内置Turbo LoRA已配置好。社区资源必须针对MiniMax-H3并匹配pruned/full底模与AdaLN宽度；SD、SDXL、Flux、Wan等模型系列不兼容。普通风格或角色LoRA建议先用Full20验证。

## Prompt 小贴士

- 描述一个连续镜头：主体、动作、镜头、光线、需要保持一致的元素。
- 明确写声音；不需要对白或音乐时写 `no speech` / `no music`。
- 五秒内避免多个剪辑和互不相关的场景。
- 可参考 [Omni-Rewriter](https://github.com/WayneJin0918/Omni-Rewriter) 与 [awesome-minimax-h3-prompts](https://github.com/Anil-matcha/awesome-minimax-h3-prompts)。

## 可选安装

48/64 GB可安装BF16-pruned stream5质量档：

```bash
python bootstrap.py --comfyui /path/to/ComfyUI --memory-tier 48 --workflow-set quality
# fast|quality|all
```

该档直接使用标准ComfyUI BF16-pruned checkpoint：Qwen 25+25后释放，DiT每次驻留5个block，随后由原装ComfyUI Video/Audio VAE解码。真实API最坏峰值42.56 GB，0 swap；stream5为208.98秒/42.56 GB，stream10为210.47秒/43.24 GB，因此48/64 GB都使用stream5。启动ComfyUI时需要`--use-pytorch-cross-attention`。

可用内存档：`24|32|48|64|96|192`。工作流不会静默下载模型，只有显式运行`bootstrap.py`才会安装。请预留模型空间并阅读MiniMax-H3上游许可。

## 实测生成时间

创作者工作流实测，均为M3 Ultra、864×480、约5秒并开启SolAttn：

| 配置 | 完整生成时间 |
| --- | ---: |
| 24 GB工作流 · Core4 offset stream2 | **239.27秒（3分59秒）** |
| Core4 resident · 32 GB默认路径 | **216.60秒（3分37秒）** |
| BF16-pruned stream5 · 48/64 GB质量档 · Turbo4 | **208.98秒（3分29秒）** |
| BF16-pruned stream5 · 48/64 GB质量档 · Turbo8 | **383.79秒（6分24秒）** |
| BF16-pruned stream5 · 48/64 GB质量档 · Full20 | **551.33秒（9分11秒）** |

BF16标准ComfyUI图的端到端数据摘自 [ComfyUI-SolAttn-MPS](https://github.com/yshenaw/ComfyUI-SolAttn-MPS)，使用M3 Ultra、Turbo4：

| 视频规格 | Native MPS SDPA | SolAttn |
| --- | ---: | ---: |
| 480p · 5.17秒 | 4分39秒 | **3分14秒** |
| 480p · 15.08秒 | 17分32秒 | **12分37秒** |
| 720p · 5秒 | 12分11秒 | **9分20秒** |
| 720p · 15.08秒 | 63分49秒 | **38分03秒** |

这些是固定Prompt与seed的M3 Ultra实测时间，不代表其他Mac或所有社区checkpoint；48/64 GB默认量化快档尚无完全匹配的单独端到端计时。Full20音频出现4个满幅样本，比例0.000012；Turbo4/8没有满幅样本。