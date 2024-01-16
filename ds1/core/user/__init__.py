import requests
from urllib import parse
from ds1.constants.url import URL


class Users:
    def __init__(self, auth_token):
        self.name = "Webapp Client"
        self.base_url = URL.BASE_URL + URL.USER_URL
        self.token = auth_token
        self.request_header = self.get_headers_for_request()

    def get_headers_for_request(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json",
        }

    def get(self, id):
        if not id:
            raise Exception("primary key not provided")

        request_url = parse.urljoin(self.base_url, f"/{id}")

        response = requests.get(request_url, headers=self.request_header)

        return response.json()
