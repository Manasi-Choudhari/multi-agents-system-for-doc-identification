from classifier_agent import classify_format, classify_intent, classify

def test_classify_format_and_intent():
    # PDF bytes with header
    pdf_bytes = b"%PDF-1.4 intro data"
    assert classify_format(pdf_bytes) == "PDF"
    assert classify_intent("PDF", pdf_bytes) == "Invoice"  # mocked to find Invoice in sample text

    # JSON dict with invoice text
    json_input = {"type": "invoice", "amount": "100"}
    fmt = classify_format(json_input)
    intent = classify_intent(fmt, json_input)
    assert fmt == "JSON"
    assert intent == "Invoice"

    # Email string
    email_str = "From: bob@example.com\nSubject: Complaint about service"
    fmt = classify_format(email_str)
    intent = classify_intent(fmt, email_str)
    assert fmt == "Email"
    assert intent == "Complaint"

    # Unknown binary input
    unknown_bytes = b"\x00\x01\x02"
    assert classify_format(unknown_bytes) == "Unknown"
    assert classify_intent("Unknown", unknown_bytes) == "Other"

def test_classify():
    assert classify("From: test@example.com\nSubject: RFQ for product") == ("Email", "RFQ")
