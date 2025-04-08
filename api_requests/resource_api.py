import requests
from utils.configs import BASE_API_URL

class ResourceApi:
    def __init__(self):
        self.base_url = BASE_API_URL

    def get_resource_list(self):
        response = requests.get(f"{self.base_url}/unknown")
        return response

    def get_single_resource(self, resource_id: int):
        response = requests.get(f"{self.base_url}/unknown/{resource_id}")
        return response 