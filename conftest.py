import pytest
from api.user_api import UserAPI
from config.config_reader import get_base_url
from common.logger import get_logger
from common.utils import unique_username, unique_email

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def base_url():
    return get_base_url()

@pytest.fixture(scope="session")
def api(base_url):
    return UserAPI(base_url)

@pytest.fixture
def new_user_payload():
    return {
        "username": unique_username("autotest"),
        "email": unique_email("autotest"),
        "password": "Pass1234!"
    }

@pytest.fixture
def created_user(api, new_user_payload):
    # Create a user and yield the created user's id, then cleanup by deleting the user if exists.
    resp = api.create_user(new_user_payload)
    logger.info("Create user response status: %s", resp.status_code)
    data = {}
    try:
        data = resp.json()
    except Exception:
        pass
    user_id = None
    if resp.status_code in (200, 201) and isinstance(data, dict):
        # try common response shapes
        user_id = data.get("data", {}).get("id") or data.get("id") or data.get("data")
    yield {"id": user_id, "payload": new_user_payload, "response": resp}
    # teardown: delete if created and API supports it
    if user_id:
        try:
            api.delete_user(user_id)
        except Exception:
            logger.exception("Failed to cleanup user %s", user_id)