# Filesystem context with OpenViking

This example demonstrates how to use [OpenViking](https://github.com/bonigarcia/openviking) to manage an agent's context as a hierarchical filesystem.

OpenViking allows agents to organize knowledge, memory, and state into directories and files, using the `viking://` protocol for navigation and retrieval.

The key features of this example include:

- Hierarchical context: Context is structured like a filesystem (e.g., `viking://resources/`, `viking://session/`).
- Tiered retrieval: Information is processed into three layers (L0: Abstract, L1: Overview, L2: Full Content) to optimize token usage.
- Filesystem operations: Agents can use familiar operations like `ls`, `read`, and `find` to interact with their context.

## Prerequisites

- Python 3.9+
- OpenViking library

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

2. Create OpenViking configuration :
```
openviking-server init
```

3. Run the script:
```bash
python openviking_example.py
```

## Output
The script will execute a task that demonstrates how OpenViking manages the agent's context as a filesystem. The output will show the structure of the virtual filesystem, the retrieval of information at different tiers, and the results of filesystem operations.
