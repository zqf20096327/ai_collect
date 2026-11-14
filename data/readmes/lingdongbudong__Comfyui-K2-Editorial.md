# Comfyui-K2-Editorial

**Krea2「白垩光 / 未来奢华编辑主视觉」长文提示词的自动装配节点** —— 选角色、母题、画幅、服装，输出 1500–2700 词的英文长提示词。一个母题决定整张画面，不是 tag 随机池。

![ComfyUI](https://img.shields.io/badge/ComfyUI-0.42.x-2f6f4e?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square)
![License](https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat-square)
![Dependencies](https://img.shields.io/badge/dependencies-none-success?style=flat-square)
![Offline](https://img.shields.io/badge/runtime-100%25%20offline-informational?style=flat-square)

> ⚠️ **使用边界**：本插件只生成**文字提示词**，不生成图片，运行时零联网、不调用任何大模型。
> 内置角色数据与立绘快照来自 [Comfyui-Anima-Wardrobe-V6](https://github.com/lingdongbudong)，
> 角色名与作品名（初音未来、原神、Fate、蔚蓝档案、明日方舟、碧蓝航线、鸣潮、绝区零、崩坏：星穹铁道等）
> **归各自权利人所有**，此处仅作提示词组装用的描述性标识，不代表任何授权或关联。
> 服装库已精简为 SFW（L0–L1，剔除 `nsfw_outfit` 分类），不含成人向条目。
> 若你所在地区对 AI 生成内容有额外限制，请自行确认合规后再使用。

## 目录

- [这是什么](#这是什么)
- [节点与用法链路](#节点与用法链路)
- [安装](#安装)
- [快速上手](#快速上手)
- [参数速查](#参数速查)
- [示例工作流](#示例工作流)
- [常见问题](#常见问题)
- [文档](#文档)
- [兼容性与已知限制](#兼容性与已知限制)
- [署名与来源](#署名与来源)
- [许可证](#许可证)

## 这是什么

Krea2 的「白垩光」是一套**一体化长文提示词**：25 段结构里母题（巨构场景 / 平面海报）决定整张画面的构图、材质、光位与排版语言，只能做有限替换。拆成随机池组合会立刻互相矛盾，所以本节点的设计是「**母题整块 + 有限替换位**」。

| 特性 | 说明 |
| --- | --- |
| 母题 | 395 条长文（3D 场景 275 / 平面海报 15 / 短提示词 105），每条自带画幅建议与中英文标题 |
| 角色 | 2432 位，跟 Anima-Wardrobe-V6 实时同步；没装则用内置快照 |
| 服装 | 8 套通用版型 + 角色官方预设 2447 套 + 服装库 98 套（11 类） |
| 替换位 | 角色身份 / 画幅 / 服装材质 / 单品 / 画内排印文字 |
| 输出 | 3 个 STRING：`提示词` / `自检报告` / `元数据` |
| 运行开销 | 单次装配约 2.4 ms，无模型、无显存占用 |
| 自检 | `python tests/run_all.py` → 15 项全绿 |

三种母题分支的写法不同，节点会自动适配：

- **scene（3D 场景）** — 20–25 段，带机位、材质分区、色盘百分比、五层景深
- **poster（平面海报）** — 保留版式与大标题，角色按海报语法适配
- **short（短提示词）** — 4–8 段短句，只换身份并追加一句服装说明

## 节点与用法链路

```
[★ K2 长文出题 · 白垩光]  ──提示词(STRING)──▶  CLIP Text Encode (positive)
        │                                    ──▶  采样 / 画幅参数节点
        └──元数据(STRING)──▶  PreviewAny（可选，排查用）
```

节点在 `Krea2/提示词` 分类下，画布上显示两行摘要（角色 · 画幅 · 服装 / 母题 · 种子）。
五个核心控件在节点上**折叠隐藏**，只在「⚙ 打开设置面板」里选 —— 同一个设置只留一个入口，但隐藏不影响工作流序列化。

面板三页：**① 角色**（2432 位，分页 + 搜索 + 作品筛选 + 收藏）、**② 服装**（版型 / 角色预设 / 服装库）、**③ 场景**（395 原始母题，分类 + 标签筛选 + 勾选池）。右侧常驻预览栏。选中即写回节点，不需要点「应用」。

## 安装

需要 ComfyUI **0.42.x** 与 **Python ≥ 3.10**（实测 3.13），无第三方依赖，不需要 `pip install`。

**方式一：git clone**

```bash
cd <ComfyUI>/custom_nodes
git clone https://github.com/lingdongbudong/Comfyui-K2-Editorial.git
```

**方式二：下载 ZIP**

在仓库页点 `Code → Download ZIP`，解压到 `<ComfyUI>/custom_nodes/Comfyui-K2-Editorial/`（注意目录名保持一致）。

装完**重启 ComfyUI**，启动日志出现下面这行即成功：

```
[K2-Editorial] v1.12.0 已加载：['K2EditorialBuilder']
```

## 快速上手

1. 画布空白处右键 → `Krea2/提示词` → **★ K2 长文出题 · 白垩光**
2. 点节点上的 **⚙ 打开设置面板** → ③ 场景选一条母题（会自动带出推荐画幅）
3. ① 角色选人 → 关面板 → 把 `提示词` 接到 `CLIP Text Encode` 的 positive → 排队

最短验证：`python tests/run_all.py --http` 能跑通，说明插件与服务都正常。

## 参数速查

常用项列在这里，**完整参数表见 [docs/USAGE.md](docs/USAGE.md#参数全表)**。

| 参数 | 默认 | 说明 |
| --- | --- | --- |
| `随机种子` | `0` | 勾了「每次重随机」时本项无效 |
| `每次重随机` | `true` | 关闭后同种子可复现；固定种子下改母题库会自动失效缓存 |
| `角色` | `miku` | 字符串，不是下拉（2432 条做成 combo 会让 `/object_info` 膨胀） |
| `母题` | 首条 | 395 条；**新增母题要重启**才进下拉，HTTP 直传 id 不用 |
| `画幅` | `16:9` | 8 种；海报 / 短提示词分支保留原版式写法 |
| `服装` | `自动（跟随母题）` | 也可选 8 套版型或「保持母题原样」 |
| `单品` | 空 | `char:<预设 id>` 或 `lib:<服装库 id>`，叠在版型段之后 |
| `覆盖提示词` | 空 | 非空则跳过装配，直接输出这段文本 |
| `画面英文文字` / `画面不显示英文` | — | 控制画内排印文字 |
| `角色随机池` / `场景随机池` | `关闭` | ⚠ 三个随机池必须在控件末尾，别往前插 |

## 示例工作流

| 文件 | 用途 | 额外依赖 |
| --- | --- | --- |
| `workflows/K2-白垩光_出题节点已接线(参考).json` | 最小接线示例：出题节点 → 文本编码 | 无 |
| `workflows/Krea2-白垩光标准档.json` | 完整出图链路（采样 / 参数 / 保存） | 需 XB_ToolBox 的 `XB_ImageParamsMaster` |
| `workflows/Krea2-平面设计档.json` | 海报分支链路，走平面图形语法 | 同上 |

前两个工作流里的 `XB_ImageParamsMaster` 是可选依赖，没有它也能跑（画幅由节点输出决定）。

## 常见问题

**Q：装完节点列表里找不到？**
看启动日志有没有 `[K2-Editorial] v... 已加载`。没有的话检查目录名是否为 `Comfyui-K2-Editorial`（`__init__.py` 必须直接在目录下，不能套一层）。

**Q：母题下拉是空的 / 只有一条？**
`presets/seeds_motifs.json` 与 `seeds_extra.json` 缺失或损坏。跑 `python tests/run_all.py` 会明确报出哪份文件读不出来。

**Q：角色页只有 2 个人（miku / furina）？**
说明既没装 Anima-Wardrobe-V6，内置副本也没被读出来。检查 `presets/anima/anima_v4_characters.json` 与 `thumbs/anima/` 是否都在；或用 `K2ED_ANIMA_SOURCE=bundle` 强制走内置。

**Q：改了母题正文，出图没变？**
母题内容在 `presets/seeds_*.json`，改完必须**重启** ComfyUI（缓存与 combo 列表都在进程内存里）。

**Q：自检报告显示 `!! 装配失败: ...`？**
首行就是原因，常见是角色 id 不存在（手写 key 只有 `miku` / `furina`，其他要用 Anima 的完整 tag）。

其余问题见 [docs/USAGE.md 的 FAQ（20+ 条）](docs/USAGE.md#常见问题-faq)。

## 文档

| 文档 | 内容 |
| --- | --- |
| [docs/USAGE.md](docs/USAGE.md) | 完整使用说明：安装细节、参数全表、面板逐项、5 个典型示例、20+ 条 FAQ、限制 |
| [docs/MAINTAINERS.md](docs/MAINTAINERS.md) | 维护者指南：改代码前必读的红线、目录结构、数据链路、测试基线、发版流程 |
| [README.md](README.md) | 本文件（门面） |

## 兼容性与已知限制

- **ComfyUI 0.42.x** 实测通过；前端依赖 `app.registerExtension` 与 `LiteGraph`，更老的版本可能缺 `widget.inputEl`。
- **Python ≥ 3.10**（用了 `X | None` 注解 + `from __future__ import annotations`）。
- **新增控件必须加在 `INPUT_TYPES["optional"]` 末尾**：放进 required 或插到中间，会让老工作流的 `widgets_values` 错位、丢掉整张输出。
- **禁止在节点代码里 `raise SystemExit`**：它继承 `BaseException`，ComfyUI 的 `execution.py` 接不住 —— 实测会让 8188 端口仍 LISTENING 但整个 HTTP 服务不再响应，只能重启。一律用 `ValueError` 子类。
- **固定种子 + 改数据文件**：`IS_CHANGED` 已纳入母题库 / 版型 / 收藏 / 勾选池的指纹与代码 mtime，改盘会自动失效输出缓存。
- **仓库体积约 47 MB**（角色立绘 29 MB + 母题预览 11 MB + 数据 7 MB），clone 会比普通节点慢。没有这些图也能跑，只是面板无预览。
- **角色名残留自检**只对母题里登记过 `character` 的 30 条生效（29 条 Hatsune Miku + 1 条 Furina）；其余母题不写死角色，无需检查。

## 署名与来源

- **本插件**：灵冻不冻 · [@lingdongbudong](https://github.com/lingdongbudong)。作者另有 [Comfyui-Anima-Wardrobe-V6](https://github.com/lingdongbudong) 与 Krea2-Portrait 系列。
- **母题库**：来自 **辞雪沐春** 提供的参考素材 —— `k2-baieguang` / `k2-chenxiguang` 两个提示词集，以及一套 32 张「MIKU - 未来科幻风格」成品图，其内嵌提示词被拆段、重写并扩展成 395 条母题库。作者口头同意再分发，未指定具体许可文本；**若作者后续声明许可，以其声明为准**。
- **角色数据与立绘**：快照自 Comfyui-Anima-Wardrobe-V6。
- **角色与作品名称**：版权归各自权利人，本项目仅作描述性标识，不主张任何权利。

## 许可证

代码以 **GNU AGPL-3.0** 发布，全文见 [LICENSE](LICENSE)。

上游素材的授权状态见 [LICENSE 末尾的 Additional attribution 段](LICENSE) —— 该段不属于许可条款，仅作来源声明。**如果你的使用场景无法接受 AGPL（例如闭源分发），请先联系原作者确认素材授权范围。**
