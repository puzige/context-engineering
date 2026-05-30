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
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig


def main():
    # 1. Initialize the analyzer and anonymizer engines
    # The analyzer uses NLP models and regex to find PII
    analyzer = AnalyzerEngine()
    # The anonymizer applies redaction or masking logic
    anonymizer = AnonymizerEngine()

    # 2. Define the sample text containing sensitive information
    text = (
        "Hello, my name is David Miller. You can reach me at "
        "david.miller@example.com or by phone at +1 212-555-0123. "
        "I live at 123 Main St, New York."
    )

    # Focus on the entity types we want to redact in this demo.
    entities = ["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "LOCATION"]

    # 3. Analyze the text
    # We scan the text for common entities like names, emails, phone numbers, and locations
    print("Analyzing text for PII...")
    results = analyzer.analyze(text=text, language='en', entities=entities)

    # 4. Define the anonymization strategy
    # We replace any found PII with a generic <REDACTED> placeholder
    operators = {
        "DEFAULT": OperatorConfig("replace", {"new_value": "<REDACTED>"}),
    }

    # 5. Execute anonymization
    print("Anonymizing sensitive entities...")
    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results,
        operators=operators
    )

    # 6. Display results
    print("-" * 20)
    print(f"Original Text: {text}")
    print("-" * 20)
    print(f"Anonymized Text: {anonymized_result.text}")


if __name__ == "__main__":
    main()
