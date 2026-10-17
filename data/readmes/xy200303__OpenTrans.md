<div align="center">
  <img src="./website/public/opentrans-mark.svg" alt="OpenTrans" width="96" />
  <h1>OpenTrans</h1>
  <p><strong>给 LLM 网关、兼容层和代理层使用的多协议请求体、响应体与 SSE 事件转换 SDK</strong></p>
  <p>OpenAI Chat / OpenAI Responses / Claude / Gemini -> 标准化中间结构 -> Target</p>
  <p>
    <a href="https://opentrans.xyun.dev/">文档与网站</a>
    ·
    <a href="#what-is-opentrans">项目介绍</a>
    ·
    <a href="#quick-start">快速开始</a>
    ·
    <a href="#protocol-matrix">协议矩阵</a>
    ·
    <a href="#web-service">Web 服务</a>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Go-1.20+-00ADD8?logo=go&logoColor=white" alt="Go 1.20+" />
    <img src="https://img.shields.io/badge/docs-opentrans.xyun.dev-2563eb?logo=googlechrome&logoColor=white" alt="docs" />
    <img src="https://img.shields.io/badge/OpenAI-supported-10a37f" alt="OpenAI supported" />
    <img src="https://img.shields.io/badge/Responses-supported-111827" alt="Responses supported" />
  </p>
  <p>
    <img src="https://img.shields.io/badge/Claude-supported-d97757" alt="Claude supported" />
    <img src="https://img.shields.io/badge/Gemini-supported-4285F4" alt="Gemini supported" />
    <img src="https://img.shields.io/badge/Gin-middleware-0f766e" alt="Gin middleware" />
    <img src="https://img.shields.io/badge/SSE-conversion-f59e0b" alt="SSE conversion" />
  </p>
  <p>
    <img src="https://img.shields.io/badge/Docker-opentransd-2496ED?logo=docker&logoColor=white" alt="Docker opentransd" />
    <img src="https://img.shields.io/badge/VitePress-docs-41B883?logo=vite&logoColor=white" alt="VitePress docs" />
  </p>
</div>

<p align="center">
  <code>go get github.com/xy200303/OpenTrans</code>
</p>

<a id="what-is-opentrans"></a>

## OpenTrans 是什么

OpenTrans 是一个用 Go 编写的多协议 LLM 适配层。它把 OpenAI Chat Completions、OpenAI Responses、Anthropic Claude、Google Gemini 的请求体、响应体、流式事件先统一到一套标准化中间结构，再按目标协议重新输出。

适合你拿它来做：

- API 网关协议适配
- 多模型供应商切换
- 兼容层与代理层开发
- 统一日志、审计、缓存与路由

<p align="center">
  <img src="./images/image.png" alt="OpenTrans request and response conversion" width="88%" />
</p>

<p align="center">
  <img src="./images/image-1.png" alt="OpenTrans web service preview" width="88%" />
</p>

## 当前能力

- 支持 `OpenAI -> 标准化中间结构 -> Target`
- 支持 `Responses -> 标准化中间结构 -> Target`
- 支持 `Claude -> 标准化中间结构 -> Target`
- 支持 `Gemini -> 标准化中间结构 -> Target`
- 支持基础多轮文本消息转换
- 支持非流式响应体转换
- 支持基础流式文本增量事件转换
- 支持 `ginx.ConvertStreamEventBody(...)` 做 SSE 中间件转换，兼容 `CRLF`、多行 `data:` 与 `event/id/comment` 元信息透传
- 支持常见采样参数：`temperature`、`top_p`、`max_tokens`
- 支持基础图片输入映射与工具调用映射

## 安装

```bash
go get github.com/xy200303/OpenTrans
```

## 导入方式

推荐直接从模块根路径导入：

```go
import opentrans "github.com/xy200303/OpenTrans"
```

根目录的 [opentrans.go](./opentrans.go) 会统一对外导出 SDK 能力，内部实现仍放在 `pkg/opentrans`。

