# -*- coding: utf-8 -*-
"""s10 场景标签：存量回填 / 抽样打标 / 评测 三命令。

用法：
  python s10_tags.py backfill                    # 666 卡回填 scenario_tags_v2 + 报告（零 API）
  python s10_tags.py tag --sample 80 --concurrency 6
  python s10_tags.py evaluate                    # 对比抽样结果与回填结果，输出验收判据

方案见 tag_vocab_v1.md；词表 tag_vocab_v1.json；映射/提名 lib_tag_vocab.py。
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import random
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import lib_card_store as cstore
import lib_tag_vocab as tv
from s8_interpret import AIClient, extract_json

ROOT = Path(__file__).resolve().parent
# 只读输入(池 topics)可指向工厂仓检出;不设则本地默认
POOL_DIR = ((Path(os.environ["FACTORY_ROOT"]) / "data" / "live")
            if os.environ.get("FACTORY_ROOT")
            else ROOT / "data" / "live")
BACKFILL_REPORT = ROOT / "state" / "s10_backfill_report.json"
SAMPLE_OUT = ROOT / "state" / "s10_sample_tags.json"
RETAG_OUT = ROOT / "state" / "s10_retag_run.json"
EVAL_OUT = ROOT / "state" / "s10_eval_report.json"
BACKUP_DIR = ROOT / "state" / "backup_tags_v1"

log = logging.getLogger("s10")


# --------------------------------------------------------------- 池子 topics
def load_pool_topics() -> dict[str, list[str]]:
    """data/live/pool_shard_*.ndjson -> {full_name: topics}（只留 topics 非空者）。"""
    idx = {}
    for fp in sorted(POOL_DIR.glob("pool_shard_*.ndjson")):
        for ln in fp.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue
            t = r.get("topics")
            if r.get("full_name") and t:
                idx[r["full_name"]] = t
    return idx


# --------------------------------------------------------------- 提示词
def vocab_block() -> str:
    v = tv.load_vocab()
    lines = []
    for g in v["groups"]:
        lines.append(f"【{g['name_zh']}】")
        for t in v["tags"]:
            if t["group"] != g["gid"]:
                continue
            neg = "；".join(t["negatives"])
            lines.append(f"- {t['slug']}｜{t['zh']}｜{t['definition']}｜不算：{neg}")
    return "\n".join(lines)


def build_prompt(card: dict, topics: list[str], nominated: list[str]) -> str:
    ident = card.get("identity") or {}
    links = card.get("links") or {}
    repo_txt = "\n".join([
        f"仓库：{card.get('fn')}",
        f"简介：{card.get('description') if card.get('description') else ident.get('one_liner', '')}",
        f"维护者 topics：{', '.join(topics[:15]) if topics else '（无）'}",
        f"一句话：{ident.get('one_liner', '')}",
        f"综述：{ident.get('review', '')}",
        f"亮点：{'；'.join(ident.get('highlights') or [])}",
        f"用途：{'；'.join(ident.get('use_cases') or [])}",
    ])
    nom_txt = "、".join(nominated) if nominated else "（提名未命中——请从词表自行挑 1-2 个最贴近的）"
    return f"""你是开源 AI 生态的编目员，从受控词表中为仓库选择场景标签。

【规则——违反即拒收】
1. 只能从下方词表选择，禁止自造标签；场景标签回答"用户用它来干什么"。
2. 界面形态/协议/部署方式/语言/技术栈不是场景（如 cli、桌面应用、mcp、自托管、pytorch），一律不选。
3. 每仓 1-4 个。简介/README 呈现多个真实不同的使用场景时应逐一给出（常见 2-3 个）；仅单场景仓库才给 1 个；不确定的宁可不选。
4. 对每个候选标签逐一裁决（include/exclude + 一句理由）；最多可额外补充 1 个词表内标签。
5. 理由只陈述事实，不用评价词。

【词表（{len(tv.load_vocab()['tags'])} 标签）】
{vocab_block()}

【仓库信息】
{repo_txt}

