# CODEMAP

This file helps agents find relevant files without scanning the whole Unity project.

Replace all examples after copying the harness into a real Unity project.

## Rules

- Use this map before searching `Assets/`.
- Prefer exact paths from this file.
- Do not list generated, temporary, or Unity cache folders.
- Keep this file concise. If it grows too large, split by domain.

## Project Roots

```text
Assets/_Project/Scripts/
Assets/_Project/Prefabs/
Assets/_Project/Scenes/
Assets/_Project/Data/
```

## Systems

### Example: Player

Status: Example only. Replace with actual project files.

- Movement: `Assets/_Project/Scripts/Player/PlayerMovement.cs`
- Input: `Assets/_Project/Scripts/Player/PlayerInputReader.cs`

### Example: UI

Status: Example only. Replace with actual project files.

- HUD: `Assets/_Project/Scripts/UI/HudPresenter.cs`

### Example: Data

Status: Example only. Replace with actual project files.

- Weapon data: `Assets/_Project/Scripts/Data/WeaponData.cs`

## Do Not Search Broadly

Do not scan these paths unless explicitly required:

```text
Assets/**
Library/
Temp/
Logs/
ProjectSettings/
Packages/
```

## Notes For Next Agent

- 
