# NEXT PROMPT

This file tells the user what to send to the next agent session.

Keep it copy-paste ready.

## Send This To

Planner / Implementer / Reviewer / Unity Guide Writer

## Prompt

```text
You are the [Planner / Implementer / Reviewer / Unity Guide Writer] Agent for this Unity project.

Read first:
- AGENTS.md
- docs/TASK.md
- docs/HANDOFF.md

Additional files to read:
- [Add only the files needed for this task]

Context Level:
- [Level 0 / Level 1 / Level 2 / Level 3 / Level 4]

Task:
[Write one clear task.]

Constraints:
- Do not expand scope.
- Do not scan the whole project.
- Do not modify Unity scene, prefab, asset, meta, ProjectSettings, Packages, or Input Actions files unless docs/TASK.md explicitly allows it.
- Use manual Unity integration instructions by default.

Required output:
1. Plan before editing or reviewing
2. Result summary
3. Changed files or reviewed files
4. Verification method
5. Manual Unity integration needed
6. Documentation updates needed
7. Update docs/HANDOFF.md, docs/REVIEW.md, or docs/NEXT_PROMPT.md if allowed by docs/TASK.md
```

## Notes For User

- Start a new session when switching agent roles.
- Paste only the prompt above plus any PR or diff context required by the task.
- Do not ask the Implementer to fix unrelated review comments in the same task.
