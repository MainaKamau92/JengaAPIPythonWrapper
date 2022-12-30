from typing import Union

from src.jengaapi import BASE_URL
from src.jengaapi.utils import prepare_request_header, send_post_request


class MPGSDirectIntegration:
    service_url = f'{BASE_URL}mpgs-direct-integration/api/v3.1/'

    @classmethod
    def mpgs_validate_payment(cls, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}validatePayment"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def mpgs_authenticate_payment(cls, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}authenticatePayment"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def mpgs_authorize_payment(cls, signature: Union[None, str], api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}authorizePayment"
        return send_post_request(headers=headers, payload=payload, url=url)





mpgs_direct_integration = MPGSDirectIntegration()