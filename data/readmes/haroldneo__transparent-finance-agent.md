# 透明财务 · Transparent Finance Agent

为一人公司（OPC）而生的开源财务报税 Agent。它把票据识别、自动记账、
经营分析和中国报税流程连成一个可追溯闭环，并在最终提交前保留人工确认。

- 产品体验：https://transparent-finance-agent.harold1998z.chatgpt.site
- 开源仓库：https://github.com/haroldneo/transparent-finance-agent

## 核心能力

- 创始人驾驶舱与可切换月、季、年的现金流像素
- PDF / 照片票据导入和会计凭证建议
- 可追溯自动记账与三大财务报表
- 自然语言经营问答
- Windows 税务系统自动填表、校验和人工提交关口
- 小规模纳税人到一般纳税人的账套衔接表达

## 本地运行

需要 Node.js `>=22.13.0`。

```bash
npm install
npm run dev
```

验证生产构建：

```bash
npm test
npm run lint
```

## 数据与隐私

公开版本中的公司经营数字、交易、客户、发票和税务数据均为合成内容，只保留
真实业务分布的展示价值，不包含原始账套、银行流水、合同、票据文件、完整税号、
个人身份信息或访问凭证。

票据导入交互仅在当前浏览器会话中生成本地预览，不会上传用户选择的文件。

## 技术栈

Next.js / React / TypeScript / vinext / Cloudflare Sites

Header 使用 ETM Refract 的实时折射实现并保留其 MIT 许可，详见
[`app/vendor/refract/LICENSE`](app/vendor/refract/LICENSE)。

## 许可证

项目主体采用 [MIT License](LICENSE) 开源。第三方代码继续适用其各自许可证。
