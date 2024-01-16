import logging
from ds1.core.user import User
from ds1.core.auth import Auth


class DubverseClient:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.auth_token = Auth(email, password).get_auth_token()
        self.user = self.initialize_user

    def initialize_user(self, user_id):
        """
        Initialize the User object with the provided user ID.

        Parameters:
        - user_id (str): User ID.
        """
        if not self.auth_token:
            raise ValueError(
                "Authentication token not available. Call 'get_auth_token' first."
            )

        self.user = User(user_id, self.auth_token)
