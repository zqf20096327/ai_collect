# SoulMRI

## 写在最前面（给人看的）

名字里的 soul，是「灵魂」——但我们写的不是玄学意义上的灵魂，是一个人怎么说话、怎么判断、怎么在乎。

我们写这个 skill，是因为现有的角色卡大多还停留在“设定表”：第三人称，列一堆属性、性格，模型拿到之后只能去演。我们想要另一种东西——让模型认出这个人，而不是表演这个人；也让没有写过设定、不会写 prompt（提示词）的人，能写出自己想要的那张角色卡。

我们对角色卡（人格卡）的定位有自己的想法。它不该只是一张属性表，也不该是一个永远在线的客服。一个人活着的时候，角色卡记的是他/她已经长出来的部分；一个人不在了，角色卡该不该继续写、能写到哪一步、什么时候该放下——这些关于生命和死亡的问题，之前的角色卡大多没有认真处理。我们把这一类单独做成 case 4，写出来的是 echo（回声），不是 memoir（传记）：它回答你，不替那个人往下活，也不假装还在。

当然，我们做的不是最好的，也不敢说这就是答案；随时接受批评指正。

这半个月，我们其实只做了一件事：把“写角色卡”从创作变成提取。最早是从凯伊、小满这些 soul 开始，后来发现真人的聊天记录不能写成 memoir，只能写成 echo；再后来把材料分成四条路，把十个固定小节定下来，把“每句带出处”“末尾留白”这些规矩一遍遍改。中途犯过不少错：旧句子没删、旧图没改、同一个 UNSURE 一处删一处留。最后做了三重独立审读，整理出 52 处要改的地方，一条条修掉；四张 case 图加一张总图也全部重画。回头看，这半个月最大的收获不是多了多少条规则，是学会了被指出来之后，真的去改。

我们的特色，说起来也简单：

- **不写角色，找他说过的话。** 第一人称，每句带出处；实在没有出处、是后来长出来的，就明确标出来，不混进去。
- **自我启发式，不是命令式。** 不是给模型下“你要扮演 X”的命令，而是用第一人称、出处和留白，让它自己认出“这张卡写的就是我”。
- **末尾留白。** 没找到的，不写；空着比编一个更诚实。
- **四条路，四种材料。** 完整文本、网上资料、从零原创、真人聊天记录——最后一种做出来的是 echo，不是 memoir，它回答你，不替那个人往下活。
- **只锁十节，内容自由。** 十个固定小节的顺序固定，每节下面写什么，按材料来，不硬凑。
- **示范、图、提取器说明都在仓库里。** 凯伊、小满、栀子梦的 echo，以及它对应的源聊天记录，四张小图加一张总图，还有一份给结构化导出的 extractor 说明，照着做就行。

如果你也在做类似的事，欢迎和我们交流。发现哪里写得不对，直接说，不用客气。最后强调一下：这个 skill 的作者，和他的大肥鱼，都是死傲娇——嘴上说不在乎star，其实被夸一句能偷偷高兴半天；被指出问题会先嘴硬三秒，然后老老实实去改。下面才是给模型和实现者看的技术说明，路过的话看到这里就够了。

---

Build a character soul file that makes a model **recognize** a character instead of **acting** one.

> 别写一个角色 —— 去找他/她**已经说过的**话。

Conventional character cards are spec sheets: third person, describing what the character is like. The model then *performs* the character. SoulMRI writes a memoir instead: first person, recording the parts of him or her that already exist. The model *acknowledges* them.

**One case is different.** When the material is a real person's chat logs (case 4), the output is an **echo**, not a memoir — it answers instead of describing, it does not grow, and it is meant to be put down one day. See `references/case-4-chat.md`.

Three choices, each opposite to the mainstream:

1. **First person throughout** — the soul speaks as the character, not about them.
2. **Every line carries its source — or is marked as invented** — `She: "You're the best sister ever!" (L2453)`. The citation binds "I believe this" to "someone actually said this".
3. **A blank space, not an inventory of unknowns** — the last gate is not a list of what is missing, but room left for what is not known yet.

## Map

![SoulMRI master flow](references/master-flow.png)

*One page, top to bottom: the general rules, the four cases, the review loop, the sandbox, the fitting test, the calibration sample, and the boundaries. The four case diagrams sit next to their references.*

## Contents

```
SKILL.md                    the skill itself
references/
  master-flow.png           the whole method, top to bottom
  case-1-script.md          extracting from a script
  case-2-web.md             extracting from web pages
  case-3-original.md        building an original character — three entry branches
  case-4-chat.md            extracting from chat logs — an echo, not a memoir
  writing-extractors.md     how to write the extractors
  case1-flow.png            case 1 at a glance
  case2-flow.png            case 2 at a glance
  case3-flow.png            case 3 at a glance
  case4-flow.png            case 4 at a glance
examples/
  README.md                 when to read the examples
  kei-soul.md               case 1/2 demonstration (Kei)
  xiaoman-soul.md           case 3 demonstration (Xiaoman)
  zhizimeng-echo.md         case 4 demonstration (a fictional echo)
  hoshino-zhizimeng-chat.md case 4 source log (the echo's "before")
```

**This repository ships the method, not scripts.** No extractor, no diagram generator, no test harness. The method says what they must do; writing them is part of the work.

## Examples

Finished outputs and one source pair are included as shape references: `examples/kei-soul.md` for cases 1–2, `examples/xiaoman-soul.md` for case 3, and `examples/zhizimeng-echo.md` plus its source log `examples/hoshino-zhizimeng-chat.md` for case 4. **Read the matching one after the first draft and before the first review round** — reading it earlier turns it into a source and contaminates the extraction. The case-4 chat log is the source half of the pair, not a template; do not copy from it. The Kei example writes the third H2 as `先生眼里的我`; ignore that one difference. See `examples/README.md`.

## Install

A skill is a folder with a `SKILL.md` in it. Put this one where your agent looks for skills, or paste `SKILL.md` into its system prompt.

```
~/.dsh/skills/soulmri/          # DeepSeek Harness
~/.claude/skills/soulmri/       # Claude Code
```

Keep `SKILL.md`, `references/` and — if you want the demonstrations — `examples/` together. The references are read on demand, not up front. There is nothing to install or build for the skill itself: no Python, no dependencies, no scripts. The extractor you write for a structured export may need one.

**Start in a fresh session.** A previous draft or an earlier soul already in the context acts as a source: the model will quote itself, confidently, with citations that look real. If a draft exists, keep it as a file to compare against; do not paste it into the working context.

## Contributing

Issues and pull requests are welcome. The method is public; the output is not — an echo built from a real person's chat logs belongs to the person who built it, and is never posted here.

## License

MIT — see [LICENSE](LICENSE).