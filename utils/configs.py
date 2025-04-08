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

DELAYED_RESPONSE_DATA = {
    "delay": 3,
    "expected_per_page": 6,
    "expected_total": 12,
    "expected_total_pages": 2,
    "expected_first_user": {
        "id": 1,
        "email": "george.bluth@reqres.in",
        "first_name": "George",
        "last_name": "Bluth",
        "avatar": "https://reqres.in/img/faces/1-image.jpg"
    }
}

REGISTER_DATA = {
    "email": "eve.holt@reqres.in",
    "password": "pistol",
    "expected_id": 4,
    "expected_token": "QpwL5tke4Pnpja7X4"
}

UNSUCCESSFUL_REGISTER_DATA = {
    "email": "sydney@fife",
    "expected_error": "Missing password"
}

RESOURCES_DATA = {
    "expected_page": 1,
    "expected_per_page": 6,
    "expected_total": 12,
    "expected_total_pages": 2,
    "expected_first_resource": {
        "id": 1,
        "name": "cerulean",
        "year": 2000,
        "color": "#98B2D1",
        "pantone_value": "15-4020"
    }
}

SINGLE_RESOURCE_DATA = {
    "resource_id": 2,
    "expected_resource": {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031"
    }
}

NON_EXISTENT_RESOURCE_DATA = {
    "resource_id": 23
}
