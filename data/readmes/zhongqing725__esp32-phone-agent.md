# ESP32-S3 Phone Agent

**Control an Android phone with an ESP32-S3 — no PC, no ADB host, no root.**

An ESP32-S3 board connects to the phone's Wi-Fi hotspot, talks to the
[Mobilerun Portal](https://github.com/droidrun/mobilerun) app over HTTP, reads the
accessibility tree, asks a DeepSeek model what to do next, and taps/swipes/types on
the phone. The whole agent loop runs on the microcontroller; the board only needs
USB power once it is flashed.

> 中文简介：一块 ESP32-S3 自制“手机操作盒子”。上电 → 连手机热点 → 通过手机上的
> Mobilerun Portal 读取界面文字/控件 → 调 DeepSeek 决策 → 自动点按/滑动/输入，
> 最后把结果打印出来。**全程不需要电脑**（USB 只在烧录/看日志时用）。

```
┌─────────────────────────┐      Wi-Fi (2.4 GHz)      ┌──────────────────────────┐
│ ESP32-S3 (MicroPython)  │  HTTP :8080 Bearer token  │ Android phone            │
│  · Wi-Fi STA            │ ◄───────────────────────► │  · Mobilerun Portal      │
│  · Portal HTTP client   │                           │    - accessibility tree  │
│  · DeepSeek HTTPS       │                           │    - tap / swipe / input │
│  · agent loop           │                           └──────────────────────────┘
│  · BOOT button = abort  │            HTTPS
└───────────┬─────────────┘   ┌──────────────────────┐
            └───────────────► │ api.deepseek.com     │
                              │ deepseek-v4-pro      │
                              └──────────────────────┘
```

## Verified results

Tested on an ESP32-S3 (N16R8: 16 MB flash + 8 MB octal PSRAM) and a OnePlus Ace 6T
(Android 16), with the phone hotspot enabled and Portal 0.7.25 installed:

| Task (natural language) | Steps | Result |
|---|---|---|
| 打开设置，找到 Android 版本 | 12 | ✅ answered `Android 16` |
| 打开设置，查看电池剩余电量 | 6 | ✅ answered `15%` (matches `dumpsys battery`) |

![evidence](evidence-esp32-android16.png)

## How it works

1. **Phone side**: install the open-source Mobilerun Portal app (or use the
   `mobilerun setup` CLI) and enable its accessibility service. Portal exposes a
   local HTTP API on `0.0.0.0:8080` protected by a Bearer token.
2. **ESP32 side**: MicroPython firmware in `firmware/`:
   - `main.py` — join the phone hotspot, find Portal via the DHCP gateway, run the task.
   - `portal.py` — tiny HTTP client for the Portal contract (`/state`, `/tap`,
     `/swipe`, `/keyboard/*`, `/app`).
   - `llm.py` — minimal HTTPS client for DeepSeek chat completions.
   - `agent.py` — compresses the a11y tree, builds the prompt, parses one JSON
     action per step, executes it, repeats until `done` (max steps bounded).
3. **Actions**: `tap`, `tap_text` (tap by visible label — much more reliable),
   `swipe`, `input`, `key` (back/home/enter/delete), `open` (start an app), `wait`, `done`.

## Requirements

- **Hardware**: ESP32-S3 devkit (8 MB PSRAM recommended; boards without PSRAM can
  still run text-only tasks). USB cable for flashing/power.
- **Phone**: Android with the Mobilerun Portal app (MIT). Only USB debugging is
  needed once to read Portal's token.
- **DeepSeek API key**: https://platform.deepseek.com
- **PC (one-time only)**: Python 3 with `esptool` and `mpremote`.

```powershell
python -m pip install esptool mpremote
```

## Quick start

### 1. Prepare the phone

1. Install the Mobilerun Portal app on the phone and enable its accessibility service
   (easiest: run `mobilerun setup` from a PC once, or install the APK manually).
2. Turn on the phone's **Personal Hotspot**, set the band to **2.4 GHz** (ESP32-S3 has
   no 5 GHz radio), and note the SSID/password. Keep the hotspot on.
