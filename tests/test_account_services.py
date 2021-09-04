from datetime import date
from unittest import mock

from src.jengaapi.account_services import AccountServices

as_instance = AccountServices(token='Bearer XXXXX')
signature = 'e967CLKebZyLfa73/YYltjW5M4cHoyWeHi/5VDKJ64gOwKBvzHJRqJJrBBc34v2m4jyKkDMBtfRJeFlxbNisMAeBtkw0TRcD2LThFK27EOqLM3m8rQYa+7CJ2FhPhK+iOa4RUY+vTfkRX5JXuqOW7a3GHds8qyPaPe19cKUY33eAJL3upXnGnA3/PEhzjhb0pqk2zCI7aRzvjjVUGwUdT6LO73NVhDSWvGpLEsP0dH/stC5BoTPNNt9nY8yvGUPV7fmaPSIFn68W4L04WgePQdYkmD1UPApGcrl+L2ALY3lPaRfI6/N+0Y3NIWQyLgix+69k7V4EGolqejWdion+9A=='


@mock.patch('src.jengaapi.account_services.requests.get')
def test_account_balance(mock_get):
    mock_get.return_value.json.return_value = {
        "currency": "KES",
        "balances": [
            {
                "amount": "997382.57",
                "type": "Current"
            },
            {
                "amount": "997382.57",
                "type": "Available"
            }
        ]
    }
    response = as_instance.account_balance(signature, 'KE', '0123456789077')
    assert response is not None


@mock.patch('src.jengaapi.account_services.requests.get')
def test_account_mini_statement(mock_get):
    mock_response = {
        "accountNumber": "0011547896523",
        "currency": "KES",
        "balance": 1000,
        "transactions": [
            {
                "chequeNumber": "123456789",
                "date": "2017-01-01T00:00:00",
                "description": "EAZZY-FUNDS TRNSF TO A/C XXXXXXXXXXXX",
                "amount": "100",
                "type": "Debit"
            },
            {
                "chequeNumber": "123456789",
                "date": "2017-01-03T00:00:00",
                "description": "SI ACCOUNT TO ACCOUNT THIRD PA",
                "amount": "51",
                "type": "Debit"
            }
        ]
    }
    mock_get.return_value.json.return_value = mock_response
    response = as_instance.account_mini_statement('KE', '0011547896523', signature)
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.account_services.requests.get')
def test_account_inquiry_bank_accounts(mock_get):
    mock_response = {
        "account": {
            "number": "0011547896523",
            "branchCode": "017",
            "currency": "KES",
            "status": "Active"
        },
        "customer": [
            {
                "id": "100200300",
                "name": "A N.Other",
                "type": "Retail"
            }
        ]
    }
    mock_get.return_value.json.return_value = mock_response
    response = as_instance.account_inquiry_bank_accounts('KE', '0011547896523', signature)
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.account_services.requests.post')
def test_opening_closing_account_balance(mock_post):
    mock_response = {
        "balances": [
            {
                "type": "Closing Balance",
                "amount": "10810.00"
            },
            {
                "type": "Opening Balance",
                "amount": "103.00"
            }
        ]
    }
    mock_post.return_value.json.return_value = mock_response
    response = as_instance.opening_closing_account_balance('KE', '0011547896523', signature)
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.account_services.requests.post')
def test_account_full_statement(mock_post):
    mock_response = {
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
    mock_post.return_value.json.return_value = mock_response
    response = as_instance.account_full_statement(from_date=date(2018, 7, 1), to_date=date(2018, 7, 30),
                                                  country_code='KE', account_id='0011547896523',
                                                  account_no='0011547896523', signature=signature, limit=3)
    assert response is not None
    assert response == mock_response
