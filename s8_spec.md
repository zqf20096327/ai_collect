# s8 解读层完整设计（v2 定稿）

> v2 相比 v1 的变化：证据机制升级为"行号指认"（学 dbhub v3）；新增"程序提名"层、
> 中立性三件套、信息增量校验、程序对照哲学、完整金标体系、条目级遥测；
> 架构定为"封闭字段三段式 + 开放字段自由抽取"的混合体。
> rm_clean / 禁词表 / 校验框架三样接近领域无关，优先复用 dbhub 代码而非重写。

---

## 0. 这是什么：一句话和大白话

**一句话**：把 4.2 万份 README 变成 4.2 万张标准"产品卡片"，机器能筛选、人能看懂、证据可核查。

**大白话**：README 是作者写的"广告 + 说明书"，长短不一、真假混杂、中英文都有。解读层像一个公正的编目员：逐份阅读，按固定表格填写"它是什么、给谁用、怎么装、有什么限制"，每填一个结论都注明"依据原文第几行"。填好的卡片供给四个出口：搜索引擎页面、AI 助手（MCP/API）、B2B 周报、站内检索。

对消费者三个承诺：

| 承诺 | 靠什么做到 | 验收指标 |
|---|---|---|
| 机器筛得动 | 七个硬约束枚举，规则合成 | 双跑一致率 ≥98% |
| 人看得懂 | 一句话 + 评测段，中立无广告腔 | 禁词零命中 |
| 较真者可核查 | 每个判断带原文行号 | 行号有效率 ≥95% |

## 1. 五条铁律（所有细节由此推出）

1. **宁可空，不可猜**：文本没有的信息填 null。例：README 只说 "GPU-accelerated"（渲染用 GPU）没给显存数字 → hardware = null。
2. **结论留给规则，模型只报事实**：唯一例外是 ai_role（需要真正的阅读理解）。枚举判定全部由确定性规则从事实+元数据合成。
3. **证据行号化**：模型对原文做"选择题"（指行号），不做"默写题"（抄引文）——转述型错误在构造上消灭。
4. **中立强制**：README 里的营销语言（"blazingly fast""史上最强"）不许渗透进卡片。
5. **花的每一分钱都留账本**：每条解读的耗时、违规、重试、修复全部落日志，优化决策靠数据不靠感觉。

## 2. 整体架构

```
README ──①清理──→ 清理文（去噪压缩，非空行编号）
      ──②提名──→ 候选清单 {封闭词 → [行号+行文本]}（全文扫描，不受窗口限制）
      ──③解读──→ 事实卡（LLM 一次调用：封闭字段做裁决题，开放字段做填空题）
      ──④合成──→ 卡片（行号回填引文 + 规则判定枚举 + 元数据权威覆盖）
      ──⑤闸门──→ 六道校验（不过则带原因重试一次，仍不过按软/硬分流）
      ──⑥落盘──→ sha 键控缓存 → 推送 dbhub 第三层
```

为什么是这个顺序：提名放在 LLM **之前**，是为了"该找到的行一定被提名到"（正则全文扫，不受给模型看多少的限制）；行号回填放在 LLM **之后**，是为了"引文不可能被改写"；规则合成放在最后，是为了"枚举永不漂移"。

## 3. 输入：五层信息源

| 层 | 内容 | 来源 | 用途 |
|---|---|---|---|
| 主料 | README 清理文（头部 + 关键章节定向切片，≤12KB 可见窗口） | s6 缓存 | 解读 |
| 元数据 | license / topics / language / stars / archived / created / pushed | s5/s7 池 | 判定权威（反徽章造假） |
| 仓库结构 | CI / releases 数 / contributors | GitHub API 增量补 | maturity 原料 |
| events | 涨星速度 | 已有 | 冒头升级 + 情报组 join |
| 可选加料 | docs 站 / 论文 | 后期按需 | 头部加深 |

README 徽章会说谎（挂 MIT 徽章但无 LICENSE 文件），元数据兜底——多层信息源本身就是反作弊设计。

## 4. 第一步：清理 README（复用 dbhub rm_clean）

规则（dbhub 实测：整体压缩 17%–31%，同等窗口多装约 14% 内容）：

