# Agentic AI Slidev Deck

内部分享演示文档，主题为「Agentic AI 入门与业务落地」。

[在线演示](https://intro-agentic-ai.lishun.me)

[演讲录像](https://www.bilibili.com/video/BV1v6o5BrEiT/)

## 运行

```bash
pnpm install
pnpm dev
```

默认地址：`http://localhost:3030`

## 构建

```bash
pnpm build
```

## 部署到 Cloudflare

仓库已包含 [`wrangler.jsonc`](wrangler.jsonc)，当前配置会把 `pnpm build` 产出的 `dist/` 目录作为静态资源发布到 Cloudflare Workers。

首次部署前，先登录 Cloudflare：

```bash
pnpm dlx wrangler login
```

如需修改线上项目名，可先编辑 `wrangler.jsonc` 里的 `name` 字段；当前默认值为 `intro-agentic-ai`。

执行构建并部署：

```bash
pnpm build
pnpm dlx wrangler deploy
```

部署成功后，Wrangler 会输出对应的 `*.workers.dev` 地址，可直接访问分享。

后续更新内容时，重新执行同一组命令即可完成覆盖发布：

```bash
pnpm build
pnpm dlx wrangler deploy
```

如需导出 PDF 或 PPTX，可在安装浏览器导出依赖后执行：

```bash
pnpm add -D playwright-chromium
pnpm export
```
