# -*- coding: utf-8 -*-
"""Jenga API Send Money Service.

This module demonstrates documentation for the money sending service foe the Equity bank JengaAPI v3.
This web service covers all 6 countries (KE, RW, UG, TZ, DRC, SS) in which Equity Bank operates in.
Including:
- send_within_equity(self, signature: str, api_token: str, **payload: dict)
- send_to_mobile_wallets(self, signature: str, api_token: str, **payload: dict)
- send_rtgs(self, signature: str, api_token: str, **payload: dict)
- send_swift(self, signature: str, api_token: str, **payload: dict)
- send_pesalink_to_bank_account(self, signature: str, api_token: str, **payload: dict)
- send_pesalink_to_mobile_number(self, signature: str, api_token: str, **payload: dict)
"""
from json import JSONDecodeError
from typing import Union

import requests
from . import BASE_URL
from .exceptions import handle_response


class SendMoneyService:
    """Send Money Service Class. This class contains all the methods for the send money service.
    """

    @staticmethod
    def _prepare_request_header(signature: str, token: str) -> dict:
        """Prepare header for the send money request to the Jenga API

        Args:
            signature(str): A SHA-256 signature to proof that this request is coming from the merchant
            token(str): The bearer token used to access the API

        Returns:
            Dict object representing the headers for the request
        """
        return {
            "Authorization": token,
            "Content-Type": "application/json",
            "signature": signature
        }

    @staticmethod
    def _send_request(headers: dict, payload: dict, param=Union[str, None]) -> Union[dict, JSONDecodeError]:
        """Sends a request to the Jenga API and returns a `dict` object of the response.

        Args:
            headers(dict): A dict matching expected headers for the request.
            payload(dict): Dict of the expected body/payload of the request.
            param(str): Extra parameter to be appended to the base url.

        Returns:
            dict: A dict object of the response.
        """
        url = BASE_URL + f'v3-apis/transaction-api/v3.0/remittance/{param}'
        response = requests.post(url, json=payload, headers=headers)
        return handle_response(response)

    def send_within_equity(self, signature: str, api_token: str, **payload: dict) -> dict:
        """Handles funds dispatch within Equity Bank.

        Args:
            signature(str): A SHA-256 signature to proof that this request is coming from the merchant.
                       Built using a String of concatenated values of the request fields with the following order:
                       source.accountNumber,transfer.amount,transfer.currencyCode,transfer.reference.
                       The resulting text is then signed with Private Key and Base64 encoded.
            api_token: The Bearer token used to access the API
            **payload(dict): Expected details of the transaction. Which should take the shape of:
                      {
                       "source": {
                          "countryCode": "KE", # the sender's ISO country code
                          "name": "John Doe", # sender's full name
                          "accountNumber": "0011547896523" # sender's account number
                       },
                       "destination": {
                          "type": "bank", # the recipient's store of value. In this case its bank
                          "countryCode": "KE", # the recipient's ISO country code
                          "name": "Tom Doe", # recipient's full name
                          "accountNumber": "0060161911111" # recipient's account number
                       },
                       "transfer": {
                          "type": "InternalFundsTransfer", # the transfer type. In this case its InternalFundsTransfer.
                          "amount": "100.00", # the amount to be transferred
                          "currencyCode": "KES", # the amount's ISO currency
                          "reference": "742194625798", # the sender's reference number. unique 12 digit string for each
                                        transfer
                          "date": "2019-05-01", # the transfer date ISO 8601 date format 'YYYY-MM-DD'
                          "description": "Some remarks here" # any additional information the sender would like to add
                       }
                    }
        Returns:
            Dict payload response from the Jenga API
            Example Response:
            {
              "status": true,
              "code": 0,
              "message": "success",
              "data": {
                "transactionId": "54154",
                "status": "SUCCESS"
              }
            }
        """
        headers = self._prepare_request_header(signature, api_token)
        return self._send_request(headers=headers, payload=payload, param="internalBankTransfer")

    def send_to_mobile_wallets(self, signature: str, api_token: str, **payload: dict):
        """This enables your application to send money to telco wallets across Kenya, Uganda, Tanzania & Rwanda.
        Kindly note in order to get a response you will need to test this in production.

        Args:
            api_token: The Bearer token used to access the API
            signature(str): A SHA-256 signature to proof that this request is coming from the merchant.
                           Built using a String of concatenated values of the request fields with the following order:
                           source.accountNumber,transfer.amount,transfer.currencyCode,transfer.reference.
                           The resulting text is then signed with Private Key and Base64 encoded.
            **payload(dict): Expected details of the transaction. Which should take the shape of:
                          {
                             "source": {
                                  "countryCode": "KE", # the sender's ISO country code
                                  "name": "John Doe", # sender's full name
                                  "accountNumber": "0011547896523" # sender's account number
                               },
                             "destination": {
                                  "type": "mobile", # the recipient's store of value type. This will always be mobile
                                  "countryCode": "KE",# the recipient's ISO country code
                                  "name": "A N.Other",# the recipient's full name.
                                  "mobileNumber": "0763123456", # the recipient's number (e.g. 0763123456)
                                  "walletName": "Mpesa" # recipient's wallet name for example Airtel,Mpesa,Equitel
                             },
                             "transfer": {
                                  "type": "MobileWallet", # the transfer mode. set to MobileWallet
                                  "amount": "1000",
                                  "currencyCode": "KES",
                                  "date": "2018-08-18", # the transfer date ISO 8601 date format 'YYYY-MM-DD'
                                  "description": "some remarks here"
                             }
                        }
        Returns:
            Dict payload response from the Jenga API
            Example Response:
            {
                "status": true,
                "code": 0,
                "message": "success",
                "data": {
                  "transactionId": "",
                  "status": "SUCCESS"
                }
            }
        """
        headers = self._prepare_request_header(signature, api_token)
        return self._send_request(headers=headers, payload=payload, param="sendmobile")

    def send_rtgs(self, signature: str, api_token: str, **payload: dict):
        """The Real Time Gross Settlement (RTGS) web-service enables an application
        to send money intra-country to other bank accounts.

        Note:
            CDD - KYC & CFT: In line with various banking regulations your send money transaction will
                             be subjected to various verifications, you may be required to provide additional
                             information.
            Transaction Time: RTGS is available on weekdays between 9am and 3pm. If you send after these hours,
                              your transaction will be queued and sent at the next available transaction window.

        Args:
            api_token: The Bearer token used to access the API
            signature(str): A SHA-256 signature to proof that this request is coming from the merchant.
                           Built using a String of concatenated values of the request fields with the following order:
                           source.accountNumber,transfer.amount,transfer.currencyCode,transfer.reference.
                           The resulting text is then signed with Private Key and Base64 encoded.
            **payload(dict): Expected details of the transaction. Which should take the shape of:
                            {"source": {
                                    "countryCode": "KE",
                                    "name": "John Doe",
                                    "accountNumber": "0011547896523",
                                    "currency" : "KES"
                                },
                                "destination": {
                                    "type": "bank",
                                    "countryCode": "KE",
                                    "name": "Tom Doe",
                                    "bankCode": "70",
                                    "accountNumber": "12365489"
                                },
                                "transfer": {
                                    "type": "RTGS",
                                    "amount": "4.00",
                                    "currencyCode": "KES",
                                    "reference": "692194625798",
                                    "date": "2019-05-01",
                                    "description": "Some remarks here"
                                }}
        Returns:
            Dict payload response from the Jenga API
            Example Response:
            {
                "transactionId": "000000403777",
                "status": "SUCCESS"
            }
        """
        headers = self._prepare_request_header(signature, api_token)
        return self._send_request(headers=headers, payload=payload, param="rtgs")

    def send_swift(self, signature: str, api_token: str, **payload: dict):
        """The swift web-service enables your application to send cross-border remittances.

        Note:
            CDD - KYC & CFT: In line with various banking regulations your send money transaction will
                             be subjected to various verifications, you may be required to provide additional
                             information.
            Transaction Time: RTGS is available on weekdays between 9am and 3pm. If you send after these hours,
                              your transaction will be queued and sent at the next available transaction window.

        Args:
            api_token: The Bearer token used to access the API
            signature(str): A SHA-256 signature to proof that this request is coming from the merchant.
                           Built using a String of concatenated values of the request fields with the following order:
                           source.accountNumber,transfer.amount,transfer.currencyCode,transfer.reference.
                           The resulting text is then signed with Private Key and Base64 encoded.
            **payload(dict): Expected details of the transaction. Which should take the shape of:
                            {"source": {
                                  "countryCode": "KE",
                                  "name": "John Doe",
                                  "accountNumber": "0011547896523"
                               },
                               "destination": {
                                  "type": "bank",
                                  "countryCode": "JP",
                                  "name": "Tom Doe",
                                  "bankBic": "BOTKJPJTXXX",
                                  "accountNumber": "12365489",
                                  "addressline1": "Post Box 56" # recipient address
                               },
                               "transfer": {
                                  "type": "SWIFT",
                                  "amount": "4.00",
                                  "currencyCode": "USD",
                                  "reference": "692194625798",
                                  "date": "2019-05-01",
                                  "description": "Some remarks here",
                                  "chargeOption": "SELF" #  charge option. Can be one of SELF OTHER. SELF -
                                                            Correspondent bank charges are levied on us as the bank
                                                            hence we charge an upfront extra $20 on the sender to
                                                            cover for some of that cost. It will be reviewed upwards
                                                            from time to time OTHER - Correspondent bank charges are
                                                            levied on funds in transit
                               }}
        Returns:
            Dict payload response from the Jenga API
            Example Response:
            {
                "transactionId": "000000403777",
                "status": "SUCCESS"
            }
        """
        headers = self._prepare_request_header(signature, api_token)
        return self._send_request(headers=headers, payload=payload, param="swift")

    def send_pesalink_to_bank_account(self, signature: str, api_token: str, **payload: dict):
        """This web service enables an application to send money to a PesaLink participating bank.
        It is restricted to Kenya.

        Note:
            To check whether your recipient's bank is participating on PesaLink, go to;
            https://ipsl.co.ke/participating-banks/

        Args:
            api_token: The Bearer token used to access the API
            signature(str): A SHA-256 signature to proof that this request is coming from the merchant.
                           Built using a String of concatenated values of the request fields with the following order:
                           source.accountNumber,transfer.amount,transfer.currencyCode,transfer.reference.
                           The resulting text is then signed with Private Key and Base64 encoded.
            **payload(dict): Expected details of the transaction. Which should take the shape of:
                            {"source": {
                              "countryCode": "KE",
                              "name": "John Doe",
                              "accountNumber": "0011547896523"
                           },
                           "destination": {
                              "type": "bank",
                              "countryCode": "KE",
                              "name": "Tom Doe",
                              "bankCode": "63",
                              "accountNumber": "0090207635001"
                           },
                           "transfer": {
                              "type": "PesaLink",
                              "amount": "4.00",
                              "currencyCode": "KES",
                              "reference": "692194625798",
                              "date": "2019-05-01",
                              "description": "Some remarks here"
                           }}
        Returns:
            Dict payload response from the Jenga API
            Example Response:
            {
               "transactionId": "10000345333355",
               "status": "SUCCESS",
               "description": "Confirmed. Ksh 100 Sent to 01100762802910 -Tom Doe
                              from your account 1460163242696 on 20-05-2019 at 141313 Ref. 707700078800 Thank you"
            }
        """
        headers = self._prepare_request_header(signature, api_token)
        return self._send_request(headers=headers, payload=payload, param="pesalinkacc")

    def send_pesalink_to_mobile_number(self, signature: str, api_token: str, **payload: dict):
        """This web service enables an application to send money to a PesaLink participating bank.
        It is restricted to Kenya.

        Note:
            To check whether your recipient's bank is participating on PesaLink, go to;
            https://ipsl.co.ke/participating-banks/

        Args:
            api_token: The Bearer token used to access the API
            signature(str): A SHA-256 signature to proof that this request is coming from the merchant.
                           Built using a String of concatenated values of the request fields with the following order:
                           source.accountNumber,transfer.amount,transfer.currencyCode,transfer.reference.
                           The resulting text is then signed with Private Key and Base64 encoded.
            **payload(dict): Expected details of the transaction. Which should take the shape of:
                            {"source": {
                              "countryCode": "KE",
                              "name": "John Doe",
                              "accountNumber": "0011547896523"
                           },
                           "destination": {
                              "type": "mobile",
                              "countryCode": "KE",
                              "name": "Tom Doe",
                              "bankCode": "01",
                              "mobileNumber": "0722000000"
                           },
                           "transfer": {
                              "type": "PesaLink",
                              "amount": "40.00",
                              "currencyCode": "KES",
                              "reference": "692194625798",
                              "date": "2019-05-01",
                              "description": "Some remarks here"
                           }}
        Returns:
            Dict payload response from the Jenga API
            Example Response:
            {
                "status": true,
                "code": 0,
                "message": "success",
                "data": {
                    "description": "Confirmed. Ksh 100.0 sent to 254764000000- John Doe from your account 1464968850106
                    on Fri Jun 24 11:07:02 EAT 2022. Ref 041108128674. Thank you",
                    "transactionId": "041108128674",
                    "status": "SUCCESS"
                }
            }
        """
        headers = self._prepare_request_header(signature, api_token)
        return self._send_request(headers=headers, payload=payload, param="pesalinkMobile")


send_money_service = SendMoneyService()
