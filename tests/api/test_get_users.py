import pytest
from api_requests.users_api import UsersApi
from utils.configs import USER_API_PARAMS
from utils.helpers import validate_json_structure



def test_get_users():
    users_api = UsersApi()
    response = users_api.get_users(page=USER_API_PARAMS["page"])
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    required_keys = ["data", "page", "total", "total_pages"]
    validate_json_structure(response_json, required_keys)
    user_data = response_json["data"]
    assert any(user["id"] == USER_API_PARAMS["expected_id"] for user in user_data), "Expected user ID not found"
    assert any(
        user["email"] == USER_API_PARAMS["expected_email"] for user in user_data), "Expected user email not found"
