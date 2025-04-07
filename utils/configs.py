BASE_UI_URL = "https://www.saucedemo.com"
BASE_API_URL = "https://reqres.in/api"
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
INVALID_USERNAME = "!!@6879"
PASSWORD = "secret_sauce"

USER_NAME_DATA = ["standard_user", "performance_glitch_user", "error_user", "visual_user"]

USER_API_PARAMS = {
    "page": 2,
    "expected_id": 7,
    "expected_email": "michael.lawson@reqres.in"
}
REQUIRED_KEYS = ["data", "page", "total", "total_pages"]

CREATE_USER_DATA={
    "name": "morpheus",
    "job": "leader"
}

UPDATE_USER_DATA={
    "name": "morpheus",
    "job": "zion resident"
}

LOGIN_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka",
    "expected_token": "QpwL5tke4Pnpja7X4"
}

INVALID_LOGIN_DATA = {
    "email": "eve.holt@reqres.in",
    "invalid_password": "wrongpassword",
    "expected_error": "user not found"
}

MISSING_PASSWORD_DATA = {
    "email": "eve.holt@reqres.in",
    "expected_error": "Missing password"
}


