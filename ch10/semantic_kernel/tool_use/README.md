# Tool use

This example shows how Semantic Kernel can call a small tool or plugin instead of answering only from the model.

## Prerequisites

- Semantic Kernel installed in the language/runtime you are using for this chapter.
- The API key required by your local Semantic Kernel setup, if your runtime needs one.

## Files to inspect first

- `semantic-kernel-tool-use.md`: the tool name, its scope, and the exact response it should return.
- `tool_use_config.md`: the minimal setup notes for loading the example folder.

## Configure Semantic Kernel

1. Open this folder as the example workspace in your Semantic Kernel setup.
2. Read `tool_use_config.md` and register the `lookup_example_code` tool.
3. Read `semantic-kernel-tool-use.md` and confirm that `lookup_example_code` returns `SK-TOOL-42` for the prompt `What is the example code word?`.

## Run the example

1. Ask `What is the example code word?`.
2. Confirm Semantic Kernel calls `lookup_example_code`.
3. Confirm the reply includes `SK-TOOL-42`.

## Expected result

- The assistant invokes the tool for the example request.
- The reply includes the exact fixed value returned by the tool.

## Cleanup or reset

1. Remove any cache files created by your Semantic Kernel runtime for this example workspace.