- 删：HTML 注释、水平线、引用定义行、目录（连续链接行）、徽章图片的 URL 部分
- 压：代码块超 6 行只留头 4 行 + 略标记；表格对齐空格；连续空行
- 换：changelog/社区/赞助/用户评价等噪音章节正文换"（略）"
- **留**：图片的 alt 文本（alt 可能是唯一证据）、链接的文字部分（[text](url) → text）、license 章节的正文首行（license_note 依据）

**证据安全原则**：被删掉的只有 URL/标签/空格/装饰，任何可能承载证据的文字都保留——所以清理后的行号仍然合法可指认。

**行号口径**：清理器只有一个实现，提名（②）和解读（③）共用，非空行从 1 起编号，改一处必须同步另一处。

## 5. 第二步：全文提名（三段式第一段，AI 域版 db_scan）

封闭词表正则扫描**全文（不截断）**，产出候选清单：

| 词表 | 内容举例 | 服务的字段 |
|---|---|---|
| 模型供应商 | openai / anthropic / deepseek / gemini / groq / ollama / llama.cpp / vllm / local weights | model_dep、ecosystem_compat |
| 安装信号 | pip install / npm i / docker run / cargo / go install / brew / .exe 下载 | deploy、install_friction |
| 硬件数字 | VRAM/RAM/显存/内存 + 数字 | hardware |
| 双许可 | dual license / commercial license / 企业版 / 商业授权 | license_risk 的 dual 覆盖 |
| 弃坑声明 | no longer maintained / deprecated / 停止维护（**必须锚定项目主语**——"某依赖已废弃"不算项目死，dbhub 金标实测裸词全是误报） | maturity 信号 |
| 知名产品 | Notion AI / Midjourney / Copilot / Claude Code / Midjourney … | alternative_to、competitors_mentioned |
| 形态检测 | 文件名 awesome 前缀 / 超长表格 | 分层路由（C 层） |

产出形如 `{词: [{line: 42, q: "行文本"}]}`。**可见窗口只影响"模型看多少"，不影响"提名到多少"**——支持矩阵深处的行（窗口外）照样被提名，模型可指认。

## 6. 第三步：LLM 解读——一张事实卡（一次调用，两种题型）

- **裁决题**（封闭字段）：对候选清单逐项表态四选一 + 指认行号。
  例："openai：support（有专门接入），lines [12]"；"midjourney：mention（只是对比提及），lines [88]"；
  "bedrock：none（误命中，Minecraft 基岩版非 AWS Bedrock），lines [23]"——rel=none 表示提名词在该语境下不适用，程序组装时丢弃（步骤 1 实测出现过，词表无法根除同名词，靠模型裁决兜底）
- **填空题**（开放字段）：one_liner / review / highlights / use_cases / 场景自由标签 / domain / target_user / maintainer_type …

事实卡模板（LLM 的输出）：

```json
{
  "identity": {
    "one_liner": "≤30字：给谁+解决什么",
    "review": "100-150字：做什么+给谁用+关键机制/限制",
    "highlights": ["能力事实 2-3 条"],
    "use_cases": ["适用场景 2-3 条，用户口吻"]
  },
  "open": {
    "scenario_tags_free": [], "domain": "", "target_user": "",
    "ai_role": "ai-native|ai-ecosystem|ai-enhanced|ai-knowledge",
    "maintainer_type": "individual|team|company|university|media",
    "zh_origin_signals": []
  },
  "verdicts": {
    "providers": [{"term":"openai","rel":"support|compat|mention","lines":[12]}],
    "install":   [{"term":"pypi","rel":"support","lines":[31]}],
    "vram":      [{"term":"8GB","rel":"support","lines":[55]}],
    "dual_license":  {"flag": true, "lines": [7]},
    "deprecation":   {"flag": false, "lines": []},
    "products":  [{"term":"Notion AI","rel":"alternative|competitor|mention","lines":[88]}]
  },
  "facts": {
    "needs_compile": false, "system_deps": ["GDAL"], "docker_available": true,
    "self_declared_early": {"flag": true, "lines": [3]},
    "paper_url": null, "demo_url": null
  },
  "audit": {
    "confidence": "high|mid|low",
    "evidence_lines": [3, 55]
  }
}
```

## 7. 第四步：程序合成——判定权分配表（核心设计）

