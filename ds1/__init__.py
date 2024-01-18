import logging

from .client import Client
from .core.users import Users


c = Client('hack4@dubverse.ai', 'localhost')
u = Users(c)
print(u.client)

