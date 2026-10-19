# -*- coding: utf-8 -*-
"""s8_repro —— 拒收家族复现脚本(v3,学 dbhub _repro_do)。

从 runlog 里挑历史拒收/失败条目,按失败家族各选代表,走当前代码全流程复验。
只读 state(除 runlog 自身的 jsonl 追加),不写卡片不写索引——修复后跑它回答
"修好了没有",与 selftest(管"没变坏")互补。

用法：
  python s8_repro.py            # 每个家族最多 2 个代表
  python s8_repro.py 5          # 每个家族最多 5 个代表
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib_card_store as cstore            # noqa: E402
from s8_interpret import (AIClient, build_context, judge,  # noqa: E402
                          pool_by_fullname, readme_path, sha_of)

ROOT = Path(__file__).resolve().parent
LOGS = ROOT / "state" / "logs"

FAMILY_RE = [
    ("禁词", re.compile(r"禁词|one_liner:『|review:『|highlights 删条|use_cases 删条")),
    ("行号", re.compile(r"行号|lines")),
    ("词不在候选", re.compile(r"词不在候选")),
    ("枚举非法", re.compile(r"非法")),
    ("结构/截断", re.compile(r"JSON|截断|非对象|缺失")),
]


def family_of(violations: list) -> str:
    txt = "；".join(str(v) for v in violations or [])
    for name, pat in FAMILY_RE:
        if pat.search(txt):
            return name
    return "其他"


def main(per_family: int = 2):
    pool = pool_by_fullname()
    # 收集历史 rejected/failed(runlog 一行一条 jsonl)
    fam_cases: dict[str, list[str]] = {}
    if LOGS.is_dir():
        for lf in sorted(LOGS.glob("s8_*.jsonl")):
            for line in lf.read_text(encoding="utf-8").split("\n"):
                if not line.strip():
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if r.get("type") == "run_summary":
                    continue
                if r.get("kind") not in ("rejected", "failed"):
                    continue
                fn = r.get("fn")
                if not fn or fn not in pool or fn.startswith("_"):
                    continue
                fam = family_of(r.get("violations") or [r.get("error") or ""])
                lst = fam_cases.setdefault(fam, [])
                if fn not in lst:
                    lst.append(fn)
    if not fam_cases:
        print("runlog 中无拒收/失败样本——无可复现项(试批全过则正常)")
        return
    ai = AIClient()
    total = done = rej = fail = 0
    for fam, fns in sorted(fam_cases.items()):
        for fn in fns[:per_family]:
            rec = pool[fn]
            p = readme_path(fn)
            if not p.is_file():
                print(f"[skip] {fn} README 已不在盘")
                continue
            sha = sha_of(p.read_text(encoding="utf-8", errors="ignore"))
            if cstore.sha_seen(sha):
                print(f"[skip] {fn} 同内容已入库(修复已生效的另一种证明)")
                continue
            r = judge(build_context(fn, rec), ai)
            total += 1
            kind = r["kind"]
            if kind == "done":
                done += 1
                f = r["card"]["filters"]
                vsum = f"ai_role={f.get('ai_role')} license={f.get('license_risk')}"
                print(f"[PASS] {fn} ({fam}) {vsum}")
            else:
                if kind == "rejected":
                    rej += 1
                else:
                    fail += 1
                why = r.get("violations") or r.get("error")
                print(f"[{kind.upper()}] {fn} ({fam}) {str(why)[:160]}")
    print(f"\n复现总结: {total} 例,过闸 {done},仍拒 {rej},失败 {fail}"
          f"(仍拒≠退步:同家族不同例难度不同,看分布不看单例)")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 2)
