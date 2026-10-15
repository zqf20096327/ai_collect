# -*- coding: utf-8 -*-
"""s1 · topic 通道采集。

每个 topic 一条基查询(stars>=10 + 360 天活跃 + 非 fork + 未归档),
total>1000 自动拆分:星档 → 创建年 → 创建月(叶子取 top,按星降序)。

用法:
  python s1_collect_topics.py                          # 全部 20 个 topic
  python s1_collect_topics.py --topics llm,rag         # 指定 topic
  python s1_collect_topics.py --limit 3                # 前 3 个 topic(抽样)
  python s1_collect_topics.py --max-pages 2            # 每条查询最多翻 2 页(抽样)
  python s1_collect_topics.py --dry-run                # 只打印查询不联网
"""
import argparse
import calendar
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402

gh._stdout_utf8()

STAR_BANDS = [(10000, None), (2000, 10000), (500, 2000), (100, 500),
              (10, 100)]


def star_bands():
    """星档:高到低,最低档下界 = 配置星线。"""
    bands = [(10000, None), (2000, 10000), (500, 2000), (100, 500)]
    if config.STAR_MIN < 100:
        bands.append((config.STAR_MIN, 100))
    return bands


def star_q(lo, hi):
    return f"stars:>={lo}" if hi is None else f"stars:{lo}..{hi}"


def base_query(topic):
    """不带星线:星档拆分时由子查询各自带(同名限定词 GitHub 只认第一个,
    基查询带了 stars:>=10 会让星档 stars:>=10000 整个被忽略)。"""
    cutoff = (datetime.now(timezone.utc)
              - timedelta(days=config.PUSHED_DAYS)).date().isoformat()
    q = f"topic:{topic} fork:false archived:false pushed:>={cutoff}"
    for r in config.EXCLUDE_REPOS:
        q += f" -repo:{r}"
    return q


def sweep(base, max_pages, depth, stats, star=None, year=None):
    """抓一条查询;>1000 时按 星档→年→月 递归拆。

    base 不带任何 stars/created 限定词(同名限定词 GitHub 只认第一个,
    拼接必重复);星档/年份走参数显式传递。子查询失败只跳过并计数。
    """
    q = base
    if depth == 0:
        q += f" stars:>={config.STAR_MIN}"
    if star:
        q += " " + star_q(*star)
    if year:
        q += f" created:{year}-01-01..{year}-12-31"
    items, total = gh.search_repos(q, max_pages=1)
    stats["queries"] += 1
    if total <= 1000 or depth >= 3:
        if total > 1000:
            print(f"    [warn] 叶子层仍 >1000({total}),取星数 top "
                  f"{max_pages * 100}", flush=True)
        if total > len(items):
            items, _ = gh.search_repos(q, max_pages=max_pages)
        return items, total
    out = list(items)
    print(f"    total={total} > 1000,depth={depth} 拆分中", flush=True)
    now = datetime.now(timezone.utc).year
    if depth == 0:
        subs = [dict(star=b) for b in star_bands()]
    elif depth == 1:                      # 星档内按年拆,星档保留
        subs = [dict(star=star, year=y) for y in range(2008, now + 1)]
    else:                                 # 年内按月拆,月末日按真实日历
        subs = [dict(month=(year, m, calendar.monthrange(year, m)[1]))
                for m in range(1, 13)]
    for kw in subs:
        try:
            if "month" in kw:
                y, m, last = kw["month"]
                mq = base
                if star:
                    mq += " " + star_q(*star)
                mq += f" created:{y}-{m:02d}-01..{y}-{m:02d}-{last:02d}"
                sub_items, _ = sweep_leaf(mq, max_pages, stats)
            else:
                sub_items, _ = sweep(base, max_pages, depth + 1, stats, **kw)
        except Exception as e:
            stats["errors"] = stats.get("errors", 0) + 1
            print(f"    [error] 子查询失败跳过: {e}", flush=True)
            continue
        out.extend(sub_items)
    return out, total


def sweep_leaf(q, max_pages, stats):
    items, total = gh.search_repos(q, max_pages=1)
    stats["queries"] += 1
    if total > 1000:
        print(f"    [warn] 叶子层仍 >1000({total}),取星数 top "
              f"{max_pages * 100}", flush=True)
    if total > len(items):
        items, _ = gh.search_repos(q, max_pages=max_pages)
    return items, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topics", help="逗号分隔,覆盖配置")
    ap.add_argument("--limit", type=int, help="只跑前 N 个 topic(抽样)")
    ap.add_argument("--max-pages", type=int, default=10,
                    help="每条查询最多翻页数,默认 10(=1000 条)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    topics = (args.topics.split(",") if args.topics
              else list(config.TOPICS))
    if args.topics:
        bad = [t for t in topics if t not in config.TOPICS]
        if bad:
            print(f"[skip] 不在配置清单里(如需采集请加进 config.TOPICS): {bad}")
            topics = [t for t in topics if t in config.TOPICS]
    if args.limit:
        topics = topics[:args.limit]

    print(f"== s1 topic 通道 | {len(topics)} 个 topic | "
          f"stars>={config.STAR_MIN} pushed>={config.PUSHED_DAYS}d | "
          f"max_pages={args.max_pages} ==")
    stats = {"queries": 0}
    for t in topics:
        q = base_query(t)
        if args.dry_run:
            print(f"[dry] {q}")
            continue
        print(f"[{t}] {q} (stars:>={config.STAR_MIN} 由根查询补)",
              flush=True)
        items, total = sweep(q, args.max_pages, 0, stats)
        seen, records = set(), []
        for it in items:
            if it["id"] in seen:
                continue
            seen.add(it["id"])
            if it["owner"]["login"] in config.EXCLUDE_USERS:
                continue
            if it["full_name"] in config.EXCLUDE_REPOS:
                continue
            records.append(st.slim(it, f"topic:{t}"))
        st.write_part(f"topic_{t}", records)
        print(f"  -> 去重后 {len(records)} 条 (total_count={total}, "
              f"查询 {stats['queries']} 次)", flush=True)
        stats["queries"] = 0
    if not args.dry_run:
        print("parts 已写入 data/parts/,下一步: python s5_merge_pool.py")


if __name__ == "__main__":
    main()
