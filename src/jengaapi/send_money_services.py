from . import BASE_URL
from .utils import prepare_request_header, send_post_request


class SendMoneyService:

    service_url = f'{BASE_URL}v3-apis/transaction-api/v3.0/remittance/'

    @classmethod
    def send_within_equity(cls, signature: str, api_token: str, **payload: dict) -> dict:
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}internalBankTransfer"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_to_mobile_wallets(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}sendmobile"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_rtgs(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}rtgs"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_swift(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}swift"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_pesa_link_to_bank_account(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}pesalinkacc"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_pesa_link_to_mobile_number(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}pesalinkMobile"
        return send_post_request(headers=headers, payload=payload, url=url)


send_money_service = SendMoneyService()
