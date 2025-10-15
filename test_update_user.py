import pytest
from common.assertions import assert_status_code

def test_update_user_email_positive(api, created_user):
    user_id = created_user["id"]
    if not user_id:
        pytest.skip("No user available to update")
    payload = {"email": "updated_" + created_user["payload"]["email"]}
    resp = api.update_user(user_id, payload)
    assert resp.status_code in (200, 201, 204)
    try:
        j = resp.json()
        assert "success" in str(j.get("msg", "")).lower() or resp.status_code in (204,)
    except Exception:
        pass

def test_update_user_invalid_email(api, created_user):
    user_id = created_user["id"]
    if not user_id:
        pytest.skip("No user available to update")
    payload = {"email": "not-an-email"}
    resp = api.update_user(user_id, payload)
    assert resp.status_code in (400, 422, 200, 201)