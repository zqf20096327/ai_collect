<div align="center">

<img src="docs/logo.png" alt="DeepSeek API Logo" width="130" />

# DeepSeek API Gateway & AI Agent (DeepSeek 2API)

### Chuyển đổi Web DeepSeek thành OpenAI API chuẩn • Hỗ trợ DeepSeek-V4 & DeepSeek-R1 • Tích hợp Web Dashboard & AI Agent

[![GitHub Stars](https://img.shields.io/github/stars/mitxyultra-cloud/Deepseek-API-AI-Agent?style=flat-square&logo=github)](https://github.com/mitxyultra-cloud/Deepseek-API-AI-Agent)
[![GitHub Forks](https://img.shields.io/github/forks/mitxyultra-cloud/Deepseek-API-AI-Agent?style=flat-square&logo=github)](https://github.com/mitxyultra-cloud/Deepseek-API-AI-Agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI%20Compatible-412991.svg?style=flat-square&logo=openai&logoColor=white)](https://platform.openai.com/docs/api-reference)
[![DeepSeek 2API](https://img.shields.io/badge/DeepSeek-2API-4D6BFE.svg?style=flat-square)](#)

[Khởi đầu nhanh](#-cài-đặt-nhanh) • [Xác thực Extension](#-xác-thực--đăng-nhập-ổn-định-qua-extension) • [Tài liệu API](#-hướng-dẫn-sử-dụng-api) • [Giao diện Dashboard](#-trải-nghiệm-giao-diện-web-ui) • [Từ khóa tìm kiếm](#-từ-khóa-liên-quan-seo)

</div>

---

> **Từ khóa nổi bật / Keywords:** `deepseek api`, `deepseek 2api`, `deepseek2api`, `deepseek to api`, `deepseek openai proxy`, `deepseek r1 api`, `deepseek V4 api`, `free deepseek api`, `deepseek reverse proxy`, `deepseek cookie extension`, `deepseek ai agent`.

---

## 📌 Giới thiệu tổng quan

**DeepSeek-API-AI-Agent** (thường gọi là **DeepSeek 2API**) là giải pháp cầu nối (gateway proxy) mã nguồn mở, biến tài khoản cá nhân trên [chat.deepseek.com](https://chat.deepseek.com) thành **API định dạng chuẩn OpenAI** (`/v1/chat/completions`, `/v1/models`).

Dự án cho phép bạn sử dụng mô hình **DeepSeek-V4** và **DeepSeek-R1 (DeepThink)** trong mọi công cụ, IDE và ứng dụng AI (như NextChat, LobeChat, Chatbox, Cursor, Cline, Open WebUI) mà không cần nạp tiền API key trả phí.

<p align="center">
  <img src="docs/dashboard.png" alt="DeepSeek API Dashboard Overview" width="95%" />
</p>

---

## ✨ Điểm nổi bật & Tính năng cốt lõi

- 🎯 **DeepSeek 2API chuẩn OpenAI**: Tương thích 100% với endpoint OpenAI SDK, curl, LangChain và các phần mềm chat client.
- 🧠 **Hỗ trợ DeepSeek R1 & V4 đầy đủ**: Kèm tư duy chuỗi suy luận (Chain-of-Thought / DeepThink) và Web Search thời gian thực.
- 🧩 **Xác thực Cookie ổn định bằng Extension**: Hỗ trợ trích xuất Token và Cookie 1-click qua tiện ích trình duyệt tại `extensions/cookie-template-extension.crx`, tránh bị chặn Captcha hay Cloudflare.
- 👥 **Quản lý đa tài khoản & Xoay tua (Account Pool)**: Thêm nhiều tài khoản DeepSeek, tự động phân phối tải và cân bằng hạn mức gọi.
- ⚡ **Bypass PoW bằng WebAssembly**: Tích hợp module Wasm (`sha3_wasm_bg.wasm`) giải mã Proof-of-Work siêu tốc nội bộ, phản hồi tức thì.
- 🖥️ **Web Dashboard hiện đại (cổng 20999)**: Cung cấp giao diện trực quan quản lý tài khoản, client API keys, giám sát nhật ký (logs), model và agent skills.
- 🤖 **Hệ thống AI Agent Skills**: Tích hợp các công cụ tự động hóa cục bộ (WebUSB, WebMIDI, custom skills).
- 💻 **Tiện ích IDE đi kèm**: Hỗ trợ mở rộng `extensions/vsk-ide.vsix` cho môi trường phát triển.

---

## 🖼️ Trải nghiệm Giao diện Web UI

Tất cả tính năng quản trị được tích hợp trong Dashboard chạy tại cổng `http://127.0.0.1:20999`:

| Quản lý tài khoản (Multi-Account) | Quản lý API Key người dùng |
| :---: | :---: |
| ![Quản lý tài khoản](docs/accounts.png) | ![Quản lý Client Keys](docs/client-keys.png) |
| **Cấu hình Model & Định tuyến** | **Playground / Creative Console** |
| ![Cấu hình Model](docs/models.png) | ![Creative Console](docs/creative-console.png) |
| **AI Agent Skills** | **Nhật ký truy vấn (Live Logs)** |
| ![AI Agent Skills](docs/skills.png) | ![Nhật ký hệ thống](docs/logs.png) |
| **Cài đặt hệ thống** | **Tài liệu API tương tác** |
| ![Cài đặt hệ thống](docs/settings.png) | ![API Docs](docs/docs.png) |

---

## 📋 Yêu cầu hệ thống

- **Hệ điều hành**: Windows 10/11, macOS, Linux
- **Python**: `>= 3.10`
- **Trình duyệt**: Google Chrome, Microsoft Edge, Brave hoặc Cốc Cốc (hỗ trợ cài file `.crx`)

---

## 🚀 Cài đặt nhanh

### 1. Clone mã nguồn

```bash
git clone https://github.com/mitxyultra-cloud/Deepseek-API-AI-Agent.git
cd Deepseek-API-AI-Agent
```

### 2. Thiết lập môi trường Python

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt trên Windows:
venv\Scripts\activate

# Kích hoạt trên Linux/macOS:
source venv/bin/activate
```

### 3. Cài đặt thư viện phụ thuộc

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Cấu hình file `.env`

Sao chép file mẫu `.env.example`:

```bash
# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

---

## 🔑 Xác thực & Đăng nhập ổn định qua Extension

Để đảm bảo kết nối ổn định không lo timeout hay vướng checkpoint Cloudflare, dự án hỗ trợ 2 phương thức:

### Cách 1: Sử dụng Extension (Khuyên dùng - Ổn định nhất)

1. Cài đặt tiện ích mở rộng có sẵn trong thư mục `extensions/`:
   - Mở trình duyệt Chrome/Edge -> truy cập `chrome://extensions/`.
   - Bật **Developer mode** (Chế độ nhà phát triển) ở góc trên bên phải.
   - Kéo thả file `extensions/cookie-template-extension.crx` vào trình duyệt để cài đặt.
2. Truy cập [chat.deepseek.com](https://chat.deepseek.com) và đăng nhập bình thường.
3. Bấm vào biểu tượng extension trên thanh công cụ để sao chép chuỗi **Cookie & Token**.
4. Khởi động server, truy cập Dashboard tại `http://127.0.0.1:20999/#/accounts` và dán vào mục **Add Account**.

### Cách 2: Tự động qua Playwright CLI

Chạy script tự động mở trình duyệt Chromium:

```bash
python -m deepseek.auth
```

Đăng nhập tài khoản và vượt qua Captcha xác thực. Hệ thống sẽ tự động lưu phiên vào thư mục `session/` để tái sử dụng.

---

## 🖥️ Khởi chạy hệ thống

### Khởi động nhanh (Windows)

Nhấp đúp chuột vào file:

```bat
run.bat
```

Script sẽ tự kiểm tra giải phóng cổng `20999`, kiểm tra bản build giao diện và mở trình duyệt tự động.

### Khởi động bằng dòng lệnh (Tất cả nền tảng)

```bash
python app.py
```

Địa chỉ dịch vụ:
- 🌐 **Web Dashboard**: `http://127.0.0.1:20999`
- 🔌 **OpenAI API Base URL**: `http://127.0.0.1:20999/v1`
- 📑 **Swagger API Docs**: `http://127.0.0.1:20999/api/docs`

---

## 📡 Mô hình hỗ trợ (Models)

| Model ID | Chế độ | Mô tả |
| :--- | :--- | :--- |
| `deepseek-chat` | Default (V4) | Tốc độ cao, trả lời hội thoại tức thời |
| `deepseek-reasoner` | Reasoner (R1) | Suy luận chuyên sâu, hiển thị Chain-of-Thought (`thinking`) |
| `deepseek-expert` | Expert | Chế độ chuyên gia giải quyết bài toán khó |
| `deepseek-4.1-pro` | Custom Routing | Model tùy biến thiết lập trong `models.json` |

---

## 💻 Hướng dẫn sử dụng API

### 1. Gọi qua Python (OpenAI SDK chính thức)

```python
from openai import OpenAI

# Trỏ base_url về cổng DeepSeek API Gateway
client = OpenAI(
    base_url="http://127.0.0.1:20999/v1",
    api_key="unused"  # Không bắt buộc nếu gọi trực tiếp local
)

# 1. Chat thông thường (DeepSeek-V4)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Viết bài thơ ngắn 4 câu về mùa thu."}
    ]
)
print("DeepSeek-V4:", response.choices[0].message.content)

# 2. Suy luận chuyên sâu (DeepSeek-R1) kèm Web Search
r1_response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "user", "content": "So sánh kiến trúc GPU Blackwell và Hopper."}
    ],
    extra_body={
        "thinking": True,  # Bật chế độ suy luận
        "search": True     # Bật tra cứu web trực tiếp
    }
)
print("DeepSeek-R1:", r1_response.choices[0].message.content)
```

### 2. Gọi qua cURL

```bash
curl -X POST http://127.0.0.1:20999/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer unused" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {"role": "user", "content": "Xin chào DeepSeek!"}
    ],
    "stream": false
  }'
```

### 3. Tích hợp ứng dụng bên thứ ba (NextChat, LobeChat, Cursor, Cline...)

- **API Base URL**: `http://127.0.0.1:20999/v1`
- **API Key**: `unused` (hoặc Client Key bạn tạo trong tab Client Keys)
- **Model Name**: `deepseek-chat` hoặc `deepseek-reasoner`

---

## 📂 Cấu trúc dự án

```text
Deepseek-API/
├── app.py                     # Entry point chính khởi động FastAPI Server
├── run.bat                    # Script chạy 1-click tối ưu cho Windows
├── requirements.txt           # Thư viện phụ thuộc Python
├── models.json                # Định nghĩa model tùy chỉnh
├── deepseek/                  # Module lõi kết nối DeepSeek Web
│   ├── auth.py                # Xử lý phiên đăng nhập và Playwright session
│   ├── client.py              # HTTP client gửi dữ liệu chat & stream
│   ├── pow.py                 # Bộ giải thuật PoW (Proof of Work)
│   └── sha3_wasm_bg.wasm      # WebAssembly binary tính toán SHA3
├── server/                    # FastAPI Server & API OpenAI
│   ├── api.py                 # Route chính (/v1/chat/completions, /v1/models)
│   ├── dashboard.py           # API phục vụ Web Dashboard & quản lý Account Pool
│   ├── openai_format.py       # Định dạng tương thích chuẩn OpenAI
│   ├── ratelimit.py           # Kiểm soát tốc độ truy vấn
│   └── tools.py / skills.py   # Thực thi Agent Tool & Skills
├── frontend/                  # Mã nguồn React + Vite + Tailwind Dashboard UI
├── extensions/                # Tiện ích mở rộng (Cookie Extractor & VSK IDE)
│   ├── cookie-template-extension.crx  # Tiện ích lấy Cookie/Token DeepSeek
│   └── vsk-ide.vsix                   # Tiện ích mở rộng IDE
├── examples/                  # Mã nguồn script mẫu đa dạng trường hợp sử dụng
└── docs/                      # Hình ảnh giao diện và tài liệu hướng dẫn
```

---

## 🔍 Từ khóa liên quan (SEO)

Nhằm hỗ trợ tìm kiếm trên GitHub và công cụ tìm kiếm:
- **Tên dự án**: `DeepSeek API`, `DeepSeek 2API`, `DeepSeek-API-AI-Agent`, `deepseek2api`
- **Chức năng**: `deepseek to openai`, `free deepseek r1 api`, `deepseek V4 api free`, `deepseek reverse proxy`, `deepseek proxy gateway`, `deepseek api bridge`, `deepseek web to api`, `deepseek playwright bridge`, `deepseek pow solver wasm`.
- **Ứng dụng tương thích**: `OpenAI SDK`, `NextChat DeepSeek`, `LobeChat DeepSeek`, `Cursor DeepSeek`, `Cline AI Agent`.

---

## ⚠️ Lưu ý & Bảo mật

- **Bảo mật phiên đăng nhập**: Không commit file `session/session.json` hay chia sẻ token cá nhân ra ngoài.
- **Sử dụng hợp lý**: Tránh spam quá nhiều request đồng thời để bảo vệ tài khoản khỏi hạn chế của nền tảng gốc.
- **Mục đích**: Mã nguồn phục vụ mục đích nghiên cứu, học tập và tích hợp công việc cá nhân.

---

## 📄 Giấy phép (License)

Dự án được phân phối theo giấy phép [MIT License](LICENSE). Đóng góp mã nguồn và ý kiến phát triển luôn được hoan nghênh tại [GitHub Repository](https://github.com/mitxyultra-cloud/Deepseek-API-AI-Agent).
