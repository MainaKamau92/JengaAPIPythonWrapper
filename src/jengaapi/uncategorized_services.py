from typing import Union

from . import BASE_URL
from .utils import prepare_request_header, send_post_request


class MiscellaneousServices:
    service_url = f'{BASE_URL}v3-apis/'

    @classmethod
    def purchase_airtime(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}transaction-api/v3.0/airtime"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def get_forex_rates(cls, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}transaction-api/v3.0/foreignExchangeRates"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def kyc(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}v3.0/validate/identity"
        return send_post_request(headers=headers, payload=payload, url=url)


miscellaneous_services = MiscellaneousServices()
