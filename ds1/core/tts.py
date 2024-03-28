from ds1.constants.url import URL
from ds1.resource import Resource


class TTS(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse TTS Service Billing"
        self.base_url = URL.TTS_SERVICE

    def get_pricing(self, speaker_type=None):
        if speaker_type:
            res = self.get_url(self.base_url + URL.TTS_PRICING + f"/{speaker_type}")
        else:
            res = self.get_url(self.base_url + URL.TTS_PRICING)
        return res

    def create_billing(
        self,
        user_id,
        total_cost,
        currency,
        usage_characters=0,
        usage_duration=0,
    ):
        res = self.post_url(
            self.base_url + URL.TTS_CREATE_BILLING,
            data={
                "user_id": user_id,
                "total_cost": total_cost,
                "currency": currency,
                "usage_characters": usage_characters,
                "usage_duration": usage_duration,
            },
        )

        return res
