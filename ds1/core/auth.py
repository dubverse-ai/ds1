import requests
from urllib import parse


class Auth:
    def __init__(self, email, password, base_url="http://localhost:8000"):
        self.name = "AuthClient"
        self.email = email
        self.password = password
        self.base_url = base_url

    def get_auth_token(self):
        url = "api/v3/auth/login"
        request_url = parse.urljoin(self.base_url, url)
        payload = {
            "email": self.email,
            "password": self.password,
        }
        response = requests.post(request_url, payload)
        return response.json().get("token")
