# Personal assistant gateway

This example shows how OpenClaw can act as a personal assistant gateway: it classifies requests into an automatic path, a clarification path, or an approval path.
The approval path uses a local notes file so the reader can see a concrete gated action.
It is self-contained, with workspace state stored inside the example folder so you can reset it without touching anything outside the repo.

## Prerequisites

- OpenClaw installed and able to load a local example folder
- `OPENAI_API_KEY` set in the environment
- OpenClaw configured to allow appending to the local `notes.md` file after approval

## Files to inspect first

- `openclaw.json5`: minimal gateway configuration
- `routing.md`: the routing rules for simple, ambiguous, and risky requests

## Configure OpenClaw

1. Open this folder in OpenClaw as a workspace.
2. Load `openclaw.json5` from the folder root.
3. Confirm the workspace path is created under the example folder's local `.openclaw/` directory.
4. Inspect `notes.md` to see where approved local updates are recorded.

## Run the example

1. Send a short request that should be handled automatically.
2. Send a request that should append a note to `notes.md`.
3. Confirm OpenClaw asks for approval before it acts.

## Success criteria

- Simple requests are handled without extra steps.
- Risky requests stop at an approval gate.
- The routing decision is clear from the README and `routing.md` alone.
