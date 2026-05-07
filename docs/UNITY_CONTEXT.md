# UNITY_CONTEXT

This file summarizes Unity project context.

This is a template. Do not assume any scene, prefab, GameObject, component, or script exists until this file is replaced with real project context.

Do not paste raw `.unity`, `.prefab`, `.asset`, or `.meta` contents here.

## Scenes

### Example: MainScene

Purpose: Main gameplay scene.

Status: Example only. Not configured in this template. Not guaranteed to exist.

Expected objects, if this project uses this scene:

- Player
- Main Camera
- GameManager

## Main GameObjects

### Example: Player

Status: Example only. Replace with actual project object summary.

Expected components, if this project uses this object:

- Rigidbody2D
- Collider2D
- PlayerMovement
- MouseAim2D
- WeaponController, later

## Prefabs

### Example: Player.prefab

Status: Example only. Not guaranteed to exist.

Expected purpose, if this prefab exists:

- Base player prefab.

## Scripts

### Example: PlayerMovement.cs

Purpose: Rigidbody2D-based movement.

Status: Example feature target. Not guaranteed to exist.

## Connection Status

- Scene objects are not connected in this template.
- MCP integration should be done after code implementation.
- Replace this section with actual scene, prefab, component, and SerializedField connection status.

## Safety Notes

- Do not manually edit scene or prefab YAML.
- Use Unity MCP or Unity Editor for object/component connections.
- Check Unity Console after MCP changes.
- Update this file after meaningful scene, prefab, or script structure changes.
- If this file exceeds about 150 lines, split summaries into `SCENE_INDEX.md`, `PREFAB_INDEX.md`, and `SCRIPT_INDEX.md`.
