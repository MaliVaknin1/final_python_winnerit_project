import pytest
from assertpy import assert_that
from api_requests.register_api import RegisterApi
from utils.configs import REGISTER_DATA, UNSUCCESSFUL_REGISTER_DATA

#Successfully register and Verify status code is 200 and verify response contains id and token
def test_successful_register():
    register_api = RegisterApi()
    response = register_api.register(
        email=REGISTER_DATA["email"],
        password=REGISTER_DATA["password"]
    )
    assert_that(response.status_code).is_equal_to(200)
    response_json = response.json()
    assert_that(response_json).contains_key("id")
    assert_that(response_json).contains_key("token")
    assert_that(response_json["id"]).is_equal_to(REGISTER_DATA["expected_id"])
    assert_that(response_json["token"]).is_equal_to(REGISTER_DATA["expected_token"])

#Unsuccessful register and Verify status code is 400 and verify response contains error
def test_unsuccessful_register():
    register_api = RegisterApi()
    response = register_api.register(
        email=UNSUCCESSFUL_REGISTER_DATA["email"], 
        password=""
    )
    assert_that(response.status_code).is_equal_to(400)
    response_json = response.json()
    assert_that(response_json).contains_key("error")
    assert_that(response_json["error"]).is_equal_to(UNSUCCESSFUL_REGISTER_DATA["expected_error"]) 