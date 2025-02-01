from enum import Enum


class ERRORS(Enum):
    INCORRECT_USERNAME_ERROR = "Epic sadface: Username and password do not match any user in this service"
    EMPTY_PASSWORD_FIELD_ERROR = "Epic sadface: Password is required"
    LOCKED_OUT_USER_ERROR = "Epic sadface: Sorry, this user has been locked out."
    EMPTY_USERNAME_FIELD_ERROR = "Epic sadface: Username is required"
