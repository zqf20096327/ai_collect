# -*- coding: utf-8 -*-
"""s5 · 合并:parts → 分片活文件 + 事件日志 + 快照。

流程:
  1. 读 data/parts/*.json,按 repo id 去重合并(src 通道并集)
  2. 黑名单过滤(双保险第二层;查询层是第一层)
  3. 与旧池(data/live 分片)对比 → 事件 in/out/chg
  4. 写分片活文件、事件日志、当日快照(不入 git)、meta 摘要
  5. 周一(或 --stars-point)写周度星数点

用法:
  python s5_merge_pool.py
  python s5_merge_pool.py --force          # 事件文件已存在时允许重写
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_store as st  # noqa: E402

st  # silence linters; keep import explicit for PATH consistency
import lib_gh as gh  # noqa: E402

gh._stdout_utf8()


def merge_parts():
    """parts 去重合并:id -> record。"""
    pool = {}
    for p in st.parts_files():
        for rec in json.loads(p.read_text(encoding="utf-8")):
            rid = rec["id"]
            if rec.get("owner") in config.EXCLUDE_USERS:
                continue
            if rec.get("full_name") in config.EXCLUDE_REPOS:
                continue
            cur = pool.get(rid)
            if cur is None:
                pool[rid] = rec
            else:
                cur["src"] = sorted(set(cur["src"]) | set(rec["src"]))
                cur["stars"] = max(cur.get("stars", 0), rec.get("stars", 0))
                if (rec.get("pushed_at") or "") > (cur.get("pushed_at") or ""):
                    cur["pushed_at"] = rec["pushed_at"]
    return pool


def diff_events(old_pool, new_pool, day):
    """对比新旧池 → 事件列表。"""
    events = []
    for rid, rec in new_pool.items():
        old = old_pool.get(rid)
        if old is None:
            rec["first_seen"] = day
            events.append({"type": "in", "date": day, "id": rid,
                           "repo": rec["full_name"],
                           "stars": rec.get("stars", 0),
                           "src": rec["src"]})
            continue
        rec["first_seen"] = old.get("first_seen", day)
        chg = {}
        if old.get("stars", 0) != rec.get("stars", 0):
            chg["stars_old"], chg["stars_new"] = old.get("stars"), rec.get("stars")
        if old.get("pushed_at") != rec.get("pushed_at"):
            chg["pushed_new"] = rec.get("pushed_at")
        if old.get("description") != rec.get("description"):
            chg["desc_changed"] = True
        ta = sorted(set(rec.get("topics", [])) - set(old.get("topics", [])))
        if ta:
            chg["topics_added"] = ta
        if chg:
            events.append({"type": "chg", "date": day, "id": rid,
                           "repo": rec["full_name"], **chg})
    for rid, old in old_pool.items():
        if rid not in new_pool:
            events.append({"type": "out", "date": day, "id": rid,
                           "repo": old["full_name"],
                           "stars_old": old.get("stars", 0),
                           "reason": "filtered_or_absent"})
    return events


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true",
                    help="当日事件文件已存在时允许重写")
    ap.add_argument("--stars-point", action="store_true",
                    help="强制写周度星数点(默认周一自动写)")
    args = ap.parse_args()

    day = st.utc_day()
    print(f"== s5 合并 | day={day} ==")
    old_pool = st.load_pool()
    print(f"旧池: {len(old_pool)} 仓")

    new_pool = merge_parts()
    print(f"新采集(去重后): {len(new_pool)} 仓")
    if not new_pool and old_pool:
        raise SystemExit("新池为空但旧池非空——疑似采集失败,拒绝合并(防空池覆盖)")

    events = diff_events(old_pool, new_pool, day)
    n_in = sum(1 for e in events if e["type"] == "in")
    n_out = sum(1 for e in events if e["type"] == "out")
    n_chg = sum(1 for e in events if e["type"] == "chg")
    print(f"事件: in={n_in} out={n_out} chg={n_chg}")

    sizes = st.save_pool(new_pool)
    over = [f"shard_{i:02d}={sz/1e6:.1f}MB" for i, sz in sizes.items()
            if sz > config.SHARD_MAX_MB * 1e6]
    print("分片: " + ", ".join(
        f"{i:02d}:{sz/1e6:.1f}MB" for i, sz in sorted(sizes.items())))
    if over:
        print(f"[红线告警] 超过 {config.SHARD_MAX_MB}MB 的分片: {over} "
              f"→ 调大 config.N_SHARDS 后重跑本脚本")

    if events:
        st.write_events(day, events, force=args.force)

    import datetime as _dt
    if args.stars_point or _dt.datetime.now(_dt.timezone.utc).weekday() == 0:
        st.write_stars_point(day, new_pool)
        print("周度星数点已写入 data/stars/")

    # 当日全量快照 + meta(不入 git)
    snap = st.snapshot_dir(day)
    pool_json = "\n".join(json.dumps(r, ensure_ascii=False)
                          for r in sorted(new_pool.values(),
                                          key=lambda x: -x.get("stars", 0)))
    (snap / "pool.ndjson").write_text(pool_json, encoding="utf-8")

    chan = {}
    disc_bucket = 0
    for rec in new_pool.values():
        for s in rec["src"]:
            key = s.split(":")[0]
            chan[key] = chan.get(key, 0) + 1
        if rec["src"] == ["topic:ai"]:
            disc_bucket += 1
    meta = {"date": day, "pool_size": len(new_pool), "in": n_in,
            "out": n_out, "chg": n_chg, "channels": chan,
            "discovery_bucket": disc_bucket,
            "shard_bytes": {str(k): v for k, v in sizes.items()}}
    (snap / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"通道分布: {chan}")
    print(f"发现桶(仅被 topic:ai 捞到): {disc_bucket} 仓")
    print(f"快照: data/snapshot_{day}/ (pool.ndjson + meta.json)")


if __name__ == "__main__":
    main()
