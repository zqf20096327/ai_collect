# goodcase

[English](README_EN.md) | 中文

[![Site](https://img.shields.io/badge/site-goodcase.ai-orange)](https://goodcase.ai/?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=badge)

**爆款 AI 提示语，我们挑出来换个模型重跑，结果好坏都公开，例证跑得稳的 skill 标成稳定复现。**

重跑过的，结果摆给你看。

```bash
npx skills add LearnPrompt/goodcase --skill goodcase
```

这一行把 goodcase 查询 skill 装进你的 agent，Claude Code、Codex、Cursor 这类认 SKILL.md 的都能用。装好以后用大白话问它就行：

- 找几个 AI 视频的爆款案例
- 有没有玻璃质感的图像提示语
- 用第 2 条，换成我的主题

它会去查 [goodcase.ai](https://goodcase.ai/?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=hero) 的公开接口，把案例的出处、作者、完整提示语、稳定分和成本档带回来，不需要任何 API Key。接口连不上的时候，它改查随包带的离线数据，并在回答里写明数据日期。

想先看案例和原片对照，去 [awesome-seedance](https://github.com/LearnPrompt/awesome-seedance?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=hero)。想看每个 skill 现在的状态，去 [goodcase.ai/skills](https://goodcase.ai/skills?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=hero)。

## 这个仓里装着什么

两样东西。

一样是上面那个 goodcase 查询 skill，在 `skills/goodcase`。

另一样是从 goodcase.ai 的热门案例里提取出来的 112 个 skill，在 `skills/generated`，一个 skill 一个目录，里面是一份 SKILL.md 和它的例证案例。其中视频 70 个，图像 27 个，网页 15 个。想单独装哪一个，把它的 slug 换进这行命令：

```bash
npx skills add LearnPrompt/goodcase --skill product-ad-shot-design
```

slug 就是 `skills/generated` 下面的目录名，也是 goodcase.ai 上那个 skill 页面地址的最后一段。

## 稳定复现是什么意思

标着稳定复现的 skill，至少有 3 条例证被重跑过，八成以上达到 70 分。

稳定复现说的是例证的原提示语重跑的结果，没测过 skill 生成的新内容。

截至 2026-11-19，全站提取的 112 个 skill 里有 48 个稳定复现。这是全站口径，视频、图像、网页都算在内。数字会随复测变化，以 [goodcase.ai/skills](https://goodcase.ai/skills?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=stable) 上的为准。剩下的 skill，有的例证还没测够 3 条，标的是待测；有的测过了但没到这条线；还有一些暂时没法实测。

## 看案例和对照

想先看东西再决定装什么，去 [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=cases)。那边是 Seedance 的案例库，每条带原帖出处和完整提示语，同一段提示语换模型重跑的结果也摆在那里，跑得不好的同样留着。

那个仓只收视频类，所以它写的 skill 数字是视频口径，跟这里的全站口径对不上是正常的。

## 本地跑站点（可选）

这个仓同时是 goodcase.ai 站点的开源版本。clone 下来就能跑起同样的界面，自带一组真实样例案例，不用配任何环境变量。

```bash
git clone https://github.com/LearnPrompt/goodcase.git
cd goodcase
npm ci
npm run dev
```

打开 http://localhost:3000 就能看到首页、案例库、案例详情和创作者页。线上站点的数据供给、审核后台与自动采集属于内部系统，不在本仓库里。想用完整数据，直接调线上公开接口，同样不需要 API Key：

```bash
curl -s "https://goodcase.ai/api/public/cases?take=3&locale=zh-CN"
```

接入文档见 [goodcase.ai/connect](https://goodcase.ai/connect?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=site)。想接自己的数据，把 `.env.example` 复制为 `.env.local`，填入你自己的 Supabase 项目地址与密钥，表结构参考 `/api/public` 路由与 `src/lib/cases.ts` 里的行类型。部署按标准 Next.js 应用来，Vercel 或任何支持 Node.js 的平台都行。

## 致谢

每个 skill 的例证都来自公开发布作品的创作者，出处和署名写在各自的 `references/cases.md` 里，谢谢他们把提示语公开出来。

安装命令用的是 [vercel-labs/skills](https://github.com/vercel-labs/skills) 这个命令行工具。

案例、稳定分和复测数据来自 [goodcase.ai](https://goodcase.ai/?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=thanks)。

## License


代码：MIT，见 [LICENSE](./LICENSE)，版权归 LearnPrompt。

随仓库附带的样例案例、提示词与媒体文件不在 MIT 范围内：`public/media/goodcase/` 目录（含其中的 `avatars` 头像）里的图片与视频，以及 `skills/generated/**/references/cases.md` 中的案例正文，版权仍归各原始创作者所有，这里只是为了标注出处、方便复现而收录。

策展与元数据（案例的分类、标签、评分、复测记录、翻译与说明文字）按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 开放，署名 GoodCase.ai 即可。

如果你是创作者，不希望作品出现在这里，或者发现出处标错，通过 [goodcase.ai/connect#feedback](https://goodcase.ai/connect?utm_source=goodcase-repo&utm_medium=github&utm_campaign=readme-zh&utm_content=license#feedback) 留言（选「内容」类型，附案例链接），或在本仓库开一个 Issue，我们会尽快下架或更正。

参与贡献看 [CONTRIBUTING.md](./CONTRIBUTING.md)，安全问题看 [SECURITY.md](./SECURITY.md)。
