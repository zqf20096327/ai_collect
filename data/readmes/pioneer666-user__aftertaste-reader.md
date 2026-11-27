# Aftertaste Reader · 回味

会写基本功能，想读懂真实项目？用回味把 AI 讲解和 Git 固定提交的源码放在一起，顺着一次请求看清数据怎样传递、何时写入、最后返回什么。

[获取预构建安装包与校验值](https://github.com/pioneer666-user/aftertaste-reader/releases) · [快速开始](#首次安装) · [反馈使用体验](https://github.com/pioneer666-user/aftertaste-reader/issues)

## 同一个收藏请求提交两次，还会再写一次数据库吗？

从左到右读 Apache Answer 的收藏闭环。悬停「查现有收藏」先看查询条件，再顺着「已经收藏」或「还未收藏」看两种结果。下方的问句可展开写入事务里的复查。

![回味闭环画布。请求经 Xorm 查找收藏关系，服务判断后分成首次收藏和直接返回两条路径。查询卡上方悬停预览，判断卡下方展开说明。](docs/usage/assets/alpha2-bookmark-loop.png)

跟到「要写入吗？」对应的文件讲解，第 61–63 行就是分岔。假设同一用户再次收藏同一问题，且上一笔已成功，服务查到已有关系便提前返回，跳过插入和计数更新。

![回味源码对照。左边是固定提交中提前返回的 Go 条件，右边解释收藏目标与现有关系如何决定分支。](docs/usage/assets/alpha2-bookmark-source.png)

截图取自回味 `0.1.0-alpha.2` 和 [Apache Answer v1.5.0 的固定提交](https://github.com/apache/answer/commit/3f1ed50f6776452c11b6ffdbdc767cd1887d629b)。图中的上游代码节选按 Apache License 2.0 使用，版权归 The Apache Software Foundation。[源码位置](https://github.com/apache/answer/blob/3f1ed50f6776452c11b6ffdbdc767cd1887d629b/internal/service/collection/collection_service.go#L57-L63) · [Apache Answer 许可](docs/usage/assets/apache-answer-LICENSE.txt) · [上游 NOTICE](docs/usage/assets/apache-answer-NOTICE.txt)

## 首次安装

以下命令适用于 Windows PowerShell。准备 Node.js 24 LTS、npm、Git 2.45+、一个已有 Git 提交的本地项目，以及能读取本机文件和运行终端命令的 AI。确认 `node --version` 显示 `v24.x`，再用 `npm --version` 和 `git --version` 检查工具可用。

拿到回味的 `aftertaste-reader-*.tgz` 后，在 PowerShell 执行以下命令。按提示粘贴包的完整路径，再输入项目目录。npm 联网安装运行依赖。工具安装在独立目录，项目保留在原来的位置。

```powershell
$package = (Resolve-Path -LiteralPath (Read-Host '回味安装包的完整路径') -ErrorAction Stop).Path
$tools = Join-Path $env:LOCALAPPDATA 'Aftertaste Reader'
New-Item -ItemType Directory -Path $tools -Force | Out-Null
npm install --prefix "$tools" --omit=dev "$package"
if ($LASTEXITCODE -ne 0) { throw '安装失败，请查看 npm 输出。' }
$project = (Resolve-Path -LiteralPath (Read-Host '要阅读的 Git 项目目录') -ErrorAction Stop).Path
$installed = Join-Path $tools 'node_modules/aftertaste-reader'
$skill = Join-Path $installed 'skills/aftertaste-reader/SKILL.md'
$skill
$project
```

把最后两行输出填入下面这句话，发给 AI。把引号里的困惑换成你真正想读的问题。

> 请显式读取「Skill 完整路径」，为「Git 项目完整路径」生成回味讲解。我想先读「例如登录后的数据如何保存」。先只生成一小批，读过再继续。请告诉我怎样打开第一篇。

AI 会确认缺失的范围和节奏。项目还没有讲法时，先从三种讲法里选一种。第一次写入前，AI 会检查这一批资料在 Git 中是否可见。如有可能纳入提交的资料，等你选择在本机忽略、按现有设置继续或暂停。默认固定开始时的 HEAD，要读其他版本可以给出本地 Git 提交。

读完第一篇，可以请 AI「从已有讲解里找一条能回答我的问题的闭环路线」。选好路线后就能保存，从图上逐步对照源码。

阅读服务在本机运行，讲解、闭环和个人阅读记录保存在所读项目里。生成讲解时，源码如何交给模型处理取决于你选择的 AI 宿主及其设置。

## 日常打开与关闭

让已读取回味 Skill 的 AI「帮我打开回味阅读器」。新讲解或闭环完成后，AI 会尝试打开选定的起读位置。浏览器没有自动打开时，把 AI 或终端返回的完整私密入口粘贴到浏览器地址栏。如果要自己选浏览器，可以说「只给我链接」。从阅读器顶栏「阅读链接」也可复制私密入口，粘贴到本机另一款浏览器，服务停止后失效。

也可打开 PowerShell，用安装后的 CLI 启动阅读器。

```powershell
$tools = Join-Path $env:LOCALAPPDATA 'Aftertaste Reader'
$cli = Join-Path $tools 'node_modules/aftertaste-reader/dist/cli/main.js'
$project = (Resolve-Path -LiteralPath (Read-Host '要阅读的 Git 项目目录') -ErrorAction Stop).Path
node "$cli" serve --project "$project"
```

在自己的终端找到启动输出中的 `url`，直接在浏览器打开。这个私密入口只供自己使用。进入后可收藏地址栏里的普通链接，在本次服务和同一浏览器中重开。更换浏览器时用本次私密入口，重启后用新入口。从左栏选一篇讲解，或从顶栏「闭环阅读」打开已保存的闭环。即使断网，页面、字体和已有讲解也由本机提供，源码从原项目的 Git 提交读取。

端口占用时可在启动命令后加 `--port 4318` 或指定另一个空闲端口。在启动终端按 Ctrl+C，看到 `status=stopped` 即已关闭。下次执行同一条启动命令，便可继续读同一项目。

把上述命令的 `serve` 换成 `open-reader`，会在就绪后请求默认浏览器打开。加 `--mode link` 只取链接。后台服务会在命令退出后继续，可请 AI 停止，或用同一个项目执行 `node "$cli" stop-reader --project "$project"`。

进一步操作见[阅读器使用说明](docs/usage/file-reader.md)和[生成讲解与闭环](docs/usage/generation-skill.md)。

## 构建本地包

维护者在干净的仓库检出中使用 Node.js 24 和唯一的锁文件。把包输出到独立目录，供读者安装。

```powershell
npm ci
npm run typecheck
$packageDir = Join-Path ([System.IO.Path]::GetTempPath()) 'aftertaste-pack'
New-Item -ItemType Directory -Path $packageDir -Force | Out-Null
npm pack --pack-destination "$packageDir"
```

`npm pack` 会先编译命令工具并构建页面。读者运行已经打包的成果，只需 Node.js、npm 和 Git。仓库中的包保持私有配置。

## 开发与沿革

- [协作入口](AGENTS.md) · [现行规格](specs/001-first-release/08-current-spec-and-acceptance.md) · [项目待办](docs/product/backlog.md)
- [Git 固定提交](specs/002-fixed-source/quickstart.md) · [讲解文档](specs/003-document-blocks/quickstart.md) · [文件依赖图](specs/004-dependency-graph/quickstart.md)
- [开发规范交接](docs/work/2026/11/D002-directory-layout/handoff.md) · [Spec Kit 接入](docs/development/spec-kit.md) · [实验](experiments/README.md)

2026-11-16 的设计交接、仓库初始化和早期 AR1 原话索引保存在本仓库历史中，可用 `git show 8bd5e7b:README.md` 查阅。现行产品行为以当前规格和后续确认的任务为准。

## 开源许可

回味自有的代码、产品 Skill、文档、设计和开发记录采用 MIT，允许使用、修改、再分发和商用。分发时请保留版权与许可声明。[MIT 许可证](LICENSE)

第三方开发技能、Spec Kit、字体及网页依赖各有原作者与许可。安装包内的 `dist/web/third-party-licenses.md` 收录网页构建所用依赖，另附 Vue Flow 已内嵌依赖的声明。[开发技能来源](.agents/README.md) · [Spec Kit 许可证](.specify/LICENSE-SpecKit.txt) · [补充第三方声明](THIRD-PARTY-NOTICES.md)
