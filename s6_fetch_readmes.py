# -*- coding: utf-8 -*-
"""s6 · README 增量抓取(ETag)。

池内仓按星数降序逐个抓 README:
  - 无缓存 → 抓
  - 有 ETag → If-None-Match,304 零成本跳过
  - 超 README_MAX_BYTES 截断
  - 出池仓的 README/ETag 由 --gc 清理(默认预览)

用法:
  python s6_fetch_readmes.py                  # 全池
  python s6_fetch_readmes.py --limit 50       # 星数最高的 50 个(抽样)
  python s6_fetch_readmes.py --only owner/repo[,owner/repo]
  python s6_fetch_readmes.py --gc             # 预览出池残留; --gc --apply 真删
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402

gh._stdout_utf8()

ETAG_FILE = st.STATE / "readme_etags.json"


def load_etags():
    if ETAG_FILE.exists():
        return json.loads(ETAG_FILE.read_text(encoding="utf-8"))
    return {}


def save_etags(etags):
    st._atomic_write(ETAG_FILE, json.dumps(etags, ensure_ascii=False))


def readme_path(full_name):
    return st.READMES / (full_name.replace("/", "__") + ".md")


def fetch_one(full_name, etag):
    hdrs = {"Accept": "application/vnd.github.raw+json"}
    if etag:
        hdrs["If-None-Match"] = etag
    h, body = gh.api_get(f"/repos/{full_name}/readme", extra_headers=hdrs,
                         want="raw")
    if body is None:          # 304
        return "not_modified", etag
    if len(body) > config.README_MAX_BYTES:
        body = body[:config.README_MAX_BYTES]
    readme_path(full_name).write_bytes(body)
    return "fetched", h.get("ETag")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only", help="owner/repo[,owner/repo2]")
    ap.add_argument("--new-only", action="store_true",
                    help="只抓无 ETag 缓存的仓(新入池;Actions 每晚增量用)")
    ap.add_argument("--gc", action="store_true", help="清理出池仓的 README/ETag")
    ap.add_argument("--apply", action="store_true", help="配合 --gc 真删")
    args = ap.parse_args()

    pool = st.load_pool()
    if not pool:
        raise SystemExit("池为空,先跑 s5_merge_pool.py")

    if args.gc:
        live = {r["full_name"] for r in pool.values()}
        etags = load_etags()
        stale = [(readme_path(fn), fn) for fn in etags if fn not in live]
        stale += [(p, p.stem.replace("__", "/")) for p in st.READMES.glob("*.md")
                  if p.stem.replace("__", "/") not in live]
        print(f"出池残留 README {len(stale)} 个"
              + ("" if args.apply else "(预览,--apply 真删)"))
        if args.apply:
            for p, fn in set(stale):
                p.unlink(missing_ok=True)
                etags.pop(fn, None)
            save_etags(etags)
        return

    recs = sorted(pool.values(), key=lambda r: -r.get("stars", 0))
    if args.only:
        want = {s.strip() for s in args.only.split(",")}
        recs = [r for r in recs if r["full_name"] in want]
    if args.new_only:
        cached = load_etags()
        recs = [r for r in recs if r["full_name"] not in cached]
    if args.limit:
        recs = recs[:args.limit]

    etags = load_etags()
    n_fetch = n_304 = n_miss = 0
    print(f"== s6 README | 目标 {len(recs)} 仓 ==")
    for i, rec in enumerate(recs, 1):
        fn = rec["full_name"]
        try:
            status, etag = fetch_one(fn, etags.get(fn))
        except Exception as e:
            n_miss += 1
            print(f"  [{i}/{len(recs)}] {fn}: MISS {e}")
            continue
        if status == "fetched":
            n_fetch += 1
            if etag:
                etags[fn] = etag
            mark = "fetch"
        else:
            n_304 += 1
            mark = "304"
        if i % 20 == 0 or status == "fetched" and rec.get("stars", 0) > 1000:
            print(f"  [{i}/{len(recs)}] {fn} {mark} "
                  f"(stars={rec.get('stars')})", flush=True)
    save_etags(etags)
    print(f"完成: 抓取 {n_fetch} · 304跳过 {n_304} · 失败 {n_miss}")


if __name__ == "__main__":
    main()