## 提取模型

现在也可以直接使用项目内提取的四种协议结构体做适配：

```go
req, err := opentrans.NormalizeOpenAIChatCompletionParams(openaiParams)
req, err := opentrans.NormalizeResponsesRequest(responsesReq)
req, err := opentrans.NormalizeClaudeMessageParams(claudeParams)
req, err := opentrans.NormalizeGeminiGenerateContentRequest(geminiReq)
```

当前提取模型适配覆盖：

- OpenAI `OpenAIChatCompletionParams` / `OpenAIChatCompletion` / `OpenAIChatCompletionChunk`
- Responses `ResponsesRequest` / `ResponsesResponse` / `ResponsesStreamEvent`
- Claude `ClaudeMessageParams` / `ClaudeMessage` / `ClaudeMessageStreamEvent`
- Gemini `GeminiGenerateContentRequest` / `GeminiGenerateContentResponse`

这一层优先走结构体直接映射，而不是整包 `json.Marshal/Unmarshal` 转换。
四种协议结构体已经提取到 `pkg/opentrans/internal/providers/<provider>/` 目录下，按请求、响应、流式类型拆分，公共包只保留对外薄封装。

## 目录结构

```text
.
|-- go.mod
|-- README.md
|-- website/
|-- opentrans.go
|-- pkg/
|   `-- opentrans/
|       |-- converter.go
|       |-- models.go
|       `-- internal/
|           `-- providers/
|               |-- canonical/
|               |-- openai/
|               |-- claude/
|               |-- gemini/
|               `-- responses/
|-- services/
|   `-- opentransd/
|       |-- Dockerfile
|       |-- docker-compose.yml
|       |-- cmd/
|       |   `-- opentransd/
|       `-- internal/
|           `-- server/
|-- test/
`-- examples/
    |-- basic/
    |-- gin_middleware/
    |-- request_convert/
    |-- normalize_request/
    |-- response_convert/
    |-- stream_convert/
    |-- image_input/
    |-- tool_call/
    `-- provider_models/
```

## 文档官网

仓库已经新增基于 `VitePress` 的官网子项目，目录在 `website/`，和 Go 代码包本体分开维护。

本地预览：

```bash
cd website
npm install
npm run dev
```

构建静态站点：

```bash
cd website
npm run build
```

仓库同时提供了 GitHub Pages 工作流 `.github/workflows/docs.yml`，会独立构建 `website/` 子项目：

- `push` 到 `main` 时自动构建并部署官网
- `pull_request` 到 `main` 时自动校验文档能否成功构建

当前线上官网地址为：

```text
https://opentrans.xyun.dev/
```

如果未绑定自定义域名，GitHub Pages 默认地址为：

```text
https://xy200303.github.io/OpenTrans/
```

<a id="quick-start"></a>

## 快速开始

```go
package main

import (
	"fmt"
	"log"

	opentrans "github.com/xy200303/OpenTrans"
)

func main() {
	src := []byte(`{
	  "model": "gpt-4.1-mini",
	  "messages": [
	    {"role": "system", "content": "You are a helpful assistant."},
	    {"role": "user", "content": "Write a haiku about Go"}
	  ],
	  "temperature": 0.4
	}`)

	out, err := opentrans.ConvertRequestBody(src, opentrans.ProtocolOpenAI, opentrans.ProtocolClaude)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(out))
}
```

## 核心接口

```go
req, err := opentrans.NormalizeRequest(opentrans.ProtocolGemini, body)
out, err := opentrans.MarshalRequest(req, opentrans.ProtocolOpenAI)
raw, err := opentrans.ConvertRequestBody(body, opentrans.ProtocolClaude, opentrans.ProtocolResponses)
resp, err := opentrans.ConvertResponseBody(respBody, opentrans.ProtocolClaude, opentrans.ProtocolOpenAI)
evt, err := opentrans.ConvertStreamEventBody(eventBody, opentrans.ProtocolResponses, opentrans.ProtocolClaude)
```

