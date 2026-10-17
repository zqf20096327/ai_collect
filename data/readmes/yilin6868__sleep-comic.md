# 睡前漫剧场

把一段睡前中文语音转换为 4–6 格、15–40 秒、1080×1920 的本地竖屏动态漫剧。

当前已完成本地 CLI 单集可恢复纵向切片，正在验证手机 Web 语音输入。正式云模型验收尚未完成；默认只允许 mock 工程链路，不会自动调用云服务或产生费用。

## 已实现范围

- WAV 文件输入和 macOS 麦克风直录。
- 版本化 episode manifest、原子写入、上一版本回退、事件日志和单 worker 锁。
- 固定状态机与失败后恢复。
- faster-whisper、Anthropic、阿里云百炼、Edge TTS、FFmpeg adapter。
- 可离线替代外部 provider 的 `--mock` 端到端链路。
- 4–6 格图片、逐格配音、字幕、轻 BGM、Ken Burns 运镜和 MP4 合成。
- 本地静态 HTML 预览、临时只读测试服务、人工批准和受控删除。
- 手机优先的 Web 录音页，支持 Safari MP4/AAC、Chrome WebM/Opus、试听、重录、文件 fallback 和任务进度轮询。
- 正式前端（`frontend/`）：Next.js 16 + React 19 + TypeScript strict + Tailwind CSS 4，通过 `rewrites` 同源代理后端 `/t/{token}/...`。
- FastAPI `/api/v1` 录音上传和状态接口，媒体由 FFmpeg 归一化为 16kHz 单声道 WAV。

本阶段不含正式生产托管、数据库、多用户、持久分享、合集和自动视觉质检。

## 环境安装

当前项目路径包含中文，setuptools editable 安装在部分 macOS 环境会触发 `.pth` 编码问题，因此使用普通本地安装；测试通过 `pythonpath=src` 直接读取工作区源码。

```bash
cd /Users/Admin/Desktop/睡前漫画
python3.11 -m venv .venv
.venv/bin/python -m pip install '.[dev]'
```

也可使用当前机器上的 uv：

```bash
UV_CACHE_DIR=/private/tmp/sleep-comic-uv-cache \
  /Users/Admin/Desktop/智能客服/.tools/bin/uv pip install \
  --python .venv/bin/python '.[dev]'
```

复制配置示例：

```bash
cp .env.example .env
```

不要把 `.env`、生活音频或生成资产提交到 Git。

## 环境检查

```bash
.venv/bin/python -m sleep_comic doctor
```

检查结果只显示 Key 为 `set` 或 `unset`，不会回显密钥值。

如果 `microphone.input_visible` 在受限执行环境中为 `false`，不一定代表本机没有麦克风；当前机器已在沙箱外确认可枚举“MacBook Air 麦克风”。最终权限只有在用户主动运行 `--record` 时才能验证。

## 先跑 mock 链路

使用麦克风：

```bash
.venv/bin/python -m sleep_comic episode new --record --mock
```

使用已有 WAV：

```bash
.venv/bin/python -m sleep_comic episode new --audio /绝对路径/输入.wav --mock
```

命令默认在录音/复制后启动后台 worker，并返回 episode ID。查看状态：

```bash
.venv/bin/python -m sleep_comic episode status EPISODE_ID
```

如果创建时使用了 `--no-run`，可手动执行：

```bash
.venv/bin/python -m sleep_comic episode run EPISODE_ID --mock
```

失败后恢复：

```bash
.venv/bin/python -m sleep_comic episode resume EPISODE_ID --mock
```

返回预览路径：

```bash
.venv/bin/python -m sleep_comic episode preview EPISODE_ID
```

只有明确需要时才自动打开浏览器：

```bash
.venv/bin/python -m sleep_comic episode preview EPISODE_ID --open
```

启动只读测试预览（默认仅绑定本机 `127.0.0.1:8765`）：

```bash
.venv/bin/python -m sleep_comic episode serve EPISODE_ID
```

命令会生成一个带随机访问令牌的 URL，只允许读取预览 HTML、分镜 PNG 和成片 MP4，不提供目录列表、manifest 或输入音频。该本地服务可通过临时隧道用于手机外网验收；它不是正式部署，终端或隧道进程停止后链接失效。

## 启动手机 Web 录音

使用 mock provider 验证录音、上传、任务和成片链路：

```bash
.venv/bin/sleep-comic web --mock
```

服务默认只绑定 `127.0.0.1:8765`，并输出带随机访问令牌的本机 URL。手机麦克风必须通过 HTTPS 安全上下文访问；把带“录音上传”能力的服务经第三方隧道公开前，必须明确确认语音数据会经过该中继服务。临时隧道只应使用无敏感信息的 mock 测试录音。

