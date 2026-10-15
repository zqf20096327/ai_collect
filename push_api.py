# -*- coding: utf-8 -*-
"""push_api · 走 GitHub REST API 推送(git 通道被掐时的兜底)。

blobs → tree → commit → (创建/更新)ref,单 commit 完整推送 git 索引内容。
传输用 curl 子进程:本机 Python TLS 被指纹掐断时 curl 稳定(实测 5/5),
git/urllib 都不通的窗口用它照样能推。

用法:python push_api.py "commit message"
"""
import base64
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import lib_gh as gh  # noqa: E402

gh._stdout_utf8()

REPO = "zqf20096327/ai_collect"


def _token():
    return gh.TOKEN or subprocess.run(["gh", "auth", "token"],
                                      capture_output=True,
                                      text=True).stdout.strip()


def curl_json(method, url, payload=None, retries=8):
    """curl 传输 + 限流感知重试。返回 (status, json_or_None)。"""
    hdrs = ["-H", "Accept: application/vnd.github+json",
            "-H", "User-Agent: ai_collect",
            "-H", f"Authorization: Bearer {_token()}"]
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        hdrs += ["-H", "Content-Type: application/json"]
    cmd = (["curl", "-sS", "-X", method, "--connect-timeout", "15",
            "--max-time", "60", "-D", "-", *hdrs, url]
           + (["--data-binary", "@-"] if data else []))
    for attempt in range(retries):
        r = subprocess.run(cmd, input=data, capture_output=True, timeout=80)
        out = r.stdout
        if not out and r.returncode != 0:
            print(f"  [curl] rc={r.returncode} {r.stderr.decode()[:80]} "
                  f"重试 {attempt + 1}/{retries}", flush=True)
            time.sleep(3 * (attempt + 1))
            continue
        head, _, body = out.partition(b"\r\n\r\n")
        status = int(head.split(b" ")[1]) if head.startswith(b"HTTP/") else 0
        hmap = {}
        for line in head.split(b"\r\n")[1:]:
            if b":" in line:
                k, v = line.split(b":", 1)
                hmap[k.decode().strip().lower()] = v.decode().strip()
        if status in (403, 429):
            if hmap.get("x-ratelimit-remaining") == "0":
                reset = int(hmap.get("x-ratelimit-reset", time.time() + 60))
                w = max(reset - int(time.time()) + 2, 2)
                print(f"  [rate-limit] sleep {int(w)}s", flush=True)
                time.sleep(min(w, 3600))
                continue
        if status >= 500:
            time.sleep(3 * (attempt + 1))
            continue
        try:
            return status, json.loads(body) if body.strip() else None
        except json.JSONDecodeError:
            print(f"  [curl] 非 JSON 响应重试(status={status})", flush=True)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"curl_json 多次失败: {method} {url}")


def main():
    msg = sys.argv[1] if len(sys.argv) > 1 else "push via api"
    r = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                       text=True)
    files = [f for f in r.stdout.splitlines() if f.strip()]
    if not files:
        raise SystemExit("git 索引为空,先 git add")
    print(f"待推 {len(files)} 个文件")

    # 空仓库兼容:git/blobs API 409 on empty repo → contents API 播种初始提交
    status, commits = curl_json(
        "GET", f"https://api.github.com/repos/{REPO}/commits?per_page=1")
    parents = []
    if status == 409 or (status == 200 and not commits):
        b64 = base64.b64encode((ROOT / ".gitignore").read_bytes()).decode()
        status, put = curl_json(
            "PUT",
            f"https://api.github.com/repos/{REPO}/contents/.gitignore",
            {"message": "bootstrap", "content": b64, "branch": "main"})
        if status not in (200, 201):
            raise SystemExit(f"播种失败: {status} {put}")
        parents = [put["commit"]["sha"]]
        print(f"空仓库已播种初始提交 {parents[0][:10]}")
    elif status == 200:
        parents = [commits[0]["sha"]]
        print(f"基于远端 head {parents[0][:10]} 快进")

    entries = []
    for i, f in enumerate(files, 1):
        raw = (ROOT / f).read_bytes()
        status, blob = curl_json(
            "POST", f"https://api.github.com/repos/{REPO}/git/blobs",
            {"content": base64.b64encode(raw).decode(), "encoding": "base64"})
        if status != 201:
            raise SystemExit(f"blob 失败 {f}: {status} {blob}")
        entries.append({"path": f.replace("\\", "/"), "mode": "100644",
                        "type": "blob", "sha": blob["sha"]})
        if i % 10 == 0 or i == len(files):
            print(f"  blob {i}/{len(files)}", flush=True)

    status, tree = curl_json(
        "POST", f"https://api.github.com/repos/{REPO}/git/trees",
        {"tree": entries})
    if status != 201:
        raise SystemExit(f"tree 失败: {status} {tree}")
    status, commit = curl_json(
        "POST", f"https://api.github.com/repos/{REPO}/git/commits",
        {"message": msg, "tree": tree["sha"], "parents": parents})
    if status != 201:
        raise SystemExit(f"commit 失败: {status} {commit}")

    status, ref = curl_json(
        "PATCH", f"https://api.github.com/repos/{REPO}/git/refs/heads/main",
        {"sha": commit["sha"], "force": False})
    if status != 200:
        raise SystemExit(f"ref 快进失败: {status} {ref}")
    print(f"完成: {commit['sha'][:10]} {msg}")


if __name__ == "__main__":
    main()
