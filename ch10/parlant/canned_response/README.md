# Parlant canned response

This companion covers canned responses for controlled wording.
Use them when you want Parlant to choose from approved response templates instead of generating free-form text.

## Requirements

* [Python](https://www.python.org/) 3.10+

## Steps for running this example in the shell

1. Install dependencies:
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

2. Run the script:
```bash
python canned_response.py
```

## What it demonstrates

* Template-based response selection
* Tighter control over wording
* A good fit for strict or highly branded replies

## Output

```
User: There is a shipping delay on my order.
Template: We are sorry for the delay. I am checking the latest status now.

User: I found a billing issue.
Template: Thanks for flagging this. I will connect you with the billing team.

User: Can you check the order status?
Template: I can help with that. Please share your order number.
```
