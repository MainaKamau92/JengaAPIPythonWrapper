from . import BASE_URL

from .utils import prepare_request_header, send_post_request


class ReceiveMoneyService:
    service_url = f'{BASE_URL}v3-apis/transaction-api/v3.0/'

    @classmethod
    def receive_payments_bill_payments(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}bills/pay"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def receive_payments_merchant_payments(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}tills/pay"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def bill_validation(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}bills/validation"
        return send_post_request(headers=headers, payload=payload, url=url)


receive_money_service = ReceiveMoneyService()
