
import pandas as pd
from database import initialize_database, save_log_to_db
from preprocessing import prepare_logs_for_analysis
from analysis import analyze_logs
from report_generator import generate_report

def main():
    print("Initializing database...")
    initialize_database()
    
    print("Loading log data...")
    # In real usage, you would load actual log files here
    log_df = pd.read_csv('log-analyzer/data/sample_logs.csv')  # Create this file or use your data
    
    print("Preprocessing logs...")
    documents = prepare_logs_for_analysis(log_df)
    
    print("Analyzing logs with LLM...")
    analysis_results = analyze_logs(documents, sample_size=20)
    
    print("Generating report...")
    report_path = generate_report(analysis_results)
    
    print(f"Analysis complete! Report saved to {report_path}")

if __name__ == "__main__":
    main()
