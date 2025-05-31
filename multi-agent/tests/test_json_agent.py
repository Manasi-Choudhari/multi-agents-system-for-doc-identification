from json_agent import extract_and_reformat, process_json

def test_extract_and_reformat_complete():
    input_json = {
        "invoiceNo": "1234",
        "dateIssued": "2023-06-10",
        "amount": "2500.5",
        "vendorName": "Widgets Inc."
    }
    reformatted, anomalies = extract_and_reformat(input_json)
    assert reformatted["invoice_number"] == "1234"
    assert reformatted["date"] == "2023-06-10"
    assert reformatted["total_amount"] == 2500.5
    assert reformatted["vendor"] == "Widgets Inc."
    assert len(anomalies) == 0

def test_extract_and_reformat_missing_fields():
    input_json = {
        "invoiceNo": "1234"
    }
    reformatted, anomalies = extract_and_reformat(input_json)
    assert "Missing expected field: date" in anomalies
    assert "Missing expected field: total_amount" in anomalies
    assert "Missing expected field: vendor" in anomalies
