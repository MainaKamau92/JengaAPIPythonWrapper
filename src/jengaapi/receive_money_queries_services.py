import requests

from src.jengaapi import API, BASE_URL
from src.jengaapi.exceptions import handle_response


class ReceiveMoneyQueriesService:

    def __init__(self):
        self.token = API.authorization_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': API.authorization_token
        }

    def get_all_eazzypay_merchants(self, per_page, page):
        """
        {'merchant': [
        {'name': 'NARAPU NGAI SOKO WOMEN GROUP', 'tillnumber': '0766123456'},
        {'name': 'ST AKIDIVA MEMORIAL HOSPITAL', 'tillnumber': '0766555002'},
        {'name': 'JOSIAH NJOROGE MUNGAI', 'tillnumber': '0766555003'},
        {'name': 'JEMIMAH NJOKI WACHIRA', 'tillnumber': '0766555004'},
        {'name': 'GEORGE JOSEPH NJOROGE', 'tillnumber': '0766555005'},
        {'name': 'SUSAN  BETT', 'tillnumber': '0766555006'},
        {'name': 'WILLIAM KARIUKI MACHARIA', 'tillnumber': '0766555016'},
        {'name': 'JAMES KAURA NJOROGE', 'tillnumber': '0766555020'},
        {'name': 'JOSEPH  NINGORI KILUSU', 'tillnumber': '0766555021'},
        {'name': 'MARTIN KARIUKI MAINGI', 'tillnumber': '0766555022'}
        ]}
        :param per_page:
        :param page:
        :return:
        """
        url = BASE_URL + f'transaction/v2/merchants?per_page={per_page}&page={page}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response

    def get_payment_status_eazzy_pay_push(self, transaction_ref):
        url = BASE_URL + f'transaction/v2/payments/{transaction_ref}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response

    def query_transaction_details(self, payments_ref):
        url = BASE_URL + f'transaction/v2/payments/details/{payments_ref}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response

    def get_all_billers(self, per_page, page):
        """
        {'billers': [{'name': 'KPLC LTD-COLLECTION A/C', 'code': '061001'},
        {'name': 'MAJAUJACKSON STEPHEN', 'code': '771654'},
        {'name': 'KNEC 1', 'code': '511000'},
        {'name': 'KNEC 2', 'code': '047002'}]}
        :param per_page:
        :param page:
        :return:
        """
        url = BASE_URL + f'transaction/v2/billers?per_page={per_page}&page={page}'
        response = requests.get(url, headers=self.headers)
        formatted_response = handle_response(response)
        return formatted_response
