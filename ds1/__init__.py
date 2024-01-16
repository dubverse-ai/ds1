import logging
from ds1.client import Client
from ds1.core.users import Users
from ds1.core.auth import Auth


class DubverseClient:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.client = Client(email, password)
