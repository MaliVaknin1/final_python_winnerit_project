import pytest
from assertpy import assert_that
from api_requests.users_api import UsersApi
from utils.configs import USER_API_PARAMS, REQUIRED_KEYS, CREATE_USER_DATA, UPDATE_USER_DATA, DELAYED_RESPONSE_DATA
from utils.helpers import validate_json_structure

#Get JSON file and validate data-id and email are exist.
#Validate the status code is 200
def test_get_users():
    users_api = UsersApi()
    response = users_api.get_users(page=USER_API_PARAMS["page"])
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    validate_json_structure(response_json, REQUIRED_KEYS)
    user_data = response_json["data"]
    expected_user = {
        "id": USER_API_PARAMS["expected_id"],
        "email": USER_API_PARAMS["expected_email"]
    }
    assert any(
        all(user[key] == expected_user[key] for key in expected_user)
        for user in user_data
    ), "Expected user data isn't found in response"


#Find a user that not found and validate status code is 404 and JSON is empty
def test_user_not_found():
    users_api = UsersApi()
    user_id = 23
    response = users_api.get_user_by_id(user_id)
    assert_that(response.status_code).is_equal_to(404).described_as("Expected status code")
    response_json = response.json()
    assert_that(response_json).is_equal_to({}).described_as("Expected empty response JSON")

#Create a user and validate status code is 201 and JSON contains correct name and job
def test_create_user():
    users_api= UsersApi()
    response= users_api.create_user(name=CREATE_USER_DATA["name"], job=CREATE_USER_DATA["job"])
    assert response.status_code == 201,f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    assert 'id' in response_json
    assert response_json["name"] == CREATE_USER_DATA["name"]
    assert response_json["job"] == CREATE_USER_DATA["job"]

#Update username and job name and validate status code is 200 and data is updated.
def test_update_user_values():
    users_api = UsersApi()
    response = users_api.update_user(name=UPDATE_USER_DATA["name"], job=UPDATE_USER_DATA["job"])
    assert response.status_code==200, f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    assert response_json["name"] == UPDATE_USER_DATA["name"]
    assert response_json["job"] == UPDATE_USER_DATA["job"]

#Delete a user and validate status code is 204
def test_delete_user():
    users_api = UsersApi()
    response = users_api.delete_user()
    assert response.status_code == 204, f"Unexpected status code: {response.status_code}"

#Get users with delay and validate response structure and data
def test_get_users_with_delay():
    users_api = UsersApi()
    response = users_api.get_users_with_delay(delay=DELAYED_RESPONSE_DATA["delay"])
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    assert "data" in response_json
    assert response_json["per_page"] == DELAYED_RESPONSE_DATA["expected_per_page"]
    assert response_json["total"] == DELAYED_RESPONSE_DATA["expected_total"]
    assert response_json["total_pages"] == DELAYED_RESPONSE_DATA["expected_total_pages"]
    first_user = response_json["data"][0]
    expected_user = DELAYED_RESPONSE_DATA["expected_first_user"]
    assert first_user["id"] == expected_user["id"]
    assert first_user["email"] == expected_user["email"]
    assert first_user["first_name"] == expected_user["first_name"]
    assert first_user["last_name"] == expected_user["last_name"]
    assert first_user["avatar"] == expected_user["avatar"]


