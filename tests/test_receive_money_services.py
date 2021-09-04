from unittest import mock

from src.jengaapi.receive_money_services import ReceiveMoneyService

instance = ReceiveMoneyService(token="Bearer xxxxxxx")
signature = 'e967CLKebZyLfa73/YYltjW5M4cHoyWeHi/5VDKJ64gOwKBvzHJRqJJrBBc34v2m4jyKkDMBtfRJeFlxbNisMAeBtkw0TRcD2LThFK27EOqLM3m8rQYa+7CJ2FhPhK+iOa4RUY+vTfkRX5JXuqOW7a3GHds8qyPaPe19cKUY33eAJL3upXnGnA3/PEhzjhb0pqk2zCI7aRzvjjVUGwUdT6LO73NVhDSWvGpLEsP0dH/stC5BoTPNNt9nY8yvGUPV7fmaPSIFn68W4L04WgePQdYkmD1UPApGcrl+L2ALY3lPaRfI6/N+0Y3NIWQyLgix+69k7V4EGolqejWdion+9A=='


@mock.patch('src.jengaapi.receive_money_services.requests.post')
def test_receive_payments_eazzypay_push(mock_post):
    mock_response = {
        "referenceNumber": "692194625798",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.receive_payments_eazzypay_push(signature, mobile_number="0763000000", description="remarks",
                                                       country_code="KE", payment_amount="1234.00")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.receive_money_services.requests.post')
def test_receive_payments_bill_payments(mock_post):
    mock_response = {
        "transactionId": "123456729123",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.receive_payments_bill_payments(signature, partner_id="567334444", payer_name="",
                                                       account="111222",
                                                       payer_mobile_number="0763000000",
                                                       biller_code="320320",
                                                       country_code="KE",
                                                       payment_amount="100.00",
                                                       currency_code="KES",
                                                       remarks="remarks of the bill payment")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.receive_money_services.requests.post')
def test_receive_payments_merchant_payments(mock_post):
    mock_response = {
        "status": "SUCCESS",
        "merchantName": "A N Other",
        "transactionId": "931118931118"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.receive_payments_merchant_payments(signature,
                                                           merchant_till="0766000000",
                                                           payment_amount="1000.00",
                                                           country_code="KE",
                                                           partner_id="0011547896523")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.receive_money_services.requests.post')
def test_bill_validation(mock_post):
    mock_response = {
        "bill": {
            "CustomerRefNumber": "28055948",
            "amount": "20000",
            "amountCurrency": "KES",
            "name": "A N Other",
            "status": True,
            "billStatus": "1",
            "createdOn": "2018-05-21T00:00:00+03:00",
            "message": "SUCCESS"
        }
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.bill_validation(biller_code="320320",
                                        customer_ref_number="111222",
                                        payment_amount="1000.00",
                                        currency_code="KES")
    assert response is not None
    assert response == mock_response
