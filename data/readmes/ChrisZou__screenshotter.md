# AutoScreenshot

一个自动截屏 + AI 分析的 macOS 工具。每隔几秒截取屏幕，调用 AI 视觉模型生成一句话描述你正在做什么（如「在编写代码」「在浏览网页」），记录到本地数据库，可选同步到自部署的服务器。

## 工作原理

```
截屏 → AI 分析（Kimi / Seed 2.0 Lite） → 本地 SQLite 存储 → （可选）同步到服务器
```

- 截图在 AI 分析完成 60 秒后自动删除，只保留文字描述
- 锁屏时自动记录「锁屏」状态，不截图
- 服务器只接收元数据，不接收图片

## 系统要求

- macOS 13.0+
- Swift 5.9+（构建客户端）
- Go 1.21+（构建服务器，可选）
- Docker（部署服务器，可选）

## 快速开始

### 1. 构建并运行客户端

```bash
cd macos_app
swift build -c release
./build.sh   # 生成 .app 和 .dmg
```

或直接开发模式运行：

```bash
cd macos_app
swift run
```

首次运行需要授予 **屏幕录制** 权限：系统设置 → 隐私与安全 → 屏幕录制 → 启用 AutoScreenshot。

### 2. 配置 AI 模型

打开应用设置，选择 AI 提供商并填入 API Key：

| 提供商 | 获取 API Key |
|--------|-------------|
| Kimi（Moonshot） | https://platform.moonshot.cn/console/api-keys |
| Seed 2.0 Lite（火山方舟） | https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey |

配置完成后点击「开始截屏」即可。

### 3. 部署服务器（可选）

如果你希望将活动记录同步到远程服务器：

```bash
cd screenshot-server

# 方式一：Docker Compose（推荐）
docker-compose up -d

# 方式二：直接运行
go run main.go
```

服务器环境变量：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `PORT` | 8080 | 监听端口 |
| `DATA_DIR` | /data | SQLite 数据目录 |
| `GIN_MODE` | release | Gin 运行模式 |
| `AUTH_TOKEN` | （空） | API 认证 Token，为空则不启用认证 |

### 4. 连接客户端到服务器

在客户端设置中填写：

- **服务器地址**：你的服务器 URL，如 `https://your-domain.com` 或 `http://your-ip:8080`
- **服务器认证 Token**：与服务器 `AUTH_TOKEN` 环境变量一致（如未设置则留空）

不配置服务器地址时，数据只保存在本地。

## 服务器 API

所有接口在 `/api/activities` 下，设置了 `AUTH_TOKEN` 时需要 `Authorization: Bearer <token>` 请求头。

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/activities` | 获取所有记录 |
| POST | `/api/activities` | 创建记录（支持 upsert） |
| POST | `/api/activities/batch` | 批量创建 |
| GET | `/api/activities/stats` | 统计信息 |
| GET | `/api/activities/:id` | 获取单条记录 |
| PUT | `/api/activities/:id` | 更新记录 |
| DELETE | `/api/activities/:id` | 删除记录 |
| GET | `/health` | 健康检查 |

## 客户端设置项

| 设置 | 说明 | 默认值 |
|------|------|--------|
| 保存路径 | 截图临时保存位置 | `~/Desktop/Screenshots` |
| AI 模型 | Kimi 或 Seed 2.0 Lite | Seed 2.0 Lite |
| 服务器地址 | 远程同步服务器 URL | （空，不同步） |
| 服务器认证 Token | 服务器 API Token | （空） |
| 自动截屏间隔 | 1s / 2s / 3s / 5s / 10s / 30s / 60s | 2 秒 |
| 截图质量 | 原始 / 高 / 中 / 低 | 原始分辨率 |
| 开机自启动 | 登录时自动启动 | 关闭 |

## 本地数据

- 数据库位置：`~/Library/Application Support/AutoScreenshot/screenshots_v2.db`
- 可用 `sqlite3` 查询：

```bash
sqlite3 ~/Library/Application\ Support/AutoScreenshot/screenshots_v2.db \
  "SELECT datetime(timestamp, 'unixepoch', 'localtime'), activityDescription FROM screenshots ORDER BY timestamp DESC LIMIT 20;"
```

## 项目结构

```
├── macos_app/                    # macOS 客户端（Swift/SwiftUI）
│   ├── Package.swift
│   ├── build.sh                  # 构建 .app + .dmg
│   └── Sources/AutoScreenshot/
└── screenshot-server/            # 同步服务器（Go/Gin/GORM）
    ├── main.go
    ├── Makefile
    ├── Dockerfile
    ├── docker-compose.yml
    └── VPS_DEPLOY.md
```

## License

MIT
