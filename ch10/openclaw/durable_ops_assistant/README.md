# Durable ops assistant

This example shows how OpenClaw can keep operational work moving across time with scheduled tasks, retries, and resume-after-interruption behavior.
The sample files in this folder provide the starter state, and OpenClaw appends runtime state to the seeded `status.md` log plus the local workspace.

## Prerequisites

- OpenClaw installed and able to load a local example folder
- `OPENAI_API_KEY` set in the environment
- OpenClaw configured to run scheduled work for a local workspace

## Files to inspect first

- `openclaw.json5`: minimal runtime defaults for scheduling and durability
- `schedule.md`: the recurring assistant tasks in this example
- `status.md`: the checkpoint log used to verify retries and resumes

## State model

- `status.md` is the visible log you can inspect after each run.
- `./.openclaw/durable-ops` is the checkpointed workspace that survives restarts.
- Completed items stay in place when OpenClaw restarts.

## Configure OpenClaw

1. Open this folder in OpenClaw as a workspace.
2. In OpenClaw, open the Scheduler panel and click `Start` for this workspace.
3. Load `openclaw.json5` from the folder root.
4. Confirm the workspace path is created under the example folder's local `.openclaw/durable-ops` directory.
5. Open `schedule.md` and confirm it is the schedule source for the example.
6. Open `status.md` so you can watch the checkpoint log change during the run.

## Run the example

1. Start the example and let the 08:00 task run, or click `Run` on the 08:00 schedule item if your setup does not wait on the clock.
2. Open the 12:00 schedule item and click `Run` if it is not already active.
3. Confirm `status.md` already contains the seeded failed item `08:05 - incident sync failed once`.
4. Wait until the 12:00 item writes `12:00 - incident sync checkpoint saved`, then stop OpenClaw and restart it with the same workspace. That checkpoint is the interruption point.
5. Reopen the same 12:00 item and choose `Resume`.
6. After the resumed 12:00 run completes, verify `status.md` adds `12:05 - retried incident sync` and leaves the seeded failure line in place.
7. Open the 18:00 item, click `Run`, and confirm `status.md` ends with `18:00 - end-of-day summary sent`.

## Expected result

Before the resumed run:

```text
- 08:00 - reviewed alerts
- 08:05 - incident sync failed once
- 12:00 - incident sync checkpoint saved
```

After the resumed run:

```text
- 08:00 - reviewed alerts
- 08:05 - incident sync failed once
- 12:00 - incident sync checkpoint saved
- 12:05 - retried incident sync
- 18:00 - end-of-day summary sent
```

## Success criteria

- Scheduled work is visible in `schedule.md`.
- Retries do not lose prior progress.
- The README explains how to observe a full schedule, retry, and resume cycle in OpenClaw.

## Cleanup or reset

1. Delete `./.openclaw/durable-ops` if you want to reset the OpenClaw workspace state.
2. Restore `status.md` from git if you want the checkpoint log back in its starter state.
