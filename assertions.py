def assert_status_code(response, expected):
    assert response.status_code == expected, f"Expected status {expected}, got {response.status_code} - body: {response.text}"

def assert_msg(response_json, expected_msg):
    msg = response_json.get("msg") or response_json.get("message") or ""
    assert expected_msg.lower() in str(msg).lower(), f"Expected message to contain '{expected_msg}', got '{msg}'"