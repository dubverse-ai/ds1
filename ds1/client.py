import json

import requests

from ds1.core.user import User

from ds1.constants.url import URL
from ds1.core.auth import Auth
from ds1.exceptions import DubverseError


class Client:
    DEFAULTS = {"base_url": URL.BASE_URL + URL.VERSION}

    def __init__(self, email, password, **options):
        self.email = email
        self.password = password
        self.base_url = self._set_base_url()
        self.auth_token = Auth(email, password).get_auth_token()
        self.session = self._get_session()
        self.user = User(client=self)

    def _set_base_url(self, **options):
        return options.get("base_url", URL.BASE_URL + URL.VERSION)

    def _get_headers_for_request(self):
        return {
            "Authorization": f"Bearer {self.auth_token}",
            "accept": "application/json",
        }

    def _get_session(self):
        s = requests.Session()
        s.headers.update(self._get_headers_for_request())
        return s

    def request(self, method, path, **options):
        url = f"{self.base_url}{path}"

        try:
            response = self.session.request(method=method, url=url, **options)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise DubverseError(f"Error Authorizing Client: {str(e)}")

    def get(self, path, params=None, **options):
        return self.request("get", path, params=params, **options)

    def post(self, path, data, **options):
        data, options = self._update_request(data, options)
        return self.request("post", path, data=data, **options)

    def patch(self, path, data, **options):
        data, options = self._update_request(data, options)
        return self.request("patch", path, data=data, **options)

    def delete(self, path, data, **options):
        data, options = self._update_request(data, options)
        return self.request("delete", path, data=data, **options)

    def put(self, path, data, **options):
        data, options = self._update_request(data, options)
        return self.request("put", path, data=data, **options)

    def file(self, path, data, **options):
        fileDict = {}
        fieldDict = {}

        if "file" not in data:
            data["file"] = ""

        fileDict["file"] = data["file"]

        for fields in data:
            if fields != "file":
                fieldDict[str(fields)] = data[fields]

        return self.request("post", path, files=fileDict, data=fieldDict, **options)

    def _update_request(self, data, options):
        data = json.dumps(data)

        if "headers" not in options:
            options["headers"] = {}

        options["headers"].update({"Content-type": "application/json"})

        return data, options
