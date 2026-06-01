# Memory and state

This example shows how Semantic Kernel can store a small state object on one turn and reuse it on a follow-up turn.

## Prerequisites

- Semantic Kernel installed in the language/runtime you are using for this chapter.
- The API key required by your local Semantic Kernel setup, if your runtime needs one.

## Files to inspect first

- `memory_state_notes.md`: the state object and the exact follow-up prompt to verify.
- `memory_state_config.md`: the minimal setup notes for loading and persisting the example state.

## Configure Semantic Kernel

1. Open this folder as the example workspace in your Semantic Kernel setup.
2. Read `memory_state_config.md` and enable persistence for the example state.
3. Read `memory_state_notes.md` and confirm the state object stays small and readable.

## Run the example

1. Send the first prompt from `memory_state_notes.md` and save the state object.
2. Send the follow-up prompt from `memory_state_notes.md`.
3. Confirm the reply uses the same saved state.

## Expected result

- The first turn stores the small state object.
- The follow-up turn reuses that same state instead of starting over.

## Cleanup or reset

1. Delete any local cache or state files created by your Semantic Kernel runtime for this example workspace.
