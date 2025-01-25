import os
import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

# Ensure the correct path based on your folder structure
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current file directory
model_path = os.path.join(current_dir, "english_to_hindi_translator")

# Convert to absolute path
model_path = os.path.abspath(model_path)

print(f"Loading translation model from: {model_path}")

# Load tokenizer and model from the specified local directory
try:
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    model = TFAutoModelForSeq2SeqLM.from_pretrained(model_path, local_files_only=True)
except Exception as e:
    print(f"Error loading model: {e}")
    raise

def translate_text(input_text: str, max_length: int = 100, num_beams: int = 5):
    tokenized_input = tokenizer([input_text], return_tensors="np")
    output_tokens = model.generate(
        **tokenized_input,
        max_length=max_length,
        num_beams=num_beams,
        early_stopping=True,
        no_repeat_ngram_size=2
    )
    translated_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return translated_text
