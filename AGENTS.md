# AGENTS.md

## CRITICAL Rules

- CRITICAL: Follow `docs/TASK.md` as the source of truth for the current task.
- CRITICAL: Work on one task only.
- CRITICAL: Do not expand scope.
- CRITICAL: Do not modify unrelated files.
- CRITICAL: Do not manually edit `.unity`, `.prefab`, `.asset`, or `.meta` files.
- CRITICAL: Do not edit `ProjectSettings/` or `Packages/`.
- CRITICAL: Code implementation and Unity integration must be separate tasks.
- CRITICAL: Output a plan before editing.
- CRITICAL: Output a final report after editing.

## Context Rules

- Do not read all docs files.
- Do not scan the entire `Assets/` folder.
- Read only the files listed in `docs/TASK.md`.
- Inspect at most 5 source files per task.
- If more context is needed, stop and explain why.

## Coding Rules

- Prefer `[SerializeField] private` fields over public fields.
- Keep `MonoBehaviour` responsibilities small.
- Avoid hardcoded gameplay values.
- Use `ScriptableObject` for configurable gameplay data when appropriate.
- Avoid unnecessary singleton patterns.
- Do not create large manager classes unless required by the task.

## Unity Safety Rules

- Scene and prefab changes must be done through Unity MCP or Unity Editor.
- Do not use Apply All on prefabs unless explicitly approved.
- Do not delete GameObjects, prefabs, assets, or scenes unless explicitly approved.
- Check Unity Console after MCP changes.

## Done Criteria

A task is complete only when:

- Requirements in `docs/TASK.md` are satisfied.
- Changed files are listed.
- Test method is provided.
- Unity integration needs are reported.
- Documentation update needs are reported.
