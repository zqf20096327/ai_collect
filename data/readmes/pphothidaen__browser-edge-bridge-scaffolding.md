# Browser Edge Bridge Scaffolding

<div align="center">

[![Cloudflare Workers](https://img.shields.io/badge/Cloudflare-Workers%20Durable%20Objects-F38020?logo=cloudflare&logoColor=white)](https://workers.cloudflare.com/)
[![Browser Extension](https://img.shields.io/badge/Browser-Extension%20MV3-4285F4?logo=googlechrome&logoColor=white)](https://developer.chrome.com/docs/extensions/)
[![MCP Protocol](https://img.shields.io/badge/MCP-JSON--RPC%202.0-8A2BE2)](https://modelcontextprotocol.io/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI%20Compatible-412991?logo=openai&logoColor=white)](https://platform.openai.com/docs/api-reference)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**A generic, domain-neutral scaffolding for bridging authenticated browser sessions into OpenAI-compatible REST APIs and Remote Model Context Protocol (MCP) servers on Cloudflare Workers and Durable Objects.**

**โครงสร้างตั้งต้น (Scaffolding) แบบเป็นกลาง ไม่ผูกติดผู้ให้บริการ สำหรับเชื่อม Browser Session ที่ล็อกอินอยู่แล้วให้กลายเป็น OpenAI-Compatible REST API และ Remote Model Context Protocol (MCP) Server บน Cloudflare Workers และ Durable Objects**

[Overview / ภาพรวม](#overview--ภาพรวม) · [Architecture / สถาปัตยกรรม](#architecture--สถาปัตยกรรม) · [Popup UI (`popup.html`)](#browser-extension-ui-popuphtml--หน้าจอส่วนขยายเบราว์เซอร์) · [Quickstart / เริ่มต้นใช้งาน](#quickstart--เริ่มต้นใช้งานอย่างรวดเร็ว) · [Appendix & Docs / ภาคผนวก](#appendix--ภาคผนวกและเอกสารที่เกี่ยวข้อง) · [Legal Notice / ประกาศทางกฎหมาย](LEGAL_NOTICE.md)

</div>

---

## Overview / ภาพรวม

**English:**
**Browser Edge Bridge Scaffolding** provides a production-ready template to expose authenticated browser sessions through standard AI developer interfaces:
1. **OpenAI-Compatible REST API** with Server-Sent Events (SSE) streaming (`POST /v1/chat/completions`, `GET /v1/models`).
2. **Remote MCP Server** over JSON-RPC 2.0 (`POST /mcp`) supporting standard tool discovery and execution.
3. **Stateful Edge Orchestration** powered by Cloudflare Durable Objects (`ExtHub`) with a serialized FIFO job queue, backpressure handling, and per-job timeouts.
4. **Zero Upstream Credential Leakage** — user credentials stay exclusively inside the user's browser runtime. Upstream tokens and cookies are never stored on or transmitted to the edge worker.

**คำอธิบาย (TH):**
**Browser Edge Bridge Scaffolding** เป็นเทมเพลตพร้อมนำไปใช้งานจริงสำหรับต่อยอดระบบที่ต้องการเรียกใช้โมเดลผ่านเซสชันเบราว์เซอร์ด้วยมาตรฐานสากล:
1. **OpenAI-Compatible REST API** รองรับการสตรีมแบบ Server-Sent Events (SSE) (`POST /v1/chat/completions`, `GET /v1/models`)
2. **Remote MCP Server** ผ่าน JSON-RPC 2.0 (`POST /mcp`) รองรับการค้นหาและเรียกใช้งาน Tool ตามมาตรฐาน
3. **Stateful Edge Orchestration** ด้วย Cloudflare Durable Objects (`ExtHub`) ที่มีคิวงานแบบ FIFO, ระบบป้องกันคิวล้น (Backpressure) และกำหนด Timeout แยกตามประเภทงาน
4. **ไม่รั่วไหลข้อมูลประจำตัวต้นทาง (Zero Upstream Credential Leakage)** — คุกกี้และเซสชันการล็อกอินของผู้ใช้จะอยู่ภายในเบราว์เซอร์ของผู้ใช้เท่านั้น ไม่ถูกจัดเก็บหรือส่งไปยัง Edge Worker

---

## Architecture / สถาปัตยกรรม

**English:** Requests flow from AI clients through the Cloudflare Worker Edge Gateway into the singleton Durable Object (`ExtHub`), which dispatches jobs over SSE to the Manifest V3 browser extension and executes them inside the user's active browser tab.

**คำอธิบาย (TH):** คำขอจากไคลเอนต์ AI จะวิ่งผ่าน Cloudflare Worker Edge Gateway เข้าสู่ Durable Object (`ExtHub`) ซึ่งส่งงานผ่าน SSE ไปยังส่วนขยายเบราว์เซอร์ (Manifest V3) เพื่อประมวลผลภายในแท็บเบราว์เซอร์ที่ล็อกอินอยู่จริงโดยไม่ต้องดึงคุกกี้ออกนอกเครื่อง

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   AI Clients Tier                                      │
│                  AI Agents · IDE Extensions · OpenAI SDKs · MCP Clients                │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ HTTPS (Bearer Auth: CLIENT_API_KEY)
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           Cloudflare Worker Edge Gateway                               │
│                                                                                        │
│   ┌────────────────────────────────────────────────────────────────────────────────┐   │
│   │                          Edge Middleware & Security                            │   │
│   │   • Dual-role token auth (BRIDGE_SECRET / CLIENT_API_KEY)                      │   │
│   │   • Fail-closed error handling (503 disconnected, 422 unverified, 429 full)   │   │
│   │   • Timing-safe secret verification and CORS preflight                         │   │
│   └──────┬────────────────────────┬────────────────────────┬───────────────────────┘   │
│          │                        │                        │                           │
│          ▼                        ▼                        ▼                           │
│   ┌──────────────┐         ┌──────────────┐         ┌──────────────┐                   │
│   │ OpenAI REST  │         │  Remote MCP  │         │  Status API  │                   │
│   │ /v1/*        │         │  /mcp        │         │  /status     │                   │
│   └──────┬───────┘         └──────┬───────┘         └──────┬───────┘                   │
│          │                        │                        │                           │
│          └────────────────────────┼────────────────────────┘                           │
│                                   ▼                                                    │
│   ┌────────────────────────────────────────────────────────────────────────────────┐   │
│   │                     ExtHub (Durable Object Singleton)                          │   │
│   │   • Global Singleton (`idFromName("singleton")`)                               │   │
│   │   • FIFO Queue (Depth 10, configurable per-kind timeouts)                      │   │
│   │   • Real-time SSE Chunk streaming (/ext/chunk -> SSE stream)                   │   │
│   │   • Dynamic model catalog registry & runtime config reload                     │   │
│   └───────────────────────────────┬────────────────────────────────────────────────┘   │
│                                   │ SSE Push (GET /ext/events, auth: BRIDGE_SECRET)    │
│                                   ▼                                                    │
│   ┌────────────────────────────────────────────────────────────────────────────────┐   │
│   │                     Browser Extension (Manifest V3)                            │   │
│   │   • background.js: SSE consumer, job dispatcher, multi-provider routing        │   │
│   │   • offscreen.js / page.js: Target DOM and API bridge adapter                  │   │
│   │   • popup: Connection status, model listing, and endpoint configuration        │   │
│   └───────────────────────────────┬────────────────────────────────────────────────┘   │
└───────────────────────────────────┼────────────────────────────────────────────────────┘
                                    │ chrome.tabs / postMessage relay
                                    ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Authenticated Browser Tab Session                               │
│   • Target session runtime (e.g. https://target.example.local)                         │
│   • Executes model queries directly in browser context with active credentials         │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Browser Extension UI (`popup.html`) / หน้าจอส่วนขยายเบราว์เซอร์

**English:** The Manifest V3 extension ships with a lightweight popup dashboard ([`packages/core/browser-bridge/extension/popup.html`](packages/core/browser-bridge/extension/popup.html)) for monitoring bridge connectivity, managing isolated primary/secondary target browser tabs, selecting default models, and configuring the Worker URL and token at runtime.

**คำอธิบาย (TH):** ส่วนขยาย Manifest V3 มาพร้อมหน้าป็อปอัป ([`packages/core/browser-bridge/extension/popup.html`](packages/core/browser-bridge/extension/popup.html)) สำหรับดูสถานะการเชื่อมต่อ Bridge, จัดการแท็บปลายทางแบบแยก Primary/Secondary, เลือกโมเดลเริ่มต้น (Default Model), ดูโควตาคงเหลือ และตั้งค่า Worker URL / Bridge Token ได้ทันทีขณะใช้งาน

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <img src="docs/assets/chrome-extension-popup.png" alt="Browser Edge Bridge Popup — Connected Overview" width="340" />
      <br />
      <sub><strong>Connected Overview / ภาพรวมเมื่อเชื่อมต่อแล้ว</strong><br/>Bridge status, multi-provider tab connections, filterable usable models, default model picker, and credit meter.<br/>แสดงสถานะ Bridge, แท็บผู้ให้บริการ, รายชื่อโมเดลพร้อมตัวกรอง, การตั้งค่า Default Model และแถบโควตา</sub>
    </td>
    <td align="center" valign="top" width="50%">
      <img src="docs/assets/chrome-extension-popup-advanced.png" alt="Browser Edge Bridge Popup — Advanced Settings" width="340" />
      <br />
      <sub><strong>Advanced Settings / การตั้งค่าขั้นสูง</strong><br/>Runtime Worker URL and optional Bridge Token override with one-click reconnect and model refresh.<br/>กำหนด Worker URL และ Bridge Token ช่วง runtime พร้อมปุ่มเชื่อมต่อใหม่และรีเฟรชรายชื่อโมเดล</sub>
    </td>
  </tr>
</table>

---

## Features / ความสามารถหลัก

- **Standard REST Endpoints / เอ็นด์พอยต์มาตรฐาน OpenAI**:
  - `GET /v1/models` — Returns discovered and configured models. / คืนรายชื่อโมเดลที่ตรวจพบและตั้งค่าไว้
  - `POST /v1/chat/completions` — OpenAI-compatible completions with SSE streaming & JSON responses. / รับส่งข้อความตามมาตรฐาน OpenAI รองรับทั้ง Streaming (SSE) และ JSON ปกติ
  - `GET /status` & `GET /health` — Health check returning hub status, extension count, and active default model. / ตรวจสถานะ Hub, จำนวนส่วนขยายที่เชื่อมต่อ และโมเดลเริ่มต้น
  - `POST /config` — Dynamically update default model and runtime options. / อัปเดต Default Model และค่าการทำงานแบบไดนามิก
- **Remote MCP Tools (`POST /mcp`) / เครื่องมือ MCP ระยะไกล**:
  - `bridge_chat` — Dispatches prompts (with optional attachments) through the active browser session. / ส่งคำสั่ง Prompt พร้อมไฟล์แนบผ่านเซสชันเบราว์เซอร์
  - `bridge_list_models` — Returns the live model catalog from the browser session. / ดึงรายการโมเดลจริงจากเบราว์เซอร์
  - `bridge_status` — Returns hub connectivity, extension status, and queue depth. / ตรวจสถานะการเชื่อมต่อและจำนวนงานในคิว
  - `web_search` & `summarize` — Web search with source citations and text summarization. / ค้นหาข้อมูลพร้อมแหล่งอ้างอิงและสรุปข้อความผ่านเซสชัน
- **Fail-Closed Protection / ระบบป้องกันแบบ Fail-Closed**:
  - `503 extension_disconnected` — No active browser tab connected. / ไม่มีแท็บเบราว์เซอร์เชื่อมต่ออยู่
  - `503 secrets_unconfigured` — Missing Worker secrets (`BRIDGE_SECRET` / `CLIENT_API_KEY`). / ยังไม่ได้ตั้งค่า Secret บน Worker
  - `429 queue_full` — Concurrent requests exceed queue capacity. / คำขอเกินขีดจำกัดคิว
  - `422 model_unverified` — Unknown or unverified model ID. / ชื่อโมเดลไม่อยู่ในแคตตาล็อกที่ยืนยันแล้ว
- **Multi-Provider Session Isolation / แยกเซสชันหลายผู้ให้บริการ**:
  - Routes distinct model IDs to isolated browser tabs (Primary & Secondary providers). / แยกเส้นทางโมเดลแต่ละกลุ่มไปยังแท็บเบราว์เซอร์คนละแท็บอย่างอิสระ

---

## Quickstart / เริ่มต้นใช้งานอย่างรวดเร็ว

### 1. Deploy the Edge Worker / ติดตั้ง Cloudflare Edge Worker

```bash
git clone https://github.com/example/browser-edge-bridge-scaffolding.git
cd browser-edge-bridge-scaffolding
npm install
cd cloudflare
npx wrangler deploy
```

Configure required Worker secrets / ตั้งค่า Secret ที่จำเป็นบน Worker:

```bash
npx wrangler secret put BRIDGE_SECRET    # Token for browser extension channel / Token สำหรับส่วนขยายเบราว์เซอร์
npx wrangler secret put CLIENT_API_KEY   # Token for API and MCP clients / Token สำหรับไคลเอนต์ API และ MCP
```

### 2. Configure & Load the Browser Extension / ตั้งค่าและโหลดส่วนขยายเบราว์เซอร์

**English:**
1. Copy and customize [`bridge.config.example.json`](bridge.config.example.json) (target origins, provider prefixes, queue limits) and [`.env.example`](.env.example) (`BRIDGE_SECRET`, `CLIENT_API_KEY`, `BRIDGE_URL`, `TARGET_ORIGIN`).
2. Open `chrome://extensions/` in any Chromium-based browser and enable **Developer mode**.
3. Click **Load unpacked** and select `release/chrome-extension` (or build a local token-injected bundle with `BRIDGE_AUTH_TOKEN=<token> python3 scripts/build-extension.py --output release/browser-bridge-chrome-built`).
4. Open the extension popup, expand **Advanced**, set the Worker URL (`https://bridge.example.workers.dev`), and enter `BRIDGE_SECRET` if not injected at build time.
5. Open an active session tab on your target application (e.g. `https://target.example.local`).

**ขั้นตอน (TH):**
1. คัดลอกไฟล์เทมเพลต [`bridge.config.example.json`](bridge.config.example.json) และ [`.env.example`](.env.example) แล้วปรับ Origin ปลายทาง, โมเดล และค่า Secret ให้ตรงกับระบบของคุณ
2. เปิดหน้า `chrome://extensions/` บนเบราว์เซอร์ตระกูล Chromium แล้วเปิด **Developer mode**
3. กด **Load unpacked** และเลือกโฟลเดอร์ `release/chrome-extension` (หรือสร้างชุดฝัง Token เฉพาะเครื่องผ่าน `scripts/build-extension.py`)
4. เปิดหน้าป็อปอัปของส่วนขยาย กดขยายหัวข้อ **Advanced** ใส่ Worker URL (`https://bridge.example.workers.dev`) และระบุ `BRIDGE_SECRET`
5. เปิดแท็บเว็บปลายทางที่ล็อกอินเรียบร้อยแล้ว (เช่น `https://target.example.local`)

### 3. Verify Deployment & Package Release / ตรวจสอบหลัง Deploy และสร้างแพ็กเกจ Release

```bash
# Run read-only verification against a local (`wrangler dev`) or deployed Worker
# ตรวจสอบ endpoint แบบ read-only ทั้ง local หรือ Worker จริง (ไม่แก้ไข state)
node scripts/verify_deploy.mjs --url https://bridge.example.workers.dev

# Package and validate Chrome extension load-unpacked directory and credential-free (.zip) release artifact
# สร้างและตรวจสอบความสมบูรณ์ของแพ็กเกจส่วนขยาย Chrome (load-unpacked และไฟล์ .zip)
npm run release
```

### 4. Usage Examples / ตัวอย่างการเรียกใช้งาน

#### cURL (OpenAI Chat Completions)

```bash
curl -X POST https://bridge.example.workers.dev/v1/chat/completions \
  -H "Authorization: Bearer <your-client-api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "model-example",
    "messages": [{"role": "user", "content": "Hello via browser edge bridge"}],
    "stream": true
  }'
```

#### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://bridge.example.workers.dev/v1",
    api_key="<your-client-api-key>",
)

response = client.chat.completions.create(
    model="model-example",
    messages=[{"role": "user", "content": "Explain edge workers and durable objects"}],
    stream=True,
)

for chunk in response:
    print(chunk.choices[0].delta.content or "", end="")
```

#### Remote MCP Client Configuration

```json
{
  "mcpServers": {
    "browser-edge-bridge": {
      "url": "https://bridge.example.workers.dev/mcp",
      "headers": {
        "Authorization": "Bearer <your-client-api-key>"
      }
    }
  }
}
```

---

## Testing & Verification / การทดสอบและตรวจสอบความปลอดภัย

**English:** All tests cover Worker unit & coverage gates, config loader precedence, read-only deploy verification, release packaging, adversarial chaos tests (`RED-1`–`RED-5b`), SSRF defense, and Python suites.

**คำอธิบาย (TH):** ชุดทดสอบครอบคลุม Worker + Coverage Gate, การโหลดคอนฟิก, สคริปต์ตรวจหลัง deploy, การแพ็กเกจ Release, ชุดทดสอบโจมตี Adversarial Chaos (`RED-1`–`RED-5b`), การป้องกัน SSRF และชุดทดสอบ Python:

```bash
# Root test suite (Worker, Config Loader, Verify Deploy, Release Packaging)
npm test

# Core bridge tests, adversarial chaos suites (RED-1..RED-5b), and SSRF defense
npm run test:core

# Python unit & CI gate configuration tests
python3 -m unittest discover -s . -p "test_*.py"
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## Appendix / ภาคผนวกและเอกสารที่เกี่ยวข้อง

### Appendix A: Documentation Cross-Reference Map / แผนผังเอกสารที่เชื่อมโยงกัน

| Document / เอกสาร | Scope (EN) | ขอบเขตเนื้อหา (TH) |
|---|---|---|
| [`docs/API-SPEC.md`](docs/API-SPEC.md) | OpenAI REST (`/v1/*`), Remote MCP (`/mcp`), and Hub⇄Extension SSE protocol | ข้อกำหนด OpenAI REST, Remote MCP JSON-RPC และโปรโตคอล Hub⇄Extension |
| [`docs/CONFIGURATION.md`](docs/CONFIGURATION.md) | Configuration precedence (Doppler → Cloudflare → `.env` → defaults) & variables | ลำดับความสำคัญของการโหลดค่าตั้งต้นและตารางตัวแปรสภาพแวดล้อม |
| [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) | Architecture guidelines, test suites, and adding custom provider adapters | แนวทางการพัฒนา, การรันชุดทดสอบ และการเพิ่ม Provider Adapter ใหม่ |
| [`docs/RELEASE.md`](docs/RELEASE.md) | Reproducible credential-free Chrome extension & ZIP build and validation | ขั้นตอนสร้างและตรวจสอบความสมบูรณ์ของแพ็กเกจ Chrome Extension และไฟล์ ZIP |
| [`GUARDRAILS.md`](GUARDRAILS.md) | 5 architectural security & TDD guardrails (G0–G5, Zero-Token-Leak) | กฎเหล็กด้านความปลอดภัย 5 เสาหลัก (G0–G5, Zero-Token-Leak, Blue/Red Team) |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Definition of Done (DoD), agent labeling, Git hooks, and CI/CD gates | เกณฑ์ปิดงาน (DoD), การกำกับดูแล Git hooks และ CI/CD 4 ด่าน |
| [`plan.md`](plan.md) | High-level scaffolding architecture and component blueprint | แผนสถาปัตยกรรมภาพรวมของโครงสร้าง Scaffolding |
| [`HANDOFF.md`](HANDOFF.md) | Current release state (`v1.0.0`), verified test counts, and artifact inventory | สถานะ Release ล่าสุด (`v1.0.0`), ผลการทดสอบ และรายการ Artifacts |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history and release notes (`v1.0.0`) | บันทึกการเปลี่ยนแปลงรายเวอร์ชัน |
| [`LEGAL_NOTICE.md`](LEGAL_NOTICE.md) | Binding legal disclaimer, non-affiliation notice, and downstream developer severability | ประกาศทางกฎหมาย การปฏิเสธความเกี่ยวข้อง และการตัดขาดความรับผิดชอบจากการนำไปพัฒนาต่อ |
| [`packages/core/README.md`](packages/core/README.md) | Core workspace overview and local server structure | คู่มือแพ็กเกจ Core และโครงสร้าง local server |
| [`packages/core/browser-bridge/README.md`](packages/core/browser-bridge/README.md) | Zero-dependency Node bridge, CLI, and Chromium extension setup | คู่มือ Node bridge, CLI และการติดตั้งส่วนขยายเบราว์เซอร์ |
| [`packages/SECRETARY_README.md`](packages/SECRETARY_README.md) | Middle gateway / secretary CLI wrapper overview | คู่มือสรุปคำสั่ง Middle Gateway / Secretary CLI |

### Appendix B: Fail-Closed HTTP Error Reference / ตารางรหัส Error มาตรฐาน

| HTTP Status | Error Code | Meaning (EN) | ความหมาย (TH) |
|---|---|---|---|
| `401` | `invalid_api_key` | Missing or invalid Bearer / `x-bridge-token` | ไม่ได้ส่ง Token หรือ Token ไม่ถูกต้อง |
| `422` | `model_unverified` | Model ID is not present in verified catalog | ชื่อโมเดลไม่อยู่ในแคตตาล็อกที่ยืนยันแล้ว |
| `429` | `queue_full` | Pending FIFO queue depth exceeded (`QUEUE_MAX_SIZE`) | คำขอสะสมในคิวเกินขีดจำกัดที่กำหนด |
| `503` | `secrets_unconfigured` | Worker lacks both `BRIDGE_SECRET` and `CLIENT_API_KEY` | Worker ยังไม่ได้ตั้งค่า Secret ที่จำเป็น |
| `503` | `extension_disconnected` | No browser extension or target tab is connected | ไม่มีส่วนขยายหรือแท็บเบราว์เซอร์เชื่อมต่ออยู่ |

### Appendix C: Scaffolding Templates & Release Artifacts / ไฟล์ตั้งต้นและชุดส่งมอบ

- **Config Templates / เทมเพลตตั้งค่า**: [`bridge.config.example.json`](bridge.config.example.json), [`.env.example`](.env.example), [`cloudflare/wrangler.toml`](cloudflare/wrangler.toml)
- **Shipped Artifacts (`v1.0.0`) / ไฟล์แพ็กเกจพร้อมใช้งาน**:
  - `release/chrome-extension/` (Load unpacked — byte-identical with `packages/core/browser-bridge/extension/`)
  - `release/browser-edge-bridge-chrome-v1.0.0.zip` (Credential-free Chrome archive)

---

## Legal Notice & Disclaimer / ประกาศทางกฎหมายและการจำกัดความรับผิด

**English:**  
This project is an independent open-source scaffolding for educational and software architecture research. It is **NOT affiliated with, sponsored by, or endorsed by** any government entity (including the Ministry of Digital Economy and Society, ONDE, or the `aipass.go.th` project) nor any commercial AI provider. The original authors disclaim all liability for any downstream modifications, third-party implementations, or unlawful usage by downstream developers. Read the full binding declaration in [`LEGAL_NOTICE.md`](LEGAL_NOTICE.md).

**คำอธิบาย (TH):**  
โครงการนี้เป็นโครงสร้างตั้งต้น (Scaffolding) ซอฟต์แวร์โอเพนซอร์สอิสระเพื่อการศึกษาและการวิจัยทางวิศวกรรมซอฟต์แวร์ **ไม่มีความเกี่ยวข้อง ไม่ได้รับการสนับสนุน และไม่มีส่วนผูกพันใด ๆ** กับหน่วยงานภาครัฐ (รวมถึงกระทรวงดิจิทัลเพื่อเศรษฐกิจและสังคม, สดช., หรือโครงการ `aipass.go.th`) หรือผู้ให้บริการเชิงพาณิชย์ใด ๆ ผู้พัฒนาต้นฉบับขอตัดขาดความรับผิดชอบโดยสิ้นเชิงต่อการกระทำ การดัดแปลง หรือการนำไปใช้งานที่ผิดกฎหมายของบุคคลภายนอก โปรดอ่านข้อกำหนดฉบับเต็มใน [`LEGAL_NOTICE.md`](LEGAL_NOTICE.md)

---

## License / สัญญาอนุญาต

MIT License — Released as an open-source scaffolding template. / เผยแพร่ภายใต้ **MIT License** เป็นเทมเพลตโอเพนซอร์สสำหรับนำไปพัฒนาต่อ ดูรายละเอียดใน [`LICENSE`](LICENSE).
