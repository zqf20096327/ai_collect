# 🧩 AGY Plugin Collection

> Google Antigravity（AGY）自用第三方插件与配套工具推荐清单。

[![Plugins](https://img.shields.io/badge/curated-6%20items-brightgreen.svg)](#插件清单)
[![Surface](https://img.shields.io/badge/surface-Desktop%202.0%20%7C%20IDE%20%7C%20CLI-orange.svg)](#插件清单)

本仓库**仅整理自用推荐的第三方插件/工具清单与作者源仓库索引**，不托管、不打包任何源码。如需安装或更新，请直接点击表格中的**源仓库地址**，前往作者仓库拉取最新版本。

---

## 插件清单

### ⚡ 性能与工具加速

| 插件名称 | 用途说明 | 源仓库 |
|---|---|---|
| `agy-fast` | 零依赖本地 MCP 加速插件：将高频代码搜索、符号大纲提取、跨文件原子编辑与并发检查合并为单次本地调用，并在启动时注入精简工作区快照，显著减少模型往返轮次与额度消耗，不影响原生 Diff 与界面 | [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast) |

### 📊 计量监控与界面增强

| 插件名称 | 用途说明 | 源仓库 |
|---|---|---|
| `usage-monitor` | 全端本地用量、速率、上下文与配额监控（支持 Desktop 2.0 / IDE / CLI / SSH 远端）：实时追踪 tok/s、TTFT、10 类上下文构成、多配额池与租约预占、主/子代理及蜂群调用明细，支持跨端会话迁移与 Excel 报表导出 | [yuhuan-dev/antigravity-usage-monitor](https://github.com/yuhuan-dev/antigravity-usage-monitor) |
| `agy-capsule` | 输入框底栏紧凑遥测胶囊与原位模型面板：实时展示上下文占用、缓存过期变色提醒、5h/周配额与生成速率动效，带慢首字与报错红黄胶囊预警、原位思考强度滑条及侧栏用量活动热力图 | [Lumidarin/agy-capsule](https://github.com/Lumidarin/agy-capsule) |

---

## ⚠️ 只能第三方 Agent 代为安装

> 以下项目涉及修改客户端本体、注入代理补丁或独立桌面端部署，**无法交由 Antigravity 自身安装**，仅支持通过**第三方 Agent** 代为安装（或手动前往源仓库按说明操作）。

| 名称 | 类型 | 用途说明 | 源仓库 |
|---|---|---|---|
| `antigravity-desktop-cn` | 中文汉化 | Antigravity 桌面版中文汉化引擎（支持 Windows / macOS / Linux 一键安装与备份无损还原）：基于 ASAR 注入动态界面翻译，严格隔离会话正文、思考流、文件树、代码区与图标防止误译，并内置轻量上下文占用圆环、分类构成与输出速率监控浮卡 | [Silas-02/antigravity-desktop-cn](https://github.com/Silas-02/antigravity-desktop-cn) |
| `antigravity-proxy` | 透明代理 | Windows 免 TUN 进程级透明代理工具：无需开启系统 TUN 模式或管理员权限，仅定向接管 Antigravity 相关进程走 SOCKS5 / HTTP 代理（支持账密认证），全覆盖桌面端、IDE、CLI（`agy`）与编辑器 ACP 模式；IDE 端附带状态栏可视化配置、出口 IP/Gemini 检测与升级自动恢复补丁 | [yuaotian/antigravity-proxy](https://github.com/yuaotian/antigravity-proxy) |
| `Antigravity-Manager` | 账号与网关 | 多账号管理与本地协议中转桌面端（Tauri v2 + Rust）：支持多账号配额余量实时监控、最优账号推荐与一键无缝切换，并可将账号会话转换为标准 OpenAI / Anthropic / Gemini 本地 API 接口，具备 429/401 自动无感轮换与模型分级路由能力 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) |

---

## 安装与更新

1. **标准第三方插件**（上方「插件清单」）：点击右侧 GitHub 源仓库链接按作者 `README` 拉取安装，或直接把源仓库地址发给 Antigravity 让其代为安装。
2. **外围工具与补丁**（上方「⚠️ 只能第三方 Agent 代为安装」）：请交由第三方 Agent 读取对应源仓库文档代为安装，或手动按源仓库说明操作。
3. **官方与合作方插件**：如 `Chrome DevTools`、`Tavily` 等内置市场插件，可直接在客户端左侧栏 **Customizations → Marketplace** 搜索并一键添加。

---

## 💡 自用搭配说明

- **双监控并存**：`usage-monitor` 与 `agy-capsule` 均基于只读本机数据库与独立 Shadow DOM 实现，可同时开启互不冲突——前者挂在「顶栏 + 右侧辅助栏」看全局配额预占、子代理/蜂群明细与历史报表；后者留在「输入框底栏」看当轮紧凑上下文、缓存过期倒计时与原位思考强度滑条。
- **胶囊显示提示**：顶栏/底栏胶囊依赖本机调试端口（`--remote-debugging-port=0`）。按各插件源仓库说明配置好快捷方式后，请通过快捷方式启动 Antigravity。

---

## 🛡️ 免责声明

本仓库仅作个人插件推荐与链接导航，不对第三方插件的安全性与兼容性作任何担保；安装前请自行审阅对应源仓库代码。
