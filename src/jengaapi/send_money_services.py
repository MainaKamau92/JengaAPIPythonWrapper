import json
from datetime import date

import requests

from src.jengaapi import API, BASE_URL, COUNTRY_CODE, ACCOUNT_NO
from src.jengaapi.exceptions import handle_response, generate_reference


class SendMoneyService:

    def __init__(self, transfer_date, transfer_amount, **kwargs):
        self.transfer_date = transfer_date or date.today()
        self.transfer_amount = transfer_amount or 0.00
        self.currency_code = kwargs.get('currency_code', 'KES')
        self.country_code = kwargs.get('country_code', COUNTRY_CODE)
        self.source_name = kwargs.get('source_name', "John Doe")
        self.source_account_number = kwargs.get('source_account_number', ACCOUNT_NO)
        self.destination_name = kwargs.get('destination_name', "Jane Doe")
        self.description = kwargs.get('description', "Sending money")
        self.reference_no = generate_reference()
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': API.authorization_token
        }
        self.payload_source = dict(
            countryCode=self.country_code,
            name=self.source_name,
            accountNumber=self.source_account_number
        )
        self.payload_destination = dict(
            type=None,
            countryCode=self.country_code,
            name=self.destination_name,
        )
        self.payload_transfer = dict(
            type=None,
            amount=str(transfer_amount),
            currencyCode=self.currency_code,
            reference=self.reference_no,
            date=transfer_date.strftime("%Y-%m-%d"),
            description=self.description
        )

    @staticmethod
    def _send_request(headers, payload):
        url = BASE_URL + f'transaction/v2/remittance'
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        formatted_response = handle_response(response)
        return formatted_response

    def send_within_equity(self, destination_account_number):

        signature = API.signature((self.source_account_number, self.transfer_amount,
                                   self.currency_code, self.reference_no))
        self.headers["signature"] = signature
        self.payload_destination["type"] = "bank"
        self.payload_destination["accountNumber"] = destination_account_number
        self.payload_transfer["type"] = "InternalFundsTransfer"
        payload = dict(source=self.payload_source,
                       destination=self.payload_destination,
                       transfer=self.payload_transfer)
        return self._send_request(headers=self.headers, payload=payload)

    def send_to_mobile_wallets(self, wallet_name, destination_mobile_number):
        if wallet_name == 'Equitel':
            signature = API.signature((self.source_account_number, self.transfer_amount,
                                       self.currency_code, self.reference_no))
        else:
            signature = API.signature((self.transfer_amount, self.currency_code,
                                       self.reference_no, self.source_account_number))
        self.headers["signature"] = signature
        self.payload_destination["type"] = "mobile"
        self.payload_destination["mobileNumber"] = destination_mobile_number
        self.payload_destination["walletName"] = wallet_name
        self.payload_transfer["type"] = "MobileWallet"
        payload = dict(source=self.payload_source,
                       destination=self.payload_destination,
                       transfer=self.payload_transfer)
        return self._send_request(headers=self.headers, payload=payload)

    def send_rtgs(self, destination_account_number, bank_code):
        signature = API.signature((self.reference_no, self.transfer_date,
                                   self.source_account_number, destination_account_number,
                                   self.transfer_amount))

        self.headers["signature"] = signature
        self.payload_destination["type"] = "bank"
        self.payload_destination["bankCode"] = bank_code
        self.payload_destination["accountNumber"] = destination_account_number
        self.payload_transfer["type"] = "RTGS"
        payload = dict(source=self.payload_source,
                       destination=self.payload_destination,
                       transfer=self.payload_transfer)
        return self._send_request(headers=self.headers, payload=payload)

    def send_swift(self, destination_account_number, **kwargs):
        bank_bic = kwargs.get('bank_bic')
        address_line = kwargs.get('address_line')
        charge_option = kwargs.get('charge_option')

        signature = API.signature((self.reference_no, self.transfer_date,
                                   self.source_account_number, destination_account_number,
                                   self.transfer_amount))
        self.headers["signature"] = signature
        self.payload_destination["type"] = "bank"
        self.payload_destination["bankBic"] = bank_bic
        self.payload_destination["accountNumber"] = destination_account_number
        self.payload_destination["addressline1"] = address_line
        self.payload_transfer["type"] = "SWIFT"
        self.payload_transfer["chargeOption"] = charge_option
        payload = dict(source=self.payload_source,
                       destination=self.payload_destination,
                       transfer=self.payload_transfer)
        return self._send_request(headers=self.headers, payload=payload)

    def send_eft(self, destination_account_number, **kwargs):

        bank_code = kwargs.get('bank_code')
        branch_code = kwargs.get('branch_code')

        signature = API.signature((self.reference_no, self.source_account_number,
                                   destination_account_number, self.transfer_amount,
                                   bank_code))

        self.headers["signature"] = signature
        self.payload_destination["type"] = "bank"
        self.payload_destination["bankCode"] = bank_code
        self.payload_destination["branchCode"] = branch_code
        self.payload_destination["accountNumber"] = destination_account_number
        self.payload_transfer["type"] = "EFT"
        payload = dict(source=self.payload_source,
                       destination=self.payload_destination,
                       transfer=self.payload_transfer)
        return self._send_request(headers=self.headers, payload=payload)

    def send_pesalink_to_bank_account(self, destination_account_number, **kwargs):
        bank_code = kwargs.get('bank_code')
        mobile_number = kwargs.get('mobile_number')

        signature = API.signature((self.transfer_amount, self.currency_code, self.reference_no,
                                   self.destination_name, self.source_account_number))

        self.headers["signature"] = signature
        self.payload_destination["type"] = "bank"
        self.payload_destination["bankCode"] = bank_code
        self.payload_destination["mobileNumber"] = mobile_number
        self.payload_destination["accountNumber"] = destination_account_number
        self.payload_transfer["type"] = "PesaLink"
        payload = dict(source=self.payload_source,
                       destination=self.payload_destination,
                       transfer=self.payload_transfer)
        return self._send_request(headers=self.headers, payload=payload)

    def send_pesalink_to_mobile_number(self, destination_mobile_number, **kwargs):
        bank_code = kwargs.get('bank_code')
        signature = API.signature((self.transfer_amount, self.currency_code,
                                   self.reference_no, self.destination_name,
                                   self.source_account_number))

        self.headers["signature"] = signature
        self.payload_destination["type"] = "mobile"
        self.payload_destination["bankCode"] = bank_code
        self.payload_destination["mobileNumber"] = destination_mobile_number
        payload = dict(source=self.payload_source,
                       destination=self.payload_destination,
                       transfer=self.payload_transfer)
        return self._send_request(headers=self.headers, payload=payload)
