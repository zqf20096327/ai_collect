# -*- coding: utf-8 -*-
"""s2 · org 通道采集。

dedicated(org 即 AI 产品):星线+活跃线+fork/archived 三道闸。
superset(大厂综合 org):在三道闸之上,要求 挂任一配置 topic 或
描述/名称命中 AI 关键词(挡掉 microsoft 的文档仓/示例仓噪音)。
按 pushed 降序翻页,越过活跃线即提前停止。

用法:
  python s2_collect_orgs.py                       # 全部 org
  python s2_collect_orgs.py --orgs deepseek-ai,open-webui
  python s2_collect_orgs.py --only-dedicated     # 跳过 superset
  python s2_collect_orgs.py --max-pages 2        # 每 org 最多翻 2 页(抽样)
  python s2_collect_orgs.py --dry-run
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

TOPIC_SET = set(config.TOPICS)


def active_cutoff():
    return (datetime.now(timezone.utc)
            - timedelta(days=config.PUSHED_DAYS)).strftime("%Y-%m-%d")


def is_relevant(it):
    """superset 二级过滤:topic 或 名称/描述 关键词。"""
    if TOPIC_SET & set(it.get("topics") or []):
        return True
    text = ((it.get("name") or "") + " " + (it.get("description") or "")).lower()
    return any(k in text for k in config.AI_KEYWORDS)


def sweep_org(org, org_class, max_pages, cutoff, dry):
    q = f"/orgs/{org}/repos (sort=pushed desc, {org_class})"
    if dry:
        print(f"[dry] {q}")
        return None
    print(f"[{org}] {org_class} 采集中", flush=True)
    records, page = [], 1
    skipped_old = 0
    while page <= max_pages:
        _, repos = gh.api_get(f"/orgs/{org}/repos",
                              {"per_page": 100, "page": page,
                               "sort": "pushed", "direction": "desc"})
        if not repos:
            break
        for it in repos:
            if (it.get("pushed_at") or "")[:10] < cutoff:
                skipped_old += 1
                continue  # sort=pushed 保证后面的更老,页末统一 break
            if it.get("fork") or it.get("archived"):
                continue
            if it.get("stargazers_count", 0) < config.STAR_MIN:
                continue
            if org_class == "superset" and not is_relevant(it):
                continue
            if it["owner"]["login"] in config.EXCLUDE_USERS:
                continue
            if it["full_name"] in config.EXCLUDE_REPOS:
                continue
            records.append(st.slim(it, f"org:{org}"))
        last_pushed = min((r.get("pushed_at") or "")[:10] for r in repos)
        if len(repos) < 100 or last_pushed < cutoff:
            break
        page += 1
    st.write_part(f"org_{org}", records)
    print(f"  -> {len(records)} 条 (翻 {page} 页, 越线旧仓 "
          f"{skipped_old}+)", flush=True)
    return len(records)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orgs", help="逗号分隔,覆盖配置(dedicated+superset 混合)")
    ap.add_argument("--only-dedicated", action="store_true")
    ap.add_argument("--max-pages", type=int, default=100,
                    help="每 org 最多翻页数,默认 100")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.orgs:
        chosen = [o.strip() for o in args.orgs.split(",") if o.strip()]
        orgs = [(o, "superset" if o in config.ORG_SUPERSET else "dedicated")
                for o in chosen]
    else:
        orgs = [(o, "dedicated") for o in config.ORG_DEDICATED]
        if not args.only_dedicated:
            orgs += [(o, "superset") for o in config.ORG_SUPERSET]

    print(f"== s2 org 通道 | {len(orgs)} 个 org | "
          f"stars>={config.STAR_MIN} pushed>={config.PUSHED_DAYS}d ==")
    total = 0
    for org, cls in orgs:
        n = sweep_org(org, cls, args.max_pages, active_cutoff(),
                      args.dry_run)
        if n is not None:
            total += n
    if not args.dry_run:
        print(f"合计 {total} 条,parts 已写入 data/parts/")


if __name__ == "__main__":
    main()
