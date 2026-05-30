# Fine-tuning: customizing model behavior

This example demonstrates how to fine-tune a small language model ([DistilGPT2](https://huggingface.co/distilbert/distilgpt2)) on a tiny instruction-response dataset so it adopts a simple clinic-assistant persona.

## Requirements

This project requires [Python](https://www.python.org/) 3.x and the libraries listed in `requirements.txt`.

## Steps for running this example

1. Install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows cmd: .venv\Scripts\activate # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the script:
```bash
python fine_tuning.py
```

## Output

The script loads the dataset, tokenizes the examples, configures a Hugging Face `Trainer`, runs a short training loop, saves the updated model, and prints a sample generation.

```text
[INFO] Loading tokenizer and model: distilgpt2
[INFO] Preparing dataset...
[INFO] Configuring trainer...
...
[INFO] Saving model to ./clinic-assistant-distilgpt2
[INFO] Testing fine-tuned model...
Generated Output:
Instruction: Help me book an appointment.
Response: Please arrive 15 minutes early to complete any necessary forms.
```
