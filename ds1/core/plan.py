from ds1.constants.url import URL
from ds1.resource import Resource


class Plan(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse Plan"
        self.base_url = URL.ADMIN_PREFIX + URL.PLAN_URL