【程序提名候选】（来自 topics/简介/卡片摘要的关键词命中）
{nom_txt}

【输出 JSON，不要输出其他内容】
{{"decisions": [{{"slug": "...", "include": true, "reason": "一句话"}}, ...],
  "final_tags": ["slug", ...]}}
"""


# --------------------------------------------------------------- 裁决与守卫
def _guard_tags(data: dict) -> list[str]:
    v = tv.load_vocab()
    out = []
    if not isinstance(data, dict):
        return out
    raw = data.get("final_tags")
    if not isinstance(raw, list):
        return out
    for s in raw:
        if not isinstance(s, str):
            continue
        k = tv.normalize(s)
        slug = v["_alias_map"].get(k) or (s if s in v["_by_slug"] else None)
        if slug and slug not in out:
            out.append(slug)
        if len(out) >= 4:
            break
    return out


def _guard_decisions(data: dict, allowed: set) -> list:
    out = []
    if not isinstance(data, dict):
        return out
    raw = data.get("decisions")
    if not isinstance(raw, list):
        return out
    for d in raw:
        if not isinstance(d, dict):
            continue
        slug = d.get("slug")
        inc = d.get("include")
        reason = d.get("reason")
        if (isinstance(slug, str) and isinstance(inc, bool)
                and isinstance(reason, str) and slug in allowed):
            out.append({"slug": slug, "include": inc, "reason": reason[:120]})
    return out[:12]


def adjudicate(client: AIClient, card: dict, topics: list[str]) -> dict:
    """单仓打标：提名 -> LLM 二值裁决 -> 守卫过滤。

    重试仅针对真解析失败/全无效 slug；模型合法给出空 final_tags 不重试（宁缺勿滥）。
    """
    ident = card.get("identity") or {}
    nominated = tv.nominate({
        "topics": " ".join(topics or []),
        "desc": card.get("description") or "",
        "card": " ".join([ident.get("one_liner") or "", ident.get("review") or "",
                          " ".join(ident.get("highlights") or []),
                          " ".join(ident.get("use_cases") or [])]),
    })
    prompt = build_prompt(card, topics, nominated)
    allowed = set(tv.load_vocab()["_by_slug"])
    t0 = time.time()
    tags, decisions, tries, raw_len = [], [], 0, 0
    for attempt in range(2):
        r = client.chat(prompt)
        tries += r.get("tries", 1)
        raw_len = len(r.get("content") or "")
        data = extract_json(r.get("content") or "")
        tags = _guard_tags(data)
        decisions = _guard_decisions(data or {}, allowed)
        raw_final = data.get("final_tags") if isinstance(data, dict) else None
        parse_ok = isinstance(data, dict) and isinstance(raw_final, list)
        all_invalid = parse_ok and raw_final and not tags   # 有输出但全是不认识的 slug
        if tags or (parse_ok and not all_invalid):
            break
        log.warning("%s 第 %d 次解析失败或全无效（content %d 字符），重试",
                    card.get("fn"), attempt + 1, raw_len)
    return {"nominated": nominated, "tags": tags, "decisions": decisions,
            "secs": round(time.time() - t0, 1), "tries": tries,
            "ok": bool(tags)}


# --------------------------------------------------------------- 子命令
def cmd_backfill(args) -> dict:
    """存量 666 卡：links.scenario_tags(自由) -> links.scenario_tags_v2(规范)。"""
    if args.dry_run:
        cards = {fn: c for fn, c in cstore.iter_cards()}
    else:
        cards = cstore.all_cards()
    rep = {"vocab_ver": tv.load_vocab()["vocab_ver"], "ts": time.strftime("%F %T"),
           "cards": 0, "instance_buckets": Counter(), "per_tag": Counter(),
           "zero_tag_n": 0, "zero_tag": [], "unmapped": Counter(), "excluded": Counter(),
           "over_cap": 0}
    if not args.dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    for fn, card in cards.items():
        rep["cards"] += 1
        free = (card.get("links") or {}).get("scenario_tags") or []
        m = tv.map_free_tags(free)
        rep["instance_buckets"].update(m["stats"])
        canonical = m["canonical"][:tv.load_vocab()["rules"]["max_per_repo"]]
        rep["per_tag"].update(canonical)
        for t in free:
            kind, val = tv.classify_free_tag(t)
            if kind == "excluded":
                rep["excluded"].update([val or "?"])
            elif kind == "unmapped":
                rep["unmapped"].update([t])
        if not canonical:
            rep["zero_tag_n"] += 1
            if len(rep["zero_tag"]) < 50:
                rep["zero_tag"].append(fn)
        if len(m["canonical"]) > 4:
            rep["over_cap"] += 1
        if not args.dry_run:
            # 备份必须先于改动：存改前 links 快照（原子写，防截断残留）
            dst = BACKUP_DIR / (fn.replace("/", "__") + ".json")
            if not dst.exists():
                tmp = dst.with_suffix(".tmp")
                tmp.write_text(json.dumps({"links": card.get("links")},
                                          ensure_ascii=False), encoding="utf-8")
                tmp.replace(dst)
            if not isinstance(card.get("links"), dict):
                card["links"] = {}
            if not isinstance(card.get("trust"), dict):
                card["trust"] = {}
            card["links"]["scenario_tags_v2"] = canonical
            card["trust"]["vocab_ver"] = tv.load_vocab()["vocab_ver"]
            cstore.write_card(card)
    # top-100 高频实例落位率（canonical+excluded 算落位）
    inst = Counter()
    for fn, card in cards.items():
        for t in (card.get("links") or {}).get("scenario_tags") or []:
            inst[tv.normalize(t)] += 1
    top100 = inst.most_common(100)
    landed = sum(c for k, c in top100
                 if tv.classify_free_tag(k)[0] in ("canonical", "excluded"))
    rep["top100_landed_pct"] = round(landed / max(sum(c for _, c in top100), 1) * 100, 1)
    rep_out = {k: (dict(v) if isinstance(v, Counter) else v) for k, v in rep.items()}
    rep_out["low_density"] = tv.validate_density(
        rep["per_tag"], tv.load_vocab()["rules"]["page_threshold_current"])
    if not args.dry_run:
        BACKFILL_REPORT.write_text(
            json.dumps(rep_out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in rep_out.items()
                      if k in ("cards", "instance_buckets", "top100_landed_pct",
                               "over_cap", "zero_tag_n", "low_density")},
                     ensure_ascii=False, indent=1))
    print(f"0 标签卡 {rep['zero_tag_n']} 张; 未映射标签种类 {len(rep['unmapped'])}")
    print("报告:", BACKFILL_REPORT if not args.dry_run else "(dry-run 未落盘)")
    return rep_out


def derive_domain(tags: list[str]) -> str | None:
    """domain 组名派生（方案 §7）：取组序最靠前的标签所属组的中文名。

    无标签返回 None（调用方保留原 domain——0 标签仓的老 domain 至少是个线索）。
    """
    v = tv.load_vocab()
    gname = {g["gid"]: g["name_zh"] for g in v["groups"]}
    for s in sorted(tags, key=lambda x: v["_by_slug"][x]["group"]):
        return gname[v["_by_slug"][s]["group"]]
    return None


def cmd_tag(args) -> dict:
    cards = cstore.all_cards()
    fns = sorted(cards)
    apply_mode = args.missing or args.force
    if args.force:
        targets = fns                                    # 全量重打（覆盖 v2）
    elif args.missing:
        # 只补"从未打过 v2"的卡;v2=[] 是有理由的合法空,不重打
        targets = [fn for fn in fns
                   if "scenario_tags_v2" not in (cards[fn].get("links") or {})]
    else:
        rng = random.Random(args.seed)
        targets = rng.sample(fns, min(max(args.sample, 1), len(fns)))
    if args.limit:
        targets = targets[:args.limit]
    topics_idx = load_pool_topics()
    client = AIClient()
    items: dict[str, dict] = {}
    t0 = time.time()
    done = 0

    def persist(fn: str, result: dict) -> None:
        """apply 模式把裁决写回卡片（主线程调用，无并发写）。"""
        tags = result.get("tags") or []
        card = cards[fn]
        if not isinstance(card.get("links"), dict):
            card["links"] = {}
        if not isinstance(card.get("trust"), dict):
            card["trust"] = {}
        card["links"]["scenario_tags_v2"] = tags
        card["trust"]["vocab_ver"] = tv.load_vocab()["vocab_ver"]
        dom = derive_domain(tags)
        if dom:
            card["links"]["domain"] = dom
        cstore.write_card(card)

    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = {ex.submit(adjudicate, client, cards[fn], topics_idx.get(fn, [])): fn
                for fn in targets}
        for fut in as_completed(futs):
            fn = futs[fut]
            try:
                r = fut.result()
                if apply_mode:
                    persist(fn, r)
            except Exception as e:                       # noqa: BLE001 全身防御（s8 教训）
                log.error("%s 失败: %s", fn, str(e)[:200])
                r = {"error": str(e)[:200], "tags": [], "ok": False}
            items[fn] = r
            done += 1
            if done % 20 == 0:
                log.info("进度 %d/%d (%.0fs)", done, len(targets), time.time() - t0)
    mode = ("force" if args.force else "missing") if apply_mode else "sample"
    out = {"meta": {"mode": mode, "vocab_ver": tv.load_vocab()["vocab_ver"],
                    "model": client.harness, "targets": len(targets),
                    "seed": args.seed, "wall_s": round(time.time() - t0, 1),
                    "ts": time.strftime("%F %T")},
           "items": dict(sorted(items.items()))}
    out_path = RETAG_OUT if apply_mode else SAMPLE_OUT
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = sum(1 for r in items.values() if r.get("ok"))
    print(f"[{mode}] 完成 {ok}/{len(targets)}（0 标签 {len(targets)-ok}），"
          f"wall {out['meta']['wall_s']}s -> {out_path}")
    return out


def _zh(slugs: list[str]) -> str:
    v = tv.load_vocab()
    return "、".join(v["_by_slug"][s]["zh"] for s in slugs if s in v["_by_slug"])


def cmd_evaluate(args) -> dict:
    sample = json.loads(SAMPLE_OUT.read_text(encoding="utf-8"))
    cards = cstore.all_cards()
    v2_counter, new_counter = Counter(), Counter()
    jac, both, new_only, old_only = [], Counter(), Counter(), Counter()
    zero_new = errors = 0
    zero_old_filled = zero_old_total = 0
    for fn, r in sorted(sample["items"].items()):
        card = cards.get(fn) or {}
        old = (card.get("links") or {}).get("scenario_tags_v2") or []
        if r.get("error"):                       # 网络/异常失败≠合法不选，单列
            errors += 1
            continue
        new = r.get("tags") or []
        if not old:
            zero_old_total += 1
            if new:
                zero_old_filled += 1
        v2_counter.update(old)
        new_counter.update(new)
        if not new:
            zero_new += 1
        inter = len(set(old) & set(new))
        union = len(set(old) | set(new))
        if union:
            jac.append(inter / union)
            for s in new:
                (new_only if s not in old else both).update([s])
            for s in old:
                if s not in new:
                    old_only.update([s])
    jac.sort()
    per_repo_new = sorted(len(r.get("tags") or []) for r in sample["items"].values()
                          if not r.get("error"))
    per_repo_old = sorted(len((cards.get(fn) or {}).get("links", {}).get("scenario_tags_v2") or [])
                          for fn in sample["items"] if fn in cards)
    n = len(per_repo_new)
    q = lambda a, i: a[min(i, len(a) - 1)] if a else 0
    rep = {
        "sample_n": n, "errors": errors, "model": sample["meta"]["model"],
        "tags_per_repo_new": {"median": q(per_repo_new, n // 2), "p25": q(per_repo_new, n // 4),
                              "p75": q(per_repo_new, 3 * n // 4), "zero": zero_new},
        "tags_per_repo_old": {"median": q(per_repo_old, len(per_repo_old) // 2)},
        "jaccard_median": round(q(jac, len(jac) // 2), 3) if jac else 0,
        "zero_old_fill": {"n": zero_old_total, "filled": zero_old_filled,
                          "pct": round(zero_old_filled / max(zero_old_total, 1) * 100, 1)},
        "new_tag_counts": dict(new_counter.most_common()),
        "old_tag_counts": dict(v2_counter.most_common()),
        "top_new_only": dict(new_only.most_common(12)),
        "top_old_only": dict(old_only.most_common(12)),
        "verdicts": {},
    }
    tgt = tv.load_vocab()["rules"]
    rep["verdicts"]["median_in_2_4"] = 2 <= q(per_repo_new, n // 2) <= 4
    rep["verdicts"]["zero_new_le_5pct"] = zero_new / max(n, 1) <= 0.05
    rep["verdicts"]["jaccard_ge_034"] = rep["jaccard_median"] >= 0.34
    rep["verdicts"]["zero_old_fill_ge_80"] = rep["zero_old_fill"]["pct"] >= 80
    bf = json.loads(BACKFILL_REPORT.read_text(encoding="utf-8")) if BACKFILL_REPORT.is_file() else {}
    if bf:
        rep["verdicts"]["top100_landed_ge_90"] = bf.get("top100_landed_pct", 0) >= 90
        rep["verdicts"]["zero_backfill_diagnostic"] = round(
            bf.get("zero_tag_n", 0) / max(bf.get("cards", 1), 1) * 100, 1)  # 重打标前的诊断值
        rep["verdicts"]["density_ok"] = not bf.get("low_density")
        rep["verdicts"]["low_density_tags"] = bf.get("low_density")
    spot = []
    for fn, r in list(sample["items"].items())[:12]:
        card = cards.get(fn) or {}
        spot.append({"fn": fn,
                     "one_liner": (card.get("identity") or {}).get("one_liner", "")[:60],
                     "old_v2": _zh((card.get("links") or {}).get("scenario_tags_v2") or []),
                     "new": _zh(r.get("tags") or [])})
    rep["spot_check"] = spot
    EVAL_OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: rep[k] for k in ("sample_n", "tags_per_repo_new",
                                          "tags_per_repo_old", "jaccard_median",
                                          "verdicts")}, ensure_ascii=False, indent=1))
    print("top 新增(新打有/回填无):", dict(list(rep["top_new_only"].items())[:6]))
    print("top 丢弃(回填有/新打无):", dict(list(rep["top_old_only"].items())[:6]))
    print("抽检前 6 行:")
    for s in spot[:6]:
        print(f"  {s['fn']} | {s['one_liner']}\n    旧[{s['old_v2']}] -> 新[{s['new']}]")
    print("报告:", EVAL_OUT)
    return rep


def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s", style="%")
    ap = argparse.ArgumentParser(description="s10 场景标签：回填/抽样打标/评测")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("backfill", help="存量卡片回填 scenario_tags_v2")
    b.add_argument("--dry-run", action="store_true", help="只出报告不改卡")
    b.set_defaults(fn=cmd_backfill)
    t = sub.add_parser("tag", help="抽样并发打标")
    t.add_argument("--sample", type=int, default=80)
    t.add_argument("--seed", type=int, default=7)
    t.add_argument("--concurrency", type=int, default=6)
    t.add_argument("--missing", action="store_true",
                   help="增量模式：只给缺 scenario_tags_v2 的卡打标并写回")
    t.add_argument("--force", action="store_true",
                   help="全量重打：覆盖所有卡的 v2 并写回（含 domain 组名派生）")
    t.add_argument("--limit", type=int, default=0, help="missing/force 模式的数量上限")
    t.set_defaults(fn=cmd_tag)
    e = sub.add_parser("evaluate", help="对比抽样与回填，出验收判据")
    e.set_defaults(fn=cmd_evaluate)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
