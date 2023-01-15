from unittest import mock
from src.jengaapi.configs.config import app_config
from src.jengaapi.services.receive_money_services import ReceiveMoneyService

receive_money_service = ReceiveMoneyService(config=app_config.get('testing'))
signature = 'e967CLKebZyLfa73'
api_token = 'Bearer e967CLKebZyLfa73'


@mock.patch('src.jengaapi.services.receive_money_services.send_post_request')
def test_receive_payments_bill_payments(send_post_request_mock):
    mock_response = {
        "referenceNumber": "692194625798",
        "status": "SUCCESS"
    }
    send_post_request_mock.return_value = mock_response
    payload = {
        "biller": {
            "billerCode": "320320",
            "countryCode": "KE"
        },
        "bill": {
            "reference": "111222",
            "amount": "100.00",
            "currency": "KES"
        },
        "payer": {
            "name": "A N.Other",
            "account": "111222",
            "reference": "123456729123",
            "mobileNumber": "0763000000"
        },
        "partnerId": "0011547896523"
    }
    response = receive_money_service.receive_payments_bill_payments(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.services.receive_money_services.send_post_request')
def test_receive_payments_merchant_payments(send_post_request_mock):
    mock_response = {
        "status": "SUCCESS",
        "merchantName": "A N Other",
        "transactionId": "931118931118"
    }
    payload = {
        "merchant": {"till": "0766000000"},
        "payment": {
            "ref": "123456789123",
            "amount": "1000.00",
            "currency": "KES"
        },
        "partner": {
            "id": "0011547896523",
            "ref": "987654321"
        }
    }
    send_post_request_mock.return_value = mock_response
    response = receive_money_service.receive_payments_merchant_payments(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.services.receive_money_services.send_post_request')
def test_bill_validation(send_post_request_mock):
    mock_response = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "amount": "1000.0",
            "customerRefNumber": "101704",
            "name": "John Doe",
            "billStatus": "true",
            "message": "SUCCESS",
            "createdOn": "Fri Jun 24 11:04:14 EAT 2022",
            "amountCurrency": "KES",
            "status": True
        }
    }
    payload = {
        "billerCode": "320320",
        "customerRefNumber": "111222",
        "amount": "1000.00",
        "amountCurrency": "KES"
    }
    send_post_request_mock.return_value = mock_response
    response = receive_money_service.bill_validation(signature, api_token, **payload)
    assert response == mock_response
