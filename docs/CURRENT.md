# CURRENT

## Completed

- Initial harness guide created.
- AGENTS.md created.
- Core docs created.
- Managed context workflow defined.
- Manual Unity integration is the default workflow.
- Session-separated agent roles are defined.
- `HANDOFF.md` is the central handoff and next-prompt document.

## In Progress

- Unity Codex Harness template setup.

## Known Issues

- No project-specific Unity scene context yet.
- No actual Unity project files are included in this harness repository.
- Guard scripts are stubs and are not wired into local workflow, pre-commit, Codex wrapper, or CI.

## Next

1. Copy this harness into a Unity project repository.
2. Send `prompts/project_setup.md` to GPT Project.
3. Fill required setup docs:
   - `docs/PRD.md`
   - `docs/ARCHITECTURE.md`
   - `docs/CURRENT.md`
   - `docs/TASK.md`
   - `docs/HANDOFF.md`
   - `docs/CODEMAP.md`
   - `docs/features/001_FirstFeature.md`
4. Fill optional docs only when needed:
   - `docs/UNITY_CONTEXT.md`
   - `docs/INTEGRATION_GUIDE.md`
   - `docs/REVIEW.md`
   - `docs/DECISIONS_PENDING.md`
   - `docs/ADR.md`
5. Replace `docs/TASK.md` with the first real Planner or Implementer task.
6. Use `docs/HANDOFF.md` / Next Agent Prompt to start the next agent session.

## Do Not Touch

- `ProjectSettings/` unless explicitly approved.
- `Packages/` unless explicitly approved.
- `.unity`, `.prefab`, `.asset`, `.meta` files through direct text editing.
- `Assets/` broadly unless exact paths are listed in `docs/TASK.md`.

## Recent Changes

- Refocused the harness from MCP-by-default to Manual Unity Integration.
- Added Planner, Implementer, Reviewer, and Unity Guide Writer roles.
- Reduced default required docs and moved next-agent prompts into `HANDOFF.md`.