如果你已经拿到了结构体，也可以直接转换，不必先手动序列化成 `[]byte`：

```go
req, err := opentrans.NormalizeResponsesRequest(responsesReq)
req, err := opentrans.NormalizeClaudeMessageParams(claudeReq)
resp, err := opentrans.NormalizeClaudeMessage(claudeResp)
evt, err := opentrans.NormalizeClaudeMessageStreamEvent(claudeEvent)
```

也可以复用一个转换器实例：

```go
converter := opentrans.MustNewConverter(opentrans.ProtocolOpenAI, opentrans.ProtocolGemini)
out, err := converter.Convert(body)
```

如果你在做 HTTP 网关，也可以直接接 Gin 中间件：

```go
import (
	"github.com/gin-gonic/gin"
	opentrans "github.com/xy200303/OpenTrans"
	"github.com/xy200303/OpenTrans/pkg/opentrans/ginx"
)

router := gin.Default()

router.POST(
	"/v1/chat/completions",
	ginx.ConvertRequestBody(opentrans.ProtocolOpenAI, opentrans.ProtocolClaude),
	func(c *gin.Context) {
		c.Status(200)
	},
)

router.GET(
	"/v1/messages",
	ginx.ConvertResponseBody(opentrans.ProtocolClaude, opentrans.ProtocolOpenAI),
	func(c *gin.Context) {
		c.Data(200, "application/json", []byte(`{"id":"msg_1","type":"message","role":"assistant","model":"claude-sonnet-4","content":[{"type":"text","text":"hello"}],"stop_reason":"end_turn"}`))
	},
)

router.GET(
	"/v1/messages/stream",
	ginx.ConvertStreamEventBody(opentrans.ProtocolClaude, opentrans.ProtocolOpenAI),
	func(c *gin.Context) {
		c.Header("Content-Type", "text/event-stream")
		_, _ = c.Writer.Write([]byte("data: {\"type\":\"content_block_delta\",\"delta\":{\"text\":\"hello\"}}\n\n"))
		c.Writer.Flush()
		_, _ = c.Writer.Write([]byte("data: [DONE]\n\n"))
	},
)
```

这里的 `req` / `resp` / `evt` 对外统一分别对应 SDK 的标准化中间结构：

- `Request`
- `Response`
- `StreamEvent`

其中 `Request/Response/StreamEvent` 是 SDK 对外暴露的标准化结构；OpenAI、Responses、Claude、Gemini 的提取结构体则作为协议适配层按需使用。

## 设计思路

第一层：解析不同供应商请求体。

第二层：统一映射到 SDK 的标准化中间结构。

第三层：根据目标协议重新编码。

这种设计比较适合后续继续补：

- 工具调用与函数调用
- 图片、音频、文件输入
- provider 特有字段透传
- HTTP 代理层和 SSE 转发层

当前 SDK 对外统一暴露 `Request / Response / StreamEvent` 这一套标准化结构；内部实现目录仍使用 `canonical` 作为包名承载这套中间表示。OpenAI、Responses、Claude、Gemini 的结构体适配函数则用于在各协议结构和标准化结构之间做转换。

## Gin 中间件

项目提供了一个轻量的 Gin 适配层，放在 `pkg/opentrans/ginx`：

- `ginx.ConvertRequestBody(source, target)`: 读取并转换进入 Gin handler 前的请求体
- `ginx.ConvertResponseBody(source, target)`: 捕获并转换 Gin handler 写出的响应体
- `ginx.ConvertStreamEventBody(source, target)`: 按 SSE `data:` 帧转换流式事件
- `ginx.MiddlewareOptions`: 可选自定义错误处理，例如按你自己的网关错误格式返回

对应示例可以看：

- [examples/gin_middleware/main.go](./examples/gin_middleware/main.go)

<a id="web-service"></a>

## Web 服务与 Docker 部署

仓库现在把可部署的 API/Web 服务独立放在 `services/opentransd/` 子项目中：

