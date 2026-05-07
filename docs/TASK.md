# TASK

## Task ID

Harness-Setup-01

## Goal

Use this repository as a starting template for Unity + Codex + GPT Project + MCP harness engineering.

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

- Keep the harness concise.
- Keep `TASK.md` focused on one task only.
- Use `PRD.md` to define scope and MVP exclusions.
- Use `ARCHITECTURE.md` to define structure and boundaries.
- Use `ADR.md` to record decisions and tradeoffs.
- Use `UNITY_CONTEXT.md` as a summary, not raw Unity YAML.

## Out of Scope

- Do not automate phase execution yet.
- Do not generate Unity scene or prefab files.
- Do not modify Unity project settings.

## Done Criteria

- Harness documents exist.
- README explains how to use them.
- Prompts are available for Codex, MCP, and review.
- Guard script stubs are available for later extension.

## Required Report

After each task, report:

1. Changed files
2. Summary
3. Test or verification method
4. Unity integration needed
5. Documentation updates needed
