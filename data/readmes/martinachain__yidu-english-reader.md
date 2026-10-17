# 易读 · 英文阅读助手

> 直接读原文 · 卡住才求助 · 生词句子自动沉淀

**中文** · [English](./README.en.md)

🔗 **在线体验：[english-reading.zeabur.app](https://english-reading.zeabur.app)**（自带 DeepSeek key 即可使用）

**易读**是一个面向中文学习者的英文阅读工具，一个产品、两个入口：

- 📖 **网页阅读器** —— 导入 EPUB / PDF / Markdown，双击查词、划选拆句
- 🔍 **浏览器插件** —— 在任意英文网页（新闻、博客、论坛……）划词划句，不用先把内容导进来

两个入口**共享同一份生词本、句子库和间隔重复（SRS）复习队列**：不管是在书里查的词，还是刷网页时随手划的句子，都会汇总到同一个地方，一起进复习计划。

所有数据都存在你自己的浏览器里，没有账号、没有服务器数据库，**开箱即用**。

---

## 网页阅读器

- **读 EPUB / PDF / Markdown** —— 拖入或点击导入，自动提取书名、作者、封面
- **双击查词** —— 双击任意单词，AI 结合上下文给出本句中的中文释义
- **划选拆句** —— 选中一个长句，AI 拆出句子结构、关键短语、难点注解和完整翻译
- **生词本 + 句子库** —— 查过的词、拆过的句自动入库
- **间隔重复复习（SRS）** —— 按 1 / 3 / 7 / 14 / 30 / 60 天的阶梯排期，句卡连续看懂 3 次后「毕业」
- **阅读体验** —— 目录跳转、书签、续读定位、阅读进度，PDF 支持懒加载分页（几百页也不卡）
- **数据本地化** —— 全部存浏览器 IndexedDB，换设备不同步（这是设计取舍，不是 bug）

### 快速开始

需要 [Node.js](https://nodejs.org) 18+。

```bash
git clone https://github.com/martinachain/yidu-english-reader.git
cd yidu-english-reader
npm install
npm run dev
```

打开 [http://localhost:3000](http://localhost:3000)，第一次进会弹出配置框，填入你的 **DeepSeek API Key** 即可开始。

> 不需要创建 `.env` 文件——key 在界面里填，只存你本地浏览器。

## 浏览器插件

在任意英文网页划词、划句，不用先把内容导入网页阅读器——收藏的词/句会自动同步进上面那个生词本和句子库。

### 安装（目前只支持手动加载，还没上架 Chrome 商店）

1. 去 [GitHub Release](https://github.com/martinachain/yidu-english-reader/releases) 下载最新的插件 zip 包
2. 解压
3. 打开 Chrome，地址栏输入 `chrome://extensions`，回车
4. 右上角打开「开发者模式」
5. 点「加载已解压的扩展程序」，选中刚才解压出来的文件夹
6. 工具栏出现「易读」图标，点它可以看收藏统计、打开生词本、进设置页

### 功能

- **选中即查词** —— 在网页上选中一个单词（双击或拖选正好框住一个词都行），立刻弹出中文释义，不需要联网、不需要填 key（离线词典）
- **选中即解析** —— 拖选一整句话，自动弹出面板解析句子结构 + 翻译（需要在设置页填 DeepSeek API Key）
- **自动同步** —— 打开网页阅读器时，插件本地收藏的待同步词/句会自动同步进生词本，不需要手动导入

设置页可以填 DeepSeek API Key（和网页阅读器各自独立存储，两边不共享，需要各填各的）。

### 申请 DeepSeek API Key

AI 查词和拆句调用的是 [DeepSeek](https://platform.deepseek.com)（便宜、对中文友好），网页阅读器和浏览器插件都需要各自配置一份：

1. 注册并登录 [platform.deepseek.com](https://platform.deepseek.com)
2. 在 [API Keys](https://platform.deepseek.com/api_keys) 页面创建一个 key（形如 `sk-...`）
3. 充值少量额度（拆句一次几厘钱）
4. 把 key 填进应用（或插件设置页）的配置框

key 只保存在你本地（网页阅读器存浏览器 `localStorage`，插件存 `chrome.storage.local`），每次请求由你的浏览器**直接发送给 DeepSeek 官方接口**，不经过本应用的任何服务器，也不会上传到任何第三方。

## 自己部署一份

这个项目是纯前端，没有后端、不持有任何密钥，可以直接 fork 之后部署到 Vercel / Zeabur / Netlify 等任意静态托管，或者 `npm run build && npm start` 跑在自己的机器上。每个用户用自己浏览器里的 key 直连 DeepSeek，所以公开部署也不会变成「免费 DeepSeek 代理」。

### ⚠️ 自己部署时，浏览器插件的同步需要额外一步

浏览器插件往哪个网址同步，是**写死在 `extension/manifest.json` 里的**（Chrome 的 `content_scripts.matches` 不能在运行时修改）。默认只认两个地址：

```json
"matches": ["https://english-reading.zeabur.app/*", "http://localhost:3000/*"]
```

所以：

- **本地开发**（`http://localhost:3000`）—— 插件同步开箱即用 ✅
- **部署到你自己的域名** —— 网页阅读器完全能用，但**插件不会把生词同步过去**，会显示「同步超时」

要让插件同步到你自己的域名，需要改两处然后重新加载插件：

1. `extension/manifest.json` —— 两处 `matches` / `exclude_matches` 里加上你的域名
2. `extension/src/shared/storage.ts` 和 `extension/src/options/options.html` —— 把默认／可选的阅读助手地址换成你的域名

改完在 `extension/` 目录跑 `node esbuild.config.mjs` 重新打包，再去 `chrome://extensions` 重新加载。

---

## 技术栈

- **框架**：[Next.js 16](https://nextjs.org)（App Router + Turbopack）、React 19、TypeScript
- **样式**：Tailwind CSS v4
- **本地存储**：[Dexie](https://dexie.org)（IndexedDB 封装）
- **电子书解析**：[epub.js](https://github.com/futurepress/epub.js)、[pdf.js](https://mozilla.github.io/pdf.js/)
- **AI**：浏览器用 `fetch` 直连 DeepSeek 官方接口（`deepseek-chat` 模型），无服务端代理
- **浏览器插件**：Chrome Manifest V3，独立 esbuild 构建，通过 `postMessage` 和网页阅读器同步

## 项目结构

```
app/
  page.tsx              书架（导入、复习入口、API Key 配置）
  read/[bookId]/        阅读页（查词、拆句、书签、目录）
  review/               间隔重复复习
  library/              生词本
components/             阅读器、弹框、面板等
lib/
  deepseek.ts           浏览器直连 DeepSeek（查词 / 拆句）
  import-bridge.ts      接收浏览器插件同步过来的词/句
  db.ts、srs.ts 等       数据库、SRS 算法、pdf/epub 解析、API Key 管理
types/                  共享类型
extension/              浏览器插件（独立构建，Chrome Manifest V3）
```

## 说明与边界

- **数据存在浏览器本地**：清空浏览器数据 / 换浏览器 = 书和记录都没了。类型里预留了 `updatedAt` 字段，未来可接 Supabase 等做云同步。
- **可以放心公开部署**：本应用是纯前端，没有后端、不持有任何密钥。每个用户用自己浏览器里的 key 直连 DeepSeek，所以即使部署成公开网址，也不会变成「免费 DeepSeek 代理」被人白嫖——这正是改用浏览器直连、删掉服务端代理的原因。
- **key 安全**：你的 key 只存在你自己的浏览器、只发给 DeepSeek 官方接口，本应用的服务器全程接触不到它。

## License

MIT
