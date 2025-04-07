import pytest
from assertpy import assert_that
from api_requests.login_api import LoginApi
from utils.configs import LOGIN_DATA, INVALID_LOGIN_DATA, MISSING_PASSWORD_DATA

  # Success login and Verify status code is 200 and verify response contains token
def test_successful_login():
    login_api = LoginApi()
    response = login_api.login(
        email=LOGIN_DATA["email"],
        password=LOGIN_DATA["password"]
    )
    assert_that(response.status_code).is_equal_to(200)
    response_json = response.json()
    assert_that(response_json).contains_key("token")
    assert_that(response_json["token"]).is_equal_to(LOGIN_DATA["expected_token"])

#Unsuccessful login and Verify status code is 400 and verify response contains error
def test_unsuccessful_login():
    login_api = LoginApi()
    response = login_api.login(
        email=MISSING_PASSWORD_DATA["email"],
        password=""
    )
    assert_that(response.status_code).is_equal_to(400)
    response_json = response.json()
    assert_that(response_json).contains_key("error")
    assert_that(response_json["error"]).is_equal_to(MISSING_PASSWORD_DATA["expected_error"])


