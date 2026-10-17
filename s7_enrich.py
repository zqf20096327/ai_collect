# -*- coding: utf-8 -*-
"""s7 · 信号富集:commit 活跃 / release / GHSA 安全通告 / contributor / 语言构成。

移植自 dbhub enrich(分层增量 + push 依赖二分 + 三振隔离 + 跨窗续跑),
去掉 dbhub 的国产 floor=mid(AI 域无低星分区,纯星数分层)。

分层刷新(REFRESH_DAYS,None = 首轮采过即不再采):
  head(>=1000 星) commit/release 7 天、security 30 天、contrib 90 天、lang 一次
  mid (>=100 星)  commit/release 30 天、security 90 天、contrib/lang 一次
  tail            仅 security 180 天;release/contrib/lang 首轮一次;
                  不采 commit(死活看池 pushed_at,免费)

维度刷新二分(按数据变化成因):
  push 依赖(commit/release/contrib/lang):无 push 物理上不会变——
      首轮必采;此后仅当池 pushed_at 变化且到期才重采
  时间依赖(security):GHSA 披露是外部事件,到期即采
  整仓跳过:pushed_at 未变且无任何到期维度才跳过(死仓每轮只花 security)
  死仓零调用:tail 层 security 180 天轮转,平时不在目标集

状态:state/enrich_state.json(断点/三振/gone)+ state/enrich_cache_shards/
  256 桶信号侧车(sha256(fn) 前 2 位);字段级 dim_ts 防 security-only
  刷新把陈旧 commit/release 值"洗白"成今天。

预算:--max-calls/--max-minutes 按窗发新;Core 触保底线睡到失败响应的
  X-RateLimit-Reset 再续(--wait-windows);Budget/Quota 是全局事件绝不记振
  (dbhub 09-29 事故教训)。

用法:
  python s7_enrich.py --tier all --max-calls 5000 --max-minutes 220 --wait-windows 8
  python s7_enrich.py --tier all --workers 6     # 并发(CORE_PACE 自动限在配额内)
  python s7_enrich.py --tier head              # 只跑头部层
  python s7_enrich.py --only security          # 单维度
  python s7_enrich.py --tier all --dry-run     # 只看到期分布不联网
"""
import argparse
import concurrent.futures
import json
import sys
import time
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402
from lib_enrich_store import EnrichCacheStore  # noqa: E402

gh._stdout_utf8()

STATE = st.STATE / "enrich_state.json"
SUMMARY = st.STATE / "enrich_summary.json"
THREE_STRIKES = 3
DIMS = ("commit", "release", "security", "contrib", "lang")
TIER_STAR = {"head": 1000, "mid": 100, "tail": 0}
TIER_DIMS = {
    "head": ("commit", "release", "security", "contrib", "lang"),
    "mid": ("commit", "release", "security", "contrib", "lang"),
    "tail": ("release", "security", "contrib", "lang"),   # 长尾不采 commit
}
REFRESH_DAYS = {
    "head": {"commit": 7, "release": 7, "security": 30, "contrib": 90, "lang": None},
    "mid":  {"commit": 30, "release": 30, "security": 90, "contrib": None, "lang": None},
    "tail": {"commit": None, "release": None, "security": 180, "contrib": None, "lang": None},
}
SEV_ORDER = {"critical": 4, "high": 3, "moderate": 2, "low": 1}


# ---------------- 小工具 ----------------

def tier_of(stars: int) -> str:
    for name in ("head", "mid"):
        if stars >= TIER_STAR[name]:
            return name
    return "tail"


def iso_days_ago(days: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)) \
        .strftime("%Y-%m-%dT%H:%M:%SZ")


def days_since(date_str: str):
    if not date_str:
        return None
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d") \
            .replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - d).days
    except ValueError:
        return None


def _needs_refresh(rec: dict, dim: str, refresh_days):
    if refresh_days is None:
        return False
    ts = (rec.get("dims") or {}).get(dim)
    if not ts:
        return True
    try:
        done = datetime.strptime(ts, "%Y%m%d").replace(tzinfo=timezone.utc)
    except ValueError:
        return True
    return (datetime.now(timezone.utc) - done).days >= refresh_days


