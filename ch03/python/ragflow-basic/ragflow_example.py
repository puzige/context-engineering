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
from ragflow_sdk import RAGFlow
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Initialize the client
API_KEY = os.getenv("RAGFLOW_API_KEY", "your_api_key_here")
BASE_URL = os.getenv("RAGFLOW_BASE_URL", "http://localhost:9380")

rag = RAGFlow(api_key=API_KEY, base_url=BASE_URL)


def main():
    try:
        # 2. Define the embedding model
        # Note: Ensure this model is enabled in your RAGFlow UI under 'Model Providers'
        embedding_model = "gemini-embedding-001@Google"

        # 3. Create a dataset
        dataset_name = "MyQuickstartDataset"
        print(f"Creating dataset '{dataset_name}' using model: {embedding_model}...")
        dataset = rag.create_dataset(
            name=dataset_name,
            embedding_model=embedding_model
        )
        print(f"Dataset created: {dataset.name} (ID: {dataset.id})")

        # 4. Upload a document
        # We'll use this script itself as a sample document
        file_path = __file__
        print(f"Uploading document: {file_path}...")
        with open(file_path, "rb") as f:
            blob = f.read()

        uploaded_docs = dataset.upload_documents([
            {"display_name": "ragflow_example.py", "blob": blob}
        ])
        doc_ids = [doc.id for doc in uploaded_docs]
        print(f"Uploaded document IDs: {doc_ids}")

        # 5. Parse the document and wait for completion
        print("Starting parsing... this may take a minute.")
        dataset.parse_documents(doc_ids)
        print("Parsing complete.")

        # 6. Create a chat assistant
        assistant_name = f"MyAssistant_{int(time.time())}"
        print(f"Creating chat assistant '{assistant_name}'...")
        assistant = rag.create_chat(
            name=assistant_name,
            dataset_ids=[dataset.id]
        )
        print(f"Assistant created: {assistant.name}")

        # 7. Start a conversation
        print("Starting conversation...")
        session = assistant.create_session()
        question = "What does the 'main' function do in the uploaded script?"
        print(f"Asking: {question}")

        # The ask() method returns a generator even with stream=False in some versions
        response_gen = session.ask(question, stream=False)

        # Pull the response from the generator
        for response in response_gen:
            # Try to get the answer/content from the response object
            answer = getattr(response, "content", getattr(response, "answer", "No answer found"))
            print(f"Assistant: {answer}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
