# -*- coding: utf-8 -*-
"""s5 · 合并:parts → 分片活文件 + 事件日志 + 快照。

流程:
  1. 完成门控:当日应跑单元(collect_state)不齐 → 拒绝合并(防假 out)
  2. parts 漂移清理:config 已删通道的残留 part 不再混进合并
  3. 读 data/parts/*.json,按 repo id 去重合并(src 通道并集)
  4. 与旧池(data/live 分片)对比 → 事件 in/out/chg
  5. 写分片活文件、事件日志、当日快照(meta+完成标记,入 git)、meta 摘要
  6. 周一(或 --stars-point)写周度星数点;mark_done("merge") 防同日重并

用法:
  python s5_merge_pool.py
  python s5_merge_pool.py --force          # 今日已合并过仍重做
  python s5_merge_pool.py --allow-partial  # 人工恢复:通道不齐仍合并(慎用)
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
                    help="当日已合并过/事件文件已存在时允许重做")
    ap.add_argument("--stars-point", action="store_true",
                    help="强制写周度星数点(默认周一自动写)")
    ap.add_argument("--allow-partial", action="store_true",
                    help="跳过完成门控(仅人工恢复用:明知通道不齐仍合并)")
    args = ap.parse_args()

    day = st.utc_day()
    print(f"== s5 合并 | day={day} ==")

    # 当日事件文件已存在 = 今日已合并过(本地或早前运行):
    # 重采 parts 与正式合并间有天然漂移,重做会把漂移算成假 out 覆盖正式事件,
    # 故优雅跳过(exit 0)让富集/README 等后续步骤照常跑,而不是整步报错
    if st.events_path(day).exists() and not args.force:
        print(f"当日事件文件已存在 events_{day}.ndjson——今日已合并过,跳过合并;"
              "重做加 --force(会用重采数据重写当日事件,慎用)")
        return

    # 完成门控:应跑单元不齐 = 今晚池采集被预算截断/部分失败,
    # 缺的通道会让全量仓变假 out 并被真删出活池 → 拒绝合并,明晚断点续齐
    done = st.done_tokens(day)
    if "merge" in done and not args.force:
        print("今日已合并过,跳过(重跑加 --force)")
        return
    expected = set(st.expected_tokens())
    missing = sorted(expected - done)
    if missing and not args.allow_partial:
        print(f"[门控] 当日应跑 {len(expected)} 单元缺 {len(missing)} 个,拒绝合并:")
        for m in missing[:10]:
            print(f"    - {m}")
        if len(missing) > 10:
            print(f"    ... 共 {len(missing)} 个")
        print("明晚 s1-s4 断点续采补齐后自动合并;人工恢复可加 --allow-partial")
        return

    # parts 漂移清理:config 删掉的 topic/org 的残留 part 不清会永远混进合并
    keep = st.part_names_expected()
    stale = [p for p in st.parts_files() if p.name not in keep]
    for p in stale:
        p.unlink()
        print(f"[parts 清理] 删除 config 漂移残留: {p.name}")

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

    # 当日快照(瘦身版):meta + 完成标记入 git;全池历史由 live 分片 +
    # events + 周度星数点回放,不再落 33MB/天 的全池副本
    snap = st.snapshot_dir(day)
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
    st.atomic_write_json(snap / "pool.json",
                         {"date": day, "count": len(new_pool),
                          "merged": True})
    st.mark_done("merge")
    print(f"通道分布: {chan}")
    print(f"发现桶(仅被 topic:ai 捞到): {disc_bucket} 仓")
    print(f"快照: data/snapshot_{day}/ (meta.json + pool.json 完成标记)")


if __name__ == "__main__":
    main()