def due_dims(rec: dict, tier: str, pushed_changed: bool) -> list:
    """到期维度:security 到期即采;push 依赖维度首轮必采、其后需
    pushed_at 变化且到期。"""
    due = []
    for d in TIER_DIMS[tier]:
        rd = REFRESH_DAYS[tier][d]
        if d == "security":
            if _needs_refresh(rec, d, rd):
                due.append(d)
        elif not (rec.get("dims") or {}).get(d):
            due.append(d)
        elif pushed_changed and rd and _needs_refresh(rec, d, rd):
            due.append(d)
    return due


# ---------------- 富集端点(api_get + Link header 计数) ----------------

def _link_last_count(headers, body):
    """Link header rel="last" 页码 = 总数;无 Link(单页)返回条数。"""
    link = headers.get("Link", "") or ""
    for part in link.split(","):
        if 'rel="last"' in part:
            for seg in part.split(";"):
                if "page=" in seg:
                    try:
                        return int(
                            seg.strip().split("page=")[-1].strip(" >&\"'"))
                    except ValueError:
                        break
    return len(body) if isinstance(body, list) else None


def commits_count(fn: str, since_iso: str):
    """since 之后的 commit 数(Link 计数)。空仓库 409 视为 0。"""
    gh.CORE_PACE.slot()
    try:
        h, body = gh.api_get(f"/repos/{fn}/commits",
                             {"per_page": 1, "since": since_iso})
    except urllib.error.HTTPError as e:
        if e.code == 409:                     # Git Repository is empty
            return 0
        raise
    return _link_last_count(h, body) or 0


def releases(fn: str):
    gh.CORE_PACE.slot()
    _, body = gh.api_get(f"/repos/{fn}/releases", {"per_page": 12})
    return [x for x in body if not x.get("draft")]


def advisories(fn: str):
    gh.CORE_PACE.slot()
    _, body = gh.api_get(f"/repos/{fn}/security-advisories",
                         {"per_page": 30})
    return body


def contributors_count(fn: str):
    gh.CORE_PACE.slot()
    h, body = gh.api_get(f"/repos/{fn}/contributors",
                         {"per_page": 1, "anon": "false"})
    return _link_last_count(h, body)


def languages(fn: str):
    gh.CORE_PACE.slot()
    _, body = gh.api_get(f"/repos/{fn}/languages")
    return body


# ---------------- 单仓维度采集 ----------------

