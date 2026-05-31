# Orchestration with DeepAgents

This example demonstrates how to use [DeepAgents](https://github.com/deepagents/deepagents) to orchestrate complex, multi-step tasks. DeepAgents is an orchestration framework designed for long-horizon tasks. It uses a planning layer to decompose requests and a virtual filesystem to manage context overflow.

The key features of this example include:

- Hierarchical planning: Uses a `write_todos` tool to track progress and adapt to new information.
- Context offloading: Large tool outputs and intermediate artifacts are stored in a virtual filesystem instead of the active context window.
- Sub-agent delegation: Spawns specialized sub-agents with isolated context for focused work.

## Included examples

- [deep_agent_example](./deep_agent_example/README.md) - the chapter 7-style orchestration anchor
- [filesystem_context](./filesystem_context/README.md) - filesystem-backed context and memory
- [subagent_delegation](./subagent_delegation/README.md) - delegated work with isolated subagents
- [human_approval](./human_approval/README.md) - interrupt-based approval for sensitive tool calls

## Prerequisites

- Python 3.9+
- OpenAI API Key (configured via `OPENAI_API_KEY` environment variable)

## Steps for running this example

1.  Install dependencies:
```bash
python -m venv .venv

# macOS/Linux:
source .venv/bin/activate

# Windows Command Prompt:
.venv\Scripts\activate.bat

# Windows PowerShell:
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

2. Set environment variables:
   Ensure your OpenAI API key is set as an environment variable. You can do this by:
```
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```
Alternatively, create a `.env` file in the source directory with the content `OPENAI_API_KEY="YOUR_OPENAI_API_KEY"`.

3. Run the script:
```bash
python deep_agent_example.py
```

## Output
The script will execute a complex task, demonstrating how DeepAgents orchestrates multiple steps, manages context overflow, and delegates to sub-agents. The output will show the planning process, tool usage, and final results of the task execution.

```
Executing task: Research the latest trends in context engineering for 2026 and save a report.md

Task complete. (Note: Running this in a real environment requires API keys)

Final execution state (message list) contains the plan and sub-agent results.
```
