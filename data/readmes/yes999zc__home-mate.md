<p align="center">
  <img src="docs/assets/hero-banner-en.png" alt="Home Mate · XiaoRui (小瑞) — Pure-Rust Edge Voice Brain, Multi-Gateway Ecosystem & Master Family Agent" width="100%" />
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md"><strong>简体中文</strong></a> · <a href="https://mymate.homes"><strong>Official Website (mymate.homes)</strong></a>
</p>

<p align="center">
  <a href="https://mymate.homes"><img src="https://img.shields.io/badge/Website-mymate.homes-1f6b45?style=flat-square" alt="Website" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-2e7d4f?style=flat-square" alt="AGPL-3.0" /></a>
  <a href="LICENSE-PROTOCOL-APACHE-2.0"><img src="https://img.shields.io/badge/Protocol_v2_Spec-Apache--2.0-245a8d?style=flat-square" alt="Apache-2.0" /></a>
  <img src="https://img.shields.io/badge/Core-Pure_Rust_%2B_Vue_3-175536?style=flat-square" alt="Pure Rust + Vue 3" />
  <img src="https://img.shields.io/badge/Gateways-Linux_(Dot2%2FLX06)_%7C_Android_(Phone%2FPanel%2FDisplay)-364239?style=flat-square" alt="Supported Gateways" />
</p>

---

## What is Home Mate (XiaoRui / 小瑞)?

