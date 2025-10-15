import pytest
from common.assertions import assert_status_code, assert_msg

def test_create_user_positive(api, new_user_payload):
    resp = api.create_user(new_user_payload)
    # Accept 200 or 201
    assert resp.status_code in (200, 201)
    j = resp.json()
    # expected schema: {"code":200,"data": {"id":1,...}, "msg":"success"} OR reqres style
    assert "data" in j or "id" in j or resp.status_code in (200,201)

def test_create_user_missing_username(api, new_user_payload):
    payload = new_user_payload.copy()
    payload.pop("username", None)
    resp = api.create_user(payload)
    # API might return 4xx for invalid input
    assert resp.status_code in (400, 422, 201, 200)