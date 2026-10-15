# ai_collect — AI 项目采集

参考 dbhub_collect 机制,采集 AI 相关 GitHub 项目。单池、不分国际/国产,
宇宙口径:**stars>=10 + 360 天内有 push + 非 fork + 未归档**(估 3.7 万仓)。

设计文档:`../` 工作区 `ai_collect_plan.md`(topic/org/黑白名单/归档/分片全量方案)。

## 脚本一览(一功能一脚本)

| 脚本 | 功能 |
|---|---|
| `config.py` | 声明式配置:topic / org / watch / 黑白名单 / 口径与分片参数 |
| `lib_gh.py` | GitHub 客户端:代理 / token / 限流 / 重试(所有请求唯一出口) |
| `lib_store.py` | 存储:分片活文件 / 事件日志 / 周度星数点 / parts / 快照 |
| `s1_collect_topics.py` | topic 通道,>1000 自动拆分(星档→年→月) |
| `s2_collect_orgs.py` | org 通道,dedicated / superset 双策略 |
| `s3_collect_watch.py` | watch 白名单保送 |
| `s4_collect_new.py` | 新项目窗口(created≥45d + stars≥3) |
| `s5_merge_pool.py` | 合并:去重 → 分片 → 事件日志 → 快照 → 发现桶统计 |
| `s6_fetch_readmes.py` | README 增量(ETag 304 跳过,100KB 截断,--gc 清残留) |
| `q_pool_query.py` | 历史查询:--stats / --repo [--curve] / --date --entered/--exited |
| `check_strategy.py` | 配置一致性校验(--online 附带核验 org/watch 存在性) |

## 快速开始

```bash
cp .env.example .env         # 填 GITHUB_TOKEN(留空则用 gh auth token)
python check_strategy.py     # 校验配置

# 全量采集(按顺序;每步独立可断点重跑)
python s1_collect_topics.py
python s2_collect_orgs.py
python s3_collect_watch.py
python s4_collect_new.py
python s5_merge_pool.py
python s6_fetch_readmes.py

# 抽样验证(小规模跑通)
python s1_collect_topics.py --topics comfyui --max-pages 10
python s2_collect_orgs.py --orgs deepseek-ai,open-webui
python s3_collect_watch.py
python s4_collect_new.py --topics llm --max-pages 1
python s5_merge_pool.py
python s6_fetch_readmes.py --limit 20
python q_pool_query.py --stats
```

## 数据布局

```
data/live/pool_shard_NN.ndjson    池活文件(repo_id % 8,单文件红线 20MB)
data/events/events_YYYYMMDD.ndjson 每日事件(in/out/chg,append-only)
data/stars/points_YYYYMMDD.ndjson  周度星数点(留 52 周 → 星曲线)
data/parts/*.json                 各通道原始结果(合并输入,不入 git)
data/snapshot_YYYYMMDD/           当日全量 + meta(不入 git)
data/readmes/{owner}__{repo}.md   README 正文
state/                            ETag 等缓存
```

## 工程红线

- 进 git 单文件 ≤ 20MB,超线 → 调大 `config.N_SHARDS` 重跑 `s5`
- 空新池拒绝对非空旧池合并(s5 内置防空池覆盖)
- 事件文件当日已存在时拒绝重写(需 `--force`)
- README 100KB 截断;ETag 304 零成本跳过

## 后续规划(见方案文档)

富集五维(commit/release/security/contrib/lang 分层)→ interpret AI 版解读 →
归档流水线(tar.zst → Releases 月度)→ GitHub Actions 每天两窗调度。
