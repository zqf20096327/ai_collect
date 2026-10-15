# -*- coding: utf-8 -*-
"""check · 配置一致性校验(改完 config 先跑这个)。

  python check_strategy.py             # 离线校验
  python check_strategy.py --online    # 附带联网核验 org/watch 是否存在
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
import lib_gh as gh  # noqa: E402
import lib_store as st  # noqa: E402

gh._stdout_utf8()

errors, warns = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def offline():
    print(f"== 离线校验 ==")
    if not config.TOPICS:
        err("TOPICS 为空")
    dup = {t for t in config.TOPICS if config.TOPICS.count(t) > 1}
    if dup:
        err(f"TOPICS 重复: {dup}")
    bad = [t for t in config.TOPICS
           if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", t)]
    if bad:
        err(f"TOPICS 命名不合规(小写字母数字连字符): {bad}")

    all_orgs = config.ORG_DEDICATED + config.ORG_SUPERSET
    dupo = {o for o in all_orgs if all_orgs.count(o) > 1}
    if dupo:
        err(f"ORG 重复: {dupo}")
    both = set(config.ORG_DEDICATED) & set(config.ORG_SUPERSET)
    if both:
        err(f"ORG 同名出现在 dedicated 与 superset: {both}")

    for w in config.WATCH:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", w):
            err(f"WATCH 条目格式错误: {w}")
        if w in config.EXCLUDE_REPOS:
            err(f"WATCH 与仓库黑名单互斥冲突: {w}")
    dupw = {w for w in config.WATCH if config.WATCH.count(w) > 1}
    if dupw:
        err(f"WATCH 重复: {dupw}")

    for r in config.EXCLUDE_REPOS:
        if "/" not in r:
            err(f"EXCLUDE_REPOS 必须是 owner/repo 形式: {r}")
    if set(config.EXCLUDE_USERS) & {w.split("/")[0] for w in config.WATCH}:
        err("EXCLUDE_USERS 与 WATCH 所有者冲突(白名单会被黑名单吞掉)")

    if config.N_SHARDS < 1:
        err("N_SHARDS 必须 >= 1")
    if not (1 <= config.STAR_MIN <= 10000):
        warn(f"STAR_MIN={config.STAR_MIN} 不在常规区间")
    if not (30 <= config.PUSHED_DAYS <= 730):
        warn(f"PUSHED_DAYS={config.PUSHED_DAYS} 不在常规区间")

    for p in sorted(st.LIVE.glob("pool_shard_*.ndjson")):
        mb = p.stat().st_size / 1e6
        if mb > config.SHARD_MAX_MB:
            err(f"{p.name} {mb:.1f}MB 超过单文件红线 {config.SHARD_MAX_MB}MB")

    print(f"TOPICS={len(config.TOPICS)} ORG(dedicated)="
          f"{len(config.ORG_DEDICATED)} ORG(superset)="
          f"{len(config.ORG_SUPERSET)} WATCH={len(config.WATCH)} "
          f"EXCLUDE(users/repos)={len(config.EXCLUDE_USERS)}/"
          f"{len(config.EXCLUDE_REPOS)} N_SHARDS={config.N_SHARDS}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--online", action="store_true")
    args = ap.parse_args()
    offline()

    if args.online:
        import urllib.error

        def is_404(e):
            return isinstance(e, urllib.error.HTTPError) and e.code == 404

        for o in config.ORG_DEDICATED + config.ORG_SUPERSET:
            try:
                _, data = gh.api_get(f"/orgs/{o}", retries=2)
                print(f"  OK   org {o} (repos={data.get('public_repos')})")
            except urllib.error.HTTPError as e:
                (err if e.code == 404 else warn)(f"org {o}: HTTP {e.code}")
            except Exception as e:
                warn(f"org {o} 探测失败(网络?): {e}")
        for w in config.WATCH:
            try:
                _, data = gh.api_get(f"/repos/{w}", retries=2)
                print(f"  OK   watch {w} (stars={data.get('stargazers_count')})")
            except urllib.error.HTTPError as e:
                (err if e.code == 404 else warn)(f"watch {w}: HTTP {e.code}")
            except Exception as e:
                warn(f"watch {w} 探测失败: {e}")

    print()
    for w in warns:
        print(f"[warn] {w}")
    if errors:
        for e in errors:
            print(f"[FAIL] {e}")
        raise SystemExit(1)
    print("校验通过 ✓")


if __name__ == "__main__":
    main()
