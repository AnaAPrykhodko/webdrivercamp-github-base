import requests
from base.components.response_api import ResponseAPI

# Add methods for sending requests
class ClientAPI():
    def get_request(self, url, headers=None):
        response = requests.get(url, headers=headers)
        return ResponseAPI(response)

    def post_request(self, url, payload, headers=None):
        response = requests.post(url, data=payload.to_json(), headers=headers)
        return ResponseAPI(response)

    def patch_request(self, url, payload, headers=None):
        response = requests.patch(url, data=payload.to_json(), headers=headers)
        return ResponseAPI(response)

    def delete_request(self, url, headers=None):
        response = requests.delete(url, headers=headers)
        return ResponseAPI(response)