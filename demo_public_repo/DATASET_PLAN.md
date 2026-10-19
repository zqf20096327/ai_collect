# 数据仓库最终方案(v1 定稿,2026-10-18)

> 本文是字段级最终契约:s8 放量、导出器、网站生成器都以它为准。
> 改动纪律:字段一经冻结,加字段走 minor 版本并在 CHANGELOG 记录,改语义必须升 major。

## 0. 三条定案原则

1. **每个字段必须有用户问题对应**:用户选型只问六件事——是什么/给谁用、能否商用、跑不跑得动、还活着吗、别人用得怎么样、跟 X 比怎么样。答不上这六问之一的字段不进主表。
2. **每个字段必须有展示位**:网站、榜单、筛选器、卡片、周报,至少占一个;没有展示位的数据不采。
3. **冻结优先于丰富**:v1 用已验证的 593 卡试批字段冻结放量;新想法排队 v1.1+,不阻塞放量。

## 1. 主表 catalog.jsonl 字段定稿(v1)

一仓一行,按 fn 字典序稳定写。九个组:

| 组 | 字段 | 回答什么 | 状态 |
|---|---|---|---|
| 键 | fn / card_sha / card_at | 主键 / 卡片新鲜度钥匙 | ✅ 已有 |
| meta | owner_type, stars, language, license, topics, archived, created_at, pushed_at, homepage, html_url | GitHub 权威事实(反徽章造假) | ✅ 已有 |
| identity | one_liner, review, highlights, use_cases | 是什么/给谁用(六问之一) | ✅ s8 |
| filters | ai_role, license_risk, deploy, model_dep, hardware, install_friction, maturity(七枚举) | 能否商用/跑不跑得动(六问之二三) | ✅ s8 |
| eval | target_user, paper_url, demo_url, self_declared_early | 敢不敢用 | ✅ s8 |
| links | scenario_tags, domain, alternative_to, competitors_mentioned, ecosystem_compat | 跟 X 比怎么样(六问之六)+ 聚合键 | ✅ s8 |
| intel | maintainer_type, zh_origin | 谁在维护/地域信号 | ✅ s8 |
| signals | maintenance{status, pushed_days, last_release_days, releases_per_year, contributors, issue_close_days_med}; velocity{stars_now, net_window, window_days, trend, domain_rank}; downloads{ecosystem, package, downloads_month}; platform{os, protocols, interface_lang} | 还活着吗/别人用得怎么样(六问之四五) | ✅ s9 P0 |
| trust | confidence, evidence(行号引文), ver, prompt_ver, generated_at, softened | 可核查(信任底座) | ✅ s8 |

明确不上主表:forks、open_issues(无展示位);raw_verdicts(内部调试);README 全文(版权,运行时回源)。

## 2. 派生数据文件(网站的地基,不是新采集)

| 文件 | 内容 | 生成方式 | 驱动的页面 |
|---|---|---|---|
| timeseries/stars.jsonl | 每仓星数序列(fn, [(日期, 星数)]) | 周一星数点增量追加,零成本 | 详情页曲线图/爆发榜 |
| views/alternatives.jsonl | 商业产品→开源替代映射表 | alternative_to + competitors_mentioned 双向聚合成表 | 替代页/对比页(SEO 最大流量口) |
| trends/weekly-*.md(+jsonl) | 周趋势 | events×cards 聚合 | 周报页/外发素材 |
| catalog.mini.jsonl | B 层 5 字段(fn, one_liner, ai_role, license_risk, stars) | B 层放量后 | 场景页条目行 |

## 3. 网站 → 数据映射(建站时照此执行)

| 网页类型 | 数据来源 |
|---|---|
| 详情页(~8k) | catalog 一行 + cards/*.md |
| 场景聚合页 | scenario_tags 分组 |
| 替代/对比页 | views/alternatives.jsonl |
| 筛选器 | 七枚举 + maintenance.status + downloads |
| 榜单页 | velocity.net_window / downloads / stars 排序 |
| 赛道页 | domain(词表冻结后生效) |
| 周趋势页 | trends/ |
| 全站 SEO 基建 | sitemap(从 catalog fn 生成)/ robots / JSON-LD(SoftwareApplication) / llms.txt |

## 4. 排队中的字段(触发条件写死,不提前做)

| 版本 | 字段/数据 | 触发条件 |
|---|---|---|
| v1.1 | safety(安装红旗:curl\|bash/过度权限/默认遥测)+ data_handling(数据出不出本机) | 8k 放量完成后,s9 加两规则采集器 |
| v1.1 | HN/Reddit 口碑时间点 | 静态站上线后 |
| v2 | README 变更时间线/项目转向检测(独占性最强,历史从现在开始记) | 8k 卡稳定日更一个月后 |
| v2 | 论文↔代码↔引用链 | 出现对应查询需求 |
| 按需 | 贡献者流动图谱 | B2B 首个付费客户 |

永久不做:主观评分/排名推荐语、情感分析、issue 评论爬取、维护者个人级信息。

## 5. 刷新节奏与规模预算

| 数据 | 节奏 | 成本 |
|---|---|---|
| 池/README/卡片增量 | 日(夜间流水线) | 已在跑 |
| velocity/platform | 日(本地零 API) | 秒级 |
| maintenance/downloads | 月(25 天新鲜度缓存增量) | 分钟级 |
| 星数点 | 每周一自动 | ~2MB/周 |
| 月度快照 | release 附件,不进 git | — |
| 总体积(A 层 8k + B 层 34k + 时间序列) | ≈ 60-80MB | 远离 1GB 线 |

## 6. 发布节奏

1. 用现有 593 卡先上公开仓(冻结即 v1.0,数据格式不再动);
2. 8k 放量=纯数据量增长,非 schema 变更;
3. v1.1 字段按触发条件进,CHANGELOG 记版本,消费者无感升级。
