# -*- coding: utf-8 -*-
"""富集状态 JSON 的按 key 并集合并(rebase 冲突解决 + 旧数据修复)。

背景(2026-10-16 事故):同日两窗背靠背,后窗在 concurrency 队列里锁定
创建时刻的旧 SHA,开跑拿不到前窗刚推的 state;push 时 rebase 撞出
add/add,原策略整文件取本窗(--theirs)把前窗 843 仓的台账
(enrich_state.json)和信号侧车(enrich_cache_shards/)全部顶掉。

合并语义(两侧数据只追加不丢):
  enrich_state.json            items 按 fn 并集;dims 每维取更新 ts;
                               fail_count 取大;pushed_checked 取新
  enrich_cache_shards/<xx>.json 按 fn 并集;每维度取 dim_ts 更新一侧,
                               该维度信号字段整体随之(不残留被淘汰侧旧值)
  平手(同日两窗):冲突模式取 theirs(rebase 语义下=本窗,同日更晚);
                  修复旧数据用 --tie ours 保住现值、只补缺

rebase 冲突时的 stage 语义(与普通 merge 相反)::2=ours=origin/main
(前窗已推),:3=theirs=本窗正在重放的提交。

用法:
  冲突路径模式(workflow 调用;读 index 三方版本,写回并 git add):
    python tools/merge_state_json.py --path state/enrich_cache_shards/00.json
  文件模式(修复/校验;OURS=现值,THEIRS=待并入,OUT 可与 OURS 同路径):
    python tools/merge_state_json.py OURS.json THEIRS.json OUT.json [--tie ours|theirs]

退出码:0=合并成功 3=路径/形状不归本工具管(调用方回退 --theirs) 其他=异常
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

DIMS = ("commit", "release", "security", "contrib", "lang")
DIM_FIELDS = {  # 维度 -> 侧车信号字段(collect_dims 按维成组写)
    "commit": ("commit_7d", "commit_90d"),
    "release": ("rel_ver", "rel_pub", "rel_days", "rel_n90", "rel_pre",
                "rel_none"),
    "security": ("sec_n", "sec_worst", "sec_last", "sec_ids"),
    "contrib": ("contrib_n",),
    "lang": ("lang",),
}


def _pick(ours, theirs, tie):
    return theirs if tie == "theirs" else ours


def _merge_sig_entry(ours: dict, theirs: dict, tie: str) -> dict:
    """侧车单仓条目:逐维取 dim_ts 更新一侧,维度字段整体随之。"""
    if not isinstance(ours.get("dim_ts"), dict) \
            or not isinstance(theirs.get("dim_ts"), dict):
        out = dict(_pick(ours, theirs, tie))
        for k, v in _pick(theirs, ours, tie).items():
            out.setdefault(k, v)          # 无 dim_ts 的旧形状:退化为浅合并
        return out
    out: dict = {}
    dts: dict = {}
    for d in DIMS:
        a, b = ours["dim_ts"].get(d) or "", theirs["dim_ts"].get(d) or ""
        if not a and not b:
            continue
        if b > a:
            src, ts = theirs, b
        elif a > b:
            src, ts = ours, a
        else:
            src, ts = _pick(ours, theirs, tie), a
        dts[d] = ts
        for f in DIM_FIELDS[d]:
            if f in src:                  # 本侧该维没写出=本次无值,不留旧
                out[f] = src[f]
    out["enriched_at"] = max(ours.get("enriched_at") or "",
                             theirs.get("enriched_at") or "") or None
    out["dim_ts"] = dts
    return out


def _merge_state_item(ours: dict, theirs: dict, tie: str) -> dict:
    """台账单仓条目(enrich_state.items[fn])。"""
    out = dict(_pick(ours, theirs, tie))
    for k, v in _pick(theirs, ours, tie).items():
        out.setdefault(k, v)
    od, td = ours.get("dims") or {}, theirs.get("dims") or {}
    dims = {}
    for d in set(od) | set(td):
        a, b = od.get(d) or "", td.get(d) or ""
        dims[d] = b if b > a else a if a > b else _pick(a, b, tie)
    if dims:
        out["dims"] = dims
    if "fail_count" in out:
        out["fail_count"] = max(ours.get("fail_count", 0),
                                theirs.get("fail_count", 0))
    pc = max(ours.get("pushed_checked") or "",
             theirs.get("pushed_checked") or "")
    if pc:
        out["pushed_checked"] = pc
    return out


def merge_state_docs(ours, theirs, tie: str):
    """顶层文档:enrich_state 形状(items)或侧车形状(fn→信号)分派。"""
    if not isinstance(ours, dict) or not isinstance(theirs, dict):
        return _pick(ours, theirs, tie)
    if isinstance(ours.get("items"), dict) \
            and isinstance(theirs.get("items"), dict):
        out = dict(_pick(ours, theirs, tie))
        for k, v in _pick(theirs, ours, tie).items():
            if k != "items":
                out.setdefault(k, v)
        items = dict(ours["items"])
        for fn, tv in theirs["items"].items():
            items[fn] = _merge_state_item(items[fn], tv, tie) \
                if fn in items else tv
        out["items"] = items
        return out
    out = dict(ours)
    for k, tv in theirs.items():
        ov = out.get(k)
        out[k] = _merge_sig_entry(ov, tv, tie) \
            if isinstance(ov, dict) and isinstance(tv, dict) else tv
    return out


# ---------------- 文件模式 ----------------

def _dump(path: str, doc) -> None:
    # 与生产写入格式一致:enrich_state 紧凑+尾换行,侧车 indent=1
    if Path(path).name == "enrich_state.json":
        text = json.dumps(doc, ensure_ascii=False) + "\n"
    else:
        text = json.dumps(doc, ensure_ascii=False, indent=1)
    Path(path).write_text(text, encoding="utf-8", newline="\n")


def file_mode(ours_path, theirs_path, out_path, tie) -> int:
    ours = json.loads(Path(ours_path).read_text(encoding="utf-8"))
    theirs = json.loads(Path(theirs_path).read_text(encoding="utf-8"))
    _dump(out_path, merge_state_docs(ours, theirs, tie))
    return 0


# ---------------- 冲突路径模式 ----------------

def _stage(stage: str, path: str):
    r = subprocess.run(["git", "show", f"{stage}:{path}"],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def conflict_mode(path: str, tie: str) -> int:
    ours = _stage(":2", path)     # rebase 语义::2 = origin/main(前窗)
    theirs = _stage(":3", path)   # :3 = 本窗提交
    if ours is None and theirs is None:
        return 3
    merged = theirs if ours is None else ours if theirs is None \
        else merge_state_docs(ours, theirs, tie)
    _dump(path, merged)
    r = subprocess.run(["git", "add", "--", path])
    return r.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--path", help="rebase 冲突路径(读 index 三方版本)")
    ap.add_argument("--tie", choices=["ours", "theirs"], default="theirs",
                    help="同日平手取哪侧(默认 theirs=本窗更晚)")
    ap.add_argument("files", nargs="*", help="OURS THEIRS OUT 文件模式")
    args = ap.parse_args()
    if args.path:
        return conflict_mode(args.path, args.tie)
    if len(args.files) == 3:
        return file_mode(*args.files, tie=args.tie)
    ap.error("需 --path 或三个文件参数")
    return 2


if __name__ == "__main__":
    sys.exit(main())