- `services/opentransd/cmd/opentransd`
- `services/opentransd/internal/server`
- 首页提供浏览器表单
- 支持把 `kind / source / target / body` 编进 URL，一键打开即自动转换
- 支持 Docker 和 `docker compose` 直接启动

### 本地启动

```bash
go run ./services/opentransd/cmd/opentransd
```

默认监听 `:8080`，也可以通过环境变量改端口：

```bash
PORT=9090 go run ./services/opentransd/cmd/opentransd
```

启动后可访问：

- `GET /`: 转换页面
- `GET /healthz`: 健康检查
- `GET|POST /convert`: 返回原始转换结果
- `GET|POST /api/convert`: 返回带元信息的 JSON 包装

### Docker 启动

如果你只是想快速体验，不需要先自己构建镜像，直接拉已经发布到 Docker Hub 的镜像即可：

```bash
docker run --rm -p 8080:8080 -e PORT=8080 xy200303/opentrans:latest
```

如果你希望固定到当前 `main` 分支镜像，也可以使用：

```bash
docker run --rm -p 8080:8080 -e PORT=8080 xy200303/opentrans:main
```

启动后直接访问：

```text
http://localhost:8080
```

直接使用 `docker compose`：

```bash
docker compose -f services/opentransd/docker-compose.yml up --build
```

或者手动构建：

```bash
docker build -f services/opentransd/Dockerfile -t opentrans .
docker run --rm -p 8080:8080 -e PORT=8080 opentrans
```

### Docker Hub 自动发布

仓库新增了 `.github/workflows/docker.yml`，会自动执行：

- `go test ./...`
- 多架构 Docker 构建：`linux/amd64`、`linux/arm64`
- 推送镜像到 Docker Hub
- 使用的服务镜像定义位于 `services/opentransd/Dockerfile`

需要在 GitHub 仓库中配置：

- Secret: `DOCKERHUB_USERNAME`
- Secret: `DOCKERHUB_TOKEN`
- 可选 Variable: `DOCKERHUB_REPOSITORY`

如果没有设置 `DOCKERHUB_REPOSITORY`，默认推送到：

```text
docker.io/<DOCKERHUB_USERNAME>/opentrans
```

其中：

- `DOCKERHUB_USERNAME` 是你的 Docker Hub 登录用户名，不是邮箱
- `DOCKERHUB_TOKEN` 建议使用 Docker Hub `Account Settings -> Personal access tokens` 里生成的 token
- GitHub 配置入口在 `Settings -> Secrets and variables -> Actions`

如果你的 Docker Hub 主页是：

```text
https://hub.docker.com/u/xy200303
```

那么 `DOCKERHUB_USERNAME` 就填写：

```text
xy200303
```

官网和 Docker 发布的完整配置说明、Pages 自定义域名和访问异常排查，可以直接看：

- [website/guide/ci-cd.md](./website/guide/ci-cd.md)

标签策略：

- 默认分支推送 `latest`
- `main` 分支同步推送 `main`
- `v*` Git tag 推送版本标签
- 同时生成 `sha-<commit>` 标签，便于回滚

### 转换接口示例

POST 原始 JSON 到 `/convert`：

```bash
curl -X POST "http://localhost:8080/convert?kind=request&source=openai&target=claude&pretty=1" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1-mini",
    "messages": [
      {"role": "user", "content": "hello"}
    ]
  }'
```

GET `/api/convert` 也可以直接走 URL 参数：

```text
http://localhost:8080/api/convert?kind=request&source=openai&target=claude&body=%7B%22model%22%3A%22gpt-4.1-mini%22%2C%22messages%22%3A%5B%7B%22role%22%3A%22user%22%2C%22content%22%3A%22hello%22%7D%5D%7D
```

### URL 一键转换

页面会自动把输入内容编码成 `body_b64` 形式的分享链接，所以不需要手动处理 URL 编码。复制页面里的“分享链接”后，直接打开即可自动回填并执行转换。

分享链接形态如下：

