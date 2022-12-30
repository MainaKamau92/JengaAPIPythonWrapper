from . import BASE_URL
from .utils import prepare_request_header, send_post_request


class SendMoneyIMTService:

    service_url = f'{BASE_URL}v3-apis/transaction-api/v3.0/remittance/'

    @classmethod
    def send_within_equity(cls, signature: str, api_token: str, **payload: dict) -> dict:
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}internalBankTransfer/imt"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_to_mobile_wallets(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}sendmobile/imt"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_pesa_link_to_bank_account(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}pesalinkacc/imt"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def send_pesa_link_to_mobile_number(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}pesalinkMobile/imt"
        return send_post_request(headers=headers, payload=payload, url=url)


send_money_imt_service = SendMoneyIMTService()
