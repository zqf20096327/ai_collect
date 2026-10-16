# -*- coding: utf-8 -*-
"""出池仓清理(移植自 dbhub purge_outpool):absent_since 台账 + 宽限 + 备份式删除。

背景:readme_state/enrich_state/enrich_cache 只增不减,出池仓条目与
data/readmes/ 正文文件残留。核心风险=出池≠不回来(星标边缘波动、采集抖动
假出池),误删代价=重拉 API(贵得多)——故 30 天宽限、回池即清戳。

三模式:
  --stamp   每晚(collect.yml):维护 state/absent_since.json 台账,出池打戳/
            回池清戳。幂等,不写任何 state 原件(零侵入主流程)。
  (默认)    dry-run:列出到期清单不动盘。
  --apply   执行:md 文件→仓外备份目录(移动非删除);readme/enrich state
            原件备份后删条目;写 state/purge_list_日期.json manifest。

规则:普通仓 absent >=30 天;owner ∈ config.EXCLUDE_USERS 或 fn ∈
config.EXCLUDE_REPOS(采集落地即丢,物理不可能回池)>=7 天;readme failed/
三振条目整仓跳过(排查线索,state+文件都留);删 md 前校验安全名
(fn.replace('/','__'))无其他在册仓持有(含大小写不敏感);单次文件上限
500(--limit,防 git 巨量 D 撞 CI 提交步)。

用法:
  python tools/purge_outpool.py --stamp
  python tools/purge_outpool.py                 # dry-run 到期清单
  python tools/purge_outpool.py --apply --limit 500
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

import config  # noqa: E402
import lib_store as st  # noqa: E402
from lib_enrich_store import load_cache, save_cache_all  # noqa: E402

GRACE_DAYS = 30
GRACE_BLOCKED = 7
LIMIT_DEFAULT = 500


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def _age_days(stamp: str) -> int:
    d = datetime.strptime(stamp, "%Y%m%d").replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - d).days


def _universe() -> tuple[dict, dict, dict]:
    """三 state 原件(只读)+ fn 全集(enrich_cache 分片并集读)。"""
    def load(p):
        path = st.STATE / p
        if not path.is_file():
            return {}
        d = json.loads(path.read_text(encoding="utf-8"))
        return d.get("items", {})
    return (load("readme_state.json"), load("enrich_state.json"), load_cache())


def do_stamp() -> set:
    """台账维护:universe−池 打戳(已有戳保原日期),回池/已消失 清戳。"""
    alive = {r["full_name"] for r in st.load_pool().values()}
    rs, es, ec = _universe()
    universe = set(rs) | set(es) | set(ec)
    ledger_p = st.STATE / "absent_since.json"
    ledger = (json.loads(ledger_p.read_text(encoding="utf-8"))
              if ledger_p.is_file() else {})
    today = _today()
    cleared = sum(1 for fn in list(ledger) if fn in alive or fn not in universe)
    for fn in list(ledger):
        if fn in alive or fn not in universe:
            del ledger[fn]
    stamped = 0
    for fn in universe - alive:
        if fn not in ledger:
            ledger[fn] = today
            stamped += 1
    st.atomic_write_json(ledger_p, ledger)
    print(f"台账: 池 {len(alive)} · 在册 {len(universe)} · 出池 {len(ledger)}"
          f"(新打戳 {stamped},清戳 {cleared})")
    return alive


def build_plan(limit: int) -> dict:
    """到期清单 + 守卫标注。返回 {due, skipped_fail, skipped_collision, ghosts}。"""
    alive = do_stamp()                           # 顺带把台账修准
    rs, es, ec = _universe()
    ledger = json.loads((st.STATE / "absent_since.json")
                        .read_text(encoding="utf-8"))
    users_bl = {u.lower() for u in config.EXCLUDE_USERS}
    repos_bl = {r.lower() for r in config.EXCLUDE_REPOS}

    def grace_of(fn: str) -> int:
        # 黑名单仓在采集落地处即丢弃、物理不可能回池——30 天宽限防的是
        # 假出池回池,对它们只剩拖时间,给短宽限
        if fn.split("/", 1)[0].lower() in users_bl or fn.lower() in repos_bl:
            return GRACE_BLOCKED
        return GRACE_DAYS

    kept_holders: dict[str, set] = {}            # 小写安全名 → 持有者 fn 集(撞名守卫)
    for fn in set(rs) | set(es) | set(ec) | alive:
        kept_holders.setdefault(
            (fn.replace("/", "__") + ".md").lower(), set()).add(fn)

    due, skip_fail, skip_coll = [], [], []
    for fn, stamp in sorted(ledger.items(), key=lambda kv: kv[1]):   # 最老优先
        grace = grace_of(fn)
        if _age_days(stamp) < grace:
            continue
        r = rs.get(fn) or {}
        if (r.get("fail_count") or 0) >= 3 or r.get("status") == "failed":
            skip_fail.append(fn)                 # 排查线索:整仓保留
            continue
        safe = (fn.replace("/", "__") + ".md").lower()
        if len(kept_holders.get(safe) or ()) > 1:
            skip_coll.append((fn, sorted(kept_holders[safe])))     # 共享安全名保留
            continue
        safe_exact = fn.replace("/", "__") + ".md"
        due.append({"fn": fn, "since": stamp, "grace": grace,
                    "sha": r.get("sha", ""),
                    "file": safe_exact
                    if (st.READMES / safe_exact).is_file() else ""})
        if sum(1 for d in due if d["file"]) >= limit:
            break                                # 文件数触帽即止(state 同步停)

    ghosts = []
    if st.READMES.is_dir():
        state_safe = {fn.replace("/", "__") + ".md"
                      for fn in set(rs) | set(es) | set(ec)}   # 任一在册都非幽灵
        for f in st.READMES.iterdir():
            if f.name.endswith(".md") and f.name not in state_safe:
                holders = kept_holders.get(f.name.lower()) or set()
                ghosts.append({"fn": f.name,
                               "holder": ",".join(sorted(holders))})
    return {"due": due, "skip_fail": skip_fail, "skip_coll": skip_coll,
            "ghosts": ghosts}


def do_apply(limit: int, backup_dir: Path | None) -> None:
    plan = build_plan(limit)
    due, ghosts = plan["due"], [g for g in plan["ghosts"] if not g["holder"]]
    if not due and not ghosts:
        print("无到期项(dry-run 同款结论),未动任何文件")
        return
    bdir = backup_dir or _ROOT.parent / f"ai_collect_purge_backup_{_today()}"
    (bdir / "readmes").mkdir(parents=True, exist_ok=True)
    (bdir / "state").mkdir(parents=True, exist_ok=True)

    rs_p, es_p = (st.STATE / n for n in ("readme_state.json",
                                         "enrich_state.json"))
    for p in (rs_p, es_p):                       # state 原件先备份(git 恢复会丢中间增量)
        if p.is_file():
            shutil.copy2(p, bdir / "state" / p.name)
    ec = load_cache()
    (bdir / "state" / "enrich_cache_all.json").write_text(
        json.dumps(ec, ensure_ascii=False, indent=1), encoding="utf-8")

    rs = json.loads(rs_p.read_text(encoding="utf-8"))
    es = json.loads(es_p.read_text(encoding="utf-8"))
    ledger = json.loads((st.STATE / "absent_since.json")
                        .read_text(encoding="utf-8"))
    manifest, moved = {}, 0
    for d in due:
        fn, safe = d["fn"], d["file"]
        if safe:
            src = st.READMES / safe
            shutil.move(str(src), str(bdir / "readmes" / safe))  # 移动非删除
            moved += 1
        rs.get("items", {}).pop(fn, None)
        es.get("items", {}).pop(fn, None)
        ec.pop(fn, None)
        ledger.pop(fn, None)
        manifest[fn] = {**d,
                        "backup": str(bdir / "readmes" / safe) if safe else ""}
    for g in ghosts:                             # 幽灵:state 无记录,直接移出
        shutil.move(str(st.READMES / g["fn"]),
                    str(bdir / "readmes" / g["fn"]))
        manifest[g["fn"]] = {"fn": g["fn"], "since": "", "grace": 0,
                             "sha": "", "file": g["fn"], "reason": "ghost",
                             "backup": str(bdir / "readmes" / g["fn"])}
    st.atomic_write_json(rs_p, rs)
    st.atomic_write_json(es_p, es)
    save_cache_all(ec)
    st.atomic_write_json(st.STATE / "absent_since.json", ledger)
    st.atomic_write_json(st.STATE / f"purge_list_{_today()}.json", manifest)
    print(f"清理: 到期 {len(due)}(移文件 {moved}) · 幽灵 {len(ghosts)} · "
          f"跳过 failed {len(plan['skip_fail'])} / 撞名 "
          f"{len(plan['skip_coll'])}")
    print(f"备份与 manifest: {bdir} · state/purge_list_{_today()}.json")


def main() -> None:
    ap = argparse.ArgumentParser(description="出池仓清理(默认 dry-run)")
    ap.add_argument("--stamp", action="store_true",
                    help="只维护 absent_since 台账(每晚)")
    ap.add_argument("--apply", action="store_true",
                    help="执行清理(默认只列清单)")
    ap.add_argument("--limit", type=int, default=LIMIT_DEFAULT,
                    help="单次文件上限")
    ap.add_argument("--backup-dir", type=Path, default=None)
    args = ap.parse_args()
    if args.stamp:
        do_stamp()
        return
    if args.apply:
        do_apply(args.limit, args.backup_dir)
        return
    plan = build_plan(args.limit)
    print(f"到期 {len(plan['due'])}"
          f"(含文件 {sum(1 for d in plan['due'] if d['file'])}) · "
          f"幽灵可删 {len([g for g in plan['ghosts'] if not g['holder']])} · "
          f"跳过 failed {len(plan['skip_fail'])} / "
          f"撞名 {len(plan['skip_coll'])}")
    for d in plan["due"][:20]:
        print(f"  {d['since']} 起 {d['grace']}天已满 {d['fn']} "
              f"{'(有md)' if d['file'] else '(无md)'}")
    print("(dry-run: 未动任何文件;--apply 执行,先备份后删)")


if __name__ == "__main__":
    main()
