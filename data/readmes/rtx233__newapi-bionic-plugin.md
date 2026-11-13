<p align="center"><img src="../icon.png" width="96" alt="Bionic"></p>

<h1 align="center">Bionic 本地模型 · New API 插件</h1>

<p align="center">简体中文 | <a href="../README.md">English</a></p>

把 Bionic 桌面应用（Element Labs 出品，基于 LM Studio）里运行的模型接入 New API。Bionic 本地服务原生支持 OpenAI、OpenAI Responses 和 Anthropic Messages 协议，网关直接转发这些请求，并按 Bionic 返回的 token 数计费。Gemini 格式的请求会先转换成对话补全再发给 Bionic。

插件还提供：

- 从 Bionic 获取渠道的模型列表，可以只列语言模型、只列向量模型，或只列已加载的模型。
- 给每个请求加上空闲卸载时间，按需加载的模型空闲后会自动释放内存。
- 每隔几分钟检查一次 Bionic，Bionic 无法访问时（比如电脑休眠或应用关闭）自动禁用渠道密钥，恢复访问后自动启用。

需要 New API v1.0.0-rc.50 或更高版本。

## 安装

- 在网关「插件 → 插件市场」的社区插件里搜索 Bionic 安装，或者把插件码粘贴到「插件码」框里。
- 也可以在「上传插件 → 从 URL 导入」里粘贴这个地址：

  ```text
  https://raw.githubusercontent.com/rtx233/newapi-bionic-plugin/v1.0.0/plugin.js
  ```

## 准备工作

1. 在 Bionic 里打开「本地服务器」页面，启动服务，记下端口，默认是 `1234`。
2. 如果 New API 运行在另一台机器上，在服务设置里打开「在网络中提供服务」，或者用 Tailscale、frp、Cloudflare Tunnel、`ssh -R` 等隧道把端口暴露出去。
3. 可选：在服务设置里打开「Require Authentication」，并在「Manage Tokens」里创建 API Token。端口能被其他机器访问时请务必打开。

## 渠道设置

1. 安装插件后，新建渠道，类型选「任务插件」，绑定本插件。
2. Base URL：Bionic 服务地址，不带 `/v1`，例如 `http://192.168.1.20:1234`。默认值是 `http://127.0.0.1:1234`，只适用于 New API 直接运行在 Bionic 同一台电脑上的情况。New API 跑在 Docker 里时要填容器能访问到的地址，例如 Docker Desktop 下的 `http://host.docker.internal:1234`。
3. 密钥：Bionic 开启身份验证时填 API Token，否则随便填。
4. 模型：点「获取模型列表」从 Bionic 读取。模型名就是 Bionic 的模型标识，例如 `qwen/qwen3-8b`。想对外用更好记的名字，可以配置模型映射。
5. 渠道配置：
   - 获取的模型：全部模型、仅语言模型或仅向量模型。
   - 仅已加载的模型：只列出 Bionic 当前已加载到内存的模型。
   - 空闲卸载时间：为请求按需加载的模型空闲多少秒后由 Bionic 卸载。`0` 表示沿用 Bionic 自己的设置。请求里自带 `ttl` 时以请求为准。
   - 健康检查及间隔：默认开启，每 300 秒一次。渠道需要开启自动禁用，健康检查才能禁用密钥。

## 模型与接口

| 客户端接口 | 发给 Bionic 的接口 | 模型 |
| --- | --- | --- |
| `POST /v1/chat/completions` | `/v1/chat/completions` | 语言模型 |
| `POST /v1/responses` | `/v1/responses` | 语言模型 |
| `POST /v1/messages` | `/v1/messages` | 语言模型 |
| `POST /v1beta/models/{model}:generateContent` | `/v1/chat/completions`，经过转换 | 语言模型 |
| `POST /v1/completions` | `/v1/completions` | 语言模型 |
| `POST /v1/embeddings` | `/v1/embeddings` | 向量模型 |
| `GET /v1/models` | `/api/v1/models`，不可用时依次改用 `/api/v0/models` 和 `/v1/models` | 渠道表单的模型列表 |

所有对话接口都支持流式输出。Bionic 服务设置里开启「JIT（即时）模型加载」时，模型会在第一次请求时加载，这次请求要等加载完成。

## 计费

和普通 OpenAI 兼容渠道一样，按 Bionic 返回的输入和输出 token 数、以每个模型的倍率或价格计费。用户调用前，请先为每个模型名设置模型倍率或固定价格。Bionic 的向量接口不返回 token 数，这时 New API 会根据输入文本估算输入 token。

## 示例

```bash
curl https://your-gateway.example/v1/chat/completions \
  -H "Authorization: Bearer sk-..." \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen/qwen3-8b", "messages": [{"role": "user", "content": "你好"}], "stream": true}'
```

## 限制

- Bionic 在一台电脑上提供服务，大模型和并发请求受这台电脑的内存和 Bionic 的并行请求设置限制。需要分担负载时，可以为多台电脑各建一个渠道。
- Bionic 本地服务不支持 TLS。经过公网访问时，请放在隧道或 HTTPS 反向代理后面，并开启身份验证。
- 健康检查只在 New API 主节点上运行。新建渠道或网关重启后，第一次检查会在十分钟内进行。

## 开发

`new-api` 是 [New API 发布页](https://github.com/QuantumNous/new-api/releases)里的二进制文件。

```bash
new-api plugin lint plugin.js
new-api plugin test plugin.js --fixture test/golden.json
```

| 文件 | 用途 |
| --- | --- |
| `plugin.js` | 插件源码 |
| `README.md`、`README.zh-CN.md` | 网关安装页和插件市场显示的说明 |
| `CHANGELOG.md`、`CHANGELOG.zh-CN.md` | 当前版本的更新说明 |
| `icon.png` | 插件图标 |
| `test/golden.json` | 插件钩子的测试用例 |

## 许可证

[MIT](../LICENSE)