def collect_dims(fn: str, cache: EnrichCacheStore, dims: tuple,
                 pushed_changed: bool) -> dict:
    """对一个仓库执行到期的维度采集,返回信号字段(异常由调用方处理)。"""
    sig = cache.setdefault(fn, {})
    cache.touch(fn)   # 值字段原地 update,脏桶追踪看不见——采集前显式标脏
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    if "commit" in dims:
        # 7 天必采;90 天条件采——死仓(7 天 0 提交且 pushed_at 未变)的
        # 90 天数不会变,不浪费第二次调用
        c7 = commits_count(fn, iso_days_ago(7))
        if c7 or pushed_changed or "commit_90d" not in sig:
            sig["commit_90d"] = commits_count(fn, iso_days_ago(90))
        sig["commit_7d"] = c7
    if "release" in dims:
        try:
            rels = releases(fn)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                rels = []
            else:
                raise
        if rels:
            latest = rels[0]
            cutoff = (datetime.now(timezone.utc) - timedelta(days=90)) \
                .strftime("%Y-%m-%d")
            n90 = sum(1 for r in rels
                      if (r.get("published_at") or "")[:10] >= cutoff)
            sig.update({"rel_ver": latest.get("tag_name"),
                        "rel_pub": (latest.get("published_at") or "")[:10],
                        "rel_days": days_since(latest.get("published_at") or ""),
                        "rel_n90": n90, "rel_pre": bool(latest.get("prerelease")),
                        "rel_none": False})
        else:
            sig.update({"rel_ver": None, "rel_none": True})
    if "security" in dims:
        try:
            advs = advisories(fn)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                advs = []
            else:
                raise
        live = [a for a in advs if a.get("withdrawn_at") is None]
        worst = max((a.get("severity") for a in live
                     if a.get("severity") in SEV_ORDER),
                    key=lambda s: SEV_ORDER[s], default=None)
        sig.update({"sec_n": len(live),
                    "sec_worst": worst,
                    "sec_last": max(((a.get("published_at") or "")[:10]
                                     for a in live), default=None),
                    "sec_ids": [f'{a.get("ghsa_id")}'
                                f'({a.get("cve_id") or "-"},{a.get("severity")})'
                                for a in live[:8]]})
    if "contrib" in dims:
        try:
            sig["contrib_n"] = contributors_count(fn)
        except urllib.error.HTTPError as e:
            if e.code in (404, 409):
                sig["contrib_n"] = None
            else:
                raise
    if "lang" in dims:
        langs = languages(fn)
        total = sum(langs.values()) or 1
        sig["lang"] = {k: round(v * 100 / total) for k, v in
                       sorted(langs.items(), key=lambda x: -x[1])[:5]}
    sig["enriched_at"] = today
    # 字段级采集时间:security-only 刷新会 bump enriched_at 而不动旧值,
    # 消费侧判断字段新鲜度必须以 dim_ts 为准,防陈旧值被"洗白"
    tsmap = sig.setdefault("dim_ts", {})
    for d in dims:
        tsmap[d] = today
    return sig


# ---------------- 主流程 ----------------

