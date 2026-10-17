# project-ops-template

**Top-tier judgment, written down so a cheaper model can run it.**

This repo started in July 2026 as a race against a deadline: the top judgment-tier model of the day was announced to leave subscription use, and the goal was to capture how it worked before it went. The deadline did not hold — that tier is still available — but the reason for the repo never depended on it. Frontier models cost several times what mid-tier ones do, and they are the first thing you lose when a plan, a budget, or a provider changes. The point is to *capture that judgment as portable doctrine*: a rules layer that lets a mid-tier model (Sonnet-class, even Haiku-class) operate at the top-tier level on the things that matter — knowing when to delegate, when to escalate, when to stop and ask, how to verify without lying to itself, and how the rules themselves get safely revised over time.

Whether or not you keep the model, you keep the operating discipline that made it good. That transfer — top-tier judgment → concrete, executable rules a lesser model can run — is the whole idea, and it's why the rules are written concrete-to-the-point-of-executable, every one with a decision test and worked examples.

Works with Claude Code, or any harness built around a `CLAUDE.md`-style entry file plus a subagent/dispatch mechanism.

## Why this one, and not a prompt-generated template

This is not a set of rules an LLM was asked to draft in one pass and never ran. It is the operating manual of an actual long-running multi-agent deployment, extracted, sanitized, and open-sourced.

The concrete difference: after the first full version was written, the strongest model available in that deployment was handed the eight-step command loop and told to run it, for real, against a real task — not to review it, to *use* it. It came back and, in its own words, patched three concrete gaps the desk-review pass had missed (a role-assignment ambiguity, a missing "worker lane" for delegated subtasks, and a fuzzy test for telling a genuine limitation from an excuse). That's the v1.1 revision baked into these files. The rules have also since been the actual dispatch backbone for a real cross-machine deployment and ongoing multi-agent collaboration — every worked example in `ops/00-command-loop.md` and `ops/50-diagnosis.md` is a dated, real incident with the identifying details removed, not a hypothetical.

Put simply: most templates are a blueprint. This one is a floor plan traced from a house people actually live in — the floorboards that creak are marked, because someone found them by stepping on them.

## What's in the box

```
project-ops-template/
├── README.md                  ← this file (safe to delete after deployment)
├── CLAUDE.md.template         ← a lean, routing-only CLAUDE.md skeleton
├── DEPLOY.md                  ← three-step install guide
└── ops/
    ├── 00-command-loop.md     ← the entry point: an 8-step loop for handling any instruction
    ├── 10-dispatch.md         ← dispatch rules: model tiers, escalation, verify-don't-self-verify
    ├── 20-judgment.md         ← judgment rubrics: escalate / done / ask / wrong-approach / quality bar
    ├── 30-templates.md        ← 5 dispatch prompt templates: search / build / refactor / research / review
    ├── 40-maintenance.md      ← how the rules change safely: who can edit what, where lessons go
    ├── 50-diagnosis.md        ← a self-check for the 3 most common token/focus/correctness failures
    ├── 60-letter.md           ← a letter to future sessions: the traps, and how this degrades over time
    └── lessons.md             ← empty pitfall log, ready to fill in
```

## Install in three steps

Full instructions: [`DEPLOY.md`](./DEPLOY.md). Short version: copy `ops/` and `CLAUDE.md.template` into your project, open a session and have it run the bootstrap prompt in Step 2, then open a *second, fresh* session to independently sign off using Step 3's review prompt. Total time: about one session.

## Design principles (understand these before changing anything)

- **`CLAUDE.md` is a router, not an encyclopedia** — keep it under ~60 lines; every real rule lives in `ops/`.
- **Weak models need explicit, not clever** — every rule is written to be executable without taste, with a matching positive and negative example. Anything left abstract is treated as if it weren't written at all.
- **No dependency on a frontier-tier model** — the whole loop is designed to run on a mid-tier model. The cases where that genuinely isn't enough (taste calls, undefined problems) have an explicit, honest exit path documented in `ops/20-judgment.md` §6.
- **Built to evolve** — lessons land in `ops/lessons.md`, then get folded in and trimmed per `ops/40-maintenance.md`, so the rule set doesn't bloat or quietly drift out of date.

## Changelog

