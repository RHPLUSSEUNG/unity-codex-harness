# ADR

Architecture Decision Records.

Format:

```text
Decision: What was selected?
Why: Why was it selected?
Tradeoff: What was given up?
```

---

## ADR-001: Use TASK.md as the single execution contract

Decision:
Codex executes only the current task described in `docs/TASK.md`.

Why:
Unity projects have many risky files. A single execution contract reduces scope creep and accidental changes.

Tradeoff:
Longer workflows require the Planner Agent to create tasks one by one.

---

## ADR-002: Separate code implementation from Unity integration

Decision:
C# implementation and Scene/Prefab integration are separate tasks.

Why:
Unity scene and prefab changes are riskier than normal code changes.

Tradeoff:
A feature may require two passes: code first, manual Unity Editor integration second.

---

## ADR-003: Do not use execute.py automation initially

Decision:
Phase auto-execution is not used at the beginning.

Why:
Unity projects can be damaged by automated scene, prefab, asset, meta, or ProjectSettings changes.

Tradeoff:
The user must manually approve each task until guards and validation are mature.

---

## ADR-004: Use Manual Unity Integration by default

Decision:
AI agents do not use Unity MCP or directly modify Unity scenes, prefabs, assets, meta files, ProjectSettings, Packages, or Input Actions by default.

Instead, agents write manual Unity Editor instructions in `docs/INTEGRATION_GUIDE.md`.

Why:
Reading and modifying Unity scene or prefab state can consume large context and token budgets. Manual instructions keep the AI workflow focused on code and reduce the need to inspect large Unity YAML or Editor state.

Tradeoff:
The user must apply scene, prefab, component, and SerializedField changes manually in Unity Editor.

---

## ADR-005: Use Markdown handoff between separate agent sessions

Decision:
Planner, Implementer, Reviewer, and Unity Guide Writer work in separate sessions and pass minimal state through `docs/HANDOFF.md`, `docs/REVIEW.md`, and `docs/NEXT_PROMPT.md`.

Why:
Separate sessions reduce prompt bloat and keep each agent focused. Markdown handoff lets the next agent read only the context needed for the next task.

Tradeoff:
The user must keep handoff documents current and copy the correct prompt into the next agent session.
