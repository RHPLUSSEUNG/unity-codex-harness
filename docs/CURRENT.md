# CURRENT

## Completed

- Initial harness guide created.
- AGENTS.md created.
- Core docs created.
- Managed context workflow defined.
- Manual Unity integration is the default workflow.
- Session-separated agent roles are defined.
- Handoff templates are available.

## In Progress

- Unity Codex Harness template setup.

## Known Issues

- No project-specific Unity scene context yet.
- No actual Unity project files are included in this harness repository.
- Guard scripts are stubs and are not wired into local workflow, pre-commit, Codex wrapper, or CI.

## Next

1. Copy this harness into a Unity project repository.
2. Send `prompts/project_setup.md` to GPT Project.
3. Fill `docs/PRD.md` with the actual game or app concept.
4. Fill `docs/ARCHITECTURE.md` with the actual project structure.
5. Fill `docs/CODEMAP.md` with exact source paths.
6. Fill `docs/UNITY_CONTEXT.md` with scene, prefab, GameObject, component, and script summaries.
7. Create the first feature spec in `docs/features/`.
8. Replace `docs/TASK.md` with the first real Planner or Implementer task.
9. Use `docs/NEXT_PROMPT.md` to start the next agent session.

## Do Not Touch

- `ProjectSettings/` unless explicitly approved.
- `Packages/` unless explicitly approved.
- `.unity`, `.prefab`, `.asset`, `.meta` files through direct text editing.
- `Assets/` broadly unless exact paths are listed in `docs/TASK.md`.

## Recent Changes

- Refocused the harness from MCP-by-default to Manual Unity Integration.
- Added Planner, Implementer, Reviewer, and Unity Guide Writer roles.
- Added Markdown handoff documents for session-separated workflows.
