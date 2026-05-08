# Unity Codex Harness

Unity 프로젝트에서 GPT Project와 Codex를 함께 사용할 때의 **Managed Context Harness**입니다.

이 저장소는 Unity 프로젝트 자체가 아니라, **새 Unity 프로젝트 루트에 복사해서 사용하는 Markdown Harness 템플릿**입니다.

권장 위치:

```text
UnityProjectRoot/
├── Assets/
├── Packages/
├── ProjectSettings/
├── AGENTS.md
├── docs/
├── prompts/
├── phases/
└── scripts/
```

## 목표

```text
Planner Agent      = 설계, 기능 분해, TASK 작성
Implementer Agent  = TASK 기준 코드 구현
Reviewer Agent     = PR / diff / report 리뷰
User               = Unity Editor에서 씬, 프리팹, SerializedField 수동 반영
Markdown Harness   = 규칙, 상태, 작업 계약서, 인수인계서
```

이 하네스의 목표는 context를 무조건 최소화하는 것이 아닙니다.

목표는 **코드 품질에 필요한 context는 유지하고, Unity 프로젝트 전체를 무분별하게 읽지 않게 하는 것**입니다.

```text
Too much context  -> 느림, 비쌈, task focus 붕괴
Too little context -> 아키텍처 위반, 중복 시스템, 낮은 코드 품질
Managed context   -> task 위험도에 맞는 충분한 context
```

---

## 1. 핵심 원칙

```text
문서는 너무 줄이지 않는다.
실행은 너무 자동화하지 않는다.
Codex는 TASK.md의 현재 작업 하나만 수행한다.
Unity 씬/프리팹은 기본적으로 AI가 직접 수정하지 않는다.
Unity 반영은 사용자에게 Manual Integration Guide로 제공한다.
에이전트 간 인수인계는 Markdown 문서로 남긴다.
```

이 하네스는 고수준 자동 멀티 에이전트 시스템이 아닙니다.

대신 서로 다른 ChatGPT / Codex 세션에서 다음 역할을 수동으로 분리합니다.

```text
Planner session     -> TASK.md, feature spec, NEXT_PROMPT.md 작성
Implementer session -> 코드 변경, HANDOFF.md 갱신
Reviewer session    -> PR 리뷰, REVIEW.md, NEXT_PROMPT.md 갱신
Unity user action   -> Editor에서 수동 반영, INTEGRATION_GUIDE.md 참고
```

---

## 2. 왜 MCP를 기본값에서 제외하는가

Unity MCP는 유용할 수 있지만, 이 하네스의 기본 흐름에서는 제외합니다.

이유:

```text
- 씬 / 프리팹 상태를 읽고 조작하려면 context가 커진다.
- Unity Editor hierarchy, components, SerializedField 상태 확인에 토큰이 많이 든다.
- 자동 씬 수정 결과를 다시 검증해야 하므로 왕복 비용이 커진다.
- 씬 / 프리팹 / asset 변경은 코드 변경보다 복구가 어렵다.
```

기본 원칙:

```text
AI는 Unity 씬, 프리팹, asset, meta, ProjectSettings를 직접 수정하지 않는다.
AI는 사용자가 Unity Editor에서 반영할 수 있는 수동 절차를 작성한다.
사용자는 Editor에서 직접 반영한다.
반영 결과만 UNITY_CONTEXT.md와 INTEGRATION_GUIDE.md에 요약한다.
```

MCP를 꼭 써야 하는 경우에는 별도 advanced workflow로 다루고, 기본 템플릿에는 포함하지 않습니다.

---

## 3. 최종 하네스 구조

```text
project/
├── AGENTS.md
│
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── ADR.md
│   ├── CURRENT.md
│   ├── TASK.md
│   ├── HANDOFF.md
│   ├── REVIEW.md
│   ├── NEXT_PROMPT.md
│   ├── CODEMAP.md
│   ├── UNITY_CONTEXT.md
│   ├── INTEGRATION_GUIDE.md
│   ├── DECISIONS_PENDING.md
│   └── features/
│       └── 001_FirstFeature.md
│
├── prompts/
│   ├── project_setup.md
│   ├── planner.md
│   ├── implementer.md
│   ├── reviewer.md
│   └── unity_manual_integration.md
│
├── phases/
│   └── MVP.md
│
└── scripts/
    └── guards/
        ├── dangerous_cmd_guard.py
        ├── unity_yaml_guard.py
        └── circuit_breaker.py
```

처음에는 아래 파일만 채워도 충분합니다.

