# 拍片哥工作台（paipiange）

[![CI](https://github.com/paipiange/gongzuotai/actions/workflows/ci.yml/badge.svg)](https://github.com/paipiange/gongzuotai/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![npm](https://img.shields.io/npm/v/dsh-paipiange.svg)](https://www.npmjs.com/package/dsh-paipiange)

> A local-first AI content studio running as a DeepSeek Harness plugin — copywriting, images, video and Q-version comics for WeChat / Xiaohongshu / Zhihu / Toutiao, from idea to publish.

面向 DeepSeek Harness 的本地优先 AI 内容创作工作台。当前已打通原生插件入口、AI 文字/图片/本地视频生成、持久化后台任务、素材与备份、公众号漫画、发布历史和待发布清单。

## 快速开始

### 安装（作为 Harness 插件）

**新机器首选：dsh 插件命令，务必钉版本号**

```bash
dsh plugin add dsh-paipiange@0.3.7
```

也可在 Harness 插件市场（Plugin Market）搜索 `dsh-paipiange` 一键安装，或手动在 profile 的
`package.json` 声明 `"dsh-paipiange": "0.3.7"`。

> ⚠️ **四个必踩的坑，务必规避：**
>
> **1. 一定要钉版本号 `@0.3.7`，不要裸包名或 `^0.2.0`。** pnpm 的 `minimumReleaseAge`
> （默认 24 小时）会过滤「发布不足 24 小时」的版本，裸包名/范围会静默回退到旧版
> （0.2.0~0.2.3 的 `better-sqlite3` 是强依赖，缺 Python 时触发 `node-gyp` 编译失败）。
> 只有 0.2.6+ 彻底移除了 better-sqlite3 依赖（vendor 内置二进制），安装期零编译。
>
> **2. 走 npm registry 安装，绝不用本地 `file:` tarball（尤其路径含中文）。** 用
> `"file:D:/.../工作台/xxx.tgz"` 安装时，pnpm 会把中文路径 URL 编码进符号链接目录名，
> dsh 主程序 import 插件时无法解析，报 `ERR_MODULE_NOT_FOUND`，插件「只有名字、没有描述」。
> 必须用 npm 版本号走 registry（纯 ASCII 符号链接）。
>
> **3. 市场搜索务必搜 `dsh-paipiange`，不要搜裸名 `paipiange`。** 双包发布时裸名
> `paipiange` 的 client bundle 里 `__ModuleLoader__.load` 的 id 仍是 `dsh-paipiange`，
> 与 dsh 按 entry 名「paipiange」对账时 id 错配，会导致侧边栏 tab 不显示、插件无描述。
> 请优先安装 `dsh-paipiange`（id 与包名一致，正常显示）。
>
> **4. 旧版已 deprecate，但挡不住 minimumReleaseAge 门控，还是得钉 `@0.3.7`。**
>
> 若希望裸包名也能始终装到最新版，可在 Harness profile 的 `pnpm-workspace.yaml` 关闭
> 发布年龄门控：
>
> ```yaml
> minimumReleaseAge: 0            # 永久关闭门控，裸包名/范围都能追到 latest
> ```
>
> 详见 [docs/install.md](./docs/install.md)。

### 从源码构建

```bash
# 1. 克隆并安装依赖
git clone https://github.com/paipiange/gongzuotai.git
cd gongzuotai
pnpm install

# 2. 本地 UI 预览（仅调试 UI，非插件入口）
pnpm dev

# 3. 构建并一键部署到实机 Harness（自动处理 native ABI）
bash scripts/deploy.sh
```

> ⚠️ 插件依赖 `better-sqlite3`（原生 addon），其 ABI 必须匹配实机 Electron 版本。请用 `scripts/deploy.sh` 一键部署，**不要**手工 `pnpm install` 覆盖。详见 [docs/native-rebuild.md](./docs/native-rebuild.md)。

## 当前已实现

- Harness Host / Client 双端源码骨架与 `cordis.patch.yml`。
- 产品品牌统一为“拍片哥工作台”，内部标识统一为 `paipiange`。
- 参考图核心布局：内部侧栏、顶部工具条、Hero、灵感卡、分类筛选、快捷创作、精选模板与真实记录空态。
- AI 文章、图片、视频、标题、营销文案、小红书工作台界面。
- 素材、分析、发布、灵感、记录、设置页面。
- 页面导航、侧栏折叠、移动抽屉、搜索、灵感切换、Toast、表单校验反馈。
- 文章、标题、营销、小红书和图片工作台可保存用户手动输入的草稿；刷新后仍保留在当前浏览器。
- 首页最近创作、侧栏最近创作、记录搜索、继续编辑、归档、恢复与永久删除。
- 本地待发布清单和基于真实草稿状态的数据统计；不自动登录或发布到第三方平台。
- 手动草稿复制与 Markdown 导出；不会把固定样例冒充 AI 生成结果。
- Host 侧 SQLite v1 schema、跨平台私有数据目录、参数化创作仓库、版本快照、软删除/恢复与一致性备份。
- SQLite 使用真实临时数据库测试；视频类型在仓库层也会被拒绝，不会写入任务或创作记录。
- 视频双引擎：Remotion + Three.js 本地渲染（vendor 自 dsh-video-workbench，MIT），一站式出片含字幕、音乐、数字人与多引擎 TTS；另保留 ComfyUI 出帧方案。
- 未配置模型时不伪造 AI 结果。
- 375px 至桌面宽度的响应式适配、键盘焦点与减少动画支持。
- SQLite 持久化生成队列：跨页面/重启继续、并发限制、优先级、暂停/继续/取消、指数退避自动重试。
- Q 版情侣漫画支持多图批量、图中文字、统一进度与耗时记录，并可同步微信公众号草稿或导出贴图包。
- 发布管理保存操作历史、微信 `media_id`、失败原因、重试次数、状态刷新、版本快照与发布前检查。
- 真实插件 `apply()` 端到端回归覆盖 Harness 鉴权、路由、SQLite、生成队列重启恢复与发布导出。

## 界面预览

首页（暖棕金国风主题，本地优先）：

<table>
  <tr>
    <td align="center"><img src="docs/screenshots/home-hero.jpg" alt="首页 · 创作灵感" width="100%"></td>
    <td align="center"><img src="docs/screenshots/home-banner.jpg" alt="首页 · Banner" width="100%"></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><img src="docs/screenshots/home-inspiration.jpg" alt="首页 · 灵感卡" width="100%"></td>
  </tr>
</table>

## 当前边界

- 视频生成走本地 Remotion + Three.js 渲染，或 ComfyUI 出帧；不接付费文生视频供应商。
- 微信公众号只同步到草稿箱；最终群发仍由用户在公众号后台确认。
- 为保护隐私，发布重试不会把图片 Base64 或第三方凭证写入数据库；已处理的图片仅在当前面板会话内缓存，用于失败后免重传的断点重试，关闭面板即释放。

## 本地开发

```bash
pnpm install
pnpm dev
```

本地预览页只用于 UI 开发，不替代 Harness 原生插件入口。

安装、升级与卸载见 [docs/install.md](./docs/install.md)。

## 部署到实机 Harness（重要）

本插件依赖 `better-sqlite3`（原生 addon），其实机运行时为 Electron，
**ABI 与开发机标准 Node 不同**。每次改代码后，请勿手工 `pnpm install` 或
`cp` 覆盖（会破坏 native 依赖的 ABI），统一用一键部署脚本：

```bash
bash scripts/deploy.sh
```

脚本会自动完成：探测实机 Electron 版本 → 构建打包 → 针对该版本重编译
`better-sqlite3` → 同步 native 二进制 + 补齐 `bindings`/`file-uri-to-path`
→ 更新插件产物 → 用实机 Electron 实测自校验。详细原理见
[docs/native-rebuild.md](./docs/native-rebuild.md)。

遇到安装、ABI、路由 401、视频生成等问题，先查 [docs/troubleshooting.md](./docs/troubleshooting.md)。

## 验证

```bash
pnpm typecheck
pnpm test
pnpm build
```

构建输出：

- `dist/`：本地 UI 预览产物，不发布为插件。
- `lib/index.js`：Host 模块。
- `lib/client.js`：Client 模块。

UI 验收同时覆盖 1280×774、390×844 和减少动画模式。开发预览中的草稿只写入浏览器 `localStorage`，不会进入仓库；正式数据仍需在验证 Harness 认证与运行时契约后迁移到 Host SQLite。

## 隐私与安全

请遵守 [AGENTS.md](./AGENTS.md)：不要提交密钥、个人信息、真实业务数据、数据库、上传素材、日志或本地敏感配置。模型凭证只能由后续 Host 适配层安全读取，不能进入浏览器代码或 Git 历史。

## 常见问题（FAQ）

<details>
<summary>安装后插件不生效 / 路由报错？</summary>

多为 `better-sqlite3` 的 ABI 与实机 Electron 不匹配导致。请改用 `bash scripts/deploy.sh` 重新部署，它会自动探测 Electron 版本并重编译 native 依赖。详见 [docs/native-rebuild.md](./docs/native-rebuild.md)。
</details>

<details>
<summary>为什么不能直接 `pnpm install` 后覆盖到实机？</summary>

实机 Electron 的 ABI 与开发机 Node 不同，直接 install 会把 native 依赖编译成错误 ABI，导致插件启动崩溃。统一走部署脚本。
</details>

<details>
<summary>视频渲染用的是什么，会不会调用付费文生视频？</summary>

视频走本地 Remotion + Three.js 渲染，或 ComfyUI 出帧后 FFmpeg 合成，全程本地出片，不调用付费文生视频供应商。注意 Remotion 采用双重许可，3 人以上营利性公司需自行评估 Company License，见 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。
</details>

<details>
<summary>我的 API Key 会泄露吗？</summary>

不会。密钥只保存在本机 Host 侧，前端拿不到明文；仓库也不允许提交任何密钥、个人信息或真实业务数据，见 [AGENTS.md](./AGENTS.md)。
</details>

## 架构

整体为 Host / Client 双端结构，架构图与数据流见 [docs/architecture.md](./docs/architecture.md)。

## 技术方案与贡献

- 代码结构与数据流见 [docs/architecture.md](./docs/architecture.md)。
- 未来规划见 [ROADMAP.md](./ROADMAP.md)。
- 模板结构、占位符语法与贡献方式见 [docs/templates.md](./docs/templates.md)。
- 想贡献代码请先读 [CONTRIBUTING.md](./CONTRIBUTING.md)。
- 发现漏洞请查看 [SECURITY.md](./SECURITY.md)。
- 第三方依赖许可见 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。
