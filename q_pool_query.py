# -*- coding: utf-8 -*-
"""q · 历史查询工具(四个入口)。

  python q_pool_query.py --stats                          # 池/分片/事件总览
  python q_pool_query.py --repo owner/name                # 当前记录 + 事件时间线
  python q_pool_query.py --repo owner/name --curve        # 星数曲线(事件+周度点)
  python q_pool_query.py --date 20261015 --entered        # 某日进池明细
  python q_pool_query.py --date 20261015 --exited
  python q_pool_query.py --date 20261015 --entered --top 20
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_store as st  # noqa: E402


def u():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def repo_events(full_name):
    out = []
    for p in st.all_event_files():
        for line in p.read_text(encoding="utf-8").split("\n"):
            if not line.strip():
                continue
            e = json.loads(line)
            if e.get("repo") == full_name:
                out.append(e)
    return out


def cmd_stats():
    pool = st.load_pool()
    print(f"池: {len(pool)} 仓")
    chan = {}
    for r in pool.values():
        for s in r["src"]:
            k = s.split(":")[0]
            chan[k] = chan.get(k, 0) + 1
    print(f"通道分布: {chan}")
    disc = sum(1 for r in pool.values() if r["src"] == ["topic:ai"])
    print(f"发现桶(仅 topic:ai): {disc}")
    shards = sorted(st.LIVE.glob("pool_shard_*.ndjson"))
    bad = []
    for p in shards:
        mb = p.stat().st_size / 1e6
        flag = " <= 红线告警!" if mb > config.SHARD_MAX_MB else ""
        if flag:
            bad.append(p.name)
        print(f"  {p.name}: {mb:.1f}MB{flag}")
    evs = st.all_event_files()
    print(f"事件文件: {len(evs)} 份,最近: {evs[-1].name if evs else '无'}")
    n_rd = len(list(st.READMES.glob('*.md')))
    print(f"README: {n_rd} 份")
    top = sorted(pool.values(), key=lambda r: -r.get("stars", 0))[:10]
    print("Top10:")
    for r in top:
        print(f"  {r['stars']:>7}  {r['full_name']}  src={','.join(r['src'])}")


def cmd_repo(full_name, curve):
    pool = st.load_pool()
    rec = next((r for r in pool.values()
                if r["full_name"].lower() == full_name.lower()), None)
    if rec:
        print(json.dumps(rec, ensure_ascii=False, indent=1))
    else:
        print(f"[note] {full_name} 不在当前池(可能已出池或从未入池)")
    evs = repo_events(full_name)
    if not evs:
        print("(无事件记录)")
        return
    print(f"事件时间线({len(evs)} 条):")
    if curve:
        for e in evs:
            if e["type"] == "in":
                print(f"  {e['date']}  in   stars={e.get('stars')}")
            elif e["type"] == "out":
                print(f"  {e['date']}  OUT  stars_old={e.get('stars_old')} "
                      f"reason={e.get('reason')}")
            else:
                if "stars_new" in e:
                    print(f"  {e['date']}  chg  stars "
                          f"{e.get('stars_old')}->{e.get('stars_new')}")
    else:
        for e in evs:
            keys = {k: v for k, v in e.items()
                    if k not in ("type", "date", "id", "repo")}
            print(f"  {e['date']} {e['type']:>4} {keys}")


def cmd_day(day, which, top):
    evs = st.load_events(day)
    if not evs:
        print(f"{day} 无事件文件(data/events/events_{day}.ndjson)")
        return
    sel = [e for e in evs if e["type"] == which]
    print(f"{day} {which} 共 {len(sel)} 条" + (f",显示前 {top}" if top else ""))
    for e in sel[:top or len(sel)]:
        extra = e.get("stars", e.get("stars_old", ""))
        print(f"  {e['repo']:<50} stars={extra}")


def main():
    u()
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo")
    ap.add_argument("--curve", action="store_true")
    ap.add_argument("--date", help="YYYYMMDD")
    ap.add_argument("--entered", action="store_true")
    ap.add_argument("--exited", action="store_true")
    ap.add_argument("--top", type=int)
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    if args.stats or not (args.repo or args.date):
        cmd_stats()
    if args.repo:
        cmd_repo(args.repo, args.curve)
    if args.date:
        if args.entered:
            cmd_day(args.date, "in", args.top)
        if args.exited:
            cmd_day(args.date, "out", args.top)


if __name__ == "__main__":
    main()
