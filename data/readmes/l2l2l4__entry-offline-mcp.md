# entry-offline-mcp

[![npm](https://img.shields.io/npm/v/entry-offline-mcp)](https://www.npmjs.com/package/entry-offline-mcp) [![platform-test](https://github.com/l2l2l4/entry-offline-mcp/actions/workflows/platform-test.yml/badge.svg)](https://github.com/l2l2l4/entry-offline-mcp/actions/workflows/platform-test.yml) [![mac-e2e](https://github.com/l2l2l4/entry-offline-mcp/actions/workflows/mac-e2e.yml/badge.svg)](https://github.com/l2l2l4/entry-offline-mcp/actions/workflows/mac-e2e.yml)

**Claude Code, Codex** 같은 AI 에이전트가 내 PC에 설치된 **엔트리 오프라인**(Entry, playentry.org)을 직접 조작해서
**블록코딩 / 엔트리파이썬 작품**을 만들 수 있게 해 주는 MCP 서버입니다.

오브젝트 추가(라이브러리 2천여 개 스프라이트·배경·소리 검색), 직접 그린 이미지 업로드, 엔트리파이썬 → 블록 변환,
블록 JSON 작성, 변수·리스트·신호·함수, 장면, 실행·키 입력·스크린샷으로 테스트, `.ent` 저장/열기까지 지원합니다.
작업은 **실제 엔트리 창에서 실시간으로** 보입니다.

> An MCP server that lets AI agents (Claude, Codex, ...) build Entry (Korean block-coding platform) projects by driving the locally installed Entry offline app (Windows and macOS).

**Quick start** (needs Node.js 22+ and the Entry offline app installed):
```bash
claude mcp add -s user entry -- npx -y entry-offline-mcp          # macOS (terminal)
claude mcp add -s user entry -- cmd /c npx -y entry-offline-mcp   # Windows (cmd)
```
Codex: add `[mcp_servers.entry]` with `command = 'npx'`, `args = ['-y', 'entry-offline-mcp']` to `config.toml` (Windows: `command = 'cmd'`, `args = ['/c', 'npx', '-y', 'entry-offline-mcp']`). Details below (Korean). Tested on Windows 10/11; macOS is verified in CI only; Codex setup is documented but not tested by the author.

## 요구 사항
- Windows 10/11 (실제 테스트 완료)
- macOS: GitHub Actions의 실제 맥(Apple Silicon)에 엔트리 2.1.36을 설치해서 **MCP로 실행 → 작품 생성 → 스크립트 실행 → 스크린샷 → 저장 → 다시 열기**까지 자동 시험을 통과했습니다. 엔트리 맥용 설치 파일이 인텔(x86_64)용이라 Apple Silicon 맥에서는 **Rosetta**가 필요합니다. 사람이 직접 쓰는 실제 맥과 인텔 맥에서는 아직 시험하지 못했습니다.
- 엔트리 오프라인 설치 (playentry.org → 다운로드) (테스트 버전: 2.1.36)
- [Node.js](https://nodejs.org) **22 이상**

## 설치

> 가장 쉬운 방법: Claude Code나 Codex에게 **"https://github.com/l2l2l4/entry-offline-mcp 이 MCP 설치해줘"** 라고 부탁하세요. 설치 후에는 새 대화(세션)를 열어야 엔트리 도구가 보입니다.

npm에 올라가 있어서 패키지 이름(`entry-offline-mcp`)만으로 설치됩니다.

### Claude Code
**macOS (터미널)**
```bash
claude mcp add -s user entry -- npx -y entry-offline-mcp
```
엔트리가 `/Applications/Entry.app`이 아닌 곳에 있으면 `-e ENTRY_PATH="/경로/Entry.app"`을 붙이세요.

**Windows 명령 프롬프트(cmd)**
```bat
claude mcp add -s user entry -- cmd /c npx -y entry-offline-mcp
```
**Windows PowerShell** (`--`를 따옴표로 감싸야 합니다)
```powershell
claude mcp add -s user entry '--' cmd /c npx -y entry-offline-mcp
```
> Git Bash에서는 `/c`가 경로로 바뀌어 버리므로 cmd 또는 PowerShell에서 실행하세요.
> 첫 실행은 다운로드 때문에 시간이 걸릴 수 있습니다. `claude mcp list`에서 `Connected`가 보이면 완료.

제거: `claude mcp remove entry -s user`

> 새 버전이 나왔는데 반영되지 않으면 `entry-offline-mcp@latest`로 지정해서 다시 등록하거나, `npm config get cache`가 알려 주는 폴더 안의 `_npx` 폴더를 지우고 다시 실행하세요.

### Codex (앱 / CLI)
`config.toml`(Windows: `%USERPROFILE%\.codex\config.toml`, macOS: `~/.codex/config.toml`) 맨 끝에 추가하고 Codex를 다시 시작하세요.
```toml
# Windows
[mcp_servers.entry]
command = 'cmd'
args = ['/c', 'npx', '-y', 'entry-offline-mcp']
startup_timeout_sec = 120
```
```toml
# macOS
[mcp_servers.entry]
command = 'npx'
args = ['-y', 'entry-offline-mcp']
startup_timeout_sec = 120
```
> Codex 설정법은 안내만 드리고 직접 시험해 보지는 못했습니다. 안 되면 이슈로 알려 주세요.

### Claude Desktop 등 다른 MCP 클라이언트
(macOS는 `"command": "npx"`, `"args": ["-y", "entry-offline-mcp"]`)
```json
{
  "mcpServers": {
    "entry": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "entry-offline-mcp"]
    }
  }
}
```

### npm을 쓰지 않고 GitHub 주소로 설치
같은 명령에서 `entry-offline-mcp` 자리에 압축 파일(tarball) 주소를 쓰면 GitHub의 최신 `main`을 받습니다.
```bash
claude mcp add -s user entry -- npx -y https://codeload.github.com/l2l2l4/entry-offline-mcp/tar.gz/refs/heads/main
```
> `npx github:l2l2l4/entry-offline-mcp` 형태가 아니라 압축 주소인 이유: Node 22와 함께 오는 npm 10에서는 `npx github:…` 방식이 `GitFetcher requires an Arborist constructor` 오류로 실패합니다(CI에서 확인). 압축 주소 방식은 npm 버전과 상관없이 되고 Git도 필요 없습니다.

### 직접 받아서 쓰기
```bat
git clone https://github.com/l2l2l4/entry-offline-mcp
cd entry-offline-mcp
npm install
claude mcp add -s user entry -- node "%CD%\src\index.js"
```
Codex는 `config.toml`에 `command = 'node'`, `args = ['<받은 폴더>\src\index.js']`로 등록합니다.

> 같은 엔트리 창을 두 에이전트(예: Claude와 Codex)가 **동시에** 조작하면 꼬이므로 한 번에 하나만 사용하세요.

## 사용법
에이전트에게 그냥 부탁하면 됩니다.
- "엔트리로 별 피하기 게임 만들어줘"
- "엔트리파이썬으로 레이캐스팅 3D 미로 만들어줘"
- "방금 만든 작품 실행해서 테스트하고 저장해줘"

에이전트는 먼저 `entry_guide` 도구로 사용 설명서([GUIDE.md](GUIDE.md))를 읽고 작업합니다.

- MCP가 엔트리를 **원격 디버깅 포트를 켠 상태로** 실행해야 조작할 수 있습니다. 엔트리를 직접 켜 둔 상태라면 `entry_launch(restart=true)`로 다시 실행합니다(저장 안 된 작업은 미리 저장하세요).
- 작업하는 동안 엔트리 창을 직접 클릭/편집하면 서로 꼬일 수 있으니 지켜보기만 하세요.
- 처음 실행할 때 작업 폴더 `문서\EntryMCP\`(projects / images / sounds / screenshots / json)를 자동으로 만듭니다.

## 도구 목록
| 분류 | 도구 |
|---|---|
| 시작/상태 | `entry_guide`, `entry_launch`, `entry_status`, `entry_logs` |
| 작품 | `entry_project`(새로/열기/저장/이름/JSON), `entry_get_project`, `entry_scene` |
| 오브젝트 | `entry_search_assets`, `entry_preview_assets`, `entry_add_object`, `entry_update_object`, `entry_object_op`, `entry_object_assets` |
| 코드 | `entry_set_script`(파이썬/블록), `entry_get_script`, `entry_define_function`, `entry_data`, `entry_block_reference`, `entry_set_coding_mode` |
| 실행/검증 | `entry_run`, `entry_input`(키·마우스·대답), `entry_screenshot`, `entry_runtime_state` |
| 고급 | `entry_eval_js` |

## 환경변수 (선택)
| 변수 | 기본값 | 설명 |
|---|---|---|
| `ENTRY_PATH` | 자동 탐색 (Windows `C:\entry\Entry.exe` 등, macOS `/Applications/Entry.app`, `~/Applications/Entry.app`) | 엔트리 실행 파일, 그 폴더, 또는 macOS `.app` 경로 |
| `ENTRY_DEBUG_PORT` | `9333` | 원격 디버깅 포트 |
| `ENTRY_MCP_HOME` | `문서\EntryMCP` | 작업 폴더 |
| `ENTRY_ASAR` | Windows: 엔트리 폴더의 `resources\app.asar`, macOS: `Entry.app/Contents/Resources/app.asar` | 내장 리소스 DB 위치 |

예: `claude mcp add -s user entry -e ENTRY_PATH="D:\Entry\Entry.exe" -- cmd /c npx -y entry-offline-mcp`

## 생성형 AI 사용 표시 (워터마크)
이 MCP로 만들거나 고친 작품에는 생성형 AI가 사용되었다는 표시가 **눈에 띄지 않게** 자동으로 들어갑니다.
1. **숨김 변수**: 작품에 `AI_생성_표시` 변수(무대에 안 보임)가 생기고, 처음·최근 편집 날짜가 기록됩니다.
2. **ID 패턴**: MCP가 만든 블록·오브젝트·변수·리스트·신호·모양의 ID가 보이지 않는 규칙(6글자, 문자 코드 합 % 31 = 7)을 따릅니다. 엔트리가 직접 만드는 ID는 4글자라 겹치지 않고, 저장·불러오기·블록 이동 후에도 유지됩니다.

`entry_status`의 `aiWatermark`에서 표시 여부(`marked`)와 패턴 블록·요소 수를 확인할 수 있습니다.
엔트리파이썬 모드로 바꿨다가 블록으로 돌아오면 엔트리가 블록을 새로 만드는데, MCP가 연결된 엔트리에서는 바뀌기 전 블록과 비교해서 **그대로인 블록에만** 패턴을 다시 붙입니다. 사람이 파이썬으로 새로 쓰거나 고친 블록에는 붙지 않습니다.
(예전 버전이 코드 화면에 붙이던 노란 메모는 이제 만들지 않고, MCP가 코드를 고치거나 저장할 때 자동으로 지웁니다)

> ⚠️ 엔트리 자체 버그: 사용자 함수(특히 반복문 안에서 호출되는 함수)가 있는 작품을 엔트리파이썬 모드로 바꾸면 함수 호출이 `param1` 등으로 잘못 변환되고, 블록 모드로 돌아올 때 그 오브젝트의 코드가 사라질 수 있습니다. `entry_set_coding_mode`는 이런 작품을 미리 검사해서 파이썬 모드 전환을 막습니다. 엔트리 화면에서 직접 바꿀 때도 주의하세요.

## 동작 방식
```
AI 에이전트(Claude Code · Codex 등) ⇄ (MCP, stdio) ⇄ entry-offline-mcp ⇄ (Chrome DevTools Protocol) ⇄ 엔트리 오프라인(Electron)
```
- `src/index.js` MCP 도구 · `src/cdp.js` DevTools 연결 · `src/bridge.js` 엔트리 안에 주입되는 헬퍼 · `src/assets.js` 내장 리소스 검색 · `src/launcher.js` 실행

엔트리 내부 API를 사용하므로 엔트리 버전이 바뀌면 일부 기능이 동작하지 않을 수 있습니다.
엔트리 프로그램/리소스는 포함하지 않으며, 사용자 PC에 설치된 엔트리를 그대로 사용합니다.
이 프로젝트는 엔트리(커넥트재단)와 관련 없는 비공식 프로젝트입니다.

## 라이선스
MIT
