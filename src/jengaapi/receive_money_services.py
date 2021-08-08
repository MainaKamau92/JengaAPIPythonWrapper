import json

import requests

from src.jengaapi import API, MERCHANT_CODE, COUNTRY_CODE, BASE_URL, PARTNER_ID, BILLER_CODE, PAYER_NAME, \
    PAYER_ACCOUNT
from src.jengaapi.exceptions import generate_reference, handle_response


class ReceiveMoneyService:
    def __init__(self, payment_amount, country_code, description=None, currency_code='KES'):
        self.token = API.authorization_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': API.authorization_token
        }
        self.reference_no = generate_reference()
        self.payment_amount = payment_amount or 0.00
        self.country_code = country_code or COUNTRY_CODE
        self.description = description
        self.currency_code = currency_code
        self.partner_id = PARTNER_ID
        self.biller_code = BILLER_CODE
        self.payer_name = PAYER_NAME
        self.payer_account = PAYER_ACCOUNT

    def receive_payments_eazzypay_push(self, mobile_number):
        signature = API.signature((self.reference_no, self.payment_amount,
                                   MERCHANT_CODE, COUNTRY_CODE))
        self.headers["signature"] = signature
        payload = {
            "customer": {
                "mobileNumber": mobile_number,
                "countryCode": self.country_code
            },
            "transaction": {
                "amount": self.payment_amount,
                "description": self.description,
                "type": "EazzyPayOnline",
                "reference": self.reference_no
            }
        }
        url = BASE_URL + 'transaction/v2/payments'
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response

    def receive_payments_bill_payments(self, **kwargs):
        ref = self.reference_no
        payer_name = kwargs.get("payer_name", self.payer_name)
        account = kwargs.get("account", self.payer_account)
        payer_mobile_number = kwargs.get("payer_mobile_number", self.payer_account)
        biller_code = kwargs.get("biller_code", self.biller_code)
        signature = API.signature((biller_code, self.payment_amount,
                                   ref, PARTNER_ID))
        self.headers["signature"] = signature

        payload = {
            "biller": {
                "billerCode": biller_code,
                "countryCode": self.country_code
            },
            "bill": {
                "reference": self.reference_no,
                "amount": self.payment_amount,
                "currency": self.currency_code
            },
            "payer": {
                "name": payer_name,
                "account": account,
                "reference": ref,
                "mobileNumber": payer_mobile_number
            },
            "partnerId": PARTNER_ID,
            "remarks": self.description
        }
        url = BASE_URL + 'transaction/v2/bills/pay'
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response

    def receive_payments_merchant_payments(self, merchant_till):
        ref = self.reference_no
        signature = API.signature((merchant_till, PARTNER_ID,
                                   self.payment_amount, self.currency_code, ref))
        self.headers["signature"] = signature

        payload = {
            "merchant": {
                "till": merchant_till
            },
            "payment": {
                "ref": self.reference_no,
                "amount": self.payment_amount,
                "currency": self.country_code
            },
            "partner": {
                "id": PARTNER_ID,
                "ref": self.reference_no
            }
        }
        url = BASE_URL + 'transaction/v2/tills/pay'
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response

    def bill_validation(self, biller_code, customer_ref_number):
        payload = {
            "billerCode": biller_code,
            "customerRefNumber": customer_ref_number,
            "amount": self.payment_amount,
            "amountCurrency": self.currency_code
        }
        url = BASE_URL + 'transaction/v2/tills/pay'
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response
