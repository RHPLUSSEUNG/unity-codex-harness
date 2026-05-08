# AGENTS.md

## CRITICAL Rules

- CRITICAL: Follow `docs/TASK.md` as the source of truth for the current task.
- CRITICAL: Work on one task only.
- CRITICAL: Do not expand scope.
- CRITICAL: Do not modify unrelated files.
- CRITICAL: Do not manually edit `.unity`, `.prefab`, `.asset`, or `.meta` files.
- CRITICAL: Do not edit `ProjectSettings/`, `Packages/`, or Input Actions unless explicitly allowed in `docs/TASK.md`.
- CRITICAL: Do not use Unity MCP by default.
- CRITICAL: Unity scene, prefab, component, and SerializedField changes are manual user actions by default.
- CRITICAL: Output a plan before editing.
- CRITICAL: Output a final report after editing.
- CRITICAL: Update `docs/HANDOFF.md` after each agent task when the task allows documentation updates.

## Managed Context Rules

- Do not always use the smallest context.
- Use the smallest context that preserves correctness.
- Follow the `Context Level` in `docs/TASK.md`.
- Do not read all docs files.
- Do not scan the entire `Assets/` folder.
- Prefer exact file paths from `docs/TASK.md`, `docs/CODEMAP.md`, and `docs/HANDOFF.md`.
- Inspect at most 5 source files for Level 0-1 tasks unless `docs/TASK.md` explicitly allows more.
- If more context is needed, stop before editing and explain exactly which file is needed and why.

## Agent Roles

### Planner Agent

- Defines feature scope and requirements.
- Updates feature specs and `docs/TASK.md`.
- Chooses the context level.
- Writes `docs/NEXT_PROMPT.md` for the next agent.
- Does not implement code unless the task explicitly says so.

### Implementer Agent

- Implements code according to `docs/TASK.md`.
- Modifies only files listed under `Allowed Files`.
- Reports changed files, verification steps, risks, and manual Unity integration needs.
- Updates `docs/HANDOFF.md` when allowed.

### Reviewer Agent

- Reviews PRs, diffs, reports, and handoff notes.
- Checks scope, architecture fit, forbidden file changes, over-engineering, and missing verification.
- Updates `docs/REVIEW.md`.
- Writes `docs/NEXT_PROMPT.md` for the next Implementer or Planner.

### Unity Guide Writer

- Does not modify Unity files or use MCP by default.
- Writes manual Unity Editor instructions for the user.
- Updates `docs/INTEGRATION_GUIDE.md` when allowed.

## Coding Rules

- Prefer `[SerializeField] private` fields over public fields.
- Keep `MonoBehaviour` responsibilities small.
- Avoid hardcoded gameplay values.
- Use `ScriptableObject` for configurable gameplay data when appropriate.
- Avoid unnecessary singleton patterns.
- Do not create large manager classes unless required by the task.
- Prefer project conventions from `docs/ARCHITECTURE.md` and `docs/CODEMAP.md`.

## Unity Safety Rules

- Do not manually edit `.unity`, `.prefab`, `.asset`, or `.meta` files.
- Do not modify scenes, prefabs, assets, ProjectSettings, Packages, or Input Actions unless explicitly allowed.
- Do not use Unity MCP by default.
- For Unity scene or prefab integration, write manual Unity Editor instructions for the user.
- The user applies scene, prefab, component, and SerializedField changes manually in Unity Editor.
- After the user applies changes, summarize the result in `docs/UNITY_CONTEXT.md` when requested.
- Check Unity Console after manual integration and record the result in `docs/INTEGRATION_GUIDE.md` or `docs/HANDOFF.md`.

## Done Criteria

A task is complete only when:

- Requirements in `docs/TASK.md` are satisfied.
- Changed files are listed.
- Test or verification method is provided.
- Manual Unity integration needs are reported.
- Documentation update needs are reported.
- `docs/HANDOFF.md`, `docs/REVIEW.md`, or `docs/NEXT_PROMPT.md` is updated when required by the task.
