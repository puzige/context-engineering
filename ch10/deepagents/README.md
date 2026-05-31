# DeepAgents

This example demonstrates how to use [DeepAgents](https://github.com/deepagents/deepagents) to orchestrate complex, multi-step tasks. DeepAgents is an orchestration framework designed for long-horizon tasks. It uses a planning layer to decompose requests and a virtual filesystem to manage context overflow.

## Included examples

- [deep_agent_example](./deep_agent_example/README.md) - the chapter 7-style orchestration anchor
- [filesystem_context](./filesystem_context/README.md) - filesystem-backed context and memory
- [subagent_delegation](./subagent_delegation/README.md) - delegated work with isolated subagents
- [human_approval](./human_approval/README.md) - interrupt-based approval for sensitive tool calls