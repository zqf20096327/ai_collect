# DATASET.md — 数据集卡与字段字典

主表 `data/catalog.jsonl`,一仓一行(JSON Lines,UTF-8,按 `fn` 字典序稳定排序)。
卡片数据版本与格式版本见文末。校验文件:`data/schema/card.schema.json`。

## 顶层结构

| 字段 | 类型 | 说明 |
|---|---|---|
| `fn` | string | `owner/repo`,全数据集主键 |
| `card_sha` | string | 解读所依据 README 内容的 sha 前缀;README 变了它就变,是卡片新鲜度的钥匙 |
| `card_at` | date | 卡片生成日 |
| `meta` | object | GitHub 元数据(权威层,反 README 徽章造假) |
| `identity` | object | 检索组:人读的"它是什么" |
| `filters` | object | 筛选组:七个硬约束枚举 |
| `eval` | object | 评估组:敢不敢用 |
| `links` | object | 关联组:替代品/竞品/生态兼容 |
| `intel` | object | 情报组:维护者与地域信号 |
| `signals` | object | 信号组:维护健康/涨星速度/包下载/平台协议(P0) |
| `trust` | object | 信任组:置信度与行号证据 |

## meta(GitHub 元数据)

`owner_type / stars / forks / language / license / topics / archived / created_at / pushed_at / homepage / html_url`

## identity(检索组)

| 字段 | 说明 |
|---|---|
| `one_liner` | ≤30 字:给谁 + 解决什么 |
| `review` | 100–150 字:做什么、给谁用、关键机制与限制;保证含 GitHub description 之外的信息 |
| `highlights` | 能力事实 2–4 条 |
| `use_cases` | 适用场景,用户口吻 |

## filters(筛选组)— 七个枚举

| 字段 | 取值 | 判定要点 |
|---|---|---|
| `ai_role` | `ai-native` / `ai-ecosystem` / `ai-enhanced` / `ai-knowledge` | 去掉 AI 部分产品还成立吗?成立→enhanced;本体是模型/模型工具→native;LLM 周边工具→ecosystem;清单→knowledge |
| `license_risk` | `permissive` / `viral` / `dual` / `none` | 以 GitHub 元数据为准(MIT/Apache/BSD→permissive;GPL/AGPL/SSPL→viral);README 明示双许可且行号核验过→dual |
| `deploy` | `desktop` / `cloud-api` / `self-host` / `library` | 安装包→desktop;仅 SaaS→cloud-api;docker/自建→self-host;pip/npm→library |
| `model_dep` | `no-llm` / `local-ok` / `locked-api` / `null` | 无需 LLM 的确定性路径→no-llm;支持本地模型→local-ok;仅云 API key→locked-api |
| `hardware` | `gpu-24g` / `gpu-8g` / `cpu-ok` / `null` | **只认带数字的原话**;"GPU-accelerated" 等形容词不算 |
| `install_friction` | `low` / `medium` / `high` | docker 或无编译无系统依赖→low;有其一→medium;都有→high |
| `maturity` | `idea` / `mvp` / `stable` / `deprecated` / `null` | 由 CI/发布/贡献者/弃坑声明等结构信号合成;无 README 佐证→null |

**null 纪律**:`null` 表示"README 没说",不是"没有"。筛选时应把 null 当未知处理,而不是当否。

## signals(信号组)— P0 四件

回答两个最高频的问题:"还活着吗"(maintenance)与"别人用得怎么样"(velocity/downloads);platform 喂对比页。
仓库级事实月更(maintenance/downloads),市场级信号日更(velocity);null 纪律同上。

| 字段 | 说明 |
|---|---|
| `maintenance.status` | `active` / `maintenance` / `declining` / `abandoned`。规则合成:archived 或 >365 天无 push → abandoned;>180 → declining;>90 → maintenance;≤90 → active |
| `maintenance.pushed_days` | 距最近一次 push 的天数 |
| `maintenance.last_release_days` / `releases_per_year` | 最近 release 距今天数 / 近一年 release 数(单页封顶 100) |
| `maintenance.contributors` | 贡献者数(分页计数,封顶 500) |
| `maintenance.issue_close_days_med` | 近 30 条已关闭 issue 的中位关闭天数;样本 <5 条 → null |
| `velocity.net_window` / `window_days` | 窗口内净涨星与窗口天数;当前采集历史不足 90 天时按可用历史计,快照逐日累积后窗口自动放大到 90 |
| `velocity.domain_rank` / `domain_size` | 同领域内按净涨星排名 / 领域内卡片总数 |
| `velocity.trend` | `accelerating` / `steady` / `decelerating`;星数序列 ≥4 点才判,否则 null |
| `downloads.ecosystem` / `package` / `downloads_month` | README 明写的 pip/npm 安装命令对应的包与月下载量(PyPI/npm 官方口径);README 没写安装命令 → null |
| `platform.os` | `windows` / `macos` / `linux` / `android` / `ios` / `web`,README 徽章与正文信号 |
| `platform.protocols` | `openai-api` / `mcp` / `ollama`,模型互通协议 |
| `platform.interface_lang` | `en` / `zh`,界面语言信号 |

## eval / links / intel / trust

| 组 | 字段 |
|---|---|
| eval | `target_user`、`paper_url`、`demo_url`、`self_declared_early`(自述早期阶段) |
| links | `scenario_tags`(场景标签,中文归一)、`domain`、`alternative_to`(可替代的知名产品)、`competitors_mentioned`(README 竞品自白)、`ecosystem_compat`(兼容 Ollama/OpenAI 协议等) |
| intel | `maintainer_type`(individual/team/company/university/media)、`zh_origin` 及信号 |
| trust | `confidence`(high/mid/low)、`evidence`(行号+原文引句,如 `L11: ...`)、`ver`(卡片架构版本)、`prompt_ver`、`generated_at` |

## 质量口径

- 同一批 README 双跑,枚举一致率 ≥98% 才放量;
- 引文须与清理后 README 对应行一致,模型只指行号不默写原文(转述型幻觉在构造上被消灭);
- 禁词扫描(最强/颠覆/revolutionary…约 80 词)不过则重试,仍不过软放行并留痕;
- `card_sha` 变化即自动重解读,卡片不会对旧 README 说新话。

## 许可与引用

数据 CC BY 4.0;元数据来自 GitHub 公开 API;引文版权归原项目,已附回链。引用格式见 [README.md](README.md#引用)。
