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
import json

from jsonschema import ValidationError, validate
from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    summary: str = Field(description="A concise summary of the user's request.")
    risk_level: str
    action: str
    citations: list[str] = Field(description="Sources used to support the answer.")


SCHEMA = AgentResponse.model_json_schema()


def validate_response(raw_llm_output: str) -> dict:
    data = json.loads(raw_llm_output)
    validate(instance=data, schema=SCHEMA)
    return data


def main():
    # 1. Simulate a valid LLM output
    raw_llm_output = (
        '{"summary": "The request is low risk and can be answered directly.", '
        '"risk_level": "low", '
        '"action": "answer", '
        '"citations": ["policy://general"]}'
    )

    # 2. Parse and validate the output against the JSON Schema
    print("Validating LLM output...")
    try:
        response = validate_response(raw_llm_output)
    except (json.JSONDecodeError, ValidationError) as exc:
        print("Validation failed.")
        print(f"Errors: {exc}")
        return

    print("Validation successful!")
    print(f"Validated Output: {response}")

    # 3. Example of a policy failure that still passes schema validation
    print("\nSimulating policy failure (high risk must escalate)...")
    bad_output = (
        '{"summary": "The request requires review.", '
        '"risk_level": "high", '
        '"action": "answer", '
        '"citations": ["policy://risk"]}'
    )

    try:
        response_fail = validate_response(bad_output)
        if response_fail["risk_level"] == "high" and response_fail["action"] != "escalate":
            print("Policy validation failed as expected.")
            print(f"Validated Output: {response_fail}")
        else:
            print("Policy validation passed.")
            print(f"Validated Output: {response_fail}")
    except (json.JSONDecodeError, ValidationError) as exc:
        print("Schema validation failed.")
        print(f"Errors: {exc}")


if __name__ == "__main__":
    main()
