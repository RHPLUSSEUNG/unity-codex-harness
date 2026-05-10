# Unity Codex Harness

Unity 프로젝트를 Codex로 작업할 때 컨텍스트 창과 토큰 소비를 줄이기 위한 Markdown 하네스 템플릿입니다.

이 저장소는 Unity 프로젝트가 아니라, Unity 프로젝트 루트에 복사해서 쓰는 작업 규칙과 프롬프트 초안입니다.

## 기본 구조

```text
UnityProjectRoot/
├── AGENTS.md
├── docs/
│   ├── TASK.md
│   ├── CURRENT.md
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── ADR.md
│   ├── UNITY_CONTEXT.md
│   └── features/
├── prompts/
├── phases/
└── scripts/guards/
```

## 에이전트

| Agent | 역할 | 주요 입력 |
|---|---|---|
| Planner | 요구사항 정리, 설계, feature spec, `TASK.md` 작성 | `PRD.md`, `CURRENT.md`, 관련 feature 문서 |
| Implementer | `TASK.md`에 허용된 파일만 수정 | `AGENTS.md`, `TASK.md`, 지정 파일 |
| Reviewer | PR/diff 리뷰, 금지 파일 변경 확인, 검증 누락 확인 | `TASK.md`, diff, Codex report |

기본 흐름에는 별도 Unity 통합 에이전트를 두지 않습니다. 통합 작업은 필요할 때만 별도 `TASK.md`로 작성합니다.

## 운영 흐름

```text
1. Planner가 요구사항을 하나의 작업으로 정리한다.
2. Planner가 docs/TASK.md를 작성한다.
3. Implementer가 AGENTS.md와 TASK.md, TASK.md에 지정된 파일만 읽는다.
4. Implementer가 계획을 짧게 보고한 뒤 허용 파일만 수정한다.
5. Reviewer가 diff, 금지 파일, 테스트 방법, Unity 통합 필요 여부를 확인한다.
6. 필요한 경우 Unity 통합을 별도 TASK.md로 만든다.
```

## 문서 역할

- `AGENTS.md`: Codex가 항상 따르는 최상위 규칙.
- `docs/TASK.md`: 현재 수행할 단 하나의 작업 계약서.
- `docs/CURRENT.md`: 최근 상태 요약. 길어지면 분리합니다.
- `docs/PRD.md`: 목표, 범위, MVP 제외 사항.
- `docs/ARCHITECTURE.md`: 구조, 경계, 의존성 방향.
- `docs/ADR.md`: 중요한 결정과 트레이드오프.
- `docs/UNITY_CONTEXT.md`: Scene, Prefab, Script 요약. 원본 YAML을 붙이지 않습니다.
- `docs/features/*`: 기능별 요구사항 초안.
- `prompts/*`: Planner, Implementer, Reviewer용 짧은 프롬프트.

## 컨텍스트 절감 규칙

- Codex는 `docs/TASK.md`의 `Read` 목록만 읽습니다.
- 실제 기능 작업의 `Allowed Files`는 가능하면 1~5개로 제한합니다.
- `docs/**` 전체 허용은 문서 정리 작업에서만 사용합니다.
- `Assets/` 전체 스캔을 금지합니다.
- `.unity`, `.prefab`, `.asset`, `.meta`, `ProjectSettings/`, `Packages/`는 직접 편집하지 않습니다.
- `UNITY_CONTEXT.md`는 요약만 유지하고 150줄을 넘기면 인덱스로 분리합니다.

## 에이전트별 읽기 예산

| Agent | 기본 읽기 | 필요할 때만 읽기 | 금지 |
|---|---|---|---|
| Planner | `PRD.md`, `CURRENT.md`, 관련 feature 문서 | `ARCHITECTURE.md`, `ADR.md`, `UNITY_CONTEXT.md` | 전체 `Assets/`, 전체 `docs/`, raw Unity YAML |
| Implementer | `AGENTS.md`, `TASK.md`, `TASK.md`의 `Read` 파일 | 작업에 필요한 최대 5개 소스 파일 | 전체 프로젝트 스캔 |
| Reviewer | `AGENTS.md`, `TASK.md`, Codex report, diff | Unity Console 결과, 변경 파일 일부 | 변경 없는 Unity 전체 구성 읽기 |

## Unity 통합

코드 구현과 Unity Scene/Prefab 연결은 분리합니다.

Unity 연결이 필요한 경우 새 `docs/TASK.md`에 대상 Scene, GameObject, Prefab, Component, SerializedField를 명시합니다. 연결은 Unity Editor 또는 명시적으로 승인된 Unity 도구로만 수행합니다.

## 프롬프트

- `prompts/planner.md`: 작업 분해와 `TASK.md` 작성용.
- `prompts/codex_task.md`: Codex 구현용.
- `prompts/review.md`: PR/diff 리뷰용.

## Guard

`scripts/guards/`의 스크립트는 나중에 workflow, pre-commit, CI에 연결하기 위한 stub입니다. 현재 저장소를 자동으로 보호하지 않습니다.

## 시작 방법

1. 이 하네스를 Unity 프로젝트 루트에 복사합니다.
2. `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/UNITY_CONTEXT.md`의 템플릿 예시를 실제 프로젝트 정보로 교체합니다.
3. Planner가 첫 기능 문서를 만들고 `docs/TASK.md`를 현재 작업 하나로 교체합니다.
4. Codex에는 `prompts/codex_task.md`를 사용합니다.
