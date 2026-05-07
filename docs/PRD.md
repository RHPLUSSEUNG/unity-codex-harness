# PRD: Unity Codex Harness Project

## Goal

Create a Unity project workflow that uses GPT Project, Codex, Unity MCP, and Markdown harness documents to improve AI-assisted development quality.

## Core Loop

Plan with GPT Project -> Implement with Codex -> Review with GPT Project -> Integrate with Unity MCP -> Update Markdown state -> Commit.

## Core Features

1. Markdown-based project harness.
2. Codex task contract using `docs/TASK.md`.
3. Unity context compression using `docs/UNITY_CONTEXT.md`.
4. Clear separation between code implementation and Unity integration.
5. Review workflow for Codex output.
6. Optional phase plan and guard scripts.

## MVP Scope

- Provide starting Markdown templates.
- Provide prompt templates for Codex, MCP, and review.
- Provide a safe workflow for Unity projects.
- Avoid automatic phase execution at the beginning.

## MVP Exclusions

- No full execute.py automation initially.
- No automatic Unity scene generation.
- No direct `.unity` or `.prefab` YAML editing.
- No ProjectSettings automation.
- No package manager automation.
- No forced TDD requirement for every early prototype task.
