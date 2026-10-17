# Easy Resume Review

Easy Resume Review（Easy 简历审查）是一套可私有部署的 AI 技术简历审查平台，提供 Web、桌面端和 CLI。它聚焦 AI/LLM 工程岗位，通过七维评分、证据检测、本地 OCR 和两轮模型复核，区分真实项目深度与关键词堆砌、教程式项目、薄弱技术选型和夸大表述。

> The project is designed for recruiter-side screening assistance. It is not a replacement for interviews, reference checks, or human judgment.

## Features

- **GUI + CLI**: Tkinter desktop UI for batch screening and a CLI for one-off reviews.
- **Seven scoring dimensions**: role match, authenticity, project depth, data credibility, education, formality, and cost-performance.
- **Batch projects**: each project stores copied resumes, JSON results, PDF reports, and a Markdown summary under `projects/<name>/`.
- **Resume parsing**: supports text/scanned PDF, PNG, JPG, WebP, BMP, TIFF, TXT, and MD.
- **Local OCR**: Tesseract-based Chinese/English OCR with image preprocessing; no vision-model dependency.
- **PDF reports**: generates per-candidate PDF reports with scores, red flags, highlights, and hiring suggestions.
- **Heuristic evidence brief**: deterministic detectors report objective counts to the LLM, reducing over-trust in polished wording.
- **LLM provider agnostic**: uses the OpenAI Python SDK and supports OpenAI-compatible endpoints.
- **招聘漏斗**：按租户和招聘计划隔离候选人，自动恢复中断的简历审查，并向全部有效邮箱幂等发送 Agent 作业；录取名额只用于最终审批统计。
- **录用名额控制**：候选人作业通过后通知招聘负责人，只有负责人确认录用才原子扣减剩余名额，名额归零后停止发送。
- **微信客服简历入口**：可接收已绑定微信客服账号中的文件消息并下载临时素材；不扫描企业成员的私聊或任意会话。

## What It Checks

ResumeProbe combines LLM review with code-level evidence detectors:

- Skill stuffing and skill-to-project corroboration gaps
- Real-work fingerprints: parameters, trade-offs, meaningful metrics, diverse duties, diverse stacks
- Low information density and template-like writing
- AI/RAG/fine-tuning/Agent depth signals
- Pure API wrapping patterns
- Weak model dependency in core high-stakes tasks
- Buzzword inflation: excessive frontier terms used to mask shallow implementation
- Technology anachronisms, such as claiming a project used a framework before its public release
- Project timeline and work-history consistency, focusing on project feasibility rather than student/worker identity labels

## Installation

```bash
git clone https://github.com/redmaplewww/easy-resume-review.git
cd easy-resume-review
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and fill your own API key:

```ini
LLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4
LLM_API_KEY=your_api_key_here
LLM_MODEL=GLM-5
LLM_VISION_MODEL=GLM-5
LLM_TIMEOUT=180
```

No API key is committed to this repository. The GUI also lets you enter and persist configuration locally in `~/.resume_agent/config.json`.

## Run

### GUI

```bash
python gui.py
```

### CLI

```bash
python cli.py
python cli.py path/to/resume.pdf
```

### Web 工作台

```bash
pip install -r requirements.txt
uvicorn web_app:app --host 0.0.0.0 --port 8000
```

浏览器访问 `http://localhost:8000`。Web 版支持多文件上传、后台审查进度、
历史任务、候选人详情与 PDF 报告下载。任务和报告默认保存在 `web_data/`。

图片和扫描版 PDF 需要系统安装 Tesseract 及中英文语言包。Ubuntu/Debian：

```bash
sudo apt install tesseract-ocr tesseract-ocr-chi-sim tesseract-ocr-eng
```

### Docker 部署

先按上文配置 `.env`，然后运行：

```bash
docker compose up -d --build
```

服务监听 `8000` 端口，审查数据保存在 Docker 命名卷 `resumeprobe-data`。
Web 版提供站内注册和登录，密码以 PBKDF2 加盐哈希保存，任务和报告按账号隔离。
公网部署应配置 Nginx/Caddy HTTPS 反向代理，并在 `.env` 中设置
`WEB_COOKIE_SECURE=1`。保持 Uvicorn 单进程；Web 任务状态当前保存在进程内并同步
落盘，多进程会产生不一致。

招聘控制台位于 `/recruitment/admin`。设置 `RECRUIT_ADMIN_TOKEN` 后，先创建招聘计划并填写
待招聘人数、通知邮箱和岗位要求，再导入简历或绑定 `open_kfid`。简历统一完成批量审查后，
系统只给当前排名前五的候选人发送测试邮件。完整状态和正式接入边界见
[`docs/RECRUITMENT_FUNNEL.md`](docs/RECRUITMENT_FUNNEL.md)。

### Linux systemd 部署

对于未安装 Docker 的服务器，可将运行代码部署到 `/opt/resumeprobe`，创建虚拟环境并
安装依赖，然后把 `deploy/resumeprobe.service` 安装到 `/etc/systemd/system/`：

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now resumeprobe
sudo systemctl status resumeprobe
```

服务默认监听 `8765` 端口，生产环境仍建议通过 HTTPS 反向代理访问。

## Build Windows EXE

```bash
pip install pyinstaller
pyinstaller ResumeReviewAgent.spec
```

The built executable is generated under `dist/ResumeReviewAgent/`.

## Repository Layout

```text
agent/
  analyzer.py      # deterministic resume evidence detectors
  config.py        # prompts and scoring dimension definitions
  inspector.py     # LLM review orchestration + evidence brief
  llm.py           # OpenAI-compatible API wrapper
  parser.py        # PDF/TXT/MD parsing and extraction noise handling
  report.py        # PDF report generation
  scorer.py        # final score synthesis
  storage.py       # local config/result persistence
gui.py             # Tkinter desktop app
cli.py             # interactive CLI
review_imported_resumes.py  # batch-review script
qq_import_recent.py          # optional mailbox import helper
ResumeReviewAgent.spec       # PyInstaller spec
docs/             # usage and design documentation
recruitment/      # LangGraph candidate interview and handoff workflow
config/           # editable interview question banks and policies
```

The candidate interview MVP is documented in `docs/INTERVIEW_WORKFLOW.md`. Its committed
configuration is simulation-only; real Enterprise WeChat delivery is not enabled.

## Privacy and Security

- Do **not** commit `.env`, resume PDFs, generated reports, or review result JSON.
- The default `.gitignore` excludes resumes, logs, output directories, build artifacts, and local configuration.
- If you use mailbox import helpers, review all downloaded files before sharing or committing anything.

## Limitations

- The tool reviews claims in resumes; it cannot prove truth without interviews or external verification.
- Heuristic detectors may produce false positives/negatives and are intentionally treated as evidence, not hard verdicts.
- Model behavior depends on the configured LLM and prompt-following quality.

## License

MIT. See `LICENSE`.
