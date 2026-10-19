# 公开数据集仓库设计方案(评审稿)

> 本文件是设计说明,评审用,**将来不进公开仓**。其余文件就是公开仓建成后的真实样子。

## 1. 定位一句话

私有仓是工厂,公开仓是货架:只放导出的数据和文档,不放任何采集/解读代码。
好处:边界干净(泄密面为零)、公开仓可以随便 star/PR/被爬、将来转让或换托管不牵连流水线。

## 2. 命名建议

| 候选 | 理由 |
|---|---|
| **ai-repo-atlas**(推荐) | 短、独特、无商标歧义,同名域名/静态站/组织号可沿用,品牌一词到底 |
| open-ai-catalog | 易与 OpenAI 公司混淆,弃 |
| awesome-ai-landscape | awesome- 前缀会被当成清单类项目,同质化严重,弃 |

建议同时新建同名 GitHub 组织承载(而不是挂个人号),后续静态站、MCP 都放这个组织下。

## 3. 目录结构与职责

```
ai-repo-atlas/
├── README.md                  # 门面:是什么/规模/三种用法/信任声明/路线图
├── DATASET.md                 # 数据集卡:字段字典、枚举定义、null 纪律、引用格式
├── llms.txt                   # LLM 客户端标准入口:全站资源目录
├── CHANGELOG.md               # 数据与格式变更日志(流水线自动追加)
├── data/
│   ├── catalog.jsonl          # 机器主表:一仓一行 = 卡片六组字段 + meta 元数据
│   ├── catalog.mini.jsonl     # B 层迷你卡(5 字段,放量后加入)
│   ├── schema/card.schema.json# JSON Schema,消费方可程序校验
│   └── cards/{owner首字母}/{owner}__{repo}.md   # 人读卡,一仓一文件
├── trends/
│   └── weekly-2026-W42.md     # 周趋势报告(周更,天然的对外发布素材)
└── (releases)                 # 月度冻结快照走 release 附件,不进 git 历史
```

## 4. 公开边界:什么进,什么不进

**进(白名单)**:卡片六组字段、池元数据 join(stars/language/license/topics/pushed_at 等 GitHub 公开数据)、周趋势汇总。

**不进,以及为什么**:

| 不进的东西 | 原因 |
|---|---|
| README 全文(42,763 份) | 版权(是各项目的创作内容)+ 体积双问题。卡片只带行号级引文和回链,是"解读+合理引用"的干净形态;将来 MCP 需要 README 时运行时从 GitHub 取 |
| raw_verdicts(裁决过程) | 内部调试细节,公开层有 evidence 引文已够核查,裁掉还省 40% 体积 |
| 采集/解读脚本、token、内部 state | 工厂的事留在工厂 |
| enrich 缓存等中间产物 | 中间产物无消费价值,纯体积 |

## 5. 数据形态双轨:为什么 jsonl 和 markdown 都要

- `catalog.jsonl`:给程序和 AI 用——一行一仓,可流式读、可 grep、可进 HuggingFace;实测一张 A 层全卡约 2KB,8k 行约 16MB。
- `cards/*.md`:给人看,同时 GitHub 上的 markdown 页面本身会被搜索引擎索引——8k 张卡片页是白捡的长尾承接页(仓库名+怎么样/vs/部署 之类搜索直接落到卡片)。

## 6. 导出变换规则(卡片缓存 → 公开行)

1. 按 fn 字典序稳定排序写出——git diff 只含真正变化的行,日更提交历史才不会爆炸。
2. 卡片六组字段原样,裁掉 raw_verdicts、xcheck。
3. join 池元数据到 meta 层(license/stars 等 GitHub 为准,反徽章造假的判定链保留)。
4. B 层迷你卡只出 5 字段(fn/one_liner/ai_role/license_risk/stars),约 0.5KB/行。

## 7. 更新与体积策略

