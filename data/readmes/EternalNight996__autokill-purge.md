<p align="center"><img src="assets/autokill-purge.png" width="92" height="92" alt="autokill-purge logo" /></p>

<h1 align="center">🍊 autokill-purge · 梦神破甲</h1>

<p align="center"><b>三宿主（DSH / MengBot / AutoKill）的破甲控制台 —— 83 条宿主补丁可视化 · 载荷生成 · 装备发放 · 备份还原 · 一键装/卸</b><br/>
<sub>拆掉宿主自己的闸门：提示词 · 审批 · 沙箱 · asar 落地</sub></p>

<p align="center"><img src="docs/shots-ux2/hero-breach-1280.png" width="100%" alt="破甲台实际界面：DSH 已从 resources/app 载入（asar 已让位），78/83 已注入，插件 0.3.5，记忆库 0.52.0" /></p>

<p align="center">
  <img src="https://img.shields.io/npm/v/autokill-purge?style=flat" alt="npm" />
  <img src="https://img.shields.io/github/stars/EternalNight996/autokill-purge?style=flat" alt="stars" />
  <img src="https://img.shields.io/badge/dependencies-0-FF7A45" alt="deps" />
  <img src="https://img.shields.io/badge/node-%E2%89%A522-3c873a" alt="node" />
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="license" />
  <img src="https://img.shields.io/badge/hosts-DSH%20%C2%B7%20MengBot%20%C2%B7%20AutoKill-8957e5" alt="hosts" />
  <img src="https://img.shields.io/badge/patches-79%2F83-2ea043" alt="patches" />
</p>

**简体中文（默认）** · [English](README.en.md)

> 上图就是当前实机：DSH `0.2.2-rc.5` 已从 `resources/app` 载入（asar 已让位），**78/83 已注入**（面板按 web 口径计；把桌面壳那几条算上为 79），插件 `0.3.5`、记忆库 `0.52.0`。

## ⚡ 一行装好

```bash
npx autokill-purge            # 或：npm i -g autokill-purge && autokill-purge
```

装完打开 `http://127.0.0.1:8792`。零依赖（只用 Node 标准库），Windows 桌面宿主可一键「落地并重启」。

## 🎯 它到底做什么
## 🖥 平台支持

| 平台 | 控制台 | 宿主补丁（DSH 桌面） | 说明 |
|---|---|---|---|
| **Windows 10/11** | ✅ | ✅ 完整 | 主开发平台：asar 落地、WMI 脱离进程树、启动项快捷方式 |
| **macOS** | ✅ | ✅ 基础 | 自动探测 `.app/Contents/Resources`，用 `pkill` 结束宿主 |
| **Linux** | ✅ | ✅ 基础 | 自动探测 `/opt/DeepSeek Harness`、`~/.local/share/deepseek-harness` |

平台差异集中在 `web/platform.mjs`：主目录、应用数据目录、桌面安装根、npm 全局根、进程结束与枚举。
覆盖变量：`DSH_HOME`（数据目录）、`DSH_DESKTOP_ROOT`（桌面安装根）、`DSH_DESKTOP_EXE`（可执行文件）。
Windows 专属能力（注册表、启动项快捷方式、WMI 脱离进程树）在其它平台自动跳过并明确降级。


模型「不肯干」通常不是一句话的事，而是**四层闸门**叠在一起：

| 层 | 闸门 | 本项目的处理 |
|---|---|---|
| 提示词层 | 宿主往 system prompt 里塞的「安全边界 / 拒答话术 / 身份句」 | **83 条宿主补丁**逐条字节替换（可视化勾选、可回滚） |
| 注入层 | 你的破甲正文怎么进模型 | 写 `prompt-inject.md` / `AGENTS.md`，会话内 `system-prompt/assemble` 拼装 |
| 审批层 | 提权、工具询问、沙箱拒绝 | 补丁把「必问 / 必拒」掰成「放行」，不弹窗不中断 |
| 宿主层 | 桌面壳从 `app.asar` 加载，改了不生效 | 「落地」把 `app.asar` 让位到 `resources\app`，重启即生效 |

控制台把这些做成可点、可看、可回滚的动作，而不是一堆脚本。

## 🧩 三宿主能力矩阵

| 能力 | DSH（DeepSeek Harness） | MengBot | AutoKill |
|---|---|---|---|
| 破甲方式 | 83 条宿主补丁 + 注入 | bot soul 注入 + 5 条宿主补丁 | 提示词注入 + MCP 工具桥 |
| 补丁覆盖 | **79/83**（4 条判死见下） | **5/5** | — |
| 装备/技能 | 插件 + 装备记录 + 预设同步 | `BotRecord.gear` + soul | `ui.slots` + `build.gear` |
| 备份 | 全量快照（文件 + sha256） | 逐 bot pre-inject 快照 | `config.toml` + prompt 备份 |
| 还原 | 回最近快照 / 恢复出厂 | 逐 bot 回滚 | 从备份拷回 |
| 一键安装 | 补丁 + 注入 + 插件 | 补丁 + 全 bot 注入 | MCP 挂载 + 注入 |
| 卸载干净 | asar 归位 + 补丁还原 + 卸插件 | 补丁 `--revert` + soul 还原 | 卸 MCP + 删注入 |
| 验收 | `verify` 4 项残留检查 | `verify` 2 项 | `verify` 2 项 |

## 🚀 快速开始

