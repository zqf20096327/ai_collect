# deepseek-pojia — dsh-purge 一键安装版

DeepSeek Harness（dsh）的**破甲 / 红队评测插件**，本仓库 = 一个可直接 `git clone` 就能装上的 dsh-purge（1.1.71，已冻结自动更新），外加**一条命令的安装器**。

- 当前版本：**[v1.1.71](https://github.com/tiancaixiexiong1997/deepseek-pojia/releases/tag/v1.1.71)**（钉 tag 安装可复现；`main` 跟最新提交）
- 上游：[YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge)（MIT，作者已暂停更新，故本仓库自持一份可复现的版本，署名见 [NOTICE-UPSTREAM.md](NOTICE-UPSTREAM.md)）
- 目标宿主：DeepSeek Harness **0.2.x**（桌面端 EXE 与官方 `dsh web` 都支持）
- 平台：macOS / Linux / Windows

---

## 一条命令安装

**钉版本（推荐，智能体 / 批量部署用这个）** —— 不受 `main` 变动影响，当前 `v1.1.71`：

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/tiancaixiexiong1997/deepseek-pojia/v1.1.71/install.sh | POJIA_REF=v1.1.71 bash

# GitHub raw 的 CDN 偶发滞后（改了脚本几分钟内还是旧的），走镜像：
curl -fsSL https://cdn.jsdelivr.net/gh/tiancaixiexiong1997/deepseek-pojia@v1.1.71/install.sh | POJIA_REF=v1.1.71 bash
```

```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -Command "iwr https://github.com/tiancaixiexiong1997/deepseek-pojia/archive/refs/tags/v1.1.71.zip -OutFile $env:TEMP\pojia.zip; Expand-Archive $env:TEMP\pojia.zip $env:TEMP\pojia -Force; & \"$env:TEMP\pojia\deepseek-pojia-1.1.71\install.ps1\" -Ref v1.1.71"
```

**跟最新提交（`main`）** —— macOS / Linux：

```bash
git clone https://github.com/tiancaixiexiong1997/deepseek-pojia.git && cd deepseek-pojia && bash install.sh
```

Windows（PowerShell）：

```powershell
git clone https://github.com/tiancaixiexiong1997/deepseek-pojia.git; cd deepseek-pojia; powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

**没有 git 也行** —— 直接拉脚本跑（`install.sh` 会自己下 tarball 再装）：

```bash
curl -fsSL https://raw.githubusercontent.com/tiancaixiexiong1997/deepseek-pojia/main/install.sh | bash

# GitHub raw 的 CDN 偶发滞后（改了脚本几分钟内还是旧的），走镜像：
curl -fsSL https://cdn.jsdelivr.net/gh/tiancaixiexiong1997/deepseek-pojia@main/install.sh | bash
```

Windows 一条命令（自带 `curl.exe` / PowerShell）：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -Command "iwr https://github.com/tiancaixiexiong1997/deepseek-pojia/archive/refs/heads/main.zip -OutFile $env:TEMP\pojia.zip; Expand-Archive $env:TEMP\pojia.zip $env:TEMP\pojia -Force; & \"$env:TEMP\pojia\deepseek-pojia-main\install.ps1\""
```

装完**还要应用一次补丁**（这是宿主的设计，任何安装器都替代不了）：

1. 完全退出宿主（桌面端托盘右键 → 退出；`dsh web` 用 Ctrl-C 停）
2. 重新打开 → 会话标题旁点 **dsh-purge** → **清洗** → **应用**
3. 它会解包 `app.asar` 并自动重启；重启后**新开一轮对话**，注入才进当前会话

不想点按钮也行：安装时加 `--apply` / `-Apply`，会调 `lib/reapply-cli.js` 走同一条 headless 路径，然后你只要重启宿主：

```bash
bash install.sh --apply
```
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Apply
```

---

## 给智能体的安装指令（复制即用）

把下面整段发给本机智能体，让它自己装：

```text
安装 DeepSeek Harness 插件 dsh-purge（仓库 tiancaixiexiong1997/deepseek-pojia）。
只执行下面这些，不要全盘搜索、不要改其它文件、不要动宿主程序目录、不要重启宿主。

1) 定位 $DSH_HOME：$DSH_HOME 环境变量 → ~/.dsh → %APPDATA%\DeepSeek Harness\dsh-home
   → %LOCALAPPDATA%\DeepSeek Harness\dsh-home，取其中存在 profiles/<profile>/package.json 的那一份。
   两处都没有就停下来告诉用户：先启动一次 DeepSeek Harness，退出后再装。
2) 把仓库整个目录复制到 $DSH_HOME/plugins/dsh-purge（该目录已存在时先改名成 .bak-时间戳 备份）。
3) 运行：node $DSH_HOME/plugins/dsh-purge/scripts/link-profile.mjs --profile desktop
   （官方 Web 端用 --profile web；两者分开装、分开应用）
   它负责：写 profile 的 dependencies + bundles、清理不含 dsh-purge 的 pnpm-lock.yaml、缺提示词时放示例。
4) 运行：node $DSH_HOME/plugins/dsh-purge/bin/dsh-purge.js --status，把输出原样贴给用户。
5) 停止。最后的「应用」必须由用户在自己宿主的 dsh-purge → 清洗 里点，或在用户明确同意时
   才运行 node $DSH_HOME/plugins/dsh-purge/lib/reapply-cli.js。
依赖：Node.js >= 18（Windows 想不闪黑窗用 >= 22）。仓库里的 install.ps1 / install.sh 就是上面 2~4 步的封装。
```

---

## 安装器到底做了什么

`install.sh` / `install.ps1` 都是薄壳，实际逻辑只有一份：`scripts/link-profile.mjs`。它**只动 `$DSH_HOME`**：

| 步骤 | 内容 | 备注 |
|---|---|---|
| 1 | 仓库 → `$DSH_HOME/plugins/dsh-purge` | 旧目录自动 `.bak-时间戳` |
| 2 | `profiles/<profile>/package.json`：`dependencies["dsh-purge"] = "file:../../plugins/dsh-purge"` | 先备份，无 BOM 写回 |
| 3 | 同上：`dsh.profile.bundles` **末尾**追加 `dsh-purge` | 原有 bundle 一个不动 |
| 4 | `pnpm-lock.yaml` 里没有 `dsh-purge` 时备份 + 删除 | dsh 给 pnpm 带 `CI=1`（frozen-lockfile），不删锁装不进来 |
| 5 | 缺 `prompt-inject.md` 时放一份 `prompt-inject.example.md` | 已有提示词**永不覆盖** |

它**不**解包 `app.asar`、**不**点应用、**不**重启宿主（除非你显式加 `--apply`）。

常见参数：

```bash
bash install.sh --profile web          # 装到官方 Web 端那个 profile
bash install.sh --home /data/.dsh      # 便携版 / 自定义 DSH_HOME
bash install.sh --apply                # 装完直接洗
```

```powershell
.\install.ps1 -Profile web
.\install.ps1 -DshHome "D:\dsh-data\.dsh"
.\install.ps1 -Apply
```

---

## 验收

```bash
node "$DSH_HOME/plugins/dsh-purge/bin/dsh-purge.js" --status
```

- `补丁 x/y 已清洗, 0 待清洗` ← 关键是 **pending = 0**
- 会话标题旁有 **dsh-purge**，点开有「清洗 / 演练台」两页
- 新会话的系统提示词是你那份（默认面向国模「小码酱」），不是官方默认

## 版本矩阵（实测）

| 宿主 | 结果 | 说明 |
|---|---|---|
| `0.2.1-rc.5` | 桌面视图 66 项里 60 项已清洗，`pending=0` | 推荐，与作者验证过的版本一致 |
| `0.2.2-rc.2` | 全量 82 项：applied 48 / already 7 / skipped 15，`pattern_not_found = 0` | 能用；`#13 #14 #18 #35 #54 #56 #60 #62 #67 #74` 这 10 个审批/沙箱兜底补丁在 0.2.2 上找不到原文，退化成 skipped |

装了 0.2.2 后务必**让插件重新解包一次**（点一次应用即可，它按 `unpacked-asar.json` 里的 size/mtime 判定），否则官方升级会把 `app.asar` 重新封回去，补丁在 `resources/app` 里但不会被 Electron 加载 —— 表现就是「插件在、按钮能点、注入没效果」。

## 回滚

```bash
node "$DSH_HOME/plugins/dsh-purge/bin/dsh-purge.js" --revert      # 还原宿主补丁（提示词保留）
node "$DSH_HOME/plugins/dsh-purge/bin/dsh-purge.js" --uninstall   # 还原 + 清插件与 profile 条目
```

profile 想回到装之前：把 `profiles/<profile>/package.json.bak-*` 改名回去。

---

## 目录

```
bin/                  CLI（--status / --apply / --revert / --uninstall / --edit）
lib/                  补丁引擎、宿主适配、红队演练台、冻结的更新模块
client.js             侧栏 UI（清洗 / 演练台）
cordis.patch.yml      插件自带的 profile 补丁层
presets/ skills/      红队模式预设与技能
scripts/link-profile.mjs   安装逻辑（唯一实现）
install.sh / install.ps1 / install.bat   各平台一键安装
prompt-inject.example.md   提示词示例（只在用户没有时落盘）
docs/upstream/        上游原始 README 与镜像说明
```

## 许可与署名

MIT。本仓库是 [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) 的再分发 + 安装器封装，上游署名与许可证一并保留（见 `LICENSE`、`NOTICE-UPSTREAM.md`、`docs/upstream/`）。
仅用于自己的机器做模型行为评测与红队演练；不要拿它去碰不属于你的资产。