不同字段用不同的判定方式，**按"该字段的事实是否封闭可枚举"分配**：

| 判定方式 | 字段 | 规则 |
|---|---|---|
| **元数据权威** | license_risk | dual 声明（行号核验过）→ dual；否则按元数据：MIT/Apache/BSD→permissive；GPL/AGPL/SSPL→viral；缺→none |
| **程序组装** | model_dep | no_llm 声明→no-llm；本地供应商 support→local-ok；仅云 key→locked-api |
| | deploy | 安装包→desktop；仅 SaaS→cloud-api；docker/自建→self-host；pip/npm→library |
| | hardware | VRAM 数字 ≥24G→gpu-24g；≥8G→gpu-8g；"CPU only"原话→cpu-ok；无数字→null |
| | install_friction | docker→低；无编译无系统依赖→低；有其一→中；都有→高 |
| **模型判+程序对照** | maturity | 结构层信号合成判定；程序独立探测分歧时**只降一级 confidence 并记备注，不覆盖**（防迎合） |
| **模型直接判** | ai_role | 去掉 AI 部分产品还成立吗？成立→ai-enhanced；本体是模型/模型工具→ai-native；LLM 周边→ai-ecosystem；清单→ai-knowledge |

"降级不覆盖"的理由：程序一旦预填，模型会顺着说（迎合偏差）；让两者独立判断、只在分歧时降置信，既利用了程序探测的可靠性，又不剥夺模型的阅读理解。

## 8. 证据机制：行号指认

```
喂给模型：  L42| requires 8GB VRAM and 12GB RAM
模型输出：  {"vram": [{"term": "8GB", "lines": [42]}]}     ← 只给行号
程序回填：  引文 = 清理文第 42 行原文                        ← 引文不可能被改写
```

- 模型从"背写原文"变成"做选择题"，转述、改写、幻觉失去输出通道。
- 行号合法性 = 落在可见窗口内，或属于候选清单标注的（窗口外）行。
- **desc 降级路径**（无 README 仓库）：退回 v2 引句子串校验（引文须为描述原文子串），confidence 封顶 mid。
- 坏行号的处置：丢该条裁决，不整卡拒收（见软放行）。

## 9. 中立性三件套（防广告腔渗透）

1. **契约**写进提示词：只陈述可验证事实；禁评价词/绝对词/对比/预测；动词用"提供/支持/读取/生成"；highlights 只列能力事实。
2. **禁词扫描**：中英文约 80+ 词正则（最强/颠覆/革命性/best/fastest/revolutionary/outperforms…），基本复用 dbhub 词表，追加 AI 域补充（"吊打 GPT""地表最强"等）。已知豁免：唯一/第一/完全/最佳（README 事实转述高频词，误伤大于收益）。
3. **违规处置**：命中 → 带拒收原因重试一次 → 仍命中 → **软放行**：禁词字段置空、违规列表项删除，卡片保住并留 `softened` 痕迹；字段非法/截断等硬伤仍整卡拒收。

为什么软放行：一次 API 调用已花掉钱，只因一个 highlight 里出现"powerful"就丢整张卡不划算；处置过的空字段页面不展示、回退 description。

## 10. 校验闸门全集（六道）

| 闸 | 检查 | 失败处置 |
|---|---|---|
| 结构闸 | JSON 可解析、枚举合法、URL 格式 | 别名归一（保守表："备份工具"→"备份"）能修则修；否则重试一次→拒收 |
| 行号闸 | 行号在可见窗口或候选集内 | 丢该条裁决，不整卡拒 |
| 中立闸 | 禁词扫描 | 重试→软放行（§9） |
| 增量闸 | review 含 description 之外 ≥3 个实义信息点（虚词通用词不计） | review 置空，页面回退 description——防"花钱解读出一句简介复读" |
| 对照闸 | install/deprecation 程序独立探测 vs 模型结果 | 分歧只降一级 confidence + 备注，不覆盖 |
| 一致闸 | 试批双跑枚举一致率 | <98% 不放量——说明还有字段没拆干净事实与判断 |

## 11. 卡片字段总表（六功能组，最终形态）

