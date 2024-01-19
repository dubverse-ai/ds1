from ..constants.url import URL
from ..resource import Resource


class Subscripton(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse Subscription"
        self.base_url = URL.SUBSCRIPION_URL

