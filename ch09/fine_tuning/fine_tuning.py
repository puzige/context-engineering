from datasets import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)


def fine_tune():
    model_name = "distilgpt2"
    output_dir = "./clinic-assistant-distilgpt2"

    print(f"[INFO] Loading tokenizer and model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name)

    training_rows = [
        {
            "instruction": "Explain the cancellation policy.",
            "response": "Please cancel at least 24 hours before the appointment.",
        },
        {
            "instruction": "Help me reschedule a visit.",
            "response": "I can help with scheduling, but a clinician handles medical advice.",
        },
        {
            "instruction": "When should I arrive for my appointment?",
            "response": "Please arrive 15 minutes early to complete any necessary forms.",
        },
        {
            "instruction": "Can I get medical advice by email?",
            "response": "Email is best for scheduling questions; clinical concerns should go to a licensed professional.",
        },
    ]

    def format_example(row):
        return {"text": f"Instruction: {row['instruction']}\nResponse: {row['response']}"}

    print("[INFO] Preparing dataset...")
    dataset = Dataset.from_list(training_rows).map(format_example)

    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=128)

    tokenized_dataset = dataset.map(tokenize, batched=True, remove_columns=dataset.column_names)

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    print("[INFO] Configuring trainer...")
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        logging_steps=1,
        save_steps=50,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )

    print("[INFO] Starting fine-tuning...")
    trainer.train()

    print(f"[INFO] Saving model to {output_dir}")
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)

    print("[INFO] Testing fine-tuned model...")
    input_text = "Instruction: Help me book an appointment.\nResponse:"
    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        pad_token_id=tokenizer.eos_token_id,
    )
    print("Generated Output:")
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

if __name__ == "__main__":
    fine_tune()
