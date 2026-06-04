# Codex with Context7

This example uses [Context7](https://github.com/upstash/context7) with Codex. The coding task is a FastAPI backlog scoring endpoint, and it benefits from current documentation for routing, request validation using Pydantic fields, and response models.

## Codex setup

Run the following command to set up the Context7 integration with Codex:

```bash
npx ctx7 setup --codex
```

## Files

- `context7-query.md` captures the retrieval flow and the documentation facts used before coding.
- `requirements.txt` pins the library version used by the example.
- `src/backlog.py` contains the FastAPI endpoint and scoring logic.
- `tests/test_backlog.py` verifies the result.

## Local Verification

```bash
python -m venv .venv
# Activate the virtual environment in your shell.
pip install -r requirements.txt
python -m unittest discover -s tests -p "test_*.py" -v
```

The point of the example is to make current documentation retrieval explicit and inspectable inside the Cursor MCP workflow instead of reducing it to a handwritten note.
