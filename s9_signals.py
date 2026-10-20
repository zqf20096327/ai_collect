# -*- coding: utf-8 -*-
"""s9 · P0 信号层:在 s8 卡片之外补四类用户最关心的数据。

  维护健康  maintenance   GitHub API 三件套(releases/contributors/issues)+池内 pushed_at
                          → 规则合成 maintenance 枚举(active/maintenance/declining/abandoned),月更
  涨星速度  velocity      快照/事件/活池的星数序列 → 窗口净涨 + 动量趋势 + 域内排名,日更
  包下载量  downloads     s8 install 裁决引文里的 pip/npm 包名 → PyPI/npm 免费 API 月下载,月更
  平台协议  platform      README 徽章/正文正则 → 支持平台 + 互通协议(openai-api/mcp/ollama)+ 界面语言

用法:
  python s9_signals.py                          # 全部(尊重新鲜度缓存)
  python s9_signals.py --only velocity,platform # 只跑指定项
  python s9_signals.py --only maintenance --force --limit 5   # 调试
  python s9_signals.py --export-demo            # 重建 demo catalog.jsonl(3 行加 signals 组)

状态: state/p0_{maintenance,velocity,downloads,platform}.json(原子写,留 3 代)。
对象: s8 缓存中 status=done 的卡片仓(A 层,试批 593)。
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402

STATE = st.STATE
MAINT_FRESH_DAYS = 25          # 维护事实慢变,月更口径
DL_FRESH_DAYS = 25
CHUNK_SAVE = 50                # 每处理 N 仓落盘一次


def u():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return default


def load_done_cards():
    """一仓一文件存储 → {fn: 卡片}(cstore 已按文件序≈fn 序,无需再选最新)。"""
    import lib_card_store as cstore
    return cstore.all_cards()


# ---------------- 涨星速度(本地) ----------------

def snap_star_points(target: set):
    """{fn: [(yyyymmdd, stars), ...]}:三个来源按日合并——
    ① data/stars/points_*.ndjson(现行设计:周一全池星数点,~2MB/周)
    ② snapshot_*/pool.ndjson(10-16 及以前的旧式全池快照,兼容历史)
    ③ 今日活池(当下值)。"""
    series = {fn: [] for fn in target}
    for f in sorted(st.DATA.glob("stars/points_*.ndjson")):
        day = f.name.replace("points_", "").replace(".ndjson", "")
        for line in f.open(encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            fn = r.get("full_name")
            if fn in series:
                series[fn].append((day, r.get("stars", 0)))
    days = []
    for f in sorted(st.DATA.glob("snapshot_*/pool.ndjson")):
        day = f.parent.name.replace("snapshot_", "")
        days.append(day)
        for line in f.open(encoding="utf-8"):
            if not line.strip():
                continue
            r = json.loads(line)
            fn = r.get("full_name")
            if fn in series:
                series[fn].append((day, r.get("stars", 0)))
    today = st.utc_day()
    for fn, rec in {r["full_name"]: r for r in st.load_pool().values()}.items():
        if fn in series and all(d != today for d, _ in series[fn]):
            series[fn].append((today, rec.get("stars", 0)))
    return series, days


def cmd_velocity(cards):
    target = set(cards)
    series, days = snap_star_points(target)
    span = (datetime.strptime(days[-1], "%Y%m%d") -
            datetime.strptime(days[0], "%Y%m%d")).days if days else 0
    win = min(90, max(span, 0))
    out = {"computed_at": st.utc_day(), "window_days": win,
           "history_days": span, "items": {}}
    # 域内排名:同 links.domain 按 win 净涨排序
    domains = {}
    for fn, pts in series.items():
        if not pts:
            continue
        d = (cards[fn].get("links", {}) or {}).get("domain")
        domains.setdefault(d, []).append(fn)
    for fn, pts in series.items():
        if not pts:
            continue
        pts = sorted(pts)
        stars_now = pts[-1][1]
        if win <= 0:
            start = pts[0]
        else:
            cutoff = (datetime.strptime(pts[-1][0], "%Y%m%d") -
                      timedelta(days=win)).strftime("%Y%m%d")
            start = max((p for p in pts if p[0] <= cutoff), default=pts[0])
        net = stars_now - start[1]
        d = (cards[fn].get("links", {}) or {}).get("domain")
        peers = [x for x in domains.get(d, []) if x in series and series[x]]
        rank = 1 + sum(1 for x in peers
                       if x != fn and
                       (series[x][-1][1] - series[x][0][1]) > net) if peers else None
        out["items"][fn] = {
            "stars_now": stars_now,
            "net_window": net,
            "window_from": start[0],
            "points": len(pts),
            "domain": d,
            "domain_rank": rank,
            "domain_size": len(peers) or None,
            "trend": None,   # 序列点数 ≥4 才判加速/减速,当前历史不足先置 null
        }
    st.atomic_write_json(STATE / "p0_velocity.json", out)
    n = len(out["items"])
    print(f"velocity: {n} 仓,历史 {span} 天,窗口 {win} 天"
          f"(历史不足 90 天属预期,周一星数点逐周累积后窗口自动放大)")
    top = sorted(out["items"].items(), key=lambda kv: -kv[1]["net_window"])[:5]
    for fn, v in top:
        print(f"  {fn}: {v['net_window']:+d} stars/{win}d  ({v['domain']})")


# ---------------- 平台/协议(本地 README 扫描) ----------------

PLAT_PATS = {
    "windows": re.compile(r"\bwindows\b", re.I),
    "macos": re.compile(r"\bmac ?os\b|\bmac os x\b", re.I),
    "linux": re.compile(r"\blinux\b", re.I),
    "android": re.compile(r"\bandroid\b", re.I),
    "ios": re.compile(r"\bios\b", re.I),
    "web": re.compile(r"\bweb[- ]based\b|\bbrowser[- ]based\b|\bweb ui\b"
                      r"|\bwebui\b|\bweb interface\b|\bweb app\b", re.I),
}
PROTO_PATS = {
    "openai-api": re.compile(r"openai[- ]compatible|openai api|chat/completions", re.I),
    "mcp": re.compile(r"\bmcp\b|model context protocol", re.I),
    "ollama": re.compile(r"\bollama\b", re.I),
}
CJK = re.compile(r"[\u4e00-\u9fff]")


def cmd_platform(cards, limit=None):
    out = {"computed_at": st.utc_day(), "items": {}}
    fns = list(cards)[:limit] if limit else list(cards)
    miss = 0
    for fn in fns:
        p = st.READMES / (fn.replace("/", "__") + ".md")
        if not p.exists():
            miss += 1
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            miss += 1
            continue
        head = text[:6000]          # 徽章区集中在头部;平台声明亦然
        plats = [k for k, pat in PLAT_PATS.items() if pat.search(head)]
        protos = [k for k, pat in PROTO_PATS.items() if pat.search(text)]
        n_cjk = len(CJK.findall(text))
        langs = []
        if n_cjk >= max(80, int(len(text) * 0.02)):
            langs.append("zh")
        if re.search(r"[A-Za-z]{3,}", text):
            langs.append("en")
        out["items"][fn] = {"os": plats, "protocols": protos,
                            "interface_lang": langs}
    st.atomic_write_json(STATE / "p0_platform.json", out)
    n_os = sum(1 for v in out["items"].values() if v["os"])
    n_pr = sum(1 for v in out["items"].values() if v["protocols"])
    n_zh = sum(1 for v in out["items"].values() if "zh" in v["interface_lang"])
    print(f"platform: {len(out['items'])} 仓(缺 README {miss}),"
          f"有平台信号 {n_os},有协议信号 {n_pr},含中文界面 {n_zh}")


# ---------------- 维护健康(GitHub API,月更) ----------------

def _days(iso):
    if not iso:
        return None
    try:
        t = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return round((datetime.now(timezone.utc) - t).total_seconds() / 86400, 1)
    except ValueError:
        return None


def _fresh_within(iso, max_days):
    """显式判 None:0.0 天(刚取)是新鲜,不能用 `or 默认值` 写法(0.0 是 falsy)。"""
    d = _days(iso)
    return d is not None and d < max_days


def fetch_maint_one(fn):
    """三件套调用(core 配额,0.8s/次节奏由 CORE_PACE 管)。"""
    gh.CORE_PACE.slot()
    _, rels = gh.api_get(f"/repos/{fn}/releases", {"per_page": 100})
    gh.CORE_PACE.slot()
    h, contrib = gh.api_get(f"/repos/{fn}/contributors", {"per_page": 1})
    gh.CORE_PACE.slot()
    _, issues = gh.api_get(f"/repos/{fn}/issues",
                           {"state": "closed", "sort": "updated",
                            "direction": "desc", "per_page": 30})
    rel_days = [d for d in (_days(r.get("published_at")) for r in rels)
                if d is not None and d <= 365]
    last_rel = min(rel_days) if rel_days else None
    per_year = len(rel_days)
    # 资产累计下载:同一响应免费捎带(附件自带 download_count,累计口径)
    asset_dl = sum(a.get("download_count") or 0
                   for r in rels for a in (r.get("assets") or []))
    link = h.get("Link") or ""
    m = re.search(r'[?&]page=(\d+)>; rel="last"', link)
    contributors = min(int(m.group(1)), 500) if m else len(contrib)
    closed = [(_days(i["closed_at"]) - _days(i["created_at"]))
              for i in issues
              if "pull_request" not in i and i.get("closed_at")
              and i.get("created_at")]
    closed = [c for c in closed if c is not None and c >= 0]
    closed.sort()
    med = closed[len(closed) // 2] if len(closed) >= 5 else None
    return {"last_release_days": last_rel, "releases_per_year": per_year,
            "contributors": contributors, "issue_close_days_med": med,
            "issue_sample": len(closed),
            "asset_downloads_total": asset_dl, "releases_counted": len(rels)}


def maint_enum(facts, pool_rec):
    archived = bool(pool_rec.get("archived"))
    pushed = _days(pool_rec.get("pushed_at"))
    if archived or (pushed is not None and pushed > 365):
        return "abandoned"
    if pushed is None:
        return None
    if pushed > 180:
        return "declining"
    if pushed > 90:
        return "maintenance"
    return "active"


def _merge_gh_dl(state_items: dict, fn: str, total: int, counted: int,
                today: str) -> None:
    """把 release 资产累计下载写进 p0_downloads 的 fn:github 条目(保留上次值供月差分)。"""
    key = f"{fn}:github"
    old = state_items.get(key) or {}
    prev_total, prev_at = old.get("downloads_total"), old.get("fetched_at")
    if prev_at == today:                    # 同日重跑不覆盖 prev
        prev_total, prev_at = old.get("prev_total"), old.get("prev_at")
    state_items[key] = {"package": "release-assets", "ecosystem": "github",
                        "downloads_total": total, "releases_counted": counted,
                        "prev_total": prev_total, "prev_at": prev_at,
                        "fetched_at": today,
                        "fetched_at_iso": datetime.now(timezone.utc).isoformat()}


def cmd_maintenance(cards, limit=None, force=False):
    path = STATE / "p0_maintenance.json"
    state = load_json(path, {"items": {}})
    today = st.utc_day()
    pool = {r["full_name"]: r for r in st.load_pool().values()}
    todo = []
    for fn in cards:
        it = state["items"].get(fn)
        fresh = it and not force and (
            it.get("fetched_at") == today or
            _fresh_within(it.get("fetched_at_iso"), MAINT_FRESH_DAYS))
        if not fresh:
            todo.append(fn)
    if limit:
        todo = todo[:limit]
    print(f"maintenance: 待取 {len(todo)}"
          f"(缓存新鲜 {len(cards) - len(todo)})")
    dl_path = STATE / "p0_downloads.json"
    dl_state = load_json(dl_path, {"items": {}})
    done = err = 0
    t0 = time.time()
    for i, fn in enumerate(todo):
        try:
            facts = fetch_maint_one(fn)
        except (gh.BudgetOut, gh.CoreReserveOut, gh.QuotaPatienceOut):
            print("  [budget] 预算到,收尾(进度已落盘)")
            break
        except Exception as e:                      # noqa: BLE001 单仓失败不挡批
            err += 1
            state["items"][fn] = {"error": str(e)[:120],
                                  "fetched_at": today,
                                  "fetched_at_iso": datetime.now(
                                      timezone.utc).isoformat()}
        else:
            rec = pool.get(fn, {})
            state["items"][fn] = {**facts,
                                  "pushed_days": _days(rec.get("pushed_at")),
                                  "archived": bool(rec.get("archived")),
                                  "status": maint_enum(facts, rec),
                                  "fetched_at": today,
                                  "fetched_at_iso": datetime.now(
                                      timezone.utc).isoformat()}
            # 同响应捎带:资产累计下载合入 p0_downloads(fn:github)
            _merge_gh_dl(dl_state["items"], fn,
                         facts["asset_downloads_total"],
                         facts["releases_counted"], today)
            done += 1
        if (i + 1) % CHUNK_SAVE == 0:
            st.atomic_write_json(path, state)
            st.atomic_write_json(dl_path, dl_state)
            print(f"  ... {i + 1}/{len(todo)} ({time.time() - t0:.0f}s,"
                  f"err {err})", flush=True)
    st.atomic_write_json(path, state)
    st.atomic_write_json(dl_path, dl_state)
    dist = {}
    for v in state["items"].values():
        dist[v.get("status") or "null"] = dist.get(v.get("status") or "null", 0) + 1
    print(f"maintenance: 新取 {done},失败 {err},分布 {dist}")


def cmd_dl_github(cards, limit=None, force=False):
    """一次性回填:每仓调一次 /releases 抽资产累计下载(fn:github 条目)。

    之后由 cmd_maintenance 月更捎带刷新,无需单独再跑。
    """
    path = STATE / "p0_downloads.json"
    state = load_json(path, {"items": {}})
    today = st.utc_day()
    todo = []
    for fn in cards:
        it = state["items"].get(f"{fn}:github")
        fresh = it and not force and (
            it.get("fetched_at") == today or
            _fresh_within(it.get("fetched_at_iso"), MAINT_FRESH_DAYS))
        if not fresh:
            todo.append(fn)
    if limit:
        todo = todo[:limit]
    print(f"dl-github: 待取 {len(todo)}(缓存新鲜 {len(cards) - len(todo)})")
    ok = err = has_assets = 0
    t0 = time.time()
    for i, fn in enumerate(todo):
        try:
            gh.CORE_PACE.slot()
            _, rels = gh.api_get(f"/repos/{fn}/releases", {"per_page": 100})
        except (gh.BudgetOut, gh.CoreReserveOut, gh.QuotaPatienceOut):
            print("  [budget] 预算到,收尾(进度已落盘)")
            break
        except Exception as e:                      # noqa: BLE001 单仓失败不挡批
            err += 1
            print(f"  {fn}: {str(e)[:80]}")
            continue
        total = sum(a.get("download_count") or 0
                    for r in rels for a in (r.get("assets") or []))
        if total:
            has_assets += 1
        _merge_gh_dl(state["items"], fn, total, len(rels), today)
        ok += 1
        if (i + 1) % CHUNK_SAVE == 0:
            st.atomic_write_json(path, state)
            print(f"  ... {i + 1}/{len(todo)} ({time.time() - t0:.0f}s,"
                  f"有资产 {has_assets},err {err})", flush=True)
    st.atomic_write_json(path, state)
    print(f"dl-github: 成功 {ok},其中带资产下载 {has_assets},失败 {err}")
    top = sorted((v for v in state["items"].values()
                  if v.get("ecosystem") == "github"
                  and v.get("downloads_total")),
                 key=lambda v: -v["downloads_total"])[:5]
    for v in top:
        print(f"  github/{v['package']}: 累计 {v['downloads_total']:,}"
              f"({v['releases_counted']} releases)")


# ---------------- 包下载量(PyPI/npm 免费 API,月更) ----------------

PIP_RE = re.compile(r"pip3? install\s+(?:-\S+\s+)*([A-Za-z0-9][A-Za-z0-9._-]*)")
NPM_RE = re.compile(r"(?<![A-Za-z])npm\s+(?:i|install)\s+(?:-\S+\s+)*"
                    r"(@[A-Za-z0-9._-]+/[A-Za-z0-9._-]+|[A-Za-z0-9][A-Za-z0-9._-]*)"
                    r"|(?<![A-Za-z])npx\s+(@?[A-Za-z0-9][A-Za-z0-9._@/-]*)")
NPM_SKIP = {"-g", "--global"}
PKG_BLOCK = {"pip", "pip3", "setuptools", "wheel", "npm", "npx", "node",
             "python", "poetry", "uv", "pnpm", "yarn", "bun",
             "requirements.txt"}   # 包管理器自身/样板话,非项目包


def _norm_pkg(s):
    return s.lower().replace("_", "-").rstrip(".")


def pick_packages(card):
    """README 原文 → {ecosystem: package}。只认明写的安装命令,null 纪律。
    主源是 README 全文(s8 证据引文只覆盖提名词命中的行,会漏 npx 等);
    README 文件缺失时退回裁决引文。同一 README 多条安装命令时,
    优先取与仓库同名的包(防 pytest 等开发依赖冒名),否则取第一条。"""
    fn = card.get("fn") or ""
    repo_name = _norm_pkg(fn.split("/")[-1])
    p = st.READMES / (fn.replace("/", "__") + ".md")
    quotes = []
    for v in (card.get("raw_verdicts", {}) or {}).get("install", []):
        quotes.extend(v.get("quotes") or [])
    text = ""
    if p.exists():
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            pass
    sources = ([text] if text else []) + quotes
    got, cands = {}, {"pypi": [], "npm": []}
    for q in sources:
        for m in PIP_RE.finditer(q):
            pkg = m.group(1).rstrip(".")
            if pkg not in PKG_BLOCK and pkg not in cands["pypi"]:
                cands["pypi"].append(pkg)
        for m in NPM_RE.finditer(q):
            pkg = (m.group(1) or m.group(2) or "").rstrip(".")
            if pkg and pkg not in PKG_BLOCK and pkg not in cands["npm"]:
                cands["npm"].append(pkg)
    for eco, lst in cands.items():
        for pkg in lst:
            if _norm_pkg(pkg) == repo_name:
                got[eco] = pkg
                break
        else:
            if lst:
                got[eco] = lst[0]
    return got


def _fetch_url(url):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "ai_collect"})
    opener = gh.OPENER
    for attempt in range(2):
        try:
            with opener.open(req, timeout=20) as r:
                return json.loads(r.read())
        except Exception:                           # noqa: BLE001
            if attempt:
                return None
            opener = urllib.request.build_opener(
                urllib.request.ProxyHandler({}))     # 直连重试一次
    return None


def fetch_downloads_one(ecosystem, pkg):
    if ecosystem == "pypi":
        d = _fetch_url(f"https://pypistats.org/api/packages/{pkg}/recent")
        if d and d.get("data", {}).get("last_month") is not None:
            return {"downloads_month": d["data"]["last_month"]}
        return None                                  # 404=未发布/私有名
    d = _fetch_url("https://api.npmjs.org/downloads/point/last-month/"
                   + pkg.replace("/", "%2F"))
    if d and d.get("downloads") is not None:
        return {"downloads_month": d["downloads"]}
    return None


def cmd_downloads(cards, limit=None, force=False):
    path = STATE / "p0_downloads.json"
    state = load_json(path, {"items": {}})
    today = st.utc_day()
    want = {}
    for fn, card in cards.items():
        for eco, pkg in pick_packages(card).items():
            it = state["items"].get(f"{fn}:{eco}")
            if force or not it or \
                    not _fresh_within(it.get("fetched_at_iso"), DL_FRESH_DAYS):
                want[(fn, eco)] = pkg
    todo = list(want.items())
    if limit:
        todo = todo[:limit]
    print(f"downloads: 候选包 {sum(len(pick_packages(c)) for c in cards.values())},"
          f"待取 {len(todo)}")
    ok = miss = 0
    for i, ((fn, eco), pkg) in enumerate(todo):
        r = fetch_downloads_one(eco, pkg)
        key = f"{fn}:{eco}"
        if r:
            state["items"][key] = {**r, "package": pkg, "ecosystem": eco,
                                   "fetched_at": today,
                                   "fetched_at_iso": datetime.now(
                                       timezone.utc).isoformat()}
            ok += 1
        else:
            state["items"][key] = {"package": pkg, "ecosystem": eco,
                                   "downloads_month": None,
                                   "note": "not_found_or_unreachable",
                                   "fetched_at": today,
                                   "fetched_at_iso": datetime.now(
                                       timezone.utc).isoformat()}
            miss += 1
        time.sleep(0.5)                              # 免费接口留余地
        if (i + 1) % CHUNK_SAVE == 0:
            st.atomic_write_json(path, state)
            print(f"  ... {i + 1}/{len(todo)}", flush=True)
    st.atomic_write_json(path, state)
    top = sorted((v for v in state["items"].values()
                  if v.get("downloads_month")),
                 key=lambda v: -v["downloads_month"])[:5]
    print(f"downloads: 成功 {ok},未找到/失败 {miss}")
    for v in top:
        print(f"  {v['ecosystem']}/{v['package']}: {v['downloads_month']:,}/月")


# ---------------- demo 导出 ----------------

DEMO_FNS = ["morluto/rea", "n8n-io/n8n", "openclaw/openclaw"]


def cmd_export_demo():
    cards = load_done_cards()
    maint = load_json(STATE / "p0_maintenance.json", {"items": {}})["items"]
    velo = load_json(STATE / "p0_velocity.json", {"items": {}})["items"]
    dls = load_json(STATE / "p0_downloads.json", {"items": {}})["items"]
    plat = load_json(STATE / "p0_platform.json", {"items": {}})["items"]
    pool = {r["full_name"]: r for r in st.load_pool().values()}
    rows = []
    for fn in sorted(DEMO_FNS):
        c, m = cards[fn], pool[fn]
        row = {
            "fn": fn, "card_sha": c["sha"],
            "card_at": c["trust"]["generated_at"],
            "meta": {k: m.get(k) for k in
                     ["owner_type", "stars", "forks", "language", "license",
                      "topics", "archived", "created_at", "pushed_at",
                      "homepage", "html_url"]},
            "identity": c["identity"], "filters": c["filters"],
            "eval": c["eval"], "links": c["links"], "intel": c["intel"],
            "signals": {
                "maintenance": {k: maint.get(fn, {}).get(k) for k in
                                ["status", "pushed_days", "last_release_days",
                                 "releases_per_year", "contributors",
                                 "issue_close_days_med"]},
                "velocity": velo.get(fn),
                "downloads": next((dls[k] for k in (f"{fn}:pypi", f"{fn}:npm")
                                   if dls.get(k, {}).get("downloads_month")),
                                  (dls.get(f"{fn}:pypi") or
                                   dls.get(f"{fn}:npm"))),
                "platform": plat.get(fn),
            },
            "trust": {k: c["trust"][k] for k in
                      ["confidence", "evidence", "ver", "prompt_ver",
                       "generated_at"]},
        }
        rows.append(row)
    out = Path("demo_public_repo/data/catalog.jsonl")
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False,
                                        separators=(",", ":")) for r in rows)
                   + "\n", encoding="utf-8")
    print(f"export-demo: {len(rows)} 行 → {out}")


def main():
    u()
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="maintenance,velocity,downloads,platform",
                    help="逗号分隔:maintenance,velocity,downloads,platform,export-demo")
    ap.add_argument("--force", action="store_true", help="忽略新鲜度缓存")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    only = set(args.only.split(","))
    cards = load_done_cards()
    print(f"A 层卡片: {len(cards)} 仓")
    if "velocity" in only:
        cmd_velocity(cards)
    if "platform" in only:
        cmd_platform(cards, args.limit)
    if "downloads" in only:
        cmd_downloads(cards, args.limit, args.force)
    if "dl-github" in only:
        gh.set_budget(gh.Budget(max_minutes=55, reserve_remaining=300))
        try:
            cmd_dl_github(cards, args.limit, args.force)
        except (gh.BudgetOut, gh.CoreReserveOut, gh.QuotaPatienceOut) as e:
            print(f"[budget] {e}(进度已落盘,重跑续取)")
    if "maintenance" in only:
        gh.set_budget(gh.Budget(max_minutes=55, reserve_remaining=300))
        try:
            cmd_maintenance(cards, args.limit, args.force)
        except (gh.BudgetOut, gh.CoreReserveOut, gh.QuotaPatienceOut) as e:
            print(f"[budget] {e}(进度已落盘,重跑续取)")
    if "export-demo" in only:
        cmd_export_demo()


if __name__ == "__main__":
    main()
