import json
import os
import re
from typing import Tuple, Dict, Any

# A simple mock classifier that identifies format and intent

def classify_format(input_data: Any) -> str:
    """
    Classify the format of the input data.
    Returns one of: "PDF", "JSON", "Email"
    """
    # If input is bytes and looks like PDF header, classify as PDF
    if isinstance(input_data, bytes):
        if input_data.startswith(b"%PDF"):
            return "PDF"
        else:
            return "Unknown"
    elif isinstance(input_data, dict):
        return "JSON"
    elif isinstance(input_data, str):
        # simple heuristic: if looks like email with From:, Subject:, etc.
        if re.search(r"From: ", input_data) or re.search(r"Subject: ", input_data):
            return "Email"
        else:
            # Could be raw text, treat as Email for demo
            return "Email"
    else:
        return "Unknown"

def classify_intent(format_type: str, input_data: Any) -> str:
    """
    Classify intent based on format and content.
    Intents: Invoice, RFQ, Complaint, Regulation, Other
    For demo, uses simple keyword search.
    """
    content = ""
    if format_type == "PDF":
        # For simplicity, pretend we performed OCR and got text
        # In reality, you'd parse PDF text here
        content = "Sample text extracted from PDF Invoice"
    elif format_type == "JSON":
        try:
            if isinstance(input_data, dict):
                content = json.dumps(input_data).lower()
            else:
                content = str(input_data).lower()
        except Exception:
            content = ""
    elif format_type == "Email":
        if isinstance(input_data, str):
            content = input_data.lower()
        else:
            content = ""
    else:
        return "Other"

    if "invoice" in content:
        return "Invoice"
    elif "rfq" in content or "request for quote" in content:
        return "RFQ"
    elif "complaint" in content:
        return "Complaint"
    elif "regulation" in content:
        return "Regulation"
    else:
        return "Other"

def classify(input_data: Any) -> Tuple[str, str]:
    """
    Classify input data into format and intent.
    Returns (format, intent)
    """
    format_type = classify_format(input_data)
    intent = classify_intent(format_type, input_data)
    return (format_type, intent)

