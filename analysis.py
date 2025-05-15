# Paste your entire new code here, multiple lines are allowed
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_llm():
    model_name = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

def analyze_logs(logs, sample_size=20):
    tokenizer, model = load_llm()
    # your code here
    return "analysis done"
