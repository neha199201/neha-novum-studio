# User Management API Automation Framework

This repository contains an API automation testing framework for a sample User Management API.

## Features
- Tests for Create, Get, Update, Delete and Batch Query endpoints
- Positive and negative test cases
- Allure reporting compatible
- Multi-environment configuration via `config/config_{env}.json` or `BASE_URL` env var
- Dynamic test data generation

## Project structure
```
api/           # API wrapper layer
common/        # logger, assertions, utils
config/        # environment config files
testcases/     # pytest test suites
reports/       # allure report output
```

## Setup
1. Create a virtualenv and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure the base URL:
   - `config/config_dev.json` is pre-set to `https://reqres.in` (a public mock API).  
   - To override, set `BASE_URL` environment variable:
     ```bash
     export BASE_URL="https://your-api.example.com"
     ```
   - Or switch environment via:
     ```bash
     export API_ENV=stage
     ```

3. Run tests:
```bash
pytest --alluredir=reports
```

4. Serve allure report (if allure CLI installed):
```bash
allure serve reports
```

## Notes
- The tests assume the API responds with JSON objects similar to the assignment screenshots:
  `{ "code":200, "data": {...}, "msg":"success" }` but are defensive to support slightly different shapes (e.g., reqres).
- Tests are defensive and will skip if the setup step (user creation) fails.