def main():
    ap = argparse.ArgumentParser(
        description="信号富集:commit/release/security/contrib/lang")
    ap.add_argument("--tier", choices=["head", "mid", "tail", "all"],
                    default="all")
    ap.add_argument("--only", choices=DIMS, help="只跑单维度")
    ap.add_argument("--max-calls", type=int, default=5000)
    ap.add_argument("--max-minutes", type=float, default=220.0)
    ap.add_argument("--wait-windows", type=int, default=8,
                    help="Core 触保底线后睡到下一小时窗续跑的最多次数")
    ap.add_argument("--workers", type=int, default=1,
                    help="并发线程数(默认 1=串行,兼容 Actions;本地建议 6,"
                         "CORE_PACE 会把总请求速率压在 core 配额内)")
    ap.add_argument("--limit", type=int, help="最多处理 N 个到期目标(抽样)")
    ap.add_argument("--dry-run", action="store_true",
                    help="只看到期分布不联网")
    args = ap.parse_args()

    pool = list(st.load_pool().values())
    if STATE.is_file():
        s = json.loads(STATE.read_text(encoding="utf-8"))
    else:
        s = {"version": 1, "items": {}}
    items = s.setdefault("items", {})
    cache = EnrichCacheStore()

    tiers = ["head", "mid", "tail"] if args.tier == "all" else [args.tier]
    want_dims = [args.only] if args.only else None

    def pick_due() -> list:
        """到期目标:star 降序;已新鲜(无到期维度——含长尾死仓 pushed_at
        未变)排除。跨窗重取:上窗盖过时间戳的维度自动退出目标集。"""
        out = []
        for it in sorted(pool, key=lambda x: -(x.get("stars") or 0)):
            fn = it["full_name"]
            rec = items.get(fn) or {}
            if rec.get("status") in ("failed", "gone"):
                continue
            tier = tier_of(it.get("stars") or 0)
            if tier not in tiers:
                continue
            changed = (it.get("pushed_at") or "") != rec.get("pushed_checked")
            due = due_dims(rec, tier, changed)
            if want_dims:
                due = [d for d in due if d in want_dims]
            if due:
                out.append(fn)
        return out

    n_tier = {t: sum(1 for it in pool if tier_of(it.get("stars") or 0) == t)
              for t in ("head", "mid", "tail")}
    targets = pick_due()
    if args.limit:
        targets = targets[:args.limit]
    print(f"== s7 富集 | 层 {tiers} | 维度 {want_dims or '按层'} | "
          f"池 {len(pool)}({n_tier}) | 到期目标 {len(targets)} | "
          f"预算 {args.max_calls} 次/{args.max_minutes} 分钟 | "
          f"跨窗等待≤{args.wait_windows} ==")
    if args.dry_run:
        from collections import Counter
        dim_c, tier_c = Counter(), Counter()
        for it in sorted(pool, key=lambda x: -(x.get("stars") or 0)):
            rec = items.get(it["full_name"]) or {}
            if rec.get("status") in ("failed", "gone"):
                continue
            tier = tier_of(it.get("stars") or 0)
            if tier not in tiers:
                continue
            changed = (it.get("pushed_at") or "") != rec.get("pushed_checked")
            due = [d for d in due_dims(rec, tier, changed)
                   if not want_dims or d in want_dims]
            if due:
                tier_c[tier] += 1
                for d in due:
                    dim_c[d] += 1
        print(f"到期分布(按层): {dict(tier_c)}")
        print(f"到期分布(按维): {dict(dim_c)}")
        return

    t0 = time.time()
    deadline = t0 + args.max_minutes * 60
    counts = {"done": 0, "failed": 0, "gone": 0}
    quarantined = []
    stop_reason = None
    windows = waits = stuck_rounds = 0
    by_fn = {it["full_name"]: it for it in pool}

    while True:
        if time.time() >= deadline:
            stop_reason = f"总时长达上限 {args.max_minutes} 分钟"
            break
        targets = pick_due()
        if args.limit:
            targets = targets[:args.limit]
        if not targets:
            break
        # 预算按窗发新(跨窗续跑时各窗各得一份)
        gh.set_budget(gh.Budget(max_calls=args.max_calls,
                                max_minutes=args.max_minutes,
                                reserve_remaining=800))
        windows += 1
        done0 = counts["done"] + counts["failed"] + counts["gone"]
        print(f"[窗 {windows}] 到期目标 {len(targets)} 项", flush=True)
        try:
            BATCH = 50
            for b0 in range(0, len(targets), BATCH):
                batch = targets[b0:b0 + BATCH]
                jobs = []          # (fn, dims, changed):到期维度主线程预算好
                for fn in batch:
                    it = by_fn.get(fn, {})
                    tier = tier_of(it.get("stars") or 0)
                    rec = items.setdefault(fn, {"dims": {}, "fail_count": 0})
                    changed = (it.get("pushed_at") or "") != rec.get("pushed_checked")
                    dims = due_dims(rec, tier, changed)
                    if want_dims:
                        dims = [d for d in dims if d in want_dims]
                    if dims:
                        jobs.append((fn, dims, changed))
                if not jobs:
                    continue
                today = datetime.now(timezone.utc).strftime("%Y%m%d")
                stop_exc = None
                with concurrent.futures.ThreadPoolExecutor(
                        max_workers=max(1, args.workers)) as ex:
                    futs = {ex.submit(collect_dims, fn, cache, tuple(dims),
                                      changed): (fn, dims)
                            for fn, dims, changed in jobs}
                    for fut in concurrent.futures.as_completed(futs):
                        fn, dims = futs[fut]
                        rec = items[fn]
                        try:
                            fut.result()
                            for d in dims:        # 只给真正采到的维度盖时间戳
                                rec.setdefault("dims", {})[d] = today
                            rec["pushed_checked"] = \
                                (by_fn.get(fn) or {}).get("pushed_at") or ""
                            rec["fail_count"] = 0
                            rec.pop("last_error", None)
                            counts["done"] += 1
                        except urllib.error.HTTPError as e:
                            if e.code in (404, 410):   # 仓库已删/私有:标记并隔离
                                rec.update({"status": "gone",
                                            "last_error": f"HTTP {e.code}"})
                                counts["gone"] += 1
                                continue
                            # 其余 HTTP 状态按仓记振继续,绝不 raise:
                            # 毒仓会每晚卡死在同一位置,阻断其后全部目标
                            rec["fail_count"] += 1
                            rec["last_error"] = f"HTTP {e.code}"[:200]
                            if rec["fail_count"] >= THREE_STRIKES:
                                rec["status"] = "failed"
                                quarantined.append(fn)
                            counts["failed"] += 1
                            print(f"  {fn} HTTP {e.code}({rec['fail_count']})",
                                  flush=True)
                            continue
                        except (gh.BudgetOut, gh.CoreReserveOut,
                                gh.QuotaPatienceOut) as e:
                            # 预算/配额停止不算仓库失败:记下首个停止原因,
                            # 取消未启动任务;在飞的很快会自行停止
                            stop_exc = stop_exc or e
                            for f2 in futs:
                                f2.cancel()
                            continue
                        except concurrent.futures.CancelledError:
                            continue            # 预算停止后未跑到的仓,留给下窗
                        except Exception as e:   # noqa: BLE001
                            rec["fail_count"] += 1
                            rec["last_error"] = str(e)[:200]
                            if rec["fail_count"] >= THREE_STRIKES:
                                rec["status"] = "failed"
                                quarantined.append(fn)
                            counts["failed"] += 1
                            print(f"  {fn} 失败({rec['fail_count']}): "
                                  f"{str(e)[:80]}", flush=True)
                            continue
                # 批边界落盘:此刻 executor 已退出、无并发写,flush 安全
                st.atomic_write_json(STATE, s)
                cache.flush()
                print(f"  进度 {min(b0 + BATCH, len(targets))}/{len(targets)}"
                      f" {counts}", flush=True)
                if stop_exc is not None:
                    raise stop_exc
            break                             # 本窗自然扫完且无剩余到期项
        except gh.CoreReserveOut as e:
            # Core 触保底线:按响应头 reset 睡到下一小时窗再续(跨窗推进关键)
            if args.wait_windows <= 0 or waits >= args.wait_windows:
                stop_reason = str(e)
                break
            reset = getattr(e, "reset", None)
            wait_sec = max(5.0, reset - time.time() + 5) if reset else 600.0
            if time.time() + wait_sec > deadline:
                stop_reason = f"{e},等下一窗需 {wait_sec / 60:.0f} 分钟将超总时长"
                break
            waits += 1
            print(f"[跨窗] {e} — 睡 {wait_sec / 60:.0f} 分钟到下一小时窗"
                  f"(等待 {waits}/{args.wait_windows})", flush=True)
            time.sleep(wait_sec)
            continue
        except (gh.BudgetOut, gh.QuotaPatienceOut) as e:
            # 调用数达上限:有进展且允许跨窗 → 发新预算续跑;连续无进展收尾
            progressed = (counts["done"] + counts["failed"]
                          + counts["gone"]) > done0
            stuck_rounds = 0 if progressed else stuck_rounds + 1
            if args.wait_windows <= 0 or stuck_rounds >= 2:
                stop_reason = str(e) + ("(连续无进展,收尾防空转)"
                                        if stuck_rounds >= 2 else "")
                break
            if time.time() >= deadline:
                stop_reason = f"{e},已达总时长上限"
                break
            print(f"[续窗] 本窗停止:{e}(断点已存)", flush=True)
            continue
        finally:
            st.atomic_write_json(STATE, s)
            cache.flush()

    gh.set_budget(None)
    summary = {"tiers": tiers, "dims": want_dims or "per-tier",
               "counts": counts, "windows": windows, "waits": waits,
               "elapsed_min": round((time.time() - t0) / 60, 1),
               "stop_reason": stop_reason, "quarantined": quarantined[:20]}
    st.atomic_write_json(SUMMARY, summary)
    print(f"收工: {counts} | 窗 {windows} | 跨窗等待 {waits} | "
          f"{summary['elapsed_min']} 分钟"
          + (f" | 停因: {stop_reason}" if stop_reason else ""))
    remaining = pick_due()
    print(f"剩余到期: {len(remaining)}(断点已存,重跑同命令续)")
    if quarantined:
        print(f"三振隔离 {len(quarantined)} 项: {quarantined[:10]}")


if __name__ == "__main__":
    main()
