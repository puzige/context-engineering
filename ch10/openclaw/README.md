# OpenClaw examples

These examples show OpenClaw as an assistant gateway: it routes messages, coordinates specialized agents, and keeps longer-running work recoverable.
Each folder is self-contained so you can inspect the config, read the supporting notes, and run one scenario without pulling in the others.

## Requirements

- An OpenClaw installation that can load a local folder containing `openclaw.json5`
- The API key required by the example you want to run; each example README lists its provider

## Examples

- [`personal_assistant_gateway/`](./personal_assistant_gateway/): Channel routing, local tool access, and approval gates.
- [`specialized_agent_team/`](./specialized_agent_team/): Lead plus specialist agents with shared project memory.
- [`durable_ops_assistant/`](./durable_ops_assistant/): Scheduling, retries, and resume-after-interruption behavior.

## How to use these examples

1. Open the example folder you want to explore.
2. Read its `README.md` first.
3. Inspect the config and support files referenced in that README.
4. In OpenClaw, open the folder as a workspace and load the `openclaw.json5` file from the folder root.
