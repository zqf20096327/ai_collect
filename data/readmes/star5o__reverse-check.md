# 🔍 reverse-check：LLM API 逆向检测工具
**当前版本：v0.02**

[English Version](./README_EN.md) | 中文版

**项目地址**：[GitHub](https://github.com/star5o/reverse-check) | [网站1（vercel域名）](https://reverse-check.vercel.app/) | [网站2（我的域名）](https://reverse-check.no-reverse-api.com)

**Vercel一键部署**：[![使用 Vercel 部署](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/star5o/Freverse-check&project-name=reverse-check&repository-name=reverse-check)

本工具是一个基于是否支持官方参数的逆向检测工具。不能通过本工具检测的API极大概率是逆向的。

目前项目处于初步阶段，暂时需要人工对比响应结果与示例进行判断。

## 功能特性

- 🔍 支持多种模型提供商的API检测
  - OpenAI
  - Claude
  - Gemini

- 🛠 丰富的参数测试选项
  - max_tokens参数检测
  - logprobs参数检测
  - n参数检测
  - stop参数检测
  - function_call/tools参数检测
  - response_format参数检测
  - 图像输入检测

- 📊 直观的结果展示
  - API请求信息实时展示
  - 响应结果对比分析
  - 官方示例参考
  - 简洁/完整响应切换

## 技术栈

- 前端框架：Vue 3
- UI组件：Tailwind CSS
- 构建工具：Vite

## 手动部署

### 安装依赖

```bash
npm install
```

### 运行开发服务器

```bash
npm run dev
```

### 构建生产版本

```bash
npm run build
```

## 使用说明

1. 选择模型提供商（OpenAI/Claude/Gemini）
2. 选择要测试的参数类型
3. 填写API配置信息
   - API Base URL
   - API Key
   - 模型名称
4. 点击「开始检测」按钮
5. 查看检测结果和对比信息

## 参数详情

### OpenAI 参数

| **参数**     | **说明**                                                           |
|------------------|--------------------------------------------------------------------------|
| **max_tokens**   | 官方API严格遵循token限制（如max_tokens=10），逆向API会忽略限制。 |
| **logprobs**     | 官方API会返回每个token的logprobs信息，逆向API不支持此功能。 |
| **n**            | 官方API可以返回多个答案（如n=2），逆向API只返回一个。 |
| **stop**         | 官方API会在遇到停止词时停止生成，逆向API会忽略停止词。 |
| **image_url**    | 官方API能正确处理图片URL并生成描述，逆向API无法处理图片。 |
| **function_call**| 官方API返回JSON格式的函数调用，逆向API不调用函数。 |
| **response_format**| 官方API返回指定格式（如JSON），逆向API只返回字符串。 |

### Claude 参数

| **参数**     | **说明**                                                           |
|------------------|--------------------------------------------------------------------------|
| **max_tokens**   | 官方API严格遵循token限制（如max_tokens=10），逆向API会忽略限制。 |
| **stop**         | 官方API会在遇到停止词时停止生成，逆向API会忽略停止词。 |
| **function_call**| 官方API返回JSON格式的函数调用，逆向API不调用函数。 |

### Gemini 参数

| **参数**     | **说明**                                                           |
|------------------|--------------------------------------------------------------------------|
| **max_tokens**   | 官方API严格遵循token限制（如max_tokens=10），逆向API会忽略限制。 |
| **codeExecution**| 官方API有内置的代码执行工具，逆向实现无法执行代码。 |
| **googleSearch** | 官方API能正确调用Google搜索并返回结果，逆向实现无法使用Google搜索工具。 |
| **response_format**| 官方API返回指定格式（如JSON），逆向实现只返回字符串。 |

## 待办事项

1. 实现自动化逆向检测
2. 实现与Uptime Kuma的集成以进行持续监控

## change log
### v0.0.2
1. 增加了推理模型专用检测参数
   - OpenAI: reasoning_max_tokens参数检测
   - Claude: reasoning_stop参数检测
2. 当API响应返回错误时（如520错误），也能在页面上显示完整的响应体，而不是弹窗提示。

## 推理模型说明
OpenAI的 API 不会返回reasoning_content字段

## API文档参考

- [OpenAI API文档](https://platform.openai.com/docs/api-reference/chat)
- [Claude API文档](https://docs.anthropic.com/en/api/messages)
- [Gemini API文档](https://ai.google.dev/gemini-api/docs)

## 许可证

MIT License