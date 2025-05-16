import os

# -------------------------------
# Database Configuration
# -------------------------------
DB_CONFIG = {
    'dbname': 'logs_db',
    'user': 'postgres',
    'password': 'laiba124',
    'host': 'localhost',
    'port': '5432'
}

# -------------------------------
# Language Model Configuration
# -------------------------------
LLM_MODEL = "meta-llama/Meta-Llama-3-8B"  # Pre-trained LLaMA model used for log analysis
MAX_TOKENS = 512                          # Maximum token limit for model input
TEMPERATURE = 0.7                         # Sampling temperature for response diversity

# -------------------------------
# Analysis Parameters
# -------------------------------
ANOMALY_THRESHOLD = 0.8                   # Threshold score to classify a log as anomalous
CRITICAL_LEVELS = ['ERROR', 'CRITICAL']   # Log levels considered critical for prioritization
