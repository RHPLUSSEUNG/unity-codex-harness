# UNITY_CONTEXT

This file summarizes Unity project context. Do not paste raw `.unity`, `.prefab`, `.asset`, or `.meta` contents here.

## Scenes

### MainScene

Purpose: Main gameplay scene.

Status: Not configured in this template.

Expected objects:

- Player
- Main Camera
- GameManager

## Main GameObjects

### Player

Status: Project-specific.

Expected components:

- Rigidbody2D
- Collider2D
- PlayerMovement
- MouseAim2D
- WeaponController, later

## Prefabs

### Player.prefab

Status: Project-specific.

Expected purpose:

- Base player prefab.

## Scripts

### PlayerMovement.cs

Purpose: Rigidbody2D-based movement.

Status: Example feature target.

## Connection Status

- Scene objects are not connected in this template.
- MCP integration should be done after code implementation.

## Safety Notes

- Do not manually edit scene or prefab YAML.
- Use Unity MCP or Unity Editor for object/component connections.
- Check Unity Console after MCP changes.
- Update this file after meaningful scene, prefab, or script structure changes.
