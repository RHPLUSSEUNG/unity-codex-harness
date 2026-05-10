# PRD: Unity Codex Harness

## Goal

Create a lightweight Unity project workflow for Codex that reduces context size, limits token use, and keeps AI edits scoped.

## Core Loop

Plan -> Write one `docs/TASK.md` -> Implement with Codex -> Review PR/diff -> Integrate in Unity only when a separate task allows it -> Update concise state -> Commit.

## Core Features

1. Markdown-based project harness.
2. Codex task contract using `docs/TASK.md`.
3. Unity context compression using `docs/UNITY_CONTEXT.md`.
4. Clear separation between code implementation and Unity integration.
5. Three-agent workflow: Planner, Implementer, Reviewer.
6. Review workflow for Codex output.
7. Optional phase plan and guard scripts.

## MVP Scope

- Provide starting Markdown templates.
- Provide prompt templates for planning, Codex implementation, and review.
- Provide a safe workflow for Unity projects.
- Avoid automatic phase execution at the beginning.
- Keep documents short enough to be pasted or attached selectively.

## MVP Exclusions

- No full execute.py automation initially.
- No automatic Unity scene generation.
- No direct `.unity` or `.prefab` YAML editing.
- No ProjectSettings automation.
- No package manager automation.
- No forced TDD requirement for every early prototype task.
- No default MCP agent or MCP prompt.
