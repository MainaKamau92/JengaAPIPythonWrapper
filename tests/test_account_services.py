from unittest import mock

from src.jengaapi.configs.config import app_config
from src.jengaapi.services.account_services import AccountServices

account_services = AccountServices(config=app_config.get('testing'))
signature = 'e967CLKebZyLfa73'
api_token = 'Bearer e967CLKebZyLfa73'


@mock.patch('src.jengaapi.services.account_services.send_get_request')
def test_account_balance(send_get_request_mock):
    response_payload = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "balances": [
                {
                    "amount": "485678467.54",
                    "type": "Available"
                },
                {
                    "amount": "485678467.54",
                    "type": "Current"
                }
            ],
            "currency": "KES"
        }
    }
    send_get_request_mock.return_value = response_payload
    response = account_services.account_balance(signature, api_token, "KE", "1234567890")
    assert response == response_payload


@mock.patch('src.jengaapi.services.account_services.send_get_request')
def test_account_mini_statement(send_get_request_mock):
    response_payload = {
        "status": "true",
        "code": 0,
        "message": "success",
        "data": {
            "accountNumber": "0011547896523",
            "currency": "KES",
            "balance": 1000,
            "transactions": [
                {
                    "chequeNumber": None,
                    "date": "2017-01-01T00:00:00",
                    "description": "EAZZY-FUNDS TRNSF TO A/C XXXXXXXXXXXX",
                    "amount": "100",
                    "type": "Debit"
                },
                {
                    "chequeNumber": None,
                    "date": "2017-01-03T00:00:00",
                    "description": "SI ACCOUNT TO ACCOUNT THIRD PA",
                    "amount": "51",
                    "type": "Debit"
                },
                {
                    "chequeNumber": None,
                    "date": "2017-01-05T00:00:00",
                    "description": "CHARGE FOR OTC ECS TRAN",
                    "amount": "220",
                    "type": "Debit"
                },
                {
                    "chequeNumber": None,
                    "date": "2017-01-05T00:00:00",
                    "description": "SI ACCOUNT TO ACCOUNT THIRD PA",
                    "amount": "20",
                    "type": "Debit"
                }
            ]
        }
    }
    send_get_request_mock.return_value = response_payload
    response = account_services.account_mini_statement(signature, api_token, "KE", "1234567890")
    assert response == response_payload


@mock.patch('src.jengaapi.services.account_services.send_get_request')
def test_account_inquiry_bank_accounts(send_get_request_mock):
    response_payload = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "account": {
                "branchCode": "145",
                "number": "1450160649886",
                "currency": "KES",
                "status": "Active"
            },
            "customer": [
                {
                    "name": "CATHERINE MURANDITSI MUKABWA",
                    "id": "54307789658",
                    "type": "Retail"
                }
            ]
        }
    }
    send_get_request_mock.return_value = response_payload
    response = account_services.account_inquiry_bank_accounts(signature, api_token, "KE", "1234567890")
    assert response == response_payload


@mock.patch('src.jengaapi.services.account_services.send_post_request')
def test_opening_closing_account_balance(send_get_request_mock):
    response_payload = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "balances": [
                {
                    "amount": "0",
                    "type": "Closing Balance"
                },
                {
                    "amount": "0",
                    "type": "Opening Balance"
                }
            ]
        }
    }
    payload = {
        "countryCode": "KE",
        "accountId": "0011547896523",
        "date": "2018-08-18"
    }
    send_get_request_mock.return_value = response_payload
    response = account_services.opening_closing_account_balance(signature, api_token, **payload)
    assert response == response_payload


@mock.patch('src.jengaapi.services.account_services.send_post_request')
def test_account_full_statement(send_get_request_mock):
    response_payload = {
        "accountNumber": "0011547896523",
        "currency": "KES",
        "balance": 997382.57,
        "transactions": [
            {
                "reference": 541,
                "date": "2018-07-13T00:00:00.000",
                "description": "EQUITEL-BUNDLE/254764555383/8755",
                "amount": 900,
                "serial": 1,
                "postedDateTime": "2018-07-13T09:51:27.000",
                "type": "Debit",
                "runningBalance": {
                    "currency": "KES",
                    "amount": 1344.57
                }
            },
            {
                "reference": "S4921027",
                "date": "2018-07-18T00:00:00.000",
                "description": "EAZZY-AIRTIME/EQUITEL/254764555383/100000939918/18",
                "amount": 200,
                "serial": 1,
                "postedDateTime": "2018-07-18T16:27:18.000",
                "type": "Debit",
                "runningBalance": {
                    "currency": "KES",
                    "amount": 1144.57
                }
            },
            {
                "reference": 5436,
                "date": "2018-07-19T00:00:00.000",
                "description": "CREDIT TRANSFER",
                "amount": 1000000,
                "serial": 2,
                "postedDateTime": "2018-07-19T12:01:47.000",
                "type": "Credit",
                "runningBalance": {
                    "currency": "KES",
                    "amount": 1001144.57
                }
            }
        ]
    }
    payload = {
        "countryCode": "KE",
        "accountNumber": "0011547896523",
        "fromDate": "2018-01-18",
        "toDate": "2018-04-19",
        "limit": 3
    }
    send_get_request_mock.return_value = response_payload
    response = account_services.account_full_statement(signature, api_token, **payload)
    assert response == response_payload
