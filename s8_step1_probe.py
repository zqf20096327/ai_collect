# -*- coding: utf-8 -*-
"""s8_step1_probe —— 步骤1 验收探针（s8_spec.md §19）。

抽 200 篇 README 实测：
  ① 清理压缩率（lib_rm_clean 移植后在本域的效果）
  ② 提名召回（六张词表的命中率分布）
  ③ 窗口外候选行（全文提名 vs 只看 12KB 窗口的差异——三段式架构的关键论据）
  ④ 形态检测（awesome/超大表格 → C 层路由）

用法：python s8_step1_probe.py [--n 200] [--seed 20261018] [--window 12000]
报告落盘 state/s8_step1_report.json。
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
import time
from pathlib import Path

from lib_rm_clean import clean_readme, number_lines, visible_line_limit
from lib_nominate import scan_lines, detect_form

HERE = Path(__file__).resolve().parent
READMES = HERE / "data" / "readmes"
REPORT = HERE / "state" / "s8_step1_report.json"

CATS = ("providers", "install", "hardware", "dual", "depre", "products")

KNOWN = [  # 会话中人工读过的样本，做定性对照
    "AprilNEA__ChatGPUI.md", "Vbj1808__Dokis.md", "Janson20__FMCL.md",
    "PatBall1__detectree2.md", "HRNPH__AIwaifu.md", "UditAkhourii__brane-code.md",
]


def probe(n: int, seed: int, window: int) -> dict:
    files = sorted(p.name for p in READMES.glob("*.md"))
    if not files:
        raise SystemExit(f"no readmes under {READMES}")
    rng = random.Random(seed)
    sample = rng.sample(files, min(n, len(files)))

    compress: list[float] = []
    lines_total: list[int] = []
    cat_files: dict[str, int] = {c: 0 for c in CATS}
    cat_hits: dict[str, int] = {c: 0 for c in CATS}
    cat_terms: dict[str, set] = {c: set() for c in CATS}
    oow_total = 0
    nom_total = 0
    oow_files = 0
    forms = {}
    t0 = time.time()

    for name in sample:
        raw = (READMES / name).read_text(encoding="utf-8", errors="ignore")
        cleaned = clean_readme(raw)
        numbered = number_lines(cleaned)
        compress.append(100 - len(cleaned) * 100 / max(len(raw), 1))
        lines_total.append(len(numbered))
        vis = visible_line_limit(numbered, window)
        cands = scan_lines(numbered)
        form = detect_form(name, raw, cleaned)
        if form:
            forms[form] = forms.get(form, 0) + 1
        file_oow = 0
        for cat, items in cands.items():
            cat_files[cat] += 1
            cat_hits[cat] += len(items)
            cat_terms[cat] |= {i["term"] for i in items}
            file_oow += sum(1 for i in items if i["line"] > vis)
        nom_total += sum(len(v) for v in cands.values())
        oow_total += file_oow
        if file_oow:
            oow_files += 1

    def pct(vals, p):
        if not vals:
            return 0
        s = sorted(vals)
        return round(s[min(len(s) - 1, max(0, int(round(p / 100 * (len(s) - 1)))))], 1)

    report = {
        "ran_at": time.strftime("%Y-%m-%d %H:%M"), "n": len(sample), "seed": seed,
        "window_chars": window, "secs": round(time.time() - t0, 1),
        "compression_pct": {"mean": round(statistics.mean(compress), 1),
                            "median": round(statistics.median(compress), 1),
                            "p10": pct(compress, 10), "p90": pct(compress, 90),
                            "min": round(min(compress), 1), "max": round(max(compress), 1)},
        "cleaned_lines_mean": round(statistics.mean(lines_total), 1),
        "nomination": {c: {"files_hit": cat_files[c],
                           "files_hit_pct": round(cat_files[c] * 100 / len(sample), 1),
                           "total_hits": cat_hits[c],
                           "mean_hits_per_hit_file": round(cat_hits[c] / cat_files[c], 2) if cat_files[c] else 0,
                           "distinct_terms": len(cat_terms[c])} for c in CATS},
        "out_of_window": {"nominations": nom_total, "oow": oow_total,
                          "oow_pct": round(oow_total * 100 / max(nom_total, 1), 2),
                          "files_with_oow": oow_files,
                          "files_with_oow_pct": round(oow_files * 100 / len(sample), 1)},
        "form_detection": forms,
        "sample_files": sample[:0],  # 不入报告，省体积
    }
    return report


def qualitative():
    """已知样本的定性对照：人读过的 6 篇，看提名是否符合预期。"""
    print("\n—— 定性对照（会话中人工读过的样本）——")
    for name in KNOWN:
        p = READMES / name
        if not p.is_file():
            continue
        raw = p.read_text(encoding="utf-8", errors="ignore")
        cands = scan_lines(number_lines(clean_readme(raw)))
        brief = {c: [f'{i["term"]}@L{i["line"]}' for i in items[:4]]
                 for c, items in cands.items()}
        print(f"\n{name}")
        for c, terms in brief.items():
            print(f"  {c}: {'; '.join(terms) if terms else '(无)'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20261018)
    ap.add_argument("--window", type=int, default=12000)
    ap.add_argument("--qualitative", action="store_true", help="附已知样本对照")
    args = ap.parse_args()

    report = probe(args.n, args.seed, args.window)
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"n={report['n']}  用时 {report['secs']}s  报告 → {REPORT}")
    c = report["compression_pct"]
    print(f"压缩率: mean {c['mean']}% / median {c['median']}% / p10 {c['p10']}% / p90 {c['p90']}%")
    print(f"清理后行数 mean: {report['cleaned_lines_mean']}")
    print("\n提名召回（六张词表）:")
    for cat, s in report["nomination"].items():
        print(f"  {cat:<10} 命中文件 {s['files_hit']:>3} ({s['files_hit_pct']:>5}%)  "
              f"总命中 {s['total_hits']:>4}  均值 {s['mean_hits_per_hit_file']}/文件  "
              f"词种 {s['distinct_terms']}")
    o = report["out_of_window"]
    print(f"\n窗口外候选行: {o['oow']}/{o['nominations']} ({o['oow_pct']}%)  "
          f"涉及文件 {o['files_with_oow']} ({o['files_with_oow_pct']}%)"
          f"  ← 这些行只看 {args.window} 字窗口会漏掉")
    print(f"形态检测: {report['form_detection'] or '无'}")
    if args.qualitative:
        qualitative()


if __name__ == "__main__":
    main()
