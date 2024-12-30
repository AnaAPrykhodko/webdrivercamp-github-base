import requests
from response_api import ResponseAPI

# Add methods for sending requests
class ClientAPI():
    def get_request(self, url, headers=None):
        response = requests.get(url, headers)
        response.raise_for_status()
        return ResponseAPI(response)

    def post_request(self, url, payload, headers=None):
        response = requests.post(url, payload.to_json(), headers)
        response.raise_for_status()
        return ResponseAPI(response)

    def patch_request(self, url, payload, headers=None):
        response = requests.patch(url, payload.to_json(), headers)
        response.raise_for_status()
        return ResponseAPI(response)

    def delete_request(self, url, headers=None):
        response = requests.get(url, headers)
        response.raise_for_status()
        return ResponseAPI(response)