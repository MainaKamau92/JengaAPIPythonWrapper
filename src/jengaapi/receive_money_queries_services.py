from . import BASE_URL
from .utils import prepare_request_header, send_get_request


class ReceiveMoneyQueriesService:
    service_url = f'{BASE_URL}v3-apis/transaction-api/v3.0/'

    @classmethod
    def get_all_eazzy_pay_merchants(cls, api_token: str, page: int = 1, per_page: int = 1):
        headers = prepare_request_header(None, api_token)
        url = f"{cls.service_url}merchants?page={page}&per_page={per_page}"
        return send_get_request(headers=headers, url=url)

    @classmethod
    def query_transaction_details(cls, api_token: str, ref: str):
        headers = prepare_request_header(None, api_token)
        url = f"{cls.service_url}payments/details/{ref}"
        return send_get_request(headers=headers, url=url)

    @classmethod
    def get_all_billers(cls, api_token: str, page: int = 1, per_page: int = 1, category: str = None):
        headers = prepare_request_header(None, api_token)
        url = f"{cls.service_url}billers?page={page}&per_page={per_page}&category={category}"
        return send_get_request(headers=headers, url=url)


receive_money_queries_service = ReceiveMoneyQueriesService()
