# Tool use

This example shows how Semantic Kernel can register a small plugin function and use it to answer the exact prompt `What is the example code word?`.

## Prerequisites

- Python 3.10+
- `semantic-kernel` installed from this folder's `requirements.txt`

## Configure Semantic Kernel

1. Create and activate a virtual environment.
2. Install the dependencies from `requirements.txt`.
3. Run `semantic_kernel_tool_use.py` and confirm the plugin function returns `SK-TOOL-42` for the prompt `What is the example code word?`.

## Run the example

1. Run `python semantic_kernel_tool_use.py` from this folder.
2. Confirm the script uses Semantic Kernel to invoke the `lookup_example_code` plugin function.
3. Confirm the printed output includes `SK-TOOL-42`.

## Expected result

- The prompt `What is the example code word?` resolves to `SK-TOOL-42`.
- The script prints `Tool-backed example output: SK-TOOL-42`.

## Cleanup or reset

1. Remove any virtual environment or cache files created for this example.
