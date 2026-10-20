# -*- coding: utf-8 -*-
"""s12 每日数据点:全池 stars/forks/open_issues 快照 → data/stars/points_YYYYMMDD.ndjson。

给"每天有变化的曲线"供料(程序层零 API):
  - 每仓星数曲线(velocity 已在读 points_*.ndjson,窗口自动放大)
  - forks 曲线、open_issues 曲线(新增字段,读端按名取、多余字段无副作用)
设计:幂等(当日文件已存在则跳过);full_name 字典序稳定排序;~1.5MB/日。
用法:python s12_points.py [--force]
"""
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# 只读输入(池)可指向工厂仓检出;输出点文件永远写本地 data/stars
POOL_DIR = ((Path(os.environ["FACTORY_ROOT"]) / "data" / "live")
            if os.environ.get("FACTORY_ROOT")
            else ROOT / "data" / "live")
OUT_DIR = ROOT / "data" / "stars"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="当日文件已存在也重写")
    args = ap.parse_args()
    day = time.strftime("%Y%m%d")
    out = OUT_DIR / f"points_{day}.ndjson"
    if out.exists() and not args.force:
        print(f"今日点已存在: {out} ({out.stat().st_size // 1024} KB),跳过")
        return
    # 富集窗并发写池:同一仓可能跨分片重复,按 full_name 去重(后见覆盖=最新)
    dedup: dict[str, dict] = {}
    for fp in sorted(POOL_DIR.glob("pool_shard_*.ndjson")):
        for ln in fp.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue                    # 富集窗并发追加的半行
            if r.get("full_name"):
                dedup[r["full_name"]] = {
                    "id": r.get("id"), "full_name": r["full_name"],
                    "stars": r.get("stars"), "forks": r.get("forks"),
                    "open_issues": r.get("open_issues")}
    rows = [dedup[k] for k in sorted(dedup)]
    tmp = out.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    tmp.replace(out)
    print(f"{day}: {len(rows)} 仓 -> {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