```text
http://localhost:8080/?kind=request&source=openai&target=claude&body_b64=...&autorun=1
```

## 标准化结构

### Request

`Request` 表示统一后的请求结构，核心字段包括：

- `Model`: 目标模型名
- `Messages`: 统一消息数组
- `Temperature` / `TopP` / `MaxTokens`: 常见采样参数
- `Stream`: 是否流式输出
- `Tools`: 统一工具定义
- `Metadata`: 通用元信息
- `Extra`: 当前未标准化、但希望保留的扩展字段

其中 `Messages` 的每一项都是：

- `Role`: 典型值如 `system`、`user`、`assistant`、`tool`
- `Content`: 统一内容片段数组
- `Name`: 可选消息名

### Response

`Response` 表示统一后的非流式响应结构，核心字段包括：

- `ID`: 响应 ID
- `Model`: 实际返回的模型名或模型版本
- `Role`: 通常为 `assistant`
- `Output`: 统一输出内容数组
- `StopReason`: 停止原因
- `Usage`: token 使用信息
- `Metadata`: 通用元信息
- `Extra`: 当前未标准化的扩展字段

### StreamEvent

`StreamEvent` 表示统一后的流式事件结构，核心字段包括：

- `Type`: 事件类型
- `ID`: 响应 ID
- `Model`: 模型名
- `Role`: 当前事件关联角色
- `Delta`: 增量内容
- `StopReason`: 结束原因
- `Usage`: token 使用信息
- `Sequence`: 可选事件序号
- `Metadata`: 通用元信息

当前内置事件类型包括：

- `response_start`
- `content_delta`
- `response_stop`
- `usage`

### ContentPart

`ContentPart` 是请求消息、响应输出、流式增量共用的统一内容单元。当前常见 `Type` 包括：

- `text`: 文本内容，使用 `Text`
- `image_url`: 图片 URL 输入，使用 `ImageURL`
- `image_base64`: Base64 图片内容，使用 `MIMEType` + `Data`
- `tool_call`: 工具调用，使用 `CallID` + `Name` + `Arguments`
- `tool_result`: 工具结果，使用 `CallID` + `Name` + `Result`

这套设计的目标是尽量先覆盖不同协议之间最常见、最稳定的公共能力；对于暂未标准化的字段，可以先挂在 `Extra` 或 `Metadata` 中，后续再逐步补齐。

<a id="protocol-matrix"></a>

## 协议映射矩阵

下表描述的是当前版本里“已经有代码实现并可直接使用”的主要能力范围。这里的“支持”表示已经接入标准化结构并可参与转换；“部分支持”表示只覆盖常见子集；“未完整支持”表示还没有稳定打通全部映射。

图例：

- `✅` 已支持
- `🟡` 部分支持
- `❌` 未完整支持

| 能力 | OpenAI Chat | OpenAI Responses | Claude | Gemini |
| --- | --- | --- | --- | --- |
| 请求文本输入 | ✅ | ✅ | ✅ | ✅ |
| 请求图片 URL 输入 | ✅ | ✅ | ✅ | ✅ |
| 请求 Base64 图片输入 | ❌ | ❌ | ✅ | ✅ |
| 请求工具定义 | ✅ | ✅ | ✅ | ✅ |
| 请求工具调用消息 | ✅ | ✅ | ✅ | ✅ |
| 请求工具结果消息 | ✅ | ✅ | ✅ | ✅ |
| 非流式文本响应 | ✅ | ✅ | ✅ | ✅ |
| 非流式图片/视频输出 | ❌ | ❌ | ❌ | ❌ |
| 流式文本增量 | ✅ | ✅ | ✅ | ✅ |
| 流式开始/结束/usage 事件 | ✅ | ✅ | ✅ | ✅ |
| provider 特有高级字段透传 | 🟡 | 🟡 | 🟡 | 🟡 |

当前可以这样理解：