```text
AGENTS.md
docs/PRD.md
docs/ARCHITECTURE.md
docs/CURRENT.md
docs/TASK.md
docs/HANDOFF.md
docs/NEXT_PROMPT.md
docs/CODEMAP.md
docs/UNITY_CONTEXT.md
docs/INTEGRATION_GUIDE.md
docs/features/001_FirstFeature.md
```

---

## 4. Context Levels

작업별 위험도에 따라 context 양을 다르게 사용합니다.

| Level | Use Case | Read |
|---|---|---|
| Level 0 | Tiny fix | `AGENTS.md`, `docs/TASK.md`, target file |
| Level 1 | Normal feature | `AGENTS.md`, `docs/TASK.md`, `docs/CURRENT.md`, relevant `ARCHITECTURE.md` section, feature spec, 2-5 source files |
| Level 2 | Architecture-impacting feature | `AGENTS.md`, `docs/TASK.md`, `docs/CURRENT.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, feature spec, 5-10 source files |
| Level 3 | Manual Unity integration | `AGENTS.md`, `docs/TASK.md`, `docs/CURRENT.md`, `docs/UNITY_CONTEXT.md`, `docs/INTEGRATION_GUIDE.md`, changed file list |
| Level 4 | Review / refactor | `AGENTS.md`, `docs/TASK.md`, `docs/HANDOFF.md`, `docs/REVIEW.md`, PR diff, changed files |

원칙:

```text
Do not always use the smallest context.
Use the smallest context that preserves correctness.
```

---

## 5. 문서별 역할

### AGENTS.md

모든 세션이 따르는 최상위 규칙입니다.

포함 내용:

```text
- Managed context rules
- One task only
- No scope expansion
- No Unity scene / prefab / asset direct edits
- Manual Unity integration by default
- Handoff required after each agent task
```

### docs/PRD.md

무엇을 만들고, 무엇을 만들지 않을지 정의합니다.

중요 항목:

```text
Goal
Core Loop
Core Features
MVP Exclusions
Target Platform
Non-goals
```

### docs/ARCHITECTURE.md

어떻게 만들지 정의합니다.

포함 내용:

```text
- 실제 폴더 구조
- 시스템 경계
- 의존성 방향
- 네이밍 규칙
- Scene / Prefab 처리 원칙
- ScriptableObject 사용 기준
```

### docs/ADR.md

왜 그렇게 결정했는지 기록합니다.

형식:

```text
Decision: 무엇을 선택했는가
Why: 왜 선택했는가
Tradeoff: 무엇을 포기했는가
```

### docs/CURRENT.md

현재 프로젝트 상태판입니다.

포함 내용:

```text
Completed
In Progress
Known Issues
Next
Do Not Touch
Recent Changes
```

### docs/TASK.md

현재 agent가 수행할 단일 작업 계약서입니다.

반드시 포함:

```text
Task ID
Agent Role
Context Level
Goal
Read
Allowed Files
Forbidden Files
Requirements
Out of Scope
Unity Integration Mode
Done Criteria
Handoff Output Required
```

중요 규칙:

```text
TASK.md에는 현재 작업 하나만 둔다.
여러 작업을 넣지 않는다.
Allowed Files는 가능한 1-5개 수준으로 좁힌다.
docs/** 같은 넓은 범위는 문서 정리 작업에서만 사용한다.
```

### docs/HANDOFF.md

단순 로그가 아니라 **다음 세션을 위한 최소 인수인계서**입니다.

포함 내용:

```text
Current Feature
Last Agent
What Changed
Why It Changed
Files Changed
Files To Read Next
Known Risks
Verification Status
Next Recommended Agent
Next Agent Instructions
```

### docs/REVIEW.md

Reviewer Agent가 PR / diff / report를 검토한 결과를 남기는 문서입니다.

포함 내용:

```text
Verdict
Scope Check
Problems
Required Fixes
Suggested Prompt For Implementer
Documentation Updates Needed
```

### docs/NEXT_PROMPT.md

사용자가 다음 세션에 그대로 복사해 넣을 prompt입니다.

```text
Send this to: Planner / Implementer / Reviewer / Unity Guide Writer
Prompt body
Required files to read
Expected output
```

### docs/CODEMAP.md

Codex가 파일을 찾느라 `Assets/` 전체를 검색하지 않도록 돕는 index입니다.

```text
System -> key files
Feature -> related files
Do-not-search-broadly notes
```

### docs/UNITY_CONTEXT.md

Unity scene, prefab, GameObject, script 상태 요약입니다.

원칙:

```text
.unity, .prefab, .asset, .meta 원문을 붙이지 않는다.
요약만 쓴다.
150줄을 넘으면 SCENE_INDEX.md / PREFAB_INDEX.md / SCRIPT_INDEX.md로 분리한다.
```

### docs/INTEGRATION_GUIDE.md

사용자가 Unity Editor에서 직접 반영할 수동 절차를 기록합니다.

포함 내용:

```text
Target scene or prefab
GameObjects to select
Components to add
SerializedFields to assign
Inspector values to set
PlayMode verification steps
Console checks
```

### docs/DECISIONS_PENDING.md

Planner 또는 사용자가 결정해야 하는 미해결 질문을 모읍니다.

---

## 6. 새 Unity 프로젝트 세팅 방법

### Step 1. Harness 복사

이 저장소의 파일을 Unity 프로젝트 루트로 복사합니다.

```text
UnityProjectRoot/
├── AGENTS.md
├── docs/
├── prompts/
├── phases/
└── scripts/
```

`Assets/` 안에 넣지 않는 것을 권장합니다.

### Step 2. GPT Project에 setup 요청

`prompts/project_setup.md` 내용을 GPT Project에 보냅니다.

GPT는 구현 코드를 작성하지 않고 다음 문서를 프로젝트에 맞게 채워야 합니다.

```text
docs/PRD.md
docs/ARCHITECTURE.md
docs/CURRENT.md
docs/UNITY_CONTEXT.md
docs/CODEMAP.md
docs/INTEGRATION_GUIDE.md
docs/features/001_FirstFeature.md
docs/TASK.md
docs/NEXT_PROMPT.md
```

### Step 3. 템플릿 예시 교체

Player / Weapon / Enemy 같은 예시는 실제 프로젝트 truth가 아닙니다.

실제 프로젝트 구조, scene, prefab, script 상태로 교체합니다.

### Step 4. 첫 feature spec 작성

```text
docs/features/001_FirstRealFeature.md
```

포함 항목:

```text
Purpose
Requirements
Related Files
Forbidden Changes
Manual Unity Integration Needed
Done Criteria
```

### Step 5. TASK.md 교체

`docs/TASK.md`는 항상 현재 작업 하나만 담습니다.

### Step 6. NEXT_PROMPT.md를 다음 agent에게 전달

예:

```text
Planner가 NEXT_PROMPT.md 작성
-> 사용자가 새 Codex 세션에 Implementer prompt 전달
-> Implementer가 코드 구현 후 HANDOFF.md 갱신
-> 사용자가 Reviewer 세션에 REVIEW prompt 전달
```

---

## 7. 운영 워크플로우

```text
1. User gives high-level request
2. Planner Agent updates feature spec and TASK.md
3. Planner Agent writes docs/NEXT_PROMPT.md for Implementer
4. User starts a new session with Implementer Agent
5. Implementer reads TASK.md + HANDOFF.md + required files
6. Implementer changes code only
7. Implementer updates HANDOFF.md
8. User opens PR
9. Reviewer Agent reviews PR / diff / HANDOFF.md
10. Reviewer updates REVIEW.md
11. Reviewer writes NEXT_PROMPT.md for Implementer or Planner
12. If Unity scene/prefab work is needed, Unity Guide Writer writes manual editor steps
13. User applies Unity Editor changes manually
14. User updates or asks GPT to update UNITY_CONTEXT.md summary
15. Planner prepares next TASK.md
```

---

## 8. Agent prompts

| Prompt | Use |
|---|---|
| `prompts/project_setup.md` | 새 Unity 프로젝트에 harness 적용 |
| `prompts/planner.md` | 설계, feature 분해, TASK 작성 |
| `prompts/implementer.md` | 코드 구현 |
| `prompts/reviewer.md` | PR / diff 리뷰 |
| `prompts/unity_manual_integration.md` | Unity Editor 수동 반영 절차 작성 |

---

## 9. Guard 도입 기준

초기에는 문서 규칙과 Git 체크포인트로 충분합니다.

위험이 커지면 아래 guard를 workflow, pre-commit hook, Codex wrapper, CI 검사에 연결합니다.

```text
scripts/guards/dangerous_cmd_guard.py
scripts/guards/unity_yaml_guard.py
scripts/guards/circuit_breaker.py
```

주의:

```text
현재 guard 스크립트는 stub입니다.
로컬 workflow, pre-commit hook, Codex wrapper, CI 검사에 직접 연결하지 않으면 저장소를 자동으로 보호하지 않습니다.
```

---

## 10. 요약

이 하네스는 다음을 지향합니다.

```text
Minimum context가 아니라 Managed context
MCP 기본 사용이 아니라 Manual Unity Integration
단일 로그가 아니라 Markdown Handoff
자동 멀티에이전트가 아니라 세션 분리형 역할 분담
전체 repo 스캔이 아니라 TASK.md 기반 작업 계약
```
