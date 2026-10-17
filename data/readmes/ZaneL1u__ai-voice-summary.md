# 🎙️ AI 语音妙记 - 智能会议纪要

基于火山引擎[豆包语音妙记](https://www.volcengine.com/docs/6561/1798094?lang=zh) API 的音频转写工具，支持说话人分离、AI 总结、同步播放。基于 Nuxt 4 构建，完全隐私安全，零配置开箱即用，Serverless 友好~

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Node](https://img.shields.io/badge/node-%3E%3D20-green.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

<img src="https://cdn.zaneliu.me/2026/01/dcRE2W.png" style="zoom:50%;" />
<img src="https://cdn.zaneliu.me/2026/01/3kLfyt.png" style="zoom:50%;" />

## ✨ 特性

- 💾 **本地存储** - Token 存储在 localStorage，任务记录存储在 IndexedDB
- 🔄 **智能轮询** - 自动查询任务状态，页面隐藏时暂停
- 📥 **音频下载** - 原始音频保存在本地，支持随时下载
- 🗣️ **说话人分离** - 支持多人对话场景，可重命名说话人
- 🤖 **AI 总结** - 自动生成会议/音频内容摘要
- 🎵 **歌词式播放** - 播放时自动滚动高亮当前句子
- ✂️ **音频裁剪** - 超长音频自动提示裁剪
- ☁️ **S3 存储** - 可选配置 S3 兼容存储（R2/MinIO 等）

## 🚀 快速开始

### 方式一：Docker 部署（推荐）

#### 使用 Docker Compose

```bash
# 克隆项目
git clone https://github.com/ZaneL1u/ai-voice-summary.git
cd ai-voice-summary

# 启动服务
docker compose up -d

# 访问 http://localhost:3000
```

#### 使用 Docker 命令

```bash
# 构建镜像
docker build -t ai-voice-summary .

# 运行容器
docker run -d -p 3000:3000 --name ai-voice-summary ai-voice-summary

# 访问 http://localhost:3000
```

#### 使用预构建镜像

```bash
docker run -d -p 3000:3000 ghcr.io/ZaneL1u/ai-voice-summary:latest
```

### 方式二：本地开发

#### 1. 安装依赖

```bash
# 需要 Node.js >= 20 和 pnpm
pnpm install
```

#### 2. 启动开发服务器

```bash
pnpm dev
```

#### 3. 配置凭证

1. 访问 <http://localhost:3000/settings>
2. 前往 [火山引擎控制台](https://console.volcengine.com/speech/service/8) 获取 AppId 和 Token
3. 填入并保存

#### 4. 开始使用

1. 回到首页，拖拽或点击上传音频文件
2. 等待转写完成
3. 查看结果、复制文本或下载音频

## 🔧 部署

### Vercel

```bash
# 修改 nuxt.config.ts
nitro: {
  preset: 'vercel'
}

# 部署
vercel
```

### Netlify

```bash
# 修改 nuxt.config.ts
nitro: {
  preset: 'netlify'
}

# 部署
netlify deploy
```

### Cloudflare Pages

```bash
# 修改 nuxt.config.ts
nitro: {
  preset: 'cloudflare-pages'
}
```

### Docker

参见上方 [Docker 部署](#方式一docker-部署推荐) 章节。

## 📁 项目结构

```
├── app/
│   ├── app.vue                    # 根组件
│   ├── assets/css/main.css        # 全局样式
│   ├── components/
│   │   ├── AudioPlayer.vue        # 底部悬浮播放器
│   │   ├── TaskCard.vue           # 任务卡片组件
│   │   ├── TrimDialog.vue         # 音频裁剪弹窗
│   │   └── ui/                    # shadcn-vue 组件
│   ├── composables/
│   │   ├── useAudioPlayer.ts      # 音频播放器状态
│   │   ├── useTokenStorage.ts     # Token 存储 (localStorage)
│   │   ├── useTaskStore.ts        # 任务存储 (IndexedDB)
│   │   ├── usePolling.ts          # 智能轮询
│   │   ├── useS3Storage.ts        # S3 存储
│   │   └── useTranscription.ts    # 转写业务逻辑
│   ├── pages/
│   │   ├── index.vue              # 首页 - 上传
│   │   ├── history.vue            # 历史记录
│   │   └── settings.vue           # 设置页面
│   └── types/
│       └── index.ts               # TypeScript 类型定义
├── server/
│   └── api/
│       ├── transcribe/            # 转写 API
│       └── s3/                    # S3 代理 API
├── Dockerfile
├── docker-compose.yml
├── nuxt.config.ts
└── package.json
```

## 📝 API 说明

### POST /api/transcribe

提交转写任务

**Headers:**

- `x-vc-token`: 火山引擎 Token
- `x-vc-appid`: 火山引擎 AppId

**Body:**

```json
{
  "fileUrl": "https://example.com/audio.mp3"
}
```

**Response:**

```json
{
  "taskId": "xxx",
  "requestId": "xxx"
}
```

### POST /api/transcribe/batch

批量查询任务状态

**Body:**

```json
{
  "taskIds": ["task1", "task2"]
}
```

## ⚙️ 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `NUXT_HOST` | 监听地址 | `0.0.0.0` |
| `NUXT_PORT` | 监听端口 | `3000` |

> 注意：火山引擎凭证在浏览器端配置，不需要服务端环境变量。

## 🔒 隐私说明

- ✅ Token 仅存储在您的浏览器本地
- ✅ 音频文件、历史记录仅存储在您的浏览器 IndexedDB
- ✅ 服务端不保存任何用户数据
- ✅ 音频数据直接发送到火山引擎，服务端仅作代理

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

[MIT](LICENSE)
