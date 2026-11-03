# awesome-ai-recreations

> 用 AI 把真实作品复刻成**能跑起来**的东西。方法、源码、成品、可跟做的步骤，都在这。
> 同一批原作由不同模型分别复刻，成品并列对照：**DeepSeek 版（00/01，主推）** 与 **GLM 5.3-Flash 版（9 台）**。
> 在线预览：<https://topmindspace.github.io/awesome-ai-recreations/>（GitHub Pages，随 main 自动部署）。

## 系列

| # | 系列 | 内容 | 状态 |
|---|---|---|---|
| 01 | [机械复刻系列](series/机械复刻系列/) | 两个模型的复刻：**DeepSeek 版**（00/01，4 页）· **GLM 5.3-Flash 版**（9 台，18 页 + 25 s 成片），均附完整源码 | ✅ 两版可用 |

新系列从这张表往下加；同一系列的实现版本（模型版本）登记在系列 README 与下方对应小节，约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## DeepSeek 版（主推）

[![00 机械章鱼 OC-8 · DeepSeek 版](series/机械复刻系列/deepseek复刻/covers/00-机械章鱼OC-8-封面-4x3.jpg)](series/机械复刻系列/deepseek复刻/00-机械章鱼OC-8/机械章鱼OC-8-互动页.html) [![01 V8 发动机 · DeepSeek 版](series/机械复刻系列/deepseek复刻/covers/01-V8发动机-封面-4x3.jpg)](series/机械复刻系列/deepseek复刻/01-V8发动机/V8发动机-互动页.html)

同一原作、另一次独立实现：**全中文界面 + 宝石紫 `#7c3aed` 强调色**，3D 模型与 HUD 按原作版式重新编写。
含互动页 + 影片页（单文件离线）+ 完整源码 + 参考图 + 4:3 封面 + 逐拍验收截图。

| # | 机器 | 巡览 | 互动页 | 影片页 | 说明 |
|---|---|---|---|---|---|
| 00 | 机械章鱼 OC-8（Pelagos OC-8） | 25 s / 10 拍 | [互动页](series/机械复刻系列/deepseek复刻/00-机械章鱼OC-8/机械章鱼OC-8-互动页.html) | [影片页](series/机械复刻系列/deepseek复刻/00-机械章鱼OC-8/机械章鱼OC-8-影片页.html) | [源码与验收](series/机械复刻系列/deepseek复刻/README.md) |
| 01 | V8 发动机（90° 十字曲轴 · 四冲程） | 26 s / 9 拍 | [互动页](series/机械复刻系列/deepseek复刻/01-V8发动机/V8发动机-互动页.html) | [影片页](series/机械复刻系列/deepseek复刻/01-V8发动机/V8发动机-影片页.html) | [源码与验收](series/机械复刻系列/deepseek复刻/README.md) |

- 实现版本说明、与 GLM 版的逐项对照、验收记录：[`series/机械复刻系列/deepseek复刻/`](series/机械复刻系列/deepseek复刻/README.md)
- 复现：`cd series/机械复刻系列/deepseek复刻/src/kit && node build.mjs all`

---

## GLM 5.3-Flash 版（9 台）

> 复刻模型：**GLM 5.3-Flash**（Z Code 会话内完成）。全中文界面、钴蓝 `#1e5fd6` 强调色。

