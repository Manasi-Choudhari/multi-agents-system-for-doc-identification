# Multi-Agent AI System

## Overview

This project implements a multi-agent AI system that accepts input in PDF, JSON, or Email (text) format, classifies the format and intent, and routes it to appropriate agents for processing.

The system maintains shared context for chaining and traceability using a lightweight SQLite-backed shared memory module.

## Components

- **Classifier Agent**: Classifies input format and intent.
- **JSON Agent**: Processes structured JSON payloads, extracts and reformats data, flags anomalies.
- **Email Agent**: Processes email content, extracts sender, intent, urgency, and formats for CRM.
- **Shared Memory Module**: Stores logs and extracted data, accessible across agents.


project structure :
multi-agent-ai-system/
│
├── README.md
├── requirements.txt
├── main.py                   # Entry point for the application
├── classifier_agent.py       # Classifier Agent implementation
├── json_agent.py             # JSON Agent implementation
├── email_agent.py            # Email Agent implementation
├── shared_memory.py          # Shared Memory Module implementation
│
├── tests/                    # Unit tests for each component
│   ├── test_classifier.py
│   ├── test_json_agent.py
│   └── test_email_agent.py
│
├── samples/                  # Sample input files
│   ├── sample_email.txt
│   ├── sample_json.json
│   └── sample_pdf.pdf
│
└── logs/                     # Sample output logs or screenshots
    ├── log_1.png
    └── log_2.png
    └── log_3.png

## Setup

1. Clone the repo.
2. Create a Python 3 virtual environment and activate it.
3. Install dependencies: pip install -r requirements.txt
4. Run the main script with a sample input file path:
   
The system will:
- Classify the input.
- Route to the appropriate agent.
- Print processed data.
- Log details into shared memory.

## Sample Inputs

- `samples/sample_email.txt`: Sample email content.
- `samples/sample_json.json`: Sample JSON payload.
- `samples/sample_pdf.pdf`: Sample PDF file (binary, for demo purpose not really parsed).

## Logs and Output

Output logs and session info are printed on the console.

*sample inputs are in the sample folder

output: in logs folders


