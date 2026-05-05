"""
(C) Copyright 2026 Boni Garcia (https://bonigarcia.github.io/)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import time
from pageindex import PageIndexClient


def main():
    # Initialize the PageIndex client
    # You can get an API key from https://dash.pageindex.ai/
    api_key = os.getenv("PAGEINDEX_API_KEY")
    if not api_key:
        print("Please set the PAGEINDEX_API_KEY environment variable.")
        return

    client = PageIndexClient(api_key=api_key)

    # Path to the local PDF file
    pdf_path = "sample.pdf"
    print(f"--- Indexing document: {pdf_path} ---")

    # 1. Upload and index the document
    # submit_document returns a dictionary containing the doc_id
    upload_result = client.submit_document(pdf_path)
    doc_id = upload_result.get("doc_id")

    print(f"Document submitted. ID: {doc_id}")
    print("Waiting for indexing to complete...")

    # Poll for completion status
    while True:
        doc_info = client.get_document(doc_id)
        status = doc_info.get("status")
        if status == "completed":
            break
        elif status == "failed":
            print("Indexing failed.")
            return
        time.sleep(2)

    print("Indexing complete.\n")

    # 2. Reasoning-based Retrieval and Generation
    query = "What happens if the same note is changed on two different devices?"
    print(f"Query: {query}")

    # chat_completions performs reasoning-based retrieval and answer generation
    # It follows an interface similar to OpenAI's chat completions
    response = client.chat_completions(
        messages=[{"role": "user", "content": query}],
        doc_id=doc_id
    )

    print("\n--- Answer ---")
    answer = response["choices"][0]["message"]["content"]
    print(answer)

    # Optional: Retrieve the tree structure or reasoning details if needed
    tree = client.get_tree(doc_id)
    print(f"\nDocument Tree structure retrieved: {len(tree)} nodes found.")


if __name__ == "__main__":
    main()
