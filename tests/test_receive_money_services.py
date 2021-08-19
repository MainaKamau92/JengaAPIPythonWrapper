from unittest import mock

from src.jengaapi.receive_money_services import ReceiveMoneyService

instance = ReceiveMoneyService(payment_amount="345.00", country_code="KE", description="Money Sent",
                               currency_code='KES', partner_id="5673344", biller_code="547547", payer_name="John Doe",
                               payer_account="0763000000", token="Bearer xxxxxxx")


@mock.patch('src.jengaapi.receive_money_services.requests.post')
def test_receive_payments_eazzypay_push(mock_post):
    mock_response = {
        "referenceNumber": "692194625798",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.receive_payments_eazzypay_push(mobile_number="0763000000", merchant_code="692194625798",
                                                       country_code="KE")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.receive_money_services.requests.post')
def test_receive_payments_bill_payments(mock_post):
    mock_response = {
        "transactionId": "123456729123",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.receive_payments_bill_payments(partner_id="567334444")
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
    response = instance.receive_payments_merchant_payments(merchant_till="0766000000")
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
    response = instance.bill_validation(biller_code="320320", customer_ref_number="111222")
    assert response is not None
    assert response == mock_response