真实生产链接仍需要身份认证、对象存储、后台 worker、数据保留/删除策略和云模型验收；当前 `web --mock` 不能冒充正式上线。

人工检查通过后归档：

```bash
.venv/bin/python -m sleep_comic episode approve EPISODE_ID
```

删除必须显式确认：

```bash
.venv/bin/python -m sleep_comic episode delete EPISODE_ID --confirm
```

## 正式前端（Next.js）

正式前端位于 `frontend/`，用 Next.js 16 + React 19 + TypeScript strict + Tailwind CSS 4 实现「录音 → 上传 → 轮询 → 成片」第一条纵向切片。前端只通过同源代理调用后端 API，不重复实现业务逻辑。

启动后端（先）：

```bash
.venv/bin/sleep-comic web --mock
```

再启动前端（另一个终端）：

```bash
cd frontend
npm install          # 若 node_modules 不存在
npm run dev          # 开发，默认 http://localhost:3000
```

访问后端输出链接中的 token，替换到前端路径 `http://localhost:3000/t/{token}`。

前端代理：`next.config.ts` 的 `rewrites` 把 `/t/:token/api/v1/:path*` 和 `/t/:token/episodes/:episodeId/:asset*` 转发到 `BACKEND_URL`（默认 `http://127.0.0.1:8765`）。**注意**：`rewrites` 的目标地址在构建期固化，部署时必须在执行 `npm run build` 时注入 `BACKEND_URL`，运行时环境变量改不到。

公开配置：`NEXT_PUBLIC_MODE_LABEL` 用于页面顶部的运行模式徽标（默认「工程验证」）。

质量门槛：

```bash
cd frontend
npm run lint
npm run typecheck   # tsc --noEmit
npm run test        # vitest 单元/组件测试
npm run test:e2e    # Playwright E2E（自动拉起后端 mock + 前端，复用本机 Chrome）
npm run build       # 生产构建（output: standalone）
```

### 时间线（我的漫画）

录音页右上角「我的漫画」进入 `/t/{token}/timeline`，列出本机全部单集（缩略图、标题、状态、进度、预览链接）。后端新增 `GET /t/{token}/api/v1/episodes` 列表接口。单用户本地应用：token 即本人访问凭证，可查看全部本机单集。

### 真机验收（HTTPS 隧道）

手机麦克风要求 HTTPS 安全上下文。用 localhost.run（无需账号）临时开一个 https 域名：

```bash
# 终端 1：后端
.venv/bin/sleep-comic web --mock --token zhenji-mock-20260828 --port 8765
# 终端 2：前端
cd frontend && npm run dev
# 终端 3：隧道（80 → 前端 3000）
ssh -o StrictHostKeyChecking=accept-new -R 80:localhost:3000 nokey@localhost.run
```

隧道会输出 `https://xxxx.lhr.life` 域名，手机上打开 `https://xxxx.lhr.life/t/zhenji-mock-20260828` 即可验收。**注意**：隧道经第三方中继，语音会先流经它，只应使用无敏感信息的 mock 测试录音；进程结束链接即失效。

生产部署（standalone，与后端分开部署）：

```bash
BACKEND_URL=https://你的后端地址 npm run build
cp -r .next/static .next/standalone/.next/static
cp -r public .next/standalone/public   # 有 public 时
node .next/standalone/server.js        # 默认端口 3000
```

## 真实云调用

推荐方案是“云端最小化出站”：原始音频由本地 faster-whisper 转写；转写文本发往 Anthropic；脱敏后的画面 prompt 发往阿里云百炼；配音文字发往 Edge TTS。它不属于严格本地处理。

真实调用前需要在 `.env` 中填写 Key，并同时显式设置：

```dotenv
CLOUD_CALLS_ENABLED=true
ALLOW_PAID_GENERATION=true
```

这两个开关表示你理解云端调用可能产生费用。未同时开启时，工作流会停止并保留可恢复状态。真实运行不要传 `--mock`。

## 测试

```bash
.venv/bin/python -m pytest
```

mock/集成测试不会调用 Anthropic、阿里云百炼或 Edge TTS。真实模型冒烟需要单独授权、Key 和可用额度，不能用 mock 结果替代。

## 数据目录

```text
data/episodes/{日期}-{episode_id}/
├── manifest.json
├── manifest.previous.json
├── events.jsonl
├── input/
├── transcript/
├── script/
├── panels/
├── audio/
├── subtitles/
├── preview/
└── output/
```

电脑进入系统睡眠时，本地 worker 会暂停；唤醒后如果进程已退出，可使用 `episode resume` 继续。

## 开源许可

本项目采用 [MIT License](LICENSE) 开源。
