import json

# Check if all required keys exist in the JSON response
def validate_json_structure(response_json, required_keys):
    for key in required_keys:
        if key not in response_json:
            raise AssertionError(f"Missing key '{key}' in JSON response")
    return True