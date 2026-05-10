# AGENTS.md

## CRITICAL Rules

- CRITICAL: Follow `docs/TASK.md` as the source of truth for the current task.
- CRITICAL: Work on one task only.
- CRITICAL: Do not expand scope.
- CRITICAL: Do not modify unrelated files.
- CRITICAL: Do not manually edit `.unity`, `.prefab`, `.asset`, or `.meta` files.
- CRITICAL: Do not edit `ProjectSettings/` or `Packages/`.
- CRITICAL: Code implementation and Unity scene/prefab integration must be separate tasks.
- CRITICAL: Output a plan before editing.
- CRITICAL: Output a final report after editing.

## Context Rules

- Read only the files listed in `docs/TASK.md`.
- Do not scan the entire `Assets/` folder.
- Inspect at most 5 source files per task unless `docs/TASK.md` explicitly allows more.
- If more context is needed, stop and explain why.
- Do not read Unity project-wide state just to orient yourself. Use `docs/UNITY_CONTEXT.md` summaries and task-listed files.

## Agent Roles

- Planner Agent: owns PRD, architecture decisions, feature specs, and `docs/TASK.md`.
- Implementer Agent: changes code or allowed docs only according to `docs/TASK.md`.
- Reviewer Agent: reviews the PR or diff against `docs/TASK.md`, forbidden files, tests, and Unity integration notes.

No separate Unity integration agent is assumed by default. Unity integration may use Unity Editor or another approved tool only when the current task explicitly allows it.

## Agent Context Budgets

- Planner default read: `docs/PRD.md`, `docs/CURRENT.md`, and the relevant feature file if it exists.
- Planner optional read: `docs/ARCHITECTURE.md`, `docs/ADR.md`, or `docs/UNITY_CONTEXT.md` only when the task needs that specific context.
- Implementer default read: `AGENTS.md`, `docs/TASK.md`, and files listed in `docs/TASK.md`.
- Reviewer default read: `AGENTS.md`, `docs/TASK.md`, Codex report, `git status --short`, and the changed-file diff.
- No agent should scan all `Assets/`, all `docs/`, all scenes, all prefabs, or raw Unity YAML for normal work.

## Coding Rules

- Prefer `[SerializeField] private` fields over public fields.
- Keep `MonoBehaviour` responsibilities small.
- Avoid hardcoded gameplay values.
- Use `ScriptableObject` for configurable gameplay data when appropriate.
- Avoid unnecessary singleton patterns.
- Do not create large manager classes unless required by the task.

## Unity Safety Rules

- Scene and prefab changes must be done through Unity Editor or an explicitly approved Unity tool.
- Do not use Apply All on prefabs unless explicitly approved.
- Do not delete GameObjects, prefabs, assets, or scenes unless explicitly approved.
- Check Unity Console after Unity integration changes.

## Done Criteria

A task is complete only when:

- Requirements in `docs/TASK.md` are satisfied.
- Changed files are listed.
- Test method is provided.
- Unity integration needs are reported.
- Documentation update needs are reported.
