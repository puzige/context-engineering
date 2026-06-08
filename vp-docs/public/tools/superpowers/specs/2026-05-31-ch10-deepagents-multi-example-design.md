# CH10 DeepAgents Multi-Example Design

**Goal:** Restore `ch10/deepagents` as a small set of runnable DeepAgents examples: one chapter anchor based on the chapter 7 orchestration sample, plus three focused demos for filesystem context, sub-agent delegation, and human approval.

**Architecture:** Keep the chapter intentionally small, but split by DeepAgents capability instead of by language or arbitrary tutorial shape. The anchor example stays close to `ch07/deepagents-orchestration` and demonstrates the core `create_deep_agent` flow. The three demos each isolate one capability so the chapter reads as a map of DeepAgents features rather than a single oversized script.

**Tech Stack:** Python, `deepagents`, `langchain-openai`, `pytest`

---

## Scope

- Keep `ch10/deepagents/deep_agent_example.py` as the primary reference-style orchestration example.
- Add three focused runnable demos:
  - `filesystem_context`
  - `subagent_delegation`
  - `human_approval`
- Update `ch10/deepagents/README.md` to present the anchor and the three demos as a single chapter set.
- Keep the tests offline by monkeypatching DeepAgents entrypoints and checking wiring/output contracts.
- Keep the example code short enough to read alongside the reference chapter 7 sample.

## Not In Scope

- Reintroducing the earlier `file_context` or `planning_loop` slices.
- Adding LangGraph examples or mixing other framework families into this chapter.
- Building a real filesystem backend, approval UI, or sub-agent runtime beyond the example wiring.

## File Plan

- Create: `ch10/deepagents/deep_agent_example.py`
- Create: `ch10/deepagents/filesystem_context/filesystem_context.py`
- Create: `ch10/deepagents/filesystem_context/README.md`
- Create: `ch10/deepagents/subagent_delegation/subagent_delegation.py`
- Create: `ch10/deepagents/subagent_delegation/README.md`
- Create: `ch10/deepagents/human_approval/human_approval.py`
- Create: `ch10/deepagents/human_approval/README.md`
- Update: `ch10/deepagents/README.md`
- Update: `ch10/deepagents/requirements.txt`
- Update: `ch10/deepagents/tests/test_examples.py`
- Delete: `ch10/deepagents/file_context/`, `ch10/deepagents/planning_loop/`, `ch10/deepagents/research_harness/`, and `ch10/deepagents/tests/test_companions.py` if they are present in the branch state

## Example Roles

### 1. Anchor example

`deep_agent_example.py` is the chapter anchor. It mirrors the chapter 7 script shape: `create_deep_agent`, a single user request, and a short printed result summary. Its purpose is to show the default DeepAgents orchestration story in the clearest possible form.

### 2. Filesystem context demo

`filesystem_context.py` shows how DeepAgents can route memory and workspace state through filesystem-like paths. The example should seed a tiny memory file and a tiny workspace file, then build an agent with explicit backend/store wiring so the concept is visible without needing a real backend service.

### 3. Sub-agent delegation demo

`subagent_delegation.py` should show how work can be split into a small number of focused helpers that each do one job: select files, summarize notes, and merge them. The example should stay simple enough to read as a delegation sketch, not a production orchestration layer.

### 4. Human approval demo

`human_approval.py` should show a checkpoint where sensitive work pauses for approval. The runnable example may support a simple `--auto-approve` mode so tests can exercise the path without interaction, while the README explains where a real interrupt would occur.

## Testing Strategy

- Add one contract test per example to verify the example wires DeepAgents the way the chapter describes.
- Monkeypatch `create_deep_agent` so tests assert on the kwargs and avoid live model calls.
- Verify the anchor example matches the chapter 7 model/prompt/tool shape.
- Verify the filesystem demo exposes the seeded memory/workspace paths.
- Verify the delegation demo produces a short merged summary.
- Verify the human approval demo prints both the waiting state and the auto-approved state.

## Success Criteria

- `ch10/deepagents` presents four runnable examples with one clear anchor and three focused demos.
- The anchor example remains faithful to the chapter 7 orchestration reference.
- The supporting demos each highlight one DeepAgents capability without overlapping too much.
- The chapter tests stay deterministic and pass without API keys.