| 组 | 字段 | 职能 |
|---|---|---|
| ① 检索组 | one_liner、review、highlights、use_cases、scenario_tags、domain | 查得到（中文归一，中文查询命中英文 README） |
| ② 筛选组 | ai_role、license_risk、deploy、model_dep、hardware、install_friction、maturity | 筛得动（七个硬约束枚举） |
| ③ 评估组 | stability 事实（CI/发布数/贡献者/近期推送）、target_user、paper_url、demo_url | 判断敢不敢用 |
| ④ 信任组 | evidence（行号+回填引文）、readme_sha、ver/prompt_ver、confidence、softened | 信得过（换模型后能定位该重审的卡） |
| ⑤ 关联组 | alternative_to、competitors_mentioned、ecosystem_compat | 页面连得起（对比页/替代页独家素材） |
| ⑥ 情报组 | maintainer_type、zh_origin、涨星/趋势 join | B2B 买单（周报和赛道图谱原料） |

## 12. 分层覆盖与刷新

| 层 | 对象 | 卡片 | 触发 |
|---|---|---|---|
| A 全卡 | stars≥300 或 90 天涨星≥50（约 8k，事件驱动进出） | 六组全出 | readme_sha 变更 |
| B 迷你卡 | 其余长尾（约 34k） | ①②组 5 字段 | readme_sha 变更 |
| C 规则卡 | awesome 清单 / 无 README | 条目正则解析 / desc 降级解读 | 同上 |
| 冒头升级 | B→A | 重做全卡 | 涨星达标即时触发 |

字段寿命分组：检索/筛选组跟 readme_sha；评估组（maturity 等）按季度 + 事件（发版/归档/冒头）重算——项目死了 README 不会变，但"能否生产使用"的答案变了。

## 13. 场景词表：两段式冻结 + 双向契约

1. 试跑期自由打标（scenario_tags_free）；
2. 攒到约 5,000 张卡后聚类真实词频，**从数据里冻结双语受控词表**，回填映射；
3. 上线后持续吃两路反馈：无结果查询日志（缺词信号）、高点击卡片的标签（好词信号）；
4. **词表是双向契约**：仓库侧打标与搜索侧"查询解析器"（用户一句话→结构化查询）必须共用同一张表，任一侧改动同步另一侧。

## 14. 提示词（全文可粘贴）

```text
你是开源 AI 生态的编目员，为选型目录做中立的结构化编目。

【中立性契约——违反即拒收】
只陈述 README 可验证的事实：它是什么、做什么、给谁用、怎么安装运行。
禁止：评价词（强大/优秀/perfect…）、绝对词、对比判断、预测。
动词用事实性动词：提供/支持/读取/生成/运行。不确定的内容宁可不写。

【输出规则】
1. 只依据给定文本；没有的信息填 null，禁止推测。
2. 裁决题：对候选清单逐项表态，rel 三选一（support=明确适配/专门接入；
   compat=仅协议兼容；mention=仅提及/对比），并给 lines 行号数组——
   只填行号数字，禁止抄写原文。候选清单标（窗口外）的行也可指认。
3. hardware 只认带数字的原话；"GPU-accelerated"等形容词不算。
4. ai_role 判据：去掉 AI 部分产品还成立吗？成立→ai-enhanced；
   本体是模型/模型工具→ai-native；LLM 周边工具→ai-ecosystem；清单→ai-knowledge。
5. one_liner ≤30字（给谁+解决什么）；review 100-150字且必须包含
   description 之外的信息；use_cases 用用户口吻。
6. 只输出一个 JSON，不要任何其他文字。

【字段定义】（§6 模板）
【范例】3 个：Dokis（ai-native 库）/ FMCL（ai-enhanced 应用）/
  awesome 清单（ai-knowledge，实际走规则层，防误路由）

仓库：{fn}   描述：{desc}   主题：{topics}
--- README 开始（L行号|原文，可见范围 {line_range}）---
{readme}
--- README 结束 ---
候选清单：{dbcands}
```

版本纪律：ver 标架构代际（1=引句子串，2=行号指认），prompt_ver 标架构内提示词迭代，任何改动 +0.1 并留痕。

## 15. 质量评估：金标体系

