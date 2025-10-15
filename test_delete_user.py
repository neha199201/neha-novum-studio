import pytest

def test_delete_user_positive(api):
    # create a fresh user to delete
    payload = {"username":"tempdelete","email":"tempdelete@example.com","password":"abc12345"}
    r = api.create_user(payload)
    try:
        j = r.json()
    except Exception:
        j = {}
    user_id = None
    if r.status_code in (200,201):
        user_id = j.get("data", {}).get("id") or j.get("id") or j.get("data")
    if not user_id:
        pytest.skip("Could not create user for delete test")
    resp = api.delete_user(user_id)
    assert resp.status_code in (200, 204)

def test_delete_user_not_found(api):
    resp = api.delete_user(9999999)
    assert resp.status_code in (404, 400)