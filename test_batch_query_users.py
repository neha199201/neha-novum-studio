def test_batch_query_users(api):
    params = {"page":1, "size":10, "keyword":"test"}
    resp = api.batch_query_users(params)
    assert resp.status_code in (200, 201)
    try:
        j = resp.json()
        data = j.get("data") or j
        assert isinstance(data, dict) or isinstance(data, list)
    except Exception:
        assert False, "Response not JSON or missing expected fields"