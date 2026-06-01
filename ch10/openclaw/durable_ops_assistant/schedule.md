# Schedule notes

This file is the durable work queue for the example.
`status.md` is the visible checkpoint log, and `./.openclaw/durable-ops` is the workspace that keeps the run state across restarts.

- 08:00 - review overnight alerts and append `08:00 - reviewed alerts` to `status.md`.
- 12:00 - write `12:00 - incident sync checkpoint saved` to `status.md`, then resume after restart and append `12:05 - retried incident sync`.
- 18:00 - send the end-of-day summary and append `18:00 - end-of-day summary sent` to `status.md`.

When a run is interrupted, reopen the workspace and rerun the same scheduled item. Completed steps stay checked off in the saved workspace state, so the assistant resumes from the last checkpoint instead of starting over.
