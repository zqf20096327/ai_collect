# Synapse Enforcer — for LEET Language Understanding

**로컬 LLM의 사고(thinking) 모드로 LEET 언어이해 수준의 고난도 지문·문항 세트를 컴파일하는 파이프라인.**
입력 팩트시트(Claude 생성 — [정직 고지](#정직-고지-한계)) → 지문 생성(2콜) → 문항 레인(문항당 통합 1콜) →
결정론 게이트(코드 감사·세트 탐지·표적 수리) → 검수 시트까지, 사람 검수자가 세부 사항만 검수하면 되는 형태로
세트를 조립함을 목표로 한다. 또한 이 프로젝트는 현재까지는 **언어이해 전용**이다.

> **English abstract** — Synapse Enforcer is a thinking-native pipeline that compiles
> high-difficulty Korean reading-comprehension item sets at the level of LEET
> (Legal Education Eligibility Test) *Language Understanding*, using a local LLM
> (Gemma4-31B-it, thinking mode) plus deterministic gates. It contributes (1) a
> codified **killer-item design grammar** — the *lexical inverse-correlation*
> principle (hard truths wear unfamiliar words, hard falsehoods wear the passage's
> own words), three hard-truth skeletons (transitive / cross-isomorphic / condensing),
> and four swap variants with polarity-riding discipline; (2) an empirical
> **judgment-ceiling** result: a 31B model *generates* steelman readings 6/6 but
> *adjudicates* them 0/6, so generation and verification must be separated; and
> (3) a same-harness **three-model benchmark** (local 31B / local 250B-MoE /
> frontier API) showing that set-level discipline leaks from every model and is
> recovered by the gate chain, i.e., the harness transmits model capability
> rather than bottlenecking it. Every run is seeded by a **fact sheet** — dry fact
> bullets, attributions, misattribution warnings, and an item plan — which was
> drafted with Claude and then fixed as the run's input; the passages and items
> themselves come from the pipeline's own model, with a human as the final gate.
> All exemplar passages and items are original works by the author.
> Verified on 2× RTX PRO 6000 (2×96 GB).

**Author** — Donghwi Seo (독립 연구; killingzerg@hotmail.com) · License Apache-2.0

---

## 핵심 주장 넷

1. **사고-네이티브 파이프라인.** 비사고 모델 시대의 다단 파이프라인(~50콜)은 "사고의 외재화"다.
   사고 모드에서는 스테이지를 사고 내부로 접는다: 지문 = 초안+관계 그래프 동시 1콜 → 다듬기 1콜
   (+코드 백스톱·재앵커링), 문항 = 계층 지침(L1 불변 계약 / L2 설계 문법 / L3 실물 / L4 스키마)의
   **통합 1콜**. 세트 전체 ~10콜, 로컬 31B로 약 7분.

2. **킬러 문항 설계 문법.** 기출 킬러의 공통 기제를 닫힌 문법으로 코드화했다.
   - **어휘 역상관**: 어려운 참의 표면은 지문에서 멀게(재개념화된 새 명명·무앵커),
     어려운 거짓의 표면은 지문에 바싹(실재 어휘의 한 끗 바꿔치기) — "가까운 어휘 = 참"
     휴리스틱을 양방향에서 처벌한다.
   - **참의 정본 3골격**: ⒜ 전이(서로 다른 문단의 연쇄로만 나오는 결론) ⒝ 교차 동형성(서두 축의
     재활성화로 먼 쌍을 동류화) ⒞ 응집(이중 지위·새 명명 아래로만 모이는 진술).
   - **바꿔치기 4변종**: 인접 개념 치환 · 관계의 결 교체 · 조사/통사 재배열 · 동일어 층위 이동 —
     규율: 앵커 전부 실재(거짓은 접합부 하나), 극성 편승, 오류는 명사구 안, 정면 반전 전면 금지.
   - 발문 극성에 따라 두 문법이 정답 자리를 **교대**한다.

3. **판정 상한과 검증 분리.** 통제 실험에서 31B는 각 선지의 반대-역할 최선 독해(스틸맨)를
   6/6 **생성**하지만, 그 독해가 지문에 봉쇄되는지는 6/6 **오판**한다 — 트랩이 요구하는 판별
   해상도와 모델의 판정 해상도가 같아서 자가 감사가 구조적으로 불가능하다. 그래서 생성과
   판정을 분리한다: 열거는 모델, **판정은 사람**(스틸맨 시트 O/X, 문항당 1~2분). 대형 모델
   판정 자동화는 정확(실측 5/5)하나 로컬 서빙에선 느려(38분/문항) 야간 배치 전용이다.

4. **게이트가 지배 변수.** 동일 하네스에 3모델(로컬 31B / 로컬 250B-MoE / 프런티어 API)을
   꽂아 본 결과 — 어떤 모델도 세트 규율(정답 번호 분포·축 중복·답 유출·오답 현저성)은 통짜
   생성에서 새고, 결정론 게이트(축 배분+슬롯 강제 → 코드 린트 → 세트 탐지 → 표적 수리)가
   이를 회수한다. **하네스는 모델 능력을 투과한다**: 더 강한 모델을 꽂으면 더 강한 세트가 나온다.

## 3모델 벤치마크 (요약 — 상세는 [docs/BENCHMARK.md](docs/BENCHMARK.md))

| 모델 | 경로 | 세트 시간 | 정답 결함 | 한 줄 평 |
|---|---|---|---|---|
| Gemma4-31B-it (로컬 vLLM) | 조립 v0 | 411초 | 1 (게이트가 검출) | 기준선 — 본선 모델 |
| Solar-Open2-250B (로컬 MoE) | 통합 런* | ~53분 | 복수정답 1 외 | 판정력↑·실행력 결함 — 실격 |
| Claude Opus 5 (API, thinking high) | 조립 v0 | 701초 | **0** | 천장 참조선 — 정답 골격이 사람 실물급 |

\* Solar는 조립 v0 이전의 통합 스크립트 조건 — 완전 동일 조건 비교는 Gemma↔Opus.

## 저장소 구조

```
application/            웹 UI + 엔진 (표준 라이브러리만 사용 — 외부 의존성 0)
  engine/generate.py      클래식 다단 + 사고-네이티브(--think-native) 지문 경로, 게이트·규칙 전부
  engine/to_hwpx.py       한글(HWPX) 조판 출력
  app.py 외               로컬 웹 UI (ThreadingHTTPServer + SSE)
native/                 조립 v0 — 사고-네이티브 문항 세트 오케스트레이터 (대표작)
  native_set.py           축 배분 → 3레인 병렬 → 린트 → 세트 탐지 → 표적 수리 → 스틸맨 시트
  nq_modules.py           L1/L2-COMMON/유형 코어(이해·추론·보기)/L3 — 킬러 문법 정본
  set_to_hwpx.py          세트 산출(json) → 한글(HWPX) 조판
  serve_native.py         웹 러너 — 브라우저에서 실행·열람·HWPX 내려받기
examples/               자작 킬러 실물 4종(해설 포함)·생성 지문·생성 세트 2종(31B/frontier)
docs/                   방법론·벤치마크
serving/                vLLM 서빙 스크립트 (Gemma4-31B-it, 사고 모드 기본)
```

## 빠른 시작

요구: Python 3.10+ (엔진은 표준 라이브러리만 사용), vLLM 서버 1대 (검증 환경: 2× RTX PRO 6000, 2×96 GB).

```bash
# 1) Gemma4-31B-it 서빙 (사고 모드 기본 켬)
bash serving/serve_gemma4_31b_it_vllm.sh
```

```bash
# 2) 문항 세트 생성 — 예시 지문 동봉이라 바로 실행 가능
python3 native/native_set.py
# → native/runs/native_set_v0.md (문항 + 설계 노트 + 스틸맨 검수 시트 + 게이트 요약)
```

```bash
# 3) 지문부터 새로 (사고-네이티브 2콜) → 그 지문으로 세트
python3 application/engine/generate.py application/engine/knowledge_vagueness_endicott.json \
  --think-native --stop-after passage --out my_passage
LEET_PASSAGE_DIR=$(pwd)/my_passage LEET_LADDER_TAG=my1 python3 native/native_set.py
```

```bash
# 4) 웹 러너 — 브라우저에서 조립 v0 실행·시트 열람·HWPX 내려받기
python3 native/serve_native.py --port 8977
```

```bash
# 5) 세트를 한글(HWPX)로 조판 (CLI) / 클래식 파이프라인 웹 UI
python3 native/set_to_hwpx.py native/runs/native_set_v0.json
cd application && python3 app.py --port 8899
```

다른 OpenAI 호환 서버(프록시 포함)로 돌리려면: `LEET_BASE_URL`·`LEET_MODEL` 환경변수.
사고형 API 모델은 `LEET_REQ_KW='{"reasoning_effort":"high","temperature":1}'` 식으로 요청 파라미터를 덮어쓸 수 있다.

## 정직 고지 (한계)

- **사람 검수가 최종 게이트다.** 이 파이프라인은 "검수자가 빠르게 판정할 수 있는 상태"까지를
  자동화하며, 무검수 출제를 주장하지 않는다 (판정 상한 실험이 그 이유다).
- 벤치마크는 1런 표본이며, API 모델은 사고 모드 제약으로 temperature=1 고정이었다.
- **입력 팩트시트는 Claude로 생성했다.** 파이프라인의 입력물인 팩트시트(`knowledge.json`의 사실
  불릿·귀속·오귀속 경고·출제 지시)는 Claude로 작성해 투입했다 — 산출물의 상류에 다른 모델이 한 번
  개입하므로 밝힌다. 사실 오류의 가능성은 지문·문항 단계뿐 아니라 이 입력 단계에도 있고, 그 판정
  역시 사람 검수의 몫이다. 벤치마크의 3모델 비교는 팩트시트가 아니라 그 아래 구간(같은 지문·같은
  모듈에서 생성 모델만 교체)이며, 표의 Claude Opus 5 행은 팩트시트 작성과 무관한 별도 조건이다.
- 예시 지문·문항·해설은 전부 저자의 자작이다. 이 프로젝트는 법학전문대학원협의회 및 LEET
  시험 주관 기관과 무관하다.

## 인용

```bibtex
@software{seo2026synapseenforcer,
  author = {Seo, Donghwi},
  title  = {Synapse Enforcer: a thinking-native compiler for LEET Language Understanding killer items},
  year   = {2026},
  url    = {https://github.com/Glockevonpavlov/synapse-enforcer-leet}
}
```
