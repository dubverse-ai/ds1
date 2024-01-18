from ...constants.url import URL
from ...resource import Resource

class Users(Resource):
    def __init__(self, client):
        # super().__init__(client)
        self.name = "Webapp Client"
        self.base_url = URL.BASE_URL + URL.VERSION + URL.USER_URL

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

        print(self.client.base_url)

        request_url = f"{self.base_url}/{user_id}"

        # try:
        #     response = requests.get(request_url, headers=self.request_header)
        #     response.raise_for_status()
        #     return response.json()
        # except requests.exceptions.RequestException as e:
        #     raise DubverseError(f"Error in API request: {str(e)}")
