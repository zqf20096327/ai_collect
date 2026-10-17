# AI 投资人 - 毒舌金主

一个 AI 副业想法验证工具。输入你的副业想法，AI 投资人会联网搜索竞品和市场数据，给出犀利的投资判断和建议。

[![使用 EdgeOne Makers 部署](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://console.cloud.tencent.com/edgeone/makers/new?repository-url=https%3A%2F%2Fgithub.com%2Fliyupi%2Fai-investor&env=WSA_API_KEY&env-description=%E8%81%94%E7%BD%91%E6%90%9C%E7%B4%A2%20API%20%E5%AF%86%E9%92%A5%EF%BC%88%E8%85%BE%E8%AE%AF%E4%BA%91%20WSAPI%EF%BC%89)

## 功能特点

- **联网搜索**：自动搜索竞品、市场规模、融资案例
- **多轮对话**：记住上下文，支持方案迭代和追问
- **投资判断**：S/A/B/C 四级评价体系
- **犀利点评**：赛道分析、核心风险、差异化建议、变现路径

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | React 18 + Vite + TypeScript |
| 后端 | EdgeOne Makers Agent Runtime |
| AI 框架 | OpenAI Agents SDK |
| Markdown 渲染 | marked |
| 部署 | EdgeOne Pages |

## 项目结构

```
├── agents/                # Agent 后端
│   ├── chat/
│   │   ├── index.ts       # 主聊天端点 (POST /chat)
│   │   └── _prompt.ts     # 系统提示词
│   ├── stop.ts            # 中止端点 (POST /stop)
│   ├── _model.ts          # LLM 模型配置
│   └── _shared.ts         # SSE 流式响应工具
├── src/                   # 前端 React 应用
│   ├── App.tsx
│   ├── lib/api.ts         # API 调用 + SSE 解析
│   └── components/
│       ├── ChatMessage.tsx # 消息渲染 (Markdown)
│       ├── Header.tsx
│       ├── InputBar.tsx
│       └── WelcomeScreen.tsx
├── edgeone.json           # EdgeOne 部署配置
└── package.json
```

## 本地开发

```bash
# 安装依赖
npm install

# 关联远程项目并拉取环境变量
edgeone makers link
edgeone makers env pull

# 启动开发服务器
edgeone makers dev
```

## 环境变量

参考 `.env.example`：

| 变量 | 说明 |
|------|------|
| `AI_GATEWAY_API_KEY` | AI Gateway 密钥（部署时自动配置） |
| `AI_GATEWAY_BASE_URL` | AI Gateway 地址（部署时自动配置） |
| `AI_GATEWAY_MODEL` | 模型名称（可选，默认 deepseek-v4-flash） |
| `WSA_API_KEY` | 联网搜索 API 密钥（使用 web_search 工具时需要） |

## 部署

```bash
edgeone makers deploy
```

## 多轮对话实现

使用 EdgeOne Makers 平台的 `context.store` 通用 API 实现对话历史持久化：

```typescript
// 读取历史
const history = await store.getMessages({ conversationId, limit: 50, order: 'asc' });
// 转为 OpenAI 输入格式
const inputItems = store.toOpenAIInput(history);
// 保存用户消息
await store.appendMessage({ conversationId, role: 'user', content: message });
// 传入 Agent
const result = await run(agent, [...inputItems, newMessage], { stream: true });
// 回复完成后保存助手消息
await store.appendMessage({ conversationId, role: 'assistant', content: fullContent });
```

## License

MIT
