import requests
from typing import Optional

class UserAPI:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout

    def create_user(self, payload: dict) -> requests.Response:
        return requests.post(f"{self.base_url}/api/v1/users", json=payload, timeout=self.timeout)

    def get_user(self, user_id: int) -> requests.Response:
        return requests.get(f"{self.base_url}/api/v1/users/{user_id}", timeout=self.timeout)

    def update_user(self, user_id: int, payload: dict) -> requests.Response:
        return requests.put(f"{self.base_url}/api/v1/users/{user_id}", json=payload, timeout=self.timeout)

    def delete_user(self, user_id: int) -> requests.Response:
        return requests.delete(f"{self.base_url}/api/v1/users/{user_id}", timeout=self.timeout)

    def batch_query_users(self, params: Optional[dict] = None) -> requests.Response:
        return requests.get(f"{self.base_url}/api/v1/users", params=params or {}, timeout=self.timeout)