# ARCHITECTURE

This file is a template. Replace project-specific examples after copying this harness into a real Unity project.

## Harness Architecture

```text
GPT Project
-> creates specs, tasks, reviews

Codex
-> implements code from TASK.md

Unity MCP
-> connects scene, prefab, component, serialized fields

Markdown Harness
-> stores project rules, state, context, and task contract
```

## Folder Structure

```text
project/
├── AGENTS.md
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── ADR.md
│   ├── CURRENT.md
│   ├── TASK.md
│   ├── UNITY_CONTEXT.md
│   └── features/
├── prompts/
├── phases/
└── scripts/guards/
```

## Unity Project Folder Rules

Default recommendation:

```text
Assets/_Project/Scripts/
Assets/_Project/Prefabs/
Assets/_Project/Scenes/
Assets/_Project/Data/
Assets/_Project/Art/
Assets/_Project/Audio/
```

Adjust this structure if the project already has a different convention.

## System Boundaries

Template example only. Do not assume these systems exist until the real project architecture is written.

Example for a top-down shooter:

- Player scripts handle player-only behavior.
- Weapon scripts handle weapon data, firing, and projectile creation.
- Enemy scripts handle enemy behavior.
- UI scripts must not contain gameplay rules.
- Scene and prefab wiring must be separated from C# implementation.

## Dependency Direction

Template example only:

```text
UI -> Game State read-only
Player -> Weapon
Weapon -> Projectile
Enemy -> Damage System
```

Replace this dependency map with the actual project dependency direction.

## Unity Integration Rule

Code is implemented first. Scene and prefab integration happens later through Unity MCP or manual Unity Editor work.

Do not manually edit `.unity`, `.prefab`, `.asset`, or `.meta` files to perform integration.
