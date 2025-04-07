import requests
from utils.configs import BASE_API_URL

class LoginApi:
    def __init__(self):
        self.base_url = BASE_API_URL

#Function to login  with email and password
    def login(self, email: str, password: str):
        response = requests.post(
            f"{self.base_url}/login",
            json={"email": email, "password": password}
        )
        return response 