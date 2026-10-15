# -*- coding: utf-8 -*-
"""s4 · 新项目窗口:创建 45 天内 + stars>=3。

主通道星线(>=10)挡住的 3~9 星新仓从这里进来,每晚最先跑。

用法:
  python s4_collect_new.py                       # 全部 topic
  python s4_collect_new.py --topics llm --max-pages 1
  python s4_collect_new.py --dry-run
"""
import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402

gh._stdout_utf8()


def new_window_slices():
    """新项目窗口切成 3 天一片(超 1000 时按片拆,避免静默截断)。"""
    end = datetime.now(timezone.utc).date()
    start = end - timedelta(days=config.NEW_DAYS)
    days = [(start + timedelta(days=i), start + timedelta(days=i + 3))
            for i in range(0, (end - start).days + 1, 3)]
    return [(a.isoformat(), b.isoformat()) for a, b in days if a <= end]


def sweep_new(topic, max_pages):
    """返回 (records, total_root)。total>1000 时按 3 天片拆分。"""
    base = (f"topic:{topic} fork:false archived:false "
            f"stars:>={config.NEW_STAR_MIN}")
    for r in config.EXCLUDE_REPOS:
        base += f" -repo:{r}"
    q = f"{base} created:>={new_window_slices()[0][0]}"
    items, total = gh.search_repos(q, max_pages=1)
    if total <= max_pages * 100:
        if total > len(items):
            items, _ = gh.search_repos(q, max_pages=max_pages)
        return items, total
    print(f"  [{topic}] total={total} 超单查询上限,按 3 天片拆分")
    out = list(items)
    for a, b in new_window_slices():
        sq = f"{base} created:{a}..{b}"
        sub, _ = gh.search_repos(sq, max_pages=max_pages)
        out.extend(sub)
    return out, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topics", help="逗号分隔,覆盖配置")
    ap.add_argument("--max-pages", type=int, default=10)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    topics = (args.topics.split(",") if args.topics
              else list(config.TOPICS))
    print(f"== s4 新项目窗口 | {len(topics)} 个 topic | "
          f"created>=45 天前 stars>={config.NEW_STAR_MIN} ==")
    for t in topics:
        q = (f"topic:{t} fork:false archived:false created:>=窗口起点 "
             f"stars:>={config.NEW_STAR_MIN}")
        if args.dry_run:
            print(f"[dry] {q}")
            continue
        items, total = sweep_new(t, args.max_pages)
        records = []
        for it in items:
            if it["owner"]["login"] in config.EXCLUDE_USERS:
                continue
            if it["full_name"] in config.EXCLUDE_REPOS:
                continue
            records.append(st.slim(it, f"new:{t}"))
        st.write_part(f"new_{t}", records)
        print(f"  {t}: {len(records)} 条 (total={total})")
    if not args.dry_run:
        print("parts 已写入 data/parts/new_*.json")


if __name__ == "__main__":
    main()
