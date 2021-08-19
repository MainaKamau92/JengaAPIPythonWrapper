from datetime import date
from src.jengaapi.send_money_services import SendMoneyService
from unittest import mock

instance = SendMoneyService(transfer_amount="5678.00", transfer_date=date.today(), token="Bearer XXXX")


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_within_equity(mock_post):
    mock_response = {
        "transactionId": "1452854",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_within_equity(destination_account_number="0022547896523")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_to_mobile_wallets(mock_post):
    mock_response = {
        "transactionId": "45865",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_to_mobile_wallets(wallet_name="Equitel",
                                               destination_mobile_number="0763123456")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_rtgs(mock_post):
    mock_response = {
        "transactionId": "000000403777",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_rtgs(destination_account_number="2564785123", bank_code="01")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_swift(mock_post):
    mock_response = {
        "transactionId": "000000403794",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_swift(destination_account_number="12365489",
                                   bank_bic="BOTKJPJTXXX",
                                   address_line="Post Box 56",
                                   charge_option="SELF"
                                   )
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_eft(mock_post):
    mock_response = {
        "transactionId": "000000403794",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_eft(destination_account_number="54545454",
                                 bank_code="01", branch_code="112")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_pesalink_to_bank_account(mock_post):
    mock_response = {
        "transactionId": "10000345333355",
        "status": "SUCCESS",
        "description": "Confirmed. Ksh 100 Sent to 01100762802910 -Tom Doe from your account 1460163242696 on "
                       "20-05-2019 at 141313 Ref. 707700078800 Thank you "
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_pesalink_to_bank_account(destination_account_number="8323524545",
                                                      bank_code="01",
                                                      mobile_number="0722000000"
                                                      )
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_pesalink_to_mobile_number(mock_post):
    mock_response = {
        "transactionId": "10000345333355",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_pesalink_to_mobile_number(destination_mobile_number="0722000000",
                                                       bank_code="01")
    assert response is not None
    assert response == mock_response
