# Vectorless RAG with PageIndex

This example demonstrates how to implement a RAG system using [PageIndex](https://pageindex.ai/), a vectorless retrieval framework. Unlike traditional RAG, which relies on vector embeddings and similarity searches, PageIndex builds a hierarchical tree structure of your documents. This allows the system to use reasoning to navigate the document's natural organization (chapters, sections, and pages) to find the most relevant information.

## Requirements

* [Python](https://www.python.org/) 3.8+
* A [PageIndex API key](https://dash.pageindex.ai/)

## Steps for running this example in the shell

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

2. Export your PageIndex API key as an environment variable:
```bash
export PAGEINDEX_API_KEY="your-api-key" # Windows cmd: set PAGEINDEX_API_KEY="your-api-key" # Windows PowerShell: $env:PAGEINDEX_API_KEY="your-api-key"
```

3. Run the script:
```bash
python vectorless-rag-pageindex.py
```

## Output

When you run the script, it will upload the `sample.pdf` file, poll until the hierarchical index is ready, and then query it.

```
--- Indexing document: sample.pdf ---
Document submitted. ID: pi-cmosqucsf09qh01qre7me7ijb
Waiting for indexing to complete...
Indexing complete.

Query: What happens if the same note is changed on two different devices?

--- Answer ---
If the same note is changed on two different devices, **LumaNote asks the user which version to keep**. This happens during the reconciliation process — when connectivity is restored after offline edits, the app compares the local edits with the cloud copy and, in the event of a conflict, prompts the user to choose the version they want to retain.
```