3. Read the Portal token once over adb:

   ```powershell
   adb shell content query --uri content://com.mobilerun.portal/auth_token
   ```

   The token is stable for one Portal installation; it only changes on reinstall.

### 2. Configure the firmware

```powershell
copy firmware\config.example.py firmware\config.py
# edit firmware\config.py: WIFI_SSID, WIFI_PASSWORD, PORTAL_TOKEN, DEEPSEEK_API_KEY, TASK
```

`firmware/config.py` is git-ignored — never commit real secrets.

### 3. Download MicroPython images (once)

```powershell
python tools\download_firmware.py
```

### 4. Flash the board

Hold **BOOT**, plug USB (or press RST), release BOOT after ~2 s, then:

```powershell
powershell -ExecutionPolicy Bypass -File flash.ps1
```

The script detects the board, reads chip/flash info, flashes the matching MicroPython
image at `0x0`, uploads the firmware files and resets. For later task changes only:

```powershell
powershell -ExecutionPolicy Bypass -File deploy.ps1
```

### 5. Run without a PC

Give the board any USB power (charger/power bank). It connects to the hotspot, runs
`TASK` from `config.py`, prints the result over serial, and stops. Press **BOOT**
during a run to abort.

To watch logs while USB is connected:

```powershell
python -m mpremote connect COM9 repl     # Ctrl-] to exit
```

## Tweaking

- **Task**: edit `TASK` and `MAX_STEPS` in `firmware/config.py`, then `deploy.ps1`.
- **Model**: `DEEPSEEK_MODEL` — `deepseek-v4-pro` (better planning) or
  `deepseek-flash` (faster/cheaper). Reasoning models need a larger `max_tokens`
  (already set to 8000 in `llm.py`).
- **Vision**: not supported on purpose — Portal screenshots are ~4 MB each, which is
  impractical for the microcontroller. The agent reasons over the accessibility tree.
- **PC prototyping**: `tools/agent_pc.py` runs the same agent logic on a PC through
  `adb forward tcp:18080 tcp:8080`, useful when tuning prompts before flashing.

## Known limitations

- No vision: apps that expose little to the accessibility tree (games, some WebViews)
  will be hard to operate.
- 3–10 s per step (the model thinks); long tasks may hit the step limit.
- Typing text (`input`) requires the **Portal keyboard** to be the active IME:
  `adb shell ime set com.mobilerun.portal/.input.MobilerunKeyboardIME`.
- The task is compiled into `config.py`; there is no on-device task input yet.
- Phone hotspot must stay on; token must be refreshed if Portal is reinstalled.
- One phone at a time. Automation may violate some apps' terms of service — use only
  on devices you own and for tasks you are allowed to automate.

## Repository layout

```
esp32-phone-agent/
├── firmware/
│   ├── config.example.py   # copy to config.py and fill in
│   ├── main.py             # boot entry: Wi-Fi → Portal → run
│   ├── portal.py           # Portal HTTP client
│   ├── llm.py              # DeepSeek HTTPS client
│   └── agent.py            # a11y tree → model decision → actions
├── tools/
│   ├── download_firmware.py  # fetch MicroPython images
│   ├── agent_pc.py           # PC prototype for prompt tuning
│   └── serial_log.py         # reset board and capture serial output
├── flash.ps1               # flash MicroPython + deploy firmware
├── deploy.ps1              # re-upload firmware files only
├── ARCHITECTURE.md         # protocol notes, design decisions, risks
├── evidence-esp32-android16.png
└── LICENSE (MIT)
```

## Credits & license

- [Mobilerun](https://github.com/droidrun/mobilerun) (formerly DroidRun) — Portal app
  and HTTP contract, MIT.
- [MicroPython](https://micropython.org) — ESP32-S3 runtime, MIT.
- DeepSeek API — LLM inference (bring your own key).

This project is MIT licensed; see [LICENSE](LICENSE).
Not affiliated with DeepSeek or Dataelem; use at your own risk.
