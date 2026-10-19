# -*- coding: utf-8 -*-
"""s8_view —— 把解读卡片渲染成可读的 Markdown 预览(v3 起读一仓一文件存储)。

用法：python s8_view.py            # 全部卡片 → state/s8_cards_preview.md
      python s8_view.py 20         # 只看前 20 张（star 降序）
"""
from __future__ import annotations
import sys
from pathlib import Path

from lib_store import load_pool
import lib_card_store as cstore

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "state" / "s8_cards_preview.md"


def badge(v) -> str:
    return "—" if v is None or v == "" else str(v)


def main(limit: int | None = None):
    cards = [c for _, c in cstore.iter_cards()]
    if not cards:
        raise SystemExit("尚无卡片（state/s8_cards/ 为空）")
    pool = {r.get("full_name"): r for r in load_pool().values()}
    cards.sort(key=lambda c: -(pool.get(c["fn"]) or {}).get("stars") or 0)
    n_total = len(cards)
    if limit:
        cards = cards[:limit]
    lines = [f"# s8 解读卡片预览（{len(cards)}/{n_total} 张，star 降序）\n",
             "> 生成于试批进行中时为快照；重跑 `python s8_view.py` 刷新\n"]
    for c in cards:
        f = c["filters"]
        stars = (pool.get(c["fn"]) or {}).get("stars") or "?"
        lines.append(f"## {c['fn']}（⭐{stars}，confidence: {c['trust']['confidence']}）\n")
        lines.append(f"**{c['identity']['one_liner']}**\n")
        filt = " · ".join(f"{k}={badge(f.get(k))}" for k in
                          ("ai_role", "license_risk", "deploy", "model_dep",
                           "hardware", "install_friction", "maturity"))
        lines.append(f"`{filt}`\n")
        if c["identity"].get("review"):
            lines.append(c["identity"]["review"] + "\n")
        for h in c["identity"].get("highlights") or []:
            lines.append(f"- {h}")
        lines.append("")
        for ev in c["trust"].get("evidence") or []:
            lines.append(f"> {ev}")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"{n_total} 张卡片 → {OUT}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
