import requests
from ds1.constants.url import URL
from ds1.exceptions import DubverseError


class User:
    def __init__(self, id, auth_token):
        """
        Initialize Users object with authentication token.

        Parameters:
        - auth_token (str): Authentication token for API requests.
        """
        self.name = "Webapp Client"
        self.base_url = URL.BASE_URL + URL.VERSION + URL.USER_URL
        self.token = auth_token
        self.request_header = self.get_headers_for_request()
        self.user = self._get_user(id)

    def get_headers_for_request(self):
        """
        Generate headers for API requests.

        Returns:
        - dict: Request headers.
        """
        return {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json",
        }

    def _get_user(self, user_id):
        """
        Retrieve user information by user ID.

        Parameters:
        - user_id (str): User ID.

        Returns:
        - dict: User information.

        Raises:
        - ValueError: If user ID is not provided.
        - DubverseError: If there is an issue with the API request.
        """
        if not user_id:
            raise ValueError("User ID not provided")

        request_url = f"{self.base_url}/{user_id}"

        try:
            response = requests.get(request_url, headers=self.request_header)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise DubverseError(f"Error in API request: {str(e)}")
