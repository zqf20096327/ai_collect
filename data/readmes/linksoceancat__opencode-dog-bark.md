# opencode-dog-bark

当 [opencode](https://opencode.ai) 智能体在思考时，循环播放一段逐渐加速的“大狗叫”；思考结束的瞬间，播放一段 5 秒的持续长嚎“叫~~~~~~”。

思路很简单：opencode 会把模型的推理过程以 `reasoning` 消息片段流式输出。一个小插件监听这些片段，发布 `thinking` / `thinking.done` 状态；一个微型播放器守护进程读取该状态，通过 [mpv](https://mpv.io) 的 IPC 套接字控制播放，分三个 3 秒阶段逐渐加速，并在推理结束时切换到最终的长嚎。

```
opencode ──reasoning 片段──▶ thinking-watch (插件) ──▶ thinking.state
                                                              │
                                                    think-audio (守护进程)
                                                              │  mpv IPC
                                                              ▼
                                          0-3s 0.7→1.0x │ 3-6s →1.6x │ 6-9s →2.5x │ 保持
                                          推理结束 ─▶ 5 秒长嚎
```

## 行为

智能体思考期间，`大狗`（`大` + `狗`）片段循环播放并不断加速：

| 已用时间 | 播放速度 |
| -------- | -------- |
| 0–3 秒   | 加速到 1.0x |
| 3–6 秒   | 加速到 1.6x |
| 6–9 秒   | 加速到 2.5x |
| > 9 秒   | 保持 2.5x，继续循环，直到思考结束 |

推理结束时播放一次 `叫_5s.wav`，然后静音，等待下一次思考。循环接缝做了淡化处理，变速是连续的，因此没有爆音、没有跳变。

## 环境要求

- Linux，且运行着音频服务（PipeWire/PulseAudio），并已安装 `mpv`
- `python3`
- opencode（用于加载插件）
- `ffmpeg`（仅在你需要从源头重新生成音频素材时需要）

## 安装

```bash
git clone <本仓库地址> opencode-dog-bark
cd opencode-dog-bark
./install.sh
```

`install.sh` 会复制以下内容：

| 从                    | 到                                        |
| --------------------- | ----------------------------------------- |
| `bin/think-audio`     | `~/.local/bin/think-audio`                |
| `plugins/thinking-watch.ts` | `~/.config/opencode/plugins/`       |
| `systemd/think-audio.service` | `~/.config/systemd/user/`         |
| `assets/*.wav`        | `~/.local/share/opencode-dog-bark/`       |

然后**重启 opencode** 以加载插件。可用以下命令检查播放器：

```bash
systemctl --user status think-audio
tail -f ~/.local/state/opencode/thinking.log   # 状态跳变记录
```

## 配置

编辑 `~/.config/systemd/user/think-audio.service`（或直接导出环境变量），然后执行
`systemctl --user restart think-audio`：

| 变量                | 默认值            | 含义                             |
| ------------------- | ----------------- | -------------------------------- |
| `THINK_START_SPEED` | `0.7`             | 起始速度                         |
| `THINK_SPEED_1/2/3` | `1.0` / `1.6` / `2.5` | 每个阶段结束时的速度         |
| `THINK_SEG`         | `3`               | 每个阶段的秒数                   |
| `THINK_END_DUR`     | `5`               | 结束长嚎的时长（秒）             |
| `THINK_VOLUME`      | `80`              | mpv 音量                         |
| `THINK_LOOP_AUDIO`  | 内置 `大狗_loop.wav` | 循环片段                     |
| `THINK_END_AUDIO`   | 内置 `叫_5s.wav`     | 结束片段                     |
| `THINK_STATE`       | `~/.local/state/opencode/thinking.state` | 状态文件 |

## 音频素材

两个运行时音频已随仓库提交，开箱即用；它们的生成流程也一并放在 `scripts/` 下：

```bash
# 1. 下载玩具的 audio-data.js（内含 base64 的 WAV）
curl -sSL --compressed \
  'https://www.bilibilitoy.com/toy/Dagou-Tap/12420391163904-v7471/audio-data.js' \
  -o audio-data.js

# 2. 提取原始片段
python3 scripts/extract_audio.py audio-data.js extracted

# 3. 生成 assets/大狗_loop.wav 与 assets/叫_5s.wav
./scripts/build_assets.sh extracted assets
```

音频的来源与版权见 [NOTICE](NOTICE)。

## 卸载

```bash
systemctl --user disable --now think-audio
rm ~/.local/bin/think-audio \
   ~/.config/opencode/plugins/thinking-watch.ts \
   ~/.config/systemd/user/think-audio.service
rm -rf ~/.local/share/opencode-dog-bark
```

## 许可证

代码采用 MIT 许可（见 [LICENSE](LICENSE)）。随附的音频**不**在 MIT 许可范围内，详见
[NOTICE](NOTICE)。