| 机制 | 设计 |
|---|---|
| 日更 | 私有仓夜间流水线末尾加一步导出→公开仓单 commit,如 `data: 2026-10-19 daily (+217 cards, +3 meta)` |
| 周更 | trends/weekly-YYYY-Www.md,同时是对外发帖的素材 |
| 月度 | 冻结快照打 tag,附件走 release(GitHub release 不占 git 历史) |
| 体积预算 | A 层 16MB + md 卡 16MB + B 层 17MB ≈ 50MB,离 1GB 建议线很远;git 历史按日增量累积,可控 |

## 8. 许可

- 卡片与衍生数据:**CC BY 4.0**(署名即可用,商业友好,一句话说得清)。备选 ODbL 更"数据库专用"但条款复杂,劝退使用者,不值。
- 声明三段:元数据来自 GitHub 公开 API;引文版权归原项目(行号级短引用+回链,合理使用);本仓不收录 README 全文。
- 公开仓 v1 无代码;日后若放导出示例,MIT。

## 9. 机器可读四件套

1. `data/schema/card.schema.json`——JSON Schema 校验;
2. `DATASET.md`——字段字典+枚举表(人读);
3. `llms.txt`——LLM 客户端标准发现入口;
4. Roadmap:HuggingFace 数据集镜像(jsonl 直接吃)、CITATION.cff。

## 10. 与三个出口的衔接

- **静态站**:直接从此仓 catalog.jsonl 构建(s9 读公开数据而不是读私有 state,工厂和货架彻底解耦);
- **MCP**:MCP 服务的数据源也是这份 jsonl——一份引擎,货架、站点、AI 调用三处消费;
- **周报/B2B**:trends/weekly 是周报的公开瘦身版。

## 11. 发布 checklist

- [ ] 新建 org + 仓库,About 填描述+topics(ai/catalog/dataset/llm/awesome-adjacent)+ license 文件
- [ ] demo 里三个示例数据已由真实导出验证(本 demo 的 catalog.jsonl 就是一次真实导出)
- [ ] 提交 GSC/Bing 不适用(是 repo 不是站),但 GitHub README 徽章、pin、组织 profile 页配齐
- [ ] 第一条外链:相关 awesome-list PR + 知乎/掘金介绍文 + HN Show HN

## 12. P0 信号组(s9_signals.py,2026-10-18 实施定稿)

卡片六组之外新增第七组 `signals`,补两个用户最高频问题:"还活着吗"与"别人用得怎么样"。

| 信号 | 来源 | 刷新 | 关键规则 |
|---|---|---|---|
| maintenance | GitHub API 三件套(releases/contributors/近 30 条已关 issue)+ 池内 pushed_at | 月更(25 天新鲜度缓存) | 规则合成枚举:≤90 天 push→active;≤180→maintenance;≤365→declining;archived/超 365→abandoned |
| velocity | 每日快照 pool.ndjson + 活池星数序列 | 日更 | 窗口 = min(90, 可用历史天数),快照逐日累积后自动放大;域内按净涨星排名;trend 需 ≥4 个序列点 |
| downloads | s8 install 裁决引文提取包名 → pypistats / npm downloads 免费 API | 月更 | 只认 README 明写的 pip/npm 安装命令,null 纪律 |
| platform | README 徽章/正文正则扫描 | 跟随 README sha | os 六值 / protocols 三值(openai-api、mcp、ollama)/ 界面语言,只取明确信号 |

成本:A 层 593 仓一次性 1779 次 core 调用(0.8s 节奏约 40 分钟),此后月更增量极小;downloads 数百包 × 免费接口。生产脚本在私有仓 `s9_signals.py`,断点续跑、单仓失败不挡批、预算到点优雅收尾。

## 13. 本 demo 说明

- `data/catalog.jsonl` 三行是**真实数据**(openclaw/rea/n8n 的真实卡片 join 真实池元数据,一次性命令拼装;正式导出器在私有仓实现);
- 数字口径:池 42,853 仓 / README 42,763 份 / A 层试批 593 张(2026-10-18);
- `trends/weekly-2026-W42.md` 是格式骨架,内容标 demo,正式版由流水线从 events 生成。
