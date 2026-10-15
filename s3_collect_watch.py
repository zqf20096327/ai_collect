# -*- coding: utf-8 -*-
"""s3 · watch 白名单保送。

点名仓库直接入池:官方不打 topic 的仓 + 曾误杀保险。
白名单不设星线/活跃线(fork/archived 状态照实记录,不因此拒收)。

用法:
  python s3_collect_watch.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402

gh._stdout_utf8()


def main():
    print(f"== s3 watch 白名单 | {len(config.WATCH)} 个仓 ==")
    records = []
    for full in config.WATCH:
        if full in config.EXCLUDE_REPOS:
            print(f"  [skip] {full} 在黑名单里(黑白名单互斥,检查配置)")
            continue
        try:
            _, it = gh.api_get(f"/repos/{full}")
        except Exception as e:
            print(f"  [miss] {full}: {e}")
            continue
        if it.get("owner", {}).get("login") in config.EXCLUDE_USERS:
            print(f"  [skip] {full} 所有者在用户黑名单里")
            continue
        rec = st.slim(it, "watch")
        records.append(rec)
        flag = "archived" if it.get("archived") else "ok"
        print(f"  {full}: stars={rec['stars']} [{flag}]")
    st.write_part("watch", records)
    print(f"-> {len(records)} 条写入 data/parts/watch.json")


if __name__ == "__main__":
    main()
