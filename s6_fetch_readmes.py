# -*- coding: utf-8 -*-
"""s6 · README 采集:weekly 增量 / monthly 全量校准 / init(移植自 dbhub readme_sweep)。

三模式:
  weekly   仅池 pushed_at 晚于 checked_pushed 的仓(新入池无记录天然 due),
           排除 no_readme/failed(三振隔离)
  monthly  全量 ETag 校准(304 不耗配额),排除本 UTC 日已校准项——
           calibrated 日戳跨 run 接力,跑不完次晚/手动窗口接着扫不重烧
  init     全池按星数降序铺(老体系迁移/灾后重建用)

状态机:pending → done / oversized(>100KB 截断)/ no_readme(404 或空文本)/
  failed(三振隔离)。Budget/QuotaPatience 是全局事件,绝不记单仓振次
  (dbhub 09-29 事故:预算触线被记成假振次,三晚错隔离 2.4k 仓)。
预算:--max-calls/--max-minutes 按窗发新 + --reserve core 保底线;
  触线睡到失败响应的 X-RateLimit-Reset 再续(--wait-windows 上限次);
  --max-total-minutes 管整次调用含等待的墙钟。
播种:每次运行幂等补种老 state/readme_etags.json 里 items 缺失的仓
  (checked_pushed 取池值、calibrated=当日),本地回填/推送时序解耦;
  老文件保留不动(退役文件,稳定后清理)。

用法:
  python s6_fetch_readmes.py --mode weekly
  python s6_fetch_readmes.py --mode monthly --max-total-minutes 300
  python s6_fetch_readmes.py --mode weekly --only owner/repo
  python s6_fetch_readmes.py --mode weekly --dry-run
"""
import argparse
import hashlib
import json
import re
import sys
import threading
import time
import urllib.error
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402

gh._stdout_utf8()

STATE = st.STATE / "readme_state.json"
LEGACY_ETAGS = st.STATE / "readme_etags.json"
THREE_STRIKES = 3
CAL_DATE = datetime.now(timezone.utc).strftime("%Y%m%d")


# ---------------- 归一化 + SHA(内容级去重键,跨仓同内容共用) ----------------

def normalize(txt: str) -> str:
    """剥徽章/链接/HTML/URL/空白——只留语义文本。"""
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", txt or "")
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"https?://\S+", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def sha1_of(txt: str) -> str:
    return hashlib.sha1(txt.encode("utf-8", "ignore")).hexdigest()[:12]


def readme_path(fn: str) -> Path:
    return st.READMES / (fn.replace("/", "__") + ".md")


# ---------------- 状态 ----------------

def load_state() -> dict:
    if STATE.is_file():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"version": 2, "items": {}}


def save_state(s: dict) -> None:
    st.atomic_write_json(STATE, s)


