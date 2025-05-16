📌 Task Summary
This project focuses on analyzing system log files using an open-source Large Language Model (LLM). The primary objectives included:

Parsing and preprocessing raw log files.

Utilizing an LLM to interpret log messages and detect potential anomalies.

Storing the results in a structured database.

Generating a comprehensive, human-readable report.

⚙️ Implementation Details
Due to resource constraints on my local machine, deploying a resource-intensive model like LLaMA 3 (8B) was not feasible. Therefore, I opted to use GPT-2 via HuggingFace and LangChain, an open-source LLM well-suited for CPU environments.

The project pipeline followed these steps:

Log Parsing: Loaded .log files and applied preprocessing techniques.

LLM Analysis: Employed GPT-2 to semantically analyze log data and highlight anomalies or issues.

Data Storage: Used SQLite for storing analysis results due to its simplicity and local compatibility (as PostgreSQL setup was not viable).

Report Generation: Created a structured and formatted report using python-docx to summarize insights and findings.

🤖 Justification for GPT-2
GPT-2 was chosen because:

It is open-source and freely available via HuggingFace.

It runs efficiently in CPU-only environments.

It fulfilled the core analytical requirements of the project.

✅ Outcome
Despite hardware limitations, all project goals were successfully achieved:

Logs were parsed and analyzed.

An LLM was integrated for semantic understanding.

Analysis results were stored in a database.

A comprehensive report was generated for stakeholders.

📝 Conclusion
This project demonstrates my ability to adapt tools and models to infrastructure constraints while delivering a complete and functional solution. It showcases practical experience in integrating open-source LLMs, handling real-world log data, and delivering structured results in a resource-constrained environment.