- **v1.2 (2026-09)** — reframed the opening (the model-sunset premise didn't hold; the cost argument does); added four rules that the source deployment learned the hard way since v1.1: a timeout-killed task is never "done" (R2.5), check past rulings before asking the requester again (R3), a symptom patch must dispose of its root cause (R7), and every delivery must name its own weakest point (report contract).
- **v1.1 (2026-07)** — revised after the eight-step loop was run end-to-end for real; see the header of `ops/00-command-loop.md`.

## Known limits (an honesty clause)

This system improves execution quality — decomposition, acceptance criteria, multi-candidate review. It does not solve the hard part of taste and ambiguous problem definition; what to do when you hit that wall is written explicitly in `ops/20-judgment.md` §6: escalate the model, get an independent second opinion, or say plainly that you can't. Separately: this template was written and generalized by a session outside the target environment it will be dropped into — that's exactly what `ops/00-command-loop.md`'s Step 0–1 and the environment-verification habit throughout `ops/10-dispatch.md` are for. Treat every environment-specific fact (model ids, tool names) as something to re-verify on arrival, not something to trust from this document.

---

# project-ops-template（繁體中文說明）

這份在 2026 年 7 月開始時是在趕一個期限：當時最頂級的判斷型模型宣布要退出訂閱制，目標是趁還能用的時候把它的做事方法記下來。後來期限沒有成真，那一級模型仍然可用，但這份存在的理由從來不靠它：頂級模型的成本是中階的好幾倍，也是預算、方案或供應商一變動就第一個失去的東西。

所以它是一套可移植的「模型調度作業系統」，讓中階模型（Sonnet 級、Haiku 級）也能穩定接管一個專案的全程運作：什麼時候該派工、什麼時候該升級模型、什麼時候該停下來問人、怎麼驗證才不會自己騙自己，以及這套規則本身該怎麼安全地被修訂。

適用於 Claude Code，或任何以「CLAUDE.md 風格入口檔 + 子代理／派工機制」為架構的 harness。

## 為什麼是這份，而不是隨便一份提示詞產生的樣板

這不是找一個 LLM 一次性生成、從沒實跑過的規則集，而是一套真實長跑多代理部署的作業手冊，經過整理、去識別化後開源。

具體差異：第一版制度寫完後，該部署中最強的模型被要求把「八步指揮迴圈」拿去**真的跑一次任務**——不是審閱，是實際使用。它跑完之後用自己的話補了三個桌面審閱沒抓到的落差（第 0 步的角色分岔沒講清楚、第 3 步少了給被派工 worker 用的「認列車道」、第 6 步分不出真假限制的判準）。這次修訂就是現在收進檔案裡的 v1.1。這套規則後來也真的撐起過一次跨機部署與持續進行中的多代理協作——`ops/00-command-loop.md` 與 `ops/50-diagnosis.md` 裡的每個實例都是去識別化後的真實日期事件，不是假設案例。

用一句話說：多數模板是藍圖；這份是從一間有人真的住過的房子描出來的平面圖——哪塊地板會叫，是有人真的踩過才標出來的。

## 包內容

```
project-ops-template/
├── README.md                  ← 本檔（部署完成後可刪）
├── CLAUDE.md.template         ← 精簡路由型 CLAUDE.md 骨架
├── DEPLOY.md                  ← 三步部署說明
└── ops/
    ├── 00-command-loop.md     ← 入口：接到任何指令的八步作業迴圈
    ├── 10-dispatch.md         ← 派工守則：模型分級、升降級、驗證不自驗
    ├── 20-judgment.md         ← 判斷力 rubric：升級／完成／該不該問／換路／品質底線
    ├── 30-templates.md        ← 五類派工模板：搜尋／實作／重構／研究／審查
    ├── 40-maintenance.md      ← 制度怎麼安全地改：誰能改什麼、教訓歸檔去哪
    ├── 50-diagnosis.md        ← token／失焦／出錯三大漏洞自檢
    ├── 60-letter.md           ← 給未來 session 的信：陷阱與制度退化的方式
    └── lessons.md             ← 空白坑卡，隨時可寫
```

## 三步部署

完整步驟見 [`DEPLOY.md`](./DEPLOY.md)。簡述：把 `ops/` 和 `CLAUDE.md.template` 複製進你的專案，開一個 session 照步驟二的指令跑部署，再開一個**全新、獨立**的 session 用步驟三的驗收指令做獨立驗收。全程約一個 session 的時間。

## 設計原則（改動本制度前先理解）

- **CLAUDE.md 是路由不是百科**：控制在 60 行以內，細節全在 `ops/`。
- **弱模型需要明確，不需要聰明**：每條規則寫到可直接執行，附一正一反例；抽象的要求視同沒寫。
- **不依賴頂級模型**：整套流程設計成中階模型可跑；真正跑不動的部分（品味判斷、問題本身沒定義清楚）在 `ops/20-judgment.md` 第 6 節有明寫的退場方式，不硬撐。
- **可長期演化**：教訓先進 `ops/lessons.md`，再依 `ops/40-maintenance.md` 收編與精簡，防止規則肥大或悄悄過時。

## 已知極限（誠實條款）

這套制度能補的是執行品質——拆解、驗收、多樣本評審；補不了品味判斷與問題定義本身的模糊。真的卡在那裡時該怎麼辦，`ops/20-judgment.md` 第 6 節寫得很明白：升級模型、找外部第二意見、或直接說做不到。另外要注意：這份模板是由目標環境之外的 session 撰寫並泛化而來——這正是 `ops/00-command-loop.md` 第 0-1 步、以及 `ops/10-dispatch.md` 貫穿全篇的「環境事實要實查不要憑印象」習慣存在的原因。任何環境相關的細節（模型 id、工具名稱）到你的環境後都請重新查證，不要直接信任本文件裡的範例值。
