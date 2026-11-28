# 明日方舟：终末地 · Baker AI 聊天模拟器

基于《明日方舟：终末地》世界观的 AI 角色聊天项目。一套后端同时服务网页版和客户端：
35 名干员 + 管理员的单聊、多角色群聊、世界书检索、干员记忆、AI 推荐回复、图片消息、SSE 流式输出。

**下载安装包**：[Releases](https://github.com/MCshamrock/endfield-baker-chat/releases)（Windows 安装器 / Android APK，附 SHA-256）。

> **同人作品声明**：本项目是非营利粉丝作品，与上海鹰角网络科技有限公司无关。
> 《明日方舟》《明日方舟：终末地》及其角色、美术、设定版权归原权利人所有。如有侵权请联系删除。
> 代码以 [MIT](LICENSE) 协议开源。

<p align="center">
  <img src="docs/screenshots/01-characters.webp" width="49%" alt="角色列表">
  <img src="docs/screenshots/02-chat.webp" width="49%" alt="单聊界面">
</p>

---

## 仓库里有什么

| 目录 | 是什么 | 技术栈 | 版本 |
|---|---|---|---|
| [`web/back/`](web/back) | 后端：会话 / 消息 / 群聊调度 / 角色提示词 / 世界书检索 / 账号 / 管理接口 / SSE 出话 | Python 3.14 · FastAPI · SQLAlchemy · MySQL 8.4 | 0.1.0 |
| [`web/front/`](web/front) | 网页前端（线上 `chat.peilika.beer` 那一套） | Vue 3 · Vite | 3.2.0 |
| [`web/panel/`](web/panel) | 管理后台：用户 / 角色 / 配置 / 密钥池 / 用量 | Vue 3 · Vite | 0.1.0 |
| [`client/`](client) | Baker AI 4 客户端：一套共享网页层 + Windows 壳（Electron + C# 安装器）+ Android 壳（Capacitor） | Vue 3 · Electron · Capacitor | 4.0.5 |
| [`deploy/`](deploy) | 部署与回滚脚本：后端 / 网页 / MySQL / nginx / systemd | Bash | — |
| [`docs/`](docs) | 设计文档（如 Qwen3TTS 干员配音方案） | Markdown | — |

三块可以独立运行：后端单独跑就能用 HTTP 调试；网页前端只依赖后端；客户端可以走默认后端，
也可以在「自定义 API 模式」下直连任何 OpenAI 兼容端点，完全不需要这个后端。

---

## 快速开始

### 1. 后端 `web/back`

需要 **Python 3.14** 和 **MySQL 8.4**（依赖版本以 `requirements.lock` 为准）。

```bash
cd web/back

# 建虚拟环境并装依赖
pwsh -File scripts/setup_venv.ps1        # Windows
# python3 -m venv .venv && .venv/bin/pip install -r requirements.lock   # Linux/macOS

# 配置：复制样例再改数据库地址
cp .env.example .env

# 建表（schema/001~010）
.venv/Scripts/python.exe scripts/migrate.py      # Linux/macOS: .venv/bin/python

# 起服务（默认 127.0.0.1:5660）
.venv/Scripts/uvicorn.exe app.main:app --port 5660
```

`GET /health` 通即成功。设计文档在 [`web/back/docs/`](web/back/docs)，
本地联调细节见 [`13-本地联调清单.md`](web/back/docs/13-本地联调清单.md)。

### 2. 网页前端 `web/front`

需要 Node 20+。

```bash
cd web/front
npm ci
npm run dev      # http://localhost:5173，/v1、/group 已代理到 5660
npm run build    # 生产构建到 dist/（同源部署，反代 /v1、/group 到后端）
```

### 3. 管理后台 `web/panel`

```bash
cd web/panel
npm ci
npm run dev
```

### 4. 客户端 `client`

需要 Node 20+；安卓另需 JDK 21 + Android SDK 36 + Gradle 8.14.3。

```bash
cd client
npm ci
npm run build          # 产出 dist/，Electron 与 APK 共用

# Windows：Electron 壳 + 安装器
pwsh -File Windows/build.ps1

# Android：同步网页资源后打包
npx cap sync android
pwsh -File Android/build-apk.ps1
```

> 仓库里**不带** APK 签名私钥。要出正式包请自备 keystore，按
> `client/Android/keys/keystore.properties` 的格式填好（该目录已在 `.gitignore` 里）。

---

## 配置与密钥

- 所有后端配置走环境变量，样例见 [`web/back/.env.example`](web/back/.env.example)（全部带 `BAKER_` 前缀）。
- **本仓库不含任何真实凭据**：没有 `.env`、没有数据库口令、没有上游模型 key、
  没有 APK 签名私钥（`*.jks`）、没有服务器私钥。自己部署时请全部换成新生成的。
- 客户端构建期注入的后端地址在 [`client/.env.production`](client/.env.production)，可自行改。

## 部署

`deploy/` 是线上用的那套脚本，作业法是「只读体检 → 备份 → 变更 → 验证 → 回滚」，
用法见 [`deploy/README.md`](deploy/README.md)。脚本假设 systemd + nginx，按自己的环境改路径即可。

## 测试

- 后端：`web/back/tests/`（pytest），`pytest -q`
- 网页 / 客户端：`scripts/*-e2e.mjs`、`scripts/contract-smoke.mjs`（需要后端在跑）

## 致谢

- 客户端设计与早期前端：[NCreeper233](https://github.com/NCreeper233)
- 项目总监 / 维护：[MCshamrock](https://github.com/MCshamrock)
- 以及群里所有报 bug、提需求、帮忙测试的干员们。

## 许可

[MIT](LICENSE)。同人内容（角色、美术、设定）不在此许可范围内。
