import json
from datetime import date

import requests

from src.jengaapi import API, COUNTRY_CODE, ACCOUNT_ID, ACCOUNT_NO, UAT_BASE_URL
from src.jengaapi.exceptions import handle_response


class AccountServices:

    def __init__(self):
        self.token = API.authorization_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': API.authorization_token
        }

    @staticmethod
    def _send_get_request(headers, url):
        response = requests.get(url, headers=headers)
        formatted_response = handle_response(response)
        return formatted_response

    @staticmethod
    def _send_post_request(headers, payload, url):
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response

    def account_balance(self):
        signature = API.signature((COUNTRY_CODE, ACCOUNT_ID))
        self.headers["signature"] = signature
        url = UAT_BASE_URL + f'account/v2/accounts/balances/{COUNTRY_CODE}/{ACCOUNT_ID}'
        return self._send_get_request(headers=self.headers, url=url)

    def account_mini_statement(self):
        signature = API.signature((COUNTRY_CODE, ACCOUNT_ID))
        self.headers["signature"] = signature
        url = UAT_BASE_URL + f'account/v2/accounts/ministatement/{COUNTRY_CODE}/{ACCOUNT_ID}'
        return self._send_get_request(headers=self.headers, url=url)

    def account_inquiry_bank_accounts(self):
        signature = API.signature((COUNTRY_CODE, ACCOUNT_ID))
        self.headers["signature"] = signature
        url = UAT_BASE_URL + f'account/v2/accounts/search/{COUNTRY_CODE}/{ACCOUNT_NO}'
        return self._send_get_request(headers=self.headers, url=url)

    def opening_closing_account_balance(self, balance_date=date.today()):
        str_date = balance_date.strftime("%Y-%m-%d")
        signature = API.signature((ACCOUNT_ID, COUNTRY_CODE, str_date))
        self.headers["signature"] = signature
        payload = {
            "countryCode": COUNTRY_CODE,
            "accountId": ACCOUNT_ID,
            "date": str_date
        }
        url = UAT_BASE_URL + 'account/v2/accounts/accountbalance/query'
        return self._send_post_request(headers=self.headers, payload=payload, url=url)

    def account_full_statement(self, from_date, to_date, limit=3, **kwargs):
        reference = kwargs.get("reference", None)
        serial = kwargs.get("serial", None)
        posted_date_time = kwargs.get("posted_date_time", None)
        signature = API.signature((COUNTRY_CODE, ACCOUNT_ID))
        self.headers["signature"] = signature
        payload = {
            "countryCode": COUNTRY_CODE,
            "accountNumber": ACCOUNT_NO,
            "fromDate": from_date.strftime("%Y-%m-%d"),
            "toDate": to_date.strftime("%Y-%m-%d"),
            "limit": limit,
            "reference": reference,
            "serial": serial,
            "postedDateTime": posted_date_time,
            "date": date.today().strftime("%Y-%m-%d"),
        }

        url = UAT_BASE_URL + 'account/v2/accounts/fullstatement'
        return self._send_post_request(headers=self.headers, payload=payload, url=url)