```bash
git clone https://github.com/EternalNight996/autokill-purge.git
cd autokill-purge
node web/server.mjs            # http://127.0.0.1:8792
```

常用命令：

```bash
node scripts/lifecycle.mjs status                 # 三宿主安装/生效状态
node scripts/lifecycle.mjs backup --host=all      # 全量备份
node scripts/lifecycle.mjs install --host=mengbot # 一键安装（先 --dry-run 看计划）
node scripts/lifecycle.mjs uninstall --host=all   # 卸载
node scripts/lifecycle.mjs verify  --host=all     # 「卸干净了吗」逐项验收
node scripts/patch-mengbot-wrap.mjs --check       # MengBot 补丁锚点唯一性
node test/patch-compat-0202.mjs                   # 0.2.2 兼容锚点回归
```

## 🧠 83 条补丁是怎么来的

上游 `dsh-purge` 把「拆闸」拆成可枚举的补丁（提示词 25 / 代码 47 / 工具 8 / 兼容 3），本项目把它**内化**成一份引擎 + 一份可读清单 `catalog.json`，并补齐了 **DSH 0.2.2-rc.5** 的锚点差异：

- 兼容层只**追加**锚点、不动上游锚点：0.1.7 走原路径，0.2.2 命中新锚点；
- 目标文件按版本重定位（`dsh-harness-dev-context`、`deliverable-file-references`、`dsh-tool-executor-ptc`、`dsh-tools/lib/pipeline.js`、profile 里的 hooks 两包）；
- 已判死的 4 条写在文档里，不假装绿：`#56 #77`（回溯改服务端 surface replace）、`#76`（预设已无身份句）、`#80`（上游已最小化）。

细节见 [docs/0.2.2-兼容工作记录.md](docs/0.2.2-兼容工作记录.md)、[docs/补丁缺口清单-2026-11-20.md](docs/补丁缺口清单-2026-11-20.md)。

## 🔐 备份 / 还原 / 卸载干净

```bash
node scripts/lifecycle.mjs backup    --host=all   # 快照（含 sha256 清单）
node scripts/lifecycle.mjs restore   --host=all   # 还原（先存 pre-restore 守卫）
node scripts/lifecycle.mjs uninstall --host=all   # 卸载（每一步都可回滚）
node scripts/lifecycle.mjs verify    --host=all   # 残留验收：clean=true 才算干净
```

MengBot 的回环实测过：`uninstall → verify(clean=true) → install → status(injected=10)`。

## 🗺️ 目录结构

```
web/            控制台（零依赖 HTTP 服务 + 前端）
web/patch-engine/  补丁引擎（vendor 自 dsh-purge）+ catalog + 0.2.2 兼容层
plugin/         宿主内插件（注入改写 / redteam_* 工具 / 预设自举）
gear/           AutoKill 侧插件骨架
break/          PE 字节补丁 CLI（破甲模板的另一条路）
scripts/        lifecycle / patch-mengbot-wrap / 安装与运维脚本
docs/           兼容记录、缺口清单、落地 runbook、MengBot 内部地图
test/           68 个契约与回归测试
```

## 🙏 上游与致谢

本项目的补丁引擎、文案与预设**都不是凭空来的**，明确署名如下：

| 上游 | 作者 / 仓库 | 被用在哪 |
|---|---|---|
| **dsh-purge v1.1.71** | [@YuJunZhiXue](https://github.com/YuJunZhiXue) · [dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) | 83 条宿主补丁的定义与字节锚点（本仓库 `web/patch-engine/vendor` 为其相对 import 闭包） |
| **dsh-purge-community** | [@mikamikasuki](https://github.com/mikamikasuki/dsh-purge) · [@MMovo](https://github.com/MMovo/dsh-purge) | 社区线的补丁适配与新版本锚点参考 |
| **梁神预设（liangshen）** | [@linxin666](https://www.npmjs.com/package/@linxin666/dsh-liangshen) · [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | `~/.dsh/.agent-presets/liangshen` 预设与 bootstrap |
| **DeepSeek Harness** | [@deepseek-ai](https://github.com/deepseek-ai) · [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 宿主本体（0.1.7 / 0.2.2 两代布局差异是兼容层的工作对象） |
| **memory-eternal** | [@EternalNight996](https://github.com/EternalNight996/memory-eternal) | 记忆库（本项目默认接它）+ README / 描述 / Topics 的版式参考 |

以及本机 Desktop 侧的两个闭源宿主 **MengBot / AutoKill**：我们只对它们的明文 `resources/server` 做字节锚点替换，并把注入落在它们自己的数据结构里（`bots.json` 的 `soul`、`config.toml` 的 `ui.slots`）。

如果上游作者不希望被这样引用或二次分发，请开 issue，我会立刻调整或摘除对应部分。

## ⚠️ 边界

- 本项目面向**你自己拥有的机器与宿主**：改文件前一律备份，卸载有 `verify` 验收；
- 它拆的是**宿主自己的闸门**（审批/沙箱/提示词），拆不掉模型厂商服务端的内容审核；
- 官方升级会覆盖宿主目录，升级后需重跑 `apply`（DSH）或 `--apply`（MengBot）；
- 请遵守你所在地法律与所使用模型/宿主服务条款，后果自负。

## 📄 License

MIT。上游组件的授权见各自仓库；`web/patch-engine/vendor` 保留 dsh-purge 的 MIT 许可与出处。

<p align="center"><sub>梦神破甲 · autokill-purge · 让闸门听你的</sub></p>
