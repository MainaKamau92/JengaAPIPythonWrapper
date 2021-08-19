import json

import requests

from src.jengaapi import API, COUNTRY_CODE, BASE_URL, MERCHANT_CODE
from src.jengaapi.exceptions import generate_reference, handle_response


class UncategorizedServices:
    def __init__(self, token=API.authorization_token, country_code=COUNTRY_CODE, currency_code="KES"):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }
        self.country_code = country_code
        self.currency_code = currency_code
        self.reference_no = generate_reference()

    def purchase_airtime(self, mobile_number, airtime_amount, telco):
        ref = self.reference_no
        signature = API.signature((MERCHANT_CODE, telco, airtime_amount, ref))
        self.headers["signature"] = signature
        payload = {
            "customer": {
                "countryCode": self.country_code,
                "mobileNumber": mobile_number
            },
            "airtime": {
                "amount": airtime_amount,
                "reference": ref,
                "telco": telco
            }
        }
        url = BASE_URL + f'transaction/v2/airtime'
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response

    def get_forex_rates(self):
        payload = {
            "countryCode": self.country_code,
            "currencyCode": self.currency_code
        }
        url = BASE_URL + f'transaction/v2/foreignexchangerates'

        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response

    def id_search_and_verification(self, document_type, **kwargs):
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        date_of_birth = kwargs.get("date_of_birth")
        document_number = kwargs.get("document_number")
        signature = API.signature((MERCHANT_CODE, document_number, self.country_code))
        self.headers["signature"] = signature
        payload = {
            "identity": {
                "documentType": document_type,
                "firstName": first_name,
                "lastName": last_name,
                "dateOfBirth": date_of_birth,
                "documentNumber": document_number,
                "countryCode": self.country_code
            }
        }
        url = BASE_URL + f'customer/v2/identity/verify'
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response
