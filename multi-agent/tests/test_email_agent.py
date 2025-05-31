from email_agent import extract_sender, extract_urgency, extract_intent, process_email

demo_email = """From: john@example.com
Subject: Urgent complaint about product

Hello,

I have an issue with the product I received.

Please address this immediately.

Thanks,
John
"""

def test_extract_sender():
    sender = extract_sender(demo_email)
    assert sender == "john@example.com"

def test_extract_urgency():
    urgency = extract_urgency(demo_email)
    assert urgency == "high"

def test_extract_intent():
    intent = extract_intent(demo_email)
    assert intent == "Complaint"

def test_process_email():
    crm_data = process_email(demo_email)
    assert crm_data["sender"] == "john@example.com"
    assert crm_data["urgency"] == "high"
    assert crm_data["intent"] == "Complaint"
