<p align="center"><img src="./assets/yomiyasu-mini.png" alt="yomiyasu-mini logo" width="600"></p>

# yomiyasu mini（よみやす みに）

## これは何？

yomiyasu-mini は、AIが書いた日本語を推敲するスキル [yomiyasu](https://github.com/nanaism/yomiyasu)（以下「本体」）を、スキルの大きさに上限がある環境に入るように短くしたスキルです。本体 v3.0.0 から、抽出表と生成のスクリプトで作っています。

SKILL.md は本体の SKILL.md を節ごとに写し、mini にない道具（lint、check の実行の記録など）を指す所と、まとめた参照ファイルの場所を替えています。参照ファイルも本体の文を写し、文書の種類ごとと分野ごとのファイルは、それぞれ1本にまとめました。意味が変わる恐れを数える検査は、本体の `yomiyasu_diff.py` と `markdown_visibility.py` から要る定義だけを取り出したスクリプトで行います。

**使うのは [`skills/yomiyasu-mini/`](./skills/yomiyasu-mini/) の17個のファイルだけです。** このリポジトリのほかのファイルは、Claude Code のプラグインとして入れるための設定（`.claude-plugin/`）と、本体から作り直したり、本体と比べて測ったりするためのものです。

| ファイル・フォルダ | 中身 |
|---|---|
| `skills/yomiyasu-mini/SKILL.md` | スキルの本文（先頭の YAML を含めて15,215字） |
| `skills/yomiyasu-mini/references/` | 参照ファイル11個（`audience.md`、`calques.md`、`doc-types.md`、`domains.md`、`fact-recovery.md`、`fact-recovery-details.md`、`gemini-syntax.md`、`persona.md`、`rephrase-test.md`、`review-points.md`、`slop-catalog.md`）。`doc-types.md` と `domains.md` は本体の `doc-types/` の13個と `domains/` の3個をまとめたもので、ほかは本体と同じ名前のファイル |
| `skills/yomiyasu-mini/scripts/` | 検査の `mini_check.py` と、本体の diff から取り出した `mini_diff_1.py`〜`mini_diff_3.py` |
| `skills/yomiyasu-mini/LICENSE.txt` | MIT ライセンス |
| `.claude-plugin/` | Claude Code のプラグインとして入れるための設定（`plugin.json` と `marketplace.json`） |
| `extract/`、`tools/`、`MANIFEST.json` | 本体から作り直すための抽出表、生成と `.zip` のスクリプト、生成の記録 |
| `measurement/` | 本体と比べて測った結果 |
| `tests/` | 生成、上限、本体との一致の試験 |

## こんなときに

スキルを読み込めるのに、SKILL.md の字数やファイルの数、1ファイルの大きさに上限があって、本体を入れられない環境のためのものです。

たとえば Microsoft 365 Copilot の宣言型エージェントのカスタムスキルについては、[Microsoft の文書](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-skills)に次のことが書かれています。

- SKILL.md の指示は2万字未満
- Agent Builder に上げる `.zip` は50MBまで、1ファイルは25MBまで
- ファイルはすべてのスキルを合わせて350個まで、フォルダの深さは3まで
- スクリプトはネットワークにつながらない場所で動き、パッケージを入れられない

mini は SKILL.md を先頭の YAML を含めて18,000字以下、スクリプトを1本90KB以下、参照ファイルを1本100KB以下にし、標準ライブラリだけで動くようにしています。配るファイルは17個（SKILL.md のほかに16個）で、[Copilot Cowork の文書](https://learn.microsoft.com/en-us/copilot/cowork/cowork-plugin-development)にある SKILL.md のほかのファイルの上限（1つのスキルで20個まで、1つ5MBまで、合わせて10MBまで）にも収めています。`.zip` には先頭のフォルダを付けずに SKILL.md をルートに置き、中のパスは `references/doc-types.md` のように、ファイル名を含めて2段までです。これらの上限は生成と `.zip` を作るたびに確かめています。

## なぜ作ったか

本体 v3.0.0 は SKILL.md（先頭の YAML を含めて15,656字）と参照ファイル、検査のための Python スクリプトなど、43個のファイルでできています。SKILL.md の字数は Microsoft の文書の上限（指示は2万字未満）に収まりますが、SKILL.md のほかのファイルは42個あり、Copilot Cowork の文書の上限（20個まで）を超えます。ほかに、Copilot Cowork の文書が置けないとするドットで始まる名前のフォルダ（`.codex-plugin/`）と、Microsoft の文書の表にない、拡張子のない `LICENSE` があります。スクリプトのうち lint、diff、check は、どれも1本で100KBを超えます。

Copilot の Agent Builder で、v2.0.0 から v2.1.0 までの本体を読み込めなかったという報告が、複数の利用者からありました。別の利用者からは Copilot のほかのアプリで、ファイルの数やスクリプト1本の大きさで引っかかったという報告がありました。

mini は本体の文を写したうえで、ファイルの数と大きさをこれらの上限に収める形にまとめた、本体とは別のスキルです。本体は lint、diff、check の検査と、種類ごと・分野ごとの参照ファイルを含めた形のままです。

## 使い方

### Agent Builder に上げる `.zip` を作る

```bash
git clone https://github.com/nanaism/yomiyasu-mini
```

```bash
cd yomiyasu-mini
```

```bash
python3 tools/build_zip.py --out dist/yomiyasu-mini-2.0.0.zip
```

`.zip` の中身は `skills/yomiyasu-mini/` の17個のファイルで、先頭のフォルダを付けずに SKILL.md を `.zip` のルートに置きます。[Microsoft の文書の Agent Builder の例](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills)と同じ形です。`build_zip.py` は作る前と作ったあとに上の上限を確かめ、超えていれば何も書かずに止まります。同じ中身からは、いつ作っても同じバイトの `.zip` ができます。

### Claude Code のプラグインとして入れる

```text
/plugin marketplace add nanaism/yomiyasu-mini
/plugin install yomiyasu-mini@yomiyasu-mini
```

Claude Code にプラグインで入れたスキルは `yomiyasu-mini:yomiyasu-mini` という名前になります。

入れたプラグインを最新版へ更新するときは、ターミナルで次のコマンドを実行します。

```bash
# マーケットプレイスの情報を更新
claude plugin marketplace update yomiyasu-mini

# プラグインを最新版へ更新
claude plugin update yomiyasu-mini@yomiyasu-mini
```

更新を反映するには、Claude Code を再起動してください。

### スキルのフォルダとして置く

`skills/yomiyasu-mini/` を、使うツールがスキルを読むフォルダに写します。測定では Claude Code の作業フォルダの `.claude/skills/yomiyasu-mini/` に置きました。

### 頼み方

名前を出して頼みます（「yomiyasu-mini で推敲して」「$yomiyasu-mini」など）。SKILL.md の description には、名前を出さずに文章を書かせる依頼では使わないと書いています。

SKILL.md では、出力の形の指定がなければ、書き直した本文、変えたところ、確認の記録を返すように決めています。残したAIっぽいところ、書き手に確かめたい点、事実の確かめの欄は、あるときだけ付けます。確認の記録には、検査のスクリプトが出した状態の行をそのまま写します。測定（Claude Code）では、mini の153回の返事のすべてにこの行がありました。

```text
yomiyasu-mini-check: ran version=2.0.0 base=v3.0.0@7b212ff meaning_risk=0 counted=0
```

`ran` は検査を最後まで実行したこと、`meaning_risk` は意味が変わる恐れの件数、`counted` はそのうち本体の `--fail-on meaning-risk` が数える件数です。Python がないときは `not_run reason=no_python`、実行を断られたときは `not_run reason=not_allowed` と書き、検査をしたとは書かないように決めています。

検査のスクリプトだけを動かすこともできます。`mini_check.py` はファイルを書かず、引数で渡されたファイルが作業フォルダの外か、作業フォルダから下の点で始まる名前のファイルやフォルダの中にあるときと、通常のファイルでないとき（FIFO など）は読みません。最終稿が空のときと、原文と最終稿が同じファイルのときは、本体と同じく検査しません。

```bash
python3 skills/yomiyasu-mini/scripts/mini_check.py --source 原文.md --final 最終稿.md
```

ファイルにできないときと、作業フォルダの外や作業フォルダから下の点で始まる名前の場所にあるファイルを検査するときは、`--stdin` で原文と最終稿を1つの標準入力にまとめて渡します。区切りの行は本体の `yomiyasu_check.py run --stdin` と同じです。

```bash
python3 skills/yomiyasu-mini/scripts/mini_check.py --stdin <<'EOF'
<<<yomiyasu:original>>>
（原文）
<<<yomiyasu:final>>>
（最終稿）
EOF
```

## 入れた決まり

SKILL.md は本体と同じ「基本原則」「実行手順」「出力フォーマット」の3つの章でできています。

- 本体 v3.0.0 の SKILL.md を節ごとに写し、見出しの名前も h1 のほかは本体のままにしています。替えたのは、mini にない道具を指す所（lint、check の run と verify と実行の記録、本体の CLI のオプション、本体の `allowed-tools` のスクリプト、本体の状態の行）と、まとめた参照ファイルの場所です。lint をかける手順（Step 2 の1）、検査（Step 3）、提出の前の照合（Step 5）は mini_check と目で見る点検の手順に書き直し、ほかの節は本体の文のままか、置き換えと削除だけを当てています。ほかに、h1 のすぐ下に mini の前書きを足し、front matter の description を280字に収まるように言い換えています。
- front matter の `allowed-tools` には `mini_check.py` を `python3`、`python`、`py -3` で呼ぶ3つだけを書いています。`mini_check.py` は、引数で渡されたパスが作業フォルダの外か、作業フォルダから下の点で始まる名前のファイルやフォルダの中にあれば、開かずに止まります（標準入力で渡された本文は読みます）。
- 資料から事実を補う手順（Step 2 の3）と「事実の確かめ」の欄、相対の日付に日付を添える決まり、`python3`、`python`、`py -3` の順に試す決まりは、本体の道具を指していないので、本体の文のまま写しています。
- 参照ファイルも本体の文を写し、mini にないファイルと道具を指す所を置き換えと削除で替えています。

本体から外したのは、おもに mini にない道具に関わる手順と出力の欄です。lint と lint の規則の名前、diff の文体の硬化と勢いの検査、check の実行の記録、確認の記録の「硬化の検査」「勢いの検査」「見直し候補」の行、lint が読む語のファイル（`references/lists/`）がこれに当たります。参照ファイルのうち、lint と check と diff の出力だけを説明する章と節（audience.md の13章、fact-recovery-details.md の8章、review-points.md の1章と2章の多くの節）も写していません。部品ごとの扱いと理由は [extract/NOTES-content.md](./extract/NOTES-content.md) の9章と、[extract/table.json](./extract/table.json) の各部品の `note` にあります。

## 測った結果

本体 v3.0.0 の `tests/corpus/` の51本（`raw_ai/` 26本、`blacklist_ai/` 24本、`edge_cases/` 1本。mini 1.1.0 と 1.2.0 の測定と同じ51本）を、本体 v3.0.0 と mini で3回ずつ推敲させました。推敲させたのは Claude Code の claude-opus-5-5 で、effort は high です。本体と mini で同じモデルと設定を使いました。意味が変わる恐れは本体の `yomiyasu_diff.py --fail-on meaning-risk` で、残った候補は本体 v2.5.0 の `yomiyasu_lint.py` で数えました。

| | 本体 | mini |
|---|---|---|
| 意味が変わる恐れ（`--fail-on meaning-risk` が数える件数。51本×3回の合計） | 4 | 3 |
| 意味が変わる恐れ（1回目・2回目・3回目） | 1・2・1 | 1・1・1 |
| 書き直した文に残った warn 以上の候補（1回目・2回目・3回目。元の文では30） | 19・20・19 | 20・22・20 |
| 書き換えた量の中央値（元の文の空白を除く1,000字あたりの字数。1回目・2回目・3回目） | 21.2・28.0・20.6 | 18.2・22.2・15.7 |
| 入力トークンの中央値（1本） | 164,403 | 135,247 |

測る前に決めた合格の条件は、mini の3回の合計が、同じ51本の本体の3回の合計を超えないことです。mini は3件で、本体の4件を超えていないので、この条件を満たしています。

測ったのは、検査のスクリプトが入力を確かめる所と人向けの出力の文、SKILL.md の Step 3 の `--stdin` を使う場面を直す前の一式です。測った153回について、それぞれ最後に検査を呼び出したコマンドを直したあとのスクリプトで動かし直すと、状態の行の `base=` の値のほかは記録と同じ出力になりました（[measurement/README.md](./measurement/README.md)）。

mini の3件を1件ずつ読みました。1件は「1メソッド」を「1つのメソッド」にした文で、本体も3回とも同じ書き換えをしています。意味は変わっていません。1件はコードレビューの2つ目の提案の文末「…見えないようにします」を「…見えないようにしてください」にした文です。書き手の意志の言い方が依頼の言い方に替わっていて、mini の返事は書き手に確かめたい点でこの文末を尋ねています。もう1件は「BFFを1枚挟む」を「BFFの層を1つ挟む」にした文で、意味は変わっていません。本体の4件は「1メソッド」を「1つのメソッド」にした文（3回）と、「業務ロジックの修正を伴う」を「業務ロジックの修正が必要になる」にした文です。

測り方と1件ずつの読みは [measurement/README.md](./measurement/README.md) に、1本ごとの数は [measurement/results.json](./measurement/results.json) にあります。前のバージョンの測定は、mini 1.2.0 のものが [measurement/v2.5.0/README.md](./measurement/v2.5.0/README.md) に、mini 1.1.0 のものが [measurement/v2.4.0/README.md](./measurement/v2.4.0/README.md) に、mini 1.0.0 のものが [measurement/v2.2.2/README.md](./measurement/v2.2.2/README.md) にあります。

## 本体との違い

| | yomiyasu-mini | yomiyasu（本体） |
|---|---|---|
| SKILL.md | 15,215字 | 15,656字（v3.0.0） |
| 参照ファイル | 11本（文書の種類ごとと分野ごとのファイルを、それぞれ1本にまとめた） | 種類ごと、分野ごとに分かれた参照ファイルと、lint が読む語のファイル |
| 検査 | 意味が変わる恐れ（本体の diff と同じ結果） | lint（AIらしい言い回しの候補）、diff、最終稿の照合と記録 |
| 状態の行 | `yomiyasu-mini-check: ran …` | `yomiyasu-check: executed …` |

mini の検査は、本体の diff が出す意味が変わる恐れ（`meaning_risks`）を、本体と同じ結果で出します。本体の `tests/corpus/` の48組と、本体の試験から集めた4,167の入力で、本体 v3.0.0 の `yomiyasu_diff.py` と同じ結果になることを試験で確かめています。

mini には lint がありません。AIらしい言い回しや直訳語と、プロジェクトの語の一覧（`.yomiyasu-words/` の `flag.txt` と `flag-patterns.txt`）の語が残っていないかは、モデルが文を読んで確かめるように SKILL.md で決めています（`allow.txt` の語は直しません）。本体の check の実行の記録（run と verify）もないので、mini の状態の行は本体と別の形にしています。

本体 v3.0.0 では `flag.txt` の1行に `使わない語<TAB>使う語`（`<TAB>` は実際のタブ文字）とも書け、lint がその使う語を指摘に添えます。mini ではモデルが `flag.txt` の行をそのまま読むので、行の形と使う語の扱いを `references/calques.md` の4章に書いています。

## どちらを使えばいいか

本体を読み込める環境なら、本体をおすすめします。

mini は、スキルの大きさに上限があって本体を入れられないときに使ってください。

## 作り直すとき

本体のバージョンが上がったら、次の手順で mini を作り直せます。抽出表 `extract/table.json` と `extract/scripts.json` は本体のファイルの場所と見出し、関数の名前で節を指し、節ごとに中身の sha256 を持っています。生成に使うのは Python 3.9 以上の標準ライブラリだけです。

1. 本体の新しいバージョンのタグを `_main/` に取り出します（下の例は v3.0.0 です）。

   ```bash
   git clone --depth 1 --branch v3.0.0 https://github.com/nanaism/yomiyasu _main
   ```

2. 本体のバージョンが変わったら、`extract/table.json` と `extract/scripts.json` の `source`（tag と commit）を書き直します。`.github/workflows/ci.yml` の `ref` と、試験用の抽出表 `tests/fixtures/basic/extract/table.json` と `scripts.json` の `source` も同じ値にします。中身が変わったときは、mini 自身のバージョン（`version`）も上げてください。上げたときは、`.claude-plugin/plugin.json` と `.claude-plugin/marketplace.json` の `version` も同じ値にします（`tests/test_plugin.py` が確かめます）。
3. 生成します。

   ```bash
   python3 tools/generate.py --source _main
   ```

   - 終了コード 2: 抽出表が指す見出しや関数が本体にない、置き換えの回数が違う、参照が切れている、上限を超えた、などのときに、何も書かずに止まります。抽出表を直します。
   - 終了コード 3: 中身が変わった節を「見直しが要る節」として出し、何も書かずに止まります。その節を読んで部品を見直し、`--accept` を付けて作り直すと、抽出表のハッシュが書き直されます。

4. 試験用の見本を作り直します。`tests/fixtures/basic/extract/` を空のフォルダ（下の例では `fx/`）の `extract/` に写して生成し、できた `fx/skills/` と `fx/MANIFEST.json` を `tests/fixtures/basic/expected/` に、`fx/extract/` の2つの表を `tests/fixtures/basic/extract/` に写し戻します。

   ```bash
   python3 tools/generate.py --source _main --table fx/extract/table.json --out fx --accept
   ```

   ```bash
   python3 tools/build_zip.py --root fx --out fx/fixture.zip
   ```

   2つ目のコマンドが出す sha256 を、`tests/test_zip.py` の `FIXTURE_ZIP_SHA256` に書きます。
5. 確かめます。

   ```bash
   python3 tools/generate.py --source _main --check
   ```

   ```bash
   YOMIYASU_MAIN=_main python3 -m unittest discover -s tests -v
   ```

   - 終了コード 4: `--check` で、リポジトリのファイルが生成物と違います。手順3で作り直します。

`skills/yomiyasu-mini/` と `MANIFEST.json` は生成のスクリプトが書きます。手で直さないでください。

## ライセンス

MIT ライセンスです。本体の yomiyasu と同じです。
