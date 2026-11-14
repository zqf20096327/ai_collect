# Girl Agent Love

[English](README-us.md) · **中文**

Girl Agent Love 是一个可以通过 Ren'Py 引擎来使用 AI 实时输出的框架。它可以用来自己做一个属于自己的 galgame。

Girl Agent Love is a framework that uses Ren'Py as the engine and lets AI write the story in real time. You can use it to build a galgame of your own.

**当前版本：1.0-b**



## 目录

- [项目结构](#项目结构)
- [人物卡和世界观](#人物卡和世界观)
- [图片](#图片)
- [声音](#声音)
- [存档与记录](#存档与记录)
- [子智能体模式](#子智能体模式)
- [自愈模式](#自愈模式)
- [版权与许可](#版权与许可)
- [起一个新作品](#起一个新作品)
- [如何使用](#如何使用)

## 项目结构

```
.
├── options.txt
├── README.md
├── README-us.md
├── LICENSE / NOTICE / THIRD_PARTY_NOTICES.md
├── game/
│   ├── ai.rpy / script.rpy / screens.rpy / options.rpy
│   ├── seikai.md
│   ├── persona/<英文id>.md
│   ├── picture/scene/<day|dusk|night>_<地点>.jpg
│   ├── picture/standing/<角色id>/<数字>.webp
│   ├── picture/ui/
│   ├── bgm/<数字id>.<格式> + bgm.md
│   ├── voice/<角色id>/<数字>.wav
│   ├── voice_example/<角色名字或id>.wav
│   ├── voice_ids.json
│   ├── opening.json
│   └── time_words.json（可选）
├── savedata/
│   ├── slot_<n>.json / .png
│   ├── history.json
│   ├── chapters.json
│   ├── diary/<角色>.json
│   └── harness/
└── skills/girl-agent-love-config/
```

`ai.rpy` 管模型调用、预取、剧情树、重注入、子智能体、日记、harness 和生图。`script.rpy` 管图片注册、渲染循环、存读档界面和动态舞台。



## 人物卡和世界观

人物卡放 `game/persona/<英文id>.md`，一个角色一个文件。文件名和 frontmatter 的 `id` 一致，下划线开头的文件不会被加载。其中`me.md` 是玩家角色。
frontmatter 常用字段：

```yaml
---
id: aya
name: 绫
gender: female
aliases: \[丛雨, 小雨，幼刀，丛雨大人]
lead: true
romance: true
affection: 0
voice\_name: Serena
---
```

1. `lead` 标记女主角，`romance` 决定是否结算好感，`affection` 是初始值。
2. 如果有专属称呼则放在说话人自己的卡里。比如*朝武芳乃*管*丛雨*叫「丛雨大人」，就加写在他们的「## 角色详细介绍」里，例如：

```markdown(朝武芳乃角色详细介绍）
管丛雨叫「丛雨大人」
```

``` markdown(丛雨角色详细介绍）
大多数人除了「主人」都叫我「丛雨大人」，我觉得太拘谨了，但没让他们改。
```

否则模型和引擎无法接上出现bug。


3. `gender` 只写 `female`、`male` 。
4. `voice\_name` 只在阿里云百炼tts时用，选固定音色。克隆声音可以不管这个。

4.正文按四节写：`开头一段`、`角色详细介绍`、`外貌与身体语言`、`立绘`。`角色详细介绍` 会整段喂给模型，写得越具体越好。可以去参考Bangumi或者萌娘百科等等的百科网站（请不要抄袭）。`外貌与身体语言` 中，对生图时写越详细立绘会更加准确地生成立绘；对文本时写越详细会更加准确写出剧情和提取立绘。**立绘要用数字 id**

示例：
```markdown
### 立绘 1

id：1
衣服：和服少女
动作：站着，双手在身前交叠
表情：张开嘴巴，瞪大眼睛，很惊讶的样子
什么时候用：日常时惊讶的时候

id：2
衣服：校服少女
动作：站着，双手在身前交叠
表情：张开嘴巴，瞪大眼睛，很惊讶的样子
什么时候用：穿着校服时惊讶的时候
```

5. `game/seikai.md` 是世界观，按七节写：简介、时代与地点、世界规则、主要场所、人物关系、禁忌与尺度、当前局势。主要场所要和 `picture/scene/` 的场所对上，模糊匹配。

## 图片

### 立绘图

1. 存入`picture/standing/<角色id>/<数字>.webp`。格式有`png` 、`jpg` 、`webp`。
2. 不支持分差，如果要不同表情要一套衣服存不同表情的立绘，然后在人设卡中描述。

### 背景图

背景图片放 `picture/scene/<时间>\_<地点>.jpg`。固定时间为day，dusk，night。格式有`png` 、`jpg` 。

## 声音

### 语音

1. **由于语音模型没有一个统一的接口，目前接口支持*阿里云百炼*，*mimo*，*Openai*，如果你有别的语音接口请根据他们的文档修改。然后语音模型生成的时间长，会出现语音跟不上模型的情况，如果出现这个情况请增大提前量。**
2. 如果是克隆声音，请将克隆的声音以`<角色英文id>.wav`形式存入`voice\_example/`中。

### 背景音

1. 支持支持 `mp3`、`ogg`、`wav`、`m4a`格式。
2. 背景音请以`<数字id>.<格式>`的形式存入`bgm/`中。在`bgm.md`中注册对应id的bgm如何使用。



## 存档与记录

存档、历史、日记都在项目目录的 `savedata/`，启动后自动创建。剧情历史不按拍数裁剪，长局会持续增长；需要控制体积时请手动归档或清空 `savedata/`。

## 子智能体模式

1. 每张非玩家 persona 卡一个子调用，各自只能拿到自己的卡、世界观、`game/agent.md` 和最近 `GALGAME_HISTORY_FEED` 拍的全局历史；父模型按 `game/director.md` 补旁白、重排拍序、写 choices，台词逐字回填。**理论上**会更加逼真。
2. 该功能可能会使子智能体生成速度有快慢区别导致的bug，也会出现子智能体错误返回的bug。这时候会降低游戏质量来保证游戏连续。
3. 关闭subagents模式时会让一个模型处理所有的文本，相对稳定。
4. `game/director.md` 和 `game/agent.md` 可以直接改；文件缺失或留空时回退到内置规则。重注入按全局历史拍数，每 `GALGAME_REINJECT_EVERY` 拍把各自的卡、世界观和规则文件升为全文。

## 自愈模式

option.txt中内置了一个自愈的开关，启动后会使用自愈模型在后台检测错误，及时修改，~~确保游戏可玩性~~。

如果你是harness模式，通过harness启动的，不需要理会这个设置。这个功能默认关闭。关闭时，如果使用harness启动，自愈模式仍在，通过harness的模型自愈。开启时，如果使用harness启动，则使用option的内置模型启动自愈，不使用harness的模型自愈。如果不想要harness的自愈，请你直接告诉harness，里面也有一个硬开关。

## 版权与许可

### Ren'py许可

Ren'Py 是 MIT 协议加部分 LGPL协议。分发的游戏要带 `game/LICENSE.txt`，保留 renpy.org 的许可证链接，不能阻止用户替换引擎。剧本不必开源。

### 关于这个框架的许可

这个框架受 Apache 2.0 协议保护，使用这个框架发布游戏时应该带上框架的声明和Ren'Py的声明。
本程序包含自由软件许可中的一些许可证，包括GNU宽通用公共许可证。 完整的软件列表请参见http://www.renpy.org/doc/html/license.html。
This program contains free software licensed under a number of licenses, including the GNU Lesser General Public License. A complete list of software is available at http://www.renpy.org/doc/html/license.html.
### 另外

1. 可能作品的图像由 AI 生成，商用前确认生成服务的条款。角色和剧本必须原创。BGM 请使用已授权素材，并在 About 页注明来源。
2. 请保护所有视觉小说作品的著作权，作者本人不建议用这个框架抄袭别的视觉小说。所有例子仅为示例，不代表作者本人抄袭或教唆抄袭该作品。



## 如何使用

### 方法一

安装 Ren’Py 8.5.3。到 [GitHub Releases](https://github.com/ACEyumoooo/Girl-Agent-Love/releases) 下载框架 ZIP 并完整解压。在 Ren’Py Launcher 中，将项目目录设置为解压后作品目录的上一级，选中作品后启动。

普通配置写入作品根目录的 `options.txt`，API 密钥写入 `key.txt`。既有作品若已使用备用配置目录，优先通过游戏内设置修改。填写真实密钥时请使用本地作品副本，提交或分享项目时请使用空白的密钥模板。

### 方法二

把他交给agent（ai），通过该项目的skill，让他来引导你做。

## 关于这个框架的维护

作者是一个非计算机的大三学生，平时还要忙做实验和上课（不要来食品专业）。我本身也会写写脚本，这玩意大多数是python写的，作者还是看得懂的，虽然我python也就哈喽沃德的水平，而且这玩意一大半都是ai写的。

作者可能会搞个superagent来替我维护，but目前来看是不大可能整这个，因为没米喵，米全去玩cosplay了，整服务器和喂好几个subagent的钱可能有点难负担得起，但是我真会考虑这个的！

所以说，在没有superagent的时候，我会抽空看看issue里面写了啥，然后会攒一些问题更新，让框架做的更好！

发布初期可能会面临一大堆bug，所以发布一个月内应该会疯狂更新。

## 一些问答

Q：我可以做女性向作品吗？
A：当然可以，这个框架虽然写着girl，但是你可以跟你的ai说“我要做一个女性向的”，他就会修改了。因为这个默认主角是男生，可攻略角色是女生。

Q：我可以把作品连同框架发布甚至用于商业吗？
A:当然可以。框架本身采用 Apache 2.0 开源许可，允许免费使用、修改和再分发，也包括随作品一起商业分发；自己的人设、立绘、背景、剧本和 BGM 归你自己，可以发布或出售，前提是遵守 Apache 2.0 和 Ren'Py 的许可。不过还是希望你不要把框架换个名字当成自己的原创作品发布，也不要用它抄袭别人的作品。Ren'Py 那边的内容请查看并遵守他们的许可。

Q：为什么UI和UX做的这么烂？
A：作者不会美术，UI是6.1sol做的，这玩意前端设计懂得都懂，我还回滚了不少。如果你在意这个，可以自己去设计，这个框架保留了设计入口，请尽情发挥！
