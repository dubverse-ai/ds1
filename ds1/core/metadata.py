from ds1.constants.url import URL
from ds1.resource import Resource


class Metadata(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse Metadata"
        self.base_url = URL.ADMIN_PREFIX + URL.METADATA_URL

    def get_for_user(self, user_id):
        res = self.all(params={"user": f"{user_id}"})

        if len(res) == 1:
            return res[0]
        else:
            raise Exception(f"Error Fetching {self.name} for User: {user_id}")
