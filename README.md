# Unity Codex Harness

Unity 프로젝트에서 GPT Project, Codex, Unity MCP를 함께 사용할 때의 하네스 구조입니다.

목표는 단순합니다.

```text
GPT Project = 설계, 작업 분해, 리뷰
Codex = 코드 구현
Unity MCP = 씬, 프리팹, 컴포넌트 연결
Markdown Harness = 규칙, 상태, 작업 계약서
```

이 README는 저장소 대문 가이드입니다. 처음 보는 사람은 이 파일만 읽어도 전체 구조와 운영 방식을 이해할 수 있어야 합니다.

---

## 1. 핵심 원칙

```text
문서는 너무 줄이지 않는다.
실행은 너무 자동화하지 않는다.
Codex는 TASK.md의 현재 작업 하나만 수행한다.
Unity 씬/프리팹 작업은 코드 구현 이후 MCP 작업으로 분리한다.
```

Claude식 하네스의 핵심은 `docs`, `CLAUDE.md`, 실행 엔진, hooks입니다. 이 프로젝트에서는 Unity + Codex 환경에 맞게 다음처럼 변환합니다.

```text
CLAUDE.md       -> AGENTS.md
/harness        -> GPT Project의 Orchestrator 역할
/review         -> GPT Project의 Reviewer 역할
execute.py      -> 초기에는 사용하지 않음
hooks           -> 필요 시 scripts/guards로 도입
```

Unity는 코드 외에도 Scene, Prefab, Asset, Meta, ProjectSettings가 얽혀 있으므로, Phase 자동 실행보다 `TASK.md` 단위 수동 승인 흐름이 안전합니다.

---

## 2. 최종 하네스 구조

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
│   ├── UNITY_CONTEXT.md
│   └── features/
│       ├── 001_PlayerMovement.md
│       ├── 002_MouseAim.md
│       └── 003_WeaponSystem.md
│
├── prompts/
│   ├── codex_task.md
│   ├── mcp_task.md
│   └── review.md
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

처음부터 전부 완성할 필요는 없습니다. 시작 시점에는 아래 파일만 있어도 충분합니다.

```text
AGENTS.md
docs/PRD.md
docs/ARCHITECTURE.md
docs/ADR.md
docs/CURRENT.md
docs/TASK.md
docs/UNITY_CONTEXT.md
docs/features/001_FirstFeature.md
```

---

## 3. 에이전트 구성

초기에는 3개면 충분합니다.

| Agent | 역할 | 사용 위치 |
|---|---|---|
| GPT Project | Orchestrator, Planner, Reviewer, Documenter | ChatGPT Project |
| Codex Implementer | C# 코드 작성, 파일 수정, 결과 보고 | Codex |
| Unity MCP Integrator | Scene, Prefab, Component, SerializedField 연결 | Codex + Unity MCP |

확장 기준:

```text
테스트가 많아짐       -> Test Agent 추가
리팩터링이 반복됨     -> Refactor Agent 추가
문서 불일치가 잦아짐  -> Documenter Agent 분리
```

---

## 4. 문서별 역할

### AGENTS.md

Codex와 MCP가 따르는 최상위 규칙입니다.

포함 내용:

```text
- CRITICAL 규칙
- 작업 전 Plan 제출
- 작업 후 Report 제출
- TASK.md 하나만 수행
- 관련 없는 파일 수정 금지
- .unity / .prefab / .asset / .meta 직접 수정 금지
- ProjectSettings 수정 금지
- 코드 구현과 Unity 연결 분리
```

### docs/PRD.md

무엇을 만들고, 무엇을 만들지 않을지 정의합니다.

중요 항목:

```text
Goal
Core Loop
Core Features
MVP Exclusions
```

특히 `MVP Exclusions`는 중요합니다. 안 만들 것을 명시하지 않으면 AI가 스코프를 계속 늘릴 수 있습니다.

### docs/ARCHITECTURE.md

어떻게 만들지 정의합니다.

포함 내용:

