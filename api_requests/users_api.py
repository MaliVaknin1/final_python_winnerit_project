import requests
from utils.configs import BASE_API_URL

class UsersApi:
    def __init__(self):
        self.base_url = BASE_API_URL

    def get_users(self, page: int):
        response = requests.get(f"{self.base_url}/users", params={"page": page})
        return response