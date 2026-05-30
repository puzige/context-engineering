# Bias detection: assessing fairness in AI recommendations

This example demonstrates how to use the [Fairlearn](https://fairlearn.org/) library to detect demographic parity issues in a model's recommendations.

## Requirements

This project requires [Python](https://www.python.org/) 3.12 or 3.13 and the libraries listed in `requirements.txt`.

## Steps for running this example
 
1. Create a virtual environment with Python 3.13 or 3.12, then install dependencies:
```bash
# macOS/Linux:
python3.13 -m venv .venv
source .venv/bin/activate

# Windows Command Prompt / PowerShell:
py -3.13 -m venv .venv
.venv\Scripts\activate.bat
# or
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

2. Run the script:
```bash
python bias_detection.py
```

## Output

The script analyzes a mock dataset of credit approval recommendations, prints the selection rate for each age group, and calculates a demographic parity ratio to identify potential bias.

```text
[INFO] Analyzing bias in credit approval recommendations...
[INFO] Demographic Parity Metrics:
Selection rate for Young: 0.20
Selection rate for Senior: 0.60
[INFO] Demographic Parity Ratio: 0.33
[WARNING] Significant disparity detected against the Young group.
[INFO] This result suggests the context or model logic may be biased.
```
