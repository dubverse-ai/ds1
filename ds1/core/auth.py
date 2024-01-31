import requests
from ds1.constants.url import URL

from ds1.exceptions import DubverseError


class Auth:
    def __init__(self):
        """
        Initialize Auth object with user credentials and base URL.

        Parameters:
        - email (str): User email.
        - password (str): User password.
        - base_url (str): Base URL of the authentication service
        """
        self.name = "AuthClient"
        self.base_url = URL.BASE_URL + URL.VERSION + URL.AUTH_URL

    def get_auth_token(self, email, password):
        """
        Retrieve authentication token by making a POST request to the login endpoint.

        Returns:
        - str: Authentication token.

        Raises:
        - requests.exceptions.RequestException: If there is an issue with the API request.
        """
        payload = {
            "email": email,
            "password": password,
        }

        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            return response.json().get("token")
        except requests.exceptions.RequestException as e:
            raise DubverseError(f"Error Authorizing Client: {str(e)}")

    def verify_token(self, token):
        try:
            url = URL.BASE_URL + URL.VERSION + URL.USER_URL
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(url, headers=headers)
            return response.json()
        except Exception as e:
            raise DubverseError(f"Verification Failed: {e}")
