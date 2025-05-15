
import sqlite3  
from config import DB_CONFIG

def get_db_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect('logs.db')
    return conn

def initialize_database():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        level TEXT,
        component TEXT,
        message TEXT,
        source_ip TEXT,
        user_id TEXT,
        processed BOOLEAN DEFAULT FALSE,
        category TEXT,
        anomaly_score REAL
    )
    ''')
    
    conn.commit()
    conn.close()

def save_log_to_db(log_data):
    """Save log entry to database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO logs (timestamp, level, component, message, source_ip, user_id)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        log_data['timestamp'],
        log_data['level'],
        log_data['component'],
        log_data['message'],
        log_data['source_ip'],
        log_data['user_id']
    ))
    
    conn.commit()
    conn.close()
