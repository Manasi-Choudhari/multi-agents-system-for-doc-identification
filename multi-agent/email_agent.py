import re
from typing import Dict, Any, Tuple

def extract_sender(email_text: str) -> str:
    match = re.search(r"From:\s*(.*)", email_text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Unknown"

def extract_urgency(email_text: str) -> str:
    # Simple keyword based urgency detection
    urgency_terms = {
        "high": ["urgent", "asap", "immediately", "immediate"],
        "medium": ["soon", "priority", "important"],
        "low": ["whenever", "no rush", "not urgent"]
    }
    text = email_text.lower()
    for level, keywords in urgency_terms.items():
        for kw in keywords:
            if kw in text:
                return level
    return "normal"

def extract_intent(email_text: str) -> str:
    # Simple keyword based intent detection
    intents = {
        "Invoice": ["invoice", "bill", "payment"],
        "RFQ": ["rfq", "request for quote", "quotation"],
        "Complaint": ["complaint", "issue", "problem"],
        "Regulation": ["regulation", "policy", "compliance"]
    }
    text = email_text.lower()
    for intent, keywords in intents.items():
        for kw in keywords:
            if kw in text:
                return intent
    return "Other"

def process_email(email_text: str) -> Dict[str, Any]:
    sender = extract_sender(email_text)
    urgency = extract_urgency(email_text)
    intent = extract_intent(email_text)

    # Format for CRM usage
    crm_format = {
        "sender": sender,
        "urgency": urgency,
        "intent": intent,
        "raw_email_preview": email_text[:200]  # keep a short preview
    }
    return crm_format
