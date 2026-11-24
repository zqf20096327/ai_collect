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

## 作者与更新

| 角色 | 作者 | B 站主页 |
| --- | --- | --- |
| 插件作者 | **灵冻不冻** | [space.bilibili.com/516891894](https://space.bilibili.com/516891894) |
| 母题创作者 | **辞雪沐春** | [space.bilibili.com/1522948414](https://space.bilibili.com/1522948414/dynamic) |

**插件作者在 B 站有插件使用教学视频**：安装、三种母题分支（3D 场景 / 平面海报 / 短提示词）的区别、
角色与服装怎么选、画幅徽标怎么联动工作流，都有对应演示。

**版本更新进度也以 B 站动态为准** —— 新增母题、角色库同步、Bug 修复会先在那里说明，
比翻 commit 记录好读得多。

想反馈问题、点名某个角色的官方服装、或者投喂母题创意，欢迎到 B 站留言。
**感谢每一位使用者与反馈者的支持。**

## 目录

- [作者与更新](#作者与更新)
- [这是什么](#这是什么)
- [节点与用法链路](#节点与用法链路)
- [安装](#安装)
- [快速上手](#快速上手)
- [参数速查](#参数速查)
- [示例工作流](#示例工作流)
- [常见问题](#常见问题)
- [文档](#文档)
- [兼容性与已知限制](#兼容性与已知限制)
- [更新日志](#更新日志)
- [署名与来源](#署名与来源)
- [许可证](#许可证)

## 这是什么

Krea2 的「白垩光」是一套**一体化长文提示词**：25 段结构里母题（巨构场景 / 平面海报）决定整张画面的构图、材质、光位与排版语言，只能做有限替换。拆成随机池组合会立刻互相矛盾，所以本节点的设计是「**母题整块 + 有限替换位**」。

| 特性 | 说明 |
| --- | --- |
| 母题 | 553 条长文（3D 场景 312 / 平面海报 15 / 短提示词 226），每条自带画幅建议与中英文标题 |
| 角色 | 2432 位，跟 Anima-Wardrobe-V6 实时同步；没装则用内置快照 |
| 服装 | 8 套通用版型 + 角色官方预设 2447 套 + 服装库 98 套（内置 SFW 快照 10 类；装了 Anima 即读其完整库） |
| 服装替换 | 按部位（上装 / 下装 / 连衣裙 / 腿部 / 鞋 / 配饰）只写母题需要的部位；长文里各种旧服装写法自动让位 |
| 替换位 | 角色身份 / 画幅 / 服装材质 / 单品 / 画内排印文字 |
| 画幅联动 | 卡片徽标点一下 `竖 → 横 → 方 → 竖` 循环，同时切当前工作流画幅 |
| 输出 | 3 个 STRING：`提示词` / `自检报告` / `元数据` |
| 运行开销 | 单次装配约 1.7 ms，无模型、无显存占用 |
| 自检 | `python tests/run_all.py` → 23 项全绿 |

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

面板三页：**① 角色**（2432 位，分页 + 搜索 + 作品筛选 + 收藏）、**② 服装**（版型 / 角色预设 / 服装库）、**③ 场景**（553 原始母题，分类 + 标签筛选 + 勾选池 + 画幅徽标）。右侧常驻预览栏。选中即写回节点，不需要点「应用」。

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
[K2-Editorial] v1.15.3 已加载：['K2EditorialBuilder']
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
| `母题` | 首条 | 553 条；**新增母题要重启**才进下拉，HTTP 直传 id 不用 |
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
- **仓库体积约 45 MB**（角色立绘 22 MB + 母题预览 14 MB + 数据与代码 8 MB），clone 会比普通节点慢。没有这些图也能跑，只是面板无预览。
- **角色名残留自检**只对母题里登记过 `character` 的 30 条生效（29 条 Hatsune Miku + 1 条 Furina）；其余母题不写死角色，无需检查。

## 更新日志

### v1.15.4

- **修：换角色后仍带初音特征（用户反馈：约 1/4 母题出图还有青绿色双马尾）**。
  母题库是围绕 Hatsune Miku 写的，装配只整段换掉「身份句 / 发型段 / 服装段 / 色盘段」，
  但正文里还有一批**角色特征锚点**，它们不是独立段，于是一路留到输出：
  - `the outer twin-tail ends` / `aqua twintails` —— 连字符和无空格写法，旧正则只认 `twin tails`；
  - `full body from boots to hair ornaments` —— 取景用「发饰」当身体上限；
  - `her face, eyes, hands and hair ornaments must stay readable` —— 可读性锚点；
  - `both aqua eyes clearly visible` —— 写死的 Miku 瞳色；
  - 护盾里的 `no duplicate Miku` / `no missing twin tails` —— 负面词反而召唤青绿双马尾；
  - `virtual-singer stillness` 与 tag 流里的 `virtual singer`。
  现在统一由 `neutralize_residual_traits()` 在装配末尾中性化（角色是 Miku 本人时原样跳过）。
- **修：短提示词母题不换角色特征**。`k2s_*` 这类 tag 流母题只做名字替换，正文
  `1girl, hatsune miku, ... teal eyes, virtual singer` 原样留下；名字替换还区分大小写，
  小写 tag 匹配不到。现在统一走同一套清洗，并把服装上的 `teal trim` 换成目标角色主色。
- **修：Miku 本人被误伤**。双马尾判定只认 `twin tail` 这一种写法，Anima 那套写
  `worn in twintails` → 认不出 → 把 Miku 的双马尾中性化成 `long hair strands`。
  换成 `has_twin_tail()` 覆盖所有写法。
- **新增：短提示词自动套角色官方服装**。`k2s_*` 这类 tag 流母题自带的是 Miku 的服装 tag
  （`detached sleeves` / `black thighhighs`）。换角色且没手选服装时，现在自动套该角色的
  **官方服装预设**（Anima `character_outfits` 的 `default`），并按 tag 粒度整组替换 ——
  逐条摘除会被 `swap_garments` 的 limit 截断，留下半套。同时补了
  `thighhigh / kneehigh / pantyhose / leggings` 等腿部名词（原先不在 `GARMENT_NOUNS` 里，
  换装后过膝袜一直留在提示词里）。手选单品仍然优先，不会被自动套用覆盖；
  场景 / 海报分支不套（服装段本来就由版型模板接管）。
- **画内文字跟着换角色名**：母题里印在画面上的 `HATSUNE MIKU` 标签会换成目标角色名，
  大小写风格跟随原文（全大写 → 全大写）；用户手填的「画面英文文字」不受影响。
- **修：`furina` 的护盾抄了 Miku 的否定项**（`no Miku, no aqua twin tails`），
  选她出图会主动召唤青绿双马尾。
- **修：Anima 桥接兜底色是 Miku 的**。认不出的瞳色一律兜到 `aqua`（缝线 / 轮廓全青绿），
  现在改为「认不出瞳色 → 用发色 → 再兜中性象牙白」。
- 回归 23 项（新增「换角色后不留原角色特征」「短提示自动套官方服装 + 画内文字换名」）。
- 联机验证（真实工作流 `Krea2-白垩光标准档.json`，8 步 turbo）：同一母题
  `k2x_veil_fall_a` 分别用 Miku / Cirno 出图 —— Miku 保留青绿双马尾，Cirno 出蓝发 + 冰翼 +
  蓝裙，无任何初音特征；`k2s_cx_023` 自动套蓝裙；手选「露肩针织 + 百褶裙」时按手选出图。
- 文档：新增[「作者与更新」](#作者与更新)一节（插件作者 B 站教学视频与更新进度、母题创作者主页），
  回归项数同步为 23；`presets/seeds_motifs.json` 的溯源路径改回相对路径，不再写入本机路径。

### v1.15.3

- **修：所有格形式的旧衣服**（`the coat's collar` / `her dress's hem`）。上一轮只处理
  `her coat`，带 `'s` 的漏了 —— 实测「废墟·地面光带」里 `One small wooden toggle at the
  coat's collar` 活下来，模型就给她加了一件外套。现在统一改成 `the outfit's`。
- 联机验证（真实工作流 `Krea2-白垩光标准档.json`，8 步 turbo，3:4 / 16:9）：
  影院门外 / 忧郁肖像 / 晨曦·暗调 三个点名母题全部换成所选晚礼服；
  随机抽 5 条（2 场景 + 2 短提示 + 1 海报）也全部生效。

### v1.15.2

- **修：影院门外 / 忧郁肖像 这类短提示词母题，换了服装也不生效**。三个具体问题：
  - 母题只写了 `coat collar pulled up` 这种**裸名词短语**（没有 her、没有动词）—— 之前被
    「必须提到她才处理」的规则挡住，外套领子一直留在提示词里，把所选上衣压掉了。
    现在裸名词短语不受该限制（成句的仍然要求提到她，避免误伤场景描述）。
  - **部位判定只看「母题提到哪些部位」**：影院门外只提了外套领子 → 判定为「只要上半身」
    → 整条裙子直接不写，出图自然看不到下装。现在改成**取景决定写哪些部位**（特写才只写上半身，
    其余默认写「上装 + 下装」），母题描述只用来补腿 / 鞋 / 配饰。
  - **全篇服装名替换的时机错了**：替换放在开头，新写进去的单品又被后面的句子处理当成
    「旧衣服」摘掉，成品里一件衣服都没有。现在放到最后执行，并加兜底：
    只要动过服装，成品里就必须出现所选单品。
- 全量 553 条 × 两套服装：断句 0、空清单 0、**每条都有服装句**；「只要上半身」从 34 条降到 25 条
  （多出来的是取景没有明确特写线索的母题，宁可多写一套下装也不丢裙子）。
- 回归测试 21 项。

### v1.15.1

- **修：换装后旧衣服还在（第三轮）**。之前的改写只认「整句列举服装」，实测还有三种写法漏掉：
  - **内联介词短语**：`standing on the grassy slope … at night in a yukata` —— 浴衣母题换了针织，
    出图还是浴衣。现在改成 `in the selected outfit`（`in front of her boots` 这类空间短语有
    白名单挡着，不会被误改）。
  - **所有格**：`the hem of her yukata` / `her wooden sandals` —— 按部位换成 `her outfit` /
    `her footwear` / `her top`。
  - **全篇反复点名**：`white top / dark skirt` 在 9 个段落里出现，只改服装段等于没改。
    现在从母题里提取「这身衣服的标准叫法」，全文统一换成所选单品（按部位配对）；
    袖口 / 下摆 / 领子这类部件词不参与整名替换。
- **服装名词表补漏**：`top` / `qipao` / `yukata` / `parka` / `blazer` / `sweatshirt` 之前不在表里 ——
  整条母题写 `white top` 也识别不出来。
- 全量 553 条 × 两套服装扫描：断句/空清单 0；旧服装残留从 19 条降到 13 条
  （剩下的是「衣架道具 / 四面反射各穿一套 / 伪身份段 / 部件细节」，有意保留）。
- 回归测试 21 项（新增「内联 / 所有格 / 全篇服装名」一项）。

### v1.15.0

- **按部位换装**：服装库和角色官方服装都按 `上装 / 下装 / 连衣裙 / 腿部 / 鞋子 / 配饰`
  六类拆分，**只写母题自己描述到的部位**。
  以前整套写入会把取景拉远：方形专辑是上半身特写，却写进了「百褶裙 + 乐福鞋」，
  模型就去补腿和脚；展纸母题写的是连衣裙、没写鞋，补了乐福鞋后构图变成坐窗台双腿垂下。
- **判定口径**：以母题正文的服装描述为准（写了哪些部位就换哪些）；母题完全没写服装时，
  退回取景线索（`close-up / upper chest` → 只上装，`full body / her feet` → 全套）。
- **空缺部位不写**：母题要鞋但这套没有鞋 → 该部位留空，不硬凑（角色官方服装同理）。
- **几条保护**：头饰（`top hat` / `beret`）永远保留——戴在头上、不进画面下方，且是识别度
  的一部分；只提到下装的母题会顺带补上装（否则上身留空）；`holding umbrella` / `sunny day`
  这类动作天气 tag 直接丢弃，`knitwear` / `long sleeves` 这类修饰词挂到主体上装。
- 效果：34 条母题判为「上半身」，519 条含下半身；全量 553 条 × 两套服装扫描，
  没有出现空清单或断句；回归测试 20 项。

### v1.14.1

- **修：海报 / 方形专辑母题换不掉服装**。除了「She wears …」这一类，实测还有三类写法
  会让旧衣服照样画出来，现在一并覆盖：
  - **衣服自己做主语**（`A dark navy coat hangs open over it.`）—— 同段已有服装清单就整句删掉；
  - **整句/整段都在讲服装**（海报 `Let the clothing behave like clothing: the ivory cardigan…`）
    —— 整句换成本次所选单品；
  - **tag 流里夹着的裸单品**（`sailor school uniform, pleated skirt, …`）—— 只摘掉那几个子句。
- **修：角色身份句里写死的原作服装**。`furina` 的 identity 写着
  `her recognizable … ceremonial outfit`、guard 钉着 `no missing top hat`，两句都比服装
  指令更硬 —— 所以选了露肩针织，出图还是全套 Fontaine 礼仪服 + 高帽。
  现在选单品时会自动剥掉身份句 / 护盾里的原作服装（手写角色可用
  `identity_plain` / `guard_plain` 精确指定；生成角色自动剥离 `detached sleeves` 这类签名）。
- **海报不再随机套版型**：指定单品 + 版型「自动」时直接按单品写平面服装段，
  不再随机抽「利落西装式 / 宫廷礼服」那套（抽中了会跟所选单品打架）。
- **修：母题自带硬换行导致身份句替换静默失败**（38 条母题带段内换行）。
  旧正则 `Preserve [^\n]*?\.` 跨不过换行，原文身份句原样留下 —— 那几条母题换角色等于没换，
  服装自然也换不掉。
- **保守化**：长篇巨构分支（scene）里 `scarf` / `cloak` / `cape` 常是画面主体而不是穿在身上的，
  只对「her dress is heavy cotton」这类材质指派下手，不做整句替换，避免把构图描述整段换掉。
- 已知保留（有意不改）：背景**衣架上的衣服 / 道具服装**、**四面反射各穿一套**这类设计项、
  以及伪身份段（`her identity must read at a glance: …`）里的服装列表 —— 后者交给身份锚点句压。
- 回归测试 19 项（新增「身份句 / 护盾 / 海报版型三处让位」）。

### v1.14.0

- **修：选了服装库服装，出图还是母题自带那套**。原先单品句是追加到**全文末尾**的，
  而母题正文里本来就写着「She wears a … spaghetti-strap dress」——贴着角色、位置更靠前，
  模型两套都读，结果偏母题那套（或干脆混成一件）。
  现在指定单品时**原地改写**母题自带的服装枚举：`She wears a … dress.` →
  `She wears only these garments: 露肩针织, 百褶裙, 乐福鞋.`，主语与动词沿用原文，
  语法不破、位置不变，服装仍然贴着角色。
- 覆盖到**三个分支**：短提示词（含 tag 流的 `wearing …`）、长篇场景（服装句常藏在
  **机位段**里，例如 `k2x_*` 系列）、平面海报。母题完全没写服装时，改成紧跟「身份锚点段」
  插入，而不是扔到末尾。
- 单品里混着的**姿势类 tag**（Anima 服装库里的 `crossed legs` 等）不再写进「她穿着…」，
  姿势交回母题；命中的 tag 会在自检报告里列出来。
- 所选单品里没有裙装时，正文残留的 `the dress` 统一改称 `the outfit`，避免两套衣服并存。
- 顺带修：短提示词分支选「保持母题原样」时会写出 `Render Miku in a keep with …` 这种病句，
  现在直接跳过版型句。
- 不选单品时输出与 v1.13.0 **逐字节一致**（19908 组参数组合比对零差异）。
- 回归测试 18 项（新增「服装库单品：就地覆盖母题自带服装」）。

### v1.13.0

- **场景画幅徽标可点**：③ 场景页的每张卡片上，画幅角标变成按钮，点一下 `竖 → 横 → 方 → 竖` 循环，
  同时切换当前工作流的画幅参数。原来只能看，现在能改。
- **画幅改到哪存哪**：改动写进独立覆盖层 `presets/user_motif_aspect.json`（在 `.gitignore` 里），
  优先级高于 `manifest.json` 的推荐值；删掉那一条就退回推荐值。构建脚本重跑不会覆盖你的改动。
- **母题库扩到 553 条**（3D 场景 312 / 平面海报 15 / 短提示词 226），比 v1.12.0 多 158 条，
  配套缩略图补齐。
- 回归测试 17 项（新增「画幅覆盖层读写」「徽标三态循环链」两项）。

### v1.12.0

- 首次开源发布。

## 署名与来源

- **本插件**：灵冻不冻 · [@lingdongbudong](https://github.com/lingdongbudong) · [B 站主页](https://space.bilibili.com/516891894)（插件使用教学视频与更新进度都在这里）。作者另有 [Comfyui-Anima-Wardrobe-V6](https://github.com/lingdongbudong) 与 Krea2-Portrait 系列。
- **母题库**：来自 **辞雪沐春** · [B 站主页](https://space.bilibili.com/1522948414/dynamic) 提供的参考素材 —— `k2-baieguang` / `k2-chenxiguang` 两个提示词集，以及一套 32 张「MIKU - 未来科幻风格」成品图，其内嵌提示词被拆段、重写并扩展成 553 条母题库。作者口头同意再分发，未指定具体许可文本；**若作者后续声明许可，以其声明为准**。
- **角色数据与立绘**：快照自 Comfyui-Anima-Wardrobe-V6。
- **角色与作品名称**：版权归各自权利人，本项目仅作描述性标识，不主张任何权利。

## 许可证

代码以 **GNU AGPL-3.0** 发布，全文见 [LICENSE](LICENSE)。

上游素材的授权状态见 [LICENSE 末尾的 Additional attribution 段](LICENSE) —— 该段不属于许可条款，仅作来源声明。**如果你的使用场景无法接受 AGPL（例如闭源分发），请先联系原作者确认素材授权范围。**
