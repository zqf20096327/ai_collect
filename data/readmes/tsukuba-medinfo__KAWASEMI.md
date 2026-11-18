<p align="center"><img src="kawasemi/web/static/img/kawasemi.png" alt="KAWASEMI" width="140"></p>

# KAWASEMI

[English](README-en.md) | **日本語**

**K**nowledge-**A**ided **W**orkflow for **A**I-assisted **S**tructured **E**HR **M**apping & **I**nput

KAWASEMI は、病院のデータから症例登録の様式（FHIR の Questionnaire / QuestionnaireResponse）を
埋める作業を支援するシステムです。JASPEHR Implementation Guide への準拠を目指しています
（完全な準拠は表明していません。[docs/jaspehr_compliance.md](docs/jaspehr_compliance.md)）。

様式は手入力もできます。**データ自動収集（AI モード）** では、各項目の取得方法の設計をローカル LLM
（Ollama または vLLM）が支援します。設計する内容は次の 4 つです。

1. 項目の臨床的な意味
2. データが、その施設のシステムのどこにあるか（所在）
3. 自然言語で書いた取得の手順書
4. 手順書から変換した、実行できる DSL

人が確認して確定した DSL を、データベース、ファイル、FHIR サーバー、CSV に対して実行します。
AI が書くのは下書きで、確定するのは人です。実行した値には、根拠（読んだ文書、SQL、LLM のプロンプト）が残ります。
施設のネットワークの内側で完結するよう設計しており、LLM もローカルで動かします。

> **状態：研究用ソフトウェアです。** KAWASEMI は医療機器ではなく、臨床上の意思決定に使ってはいけません。
> 無保証で提供します（[LICENSE](LICENSE) を参照）。
> 患者データを、issue、プルリクエスト、テストの入力データに書かないでください。

## はじめに

| ガイド | 内容 |
|---|---|
| [QUICKSTART.md](QUICKSTART.md) | ローカル起動・手動入力の基本操作 |
| [QUICKSTART_AI.md](QUICKSTART_AI.md) | データ自動収集（AI モード）を起動して動かすまで |
| [docs/ai_mode_guide.md](docs/ai_mode_guide.md) | データ自動収集（AI モード）のアーキテクチャ・各ステップの操作 |
| [docs/e2e_guide.md](docs/e2e_guide.md) | 自己完結のデモ（架空の様式とダミーデータで工程を通す E2E 試験環境） |
| [docs/dsl_specification.md](docs/dsl_specification.md) | DSL の仕様（構造・op・実行意味論・検証・再現性と監査。正本） |
| [DEVELOPMENT.md](DEVELOPMENT.md) | 開発環境の構築・コードスタイル・マイグレーション |
| [docs/development_flow.md](docs/development_flow.md) | 開発の流れと検証手順 |

DSL の機械可読なステップスキーマは [docs/schemas/dsl_step.schema.json](docs/schemas/dsl_step.schema.json) です。

## クイックスタート

```bash
uv sync --all-packages --all-groups --all-extras
cp .env.example .env
# SECRET_KEY と CSRF_SECRET_KEY が必須です（それぞれ 32 文字以上、異なる値）。
# 空のままだと、どのコマンドも設定の検証エラーで止まります。
uv run python -c "import secrets; [print(f'{k}=\"{secrets.token_urlsafe(32)}\"') for k in ('SECRET_KEY', 'CSRF_SECRET_KEY')]" >> .env
uv run alembic upgrade head   # データベースのスキーマを作る（必ず必要）
make e2e                      # 架空データで、決定的に動く E2E 試験（LLM は不要）
uv run kawasemi serve         # Web UI：http://localhost:8000/
```

シェルの環境に `SECRET_KEY` / `CSRF_SECRET_KEY` がない場合、`make test` と `make e2e` は試験用のキーを渡します。
そのため、`.env` を埋める前でも実行できます。

施設で使うには、`site.example/` を `site/` にコピーし（または `SITE_DIR` で指す）、接続先の登録、
キーの種類、データ定義書を記入します。

## リポジトリの構成

| パス | 内容 |
|---|---|
| `kawasemi/` | Web アプリケーション（FastAPI）、DSL のコンパイラと実行器 |
| `indexer/` | `kawasemi-indexer`：施設のデータ定義書を対象にした検索索引の作成（uv workspace のメンバー） |
| `examples/e2e/` | 架空の自己完結シナリオ。E2E 試験とデモで使う |
| `site.example/` | 施設固有の設定のひな型 |
| `site/` | 施設固有のデータと設定（git の管理外。別の非公開リポジトリで管理する） |
| `var/` | 生成物：索引ファイル、出力（git の管理外） |
| `CONTRACT.md` | indexer と Web アプリの間のデータ契約 |

## その他

- 残作業は、このリポジトリの GitHub Issues で管理しています。
- 脆弱性の報告は [SECURITY.md](SECURITY.md) に従ってください。
- 同梱している第三者のコードは [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) に記載しています。

## ライセンス

[Apache License 2.0](LICENSE)（帰属表示は [NOTICE](NOTICE)）
