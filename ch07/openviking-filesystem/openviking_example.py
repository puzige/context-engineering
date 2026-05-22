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
# openviking-filesystem example
import os
import sys
from openviking import OpenViking

def main():
    # 1. Initialize OpenViking with a local data path
    # This creates a virtual filesystem context from the local directory
    try:
        client = OpenViking(path="./data")
        print("OpenViking initialized at viking://resources/")
    except FileNotFoundError as e:
        print(f"Configuration Error: {e}")
        print("\nOpenViking requires a global configuration file to run.")
        print("Please initialize it by running the following command in your terminal:")
        print("  openviking-server init")
        print("\nOr manually create ~/.openviking/ov.conf as described in the documentation.")
        sys.exit(1)

    # 2. List the available context (filesystem-style navigation)
    print("\nListing available context files:")
    files = client.ls("viking://resources/")
    for f in files:
        print(f"- {f}")

    # 3. Perform a tiered retrieval
    # Tiered loading (L0, L1, L2) helps manage the context window budget
    query = "What are the core techniques for context management?"
    print(f"\nSearching for: '{query}'")

    # Retrieval results include metadata and hierarchical paths
    results = client.find(query, limit=2)

    for i, res in enumerate(results):
        print(f"\nResult {i + 1}:")
        print(f"Path: {res.path}")
        print(f"L1 (Overview): {res.l1_summary}")

        # Load L2 (Full Content) only when needed
        if "management" in res.path:
            print("Loading full content (L2)...")
            content = client.read(res.path)
            print(f"Content snippet: {content[:100]}...")


if __name__ == "__main__":
    main()
