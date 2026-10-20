# -*- coding: utf-8 -*-
"""存储共享库:分片活文件 / 事件日志 / 周度星数点 / parts / 快照。

布局:
  data/live/pool_shard_NN.ndjson   池活文件(repo_id % N_SHARDS 稳定映射)
  data/events/events_YYYYMMDD.ndjson  每日事件日志(in/out/chg,append-only)
  data/stars/points_YYYYMMDD.ndjson   周度星数点(repo_id,stars 两列)
  data/parts/*.json                各通道原始结果(合并输入,不入 git)
  data/snapshot_YYYYMMDD/          当日全量快照 + meta(不入 git)
  data/readmes/{owner}__{repo}.md  README 正文
  state/                           断点/缓存(etag 等)
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# FACTORY_ROOT:云端部署时把只读输入(池/README/事件/星数点)指到工厂仓检出目录;
# 不设则一切如常(本地默认)。state 永远在本地 ROOT。
FACTORY = Path(os.environ["FACTORY_ROOT"]).resolve() \
    if os.environ.get("FACTORY_ROOT") else ROOT
DATA = FACTORY / "data"
LIVE = DATA / "live"
EVENTS = DATA / "events"
STARS = DATA / "stars"
PARTS = DATA / "parts"
SNAP_LATEST = DATA / "snapshot_latest"
READMES = DATA / "readmes"
STATE = ROOT / "state"

if FACTORY == ROOT:                       # 本地模式维持自动建目录
    for _d in (LIVE, EVENTS, STARS, PARTS, READMES, STATE):
        _d.mkdir(parents=True, exist_ok=True)

import config  # noqa: E402


def utc_day():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def _atomic_write(path: Path, text: str):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def atomic_write_json(path: Path, data, keep: int = 3):
    """JSON 原子写 + 轮转备份(.1/.2/.3,状态写坏可回滚)+ 强制 LF。
    移植自 dbhub gh.atomic_write_json。"""
    for i in range(keep, 1, -1):                 # .2->.3
        src = path.with_suffix(path.suffix + f".{i - 1}")
        dst = path.with_suffix(path.suffix + f".{i}")
        if src.exists():
            os.replace(src, dst)
    if path.exists():                            # 旧主文件 -> .1
        os.replace(path, path.with_suffix(path.suffix + ".1"))
    _atomic_write(path, json.dumps(data, ensure_ascii=False) + "\n")


def shard_path(i: int) -> Path:
    return LIVE / f"pool_shard_{i:02d}.ndjson"


def shard_of(repo_id: int) -> int:
    return repo_id % config.N_SHARDS


def load_pool() -> dict:
    """读全池:id -> record。

    必须严格按 \\n 切行:splitlines() 还会切 U+2028 等 Unicode 行分隔符,
    description 含它的一行 JSON 会被切成两半 → 静默丢仓(10-16 实际发生 2 仓)。
    """
    pool = {}
    for p in sorted(LIVE.glob("pool_shard_*.ndjson")):
        for line in p.read_text(encoding="utf-8").split("\n"):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            pool[rec["id"]] = rec
    return pool


def save_pool(pool: dict):
    """按分片写活文件(片内按 stars 降序)。返回各片字节数。"""
    buckets = {i: [] for i in range(config.N_SHARDS)}
    for rec in pool.values():
        buckets[shard_of(rec["id"])].append(rec)
    sizes = {}
    for i, recs in buckets.items():
        recs.sort(key=lambda r: -r.get("stars", 0))
        text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs)
        _atomic_write(shard_path(i), text)
        sizes[i] = len(text.encode("utf-8"))
    return sizes


def slim(it: dict, channel: str) -> dict:
    """API 原始记录 -> 池记录(瘦身 + 通道标记)。"""
    lic = (it.get("license") or {}) or {}
    return {
        "id": it["id"],
        "full_name": it["full_name"],
        "owner": (it.get("owner") or {}).get("login"),
        "owner_type": (it.get("owner") or {}).get("type"),
        "description": it.get("description") or "",
        "topics": it.get("topics") or [],
        "language": it.get("language"),
        "license": lic.get("spdx_id"),
        "stars": it.get("stargazers_count", 0),
        "forks": it.get("forks_count", 0),
        "open_issues": it.get("open_issues_count", 0),
        "archived": bool(it.get("archived")),
        "fork": bool(it.get("fork")),
        "created_at": it.get("created_at"),
        "pushed_at": it.get("pushed_at"),
        "updated_at": it.get("updated_at"),
        "homepage": it.get("homepage") or "",
        "html_url": it.get("html_url"),
        "src": [channel],
    }


def write_part(name: str, records: list):
    _atomic_write(PARTS / f"{name}.json",
                  json.dumps(records, ensure_ascii=False))


def read_part(name: str) -> list:
    p = PARTS / f"{name}.json"
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))


def parts_files() -> list:
    return sorted(PARTS.glob("*.json"))


def events_path(day: str) -> Path:
    return EVENTS / f"events_{day}.ndjson"


def write_events(day: str, events: list, force=False):
    p = events_path(day)
    if p.exists() and not force:
        raise SystemExit(f"事件文件已存在 {p.name},加 --force 才允许重写")
    _atomic_write(p, "".join(json.dumps(e, ensure_ascii=False) + "\n"
                             for e in events))


def load_events(day: str) -> list:
    p = events_path(day)
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").split("\n"):
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def all_event_files() -> list:
    return sorted(EVENTS.glob("events_*.ndjson"))


def stars_point_path(day: str) -> Path:
    return STARS / f"points_{day}.ndjson"


def write_stars_point(day: str, pool: dict):
    lines = [json.dumps({"id": r["id"], "full_name": r["full_name"],
                         "stars": r.get("stars", 0)}, ensure_ascii=False)
             for r in sorted(pool.values(), key=lambda x: -x.get("stars", 0))]
    _atomic_write(stars_point_path(day), "\n".join(lines) + "\n")


def snapshot_dir(day: str) -> Path:
    d = DATA / f"snapshot_{day}"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------- 池采集断点(s1-s4 共享,移植自 dbhub collect_state) ----------------

COLLECT_STATE = STATE / "collect_state.json"


def load_collect_state() -> dict:
    if COLLECT_STATE.exists():
        try:
            return json.loads(COLLECT_STATE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"date": "", "done": []}


def done_tokens(day: str = None) -> set:
    """当日已完成的采集单元 token(仅同 UTC 日期恢复,跨日自动清零)。"""
    s = load_collect_state()
    day = day or utc_day()
    return set(s["done"]) if s.get("date") == day else set()


def mark_done(token: str):
    day = utc_day()
    s = load_collect_state()
    if s.get("date") != day:
        s = {"date": day, "done": []}
    if token not in s["done"]:
        s["done"].append(token)
    atomic_write_json(COLLECT_STATE, s)


def expected_tokens() -> list:
    """由 config 推导当日应跑完的全部单元 token(s5 完成门控的应到名册)。"""
    toks = [f"new:{t}" for t in config.TOPICS]
    toks += [f"topic:{t}" for t in config.TOPICS]
    toks += [f"org:{o}" for o in list(config.ORG_DEDICATED)
             + list(config.ORG_SUPERSET)]
    toks.append("watch")
    return toks


def part_names_expected() -> set:
    """与 expected_tokens 对应的 parts 文件名(清理 config 漂移残留用)。"""
    names = {f"topic_{t}.json" for t in config.TOPICS}
    names |= {f"new_{t}.json" for t in config.TOPICS}
    names |= {f"org_{o}.json" for o in list(config.ORG_DEDICATED)
              + list(config.ORG_SUPERSET)}
    names.add("watch.json")
    return names
