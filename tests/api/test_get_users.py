import pytest
from assertpy import assert_that

from api_requests.users_api import UsersApi
from utils.configs import USER_API_PARAMS
from utils.helpers import validate_json_structure

#Get JSON file and validate data-id and email are exist.
#Validate the status code is 200
def test_get_users():
    users_api = UsersApi()
    response = users_api.get_users(page=USER_API_PARAMS["page"])
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    required_keys = ["data", "page", "total", "total_pages"]
    validate_json_structure(response_json, required_keys)
    user_data = response_json["data"]
    assert_that(user_data).contains(
        {"id": USER_API_PARAMS["expected_id"], "email": USER_API_PARAMS["expected_email"]
         }).described_as("Expected user data isn't found in response")