```text
- 폴더 구조
- 시스템 경계
- 의존성 방향
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

80~120줄을 넘기면 `FEATURE_TRACKER.md`, `CHANGELOG.md`로 분리합니다.

### docs/TASK.md

Codex가 지금 수행할 단일 작업 계약서입니다.

반드시 포함:

```text
Task ID
Goal
Read
Allowed Files
Forbidden Files
Requirements
Out of Scope
Done Criteria
Required Report
```

중요 규칙:

```text
TASK.md에는 현재 작업 하나만 둔다.
여러 작업을 넣지 않는다.
```

### docs/UNITY_CONTEXT.md

Unity Scene, Prefab, Script 요약입니다.

포함 내용:

```text
Scenes
Main GameObjects
Prefabs
Scripts
Connection Status
Safety Notes
```

원칙:

```text
.unity, .prefab 원문을 붙이지 않는다.
요약만 쓴다.
150줄을 넘으면 SCENE_INDEX.md / PREFAB_INDEX.md / SCRIPT_INDEX.md로 분리한다.
```

---

## 5. 운영 워크플로우

```text
1. 사용자 요구 입력
2. GPT Project가 요구사항 정리
3. PRD / ARCHITECTURE / ADR 확인
4. Feature 문서 작성 또는 갱신
5. GPT Project가 TASK.md 작성
6. Codex가 TASK.md 기준으로 Plan 제출
7. 사용자가 Plan 확인
8. Codex가 코드 구현
9. Codex가 결과 보고
10. GPT Project가 리뷰
11. 필요 시 MCP 작업으로 Unity 연결
12. CURRENT.md / UNITY_CONTEXT.md 갱신
13. Git 커밋
```

---

## 6. Codex 실행 원칙

Codex에게는 항상 다음 원칙을 적용합니다.

```text
Read AGENTS.md and docs/TASK.md first.
Perform only the current task.
Do not scan the whole project.
Do not modify scene, prefab, asset, meta, ProjectSettings, or Packages files.
Before editing, output a plan.
After editing, output the required report.
```

Codex 기본 읽기:

```text
AGENTS.md
docs/TASK.md
docs/CURRENT.md
docs/ARCHITECTURE.md
docs/features/관련기능.md
```

필요할 때만 읽기:

```text
docs/PRD.md
docs/ADR.md
docs/UNITY_CONTEXT.md
```

읽으면 안 되는 것:

```text
docs 전체
Assets 전체
*.unity
*.prefab
*.asset
*.meta
ProjectSettings/*
Packages/*
```

---

## 7. MCP 실행 원칙

MCP는 구현자가 아니라 Unity 연결자입니다.

나쁜 지시:

```text
MCP로 무기 시스템 만들어줘.
```

좋은 지시:

```text
Codex가 WeaponController.cs를 작성한다.
GPT가 리뷰한다.
MCP가 Player에 WeaponController를 연결한다.
MCP가 FirePoint를 연결한다.
Console을 확인한다.
```

MCP 작업은 항상 코드 구현 이후 별도 Task로 분리합니다.

---

## 8. Phase와 자동 실행

`phases/MVP.md`는 장기 계획입니다.

```text
phases/MVP.md = 장기 로드맵
docs/TASK.md = 실제 Codex 실행 단위
```

중요 규칙:

```text
Codex는 phases를 직접 실행하지 않는다.
GPT Project가 phases에서 TASK.md를 하나씩 만든다.
Codex는 TASK.md 하나만 실행한다.
```

`execute.py` 기반 자동 실행은 Unity 프로젝트 초기에는 사용하지 않습니다. 자동 실행은 guard, Git checkpoint, Unity Console 검사 루틴이 갖춰진 후 도입합니다.

---

## 9. Guard 도입 기준

초기에는 문서 규칙과 Git 체크포인트로 충분합니다. 위험이 커지면 아래 guard를 도입합니다.

```text
dangerous_cmd_guard.py
unity_yaml_guard.py
circuit_breaker.py
```

### dangerous_cmd_guard.py

차단 대상:

```text
rm -rf
git reset --hard
git clean -fd
git push --force
del /s
rmdir /s
```

### unity_yaml_guard.py

차단 대상:

```text
*.unity
*.prefab
*.asset
*.meta
ProjectSettings/*
Packages/*
```

### circuit_breaker.py

감지 대상:

```text
같은 컴파일 에러 반복
같은 Unity Console 에러 반복
같은 파일 반복 수정
같은 실패 패턴 반복
```

---

## 10. 최종 규칙 요약

```text
1. PRD에는 반드시 MVP 제외 사항을 쓴다.
2. ARCHITECTURE는 짧게 유지한다.
3. ADR에는 선택과 포기한 대안을 기록한다.
4. TASK.md에는 현재 작업 하나만 둔다.
5. Codex는 TASK.md 중심으로 작업한다.
6. Codex는 작업 전 Plan을 제출한다.
7. Codex는 코드만 구현한다.
8. Unity 연결은 MCP 작업으로 분리한다.
9. GPT Project가 Codex 결과를 리뷰한다.
10. 자동 execute.py는 Unity 안정화 전까지 사용하지 않는다.
```

핵심 결론:

```text
문서는 PRD / ARCHITECTURE / ADR 수준까지는 분리한다.
실행은 TASK.md 하나로 제한한다.
Unity 자동화는 execute.py보다 MCP 분리 실행을 우선한다.
```
