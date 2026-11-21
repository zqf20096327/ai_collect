# FlowClone

> 一个**净室（clean-room）复刻** Google Flow 安卓 App 的完整示例：原生 Kotlin/Compose 客户端 + 自建 BFF Server + AI 生成后端接入 + 复刻方法论 skill。
> 仅用于个人学习、交互研究与工程实践，与 Google 无任何关联；仓库不包含原版 App 的代码、素材或品牌资源。

## 能做什么

- 账号：注册/登录、refresh token、游客/设备账号、注销账号（级联删除）
- 生成：图片/视频（经自建 Server 代理 NGSFlow Gateway，Key 不落端）、多份生成、编辑、延长
- 素材：项目/素材/多版本（编辑/延长保留原片）、集合、搜索、回收站、收藏
- 状态：生成进度、失败重试、中断恢复（jobId 持久化）、取消（上游允许时）
- 通知：仅视频任务通知、服务端任务历史、未读数
- 额度：点数账本、图片 0 点 / 视频按分辨率与秒数计费、点数不足提示
- Agent：真实 LLM 代理回复（Grok 文本模型，经 `/v1/agent/chat` 转发）
- 发布：Release APK/AAB 构建、自建服务部署文档、上架材料模板
- 方法论：`skills/bggg-copy-app`（可安装到 DeepSeek Harness）

## 架构

```
┌──────────────────────┐        ┌────────────────────────┐        ┌──────────────────────┐
│ FlowClone Android App│  HTTP  │  flowclone-server (BFF) │  HTTP  │  NGSFlow AI Gateway   │
│ Kotlin / Compose     │──────▶│  Python stdlib + SQLite  │──────▶│  image/video/text     │
│ 账号态 / 生成 / 播放   │ Bearer│  认证/额度/任务/通知/LLM  │ Key   │  模型、任务队列        │
└──────────────────────┘ token  └────────────────────────┘        └──────────────────────┘
```

- App 只连自建 Server；网关 Key 仅保存在服务端环境变量
- 生成任务：submit → 服务端 job 映射 → 轮询 → 输出缓存 → App 下载
- 视频延长：原片 + 续写片段经 Media3 Transformer 统一缩放重编码拼接

## 目录

```
native/                 Android 客户端（Kotlin/Compose，9 个文件约 5.1k 行）
backend/flowclone-server/ 自建 BFF（单文件 Python，无第三方依赖）
skills/bggg-copy-app/   复刻方法论 skill（净室流程/深度标准/踩坑/模板）
docs/                   复盘、部署、隐私政策、数据安全、上架清单
spec/                   UI 规格、差异表、行为审计、路线图
tools/                  ADB 采集脚本（ui.py / cap.sh）
scripts/                构建/启动/ADB 联调脚本
```

## 快速开始

### 1) 启动后端

```bash
cd backend/flowclone-server
cp .env.example .env        # 填 GATEWAY_URL / GATEWAY_KEY / TOKEN_SECRET / ADMIN_TOKEN
cd ../..
./scripts/run-server.sh     # 默认 :8081
```

> `GATEWAY_URL/GATEWAY_KEY` 指向你自己的 AI Gateway（OpenAI 兼容或本项目使用的 NGSFlow 协议）；本仓库不包含任何可用 Key。

### 2) 构建 App

依赖：JDK 17、Android SDK（platform 35、build-tools 35）、Gradle 8.9。

```bash
export JAVA_HOME=/path/to/jdk17
export ANDROID_HOME=/path/to/Android/sdk
cd native
gradle assembleDebug
# APK: native/app/build/outputs/apk/debug/app-debug.apk
```

App 默认服务地址见 `native/gateway.properties.example`（`http://127.0.0.1:8081`）。复制为 `native/gateway.properties` 并按需修改。

### 3) 真机联调

```bash
./scripts/adb-setup.sh          # adb reverse tcp:8081 tcp:8081
adb install -r native/app/build/outputs/apk/debug/app-debug.apk
```

打开 App → 注册或游客模式 → 开始生成。首次使用请在服务端把 `GATEWAY_URL/GATEWAY_KEY` 配好。

## 端到端检查（5 分钟）

1. `curl http://127.0.0.1:8081/health` → `{"ok": true, "gateway": true}`
2. App 注册账号 → 首页应有 100 点
3. 图片生成（0 点）→ 项目出现素材卡
4. 生成视频（480p 8s 约 8 点）→ 完成后可播放
5. 通知页应出现「成功！您的视频…」；账号页点数变化与后端账本一致

## 已知限制

- 原版 Flow 的私有模型（Nano Banana/Omni）与账号风控不可复刻；本项目使用可替换的自有网关
- 虚拟形象实拍仍调系统相机（未实现 App 内自定义相机 UI）
- 本地数据未按账号隔离；商业化缺支付（Play Billing）、FCM 真机推送、HTTPS 域名部署与邮件服务
- 上游内容下载可能很慢（数分钟），已做服务端缓存与客户端重试，但仍取决于网关
- 开源仓库**不包含**原版截图/对比证据（避免第三方版权问题），生成方式见 `docs/evidence.md`

## 发布签名

```bash
keytool -genkeypair -v -keystore native/your-release.jks -alias flowclone \
  -keyalg RSA -keysize 2048 -validity 9125
export RELEASE_KEYSTORE=native/your-release.jks
export RELEASE_STORE_PASSWORD=...
export RELEASE_KEY_ALIAS=flowclone
export RELEASE_KEY_PASSWORD=...
gradle assembleRelease
```

> 正式分发前请使用你自己的 keystore 并妥善备份（丢失将无法更新应用）。

## 文档与复盘

- [docs/replication-retrospective.md](docs/replication-retrospective.md)：完整复盘（时间线、逻辑框架、REA/craft-anything 核查、踩坑、深度标准）
- [docs/development-log.md](docs/development-log.md)：开发逐轮记录
- [spec/](spec/)：UI 规格、逐屏差异表、行为审计、商业化路线
- [skills/bggg-copy-app/](skills/bggg-copy-app/)：可复用复刻方法论 skill（净室流程、深度等级、模板、脚本）
- [docs/store/](docs/store/)：隐私政策、数据安全、审核 SOP、商店素材清单


## 合规与免责声明

- 本项目为**个人学习用途的净室复刻**：仅观察公开可见的界面与行为，不反编译、不抓包破鉴权、不搬运原版代码/素材/品牌
- 与 Google / Flow 无关联，不用于商业分发或冒充官方产品
- 使用本项目接入的第三方 AI 服务时，请遵守对应服务条款与当地法律

## 贡献

欢迎 Issue/PR：问题复现步骤、截图/日志、环境信息。提交前请确认不含任何密钥与真实账号数据。

## License

MIT，见 [LICENSE](LICENSE)。第三方依赖许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
