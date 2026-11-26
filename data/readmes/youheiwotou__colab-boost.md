# ⚡ Colab Boost 控制台 (Colab Boost Console)

> **属于我们自己的 Google Colab 模型极速部署与算力护栏控制台** — 原生支持 Windows（免 WSL / 免外部 CLI）、多账号算力实时监控、显存保底自动重抽（如锁 80GB A100 / 96GB G4）、VM 级双层自动关机护栏、原生 OpenSSH 本地端口映射与即用即关回执归档。

---

## ✨ 核心特性与设计升级

本项目在深入研究云端运行时交互机制与前人经验的基础上**完全自主构建**，针对我们在 Windows 工作站上快速部署与调用各类 AI 模型的真实痛点做了系统级升级：

| 维度 | 传统方案 / 常见痛点 | ⚡ Colab Boost 控制台（本项目） |
| --- | --- | --- |
| **Windows 运行环境** | 强依赖 WSL2 Linux 子系统与 D-Bus Keyring | **Windows 100% 原生直连**：直接通过 HTTPS + Jupyter Kernel WebSocket + Windows 原生 OpenSSH WebSocket 桥接，**零 WSL 依赖** |
| **多 Google 账号管理** | 全局共用单一 CLI 登录槽位，切换账号会影响全局且互相覆盖 | **独立多账号凭据仓（OS Keyring）**：所有账号的 OAuth 令牌独立隔离存储，同屏查看全部账号 CCU 余额与消耗速率，同时支持一键导入本机已有 `colab-cli` 登录态 |
| **GPU 显存目标保底** | Colab 分配 A100 随机给 40GB 或 80GB，大模型放不下只能手动关机重开 | **智能显存探测与自动退回重抽 (`min_vram_mib`)**：设置 `70000 MiB` 后，抽到 40GB A100 会秒级自动 `unassign` 并重试直至拿到 80GB，中途取消保证 **0 残留计费实例** |
| **双层防忘关机护栏** | 关闭本地终端后云端 GPU 继续空转扣费；或未知余额被误判为 0 | **VM 侧独立看门狗 (`watchdog.py`) + 本地红线巡检**：看门狗运行在 Colab VM 内部（同时检测任务心跳与 `nvidia-smi` 利用率），即使本机断网/关机也会到点调用 `$TBE_RUNTIME_ADDR/unassign` 停止计费；未知/过期余额诚实标记绝不伪装成 `0` |
| **即用即关回执审计** | 关机后不确定是否真正释放干净、是否有浏览器遗留孤儿实例 | **孤儿实例预警 + 一键全关 + 落盘关闭回执 (`data/receipts/`)**：自动揪出网页端打开的未受管实例，每次释放均核验 `assignments` 清空并写入 JSON 关闭回执 |
| **开箱即用模型配方** | 仅支持单一 GGUF 或每次手动执行繁琐编译脚本 | 内置 **5 套生产级部署配方**：`GGUF (llama.cpp 预编译 CUDA)`、`vLLM 高吞吐推理`、`ComfyUI 视觉/视频工作台`、`MiniMax-H3 视频人物替换极速工作台 (G4 三轨并发)`、`Faster-Whisper 语音转写与词级时间戳 API`，并自带 **GGUF 多卡显存测算矩阵（T4 / L4 / A100 40G & 80G / H100 80G / G4 96G）** 与 **OpenAI 对话测速演练场** |

---

## 🚀 快速启动

