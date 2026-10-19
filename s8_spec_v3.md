# s8 解读层 v3 设计(2026-10-18 定稿)

> 基线 = s8_spec.md v2 + prompt_ver 1.4(一致闸 98.5% 已过线)。
> v3 主题:**字段冻结不动,吸收 dbhub 精华改造工厂机器**,为放量 8k+34k 清障。
> 改动纪律:v1 契约(catalog 九组字段)不变;本文全部是机制层与 v1.1 排队字段。

## 0. 总览:三段节奏

| 阶段 | 内容 | 工作量 |
|---|---|---|
| **放量前**(必做) | 分片缓存迁移 + 拒收修复线索 + 拒收复现脚本 | 约半天 |
| **放量中** | 字段与提示词零改动,纯数据量增长 | — |
| **放量后**(v1.1) | official/persona/依赖指纹/词表冻结与重审 | 按触发逐项 |

## 1. 放量前必做三件

### 1.1 解读缓存一仓一文件(2026-10-18 修订,取代 256 桶分片)

现状 s8_cache.json 单文件,593 卡无碍,8k+34k 后预估 50-100MB(每改一条整文件
重写 + git 整 blob 重传)。**采用一仓一文件而非 dbhub 的 256 桶分片**——本项目
已有两处成功先例(data/readmes 43k 文件运转正常;公开仓 demo cards/ 本就是
一仓一 md),且与"数据仓库"的产品形态同构:

- 布局:`state/s8_cards/{owner首字母}/{owner}__{repo}.json`(工厂侧存全量 JSON,
  含 raw_verdicts;公开仓的 md/jsonl 是导出产物);
- 写入:单文件原子写(tmp+replace,复用 lib_store._atomic_write),改一卡写一文件,
  脏追踪天然免费(文件存在性+mtime);
- **内容去重保留**:s8_state.json 本就是 fn→sha 索引,增补 sha→首个 fn 的反向表;
  同 sha 的新仓不再烧 API,直接按已有卡复制(dedup 语义与 dbhub sha 键控等价);
- 加载:批量操作(预览/导出/词表聚类)扫目录读文件,本地秒级;
- 容灾:坏一个文件丢一张卡,不再牵连全量;
- 迁移:一次性把 s8_cache.json 按现有 593 张切成文件后删除(无过渡期,量小);
- s8_state.json 保持单文件(小,高频索引)。
- 注:s7 enrich 缓存**维持分片不动**——它是 sha 键控的 API 原始数据,无仓维度,
  一仓一文件不适用;sha 空间稀疏,分片是对的选择。

### 1.2 拒收信息自带修复线索

重试是带拒收原因回炉的,把原因从"判词"升级成"判词+线索":

- 行号闸:`{db/term} 的行号无效: [88]。可用行号: [12, 40, 63]`;
- 枚举闸:非法值后附合法枚举全集;
- 模型重试一次改对率提升,直接降 pass2 与成本。

### 1.3 拒收家族复现脚本(s8_repro.py)

55 行级、只读不写:从 runlog 按失败家族(禁词/行号/截断/结构)各挑代表,
改动后走当前代码全流程复验。与 selftest(few-shot,管"没变坏")互补,
管"修好了"。每次 prompt_ver/清理规则改动后必跑。

## 2. 放量后 v1.1 排队字段(判定方式全部先想死)

### 2.1 official(官方出品判定)——纯程序,零模型成本

`owner ∈ 官方组织集合`(openai/anthropics/google-deepmind/meta-llama/mistralai/
xai-org/QwenLM/deepseek-ai/MoonshotAI/zai-org/…,取 config.ORG_DEDICATED 已有名单
扩展)→ `official: true + of: org`。集合外一律 false,不猜。
展示位:卡片"官方出品"徽标 + 筛选器。**因不烧 API,可与放量同窗实施。**

### 2.2 persona(用户画像三分,AI 域版)

模型直判一枚举(同 ai_role 待遇,接受 ~95% 一致率):`builder`=造 AI 的人用 /
`user`=用 AI 产品的人用 / `operator`=运营管理者用。喂给词表冻结做分层采样。

### 2.3 依赖指纹侦查(治 model_dep/hardware 召回)

零 LLM:GitHub API 取仓库树 + 依赖清单(requirements.txt/pyproject/package.json/
Cargo.toml/go.mod) → 规则映射(含 ollama/openai sdk → provider 信号;
cuda/torch 尺寸 → hardware 佐证)。**只做 xcheck:分歧降 confidence 记备注,
不覆盖裁决**(防迎合,同 install/deprecation 对照闸)。

### 2.4 词表冻结 + 裁决规则 + 更新重审(三件套)

- **冻结**:~5k 卡后对 scenario_tags_free 聚类,从数据冻结双语受控词表(原计划);
- **裁决规则**:配套 _CAT_RULE 式互斥规则进提示词——"专用场景优先于通用;
  awesome 清单固定 ai-knowledge 不参与 domain 竞争;ai_role=ai-enhanced 的
  domain 取产品本体域而非 AI 功能域";
- **更新重审**(retro_audit 等价,补 s8 已知缺口):卡片记 `nominate_ver`;
  提名词表 bump 后,"新增词在本 README 有提名"的卡自动请出缓存重跑
  (判据=裁决覆盖度,非 readme_sha)。基线先落盘,三层回滚照抄。

## 3. 校验层两处精细化

- **按证据形态切换强度**:README 有提名的走行号校验;desc 降级卡维持引句子串
  校验 + confidence 封顶 mid(已有);窗口外候选行号维持"候选清单标注可指认"
  的两级采信(候选提示行直接采信 / 窗口内真命中行验含词)。
- **一致闸口径**:分字段门槛正式化——程序合成字段 ≥98%(1.4 实测 100),
  ai_role/persona 单列 ≥93%,文档标注边界摇摆本性。金标月度复验制度化
  (dbhub readme-monthly 校准窗等价)。

## 4. 不进解读层的(防跑偏)

- 语义向量/混合检索 → MCP 出口阶段整体照抄 dbhub;
- 评分/排行/推荐语 → 永久不做(中立性);
- unattr_judge 全套编排 → 等真实未归类堆积再按需建。
