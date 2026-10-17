# Tiny LLM Studio — 从零训练 0.1B 中文大模型的端到端工作台

在 Apple Silicon（M 系列）MacBook 上从零训练一个 ~0.1B 参数、类 LLaMA 架构（RoPE + RMSNorm + SwiGLU + GQA）的中文大模型，全程在一个 Web UI 里完成：

- **Tiny LLM Studio**（FastAPI + React Web UI）：数据源 → 采集任务 → Tokenizer → 数据集 → 训练，一站式
- 32k byte-level BPE tokenizer
- 类 LLaMA 模型实现（≈ 96M 参数）
- 预训练（pretrain）
- 监督微调（SFT）
- 直接偏好优化（DPO）
- 推理与流式 chat CLI

> 目标硬件：MacBook Pro M4 Pro / 48GB（统一内存），PyTorch ≥ 2.5 + MPS 后端。

## 快速开始

```bash
# 1. 安装依赖（推荐 uv，或直接 pip）
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# 2. 下载并清洗最小语料（默认抽样 ~5GB）
bash scripts/01_collect_minimal.sh

# 3. 训练 32k BPE tokenizer
bash scripts/02_train_tokenizer.sh

# 4. 预训练（先跑 0.5B tokens 验证，~12h on M4 Pro）
bash scripts/03_pretrain.sh

# 5. SFT
bash scripts/04_sft.sh

# 6. DPO
bash scripts/05_dpo.sh

# 7. 与模型对话
bash scripts/06_chat.sh

# 8. 启动 Tiny LLM Studio（FastAPI + Web UI）
bash scripts/07_corpus_platform.sh
# 浏览器访问 http://localhost:8000
# 想让 LAN 外的同事也能访问？看下面「公网访问 Web UI（Tunnel 模式）」一节。

# 9. 扩量训练（2-5B tokens）
bash scripts/08_pretrain_scale.sh

# 10. 评估困惑度
bash scripts/09_eval.sh checkpoints/pretrain/latest.pt
```

## Smoke test（验证模型代码）

```bash
PYTHONPATH=src pytest tests/ -v
```

## 目录结构

```text
100M/
├── configs/           # YAML 配置（模型、训练超参）
├── src/llm/           # 模型、tokenizer、训练、推理
├── src/corpus/        # Tiny LLM Studio 后端（FastAPI + React WebUI）
├── scripts/           # 一键运行脚本
├── data/              # 数据（gitignore）
└── checkpoints/       # 模型权重（gitignore）
```

## 模型规格

| 配置                      | 值        |
| ------------------------- | --------- |
| 参数量                    | ≈ 96M     |
| `vocab_size`              | 32000     |
| `hidden_size`             | 768       |
| `num_hidden_layers`       | 12        |
| `num_attention_heads`     | 12        |
| `num_key_value_heads`     | 4 (GQA)   |
| `intermediate_size`       | 2048      |
| `max_position_embeddings` | 2048      |
| `tie_word_embeddings`     | true      |

## 关于在 M4 上的训练时间

实测吞吐约 **8k–15k tokens/s**（bf16 + MPS）。

| 数据规模    | 预计时间       | 备注                  |
| ----------- | -------------- | --------------------- |
| 0.5B tokens | ~12 小时       | 验证 loss 收敛        |
| 2B tokens   | ~2 天          | 接近 Chinchilla 最优  |
| 5B tokens   | ~5–8 天        | 极限级训练            |

支持 `--resume` 中断续训，无需一次跑完。

## 镜像加速

国内访问 HuggingFace 慢，使用：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

## 公网访问 Web UI（Tunnel 模式）

类似 `expo start --tunnel`：本地启动 WebUI 后开一条公网隧道，访问者**不需要**和你在同一局域网（甚至不需要在同一个国家）即可使用 Web UI 和所有 API。

