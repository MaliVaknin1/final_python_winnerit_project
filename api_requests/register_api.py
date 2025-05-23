import allure
import requests
from utils.configs import BASE_API_URL

class RegisterApi:
    def __init__(self):
        self.base_url = BASE_API_URL
        
#Function to register with email and password
    def register(self, email: str, password: str):
        with allure.step(f"Registration by api request"):
            response = requests.post(
                f"{self.base_url}/register",
                json={"email": email, "password": password}
            )
            return response
