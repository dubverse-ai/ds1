import logging
from ds1.core.user import Users
from ds1.core.auth import Auth


class DubverseClient:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.auth_token = Auth(email, password).get_auth_token()
        self.users = Users(self.auth_token)