- OpenAI Chat 现在已经支持 `assistant.tool_calls` 与 `tool` 消息映射，适合作为文本、多轮消息、图片 URL 输入、基础工具调用链的协议源或目标
- OpenAI Responses 现在已经支持 `function_call` / `function_call_output` 请求项与标准化结构互转
- Claude 当前已经支持 `tool_use` / `tool_result` 请求内容块与标准化结构互转，也支持图片 URL / Base64 输入；system 内容仍以文本为主
- Gemini 当前在请求侧对图片 URL、Base64 图片、工具调用、工具结果的标准化映射最完整
- 图片、音频、视频等多模态“输出”还没有作为统一能力完整打通，这部分仍建议按 provider 原始结构单独处理

## 当前限制

- 当前流式转换以文本增量、开始/结束、usage 为主
- 某些 provider 的高级字段与多模态输出暂未完整映射
- 更复杂的工具调用事件和更完整的代理级 SSE 语义仍可以继续增强

## Benchmark

项目里提供了独立的基准测试目录：

```bash
go test -bench . -benchmem ./benchmark/...
```

如果你想拿更稳定的参考值，建议至少跑 `5` 轮：

```bash
go test -bench . -benchmem -count 5 ./benchmark/...
```

项目里也提供了一个 PowerShell 脚本：

```powershell
./benchmark/run.ps1 -Count 5
./benchmark/run.ps1 -Bench 'ConvertRequestBody|ConvertResponseBody|ConvertStreamEventBody' -Count 5
./benchmark/run.ps1 -Count 5 -UseLocalCache
```

基准测试代码当前按能力拆分维护：

- `benchmark/request_benchmark_test.go`: 请求转换相关
- `benchmark/response_benchmark_test.go`: 响应转换相关
- `benchmark/stream_benchmark_test.go`: 流式事件转换相关
- `benchmark/fixtures_benchmark_test.go`: 共享测试样本与辅助方法
- `benchmark/run.ps1`: 稳定测量脚本，默认支持 `-count 5`


2026-04-14 在以下环境重新测试：

- `goos`: `windows`
- `goarch`: `amd64`
- `cpu`: `AMD Ryzen 7 H 255 w/ Radeon 780M`

当前一组参考结果如下：

说明：

- README 里的数值是单轮参考值，适合快速了解量级
- 如果你在做版本间性能对比，建议使用 `-count 5` 或更多轮数，优先看中位水平而不是单次结果

### Body -> Body 整链路转换

这组数据更接近真实网关场景，因为它覆盖了完整链路：

- `source body -> 标准化结构 -> target body`

| Benchmark | ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| `BenchmarkConvertRequestBodyOpenAIToClaude` | `1807` | `1113` | `21` |
| `BenchmarkConvertResponseBodyClaudeToOpenAI` | `1978` | `1322` | `22` |
| `BenchmarkConvertStreamEventBodyClaudeToOpenAI` | `720.1` | `606` | `9` |
| `BenchmarkConvertStreamEventBodyOpenAIToClaude` | `917.8` | `638` | `11` |

### Body -> 标准化结构 / 协议输出

| Benchmark | ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| `BenchmarkConvertRequestBodyClaudeToCanonical` | `3628` | `2273` | `41` |
| `BenchmarkConvertResponseBodyClaudeToCanonical` | `1028` | `624` | `13` |
| `BenchmarkConvertStreamEventBodyOpenAIToClaude` | `917.8` | `638` | `11` |
| `BenchmarkNormalizeRequestGeminiBody` | `1559` | `984` | `24` |

### Provider Model -> 标准化结构

| Benchmark | ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| `BenchmarkConvertRequestModelClaudeToCanonical` | `916.1` | `1216` | `15` |
| `BenchmarkConvertRequestModelResponsesToCanonical` | `1484` | `985` | `21` |
| `BenchmarkConvertResponseModelClaudeToCanonical` | `301.9` | `280` | `3` |
| `BenchmarkConvertResponseModelResponsesToCanonical` | `255.9` | `280` | `3` |
| `BenchmarkConvertStreamEventModelClaudeToCanonical` | `268.4` | `256` | `2` |
| `BenchmarkConvertStreamEventModelResponsesToCanonical` | `237.5` | `256` | `2` |

