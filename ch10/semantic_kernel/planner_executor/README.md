# Planner and executor

This example shows how Semantic Kernel can turn one request into a short plan and then execute the steps in order.

## Prerequisites

- Semantic Kernel installed in the language/runtime you are using for this chapter.
- The API key required by your local Semantic Kernel setup, if your runtime needs one.

## Files to inspect first

- `planner_executor_plan.md`: the sample request and the three-step order to follow.
- `planner_executor_config.md`: the minimal setup notes for loading this example folder.

## Configure Semantic Kernel

1. Open this folder as the example workspace in your Semantic Kernel setup.
2. Read `planner_executor_config.md` and apply the planner settings there.
3. Read `planner_executor_plan.md` and confirm the step order is visible before you run anything.

## Run the example

1. Ask Semantic Kernel to break the sample request `Organize a three-step plan for a small day-of-week reminder workflow.` into steps.
2. Confirm the assistant produces the same three-step order listed in `planner_executor_plan.md`.
3. Confirm the assistant executes the steps in order and reports each step clearly.

## Expected result

- The request is split into a short, readable plan.
- The execution follows the plan in the documented order.
- The final response shows the completed steps without referencing any other example folder or file.

## Cleanup or reset

1. Remove any local cache, plan, or session state created by your Semantic Kernel runtime for this example workspace.
