# comfyui-ki-nodes

> 19 个 ComfyUI 自定义节点合集：360° 全景预览、MiniMax H3 音视频增强、Z-Image 采样加速、SelfLift 渐进分辨率采样、视频调色台、宫格拼图。

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Nodes-2f6f4e)
![Nodes](https://img.shields.io/badge/Nodes-19-1f6feb)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab)
![Deps](https://img.shields.io/badge/pip%20deps-none-success)

---

## 特性

- **零 pip 依赖**：不需要 requirements.txt，只用 ComfyUI 自带环境（torch / numpy / Pillow / ffmpeg）。
- **24 个节点，一个包**：由 9 个原独立插件合并，节点 ID、显示名、前端扩展名全部保持不变，旧工作流不用重连。
- **单一 WEB_DIRECTORY**：全部前端资源收敛到包级 `web/`，扩展统一挂在 `/extensions/comfyui-ki-nodes/`。
- **逐模块容错**：任一子模块导入失败只跳过该模块并打 WARNING，不会让整包节点全灭。
- **可选 VHS 加速**：装了 VideoHelperSuite，调色台走 VHS 原生解码/编码；没装自动退回内置 ffmpeg 实现。

## 安装

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jianzeki-dot/comfyui-ki-nodes.git
```

重启 ComfyUI 即可。唯一可选依赖是 [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)。
`ki_MiniMaxH3ReferenceToVideo` / `ki_MiniMaxH3LongVideoContinuation` 需要 ComfyUI 内核含 `comfy_extras.nodes_minimax_h3`（MiniMax H3 支持）。

> **从旧版升级**：先删除旧的 `comfyui-ki-tools`（以及任何单独安装的 ki_* 插件）再安装本包。
> 旧插件与本包存在同名节点 ID，同时存在时前端会保留旧扩展，可能出现已废弃的
> `image_1~image_10` 输入口、且字号异常。删除后重启并强制刷新浏览器（Ctrl+F5）。

---

## 节点一览

| 分类 | 节点 ID | 显示名 | 输入 → 输出 |
|---|---|---|---|
| 全景 | `Ki360PanoramaViewer` | ki_360预览截图 | IMAGE → 预览（输出节点） |
| 全景 | `Ki360PanoramaVideoViewer` | ki_360视频预览截图 | IMAGE(帧序列) + fps → 预览 |
| 全景 | `KiLoadImage` | ki_加载图像 | 文件 → IMAGE, MASK |
| 全景 | `KiCameraMarker` | ki_相机定位 | IMAGE + marks_data → IMAGE |
| H3 | `ki_MiniMaxH3ReferenceToVideo` | ki MiniMax H3 Reference to Video | CLIP/VAE/PROMPT/参考 → CONDITIONING |
| H3 | `ki_MiniMaxH3LongVideoContinuation` | ki MiniMax H3 长视频续接 | +context_latent → CONDITIONING, LATENT |
| H3 | `ki_MiniMaxH3JoinMatch` | ki MiniMax H3 接缝匹配 (Join Match) | 前后段 LATENT → 接缝参数/拼接结果 |
| H3 | `ki_MiniMaxH3RefModImages` | ki H3 RefMod 批量图片 (Pick Images) | 图片批量选取 → CONDITIONING 参考图 |
| H3 | `ki_MiniMaxH3SaveTailLatent` | ki MiniMax H3 存尾部 Latent (Save Tail Latent) | LATENT → 尾部 latent 文件 |
| H3 | `ki_MiniMaxH3LoadTailLatent` | ki MiniMax H3 读尾部 Latent (Load Tail Latent) | latent 文件 → 尾部 LATENT |
| H3 | `ki_MiniMaxH3VideoToTailLatent` | ki MiniMax H3 视频裁剪转尾部 Latent (Crop to Tail Latent) | 视频 → 尾部 LATENT |
| 显存 | `ki_H3_Force_RAM_Offload` | ki H3 Force RAM Offload | MODEL → MODEL |
| 显存 | `ki_Force_Ref_Evict` | ki Force Ref Evict | CONDITIONING(+LATENT) → CONDITIONING, LATENT |
| 加速 | `KiZImageBoost` | KI Z-Image 加速 | MODEL → MODEL, STRING |
| 采样 | `KiSelfLiftH3Sampler` | SelfLift H3 采样器 | MODEL/COND/VAE/LATENT/SIGMAS → LATENT |
| 采样 | `KiSelfLiftImageSampler` | SelfLift 图像采样器 | MODEL/COND/VAE/LATENT/SIGMAS → LATENT |
| 采样 | `KiSelfLiftH3TST` | SelfLift H3 TST | MODEL → MODEL |
| 调色 | `KiLoadVideoColorGrade` | Ki 加载视频（调色） | 视频文件 → IMAGE/帧数/音频/信息 |
| 调色 | `KiVideoCombineColorGrade` | Ki 视频合成（调色） | IMAGE(+音频) → 视频文件 |
| 拼图 | `ki_宫格拼图简易版` | ki_宫格拼图简易版 | 最多 8×IMAGE → IMAGE, STRING |
| 拼图 | `ki_宫格拼图高阶版` | ki_宫格拼图高阶版 | 最多 10 槽 → IMAGE, STRING |
| 拼图 | `ki_宫格拼图高阶版2.0` | ki_宫格拼图高阶版2.0 | 固定 C×R 网格 → IMAGE, STRING |
| 拼图 | `ki_单图标注加载` | ki_单图标注加载 | 文件 → IMAGE（带序号标注） |
| 边界框 | `ki_CreateBoundingBoxes` | 创建边界框（KI 老版节点） | 继承官方节点逻辑 |

---

## 节点详解

### 1. Ki360PanoramaViewer / Ki360PanoramaVideoViewer

等距柱状（equirectangular）全景图 / 全景视频的交互式预览。前端用 Three.js 球面投影，支持拖拽平移、滚轮缩放；视频版额外支持播放/暂停/时间轴拖动。

**算法要点**
- 后端做批量取帧 → float→uint8 → 灰度转 RGB → 按 `max_width` 缩放 → JPEG/PNG base64 编码，前端直接贴到球面贴图，不依赖额外静态服务。
- 图像版默认长边上限 6000（可到 16384 表示不缩放）；视频版默认 2048，`-1` 表示不缩放。
- 视频帧按 `fps` 参数定时序推送，输出 `video_type=360_equirectangular` 供前端选择球面材质。

### 2. KiLoadImage（ki_加载图像）

官方 `LoadImage` 的替代品，输出完全一致（IMAGE + MASK），不修改任何官方文件。

**算法要点**
- 支持把外部图片拖到节点上上传、`Ctrl+V` 粘贴剪贴板图片，默认落到 `input/ki_load/`。
- 用 `ImageOps.exif_transpose` 纠正 EXIF 方向；`I` 模式按 /255、`I;16` 按 /65535 归一化。
- 带 Alpha 通道时 MASK = `1 - alpha`，否则返回 64×64 全零掩码。
- `IS_CHANGED` 用文件 SHA-256 判断是否重跑。

### 3. KiCameraMarker（ki_相机定位）

在图片上合成机位图标（透视机位 / 全景位置），前端提供 PS 式编辑：拖动移动、四角等比缩放、中心旋转。

**算法要点**
- `marks_data = [{"t":"cam"|"pin","x":0..1,"y":0..1,"scale":1.0,"rot":0}]`，x/y 为图标中心相对坐标。
- 图标宽度 = `0.16 × 图宽 × scale`，按原比例算高，LANCZOS 缩放后用 BICUBIC 旋转（`rot` 为顺时针角度），最后按中心点贴到 RGBA 画布。

### 4. ki_MiniMaxH3ReferenceToVideo

官方 Reference-to-Video 的扩展版：行为 100% 对齐官方，额外提供按**短边**分级的参考图尺寸档位。

**参数**

| 参数 | 默认 | 说明 |
|---|---|---|
| width / height | 1344 / 768 | 对齐 32 的生成画布 |
| length | 124 | 24fps 帧数，step=17（训练区间 ~124–362） |
| ref_image_size | 1.6 | `match` / `1.2`–`3.1` / `max` |
| ref_images / ref_videos / ref_audios | — | 自动增长输入，最多 9 图 / 3 视频 / 3 音频 |

**算法要点**
- `match`：按面积匹配生成画布，缩放系数 `min(1, sqrt((W·H)/(w·h)))`。
- `1.2`：参考图短边 = 生成画布短边；`1.3`–`3.1`：短边 = `gen_short × ratio/1.2`，对齐 32 并封顶 2048；`max`：短边 ≤ 2048。
- 所有档位**只下采样、从不放大**，最终宽高对齐 32 像素网格。
- 参考图/视频经 VAE 编码、音频经 audio_vae 编码后，统一写入 conditioning 的 `minimax_refs`，供 H3 采样读取。

### 5. ki_MiniMaxH3LongVideoContinuation

长视频续接：把上一段产出的 H3 音视频联合 latent 的**尾部**作为「固定帧」钉到新片段开头，让机位、速度、动作连续，而不是重新生成一段相似的画面。

**参数**

| 参数 | 默认 | 说明 |
|---|---|---|
| length | 124 | 本段帧数，step=17 |
| context_latent | 可选 | 上一段的联合 latent；不接则退化为普通 R2V |
| context_frames | 22 | `5 / 22 / 39 / 56 / 73`，即 17k+5 网格 |
| ref_image_size | match | 同 Reference to Video |

**算法要点**
- **时间坐标而非帧内容**：H3 的时间压缩循环 `FRAME_PER_TOKEN = (1,4,4,4,4)`，每 5 个 latent 步覆盖 17 帧。
- 帧数必须落在 `17k+5` 网格（5, 22, 39, 56, 73…），因为 17 帧正好是整数个 latent 步，切不出半个 latent 帧。
- 视频尾部按单步切块，像素偏移 0/1/5/9/13/17… 逐块钉到新片段开头，模型读成「本片段更早的部分」。
- 音频按 40Hz（24fps 下 `FRAME_RESCALE = 5/3`）换算，窗口**结束于接缝并向后回溯**，起点落在负的分数坐标上，模型才会当成同一条音轨的延续。
- 注入方式：写入 conditioning 的 `minimax_keyframes`，用负时间坐标表达「固定、不再去噪」。
- 会校验 latent 步数、相位匹配与音频 overhang，避免音画错位。

### 6. ki_H3_Force_RAM_Offload / ki_Force_Ref_Evict

避免 H3 在显存占用 >95% 时 GPU stall 的两件套。

**ki_H3_Force_RAM_Offload**（MODEL → MODEL）

| 参数 | 默认 | 说明 |
|---|---|---|
| intensity | 2 | 0=关，1=轻，2=16GB 默认，3=重，4=极端 |
| vram_trigger | 0.88 | 已用显存比例超过该值才强制卸载 |
| use_pinned | True | CPU 张量使用 `pin_memory`，后续 H2D 更快 |
| empty_cache | True | 每次搬移后 `torch.cuda.empty_cache()` |

**算法要点**
- 把 patcher 的 `offload_device` 固定为 CPU。
- level≥2 且比例超阈值时，请求 `free_memory(总显存 × 0.55)`；level≥3 追加 `partially_unload(CPU, 2GB)`；level≥4 再请求 70% 并 `gc.collect()`。
- 把 `{intensity, vram_trigger, use_pinned}` 写入 `model_options["ki_h3_ram_offload"]`，供下游采样器运行时复查。

**ki_Force_Ref_Evict**（CONDITIONING → CONDITIONING）

- 递归遍历 conditioning 元数据中的 `minimax_refs`（可选 `minimax_keyframes`），把 latent 整体搬到 CPU 并可 `pin_memory`，采样期间不再占显存。
- 默认只搬 `minimax_refs`，关键帧 latent 通常保留在 GPU。

### 7. KiZImageBoost（KI Z-Image 加速）

Z-Image / Lumina 系 DiT 的**整步跳过**加速：在 `DIFFUSION_MODEL` 包装点拦截每次模型调用，对可以跳过的采样步用最近真实输出的最小二乘轨迹外推顶替。被跳过的步不产生前向计算，也不产生权重搬运（offload 下尤其明显）。

**参数**

| 参数 | 默认 | 说明 |
|---|---|---|
| enable | True | 总开关 |
| attention | default | 可选注意力实现覆盖 |
| fit_points | 4 | 拟合用最近真实点数（2–6） |
| horizon | 1 | 最大连续跳步数（1–3） |
| drift_limit | 1.0 | 偏差预算，0=不跳，≥1=按上限硬跳 |
| floor_percent / ceil_percent | 0.18 / 0.86 | 允许跳步的采样进度窗口 |
| verbose | False | 打印每步决策 |

**算法要点**
- **轨迹键**：把分支列表与实际 batch 展开成 `(分支号, 该分支第几张)`，一次调用含多分支多图时也能分别拟合。
- **横轴用采样进度** `1 - σ/σ0`，因此 σ 间隔不均匀（如 Karras）时拟合依然成立。
- **多项式最小二乘**：对最近 `fit_points` 个真实输出拟合 1 阶或 2 阶多项式；横轴先中心化+缩放并加 ridge，否则窗口内跨度只有 ~0.07，正规方程条件数会差好几个量级。
- **跳过决策门控**（任一不满足则完整评估）：首尾步（edge）→ 进度窗口外（window）→ 冷却中（guard）→ 拟合点不足（warmup）→ 偏差超预算（drift）→ 连续跳步达上限（horizon）。
- **连跳误差模型**：线性外推连跳 h 步的误差约为单步误差的 `h(h+1)/2` 倍（h=1→×1，2→×3，3→×6），据此反解当前偏差预算允许跳几步。
- **自监控**：每次真实评估后用「假如这步跳过会差多少」的影子预测更新偏差 EMA；单步偏差超过容差 2 倍立即进入冷却，并可在拟合不可用时退回完整评估。
- 注意力路径、采样器、CFG 组合逻辑全部保持 ComfyUI 原生，不做改写；int8 与 bf16 权重共用同一套逻辑。

### 8. KiSelfLiftH3Sampler / KiSelfLiftImageSampler / KiSelfLiftH3TST

训练-free 的渐进分辨率采样（Artifact-Aware Consistency Lift）。前若干步在**低分辨率 latent** 上跑，把干净端点抬升到目标分辨率，在 transition sigma 重新加噪，再以全分辨率跑完剩下的 schedule。

**KiSelfLiftH3Sampler 参数**

| 参数 | 默认 | 说明 |
|---|---|---|
| transition_step | 6 | 低分辨率阶段去噪步数 |
| lowres_scale | 0.5 | 低分辨率前缀的空间比例（0.25–1.0） |
| rho | 0.0 | 高风险时空位置向像素 VAE 锚点修正的比例；H3 默认 0（纯外部放大） |
| w_min / w_max | 0.5 / 1.0 | 修正强度下限 / 上限 |
| upscaler_model | 自动 | 外部 H3 latent 放大模型；`none` 走最近邻抬升 |
| upscaler_unload | True | 抬升后立即卸下放大模型 |
| ffn_chunks / attn_head_chunks | 2 / 8 | 高分辨率阶段的 KJ 显存分块 |

**算法要点**
- **低分辨率前缀** → **transition**（复用该步 Euler 预测，保持总 NFE 数不变）→ **lift**（nearest/bilinear 或学习式 latent 放大）→ **Artifact-Aware 修正**（按 `rho` 选取高风险位置，向 VAE 像素往返锚点插值，权重在 `w_min..w_max`）→ **重新加噪** → **高分辨率续跑**。
- `rho=0` 且 `upscaler=none` 在双阶段模式下会报错：两条修正路径全关等于没做 lift。
- 关键帧 conditioning 会被逐帧双线性缩放到低分辨率网格，并做逐通道均值匹配以消除双线性带来的色彩漂移（不做方差补偿，低分辨率网格本就无法表达）。
- 噪声掩码用 post-CFG hook 把生成区域外的 `x0` 钉回干净锚点；在 Euler 下等价于「未掩码区域 = 原图 + 该步噪声」，精确无累积误差。
- KJ-VRAM 分块（FFN token 分块 / 注意力 head 分组）是**位精确**的，不损失画质；`kjvram_low` 可把同一套分块计划扩展到低分辨率第一遍（视频编辑场景带巨大参考 KV 时有用）。
- H3 TST 变体：训练-free 的 Temporal State Transport 修正（`tau` 默认 0.2），可与头部分块对齐。

### 9. KiLoadVideoColorGrade / KiVideoCombineColorGrade

以 VHS 的 Load Video / Video Combine 为底，加载即调色 / 合成前调色，带 255 个内置 `.cube` LUT 与 0–1 强度。

**调色管线顺序（固定）**

```
白平衡 → 曝光 → 对比度 → 高光/阴影/白/黑 → 参数曲线 → HSL → 自然饱和度 → 饱和度 → LUT
```

- **色彩空间分工**：曝光与白平衡在线性光空间做，对比度 / 影调分区 / 曲线 / HSL 在 gamma 空间做——与专业后期软件一致。
- 对比度：以中灰为轴的 S 曲线，无硬裁剪；高光是乘性增益，阴影是加性提升。
- 曲线：自由控制点（PS 风格），序列化成 `"0,0;0.25,0.32;1,1"` 字符串，前端 canvas 单击加点、拖动调形、右键删点。
- HSL：Rec.709 亮度权重（0.2126 / 0.7152 / 0.0722），8 个色相通道（红/橙/黄/绿/浅绿/蓝/紫/洋红），红跨 0°，其余连续分界，PS 语义。
- 自然饱和度对灰淡像素加得多、已艳的加得少，保护肤色。
- LUT：3D LUT 用整数坐标 + 小数部分做三线性插值，1D LUT 做线性插值，结果 clamp 到 0..1；按 `lut_strength` 与原图混合。
- **资源策略**：逐批处理，单批像素数钉死在固定预算内，无论一帧还是三百帧峰值显存恒定；结果固定落 CPU，避免下游编码再占一份显存；`compute_device=auto` 只在显存宽裕时用 GPU，紧张时自动退回 CPU。
- **实时预览**：调色前的帧落盘到 `temp/ki_colorgrade`（最多 24 帧、宽度 ≤960、uint8 npy + mmap），前端通过 `/ki_colorgrade/*` 与 `/api/ki_colorgrade/*` 接口改参数即时重算，返回调色前后 base64 与直方图。
- 可选 `trim_head`（5/22/39/56/73 帧）裁掉续接片段重复头，音频同步裁剪，保证音画对齐。

### 10. 宫格拼图（简易版 / 高阶版 / 高阶版 2.0 / 单图标注加载）

**两种装配模式**
- **槽位编辑器**（简易版、高阶版）：`slot_count` 1–8/1–10，前端卡片支持点击/拖入/`Ctrl+V` 选图，双击灯箱预览；`slots_json` 保存槽位顺序。
- **固定网格**（高阶版 2.0）：`2*1`–`3*4` 等 9 种 C×R 规格，按列装配。

**通用的奇数末张策略**
- `拼图1`：末张拉满整行宽度。
- `拼图2`：末张保持行高、水平居中，两侧垫底色。
- `拼图3`：末张左置、右侧留底色。
- 9 张图强制 3×3 九宫格。

**算法要点**
- 行内先统一高度（`interpolate` + 指定 `scale_method`），再按目标宽度对齐；末张超宽时按宽度回缩。
- 两图且都为横图时走特殊拼接（上下叠放），避免出现超宽单行。
- 垫色用 `fill_color`（浅灰 240 / 界面深色 53 / 纯黑 / 纯白 / 品红 / 纯绿）。
- 标注两种渲染：`V2` 贴原图右下角，`V3` 在底部独立底栏居中；标签文本 = `bottom_text_prefix` + 序号，颜色可选。
- 字体走 `ki_font.load_label_font()`：**内置 `fonts/NotoSansSC-Regular.otf` → 系统字体 → Pillow 默认字体**。旧版直接落到 `ImageFont.load_default()`，在无中文字体的 Linux 环境会退化成固定约 10px，字号参数失效，这是“标注字特别小”的根因。
- 简易版保留左侧 `image_*` 连线输入口；高阶版 / 高阶版 2.0 已废弃这些接口，前端在读盘、添加节点、轮询时都会同步清除，避免残留无用输入口。
- 最后统一把长边限制在 `max_size`（默认 2048）；同时输出 `resolutions_info` 字符串，记录每张原图与最终合成尺寸。

### 11. ki_CreateBoundingBoxes（KI 老版节点）

内核的 `CreateBoundingBoxes` 只在 Node 2.0（Vue）渲染器下提供画布编辑器，老渲染器里只显示一行提示。本包前端扩展在 litegraph 画布内**重绘等价编辑器**，同时作用于官方节点与本模块注册的 `ki_` 等价节点，节点逻辑完全继承官方实现。

---

## 目录结构

```
comfyui-ki-nodes/
├── __init__.py              统一注册入口（逐模块隔离导入 + 重复 ID 检查）
├── ki360_nodes.py           Ki360 预览 / 载图 / 相机定位
├── ki_h3_ref.py             H3 Reference to Video
├── ki_h3_offload.py         H3 显存卸载 + 参考 latent 清理
├── ki_h3_continuation.py    H3 长视频续接
├── ki_zboost.py             Z-Image 整步跳步加速
├── ki_grid_simple.py        宫格拼图简易版
├── ki_grid_pro.py           宫格拼图高阶版 / 单图标注加载 / 高阶版 2.0
├── ki_font.py               标注字体加载（内置字体 → 系统字体 → 默认字体）
├── fonts/                   内置 Noto Sans SC（OFL-1.1），保证跨机器标注字号一致
├── ki_bbox_legacy.py        边界框老版渲染器节点
├── ki_selflift/             SelfLift 渐进采样（子包）
│   ├── nodes.py  selflift.py  h3_upscaler.py
│   ├── h3_kj_vram.py  h3_tst.py  diagnostics.py
├── ki_colorgrade/           视频调色台（子包）
│   ├── nodes.py  core.py  lut.py  params.py
│   ├── server.py  vhs_bridge.py
├── presets/luts/            255 个内置 .cube 预设
├── web/                     全部前端资源（唯一 WEB_DIRECTORY）
│   ├── js/ki_bbox_legacy_editor.js
│   ├── ki_color_grade.js / ki_gl.js / ki_colorgrade.css
│   ├── ki_camera_marker.js / ki_grid_widget.js / lib/pano_viewer.js
└── docs/                    各原插件原始说明与开发脚本（不参与运行）
```

## 兼容性与注意事项

- **节点 ID 不冲突**：24 个 ID 两两不重复，`__init__.py` 加载时做集合交集检查，真有重复直接抛错而不是静默覆盖。
- **前端扩展名唯一**：`Ki360.CameraMarker`、`ki.GridUIBeauty.v32`、`Ki360.LoadImage`、`ki.MissingMediaFix.v1`、`ki.SingleLabeledLoader.v1`、`Ki360.Preview`、`ki.videoColorGrade`、`ki.BoundingBoxesLegacyEditor`。
- **HTTP 路由**：调色台固定使用 `/ki_colorgrade/*` 与 `/api/ki_colorgrade/*`，不占用其他插件路由。
- **资源路径**：调色台靠 `__file__` 上溯两级找 `presets/luts`；SelfLift 的 debug 目录在 `ki_selflift/debug`；VHS 桥接靠 `__file__` 上溯三级找 `custom_nodes`。

## 常见问题

**Q：装了插件但某个节点不出现？**
看启动日志里的 `[comfyui-ki-nodes] 子模块 ... 加载失败`，通常是该节点依赖的 ComfyUI 内核版本较旧（如缺少 MiniMax H3 / 边界框节点）。

**Q：Z-Image 加速没有提速？**
检查 `floor_percent`/`ceil_percent` 窗口是否覆盖你的步数区间，`drift_limit` 是否为 0，以及 `verbose` 打开后每步的 `reason`（warmup/drift/horizon/window/edge）。

**Q：调色很慢或爆显存？**
把 `compute_device` 设为 `cpu`；实际调色本身是按固定像素预算分批的，主要开销来自上游解码。

**Q：续接后画面跳变？**
`context_frames` 要用 `5/22/39/56/73` 网格值，并确认传入的 `context_latent` 是同一模型、同一分辨率、同一 FPS 的产物。

**Q：标注文字特别小、只有 10px 左右？**
旧版在没有中文字体的机器上回退到 `ImageFont.load_default()`，字号参数被忽略。现在已内置 Noto Sans SC，正常情况下不会再出现；若仍异常，先确认 `fonts/NotoSansSC-Regular.otf` 存在，再看启动日志是否有字体加载告警。

**Q：高阶版节点右边还挂着 `image_1~image_10` 无用输入口？**
这是旧插件 `comfyui-ki-tools` 未卸载、或浏览器缓存了旧前端扩展导致的。删除旧插件、重启 ComfyUI、`Ctrl+F5` 强制刷新即可；本版前端在读盘/添加节点/轮询时也会主动清掉这些残留接口。

## 第三方算法出处

- H3 长视频续接的时间网格与上下文思路参考 [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context)（GPL-3.0）与 [tritant/ComfyUI_MiniMax_H3_Extender](https://github.com/tritant/ComfyUI_MiniMax_H3_Extender)。
- SelfLift 渐进分辨率采样参考 Artifact-Aware Consistency Lift（arXiv:2609.02036）；H3 TST 参考 Temporal State Transport（arXiv:2609.08505）。
- HSL 八色相语义参考 [aiaiaikkk/ComfyUI-Curve](https://github.com/aiaiaikkk/ComfyUI-Curve)（Photoshop HSL 语义）。
- 派生自 GPL-3.0 项目的部分，其分发同样受 GPL-3.0 约束。
- 内置字体 `fonts/NotoSansSC-Regular.otf` 来自 [Noto Sans SC](https://github.com/notofonts/noto-cjk)，SIL Open Font License 1.1。

## 致谢

ComfyUI 团队与上述开源项目的作者。