def seed_from_legacy(items: dict, pushed_of: dict) -> int:
    """幂等补种:老 etags 里 items 还没有的仓,从已落盘 md 补进状态机。
    本地回填与推送时序不可控,每跑一次补一次直到补齐;老 etags 清理后自动失效。"""
    if not LEGACY_ETAGS.is_file():
        return 0
    try:
        etags = json.loads(LEGACY_ETAGS.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0
    n = 0
    for fn, etag in etags.items():
        if fn in items or fn not in pushed_of or not readme_path(fn).is_file():
            continue        # 已有/不在池/无正文的跳过,无正文保持 pending
        text = readme_path(fn).read_text(encoding="utf-8", errors="replace")
        items[fn] = {
            "status": "done",      # oversized 历史未知,按 done;月度校准会修正
            "etag": etag, "sha": sha1_of(normalize(text)), "updated": "",
            "checked_pushed": pushed_of.get(fn) or "",
            "fail_count": 0, "last_error": "", "calibrated": CAL_DATE,
        }
        n += 1
    return n


# ---------------- 目标挑选 ----------------

def pick_targets(mode: str, pool: list, items: dict) -> list:
    """按模式取待扫目标(池按星数降序;monthly 排除当日已校准项防跨窗重扫)。"""
    ordered = sorted(pool, key=lambda x: -(x.get("stars") or 0))
    if mode == "init":
        skip = ("done", "oversized", "no_readme", "failed")
        return [r["full_name"] for r in ordered
                if (items.get(r["full_name"]) or {}).get("status") not in skip]
    if mode == "weekly":
        return [r["full_name"] for r in ordered
                if (r.get("pushed_at") or "")
                > (items.get(r["full_name"]) or {}).get("checked_pushed", "")
                and (items.get(r["full_name"]) or {}).get("status")
                not in ("no_readme", "failed")]
    # monthly:calibrated != 本 UTC 日
    return [r["full_name"] for r in ordered
            if (items.get(r["full_name"]) or {}).get("calibrated") != CAL_DATE]


# ---------------- 单仓处理 ----------------

def process(fn: str, rec: dict, pushed: str):
    """条件请求 + 状态更新,返回结果种类;Budget 族异常上抛给窗口层。"""
    etag = rec.get("etag")
    extra = {"If-None-Match": etag} if etag else None
    gh.CORE_PACE.slot()
    try:
        headers, body = gh.api_get(f"/repos/{fn}/readme",
                                   accept="application/vnd.github.raw+json",
                                   extra_headers=extra, want="raw")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            rec.update({"status": "no_readme", "etag": None, "fail_count": 0,
                        "last_error": "", "calibrated": CAL_DATE})
            return "no_readme"
        rec["fail_count"] = rec.get("fail_count", 0) + 1
        rec["last_error"] = f"HTTP {e.code}"[:200]
        if rec["fail_count"] >= THREE_STRIKES:
            rec["status"] = "failed"
        return "failed"
    except (gh.BudgetOut, gh.QuotaPatienceOut):
        raise
    except Exception as e:                     # 网络抖动等:按仓记振,毒仓不阻断
        rec["fail_count"] = rec.get("fail_count", 0) + 1
        rec["last_error"] = str(e)[:200]
        if rec["fail_count"] >= THREE_STRIKES:
            rec["status"] = "failed"
        return "failed"
    if body is None:                           # 304:免费,视为已校验
        rec["checked_pushed"] = pushed
        rec["calibrated"] = CAL_DATE
        return "not_modified"
    text = body.decode("utf-8", errors="replace")
    if not text.strip():
        rec.update({"status": "no_readme", "etag": None, "fail_count": 0,
                    "last_error": "", "calibrated": CAL_DATE})
        return "no_readme"
    truncated = len(body) > config.README_MAX_BYTES
    if truncated:
        text = text[:config.README_MAX_BYTES]
    with open(readme_path(fn), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    rec.update({"status": "oversized" if truncated else "done",
                "etag": headers.get("ETag") or etag,
                "sha": sha1_of(normalize(text)),
                "updated": datetime.now(timezone.utc).strftime("%Y%m%d"),
                "checked_pushed": pushed,
                "fail_count": 0, "last_error": "", "calibrated": CAL_DATE})
    return "oversized" if truncated else "done"


# ---------------- 主流程 ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True,
                    choices=["weekly", "monthly", "init"])
    ap.add_argument("--max-calls", type=int, default=4200,
                    help="每窗调用上限(默认 4200 = 5000 小时帽 − 800 保底线)")
    ap.add_argument("--max-minutes", type=float, default=60,
                    help="每窗墙钟上限,默认 60 分钟")
    ap.add_argument("--max-total-minutes", type=float, default=None,
                    help="整次调用(含跨窗等待)的墙钟上限")
    ap.add_argument("--wait-windows", type=int, default=10,
                    help="Core 触保底线时睡到下一小时窗续跑的最多次数")
    ap.add_argument("--reserve", type=int, default=800,
                    help="core 剩余配额保底线")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--only", help="只处理指定仓(逗号分隔,调试用)")
    ap.add_argument("--dry-run", action="store_true", help="只挑目标不联网")
    args = ap.parse_args()

    pool = list(st.load_pool().values())
    pushed_of = {r["full_name"]: r.get("pushed_at") or "" for r in pool}
    s = load_state()
    items = s.setdefault("items", {})
    n = seed_from_legacy(items, pushed_of)
    if n:
        save_state(s)
        print(f"[补种] 从老 readme_etags.json 补进 {n} 仓 → 新状态机")

    targets = pick_targets(args.mode, pool, items)
    if args.only:
        only = {x.strip() for x in args.only.split(",") if x.strip()}
        targets = [t for t in targets if t in only] or sorted(only)
    print(f"== s6 README | mode={args.mode} | 池 {len(pool)} | "
          f"目标 {len(targets)} | 预算 {args.max_calls} 次/{args.max_minutes} 分钟 | "
          f"跨窗等待≤{args.wait_windows} | 总时长 "
          f"{args.max_total_minutes or '∞'} 分钟 ==")
    if args.dry_run or not targets:
        st_counts = {}
        for rec in items.values():
            st_counts[rec.get("status", "pending")] = \
                st_counts.get(rec.get("status", "pending"), 0) + 1
        print(f"状态分布: {st_counts}")
        return

    t0 = time.time()
    deadline = t0 + args.max_total_minutes * 60 if args.max_total_minutes else None
    counts = {"done": 0, "oversized": 0, "not_modified": 0,
              "no_readme": 0, "failed": 0}
    stop_reason = None
    windows = waits = 0
    processed_n = [0]                                   # 主线程计数(checkpoint 用)

    def work(fn):
        if stop_evt.is_set():
            return None
        rec = items.setdefault(fn, {"status": "pending", "fail_count": 0})
        if rec.get("status") == "failed":
            return None                                 # 三振隔离,不浪费配额
        try:
            return process(fn, rec, pushed_of.get(fn, ""))
        except (gh.BudgetOut, gh.QuotaPatienceOut) as e:
            stop_evt.set()
            return e

    while targets:
        if deadline and time.time() >= deadline:
            stop_reason = f"总时长达上限 {args.max_total_minutes} 分钟"
            break
        # 每窗发新预算(跨窗续跑时各窗各得一份 max_calls/max_minutes)
        gh.set_budget(gh.Budget(max_calls=args.max_calls,
                                max_minutes=args.max_minutes,
                                reserve_remaining=args.reserve))
        stop_evt = threading.Event()
        windows += 1
        round_exc = None
        print(f"[窗 {windows}] 目标 {len(targets)} 项", flush=True)
        try:
            with ThreadPoolExecutor(args.workers) as ex:
                for outcome in ex.map(work, targets):
                    if isinstance(outcome, Exception):
                        round_exc = outcome
                        break
                    if outcome is not None:
                        counts[outcome] = counts.get(outcome, 0) + 1
                        processed_n[0] += 1
                        if processed_n[0] % 200 == 0:
                            save_state(s)
                            print(f"  进度 {processed_n[0]}/{len(targets)} "
                                  f"{counts}", flush=True)
        finally:
            save_state(s)
        if round_exc is None:
            nxt = pick_targets(args.mode, pool, items)
            if len(nxt) < len(targets):                 # 目标集仍在收缩才续
                targets = nxt
                continue
            break
        if not isinstance(round_exc, (gh.CoreReserveOut, gh.QuotaPatienceOut)):
            stop_reason = str(round_exc)                # BudgetOut 自然到顶
            break
        if waits >= args.wait_windows:
            stop_reason = f"{round_exc},跨窗等待 {args.wait_windows} 次已用尽"
            break
        reset = getattr(round_exc, "reset", None)
        wait_sec = max(5.0, reset - time.time() + 5) if reset else 600.0
        if deadline and time.time() + wait_sec > deadline:
            stop_reason = (f"{round_exc},等下一窗需 {wait_sec / 60:.0f} 分钟"
                           f"将超总时长上限")
            break
        waits += 1
        print(f"[跨窗] {round_exc} — 睡 {wait_sec / 60:.0f} 分钟到下一小时窗"
              f"(等待 {waits}/{args.wait_windows})", flush=True)
        time.sleep(wait_sec)
        targets = pick_targets(args.mode, pool, items)

    gh.set_budget(None)
    mins = (time.time() - t0) / 60
    print(f"收工: {counts} | 窗 {windows} | 跨窗等待 {waits} | "
          f"{mins:.0f} 分钟" + (f" | 停因: {stop_reason}" if stop_reason else ""))
    remaining = pick_targets(args.mode, pool, items)
    print(f"剩余目标: {len(remaining)}(monthly 未完项由 calibrated 日戳接力,"
          f"次晚/手动窗口续扫)")


if __name__ == "__main__":
    main()
