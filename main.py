import pandas as pd
from database import initialize_database, save_log_to_db
from preprocessing import prepare_logs_for_analysis
from analysis import analyze_logs
from report_generator import generate_report

def main():
    print("Initializing the database...")
    initialize_database()
    
    print("Loading log data from CSV...")
    # Replace this path with your actual log file path
    log_df = pd.read_csv('log-analyzer/data/sample_logs.csv')
    
    print("Preprocessing logs for analysis...")
    documents = prepare_logs_for_analysis(log_df)
    
    print("Running the AIOps pipeline: log analysis using LLM...")
    analysis_results = analyze_logs(documents, sample_size=20)
    
    print("Generating the final analysis report...")
    report_path = generate_report(analysis_results)
    
    print(f"Analysis complete. Report saved at: {report_path}")

if __name__ == "__main__":
    main()
