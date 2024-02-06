import requests
from cachetools import TTLCache

from ds1.constants.url import URL
from ds1.exceptions import DubverseError


class Auth:
    def __init__(self, stage=False):
        self.name = "AuthClient"
        if stage:
            self.base_url = URL.STAGE_URL + URL.VERSION
        else:
            self.base_url = URL.BASE_URL + URL.VERSION
        self.cache = TTLCache(maxsize=1, ttl=86400)  # 86400 seconds = 1 day

    def verify_token(self, token):
        cached_response = self.cache.get(token)
        if cached_response:
            return cached_response

        try:
            url = self.base_url + URL.USER_URL
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            self.cache[token] = response_json

            return response_json
        except Exception as e:
            raise DubverseError(f"Verification Failed: {e}")

    def get_auth_token(self, email, password):
        url = self.base_url + URL.AUTH_URL
        payload = {
            "email": email,
            "password": password,
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json().get("token")
        except requests.exceptions.RequestException as e:
            raise DubverseError(f"Error Authorizing Client: {str(e)}")
