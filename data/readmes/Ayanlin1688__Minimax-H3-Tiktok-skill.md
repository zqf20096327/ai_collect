# MiniMax H3 · TikTok Shop 全类目实拍带货提示词 Skill

> 让 MiniMax H3（海螺 02）生成的带货视频**不再一眼假** —— 不用多手、不悬空、不穿模、不蜡像脸。

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#版本历史)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-MiniMax%20H3%20%2F%20Hailuo%2002-orange.svg)](#)
[![Market](https://img.shields.io/badge/market-TikTok%20Shop%20US-black.svg)](#)
[![Sponsor](https://img.shields.io/badge/☕-%E8%B5%9E%E8%B5%8F%E6%94%AF%E6%8C%81-yellow.svg)](#赞赏支持)

---

## 这是什么

一套给 **MiniMax H3 视频模型**用的提示词工程规范。

你把产品图丢给它，它输出**可以直接粘贴进海螺 AI**的带货视频提示词 —— 而且写出来的提示词，能避开 AI 视频最常见的 20 多种翻车。

不是又一个"提示词模板"。它是**用真实翻车视频一轮一轮逆向修出来的规则集**：

```
第 1 轮  看到第三只手、产品分身      → 加只手守恒、单实例锁
第 2 轮  看到产品悬空、幻影、蜡像脸  → 加接触锁、单动作单运镜、去蜡人化
第 3 轮  看到红脸、折叠态错乱、乱码  → 加异色隔离、展态锁定、屏显不可读
第 4 轮  发现"太干净"也是假          → 架构升级：七层真实感正向模型
第 5 轮  看到固定痣、穿模、开头没人看 → 加随机人物池、穿模防护、前三秒钩子
```

**每一轮都有逐帧取证，不是拍脑袋加规则。**

---

## 解决什么问题

| AI 带货视频的典型翻车 | 本 Skill 的对策 |
|---|---|
| 人物长出第三只手 | 铁律 B 只手任务守恒 + J 手—物耦合 |
| 产品凭空悬浮 | 铁律 I 接触面锁定 + L 悬挂物微动 |
| 产品在切镜间变形/分身 | 铁律 E 结构锁 + F 单实例锁与连续态锁 |
| 手指穿进玻璃瓶、灯体 | 铁律 Y 穿模防护（写清手指在前还是在后） |
| 每张脸同一位置长同一颗痣 | 铁律 M 随机人物池 A–F（痣改为可选项） |
| 脸像蜡像、眼睛死黑 | 铁律 M 去蜡人化（含眼睛虹膜 + 小方形高光） |
| 满面油光、塑料反光 | 铁律 M/N（禁 redness、异色污染隔离） |
| 画面太干净，一眼渲染图 | 铁律 R 去干净化底线（噪点/高光溢出/白平衡/灰尘指纹/杂物） |
| 口播像广告配音 | 铁律 T 说不完美的话（卡壳/换气/音量不均/句尾衰减） |
| 人物站着干说、手在空中比划 | 铁律 AA 人物有事可干 |
| 前 3 秒没人看下去 | 铁律 Z 前三秒钩子 |
| 产品举起悬空、无接触 | 铁律 I 接触面锁定（磁吸/挂钩/手持各有专属句式） |
| 画面出现乱码字幕、假促销贴纸 | 铁律 P/X 屏显不可读 + 文字分层 |
| 台词说了违规极限词 | S1–S8 特殊监管品类合规层 |

---

## 核心设计：两套系统叠在一起

```
┌─────────────────────────────────────────────────────────────┐
│  第一层：正向真实感模型（把画面做"脏"、做"乱"、做"不完美"）    │
│  R 去干净化 · S 单机位 · T 说话不完美 · U 动作不完美          │
│  V 场景杂乱 · W 生活切片                                     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  第二层：反缺陷铁律（封堵解剖与结构错误）                     │
│  A–Q 共 17 条：零否定词 / 只手守恒 / 结构锁 / 接触锁 …        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  第三层：全类目路由                                          │
│  T 档位（尺寸）× C 品类（交互）× S 监管（合规）              │
└─────────────────────────────────────────────────────────────┘
```

> **为什么顺序是这样**：AI 画面"太干净"本身就是假。
> 只做反缺陷，画面依然一眼 AI；先把脏乱不完美写进去，再封堵错误，才像实拍。

---

## 27 条铁律总览

### 反缺陷层（A–Q）

| # | 铁律 | 一句话 |
|---|---|---|
| A | 正向段零否定词 | 写 `no third hand` 反而会生成第三只手 |
| B | 只手任务守恒 | 任何时刻画面 ≤2 个手部接触点 |
| C | 屏幕坐标 + 物体锚点 | 禁用 `left/right hand`，改用画面几何方位 |
| D | T1–T5 形态档位 | 尺寸决定"单手能不能边拿边按" |
| E | 产品结构锁 | 逐项复述比例/颜色/按键/端头/线缆/工艺 |
| F | 单实例锁 + 连续态锁 | 每个切镜交代"同一件东西从哪来" |
| G | 原生手机直出光影 | 去 cinematic / bokeh / rim light |
| H | 表情去夸张 + 口型守恒 | 台词词数 ≤ 秒数 × 2.5 |
| I | 接触面锁定 | 写清"哪个面压在哪个面上" |
| J | 手—物耦合 | 写清"手抓哪段 + 产品相对手的位置" |
| K | 单动作单运镜 | 触碰瞬间镜头必须 static（治残影） |
| L | 悬挂物微动 | 约 2° 一次微摆（治"完美静止=悬空"） |
| M | 去蜡人化 | 随机人物池 + 五锚点 + 禁 redness |
| N | 异色污染隔离 | 鲜红产品会把脸染红，必须写隔离句 |
| O | 展态锁定 | 可折叠品必须声明"完全展开" |
| P | 小屏显不可读 | 指定数字必出 183/188 乱码 |
| Q | 构图边界与穿模防护 | 头部完整入画、产品末端留一掌宽 |

### 正向真实感层（R–W）

| # | 铁律 | 一句话 |
|---|---|---|
| R | 去干净化底线 ★★★ | 噪点/高光溢出/白平衡/灰尘指纹/5–8 件杂物，5 项至少 4 项 |
| S | 单机位少切镜 | 15 秒最多 2–3 镜，禁 dolly/gimbal/tripod |
| T | 说不完美的话 ★★★ | 卡壳/换气/自我更正/音量不均/句尾衰减 |
| U | 动作不完美 | 打滑重抓、拇指没按到、角度重调 |
| V | 场景杂乱底线 | 5–8 件无关杂物，声明全程不动 |
| W | 生活切片而非广告脚本 | 取消显式 CTA，在动作中间结束 |

### 新增层（X–AA）

| # | 铁律 | 一句话 |
|---|---|---|
| X | 文字分层 | 禁新增字幕；保留参考图原文字；屏显不指定数字 |
| Y | 穿模防护 | 写清手指在产品前面还是后面 |
| Z | 前三秒钩子 | 动作已到一半 + 可见阻力 + 产品第 1 秒入画 |
| AA | 人物有事可干 | 每镜有可见物理任务，禁空手比划 |

---

## 全类目怎么工作：T × C × S 三层路由

**不靠穷举品类名单**，而是任何商品都先落进三层坐标：

### 第 1 步 · T 档位（尺寸）

| 档位 | 判定 | 交互语法 |
|---|---|---|
| T1 微型 | < 10cm | 单手握 + 同手拇指按 |
| T2 小型 | 10–18cm | 单手握 + 另一手食指 |
| T3 中型 | 18–35cm | 必须先放置/夹持再操作 |
| T4 长条形 | > 35cm 或长宽比 > 4.5 | **固定 → 松手 → 单手操作** |
| T5 超大件 | 需双臂 | 只抱持/放置/拍打 |

### 第 2 步 · C 品类（交互语法）

| 代号 | 品类 | 专属要点 |
|---|---|---|
| C1 | 日用百货 | 开合状态必须显式声明 |
| C2 | 美妆个护 | 皮肤细描 + 指腹接触 + 用量/轨迹/终点 |
| C3 | 车载汽配 | 车辆中性化 + 安装位具体化 + 真实脏旧 |
| C4 | 时尚配件 | 反射锚定真实环境物 |
| C5 | 穿戴 | **T 档失效**，改用身体锚点 |
| C6 | 食品饮料/清洁 | 倾倒写液面变化、喷洒写雾形落点 |
| C7 | 强反光透明 | 每个反射锚定真实物体、屏幕暗态 |
| C8 | 多人协作 | 逐人计数（每人 ≤2）+ 松手接手顺序 |

### 第 3 步 · S 监管类目（额外合规）

| 代号 | 品类 | 额外红线 |
|---|---|---|
| S1 | 保健品 | 禁疾病宣称 + FDA 免责声明 |
| S2 | 医疗器械 | 只能用 wellness/relief/comfort |
| S3 | 化妆品功效 | 只能到"外观"层，禁伪造前后对比 |
| S4 | 儿童母婴 | 禁绝对安全宣称 + 禁替代监护 |
| S5 | 锂电池 | 禁"永不爆炸" + 禁虚假容量 |
| S6 | 食品接触 | 禁疗效宣称 + 禁无依据"食品级" |
| S7 | 汽车安全件 | DOT/SAE/FMVSS 不得虚构 |
| S8 | 刀具危险品 | 部分州禁售 + 禁对人演示 |

> **实测**：20 个跨品类商品（灯/保鲜机/墨镜/精华/血压计/餐椅/折叠桌/启动电源/折叠刀/瑜伽垫/手表…）全部成功落位。

---

## 快速开始

### 三步

**① 上传产品图**（建议 2–3 张：正面含键位 / 背面含结构 / 细节特写）

**② 复制下面这段，替换中括号内容**

```text
调用 minimax-h3-tiktok-ecommerce，为这款【产品名】生成 15 秒 TikTok 美区带货提示词。

【品类】C__（1百货/2美妆/3车配/4时尚配件/5穿戴/6食品清洁/7反光透明/8多人）
【形态】T__（1微型/2小型/3中型/4长条形/5超大件）
【监管】S__（保健品/医疗/化妆品功效/儿童/电池/食品接触/车安全件/刀具；无则写"通用"）
【场景】美国家庭真实场景：厨房台面 / 客厅沙发 / 洗衣房 / 家用车库 / 餐桌 / 后院
【人物】从 persona-variation-pool.md 的 A–F 六组随机抽 1 组（不要固定痣）
【结构关键点】材质 / 颜色分布 / 按键形状位置 / 端头 / 线缆 / 表面工艺
【使用状态】完全展开 / 组装完成 / 已佩戴
【时长】15 秒

必须执行 Z 前三秒钩子、AA 人物有事可干、Y 穿模防护、M 人物随机不固定痣、
R 去干净化、T 说话不完美、产品一致性五锁；27 条铁律 + 36 项自检；双模输出。
```

**③ 拿到提示词，粘贴进海螺 AI**

上传同一组产品图 → 粘贴【单段 Master Prompt】→ 15 秒 / 9:16 → **一次生成 3 条挑 1 条**。

### 怎么确认调到了最新版

回复里必须出现这 4 个特征：

- ✅ 写出 **T / C / S** 三个代号
- ✅ 前 3 秒是**动作卡住/掉落/有人否定**，不是站着说话
- ✅ 出现**穿模防护句**（手指在产品前面还是后面）
- ✅ 人物**没有左颊固定痣** + 写明日晒色差/鱼尾纹

---

## 交付验收：真实感六问

生成后按这 6 问挑片，**任何一问不过就算假**：

| # | 问 | 不过说明 |
|---|---|---|
| 1 | 有噪点 / 高光溢出 / 白平衡不均吗？ | 画面太干净 |
| 2 | 有机身手臂疲劳微动吗？ | 像三脚架 |
| 3 | 场景有 ≥5 件无关杂物吗？ | 像样机图 |
| 4 | 产品有灰尘 / 指纹 / 磨损吗？ | 产品全新无瑕 |
| 5 | 说话有卡壳 / 换气 / 音量不均吗？ | 广告配音腔 |
| 6 | 手有打滑 / 没按到 / 重抓吗？ | 动作像机械臂 |

---

## 目录结构

```
.
├── SKILL.md                              ★ 核心规范：27 条铁律 + 36 项自检
├── universal-master-template.txt          ★ 全类目通用主模板（固定脚手架 + 6 槽）
├── prompt-template.txt                    用户输入卡（含三大品类填写示例）
├── README.md                              本文件
├── LICENSE                                MIT
├── CHANGELOG.md                           更新日志（版本号来源）
│
├── assets/
│   └── sponsor-qr.jpg                     赞赏码（README 引用）
│
├── references/                            规则库与诊断档案
│   ├── persona-variation-pool.md          ★ A–F 六组随机人物池（治固定痣）
│   ├── clipping-hook-and-scene-fix.md     ★ 穿模 + 前三秒钩子 + 美国家庭场景库
│   ├── real-footage-realism-model.md      ★ 七层真实感正向模型
│   ├── special-category-compliance.md     ★ S1–S8 特殊监管品类合规
│   ├── category-extension-grammar.md      C1–C8 品类扩展语法
│   ├── universal-product-interaction-grammar.md   T1–T5 档位 + 4 类交互模板
│   ├── h3-anti-artifact-root-causes.md    第 1 轮病理诊断（多手/分身/油光）
│   ├── contact-ghosting-waxface-fix.md    第 2 轮病理诊断（悬空/幻影/蜡人）
│   ├── v3-colorbleed-state-lock.md        第 3 轮病理诊断（红脸/折叠态/乱码）
│   ├── viral-script-vault.md              8 大爆款剧本金库
│   ├── tiktok-compliance-rules.md         美区合规防封准则
│   ├── liveness-acting-guide.md           活人感表演体系
│   ├── benchmark-video-realism-spec.md    实拍标杆光学规范
│   ├── minimax-h3-syntax.md               H3 官方 Context-IR 语法速查
│   └── case-study-example.md              完整实战案例
│
├── scripts/
│   └── fetch_tiktok_trends.py             8 大爆款原型匹配与分镜骨架生成
│
└── tools/
    ├── sync-to-github.ps1                 一键同步：推云端 + 镜像到本机技能库
    └── build-package.ps1                  一键打包：按 CHANGELOG 版本号出 zip + SHA256
```

---

## 和 MiniMax H3 官方规范的对齐

已通过自动审计 **11/11**：

| 官方规范项 | 状态 |
|---|---|
| 参考图对齐语句严格格式 | ✅ |
| 三字段顺序（integrated / soundscape / music） | ✅ |
| `[Shot 1]` 不带时间戳 | ✅ |
| 时间戳严格递增且 < 总时长 | ✅ |
| 切镜动词仅用官方 5 个白名单 | ✅ |
| `<d>[Language] "..."</d>` 标签闭合 | ✅ |
| 说话角色固定编号 | ✅ |
| 正向段零否定词 | ✅ |
| soundscape 1–4 句 | ✅ |
| non_diegetic_music 为 N/A 或 1–3 句 | ✅ |
| 时长落在 4–15 秒 | ✅ |

> 审计过程中还发现并修复了 2 处自相矛盾：正向段残留否定词、以及"零文字"与官方"保留原文字"的冲突。

---

## 装机

### 方式 A · 直接指定路径

把整个仓库 clone 到本地，然后在对话里 `@` 引用：

```bash
git clone https://github.com/Ayanlin1688/Minimax-H3-Tiktok-skill.git
```

```
@<你的路径>/SKILL.md 帮我给这款 XX 写 15 秒带货提示词
```

### 方式 B · 装进客户端全局技能库

把整个文件夹放进客户端的 skills 目录（例：`C:\Users\<你>\.dsh\skills\`），重启客户端后，
新开对话直接说 `调用 minimax-h3-tiktok-ecommerce …` 即可自动加载。

---

## 维护与同步（以后怎么更新）

**仓库目录就是唯一真源。** 改完规则后，一条命令完成三件事：镜像到本机技能库 → 提交 → 推云端。

```powershell
# 进入仓库
cd <仓库路径>

# 1) 改规则（编辑 SKILL.md / references/ 下的文件）

# 2) 一条命令同步
pwsh -File tools/sync-to-github.ps1 -Message "feat: 新增 XXX 规则"

# 3) 出可分发包（版本号自动读 CHANGELOG）
pwsh -File tools/build-package.ps1
```

### 发版流程（建议）

| 步骤 | 操作 |
|---|---|
| 1 | 在 `CHANGELOG.md` 顶部加一条 `## [x.y.z] - 日期` |
| 2 | 跑 `tools/build-package.ps1` 出 zip + SHA256 |
| 3 | 跑 `tools/sync-to-github.ps1` 推云端 |
| 4 | 在 GitHub 打 tag / 发 Release，附上 zip |

### 版本号怎么定

| 层级 | 触发 | 例 |
|---|---|---|
| **MAJOR** | 架构重构（如"反缺陷清单 → 正向真实感模型"） | 2.0.0 |
| **MINOR** | 新增铁律 / 品类层 / 规则库文件 | 1.1.0 |
| **PATCH** | 修正措辞、补漏、文档修订 | 1.0.1 |

---

## 版本历史

| 版本 | 日期 | 关键变更 |
|---|---|---|
| **v1.0.0** | 2026-11-16 | 首次开源：27 条铁律 + 36 项自检 + 全类目主模板 + 五轮病理诊断档案 |

---

## 能力边界（诚实说明）

**能做到**
- 消除第三只手、产品分身、手飘物体、完全悬空（已用真实视频闭环验证）
- 显著提升"像实拍"程度（七层真实感模型）
- 全类目通用（T × C × S 路由，20 品类实测全部落位）

**做不到**
- 100% 保证每条视频完美 —— H3 自身有随机性
- 替代真人实拍
- 保证一次过审 —— **标准工序是一次生成 3 条挑 1 条**

---

## 赞赏支持

如果这个 Skill 帮你少发了几条废片、少熬了几个夜，欢迎扫码请我喝杯咖啡 ☕

<table>
<tr><td align="center">
  <img src="assets/sponsor-qr.jpg" alt="赞赏码" width="280">
  <br>
  <b>「祝福的人都发财！」</b>
</td></tr>
</table>

> 赞赏完全自愿，**不影响任何功能与后续更新**。本项目永久 MIT 开源。
> 更实在的支持方式是：**点个 ⭐ Star**，以及把遇到的翻车帧发给我 —— 那才是让它继续变好的燃料。

---

## English Summary

A prompt-engineering Skill for **MiniMax H3 (Hailuo 02)** that generates TikTok Shop US product-video prompts which actually look like real handheld footage.

Built by reverse-engineering **five rounds of failed AI videos frame by frame**. It combines a **positive realism model** (sensor grain, highlight clipping, mixed white balance, cluttered sets, imperfect speech, fumbled actions) with **27 anti-artifact rules** covering extra hands, floating products, clipping/intersection, product duplication, waxy faces, and color bleed.

Universal across product categories via a three-axis router: **T** (physical size) × **C** (interaction grammar) × **S** (regulated-category compliance).

Ships with a copy-paste master template, a randomized persona pool, a US home-scene library, an 8-archetype viral script vault, and 36 self-checks.

---

## Support

If this Skill saved you a few wasted renders, you're welcome to buy me a coffee ☕ — scan the QR code above.

Sponsorship is entirely optional and **never gates any feature or future update**. This project stays MIT-licensed forever. The more useful support is a **⭐ Star** and sending me your failed frames — that's what keeps it improving.

---

## License

[MIT](LICENSE) © 2026 Ayanlin1688

---

<p align="center">
  <sub>把这个 Skill 当作起点，不是终点 —— 拿真实翻车视频继续迭代它。</sub>
</p>
