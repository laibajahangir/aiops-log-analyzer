
import os

# Database Configuration
DB_CONFIG = {
    'dbname': 'logs_db',
    'user': 'postgres',
    'password': 'laiba124',
    'host': 'localhost',
    'port': '5432'
}

# LLM Configuration
LLM_MODEL = "meta-llama/Meta-Llama-3-8B"
MAX_TOKENS = 512
TEMPERATURE = 0.7

# Analysis Thresholds
ANOMALY_THRESHOLD = 0.8
CRITICAL_LEVELS = ['ERROR', 'CRITICAL']
