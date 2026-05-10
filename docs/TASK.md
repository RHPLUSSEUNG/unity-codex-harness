# TASK

## Task ID

Harness-Setup-01

## Goal

Restructure this repository as a concise Unity + Codex harness template optimized for small context windows and low token use.

## Template Warning

This `TASK.md` is for harness setup only.

For real Unity feature work:

- Replace this file with the current feature task.
- Keep one task only.
- Narrow `Allowed Files` to 1-5 files when possible.
- Do not use `docs/**` unless the task is documentation-only.
- Do not allow Unity scene, prefab, asset, meta, ProjectSettings, Packages, or Input Actions changes unless explicitly required and reviewed.

## Read

- AGENTS.md
- docs/CURRENT.md
- docs/PRD.md
- docs/ARCHITECTURE.md
- docs/ADR.md
- docs/UNITY_CONTEXT.md
- docs/features/001_FirstFeature.md

## Allowed Files

- AGENTS.md
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

## Requirements

- Center the workflow on three agents: Planner, Implementer, and Reviewer.
- Define per-agent context budgets so agents do not read the full Unity project by default.
- Remove the default MCP-agent workflow and MCP prompt because it is token-heavy.
- Keep Unity integration as a separate task type that can use Unity Editor or another approved tool only when explicitly allowed.
- Keep the harness concise.
- Keep `TASK.md` focused on one task only.
- Use `PRD.md` to define scope and MVP exclusions.
- Use `ARCHITECTURE.md` to define structure and boundaries.
- Use `ADR.md` to record decisions and tradeoffs.
- Use `UNITY_CONTEXT.md` as a short summary, not raw Unity YAML.
- Mark template examples clearly so Codex does not assume they exist in the real Unity project.

## Out of Scope

- Do not automate phase execution yet.
- Do not generate Unity scene or prefab files.
- Do not modify Unity project settings.
- Do not implement Unity integration in this documentation task.

## Done Criteria

- Harness documents exist.
- README explains how to use them.
- Prompts are available for Planner, Codex implementation, and review.
- Guard script stubs are available for later extension.
- Template warnings are clear.

## Required Report

After each task, report:

1. Changed files
2. Summary
3. Test or verification method
4. Unity integration needed
5. Documentation updates needed
