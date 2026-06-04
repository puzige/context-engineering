# Cursor with instructions (Karpathy-inspired guidelines)

This example demonstrates how to use [Karpathy-inspired coding guidelines](https://x.com/karpathy/status/2015883857489522876) in Cursor to guide development. The instructions address common LLM coding pitfalls, such as silent assumptions, over-engineering, unintended side-effects, and lack of verification.

The guidelines are stored in `.cursor/rules/karpathy-guidelines.mdc` and are automatically applied by Cursor when editing Python files.

## Project Structure

- `.cursor/rules/karpathy-guidelines.mdc`: The Cursor rule file enforcing the four principles.
- `src/backlog.py`: Core backlog assistant module.
- `tests/test_backlog.py`: Unit tests.

## Running the Tests

To verify that the implementation is correct, run:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
