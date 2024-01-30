from ds1.constants.url import URL
from ds1.resource import Resource


class Config(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse User Config"
        self.base_url = URL.CONFIG_URL
