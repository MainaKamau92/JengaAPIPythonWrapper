from unittest import mock
from src.jengaapi.configs.config import app_config
from src.jengaapi.services.send_money_services import SendMoneyService

send_money_service = SendMoneyService(config=app_config.get('testing'))
signature = 'e967CLKebZyLfa73'
api_token = 'Bearer e967CLKebZyLfa73'


@mock.patch('src.jengaapi.services.send_money_services.send_post_request')
def test_send_within_equity(send_post_request_mock):
    mock_response = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "transactionId": "54154",
            "status": "SUCCESS"
        }
    }
    payload = {
        "source": {
            "countryCode": "KE",
            "name": "John Doe",
            "accountNumber": "0011547896523"
        },
        "destination": {
            "type": "bank",
            "countryCode": "KE",
            "name": "Tom Doe",
            "accountNumber": "0060161911111"
        },
        "transfer": {
            "type": "InternalFundsTransfer",
            "amount": "100.00",
            "currencyCode": "KES",
            "reference": "742194625798",
            "date": "2019-05-01",
            "description": "Some remarks here"
        }
    }
    send_post_request_mock.return_value = mock_response
    response = send_money_service.send_within_equity(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.services.send_money_services.send_post_request')
def test_send_to_mobile_wallets(send_post_request_mock):
    mock_response = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "transactionId": "",
            "status": "SUCCESS"
        }
    }
    payload = {
        "source": {
            "countryCode": "KE",
            "name": "John Doe",
            "accountNumber": "0011547896523"
        },
        "destination": {
            "type": "mobile",
            "countryCode": "KE",
            "name": "A N.Other",
            "mobileNumber": "0763123456",
            "walletName": "Mpesa"
        },
        "transfer": {
            "type": "MobileWallet",
            "amount": "1000",
            "currencyCode": "KES",
            "date": "2018-08-18",
            "description": "some remarks here"
        }
    }
    send_post_request_mock.return_value = mock_response
    response = send_money_service.send_to_mobile_wallets(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.services.send_money_services.send_post_request')
def test_send_rtgs(send_post_request_mock):
    mock_response = {
        "transactionId": "000000403777",
        "status": "SUCCESS"
    }
    payload = {
        "source": {
            "countryCode": "KE",
            "name": "John Doe",
            "accountNumber": "0011547896523"
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
        }
    }
    send_post_request_mock.return_value = mock_response
    response = send_money_service.send_rtgs(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.services.send_money_services.send_post_request')
def test_send_swift(send_post_request_mock):
    mock_response = {
        "transactionId": "000000403794",
        "status": "SUCCESS"
    }
    payload = {
        "source": {
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
            "addressline1": "Post Box 56"
        },
        "transfer": {
            "type": "SWIFT",
            "amount": "4.00",
            "currencyCode": "USD",
            "reference": "692194625798",
            "date": "2019-05-01",
            "description": "Some remarks here",
            "chargeOption": "SELF"
        }
    }
    send_post_request_mock.return_value = mock_response
    response = send_money_service.send_swift(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.services.send_money_services.send_post_request')
def test_send_pesa_link_to_bank_account(send_post_request_mock):
    mock_response = {
        "transactionId": "10000345333355",
        "status": "SUCCESS",
        "description": "Confirmed. Ksh 100 Sent to 01100762802910 "
                       "-Tom Doe from your account 1460163242696 on 20-05-2019 "
                       "at 141313 Ref. 707700078800 Thank you"
    }
    payload = {
        "source": {
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
        }
    }
    send_post_request_mock.return_value = mock_response
    response = send_money_service.send_pesa_link_to_bank_account(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.services.send_money_services.send_post_request')
def test_send_pesa_link_to_mobile_number(send_post_request_mock):
    mock_response = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "description": "Confirmed. Ksh 100.0 sent to 254764000000- "
                           "John Doe from your account 1464968850106 "
                           "on Fri Jun 24 11:07:02 EAT 2022. Ref 041108128674. Thank you",
            "transactionId": "041108128674",
            "status": "SUCCESS"
        }
    }
    payload = {
        "source": {
            "countryCode": "KE",
            "name": "John Doe",
            "accountNumber": "0011547896523"
        },
        "destination": {
            "type": "mobile",
            "countryCode": "KE",
            "name": "A N.Other",
            "bankCode": "01",
            "mobileNumber": "0722000000"
        },
        "transfer": {
            "type": "PesaLink",
            "amount": "1000",
            "currencyCode": "KES",
            "reference": "692194625798",
            "date": "2018-08-19"
        }
    }
    send_post_request_mock.return_value = mock_response
    response = send_money_service.send_pesa_link_to_mobile_number(signature, api_token, **payload)
    assert response == mock_response
