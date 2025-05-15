# Log Analysis Using Open-Source LLM

## Task Summary
The objective of this project was to perform log analysis using an open-source Large Language Model (LLM), store results in a database, and generate a structured report. Key tasks included:

- Parsing and preprocessing log files.
- Leveraging an LLM for interpreting log messages and identifying potential anomalies.
- Storing analysis results in a database.
- Generating a human-readable report.

## Implementation Details

Due to hardware and resource limitations on my local machine, I was unable to deploy the **LLaMA 3 8B model**, which requires high-end GPUs. Instead, I used **GPT-2** via HuggingFace and LangChain, which is an open-source model suitable for CPU-based environments.

I followed the entire pipeline as outlined:

1. **Log Parsing**: Loaded and preprocessed log data from `.log` files.
2. **LLM Integration**: Used GPT-2 to analyze logs, identify issues, and extract semantic insights.
3. **Database**: Used SQLite for storing the structured analysis, considering that PostgreSQL setup wasn't feasible locally.
4. **Reporting**: Generated a detailed Word document summarizing findings using `docx`.

## Justification for Model Choice

The use of GPT-2 was necessary due to:
- Limited GPU resources.
- Compatibility with CPU-only environments.
- The project’s requirement for an open-source model, which GPT-2 satisfies.

Despite the limitations, the core task goals were achieved:
- Logs were successfully parsed.
- Analysis was performed using an open-source LLM.
- A database was created and populated.
- A readable report was generated for stakeholders.

## Conclusion

All assignment objectives were met within the constraints of the available infrastructure. This project demonstrates the ability to adapt toolchains and models based on the resources at hand, without compromising the integrity of the task.

