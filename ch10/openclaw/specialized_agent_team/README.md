# Specialized agent team

This example shows a small OpenClaw team with one lead agent and two specialists. It demonstrates how a shared project memory file keeps the team aligned while each role stays focused on a narrow job.
It teaches how OpenClaw can keep a routing lead, a researcher, and a writer synchronized through shared memory and a clear handoff.

## Prerequisites

- OpenClaw installed and able to load a local example folder
- `ANTHROPIC_API_KEY` set in the environment

## Files to inspect first

- `openclaw.json5`: team defaults, role mapping, and shared memory location
- `lead.md`, `researcher.md`, `writer.md`: the role prompts for each agent
- `project-notes.md`: shared project memory that every role can read and update
- `lead-handoff.md`: the lead's latest summary for the writer

During a run, OpenClaw updates `project-notes.md` and `lead-handoff.md`; treat them as mutable working files.

## Configure OpenClaw

1. Open this folder in OpenClaw as a workspace.
2. Load `openclaw.json5` from the folder root.
3. Confirm the workspace path is created under the folder's local `.openclaw/specialized-team` directory.
4. Confirm `project-notes.md` is used as the shared memory file for the team.
5. Confirm `lead-handoff.md` is the latest lead summary the writer will read.

## Run the example

1. Ask for a three-bullet note explaining why the team uses a lead, a researcher, and a writer.
2. Expect the lead to route the work, the researcher to gather the reasons, and the writer to turn the handoff into the final response.
3. Check `project-notes.md` to see the current task and the final note the team shared.
4. Check `lead-handoff.md` to see the summary the writer consumed.
5. Verify that the lead populated `lead-handoff.md` before the writer produced the final three bullets.

Expected result:

```text
Input: "Write a three-bullet note explaining why the team uses a lead, a researcher, and a writer."
- The lead keeps the task focused and routes it to the right specialist.
- The researcher captures the key points and constraints in shared notes.
- The writer turns the lead handoff into the final three-bullet note.
```

## Success criteria

- The lead owns routing and prepares the handoff.
- The researcher produces concise findings.
- The writer turns the lead's handoff into a clean final response.
- The shared project memory file keeps the whole team aligned.

## Cleanup or reset

1. Delete `./.openclaw/specialized-team` if you want to reset the OpenClaw workspace state.
2. Restore `project-notes.md` and `lead-handoff.md` from git if you want to return the sample files to their starter content.
