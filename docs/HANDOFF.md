# HANDOFF

This file is the minimal handoff document for the next agent session.

Do not use this as a passive changelog. Keep it actionable and short enough for the next agent to read first.

This file also replaces a separate NEXT_PROMPT.md. Put the next copy-paste-ready prompt in the final section below.

## Current Feature

- Feature:
- Task ID:
- Branch / PR:

## Last Agent

Planner / Implementer / Reviewer / Unity Guide Writer

## What Changed

- 

## Why It Changed

- 

## Files Changed

- 

## Files To Read Next

The next agent should start with only these files unless more context is required:

- AGENTS.md
- docs/TASK.md
- docs/HANDOFF.md

Add task-specific files here:

- 

## Known Risks

- 

## Verification Status

- Not verified yet.

## Manual Unity Integration Needed

Yes / No

If yes, summarize what the user must do in Unity Editor:

- 

## Documentation Updates Needed

- 

## Next Recommended Agent

Planner / Implementer / Reviewer / Unity Guide Writer

## Next Agent Prompt

Keep this section copy-paste ready for the user.

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
7. Update docs/HANDOFF.md or docs/REVIEW.md if allowed by docs/TASK.md
```