实现基于 [ngrok 官方 Python SDK](https://github.com/ngrok/ngrok-python)（`pip install ngrok`，自带 Rust 客户端，**无需**安装外部 `ngrok` 二进制或 `ngrok.yml`）。

> 为什么需要 ngrok？ngrok 服务端从 2022 年起强制要求所有 client 携带 authtoken（用于反滥用），匿名 tunnel 已经被关闭，这是服务端策略，没有任何 SDK / wrapper 能绕过。注册和获取 token 都是免费的，整个流程不到 1 分钟。

### 快速三步

```bash
# 1. 安装 tunnel 可选依赖（一次性）
pip install -e ".[tunnel]"
#  ↑ 等价于 pip install ngrok ；这个依赖体积 ~5MB，且只在你想开 tunnel 时才用，
#    所以默认不在主依赖里。

# 2. 拿一个 ngrok authtoken（一次性，下面有详细步骤）
export NGROK_AUTHTOKEN="2abc...你自己的 token..."

# 3. 启动 Tiny LLM Studio + tunnel
TUNNEL=1 bash scripts/07_corpus_platform.sh
```

启动成功后会打印类似 banner（**包含可直接用手机摄像头扫描的二维码**，对齐 `expo start --tunnel` 的体验）：

```text
================================================================
  Tiny LLM Studio
  Session:    tinyllm-9g7xph45b
  Local URL:  http://localhost:8000
  Public URL: https://<random-pet-name>.ngrok-free.dev

  Scan with your phone camera to open on a mobile device:

 ▄▄▄▄▄▄▄ ▄   ▄▄   ▄   ▄▄   ▄▄▄▄▄▄▄
 █ ▄▄▄ █ ▄▀▄ ▄▄ ▄ ▄ ▄█▄▀▄█ █ ▄▄▄ █
 █ ███ █  ██  ▄ ▄ ▄ ▄ ▀▄▀  █ ███ █
 █▄▄▄▄▄█ █▀▄▀▄▀▄▀▄▀▄▀▄▀█ █ █▄▄▄▄▄█
 ...（unicode block QR，约 17 行）...
 █▄▄▄▄▄█ ▄ ▄▄▄▀▀▄▄ ███ █ █▀████  ▄

  WARNING: the WebUI is now exposed to the public internet.
           Anyone with the URL above can access /api/* and
           trigger jobs / training / publishing. Treat the
           URL as a secret.
================================================================
```

- 把 `Public URL` 发给在 PC 上的访问者；让手机用户直接扫终端里的**二维码**。二维码用 `▀▄█` 半块字符渲染，密度跟 expo 一致，主流终端（macOS Terminal / iTerm / Alacritty / Windows Terminal / VS Code 内置终端）都能正确显示。
- `Session` 是本地生成的会话标签（也作为 metadata 上报到 ngrok dashboard，方便你在多次启动之间区分会话），它**不是**公网地址。
- 如果终端没装 `qrcode` 可选依赖，二维码会被静默跳过，URL 仍然正常打印——不会因为缺一个可视化辅助而启动失败。

### 怎么申请 ngrok authtoken（详细步骤）

ngrok 全程**免费**（注册免费、tunnel 免费、流量在免费额度内免费），只是要绑定一个账号。

1. **注册账号**：打开 https://dashboard.ngrok.com/signup
   - 用邮箱/Google/GitHub 任选一种注册即可
   - 不需要绑卡、不需要付费
   - 注册完成后会自动跳到 dashboard

2. **取 authtoken**：打开 https://dashboard.ngrok.com/get-started/your-authtoken
   - 页面会直接展示你的 authtoken（形如 `2abc...XYZ`，约 50 字符）
   - 点 **Copy** 按钮复制

3. **设置环境变量**：把 token 写到 shell 配置里，以后就不用再处理了。

   - **macOS / Linux（zsh，macOS 默认）**：
     ```bash
     echo 'export NGROK_AUTHTOKEN="2abc...你自己的 token..."' >> ~/.zshrc
     source ~/.zshrc
     ```
   - **macOS / Linux（bash）**：
     ```bash
     echo 'export NGROK_AUTHTOKEN="2abc...你自己的 token..."' >> ~/.bashrc
     source ~/.bashrc
     ```
   - **fish**：
     ```fish
     set -Ux NGROK_AUTHTOKEN "2abc...你自己的 token..."
     ```
   - **Windows（PowerShell，永久）**：
     ```powershell
     [Environment]::SetEnvironmentVariable("NGROK_AUTHTOKEN", "2abc...你自己的 token...", "User")
     ```
   - **临时**（仅当前 shell 会话有效）：
     ```bash
     export NGROK_AUTHTOKEN="2abc...你自己的 token..."
     ```

4. **验证生效**：
   ```bash
   echo $NGROK_AUTHTOKEN
   #  应当输出你的 token。如果空，说明环境变量没装好，请重开终端或 source 配置文件。
   ```

### 进阶用法

```bash
# 自定义端口
TUNNEL=1 bash scripts/07_corpus_platform.sh 9000

# 不在 shell 里持久化 token，只对一次启动生效（适合临时使用别人电脑）
NGROK_AUTHTOKEN="2abc..." TUNNEL=1 bash scripts/07_corpus_platform.sh

# 直接调底层 launcher（脚本内部就是这么调的）
NGROK_AUTHTOKEN="2abc..." python -m corpus.api.launcher --port 8000 --tunnel

# 关掉 tunnel：Ctrl-C 即可，launcher 会同时清理 ngrok session 与 uvicorn 进程
```

### 常见报错

| 报错 | 原因 | 解决 |
| --- | --- | --- |
| `ngrok requires an authtoken` | 没设 `NGROK_AUTHTOKEN` | 按上面步骤导出环境变量 |
| `ngrok python SDK is not installed` | 没装可选依赖 | `pip install -e ".[tunnel]"` |
| `ngrok.forward() failed: ... ERR_NGROK_108` | 你已经有一个免费 session 在跑 | 关掉别的 ngrok 实例（dashboard 也能 kick）|
| `address already in use` | 端口被前一次未清干净的进程占着 | `pkill -f corpus.api.launcher` 后重试 |
| 二维码不显示，只看到 URL | 没装 `qrcode` 可选依赖 / 终端不支持 UTF-8 | `pip install -e ".[tunnel]"`；终端切到 UTF-8 |

### 安全提醒

> ⚠️ Tiny LLM Studio 当前没有内置鉴权，开了 tunnel 等于把所有 `/api/*`（数据采集、
> 训练、发布、删除等）暴露到公网。**任何拿到这个 URL 的人都能用你的机器训练模型 / 删除数据**。
>
> 把 URL 当作密钥处理：
> - 只通过私聊（IM/邮件）发给你信任的人，**不要**发到群、issue、博客
> - 用完 Ctrl-C 立即关闭，URL 一旦关闭就永久失效（每次启动都是新随机域名）
> - 如果担心，可在 ngrok dashboard 撤销 session 或 rotate authtoken
