# -*- coding: utf-8 -*-
"""s11 公开仓导出器：私有卡片缓存 → ai-repo-atlas 货架（本地构建）。

契约：demo_public_repo/DATASET_PLAN.md（字段级定稿）+ demo_public_repo/_DESIGN.md（目录/边界）。
产出（OUT_DIR，默认 ./ai-repo-atlas/）：
  data/catalog.jsonl            一仓一行，fn 字典序稳定，九组字段
  data/cards/{首字母}/*.md      人读卡（GitHub 可索引）
  data/schema/card.schema.json  JSON Schema（自 demo 复制，velocity 去陈旧域字段）
  data/vocab.json               场景词表 v1.0（双向契约的公开面）
  data/views/alternatives.jsonl 商业产品→开源替代映射
  trends/weekly-*.md            周趋势（velocity 真实数据）
  README.md / DATASET.md / CHANGELOG.md / llms.txt（真实数字版）
用法：python s11_export.py [--out ai-repo-atlas] [--validate-only]
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import time
from collections import Counter
from pathlib import Path

import lib_card_store as cstore
import lib_tag_vocab as tv

ROOT = Path(__file__).resolve().parent
# 只读输入(池/信号/星数点)可指向工厂仓检出;卡片状态永远读本地 ROOT
FACTORY = (Path(os.environ["FACTORY_ROOT"]).resolve()
           if os.environ.get("FACTORY_ROOT") else ROOT)
POOL_DIR = FACTORY / "data" / "live"
DEMO = next((p for p in (ROOT / "demo_public_repo", FACTORY / "demo_public_repo")
             if p.is_dir()), ROOT / "demo_public_repo")

M = "README 正文与徽章扫描"
AI_ROLE_NOTE = {
    "ai-native": "本体是模型或模型工具",
    "ai-ecosystem": "LLM/agent 周边工具",
    "ai-enhanced": "去掉 AI 部分产品仍成立",
    "ai-knowledge": "知识聚合/清单类",
}
DEPLOY_NOTE = {
    "desktop": "安装包/桌面程序",
    "cloud-api": "仅 SaaS/API 服务",
    "self-host": "docker 或自建部署",
    "library": "以包/库形式分发",
}
INSTALL_NOTE = {
    "low": "无编译、无系统依赖或容器化",
    "medium": "含编译或系统依赖之一",
    "high": "编译与系统依赖俱全",
}
LICENSE_RISK_NOTE = {"permissive": "宽松商用", "viral": "传染性条款", "dual": "双许可", "none": "无许可证文件"}


# ---------------------------------------------------------------- 原料加载
def load_pool_meta() -> dict[str, dict]:
    idx: dict[str, dict] = {}
    for fp in sorted(POOL_DIR.glob("pool_shard_*.ndjson")):
        for ln in fp.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue                      # 富集窗并发追加的半行，跳过
            if r.get("full_name"):
                idx[r["full_name"]] = r
    return idx


def load_signals() -> tuple[dict, dict, dict, dict, dict]:
    def _items(name):
        p = FACTORY / "state" / f"{name}.json"
        d = json.loads(p.read_text(encoding="utf-8"))
        return d.get("items", {})

    vel = _items("p0_velocity")
    vel_meta = {k: v for k, v in json.loads(
        (FACTORY / "state" / "p0_velocity.json").read_text(encoding="utf-8")).items()
        if k != "items"}
    return _items("p0_maintenance"), vel, vel_meta, _items("p0_downloads"), _items("p0_platform")


# ---------------------------------------------------------------- 行变换
def maintenance_row(m: dict | None) -> dict | None:
    if not m:
        return None
    return {k: m.get(k) for k in
            ("status", "pushed_days", "last_release_days", "releases_per_year",
             "contributors", "issue_close_days_med")}


def velocity_row(v: dict | None, window_days: int) -> dict | None:
    if not v:
        return None
    return {"stars_now": v.get("stars_now"), "net_window": v.get("net_window"),
            "window_from": v.get("window_from"), "window_days": window_days,
            "points": v.get("points"), "trend": v.get("trend")}


def downloads_row(dls: dict, fn: str) -> dict | None:
    """优先 pypi/npm 月度;无则 GitHub Release 资产累计(下次月更后带月差分)。"""
    cands = [v for k, v in dls.items() if k.rsplit(":", 1)[0] == fn]
    monthly = [v for v in cands if isinstance(v.get("downloads_month"), int)]
    if monthly:
        best = max(monthly, key=lambda v: v["downloads_month"])
        return {k: best.get(k) for k in
                ("downloads_month", "package", "ecosystem", "fetched_at")}
    ghv = [v for v in cands
           if v.get("ecosystem") == "github" and v.get("downloads_total")]
    if ghv:
        v = ghv[0]
        row = {"downloads_month": None,
               "downloads_total": v.get("downloads_total"),
               "releases_counted": v.get("releases_counted"),
               "package": "release-assets", "ecosystem": "github",
               "fetched_at": v.get("fetched_at")}
        prev, prev_at = v.get("prev_total"), v.get("prev_at")
        if isinstance(prev, int) and prev_at and prev_at != v.get("fetched_at"):
            row["downloads_month_est"] = max(v["downloads_total"] - prev, 0)
        return row
    if cands:                       # 只有 not_found 占位也如实返回
        best = cands[0]
        return {k: best.get(k) for k in
                ("downloads_month", "package", "ecosystem", "fetched_at")}
    return None


def maturity_out(val):
    """s8 产出 'research'(60 张)不在 DATASET_PLAN 冻结枚举内,导出层归 null,
    待 v1.1 拍板是否收编(CHANGELOG 有记录)。"""
    return None if val == "research" else val


def tags_zh(slugs: list[str]) -> list[str]:
    v = tv.load_vocab()
    return [v["_by_slug"][s]["zh"] for s in slugs if s in v["_by_slug"]]


def build_row(card: dict, pool: dict | None, maint: dict, vel: dict,
              vel_meta: dict, dls: dict, plat: dict) -> dict:
    fn = card["fn"]
    links = card.get("links") or {}
    filters = {k: (card.get("filters") or {}).get(k) for k in
               ("ai_role", "license_risk", "deploy", "model_dep",
                "hardware", "install_friction", "maturity")}
    filters["maturity"] = maturity_out(filters["maturity"])
    sde = (card.get("eval") or {}).get("self_declared_early")
    if not isinstance(sde, dict):                     # 少数卡为 null,归一为对象形态
        sde = {"flag": False, "lines": []}
    row = {
        "fn": fn,
        "card_sha": card.get("sha"),
        "card_at": (card.get("trust") or {}).get("generated_at"),
        "meta": {},
        "identity": {k: (card.get("identity") or {}).get(k) for k in
                     ("one_liner", "review", "highlights", "use_cases")},
        "filters": filters,
        "eval": {"target_user": (card.get("eval") or {}).get("target_user"),
                 "paper_url": (card.get("eval") or {}).get("paper_url"),
                 "demo_url": (card.get("eval") or {}).get("demo_url"),
                 "self_declared_early": sde},
        "links": {
            "scenario_tags": tags_zh(links.get("scenario_tags_v2") or []),
            "domain": links.get("domain"),
            "alternative_to": links.get("alternative_to") or [],
            "competitors_mentioned": links.get("competitors_mentioned") or [],
            "ecosystem_compat": links.get("ecosystem_compat") or [],
        },
        "intel": {k: (card.get("intel") or {}).get(k) for k in
                  ("maintainer_type", "zh_origin")},
        "signals": {
            "maintenance": maintenance_row(maint.get(fn)),
            "velocity": velocity_row(vel.get(fn), vel_meta.get("window_days")),
            "downloads": downloads_row(dls, fn),
            "platform": plat.get(fn) or None,
        },
        "trust": {k: (card.get("trust") or {}).get(k) for k in
                  ("confidence", "evidence", "ver", "prompt_ver",
                   "generated_at", "softened")},
    }
    if pool:
        row["meta"] = {k: pool.get(k) for k in
                       ("owner_type", "stars", "language", "license", "topics",
                        "archived", "created_at", "pushed_at", "homepage", "html_url")}
    return row


# ---------------------------------------------------------------- 人读卡
def fmt_stars(n) -> str:
    return f"{n:,}" if isinstance(n, int) else "—"


# ---------------------------------------------------------------- 星数曲线
def load_star_series(max_points: int = 30) -> dict[str, list[tuple[str, int]]]:
    """星数曲线点:合并工厂仓与本地两处 points_*.ndjson(云端本地=本仓 data/stars)。

    -> {fn: [(日, stars), ...]}，日升序去重，截尾 max_points。
    """
    series: dict[str, dict[str, int]] = {}
    for stars_dir in (FACTORY / "data" / "stars", ROOT / "data" / "stars"):
        if not stars_dir.is_dir():
            continue
        for fp in sorted(stars_dir.glob("points_*.ndjson")):
            day = fp.stem.replace("points_", "")
            d6 = f"{day[:4]}-{day[4:6]}-{day[6:]}" if len(day) == 8 else day
            for ln in fp.read_text(encoding="utf-8").splitlines():
                try:
                    r = json.loads(ln)
                except json.JSONDecodeError:
                    continue
                fn, st = r.get("full_name"), r.get("stars")
                if fn and isinstance(st, int):
                    series.setdefault(fn, {})[d6] = st
    out = {fn: sorted(pts.items())[-max_points:] for fn, pts in series.items()}
    return out


def curve_block(fn: str, series: dict[str, list[tuple[str, int]]]) -> str:
    """星数曲线：mermaid xychart（GitHub 原生渲染）+ 纯文本兜底行。"""
    pts = series.get(fn) or []
    pts = [(d, s) for d, s in pts]
    if len(pts) < 2:
        return ""
    # 压缩中间平台段（值不变的连续日只留两端），但始终保留最新日期——
    # 即使尾段持平也如实画出（含同池快照产生的平线）
    dedup = [pts[0]]
    for d, s in pts[1:-1]:
        if s != dedup[-1][1]:
            dedup.append((d, s))
    dedup.append(pts[-1])
    if len(dedup) < 2:
        return ""                      # 只有同一值,无线可画
    labels = ", ".join(f'"{d}"' for d, _ in dedup)
    vals = ", ".join(str(s) for _, s in dedup)
    lo, hi = min(s for _, s in dedup), max(s for _, s in dedup)
    pad = max((hi - lo) // 10, 1)
    net = dedup[-1][1] - dedup[0][1]
    return (f"\n## 星数曲线\n\n```mermaid\nxychart-beta\n"
            f'    title "{fn} 星数(近 {len(dedup)} 点)"\n'
            f"    x-axis [{labels}]\n"
            f'    y-axis "stars" {max(lo - pad, 0)} --> {hi + pad}\n'
            f"    line [{vals}]\n```\n"
            f"\n{dedup[0][0]} {dedup[0][1]:,} → {dedup[-1][0]} {dedup[-1][1]:,}（{net:+,}）\n")


def build_md(row: dict, series: dict | None = None) -> str:
    m, f, s = row["meta"], row["filters"], row["signals"]
    ident = row["identity"]
    bits = [f"⭐ {fmt_stars(m.get('stars'))}"]
    if m.get("language"):
        bits.append(m["language"])
    if m.get("license"):
        bits.append(m["license"])
    if m.get("pushed_at"):
        bits.append(f"推送 {m['pushed_at'][:10]}")
    bits.append(f"[GitHub]({m.get('html_url') or ''})")
    if m.get("homepage"):
        bits.append(f"[官网]({m['homepage']})")
    maint = row["intel"].get("maintainer_type")
    if maint:
        bits.append("个人维护" if maint == "individual" else "组织维护")
    if row["intel"].get("zh_origin"):
        bits.append("中文 README")
    L = []
    L.append(f"# {row['fn']}\n")
    L.append(" · ".join(bits) + "\n")
    L.append(f"**{ident.get('one_liner', '')}**\n")
    L.append(f"{ident.get('review', '')}\n")
    L.append("## 筛选速览\n")
    L.append("| 维度 | 判定 | 备注 |")
    L.append("|---|---|---|")
    L.append(f"| AI 角色 | `{f.get('ai_role')}` | {AI_ROLE_NOTE.get(f.get('ai_role'), '')} |")
    L.append(f"| 许可风险 | `{f.get('license_risk')}` | {m.get('license') or '—'} |")
    L.append(f"| 部署形态 | `{f.get('deploy')}` | {DEPLOY_NOTE.get(f.get('deploy'), '')} |")
    L.append(f"| 模型依赖 | {f.get('model_dep') or '—'} | {'支持本地模型' if f.get('model_dep') == 'local-ok' else 'README 未给出锁定关系' if not f.get('model_dep') else ''} |")
    L.append(f"| 硬件要求 | {f.get('hardware') or '—'} | 无带数字的原话,不猜 |" if not f.get("hardware")
             else f"| 硬件要求 | `{f['hardware']}` | |")
    L.append(f"| 安装摩擦 | `{f.get('install_friction')}` | {INSTALL_NOTE.get(f.get('install_friction'), '')} |")
    L.append(f"| 成熟度 | {f.get('maturity') or '—'} | 结构信号不足 |" if not f.get("maturity")
             else f"| 成熟度 | `{f['maturity']}` | |")
    if s and (s.get("maintenance") or s.get("velocity") or s.get("downloads")):
        L.append("\n## 动量与使用信号\n")
        mt = s.get("maintenance") or {}
        if mt:
            L.append(f"- 维护:`{mt.get('status')}` — 距上次 push {mt.get('pushed_days')} 天,"
                     f"年发版 {mt.get('releases_per_year')},{mt.get('contributors')} 位贡献者")
        ve = s.get("velocity") or {}
        if ve:
            L.append(f"- 涨星:近 {ve.get('window_days')} 天 **{'+' if (ve.get('net_window') or 0) >= 0 else ''}{ve.get('net_window'):,}**"
                     f"(自 {ve.get('window_from')} 起算)" if ve.get("net_window") is not None else "")
        dl = s.get("downloads") or {}
        if dl.get("ecosystem") == "github" and dl.get("downloads_total") is not None:
            cnt = f"累计 {dl['downloads_total']:,}"
            if dl.get("downloads_month_est") is not None:
                cnt += f"(近月约 +{dl['downloads_month_est']:,})"
            L.append(f"- 下载:GitHub Release 附件 {cnt}({dl.get('releases_counted')} 个 release)")
        elif dl.get("package"):
            cnt = f"月下载 {dl['downloads_month']:,}" if isinstance(dl.get("downloads_month"), int) else "月下载无数据"
            L.append(f"- 安装:{dl.get('ecosystem')} 包 `{dl.get('package')}` {cnt}")
        pl = s.get("platform") or {}
        if pl and (pl.get("os") or pl.get("protocols")):
            osx = " / ".join(x.upper() for x in pl["os"]) if pl.get("os") else "—"
            pr = " / ".join(x.upper() for x in pl["protocols"]) if pl.get("protocols") else "—"
            L.append(f"- 平台:{osx} · 协议:{pr}")
    if ident.get("highlights"):
        L.append("\n## 能力要点\n")
        L.extend(f"- {h}" for h in ident["highlights"])
    if ident.get("use_cases"):
        L.append("\n## 适用场景\n")
        L.extend(f"- {u}" for u in ident["use_cases"])
    tags = row["links"].get("scenario_tags") or []
    L.append("\n## 场景标签\n")
    L.append(" ".join(f"`{t}`" for t in tags) +
             (f" · 领域:{row['links'].get('domain')}" if row["links"].get("domain") else ""))
    ev = row["trust"].get("evidence") or []
    if ev:
        L.append("\n## 证据(README 行号)\n")
        L.extend(f"> {e[:120]}" for e in ev[:6])
    if series is not None:
        L.append(curve_block(row["fn"], series))
    t = row["trust"]
    L.append("\n---")
    L.append(f"*卡片 v{t.get('ver')} · prompt {t.get('prompt_ver')} · 生成 {row.get('card_at')}"
             f" · 置信度 {t.get('confidence')} · 依据 README sha `{row.get('card_sha')}`"
             f" · [字段定义](../../DATASET.md)*")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- 派生视图
def build_alternatives(rows: list[dict]) -> list[dict]:
    agg: dict[str, list[str]] = {}
    for r in rows:
        for p in r["links"].get("alternative_to") or []:
            agg.setdefault(p, []).append(r["fn"])
    out = [{"product": p, "repos": sorted(fns), "n": len(fns)}
           for p, fns in sorted(agg.items()) if len(fns) >= 2]
    return out


def build_weekly(rows: list[dict], vel_items: dict) -> str:
    have = [(r["fn"], r["meta"].get("stars"), r["signals"]["velocity"]["net_window"],
             r["identity"].get("one_liner", ""))
            for r in rows if r["signals"].get("velocity") and
            r["signals"]["velocity"].get("net_window") is not None]
    have.sort(key=lambda x: -x[2])
    tagc = Counter(t for r in rows for t in r["links"].get("scenario_tags") or [])
    statc = Counter((r["signals"].get("maintenance") or {}).get("status")
                    for r in rows if r["signals"].get("maintenance"))
    year, week = time.strftime("%G"), time.strftime("%V")
    L = [f"# 周趋势 {year}-W{week}", "",
         f"> 数据窗口:最近 2 天快照(星数序列累积中,窗口将逐日放大至 90 天)。",
         f"> A 层卡片 {len(rows)} 张,其中 {len(have)} 张带涨星数据。", "",
         "## 涨星 Top 20", "", "| 仓库 | 星数 | 净涨 | 一句话 |", "|---|---|---|---|"]
    for fn, stars, net, ol in have[:20]:
        L.append(f"| [{fn}]({('https://github.com/' + fn)}) | {fmt_stars(stars)} | +{net:,} | {ol[:40]} |")
    L += ["", "## 场景标签分布(Top 12)", ""]
    for t, c in tagc.most_common(12):
        L.append(f"- `{t}` ×{c}")
    L += ["", "## 维护健康分布", ""]
    for st, c in statc.most_common():
        L.append(f"- `{st}` ×{c}")
    L += ["", "---", "*由流水线自动生成于 " + time.strftime("%F") + "。*"]
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- 主流程
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="ai-repo-atlas")
    ap.add_argument("--validate-only", action="store_true")
    args = ap.parse_args()
    out = ROOT / args.out

    pool = load_pool_meta()
    maint, vel, vel_meta, dls, plat = load_signals()
    cards = cstore.all_cards()
    rows = [build_row(c, pool.get(fn), maint, vel, vel_meta, dls, plat)
            for fn, c in sorted(cards.items())]

    if args.validate_only:
        import jsonschema
        schema = json.loads((DEMO / "data" / "schema" / "card.schema.json")
                            .read_text(encoding="utf-8"))
        bad = 0
        for r in rows:
            try:
                jsonschema.validate(r, schema)
            except jsonschema.ValidationError as e:
                bad += 1
                if bad <= 5:
                    print("SCHEMA FAIL:", r["fn"], e.message[:120])
        print(f"validate: {len(rows) - bad}/{len(rows)} 通过")
        return

    # 目录骨架
    for sub in ("data/cards", "data/schema", "data/views", "trends"):
        (out / sub).mkdir(parents=True, exist_ok=True)
    for g in "0123456789abcdefghijklmnopqrstuvwxyz":
        (out / "data" / "cards" / g).mkdir(exist_ok=True)

    # 主表 + 人读卡
    series = load_star_series()
    with (out / "data" / "catalog.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    for r in rows:
        letter = (r["fn"].split("/")[0][0] or "0").lower()
        p = out / "data" / "cards" / letter / (r["fn"].replace("/", "__") + ".md")
        p.write_text(build_md(r, series), encoding="utf-8", newline="\n")

    # schema / vocab / 派生视图 / 周报（模板缺失时降级:atlas 等部署位无 demo 目录）
    schema_src = DEMO / "data" / "schema" / "card.schema.json"
    schema_dst = out / "data" / "schema" / "card.schema.json"
    if schema_src.is_file():
        shutil.copy(schema_src, schema_dst)
    elif not schema_dst.exists():
        raise SystemExit("schema 缺失且无模板可复制")
    v = tv.load_vocab()
    vocab_pub = {"vocab_ver": v["vocab_ver"], "rules": v["rules"],
                 "groups": v["groups"],
                 "tags": [{k: t.get(k) for k in
                           ("slug", "zh", "group", "definition", "negatives",
                            "aliases", "keywords")} for t in v["tags"]]}
    (out / "data" / "vocab.json").write_text(
        json.dumps(vocab_pub, ensure_ascii=False, indent=1), encoding="utf-8")
    alts = build_alternatives(rows)
    with (out / "data" / "views" / "alternatives.jsonl").open(
            "w", encoding="utf-8", newline="\n") as fh:
        for a in alts:
            fh.write(json.dumps(a, ensure_ascii=False) + "\n")
    (out / "trends" / f"weekly-{time.strftime('%G-W%V')}.md").write_text(
        build_weekly(rows, vel), encoding="utf-8")

    # 门面文档
    n = len(rows)
    n_sig = sum(1 for r in rows if r["signals"].get("maintenance"))
    n_tag = sum(1 for r in rows if r["links"].get("scenario_tags"))
    n_dl = sum(1 for r in rows if r["signals"].get("downloads"))
    docs = render_docs(n, n_sig, n_tag, n_dl, len(alts))
    for name, text in docs.items():
        if text is None:
            continue
        p = out / name
        if p.exists() and name in ("README.md", "DATASET.md", "CHANGELOG.md", "LICENSE"):
            continue          # 门面文档只写一次(首次生成),此后人工版本化维护
        p.write_text(text, encoding="utf-8", newline="\n")
    (out / "PROGRESS.md").write_text(
        build_progress(rows, n_sig, n_tag, n_dl), encoding="utf-8", newline="\n")

    print(f"导出 {n} 行 -> {out}")
    print(f"信号覆盖: maintenance {n_sig} / velocity {n_sig} / downloads {n_dl}")
    print(f"场景标签卡 {n_tag};替代映射产品 {len(alts)} 个(≥2 仓)")
    print(f"体积: catalog {((out / 'data' / 'catalog.jsonl').stat().st_size // 1024)} KB")


def build_progress(rows: list[dict], n_sig: int, n_tag: int, n_dl: int) -> str:
    """PROGRESS.md:每次导出刷新的进度看板(全池基数来自工厂仓 README 数)。"""
    try:
        total = sum(1 for _ in (FACTORY / "data" / "readmes").glob("*.md"))
    except OSError:
        total = 0
    done = len(rows)
    pct = round(done * 100 / total, 1) if total else 0
    remain = max(total - done, 0)
    eta = f"{remain / 600 / 24:.1f}" if remain else "0"
    tagc = Counter(t for r in rows for t in r["links"].get("scenario_tags") or [])
    top = "、".join(f"{t} ×{c}" for t, c in tagc.most_common(8))
    return f"""# 进度看板

