from requests.exceptions import (ConnectionError, HTTPError, RequestException,
                                 Timeout)

from ds1.constants.url import URL
from ds1.exceptions import DubverseError
from ds1.resource import Resource


class TTSError(DubverseError):
    """Base exception for TTS related errors"""

    pass


class TTSBillingError(TTSError):
    """Exception for billing specific errors"""

    pass


class TTSPricingError(TTSError):
    """Exception for pricing specific errors"""

    pass


class TTS(Resource):
    def __init__(self, client):
        super().__init__(client=client)
        self.name = "Dubverse TTS Service Billing"
        self.base_url = URL.TTS_SERVICE

    def get_pricing(self, speaker_type=None):
        """
        Get pricing information for TTS services.

        Args:
            speaker_type (str, optional): Type of speaker for pricing info

        Returns:
            dict: Pricing information

        Raises:
            TTSPricingError: If there's an error fetching pricing information
            ConnectionError: If there's a network connectivity issue
            Timeout: If the request times out
        """
        try:
            if speaker_type:
                res = self.get_url(self.base_url + URL.TTS_PRICING + f"/{speaker_type}")
            else:
                res = self.get_url(self.base_url + URL.TTS_PRICING)
            return res
        except Timeout as e:
            raise TTSPricingError(
                f"Timeout while fetching pricing information: {str(e)}"
            )
        except ConnectionError as e:
            raise TTSPricingError(f"Network error while fetching pricing: {str(e)}")
        except HTTPError as e:
            if e.response.status_code == 404:
                raise TTSPricingError(f"Invalid speaker type: {speaker_type}")
            elif e.response.status_code == 403:
                raise TTSPricingError("Unauthorized access to pricing information")
            else:
                raise TTSPricingError(f"HTTP error while fetching pricing: {str(e)}")
        except RequestException as e:
            raise TTSPricingError(f"Error fetching pricing information: {str(e)}")
        except Exception as e:
            raise TTSPricingError(f"Unexpected error while fetching pricing: {str(e)}")

    def create_billing(self, user_id, usage_logs):
        """
        Create billing entry for TTS usage.

        Args:
            user_id (str): ID of the user
            usage_logs (list): List of usage logs for billing

        Returns:
            dict: Billing creation response

        Raises:
            TTSBillingError: If there's an error in billing creation
            ValueError: If input parameters are invalid
            ConnectionError: If there's a network connectivity issue
            Timeout: If the request times out
        """
        if not user_id:
            raise ValueError("user_id cannot be empty")
        if not usage_logs or not isinstance(usage_logs, list):
            raise ValueError("usage_logs must be a non-empty list")

        try:
            res = self.post_url(
                self.base_url + URL.TTS_CREATE_BILLING,
                data={"user_id": user_id, "usage_logs": usage_logs},
                timeout=300,  # 5 minute timeout for billing operations
            )
            return res
        except Timeout as e:
            raise TTSBillingError(
                f"Billing creation timed out after 300 seconds. Please verify the billing status: {str(e)}"
            )
        except ConnectionError as e:
            raise TTSBillingError(
                f"Network error during billing creation. Please verify the billing status: {str(e)}"
            )
        except HTTPError as e:
            if e.response.status_code == 400:
                raise TTSBillingError("Invalid billing data provided")
            elif e.response.status_code == 403:
                raise TTSBillingError("Unauthorized access for billing creation")
            elif e.response.status_code == 404:
                raise TTSBillingError(f"Invalid user_id: {user_id}")
            elif e.response.status_code == 409:
                raise TTSBillingError("Duplicate billing entry detected")
            else:
                raise TTSBillingError(f"HTTP error during billing creation: {str(e)}")
        except RequestException as e:
            raise TTSBillingError(f"Error creating billing entry: {str(e)}")
        except Exception as e:
            raise TTSBillingError(f"Unexpected error during billing creation: {str(e)}")
