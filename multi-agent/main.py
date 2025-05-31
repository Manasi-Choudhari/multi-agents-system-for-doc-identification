import os
import json
import uuid
import argparse

from classifier_agent import classify
from json_agent import process_json
from email_agent import process_email
from shared_memory import SharedMemory

def read_file(path: str):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".txt" or ext == ".eml":
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    elif ext == ".json":
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif ext == ".pdf":
        with open(path, "rb") as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def main():
    parser = argparse.ArgumentParser(description="Multi-Agent AI system demo")
    parser.add_argument("input_path", help="Path to input file (pdf, json, txt/email)")
    args = parser.parse_args()

    mem = SharedMemory("memory_store.db")

    # Read input
    input_data = read_file(args.input_path)

    # Classify format and intent
    format_type, intent = classify(input_data)
    print(f"Classification: format={format_type}, intent={intent}")

    # Generate thread/conversation ID for shared memory tracking
    thread_id = str(uuid.uuid4())
    mem.log(source="ClassifierAgent", type_=format_type+"|"+intent, info="Classification done", thread_id=thread_id)

    if format_type == "JSON":
        # Route to JSON agent
        reformatted, anomalies = process_json(input_data)
        mem.save_extracted(thread_id, "reformatted_json", json.dumps(reformatted))
        mem.save_extracted(thread_id, "anomalies", "; ".join(anomalies) if anomalies else "None")
        print("JSON Agent processed data:")
        print(json.dumps(reformatted, indent=2))
        if anomalies:
            print("Anomalies found:")
            for a in anomalies:
                print("- " + a)
    elif format_type == "Email":
        # Route to Email agent
        crm_data = process_email(input_data)
        mem.save_extracted(thread_id, "crm_data", json.dumps(crm_data))
        print("Email Agent processed data:")
        print(json.dumps(crm_data, indent=2))
    elif format_type == "PDF":
        # For demo, just log and print placeholder
        mem.save_extracted(thread_id, "pdf_processed", "Extracted text placeholder")
        print("PDF Agent: (demo) processed PDF input. Extraction placeholder.")
    else:
        print("Format unknown or not supported.")

    # Print memory logs for this thread for demo
    print("\nLogs for this session:")
    logs = mem.get_thread_logs(thread_id)
    for log_entry in logs:
        print(f"- {log_entry['timestamp']}: {log_entry['source']} | {log_entry['type']} | {log_entry['info']}")

if __name__ == "__main__":
    main()
