from typing import Dict, Any, Tuple

# For demo purposes, define expected schema keys
EXPECTED_KEYS = {"invoice_number", "date", "total_amount", "vendor"}

TARGET_SCHEMA_MAPPING = {
    "invoiceNo": "invoice_number",
    "dateIssued": "date",
    "amount": "total_amount",
    "vendorName": "vendor"
}

def extract_and_reformat(json_payload: Dict[str, Any]) -> Tuple[Dict[str, Any], list]:
    """
    Extracts fields from incoming JSON and reformats to target schema.
    Returns reformatted dict and list of anomaly messages.
    """
    reformatted = {}
    anomalies = []

    # Map incoming keys to expected target schema keys
    for target_key in EXPECTED_KEYS:
        found = False
        # check original keys and mapping
        if target_key in json_payload:
            reformatted[target_key] = json_payload[target_key]
            found = True
        else:
            # try mapping
            for orig_key, mapped_key in TARGET_SCHEMA_MAPPING.items():
                if mapped_key == target_key and orig_key in json_payload:
                    reformatted[target_key] = json_payload[orig_key]
                    found = True
                    break
        
        if not found:
            anomalies.append(f"Missing expected field: {target_key}")

    # Flag missing required values or unexpected types (simplified)
    if "total_amount" in reformatted:
        try:
            reformatted["total_amount"] = float(reformatted["total_amount"])
        except Exception:
            anomalies.append("Field 'total_amount' should be a number.")

    return reformatted, anomalies

def process_json(json_payload: Dict[str, Any]) -> Tuple[Dict[str, Any], list]:
    """
    Process JSON input, extract and reformat.
    """
    reformatted, anomalies = extract_and_reformat(json_payload)
    return reformatted, anomalies
