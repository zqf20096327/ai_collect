<div align="center">

<img src="https://raw.githubusercontent.com/shigu4795-design/deepseek-plugins-storage/main/logo.png" width="130" height="130" alt="DeepSeek Harness Official Logo" />

# ⚡ DeepSeek Harness Hub
### 🚀 全球领先的 DeepSeek 官方与开源生态插件市场
**The Premier Open-Source Plugin & Extension Marketplace for DeepSeek**

<br />

[![Official Website](https://img.shields.io/badge/🌐_Official_Hub-deepseek.stream-0ea5e9?style=for-the-badge&logo=google-chrome&logoColor=white)](https://deepseek.stream)
[![Desktop Release](https://img.shields.io/github/v/release/Minglink/DeepSeek-Harness-Desktop?color=blue&style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Minglink/DeepSeek-Harness-Desktop/releases/tag/v0.1.1)
[![Topic dsh-plugin](https://img.shields.io/badge/GitHub_Topic-dsh--plugin-3b82f6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/topics/dsh-plugin)
[![Community](https://img.shields.io/badge/💬_Geek_Community-deepseek.stream%2Fcommunity-8b5cf6?style=for-the-badge)](https://deepseek.stream/community)
[![License MIT](https://img.shields.io/badge/License-MIT-emerald?style=for-the-badge)](LICENSE)

<br />

**[🌐 访问插件市场主站 (deepseek.stream)](https://deepseek.stream)** • 
**[🔥 官方必装榜 (Essential List)](https://deepseek.stream)** • 
**[💬 开发者茶馆社区 (Forum)](https://deepseek.stream/community)** • 
**[📖 生态开发规范 (Docs)](https://deepseek.stream/guide)** • 
**[⬇️ 桌面客户端 EXE 下载](https://github.com/Minglink/DeepSeek-Harness-Desktop/releases/tag/v0.1.1)**

</div>

---

## 📖 项目简介 (Introduction)

**DeepSeek Harness Hub** 是专为 **DeepSeek** 大模型与 **DeepSeek Harness (DSH)** 生态打造的现代化开源插件市场与开发者交流社区。

平台汇聚了全网最硬核实用的 DeepSeek 扩展、自动化 Agent 智能体、代码生成辅助、Prompt 精选模板与多模态扩展，旨在为千万 AI 开发者提供媲美 VS Code / Raycast 般极致的**免命令行一键装载**体验。

---

## 🌟 核心功能特性 (Key Features)

| 核心模块 | 功能特性与用户价值 |
| :--- | :--- |
| **⚡ 一键极速装载** | 深度集成系统级 `dsh://plugin/install?...` 自定义协议，网页或文档一键拉起桌面端 (EXE)，0 门槛自动装载。 |
| **⭐ 官方必装精选榜** | 站长与社区算法双重甄选，实时汇聚高口碑、高稳定性的必备生产力工具。 |
| **💬 极客茶馆社区** | 采用 Linux.do / NodeLoc 现代化论坛风格，支持富文本排版、本地插图秒传、代码高亮与自动「🔥 热帖」打标。 |
| **🙋 需求悬赏中心** | 提出特定场景的插件定制需求，发布悬赏令，由全球开源极客协同接单实现。 |
| **🛡️ 银行级安全防护** | 全站部署 Strict-Transport-Security (HSTS)、防点击劫持、防爆破限流与文件二进制魔数头隔离防护。 |

---

## 🚀 插件一键装载与使用指南 (Usage Guide)

### 方法一：官方桌面客户端一键装载（推荐 ⚡）
1. 访问 **[DeepSeek-Harness-Desktop Release](https://github.com/Minglink/DeepSeek-Harness-Desktop/releases/tag/v0.1.1)** 下载并安装最新版桌面客户端 (`.exe`)；
2. 打开 **[deepseek.stream](https://deepseek.stream)** 插件市场，挑选心仪插件；
3. 点击 **「⚡ 一键安装到桌面版」**，浏览器将自动唤醒本地客户端并完成沙箱装载！

### 方法二：终端命令行 CLI 安装
打开 PowerShell、CMD 或 Linux 终端，执行以下命令：

```bash
# 推荐：直接从 GitHub 仓库源拉取安装
dsh plugin --profile web add "github:Minglink/dsh-infinite-gen-2"

# 或通过插件市场标准包名安装
dsh plugin add <plugin-id>
```

---

## 🔌 开发者接入：一键安装联动协议规范 (`dsh://`)

DeepSeek Harness 官方桌面客户端（EXE）内置支持 `dsh://` 自定义系统协议，任何开源作者均可将一键安装链接或徽章加入到自己的项目主页中：

### 1. 协议 URL 规范
```text
dsh://plugin/install?id={id}&name={name}&version={version}&repo={repo}&permissions={permissions}&downloadUrl={downloadUrl}
```

### 2. Markdown / HTML 一键安装徽章（直接复制）
```html
<a href="dsh://plugin/install?id=open-design&name=Open%20Design&version=1.0.0&repo=nexu-io/open-design">
  <img src="https://img.shields.io/badge/Install%20in-DeepSeek%20Harness-0ea5e9?style=for-the-badge&logo=deepseek" alt="一键安装到 DeepSeek Harness" />
</a>
```

### 3. 前端 JavaScript 安全触发函数
```typescript
export function installToDeepSeekDesktop(plugin: { id: string; name: string; version: string; repo: string }) {
  const params = new URLSearchParams({
    id: plugin.id,
    name: plugin.name,
    version: plugin.version || 'latest',
    repo: plugin.repo,
  });
  const iframe = document.createElement('iframe');
  iframe.style.display = 'none';
  iframe.src = `dsh://plugin/install?${params.toString()}`;
  document.body.appendChild(iframe);
  setTimeout(() => document.body.removeChild(iframe), 2000);
}
```

---

## 🏷️ 社区标签 (GitHub Topics)

为了让全球开发者更容易在 GitHub 上探索和发现 DeepSeek 插件生态，本项目长期维护以下 GitHub Topic 标签体系：

- **[`dsh-plugin`](https://github.com/topics/dsh-plugin)**
- **[`deepseek`](https://github.com/topics/deepseek)**
- **[`deepseek-harness`](https://github.com/topics/deepseek-harness)**
- **[`ai-agent`](https://github.com/topics/ai-agent)**
- **[`plugin-marketplace`](https://github.com/topics/plugin-marketplace)**

---

## 🔗 官方直达导航 (Official Links)

- 🌐 **插件市场主站**：[https://deepseek.stream](https://deepseek.stream)
- 💬 **开发者茶馆论坛**：[https://deepseek.stream/community](https://deepseek.stream/community)
- 📖 **开发者白皮书 & 协议规范**：[https://deepseek.stream/guide](https://deepseek.stream/guide)
- 🖥️ **桌面客户端 Release 仓库**：[Minglink/DeepSeek-Harness-Desktop](https://github.com/Minglink/DeepSeek-Harness-Desktop)

---

## 📄 开源许可证 (License)

本项目遵循 [MIT License](LICENSE) 开源协议。欢迎全球开发者 Fork、Star 与生态共建！

<div align="center">
  <p>© 2026 DeepSeek Harness Community • Empowering the Next Generation of AI Agents</p>
</div>
