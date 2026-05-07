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
Longer workflows require GPT Project to create tasks one by one.

---

## ADR-002: Separate code implementation from Unity integration

Decision:
C# implementation and Scene/Prefab integration are separate tasks.

Why:
Unity scene and prefab changes are riskier than normal code changes.

Tradeoff:
A feature may require two passes: code first, MCP or Unity Editor integration second.

---

## ADR-003: Do not use execute.py automation initially

Decision:
Phase auto-execution is not used at the beginning.

Why:
Unity projects can be damaged by automated scene, prefab, asset, meta, or ProjectSettings changes.

Tradeoff:
The user must manually approve each task until guards and validation are mature.