**Home Mate (小瑞)** is the next-generation evolution of [rui (小瑞)](https://github.com/yes999zc/rui), rewritten from scratch in **pure Rust** with a three-layer sovereign household architecture:

1. **On-Speaker Sovereign Edge Brain (`hm-core`) — Or NAS Docker Multi-Room Hub**
   - Unlike first-generation `rui`, Home Mate compresses the voice runtime (`hm-core` + Vue 3 Web Console `:8930` + `hm-gateway` + `hm-kws` Zipformer & Silero VAD) to run **100% directly inside ARM64 smart speakers** (Echo Dot 2 & 256 MB Xiaomi LX06) — with zero external streaming server required.
   - The exact same `hm-core` also runs in **Full Docker mode on a NAS / home server** (`linux/amd64` & `linux/arm64`), hosting **128 MB LX06 thin gateways** and **Android phones, tablets, smart displays, and 86 wall panels** simultaneously.
2. **Master Brain / Family Agent Orchestration (`brain.delegate / status / steer / cancel`)**
   - The edge speaker handles low-latency wake, instant Q&A, music/stories/reminders, and closed-loop Home Assistant control with mandatory post-action readback.
   - Complex long-horizon tasks, cross-tool research, briefings, and fleet diagnostics (`skills/home-mate-fleet`) are **delegated asynchronously to a Household Master Brain Agent** (Hermes / OpenAI-compatible Agent gateway) — never blocking everyday voice turns, with spoken callbacks back to the initiating room.
3. **Edge Brain + Multi-Gateway Strict Isolation (`Northbound Protocol v2`)**
   - A single `hm-core` concurrently manages multiple heterogeneous gateways (Echo Dot 2, LX06 256 MB / 128 MB, multiple Android devices) with:
     - **Per-device isolated sessions**, retreat context archiving (`退下`), and unified current + archived conversation clear (`DELETE /api/v0/devices/{id}/conversation`);
     - **Per-hardware-family KWS sensitivity isolation** (Dot2 `0.32 / 2.50`, LX06 `0.20 / 2.50`, Android `0.22 / 3.00`, with explicit per-device overrides winning — zero cross-family clobbering);
     - **Oneshot `wake_dur_ms` command slicing**, wake-ack tail bridging, millisecond local-exit interruption, and Bearer Token + opt-in private-LAN exemption (`lan_gateway_exempt`) security boundaries.
     - *(Note: Everyday voice interaction defaults to stable half-duplex with wake-word & local-exit barge-in; **Full-Duplex is currently in active development** and clearly labeled `In Dev` across the console and Android app.)*

> [!IMPORTANT]
> **Hardware Research Disclaimer & Custom Speaker Roadmap**
> 1. **For Research & Personal Experimentation Only**: Adaptation of third-party commercial speakers (**Xiaomi AI Speaker Pro `LX06`** and **Amazon Echo Dot 2 `RS03QR`**) in this project is provided **strictly for edge-AI architectural research, acoustic arbitration validation, and personal non-commercial experimentation**. All trademarks belong to their respective owners. This project is not affiliated with Xiaomi or Amazon and **does not sell modified third-party brand-name speakers**.
> 2. **First-Party Custom Speaker Under Active Development**: We are actively engineering a **dedicated custom Home Mate (小瑞) smart speaker hardware platform** featuring an open far-field microphone array, tuned acoustic enclosure, and native sovereign Rust firmware out of the box—requiring zero third-party unlock steps.

---

## Unified 3-Repository Ecosystem (Now Open: Linux Unified Gateway & Android Universal APK)

<p align="center">
  <img src="docs/assets/architecture-v3-en-light.png" alt="Home Mate Edge Brain, Multi-Gateway Isolation & Master Family Agent Architecture" width="100%" />
</p>

We have consolidated and opened the complete **3-repository Home Mate ecosystem**:

| Repository | Role & Highlights | License |
| :--- | :--- | :--- |
| **[yes999zc/home-mate](https://github.com/yes999zc/home-mate)** *(this repo)* | **Core Edge Brain & Console**: `hm-core` (Full Docker with in-process Silero VAD & `--slim` speaker build), Master Brain delegation, Multi-Gateway isolation, `hm-release` Ed25519 signed OTA manager, Vue 3 Web Console (`web/`), `tools/hm-provision.sh`, and Northbound v2 protocol contract. | `AGPL-3.0` (`Apache-2.0` Protocol v2 Spec) |
| **[yes999zc/home-mate-gateway-linux](https://github.com/yes999zc/home-mate-gateway-linux)** *(Unified Linux Gateway)* | **Replaces legacy separate `dot2` & `lx06` repos**: Feature-gated Rust hardware gateway supporting **Echo Dot 2 (`board-dot2`)**, **Xiaomi LX06 256 MB** (on-speaker Scheme A dual-wake), and **Xiaomi LX06 128 MB** (auto-detected Thin Gateway pairing with NAS Full Docker Core). | `AGPL-3.0` |
| **[yes999zc/home-mate-gateway-android](https://github.com/yes999zc/home-mate-gateway-android)** *(Universal Android Gateway)* | **One adaptive zero-dependency APK** (Android 5–16) turning **Android smart displays, 4-inch 86 wall panels (1:1), tablets, everyday phones, and repurposed old Android phones** into offline-KWS far-field voice terminals & multi-room controllers with GitHub Releases auto-update. | `AGPL-3.0` |

> **Migration Note**: Legacy single-board repositories (`home-mate-gateway-dot2` and `home-mate-gateway-lx06`) have been unified into **[yes999zc/home-mate-gateway-linux](https://github.com/yes999zc/home-mate-gateway-linux)**. All new deployments and AI agent scripts should target `home-mate-gateway-linux`.

### Which Combination Should I Choose?

| What Hardware You Have | Recommended Topology | External NAS/Server Needed? |
| :--- | :--- | :--- |
| **Xiaomi LX06 (256 MB RAM)** | On-speaker `hm-core --slim` + `hm-gateway` + `hm-kws` (Scheme A dual-wake with stock XiaoAi) | **No** (100% on-speaker) |
| **Xiaomi LX06 (128 MB RAM batch)** | Auto-detected **Thin Gateway** (`~1.6 MiB`) on speaker → **Full Docker `hm-core`** on NAS/Server | **Yes** (Full Docker `hm-core` on NAS/server) |
| **Amazon Echo Dot 2 (`RS03QR`)** | On-speaker Full `hm-core` + `hm-gateway` + `hm-kws` (7-mic + 160ms AEC + 12-LED ring) | **No** (100% on-speaker) |
| **Android Smart Display / 86 Wall Panel / Tablet / Old Android Phone** | **Full Docker `hm-core`** on NAS/Mac/PC + **Android Universal APK** (zero hardware flashing!) | **Yes** (or connect to an existing speaker Core in Manage-Only mode) |

---

## Xiaomi AI Speaker Pro (`LX06`) Highlights (Adaptive 256 MB / 128 MB)

Deployed via **[yes999zc/home-mate-gateway-linux](https://github.com/yes999zc/home-mate-gateway-linux)**, Home Mate automatically inspects `MemTotal` in `/proc/meminfo` and adapts to both Xiaomi factory batches:

1. **Adaptive 256 MB On-Speaker vs. 128 MB Thin Mode**:
   - **256 MB batch (`MemTotal >= 180,000 kB`)**: Unpacks the `<= 6.0 MiB` Scheme A archive (`/data/hm/hm-bundle.tar.xz`) into `120.9 MiB` `/tmp` RAM tmpfs on boot — `hm-core --slim`, Vue 3 Console (`:8930`), `hm-gateway`, and `hm-kws` (with hardware-calibrated `0.20 / 2.50` KWS sensitivity) run **100% on-speaker**.
   - **128 MB batch (`MemTotal < 180,000 kB`, ~59 MB `/tmp`)**: Automatically enters **Thin Gateway mode** (`hm-lx06-thin.tar.xz`, ~550 KB compressed / ~1.6 MiB unpacked, no local `hm-core` or `hm-kws`), dialing your **NAS / server Full Docker `hm-core`** over private LAN `:8932` (`--allow-lan-core`) or SSH reverse tunnel.
2. **Zero Damage to Stock Firmware (Dual-System Coexistence)**:
   - **0 bytes modified in stock SquashFS**: Factory read-only `mtd4 (system0)` and `mtd5 (system1)` partitions remain **100% untouched** (zero brick risk).
   - **1-Line Factory Restore**: Run `rm -rf /data/hm /data/init.sh && reboot` over SSH to return to 100% stock state.
3. **Instant System Switching by Wake Word (256 MB Dual-Wake)**:
   - Say **"XiaoAi TongXue" (小爱同学)** → Answered natively by stock Xiaomi XiaoAi.
   - Say **your custom wake word (e.g. "NiHao GaoDa" / "NiHao XiaoZhi")** → Answered by **Home Mate**.
   - Say **"QieHuan XiaoAi" (切换小爱)** *(or long-press Play/Pause 1.5 s)* → Immediately yields or toggles pinned stock XiaoAi mode.

---

## Live Interface Gallery: Android Universal App & Web Console

### Android Universal Client & Voice Gateway (`v2.3.10+` · 4:3 & 1:1 Adaptive Layouts)

One APK adapts cleanly across phones, repurposed spare phones, 4-inch 86 wall control panels (`1:1`), and smart displays / tablets (`4:3`) — featuring offline Sherpa-ONNX JNI KWS, mid-playback PBFDAF AEC barge-in, unified conversation history with one-tap clear, whole-house multi-room controls, battery exemption management, and GitHub Releases auto-updates:

<table>
  <tr>
    <td width="50%">
      <img src="docs/assets/android-en-voice-history-4x3.png" alt="Android Voice Orb & Unified History Sheet (4:3)" />
      <p align="center"><strong>1. Voice Companion &amp; Unified History Clear (Phone · 4:3)</strong><br>3D nebula orb, bottom live transcript synced with top-right history sheet &amp; one-tap Clear (current + archived)</p>
    </td>
    <td width="50%">
      <img src="docs/assets/android-en-rooms-settings-4x3.png" alt="Android Whole-House Rooms & Settings (4:3)" />
      <p align="center"><strong>2. Whole-House Control &amp; Settings (Phone · 4:3)</strong><br>Multi-room Core switching, Kiosk 86-panel launcher, battery keep-alive &amp; GitHub Releases auto-update</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="docs/assets/android-en-display-4x3.png" alt="Android Smart Display & Tablet Layout (4:3)" />
      <p align="center"><strong>3. Smart Display / Tablet Adaptive Layout (Native 4:3)</strong><br>Automatic left navigation rail for landscape smart displays, bedside stands &amp; tablets</p>
    </td>
    <td width="50%">
      <img src="docs/assets/android-en-panel86-1x1.png" alt="Android 4-Inch 86 Wall Control Panel Layout (1:1)" />
      <p align="center"><strong>4. 4-Inch 86 Wall Control Panel Layout (Native 1:1)</strong><br>Compact square UI with optional Kiosk Home Launcher mode for wall-mounted Android panels</p>
    </td>
  </tr>
</table>

### Built-In Web Console (`:8930` · Light Theme Default)

Every Core (on-speaker or NAS Docker) serves the responsive Vue 3 Web Console directly at `http://<CORE_IP>:8930`:

<table>
  <tr>
    <td width="50%">
      <img src="docs/assets/lx06-en-status-light.png" alt="Status Overview (/status)" />
      <p align="center"><strong>1. Status Overview (<code>/status</code>)</strong><br>Readiness checks, gateway connection generation, microphone capture state &amp; active program</p>
    </td>
    <td width="50%">
      <img src="docs/assets/lx06-en-interaction-light.png" alt="Wake Word & Interaction (/interaction)" />
      <p align="center"><strong>2. Wake Words &amp; Follow-up (<code>/interaction</code>)</strong><br>Custom wake phrases, per-family sensitivity, 9s follow-up window &amp; local exit words</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="docs/assets/lx06-en-devices-light.png" alt="Hardware & Audio Gate (/devices)" />
      <p align="center"><strong>3. Hardware &amp; Audio Gate (<code>/devices</code>)</strong><br>Firmware status, room assignment, Silero VAD dBFS gates &amp; post-playback blind window</p>
    </td>
    <td width="50%">
      <img src="docs/assets/lx06-en-eq-vad-light.png" alt="Custom 3-Band EQ (/devices)" />
      <p align="center"><strong>4. Speaker Voicing EQ (<code>/devices</code>)</strong><br>Dedicated 3-band custom woofer curve for Xiaomi LX06 and 10-band EchoMuse curve for Echo Dot 2</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="docs/assets/console-en-services-light.png" alt="AI Brain Services (/services)" />
      <p align="center"><strong>5. LLM, ASR, TTS &amp; Master Brain (<code>/services</code>)</strong><br>Primary/fallback LLMs (DeepSeek / GLM / OpenAI), Qwen3-ASR, Volcengine TTS &amp; Master Family Agent config</p>
    </td>
    <td width="50%">
      <img src="docs/assets/console-en-ha-readback-light.png" alt="Home Assistant Readback (/tools)" />
      <p align="center"><strong>6. Home Assistant Closed-Loop Readback (<code>/tools</code>)</strong><br>Auto-discovered Assist entities with mandatory post-action state readback verification</p>
    </td>
  </tr>
</table>

---

## Quickstart & AI Coding Agent Deployment Prompts (4 Tracks)

### Track A: Xiaomi AI Speaker Pro (`LX06`) — Adaptive 256 MB / 128 MB Deploy

#### Prerequisites
1. **Model & Memory Check**: Black cylinder **Xiaomi AI Speaker Pro (`LX06`, A113X `aarch64`)**. Always run `grep ^MemTotal /proc/meminfo` over SSH first to identify **256 MB (`>= 180,000 kB`)** vs. **128 MB (`< 180,000 kB`)**.
2. **Root SSH Unlocked**: Enable root SSH (port 22) via [idootop/open-xiaoai](https://github.com/idootop/open-xiaoai).
3. **If 128 MB Batch**: Deploy **Track C (Full Docker `hm-core` on NAS/Server)** first — never use `--slim` on the NAS.

#### Manual Commands
```bash
git clone https://github.com/yes999zc/home-mate.git
git clone https://github.com/yes999zc/home-mate-gateway-linux.git
cd home-mate-gateway-linux

# Option A1 — 256 MB LX06 (100% on-speaker dual-wake):
./tools/pack_lx06_bundle.sh
python3 -m http.server 18089 --directory build/lx06 &
./deploy/lx06/install-lx06.sh --device-ip 192.168.1.50 --kws-url http://192.168.1.10:18089/hm-kws-lx06.tar.xz

# Option A2 — 128 MB LX06 (Thin Gateway -> NAS Full Docker hm-core):
./tools/pack_lx06_bundle.sh --thin
./deploy/lx06/install-lx06.sh --thin --device-ip 192.168.1.50 --core-addr 192.168.1.10:8932 --device-id lx06-living
```

#### Let an AI Coding Agent Deploy LX06 (Auto-Detects 256 MB vs 128 MB)
Copy and paste into **Claude Code, Cursor, Codex, or Antigravity** *(replace the example IPs `192.168.1.50` and `192.168.1.10` with your real LAN IPs)*:
```text
Help me deploy Home Mate (XiaoRui) onto my Xiaomi AI Speaker Pro (LX06, root SSH enabled via open-xiaoai):
[Replace the two example IPs below with your real LAN IPs]
- LX06 Speaker SSH: root@192.168.1.50
- LAN NAS / Host IP: 192.168.1.10

Follow these strict rules:
1. NEVER modify stock SquashFS partitions (mtd4 / mtd5). Use only non-invasive Storage Scheme A under /data/hm and /data/init.sh.
2. Clone https://github.com/yes999zc/home-mate.git and https://github.com/yes999zc/home-mate-gateway-linux.git side by side.
3. SSH into root@<SPEAKER_IP> and inspect `uname -m`, `grep ^MemTotal /proc/meminfo`, and `df -k /data /tmp`:
   - If MemTotal >= 180000 kB (256 MB batch -> On-Speaker Dual-Wake):
     a) Verify /data has >= 6000 KB free, pack with `./tools/pack_lx06_bundle.sh`, and serve `build/lx06/` on <HOST_IP>:18089 (confirm HTTP 200 on `hm-kws-lx06.tar.xz`).
     b) Run `./deploy/lx06/install-lx06.sh --device-ip <SPEAKER_IP> --kws-url http://<HOST_IP>:18089/hm-kws-lx06.tar.xz`.
     c) Verify `hm-core`, `hm-gateway`, and `hm-kws` are running, `http://<SPEAKER_IP>:8930` loads HTTP 200, and `/api/v0/mode` shows LX06 KWS `0.20 / 2.50`.
   - If MemTotal < 180000 kB (128 MB batch -> Thin Gateway + NAS Full Core):
     a) First deploy or verify **Full Docker `hm-core`** (NOT `--slim`, with `HM_GATEWAY_ALLOW_LAN=1`) from `yes999zc/home-mate` on <HOST_IP> (`docker compose up -d`).
     b) In `home-mate-gateway-linux`, run `./tools/pack_lx06_bundle.sh --thin` and install with `./deploy/lx06/install-lx06.sh --thin --device-ip <SPEAKER_IP> --core-addr <HOST_IP>:8932` (pass `--core-token` if `lan_gateway_exempt` is disabled).
     c) Verify ONLY `hm-gateway` runs on the speaker (no local `hm-core`/`hm-kws`) and the speaker appears online at `http://<HOST_IP>:8930`.
4. Never commit real IPs or tokens to Git. Pair a household admin token and save it to `~/.home-mate/` (chmod 600).
```

---

### Track B: Amazon Echo Dot 2 (`RS03QR`) — 1-Command Provisioning (`tools/hm-provision.sh`)

#### Prerequisites
1. **Bootrom Unlocked via `firebreak` (`amonet`)**: Unlock over Micro-USB using [yes999zc/firebreak](https://github.com/yes999zc/firebreak) (`uvx firebreak@latest`) with your stock `p10` partition backed up.
2. **`emOS` Audio Base & Wi-Fi**: USB serial console (`/dev/cu.usbmodem*` or `/dev/ttyACM*`) responds with `ID=emos` and is connected to Wi-Fi via `em-wifi`.

#### Manual Commands
```bash
# 1. Read-only dry-run preflight:
./tools/hm-provision.sh --device-id dot2-living \
  --seed build/bootstrap/home-mate-bootstrap-dot2-living.tar.gz \
  --release build/release/home-mate-release.tar \
  --serial /dev/cu.usbmodem8401 --ip 192.168.1.73 \
  --wake-word 你好小智 --dry-run

# 2. Remove --dry-run to install, activate (8/8 health checks), pair token & optionally clone config:
./tools/hm-provision.sh --device-id dot2-living \
  --seed build/bootstrap/home-mate-bootstrap-dot2-living.tar.gz \
  --release build/release/home-mate-release.tar \
  --serial /dev/cu.usbmodem8401 --ip 192.168.1.73 \
  --wake-word 你好小智
```

#### Let an AI Coding Agent Provision Echo Dot 2
```text
I have an Amazon Echo Dot 2 (RS03QR) unlocked via firebreak (amonet) and running emOS on Wi-Fi:
- USB Serial Port: /dev/cu.usbmodem8401   <-- Replace or auto-detect via `ls /dev/cu.usbmodem* /dev/ttyACM*`
- Speaker LAN IP:  192.168.1.73           <-- Replace with actual LAN IP
- (Optional) Reference Speaker IP: 192.168.1.50

In `yes999zc/home-mate` (with `yes999zc/home-mate-gateway-linux` if rebuilding firmware via `./tools/build_firmware.sh` — never raw `cargo zigbuild`), run `./tools/hm-provision.sh --dry-run` first for `--device-id dot2-living --wake-word 你好小智`, report preflight results, then execute the real provision, verify 8/8 activation health checks, and save the token to `~/.home-mate/dot2-living.token` (chmod 600).
```

---

### Track C: NAS / Docker Full Core (Multi-Gateway Hub for 128 MB LX06 & Android)

Deploy **Full `hm-core`** (including in-process Silero VAD + Vue 3 Console) on Synology, fnOS, UGREEN, Unraid, Raspberry Pi, Linux, or macOS. With `HM_GATEWAY_ALLOW_LAN=1`, it hosts multiple Android terminals and 128 MB LX06 thin gateways concurrently while keeping every device's sessions, audio streams, and KWS thresholds strictly isolated.

```bash
docker run -d \
  --name home-mate-core \
  --restart unless-stopped \
  -p 8930:8930 \
  -p 8932:8932 \
  -p 8933:8933/udp \
  -e TZ=Asia/Shanghai \
  -e HM_GATEWAY_ALLOW_LAN=1 \
  -v "$(pwd)/data:/data" \
  ghcr.io/yes999zc/home-mate:latest
```
*(Or run `docker compose up -d` using the bundled `docker-compose.yml`; always pair a household admin token immediately on first login at `http://<NAS_IP>:8930`!)*

#### Let an AI Coding Agent Deploy NAS Docker Full Core + Master Brain
```text
Help me deploy Home Mate Full Docker `hm-core` on my LAN NAS/server at 192.168.1.10 from https://github.com/yes999zc/home-mate:
1. Start the standard FULL `hm-core` image (NEVER `--slim`) with `HM_GATEWAY_ALLOW_LAN=1`, persistent volume `./data:/data`, and ports 8930/tcp (Web Console), 8932/tcp (Northbound v2 Gateways), and 8933/udp (LAN Auto-Discovery).
2. Verify `http://192.168.1.10:8930/` returns HTTP 200 and `/api/v0/status` reports healthy vault & DB.
3. Immediately pair a household admin Bearer token via `/api/v0/auth/provision` (save to `~/.home-mate/nas.token`, chmod 600) so the NAS is never left unauthenticated on LAN; guide me on configuring LLM/ASR/TTS, optional Master Family Agent (`master_brain`), and optional `lan_gateway_exempt` for trusted LAN devices.
```

---

### Track D: Android Universal Terminal (Smart Displays, 86 Panels, Tablets & Old Phones)

Turn any Android 5–16 device (smart display, 4-inch 86 wall panel, tablet, primary phone, or spare old phone) into a Home Mate far-field voice terminal & whole-house controller in 3 minutes with **zero hardware unlocking**:

1. **Choose Your APK** from **[yes999zc/home-mate-gateway-android](https://github.com/yes999zc/home-mate-gateway-android/releases)**:
   - **`full-arm64` (~13 MB)** — Recommended for modern 64-bit phones/tablets (offline KWS included, smallest full package).
   - **`universal` (~21 MB)** — Includes both `arm64-v8a` + `armeabi-v7a` offline KWS (best for 32-bit 86 wall panels, older tablets, or if unsure).
   - **`slim` (~225 KB)** — Ultra-lightweight pure-Java client without offline KWS (for pure remote control / tap-to-talk / text chat).
2. **Connect**: Tap **Scan LAN** (discovers Cores over UDP `:8933`) or add `http://<CORE_IP>:8930` manually, enter your household token (or enable `lan_gateway_exempt` on your Core), and start talking!
3. **Auto-Updates**: Checks **GitHub Releases** by default with ABI-aware APK selection (and also supports custom LAN `version.json` mirrors).

#### Let an AI Coding Agent Set Up or Build the Android Gateway
```text
Help me connect (or build from source) the Home Mate Android Universal Gateway (`https://github.com/yes999zc/home-mate-gateway-android`) against my Home Mate Core at 192.168.1.10:
1. Verify `http://192.168.1.10:8930/api/v0/auth` is reachable, `HM_GATEWAY_ALLOW_LAN=1` is enabled on `:8932`, and UDP `:8933` is open for auto-discovery.
2. Recommend the right APK variant (`full-arm64` for 64-bit phones, `universal` for 32-bit 86 wall panels / older devices, `slim` for lightweight control-only).
3. If building locally from source, run `./tools/test_jvm.sh` and `./tools/build_apk.sh` (using a dedicated release keystore for public distribution, never debug credentials).
```

---

## Acknowledgments

Home Mate stands on the shoulders of many open-source projects and hardware communities. Full license details live in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

- **On-Speaker & Gateway Pipeline**: [idootop/open-xiaoai](https://github.com/idootop/open-xiaoai) & [@coderzc/open-xiaoai](https://github.com/coderzc/open-xiaoai) (MIT), [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) (Apache-2.0), [Microsoft ONNX Runtime](https://github.com/microsoft/onnxruntime) (MIT), [snakers4/silero-vad](https://github.com/snakers4/silero-vad) (MIT), [xiph/speexdsp](https://github.com/xiph/speexdsp) (BSD-3-Clause), [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) (MPL-2.0), Tokio, Axum, Rusqlite, RustCrypto, Vue 3, and Lucide.
- **Community Contributors**: Special thanks to **[@jiantongzh](https://github.com/jiantongzh)** for hardware-validating the 128 MB LX06 batch and inspiring Thin Gateway mode.
- **Architectural Lineage**: [yes999zc/rui](https://github.com/yes999zc/rui), [wilbowes/EchoMuse](https://github.com/wilbowes/EchoMuse), [Rhasspy](https://github.com/rhasspy/rhasspy) / [Wyoming](https://github.com/rhasspy/wyoming), [Home Assistant](https://github.com/home-assistant/core), and [Navidrome](https://github.com/navidrome/navidrome).

---

## License & Contact

- **Open-Source License**: **[GNU AGPL v3.0](LICENSE)** for personal, family, and community self-hosting. The Northbound v2 protocol specification is licensed under **[Apache-2.0](LICENSE-PROTOCOL-APACHE-2.0)**.
- **Official Website**: **[https://mymate.homes](https://mymate.homes)**
- **Contact (Custom Speaker R&D / Commercial OEM Licensing)**: **`zhangcong1985@gmail.com`** / **`yes999zc@163.com`**
