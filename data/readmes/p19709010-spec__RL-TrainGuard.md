# RL-TrainGuard

**A Lightweight Real-Time Monitoring Dashboard for AI Training**

RL-TrainGuard 是一个独立、通用的训练监控工具。只需在训练命令前加上 `rlguard run --`，就可以在浏览器中实时查看硬件资源、训练进度、ETA、Loss、Reward、学习率，以及本地保存的历史 Run 对比。

![RL-TrainGuard Dashboard](docs/dashboard.png)

## 功能

- 自动采集系统 CPU、RAM、Swap，以及训练进程 CPU、RSS。
- 通过 NVIDIA NVML 采集 GPU 利用率、VRAM、温度和功耗；GPU 不可用时自动降级。
- 记录训练 PID、起止时间、耗时、退出码，并判断 Running / Finished。
- 通过简单 Python API 上报 Step、Epoch、Loss、Reward 和学习率。
- 根据 `step / total_steps` 或 `epoch / total_epochs` 计算进度与 ETA。
- Dashboard 每秒刷新训练指标和资源曲线。
- 使用本地 SQLite 持久化资源与训练指标历史，不依赖数据库服务。
- 支持选择 2–3 个 Run，按 Step 对比 Loss 和 Reward 曲线。

> GPU 利用率和显存是整张 GPU 的设备级指标，不代表训练进程独占使用量。

## 安装

环境要求：Python 3.10+，推荐 Python 3.12。GPU 监控需要可用的 NVIDIA 驱动。

```bash
cd ~/projects/RL-TrainGuard
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 启动 Demo

```bash
rlguard run -- python examples/demo_train.py
```

打开：

```text
http://127.0.0.1:7865
```

Demo 是 CPU-only 任务，不进行 GPU 压力测试，并会持续上报全部训练指标。再次运行 Demo 后，Dashboard 历史列表会保留之前的 Run；勾选两到三条记录即可对比 Loss 和 Reward 曲线。

监控自己的训练任务：

```bash
rlguard run -- python train.py
```

修改端口或历史目录：

```bash
rlguard run --port 8080 --data-dir .rlguard -- python train.py
```

训练自然退出后，监控服务会继续运行，以便查看最终状态和历史。按 `Ctrl+C` 退出监控；如果训练仍在运行，退出时会正常终止训练进程。

## 上报训练指标

在训练代码中调用 `rlguard.log()`：

```python
from rlguard import log

log(
    step=100,
    total_steps=10000,
    epoch=2,
    total_epochs=100,
    loss=0.35,
    reward=0.72,
    learning_rate=1e-4,
)
```

`rlguard run` 会向训练进程注入 `RLGUARD_API_URL` 和 `RLGUARD_RUN_ID`，因此无需额外配置。推荐每 N 个 Step 上报一次，避免对训练循环造成不必要的网络开销。

所有字段都是可选的，未提供的值会沿用最后一次上报结果。`total_steps` 优先用于进度计算；未提供时使用 `total_epochs`。如果在 `rlguard run` 之外调用，或监控服务暂时不可达，`log()` 返回 `False`，不会中断训练。

## API

- `GET /api/status`：当前 Run 状态、最新硬件采样。
- `GET /api/history`：当前 Run 的资源与训练指标历史。
- `POST /api/metrics`：训练进程指标上报入口。
- `GET /api/runs`：持久化的 Run 列表。
- `GET /api/runs/{run_id}`：指定 Run 的完整资源与指标历史。

历史默认写入 `.rlguard/history.sqlite3`。CPU/RAM 曲线在 Dashboard 中显示最近 90 个采样点，完整资源采样最多在内存中保留最近 3600 个点并同步写入 SQLite。

## 测试

```bash
pytest
ruff check .
```

## 范围

当前版本面向本机单次训练监控，只采集 GPU 0。它不负责训练控制、自动终止、Checkpoint 管理或远程多用户认证。
