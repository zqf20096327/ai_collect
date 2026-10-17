# ai_collect 采集策略对齐 dbhub_collect(通俗版)

## 目标

把 dbhub_collect 的六套成熟机制移植进 ai_collect 现有代码结构(保留 s1-s7 脚本 + lib_gh/lib_store,不搬 dbhub 的架构),ai 已有的优势不动:并发翻页+Pacer 限速、events 事件日志、周度星数点、8 分片 live。

## 六项改造

**1. 预算管家 + 断点续采(lib_gh.py / lib_store.py / s1-s5)**
- lib_gh.py 加 `Budget` 类(max_calls/max_minutes/reserve,线程安全)与异常 BudgetOut / CoreReserveOut(带 reset 时刻)/ QuotaPatienceOut;api_get 请求前查预算,core 配额触保底线抛 CoreReserveOut,调用方睡到下一小时窗续跑(最多 N 次)。
- lib_store.py 加 `atomic_write_json`(原子写+3 份轮转+LF)。
- s1-s4 加 `state/collect_state.json` 断点(token 粒度:topic:{t}/new:{t}/org:{o}/watch/merge,同日期恢复),每完成一个单元写 part+checkpoint;池阶段共享 90 分钟墙钟。
- s5 合并门控:config 推导的应跑 token 不齐 → 跳过 merge 与事件写出(防预算截断夜产生假 out);保留空池保护。

**2. README 三件套(s6_fetch_readmes.py 重写)**
- `state/readme_state.json`(status/fail_count/etag/sha/checked_pushed/calibrated/last_error)。
- weekly:池 pushed_at 变化才拉;monthly(每月 1 号自动/workflow 可 force):全池 ETag 校准,304 不耗配额,calibrated 日戳跨 run 接力;新入池仓天然进 weekly,stars 降序。
- 状态机 done/oversized(>100KB 截断)/no_readme/failed,失败三振隔离;Budget 类异常不记振。
- normalize+sha1[:12] 内容级去重记入 state;预算 --max-calls/--max-minutes/--wait-windows/--max-total-minutes,每 200 条 checkpoint;保留 6 线程。
- 一次性播种:从现有 readme_etags.json + 6787 个 md 生成 items(checked_pushed=池 pushed_at,calibrated=当日);移除 --new-only/--limit/--gc。前置:本地 42k README 回填完成并推送后再切换。

**3. 五维富集(s7_enrich.py 新增,已拍板全量纳入)**
- 移植 dbhub enrich.py+enrich_store.py:commit 活跃(Link 计数)/release(最新 tag+90 天 n)/GHSA 安全/contributor 计数/语言前 5。
- 分层:head(≥1000 星)commit/release 7 天、security 30 天、contrib 90 天、lang 一次;mid(≥100)30/30/90;tail 仅 security 180 天+首轮其余一次。去掉 dbhub 的国产 floor。
- push 依赖二分:四维首采无条件、之后需 pushed_at 变化且到期;security 到期即采。
- 目标 stars 降序,首轮 15-20 万调用高星先落(夜窗 5000/晚约 4-6 周);state/enrich_state.json + enrich_cache_shards/ 256 桶。

**4. 出池宽限(tools/purge_outpool.py 移植)**
- 每晚 --stamp 写 state/absent_since.json(零 API);每月 1 号 dry-run 清单,人工过目后本地 --apply(md 移入备份目录+manifest);宽限 30 天/黑名单 7 天;守卫:三振仓跳过、安全名共享跳过、单次 limit 500。

**5. 快照瘦身 + Releases 归档(已拍板瘦身)**
- s5 快照只留 meta.json+完成标记(几 KB/天)入 git,取消 33MB 全池副本;激活 SNAP_LATEST:每晚从 live 分片生成 data/snapshot_latest/pool.json 作 enrich/readme 输入桥(不入 git)。
- tools/release_archive.py+archive_snapshot.py 移植:≥15 天目录 tar.zst 上 Releases(按月 archive-YYYY-MM),digest 校验幂等、不一致拒绝覆盖,仓库 slug 从 git remote 解析。
- .gitignore:取消忽略 data/snapshot_*/;新增 state/*.json.[0-9]、_archive_tmp/、enrich_cache_shards/*.tmp。

**6. workflow 重排(collect.yml + 新增 readme-monthly.yml)**
- collect.yml:timeout 300→360;JOB_T0 自计时;采集步骤显式传 GITHUB_TOKEN;顺序 s1-s4 → s5 门控合并 → snapshot_latest 桥 → s7 富集(5000 次/220 分钟/wait-windows 8)→ s6 README(4200 次/60 分钟/wait-windows 10/总时长=剩余-10 分钟,每月 1 号自动 monthly,dispatch 可 force_monthly)→ absent 打戳 → 月度 purge dry-run → 归档 rotate → 提交(5 轮 rebase+40s 重试,保留 if:always)。cron 保持 0 13 * * *。
- readme-monthly.yml:仅手动 dispatch(参数 max_total_minutes),同 concurrency 组 collect,跑 monthly 接力校准。

## 实施顺序与验证

P1 预算管家 → P2 断点+门控 → P3 README → P4 富集 → P5 清理+归档 → P6 workflow → P7 check_strategy.py 扩展检查 + 本地逐脚本 dry-run + workflow_dispatch 手动跑一晚观察配额与 checkpoint。

## 不移植

org 周扫携带(ai org 通道每晚仅 ~200 调用)、db_profiles/strategy 双层配置、interpret 解读层耦合、pool_intl/pool_cn 双侧活文件。

## 风险与回滚

播种用池 pushed_at 最多少抓一轮周更(月度校准兜底);首周富集吃满 220 分钟属预期;所有新状态文件独立、live/events/readmes 格式不变,回退 collect.yml 到上一 commit 即恢复旧行为;42k 月度校准单窗跑不完由 calibrated 接力+手动补跑兜底。