### 标准化结构 -> Provider Model

| Benchmark | ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| `BenchmarkMarshalRequestCanonicalToOpenAIModel` | `758.3` | `544` | `10` |
| `BenchmarkMarshalRequestCanonicalToClaudeModel` | `3074` | `2419` | `38` |
| `BenchmarkMarshalRequestCanonicalToResponsesModel` | `1356` | `984` | `8` |
| `BenchmarkMarshalResponseCanonicalToOpenAIModel` | `176.9` | `184` | `4` |
| `BenchmarkMarshalResponseCanonicalToClaudeModel` | `533.2` | `641` | `11` |
| `BenchmarkMarshalResponseCanonicalToResponsesModel` | `156.4` | `168` | `3` |
| `BenchmarkMarshalStreamEventCanonicalToOpenAIModel` | `43.81` | `64` | `1` |
| `BenchmarkMarshalStreamEventCanonicalToClaudeModel` | `218.3` | `368` | `4` |
| `BenchmarkMarshalStreamEventCanonicalToResponsesModel` | `15.36` | `0` | `0` |

### Provider Model -> Provider Model

| Benchmark | ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| `BenchmarkConvertRequestModelClaudeToGemini` | `1894` | `2081` | `29` |
| `BenchmarkConvertResponseModelClaudeToOpenAI` | `767.7` | `1001` | `16` |
| `BenchmarkConvertStreamEventModelClaudeToGemini` | `548.4` | `624` | `7` |

### 与常见实现方式的函数级对比

这组不是拿完整代理服务做对比，而是拿几种常见的“本地函数级协议互转实现方式”做同口径 benchmark：

- `OpenTrans`: 当前 SDK 的 `ConvertRequestBody`
- `StdJSON struct bridge`: 使用 `encoding/json` 解析到 typed struct，再手写桥接到目标协议结构
- `Map bridge`: 使用 `encoding/json` 解析到 `map[string]any`，再手写拼装目标协议结构

测试环境同上，当前一组参考值如下：

#### 纯文本 `OpenAI -> Claude`

| 实现 | ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| `OpenTrans` | `4048` | `1715` | `32` |
| `StdJSON struct bridge` | `6919` | `1409` | `27` |
| `Map bridge` | `10183` | `3659` | `76` |

#### 多模态 `OpenAI -> Claude`

样本包含：

- `system` 文本
- `user` 文本
- `image_url` 图片 URL 输入

| 实现 | ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| `OpenTrans` | `8832` | `3694` | `74` |
| `StdJSON struct bridge` | `11233` | `2009` | `41` |
| `Map bridge` | `15839` | `5925` | `111` |

可以把这组数据理解为：

- 对纯文本请求，`OpenTrans` 相比常见手写桥接实现已经有明显速度优势
- 对多模态请求，`OpenTrans` 目前也快于这两种常见基线实现
- `map[string]any` 风格的动态桥接在速度和分配上都明显最吃亏
- `OpenTrans` 之所以分配数不一定总是最低，是因为它在统一中间结构里保留了更多协议兼容信息和后续可扩展空间

可以粗略看出两点：

- 运行时热路径已经切到更高性能的 JSON 实现，`[]byte` 路径相比之前有了明显下降
- 整链路 `Body -> Body` 转换已经控制在微秒级，适合放在 API 网关或协议代理层
- 标准化结构回写到目标协议模型的开销整体较低，尤其是响应和流式事件
- Responses 结构体路径已经去掉 JSON 往返，归一化和回写的开销都进一步下降
- Claude / Gemini 的结构体公开 API 也已经切到 provider 直转，避免再绕 OpenAI 结构中转
- 对于网关或代理层，流式事件转换已经足够轻量；如果是 SDK 内部链路，优先直接走结构体版本会更合适
