from http.client import responses

import allure
import requests
from utils.configs import BASE_API_URL

class UsersApi:
    def __init__(self):
        self.base_url = BASE_API_URL

#function to get list of users by get call
    def get_users(self, page: int):
        with allure.step("Get all users by api request"):
            response = requests.get(f"{self.base_url}/users", params={"page": page})
            return response

    def get_users_with_delay(self, delay: int):
        with allure.step("Get all users with delay by api request"):
            response = requests.get(f"{self.base_url}/users", params={"delay": delay})
            return response

#function to get user by ID- get call
    def get_user_by_id(self, user_id: int):
        with allure.step("Get user by api request"):
            response = requests.get(f"{self.base_url}/users/{user_id}")
            return response
#function to create user by post call
    def create_user(self, name: str, job:str):
        with allure.step("Create user by api request"):
            response = requests.post(f"{self.base_url}/users", data={"name": name, "job": job})
            return response

#function to update username and job by put call
    def update_user(self, name: str, job:str ):
        with allure.step("Update user by api request"):
            response= requests.put(f"{self.base_url}/users/2", data={"name": name, "job": job})
            return response

#function to delete user by ID using delete call
    def delete_user(self):
        with allure.step("Delete user by api request"):
            response = requests.delete(f"{self.base_url}/users/2")
            return response