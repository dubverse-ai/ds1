import urllib.parse
import requests


class ExternalHTTPException(Exception):
    pass


class BaseHTTPClient:
    SUCCESS_RESPONSE_CODES = [200, 203, 300, 302, 301]

    def __init__(
        self,
        base_url,
        name="BaseHTTPClient",
        timeout=None,
        retries=None,
    ):
        self.base_url = base_url
        self.name = name
        self.timeout = timeout
        self.retries = retries

    def post(
        self,
        url,
        json=None,
        files=None,
        headers=None,
        raise_exception=True,
        success_response_codes=SUCCESS_RESPONSE_CODES,
    ):
        final_url = urllib.parse.urljoin(self.base_url, url)

        response = requests.post(
            final_url, json=json, files=files, headers=headers, timeout=self.timeout
        )

        if response.status_code not in success_response_codes and raise_exception:
            raise ExternalHTTPException(
                f"{self.name} failed with {response.status_code} while making POST request to {final_url}: {response.text}"
            )
        return response

    def get(
        self,
        url,
        params=None,
        headers=None,
        raise_exception=True,
        success_response_codes=SUCCESS_RESPONSE_CODES,
    ):
        final_url = urllib.parse.urljoin(self.base_url, url)

        response = requests.get(
            final_url, params=params, headers=headers, timeout=self.timeout
        )

        if response.status_code not in success_response_codes and raise_exception:
            raise ExternalHTTPException(
                f"{self.name} failed with {response.status_code} while making GET request to {final_url}: {response.text}"
            )
        return response

    def delete(
        self,
        url,
        headers=None,
        raise_exception=True,
        success_response_codes=SUCCESS_RESPONSE_CODES,
    ):
        final_url = urllib.parse.urljoin(self.base_url, url)

        response = requests.delete(final_url, headers=headers, timeout=self.timeout)

        if response.status_code not in success_response_codes and raise_exception:
            raise ExternalHTTPException(
                f"{self.name} failed with {response.status_code} while making DELETE request to {final_url}: {response.text}"
            )
        return response

    def patch(
        self,
        url,
        json=None,
        headers=None,
        raise_exception=True,
        success_response_codes=SUCCESS_RESPONSE_CODES,
    ):
        final_url = urllib.parse.urljoin(self.base_url, url)

        response = requests.patch(
            final_url, json=json, headers=headers, timeout=self.timeout
        )

        if response.status_code not in success_response_codes and raise_exception:
            raise ExternalHTTPException(
                f"{self.name} failed with {response.status_code} while making PATCH request to {final_url}: {response.text}"
            )
        return response
