import json
import os

def get_base_url():
    # Priority: BASE_URL env var overrides config; API_ENV selects file
    manual = os.environ.get("BASE_URL")
    if manual:
        return manual.rstrip('/')
    env = os.environ.get("API_ENV", "dev").lower()
    path = os.path.join(os.path.dirname(__file__), f"config_{env}.json")
    with open(path) as f:
        return json.load(f)["base_url"].rstrip('/')