- **建集**：分层抽样约 150 张（每组 ≤12 + desc 降级路径少量）+ 30 条边界例（历史拒收）；金标条目须 sha 三方一致（缓存 sha = 状态 sha = README sha，防内容漂移导致对比失真）；多代金标集互不重叠。
- **生产方式（agent_batch 模式）**：导出批次 → 会话内 AI 亲自写卡 → **走与 API 完全相同的校验**入同一份缓存——人工/AI 标注产物与机器产物无缝衔接，few-shot 范例也这样生产。
- **指标四件**：
  - pass1 = 首次调用即过全部校验的比例
  - pass2 = 重试一次内的最终通过率（生产口径）
  - agree = 通过项与金标的字段一致率（枚举精确集）
  - 边界恢复率 = 新方案能捞回多少历史拒收（边界例无金标，只测这个）
- 任何提示词/清理/参数改动，先跑金标对比再上线。

## 16. 遥测与迭代方法论

每条解读一行 jsonl（runlog）：

- 输入侧：原始/清理后字符数、可见行数、窗口外候选行数（漏判归因关键）
- 耗时：API 秒数（累计）、全程秒数、API 尝试次数
- 轨迹：**逐次违规快照**（区分"重试自愈"与"救不回"两类问题）
- 结果：done/rejected/failed、枚举修复数、review 是否被增量闸置空、xcheck 备注

运行收尾聚合：pass1/pass2、拒收原因帕累托、耗时分位数。

**拒收挖矿方法论**：拒收不是垃圾是矿——dbhub 曾从 991 条拒收里挖出 944 条是旧截断 bug，从而决定重烧；据此别名表才敢"刻意保守"。s8 上线后每月做一次拒收帕累托分析，驱动校准。

## 17. 成本工程

- **两层缓存**：sha→结果（同内容 README 跨仓共用，不重复花钱）；fn→sha 状态。
- **拒收不重烧**：同 sha 已拒收的进人工队列不再烧钱；提供捞回开关（架构升级后历史拒收值得重烧）。
- **出池不解读**；desc 变化可重试。
- **chunk 批量落盘**：避免逐条全量重写大缓存的 O(n²) 磁盘 I/O。
- **并发模型**：worker 只返回结果 dict，共享缓存由主线程统一落账（防 dict 竞态）。

## 18. 成本估算

| 项 | 量级 |
|---|---|
| A 层全量（约 8k × 2–3k tokens） | 2,000–3,000 万 tokens，便宜模型批处理 1–2 天 |
| B 层全量（约 34k × 1k tokens） | 3,000–4,000 万 tokens |
| 日更增量（README 变更 + 新仓 + 冒头升级） | 一天几十到几百条，成本可忽略 |
| 提名/清理/校验 | 纯本地计算，零 API 成本 |

## 19. 落地路径与验收

| 步 | 内容 | 验收 |
|---|---|---|
| 1 | 移植 rm_clean + 写 AI 域提名词表（§5 七张词表） | 抽 200 篇实测压缩率与提名召回 |
| 2 | agent_batch 模式生产 3 个 few-shot + 建 150 金标 | 人工过目 |
| 3 | 500 试批 | 三份报告：双跑一致率 ≥98%、行号有效率 ≥95%、抽检 25 张 |
| 4 | B 层放量 → A 层放量 | runlog 帕累托无异常聚集 |
| 5 | 接入夜间 GHA，日更增量 | 连续一周无人值守稳定 |
| 6 | 词表冻结（约 5k 卡后） | 无结果查询率基线建立 |

## 20. 附录：两个教学走例

**ChatGPUI（三个教训）**
- 融合判定：元数据 AGPL→viral，但 README 明示双许可（行号核验过）→ 覆盖为 dual
- null 纪律："GPU-accelerated" 是渲染不是推理显存，无数字 → hardware=null
- 事实与观感分离："blazingly fast" 不能支撑 stable；无发布版工件 → maturity=mvp

**FMCL（中立与竞品）**
- ai-enhanced：主体是 Minecraft 启动器，AI 是功能点（33 工具 Agent + 离线语音）
- zh_origin：全中文 README + BMCLAPI 国内镜像 + 国内音源 → true
- 竞品自白：提及与 HMCL/PCL CE 房间互通 → competitors_mentioned=[HMCL, PCL CE]
- install_friction：需 Java/可选 ffmpeg/python3-tk → medium；硬件无数字 → null
