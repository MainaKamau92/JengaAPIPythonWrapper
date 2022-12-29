from . import BASE_URL
from .utils import prepare_request_header, send_get_request, send_post_request


class AccountServices:
    service_url = f'{BASE_URL}v3-apis/account-api/v3.0/accounts/'

    @classmethod
    def account_balance(cls, signature: str, api_token: str, country_code: str, account_id: str):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}balances/{country_code}/{account_id}"
        return send_get_request(headers, url)

    @classmethod
    def account_mini_statement(cls, signature: str, api_token: str, country_code: str, account_no: str):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}ministatement/{country_code}/{account_no}"
        return send_get_request(headers, url)

    @staticmethod
    def account_inquiry_bank_accounts(signature: str, api_token: str, country_code: str, account_no: str):
        headers = prepare_request_header(signature, api_token)
        url = f"{BASE_URL}v3-apis/account-api/v3.0/search/{country_code}/{account_no}"
        print(url)
        return send_get_request(headers, url)

    @classmethod
    def opening_closing_account_balance(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}accountbalance/query"
        return send_post_request(headers=headers, payload=payload, url=url)

    @classmethod
    def account_full_statement(cls, signature: str, api_token: str, **payload: dict):
        headers = prepare_request_header(signature, api_token)
        url = f"{cls.service_url}fullstatement"
        return send_post_request(headers=headers, payload=payload, url=url)


account_services = AccountServices()
