from ds1.constants.url import URL
from ds1.resource import Resource


class Config(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse User Config"
        self.base_url = URL.ADMIN_PREFIX + URL.CONFIG_URL

    def get_for_user(self, user_id):
        res = self.all(params={"user": f"{user_id}"})

        if len(res) == 1:
            return res[0]
        else:
            raise Exception(f"Error Fetching {self.name} for User: {user_id}")
