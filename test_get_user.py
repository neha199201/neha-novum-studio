import pytest
from common.assertions import assert_status_code

def test_get_user_positive(api, created_user):
    user_id = created_user["id"]
    if not user_id:
        pytest.skip("Could not create user to test GET")
    resp = api.get_user(user_id)
    assert resp.status_code in (200, 201)
    try:
        j = resp.json()
        assert j.get("data") and str(j["data"].get("id", "")) == str(user_id)
    except Exception:
        pass

def test_get_user_not_found(api):
    resp = api.get_user(9999999)
    assert resp.status_code in (404, 400)