| | | |
|---|---|---|
| [![00 机械章鱼 OC-8](series/机械复刻系列/glm5.3-flash复刻/covers/00-机械章鱼OC-8-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/00-机械章鱼OC-8/机械章鱼OC-8-互动页.html) | [![01 V8 发动机](series/机械复刻系列/glm5.3-flash复刻/covers/01-V8发动机-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/01-V8发动机/V8发动机-互动页.html) | [![02 塞斯纳 337 起落架](series/机械复刻系列/glm5.3-flash复刻/covers/02-塞斯纳337起落架-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/02-塞斯纳337起落架/塞斯纳337起落架-互动页.html) |
| [![03 海滩兽 Strandbeest](series/机械复刻系列/glm5.3-flash复刻/covers/03-海滩兽Strandbeest-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/03-海滩兽Strandbeest/海滩兽Strandbeest-互动页.html) | [![04 仿生沙虫 MK-X](series/机械复刻系列/glm5.3-flash复刻/covers/04-仿生沙虫MK-X-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/04-仿生沙虫MK-X/仿生沙虫MK-X-互动页.html) | [![05 机械水母 MJ-9](series/机械复刻系列/glm5.3-flash复刻/covers/05-机械水母MJ-9-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/05-机械水母MJ-9/机械水母MJ-9-互动页.html) |
| [![06 六足机器人 HX-18](series/机械复刻系列/glm5.3-flash复刻/covers/06-六足机器人HX-18-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/06-六足机器人HX-18/六足机器人HX-18-互动页.html) | [![07 机械蜜蜂 HB-7](series/机械复刻系列/glm5.3-flash复刻/covers/07-机械蜜蜂HB-7-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/07-机械蜜蜂HB-7/机械蜜蜂HB-7-互动页.html) | [![08 机械蝎子 SC-8](series/机械复刻系列/glm5.3-flash复刻/covers/08-机械蝎子SC-8-封面A-4x3.png)](series/机械复刻系列/glm5.3-flash复刻/pages/08-机械蝎子SC-8/机械蝎子SC-8-互动页.html) |

- 9 台真实机器 → 18 个离线 3D 页面（互动页 + 影片页）+ 25 s 成片，附完整源码
- 入口与目录索引：[`series/机械复刻系列/glm5.3-flash复刻/`](series/机械复刻系列/glm5.3-flash复刻/README.md)

> 在线玩：**[topmindspace.github.io/awesome-ai-recreations](https://topmindspace.github.io/awesome-ai-recreations/)** —— 点封面直达互动页；也可克隆或下载本仓库后双击打开（单文件、断网可跑）。

---

## 怎么用

### 我只想看

**在线版**：<https://topmindspace.github.io/awesome-ai-recreations/>（点封面或表格链接直达）。

本地打开对应目录下的 HTML 即可：

- DeepSeek 版：`series/机械复刻系列/deepseek复刻/<机器>/<机器>-互动页.html`（另有影片页）
- GLM 5.3-Flash 版：`series/机械复刻系列/glm5.3-flash复刻/pages/<机器>/<机器>-互动页.html`（另有影片页）

单个 HTML 文件，three.js、字体、贴图全部内联 —— **双击即开，断网也能跑**，不用装任何东西。

### 我想自己复刻一台

把仓库克隆下来，交给 agent 工具（Claude Code / Cursor / Codex / Gemini CLI 都行），然后说：

> 按 `series/机械复刻系列/docs/01` 的十步流程，复刻一台 <机器名>。

agent 需要的东西仓库里都备好了：

| 要什么 | 在哪 |
|---|---|
| 完整流程与踩坑 | `series/机械复刻系列/docs/01-机械章鱼OC-8-teardown机器模拟器.md` |
| 可直接用的建模提示词 | `series/机械复刻系列/docs/提示词原文/` |
| 公共库、构建脚本、配乐合成器 | `series/机械复刻系列/glm5.3-flash复刻/src/kit/` |
| 9 台已完成范例（参数、行数、耗时、问题与改法） | `series/机械复刻系列/glm5.3-flash复刻/records/` |
| 另一模型的独立实现范例 | `series/机械复刻系列/deepseek复刻/` |

人工照着做很费劲；**交给 agent 按流程做，才是这套仓库设计的主要用法**。

---

## 目录结构

```
awesome-ai-recreations/
├── README.md          总索引（本文件）
├── CONTRIBUTING.md    怎么加一个新系列 / 一个案例 / 一个实现版本
├── NOTICE.md          署名与来源总表
├── docs/              跨系列文档：通用基础与约定
└── series/
    └── 机械复刻系列/
        ├── README.md          系列主 page：两个实现、方法、复现
        ├── docs/              方法论文档与提示词原文（两版共用）
        ├── deepseek复刻/      DeepSeek 版（主推，00/01，自包含）
        └── glm5.3-flash复刻/  GLM 5.3-Flash 版（9 台）
            ├── pages/         18 个离线 HTML（互动页 + 影片页）
            ├── src/           完整源码（kit/ + upstream-teardown/ 快照）
            ├── covers/        9 台封面
            ├── references/    参考图与规格
            └── records/       复刻记录
```

## 通用约定

- **逐帧渲染**：画面只由帧号或时间决定，不读真实时钟；配乐读同一份时间线，音画不错位
- **数字同源**：屏上没有一个写死的读数，姿态、曲线、面板值全部由源码算出
- **来源如实**：原作者、链接、数据口径写清，每个数字标 frame / ref / guess；复刻模型写清
- **实现版本单独存放**：同一原作的另一次实现放 `series/<系列>/<模型名>复刻/`，自包含、不覆盖其他版本；通用约定不变，复刻模型与强调色在版本与通用文档中登记
- **不写密钥**，**不拷贝别人的源码**，引用别人的提示词必留来源与署名

完整版见 [`docs/通用基础与约定.md`](docs/通用基础与约定.md)。

## 许可

本仓库内容以 **MIT** 许可发布，见 [LICENSE](LICENSE)；
各版本的复刻模型、第三方素材、上游仓库快照与参考图来源，见 [NOTICE.md](NOTICE.md)。
