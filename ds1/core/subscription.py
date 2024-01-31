from ds1.constants.url import URL
from ds1.resource import Resource


class Subscription(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse Subscription"
        self.base_url = URL.ADMIN_PREFIX + URL.SUBSCRIPION_URL