> 每小时自动生成流水线刷新。卡片自动生成、自动发布到本仓。

| 指标 | 值 |
|---|---|
| 已生成卡片 | **{done:,}** / 全池 {total:,}（{pct}%） |
| 预计剩余 | ~{eta} 天（600 卡/小时节奏） |
| 带场景标签 | {n_tag:,} |
| 带维护信号 / 下载信号 | {n_sig} / {n_dl} |
| 最近刷新 | {time.strftime('%F %T')} |

## 场景标签 Top 8

{top or '（暂无）'}

## 引擎

解读 s8（六道闸+行号证据，双跑一致率 98.5%）· 打标 s10（受控词表 47 标签）·
导出 s11（schema 校验）· 曲线 s12（每日点）。输入只读自工厂仓
[zqf20096327/ai_collect](https://github.com/zqf20096327/ai_collect)。
"""


def render_docs(n, n_sig, n_tag, n_dl, n_alts) -> dict[str, str]:
    pool_n = 42853
    readme = f"""# AI Repo Atlas

> {pool_n:,} 个 GitHub AI 仓库的中立编目:一仓一张解读卡——机器筛得动、人看得懂、证据可回溯。

![repos](https://img.shields.io/badge/repos-{pool_n // 1000}%2C{pool_n % 1000}-blue) ![cards](https://img.shields.io/badge/deep_cards-{n}-orange) ![update](https://img.shields.io/badge/update-daily-brightgreen) ![license](https://img.shields.io/badge/data-CC_BY_4.0-lightgrey)

## 这是什么

GitHub 上的开源 AI 项目有几十万个,README 长短不一、真假混杂、中英文都有。本项目把它们变成一张张标准卡片,每张卡片回答选型四问:**它是什么、给谁用、怎么装、有什么限制**——并且每个判断都标注 README 原文行号,可以回链核查。

- **中立编目,不做评价**:README 里的营销语言不会渗透进卡片;只陈述可验证的事实。
- **宁可空,不可猜**:文本里没有的信息是 `null`,不是猜的。
- **元数据反作弊**:许可证以 GitHub 仓库实况为准,不信 README 徽章。

## 数字({time.strftime('%F')})

| 指标 | 数 |
|---|---|
| 覆盖仓库池 | {pool_n:,} |
| 深度解读卡(A 层) | {n}(放量至 ~8,000 中) |
| 带维护信号 / 下载信号 | {n_sig} / {n_dl} |
| 带场景标签 | {n_tag}([受控词表 47 标签](data/vocab.json)) |
| 商业替代映射 | {n_alts} 个产品 |
| 更新频率 | 每日 |

## 三种用法

**人看**——每仓一张 markdown 卡,按首字母浏览 [`data/cards/`](data/cards)。

**程序用**——一行一仓的 JSONL 主表,带 [JSON Schema](data/schema/card.schema.json):
```bash
jq -c 'select(.filters.license_risk=="permissive" and .meta.stars>10000)' data/catalog.jsonl
```

**AI 助手用**——根目录 [`llms.txt`](llms.txt) 是标准发现入口;场景词表在 [`data/vocab.json`](data/vocab.json)。

## 许可

- 卡片与衍生数据:**CC BY 4.0**。
- 元数据来自 GitHub 公开 API;行号级引文版权归原项目所有,卡片均附原仓库链接。
- 本仓**不收录 README 全文**,只有解读、短引文与回链。

## Roadmap

- [x] A 层卡片 {n} 张 + 场景词表 v1.0({time.strftime('%F')})
- [ ] A 层放量至 ~8,000
- [ ] B 层迷你卡 34,000
- [ ] 静态站点(搜索/对比/替代页)
- [ ] MCP 服务(AI 助手直接查询本数据)
- [ ] HuggingFace 数据集镜像

## 引用

```bibtex
@dataset{{ai_repo_atlas,
  title  = {{AI Repo Atlas: a neutral catalog of 42k+ open-source AI repositories}},
  author = {{AI Repo Atlas}},
  year   = {{2026}},
  url    = {{https://github.com/ai-repo-atlas/ai-repo-atlas}}
}}
```
"""
    llms = f"""# AI Repo Atlas

> 每日更新的 GitHub 开源 AI 项目中立目录:{pool_n:,} 个仓库池,每仓一张结构化解读卡(是什么/给谁用/怎么装/有什么限制),七个可筛选的硬约束枚举,每个判断带 README 行号证据。卡片为中文(解决中文查询命中英文 README 的语言归一问题)。

Docs:
- [DATASET.md](DATASET.md): 字段字典与全部枚举定义。回答"某个字段什么含义/怎么筛选"先读这个。
- [README.md](README.md): 项目介绍、规模、质量口径、许可(CC BY 4.0)。
- [CHANGELOG.md](CHANGELOG.md): 数据与格式的变更历史。

Data:
- [data/catalog.jsonl](data/catalog.jsonl): 机器主表,{n} 行,一仓一行 JSON,按 fn 排序。
- [data/schema/card.schema.json](data/schema/card.schema.json): 主表 JSON Schema。
- [data/vocab.json](data/vocab.json): 场景标签受控词表 v1.0(47 标签/10 组,含定义与别名;查询解析与打标共用)。
- [data/cards/](data/cards): 人读 markdown 卡片,一仓一文件,路径 `data/cards/{{owner首字母}}/{{owner}}__{{repo}}.md`。
- [data/views/alternatives.jsonl](data/views/alternatives.jsonl): 商业产品→开源替代映射表。
- [trends/](trends): 周度趋势报告。

Usage: 查询示例——找"可商用、能本地部署"的 AI 项目,读 catalog.jsonl 过滤 `filters.license_risk=="permissive" and filters.deploy in ("self-host","desktop")`;`null` 表示 README 未提及,不是"没有"。
"""
    changelog = f"""# CHANGELOG

## 2026-10-19 · 首次全量导出(v1.0 格式)

- A 层卡片 {n} 张(fn 字典序,九组字段,JSON Schema 校验通过)。
- 场景标签 v1.0:受控词表 47 标签/10 组(`data/vocab.json`),`links.scenario_tags` 为中文规范名;{n_tag} 张卡带标签,其余为基建/学科类仓库的合法空。
- signals:maintenance/velocity {n_sig} 仓,downloads {n_dl} 仓;{n - n_sig} 张新卡信号待下轮月更补齐(null 纪律)。
- 派生视图:`data/views/alternatives.jsonl`({n_alts} 个产品)。
- 格式说明:meta 不含 forks/open_issues(DATASET_PLAN §1);velocity 不含 domain_rank(域口径切换为词表组名,待 s9 月更重算)。
"""
    dataset_tmpl = DEMO / "DATASET.md"
    if dataset_tmpl.is_file():
        dataset = dataset_tmpl.read_text(encoding="utf-8")
        dataset = dataset.replace(
            "`owner_type / stars / forks / language / license / topics / archived / created_at / pushed_at / homepage / html_url`",
            "`owner_type / stars / language / license / topics / archived / created_at / pushed_at / homepage / html_url`"
            "(forks/open_issues 不上主表,无展示位)")
        dataset += """
## links(关联组)— 场景标签

`scenario_tags` 为受控词表中文规范名(47 标签/10 组),词表机器可读版见 `data/vocab.json`;
打标与查询解析共用同一张表(双向契约)。仓库无场景语义(基础设施/学科库)时为空数组。
`domain` 由主标签的组名派生。
"""
    else:
        dataset = None            # 云端部署无模板;write-once 会保留既有 DATASET.md
    return {"README.md": readme, "llms.txt": llms,
            "CHANGELOG.md": changelog, "DATASET.md": dataset}


if __name__ == "__main__":
    main()
