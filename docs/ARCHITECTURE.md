# ARCHITECTURE

This file is a template. Replace project-specific examples after copying this harness into a real Unity project.

## Harness Architecture

```text
Planner Agent
-> creates specs, breaks work into tasks, chooses context level, writes NEXT_PROMPT.md

Implementer Agent
-> implements code from TASK.md and updates HANDOFF.md

Reviewer Agent
-> reviews PRs, diffs, reports, and updates REVIEW.md / NEXT_PROMPT.md

Unity Guide Writer
-> writes manual Unity Editor integration instructions

User
-> applies scene, prefab, component, and SerializedField changes in Unity Editor

Markdown Harness
-> stores project rules, state, context, task contract, and handoff notes
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
│   ├── HANDOFF.md
│   ├── REVIEW.md
│   ├── NEXT_PROMPT.md
│   ├── CODEMAP.md
│   ├── UNITY_CONTEXT.md
│   ├── INTEGRATION_GUIDE.md
│   ├── DECISIONS_PENDING.md
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
- Manual Unity integration instructions are preferred over direct AI scene manipulation.

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

Code is implemented first.

Scene, prefab, component, and SerializedField integration is described in `docs/INTEGRATION_GUIDE.md` and applied manually by the user in Unity Editor.

Do not manually edit `.unity`, `.prefab`, `.asset`, or `.meta` files to perform integration.

Do not use Unity MCP by default. Treat MCP as an advanced optional workflow outside the default harness path.
