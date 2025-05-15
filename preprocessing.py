
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

def clean_log_message(message):
    """Clean raw log message"""
    # Remove timestamps if embedded
    message = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '', message)
    # Remove IP addresses
    message = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '[IP]', message)
    # Remove excessive whitespace
    return ' '.join(message.split()).strip()

def prepare_logs_for_analysis(log_df):
    """Prepare DataFrame of logs for LLM processing"""
    log_df['cleaned_message'] = log_df['message'].apply(clean_log_message)
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50
    )
    
    documents = []
    for _, row in log_df.iterrows():
        text = f"Level: {row['level']}, Component: {row['component']}, Message: {row['cleaned_message']}"
        docs = text_splitter.create_documents([text])
        documents.extend(docs)
    
    return documents