### 环境要求
- Python `>= 3.12` 与 [`uv`](https://docs.astral.sh/uv/)（本机已安装）
- Windows 自带 OpenSSH (`ssh.exe` / `ssh-keygen.exe`，用于端口映射)

### 1. 一键启动演示沙盒模式（默认安全模式 · 0 计费）
无需登录 Google 账号、不触碰任何真实云端资源即可完整体验多账号看盘、80GB A100 显存重抽、GGUF 显存适配矩阵、分阶段部署、端口映射与对话测速：

```powershell
# 双击 start_demo.bat（也支持透传参数如 start_demo.bat --port 8766）或在终端运行：
uv run colab-boost --mock --mock-scenario demo --open-browser
```

启动后访问：`http://127.0.0.1:8765`

### 2. 切换至真实 Google Colab 生产模式
```powershell
# 双击 start_console.bat 无参启动会自动打开浏览器；传参时直接透传给 colab-boost
uv run colab-boost --real --open-browser
```
> 若需绑定非回环地址（如 `--host 0.0.0.0`），必须先设置环境变量 `COLAB_BOOST_API_TOKEN` 启用 Bearer 鉴权，否则服务会拒绝启动。

也可以在网页顶栏随时点击状态徽章在 **「演示沙盒模式」** 与 **「真实 Colab 模式」** 之间切换：
1. 进入 **「多账号与关闭回执」** 页面，点击 **「➕ 添加 Google 账号」**（若本机装过 `google-colab-cli` 并登录过，也可直接点 **「📥 导入本机 colab-cli 登录态」**）。
2. 如需下载 Hugging Face 私有/Gated 模型，在 **「成本护栏与密钥」** 页存入 `Hugging Face Token`（保存在 Windows 凭据管理器中，日志自动脱敏为 `***`）。
3. 进入 **「极速部署模型」**，选择配方与目标 GPU，点击 **「一键启动部署并自动映射到本地」**！

---

## 🧩 内置五大极速部署配方 (`recipes/`)

1. **`llama-cpp-gguf` — 部署 GGUF 大模型 (llama.cpp 预编译 CUDA)**
   - 免去 10+ 分钟源码编译耗时，自动按 GitHub Release 资产匹配并动态回退 CUDA 版本，强制注入 `/usr/lib64-nvidia` 驱动路径，校验 `CUDA0` 与实际显存占用，杜绝静默退回 CPU；API Key 仅通过 `LLAMA_API_KEY` 环境变量传递，绝不暴露于进程命令行。
   - 通过 HTTP `Range` 读取远程 GGUF 文件头架构元数据（支持 DeepSeek MLA `kv_lora_rank`、滑动窗口与按上下文缩放的 compute buffer），自动覆盖 T4 / L4 / A100 / H100 / G4 显存规划（T4 可自动降档至 4096 上下文），挑选放得下的最高量化档位，预热 CUDA 算子并输出实测 `tok/s`。
2. **`vllm-openai` — 部署 vLLM 高吞吐 Safetensors / AWQ / GPTQ / 多模态推理服务**
   - 适合 `Qwen2.5-VL`、`Qwen3`、`DeepSeek-R1-Distill` 等标准权重仓库，下载完成后清理常驻进程中的 `HF_TOKEN` 并通过 `VLLM_API_KEY` 环境变量传递访问密钥，暴露标准 `http://127.0.0.1:8000/v1` OpenAI 接口。
3. **`comfyui-studio` — 部署 ComfyUI 视觉/视频生成工作台**
   - 自动过滤 `requirements.txt` 中的 `torch`/`torchvision`/`torchaudio` 以保护 Colab 预装 CUDA PyTorch，支持断点续传（`-C -` + `.part` 原子写）预下载底模并将 `8188` 映射至本地浏览器。
4. **`minimax-h3-studio` — 部署 MiniMax-H3 视频人物替换极速工作台（G4 三轨并发）**
   - 专为 Colab G4 Blackwell (96GB) 定制：轨道 A（`uv` 并行安装 PyTorch 2.9.1+cu130 + 过滤 `requirements.txt` 防覆盖 CUDA PyTorch + 预编译 `SageAttention 2.2 sm120` wheel）与轨道 B（`hf_xet` / `aria2c` 并发拉取 MiniMax-H3 Ref2VA + CharacterSwap v1.5 权重：**4 核心文件 39.62 GB**，含默认原生 Audio VAE 共 **5 文件 40.23 GB**）完全并行；默认免单核重复读盘校验（可选多核 `sha256sum`），支持热实例 0 秒复用、自动归档输出视频与编译出的 `.whl` 至 `data/keep/`，并可选一键安装 `LatentSync + Demucs` 口型精修节点。
5. **`faster-whisper-api` — 部署 Faster-Whisper 语音转写与字幕对齐 API**
   - GPU 加速 `large-v3-turbo` / `large-v3`，自动注入 `/usr/lib64-nvidia` 与 pip cuDNN `LD_LIBRARY_PATH`，采用同步线程池处理与分块流式上传临时文件（不阻塞 `/health` 与事件循环），提供兼容 OpenAI `/v1/audio/transcriptions` 的词级时间戳接口。

---

## 🤖 Agent / 终端快捷调度命令 (`colab-boost` CLI)

控制台运行后，用户或 Antigravity 代理可直接通过命令行/HTTP API 全自动调度（配合全局 Skill `colab-boost`）；所有子命令均支持 `--json` 与 `--api-url <url>`（亦可通过 `COLAB_BOOST_API_URL` / `COLAB_BOOST_API_TOKEN` 环境变量配置），且可直接通过 `start_console.bat <subcommand>` 调用：

```powershell
# 查看多账号余额、运行中实例与映射端口
uv run colab-boost status

# 列出可用配方（内置 + 自定义）
uv run colab-boost recipes

# 一键开 G4 部署 MiniMax-H3（含默认 Audio VAE，共 5 文件 40.23 GB）并等待就绪与本地 8188 映射
uv run colab-boost deploy minimax-h3-studio --accel G4 --min-vram 80000 --wait

# 远程执行 Shell / Python（日志自动脱敏）
uv run colab-boost exec <session> "nvidia-smi" --shell

# 带 SHA256 校验的分块直传与拉取文件
uv run colab-boost upload <session> "G:\local\file.zip" "/content/file.zip"
uv run colab-boost download <session> "/content/minimax-h3/output/shot.mp4" "G:\local\shot.mp4"

# 释放单个实例并核验 unassign 回执
uv run colab-boost stop <session>

# 一键释放全部实例并核验零计费残留 + 生成关闭回执
uv run colab-boost stop-all
```

---

## 🧪 自动化测试

所有测试均在本地隔离目录与模拟协议服务下运行，**绝不触碰真实 Google 账号或产生任何计费**：

```powershell
uv run pytest -v
```

架构细节、Colab 底层协议说明与自定义配方编写规范请参见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。
