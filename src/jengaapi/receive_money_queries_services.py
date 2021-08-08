import requests

from src.jengaapi import API, UAT_BASE_URL
from src.jengaapi.exceptions import handle_response


class ReceiveMoneyQueriesService:

    def __init__(self):
        self.token = API.authorization_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': API.authorization_token
        }

    def get_all_eazzypay_merchants(self, per_page, page):
        url = UAT_BASE_URL + f'transaction/v2/merchants?per_page={per_page}&page={page}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response

    def get_payment_status_eazzy_pay_push(self, transaction_ref):
        url = UAT_BASE_URL + f'transaction/v2/payments/{transaction_ref}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response

    def query_transaction_details(self, payments_ref):
        url = UAT_BASE_URL + f'transaction/v2/payments/details/{payments_ref}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response

    def get_all_billers(self, per_page, page):
        url = UAT_BASE_URL + f'transaction/v2/billers?per_page={per_page}&page={page}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response
