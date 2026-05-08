# TASK

## Task ID

Harness-Setup-02

## Agent Role

Planner / Implementer / Reviewer / Unity Guide Writer

Use exactly one role for each real task.

## Context Level

Level 1 - Normal harness setup

For real work, choose one:

```text
Level 0 - Tiny fix
Level 1 - Normal feature
Level 2 - Architecture-impacting feature
Level 3 - Manual Unity integration
Level 4 - Review / refactor
```

## Goal

Use this repository as a starting template for Unity + Codex + GPT Project harness engineering with managed context, session-separated agents, and Markdown handoff.

## Template Warning

This `TASK.md` is for harness setup only.

For real Unity feature work:

- Replace this file with the current feature task.
- Keep one task only.
- Choose one `Agent Role`.
- Choose one `Context Level`.
- Narrow `Allowed Files` to 1-5 files when possible.
- Do not use `docs/**` unless the task is documentation-only.
- Do not allow Unity scene, prefab, asset, meta, ProjectSettings, Packages, or Input Actions changes unless explicitly required and reviewed.
- Use `Manual Instructions Only` for Unity integration by default.
- Split `Read` into required and optional files so agents do not read every harness document by default.

## Read

### Required

- AGENTS.md
- docs/TASK.md
- docs/CURRENT.md
- docs/HANDOFF.md
- docs/CODEMAP.md
- docs/PRD.md
- docs/ARCHITECTURE.md
- docs/features/001_FirstFeature.md

### Optional, only if relevant

- docs/REVIEW.md
- docs/UNITY_CONTEXT.md
- docs/INTEGRATION_GUIDE.md
- docs/DECISIONS_PENDING.md

## Allowed Files

- AGENTS.md
- README.md
- docs/**
- prompts/**
- phases/**
- scripts/guards/**

## Forbidden Files

- `*.unity`
- `*.prefab`
- `*.asset`
- `*.meta`
- `ProjectSettings/*`
- `Packages/*`
- `Assets/**`

## Requirements

- Keep the harness concise.
- Define managed context rather than minimum context.
- Remove Unity MCP from the default workflow.
- Use manual Unity integration instructions by default.
- Define Planner, Implementer, Reviewer, and Unity Guide Writer roles.
- Use Markdown files as minimal handoff documents between separate agent sessions.
- Use `HANDOFF.md` as an actionable handoff, not a passive log.
- Store the next copy-paste-ready agent prompt in `HANDOFF.md`.
- Use `CODEMAP.md` to reduce broad source searching.
- Treat `REVIEW.md`, `INTEGRATION_GUIDE.md`, `UNITY_CONTEXT.md`, and `DECISIONS_PENDING.md` as optional unless the current task requires them.
- Mark template examples clearly so Codex does not assume they exist in the real Unity project.

## Out of Scope

- Do not automate phase execution yet.
- Do not generate Unity scene or prefab files.
- Do not modify Unity project settings.
- Do not use Unity MCP as the default integration path.
- Do not implement a real Unity feature in this setup task.

## Unity Integration Mode

Manual Instructions Only

AI agents must not directly modify Unity scenes, prefabs, assets, meta files, ProjectSettings, Packages, or Input Actions by default.

## Done Criteria

- Harness documents exist.
- README explains managed context and manual Unity integration.
- README explains new Unity project setup.
- README explains session-separated agent workflow.
- README distinguishes Core docs from Optional docs.
- Prompts are available for project setup, planning, implementation, review, and manual Unity integration.
- `HANDOFF.md` is the single next-prompt handoff location.
- Guard script stubs remain available for later extension.
- Template warnings are clear.

## Handoff Output Required

After each task, update `docs/HANDOFF.md` when documentation updates are allowed.

Include:

1. Last agent
2. What changed
3. Why it changed
4. Files changed
5. Files to read next
6. Known risks
7. Verification status
8. Next recommended agent
9. Next agent prompt

## Required Report

After each task, report:

1. Changed files
2. Summary
3. Test or verification method
4. Manual Unity integration needed
5. Documentation updates needed
6. Suggested next agent
