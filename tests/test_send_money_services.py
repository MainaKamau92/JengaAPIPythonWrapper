from datetime import date
from unittest import mock

from src.jengaapi.send_money_services import SendMoneyService

instance = SendMoneyService(token="Bearer XXXX")

signature = b'e967CLKebZyLfa73/YYltjW5M4cHoyWeHi/5VDKJ64gOwKBvzHJRqJJrBBc34v2m4jyKkDMBtfRJeFlxbNisMAeBtkw0TRcD2LThFK27EOqLM3m8rQYa+7CJ2FhPhK+iOa4RUY+vTfkRX5JXuqOW7a3GHds8qyPaPe19cKUY33eAJL3upXnGnA3/PEhzjhb0pqk2zCI7aRzvjjVUGwUdT6LO73NVhDSWvGpLEsP0dH/stC5BoTPNNt9nY8yvGUPV7fmaPSIFn68W4L04WgePQdYkmD1UPApGcrl+L2ALY3lPaRfI6/N+0Y3NIWQyLgix+69k7V4EGolqejWdion+9A=='


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_within_equity(mock_post):
    mock_response = {
        "transactionId": "1452854",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_within_equity(signature, destination_account_number="0022547896523",
                                           country_code="KE",
                                           source_name="A N.Other",
                                           source_account_number="0011547896523",
                                           destination_name="John Doe",
                                           transfer_amount="1000.00",
                                           currency_code="KES",
                                           reference_no="692194625798",
                                           transfer_date=date.today(),
                                           description="some remarks here")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_to_mobile_wallets(mock_post):
    mock_response = {
        "transactionId": "45865",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_to_mobile_wallets(signature, wallet_name="Equitel",
                                               destination_mobile_number="0763123456",
                                               country_code="KE",
                                               source_name="John Doe",
                                               source_account_number="0011547896523",
                                               destination_name="A N.Other",
                                               transfer_amount="1000.00",
                                               currency_code="KES",
                                               reference_no="692194625798",
                                               transfer_date=date.today(),
                                               description="some remarks here")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_rtgs(mock_post):
    mock_response = {
        "transactionId": "000000403777",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_rtgs(signature, destination_account_number="2564785123", bank_code="01",
                                  country_code="KE",
                                  source_name="John Doe",
                                  source_account_number="0011547896523",
                                  destination_name="A N.Other",
                                  transfer_amount="1000.00",
                                  currency_code="KES",
                                  reference_no="692194625798",
                                  transfer_date=date.today(),
                                  description="some remarks here")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_swift(mock_post):
    mock_response = {
        "transactionId": "000000403794",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_swift(signature, destination_account_number="12365489",
                                   bank_bic="BOTKJPJTXXX",
                                   address_line="Post Box 56",
                                   charge_option="SELF",
                                   country_code="KE",
                                   source_name="John Doe",
                                   source_account_number="0011547896523",
                                   destination_name="A N.Other",
                                   transfer_amount="10000.00",
                                   currency_code="USD",
                                   reference_no="692194625798",
                                   transfer_date=date.today(),
                                   description="some description here")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_eft(mock_post):
    mock_response = {
        "transactionId": "000000403794",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_eft(signature, destination_account_number="54545454",
                                 bank_code="01", branch_code="112",
                                 country_code="KE",
                                 source_name="John Doe",
                                 source_account_number="0011547896523",
                                 destination_name="A N.Other",
                                 transfer_amount="10000.00",
                                 currency_code="USD",
                                 reference_no="692194625798",
                                 transfer_date=date.today(),
                                 description="some description here")
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
    response = instance.send_pesalink_to_bank_account(signature, destination_account_number="8323524545",
                                                      bank_code="01",
                                                      mobile_number="0722000000",
                                                      country_code="KE",
                                                      source_name="John Doe",
                                                      source_account_number="0011547896523",
                                                      destination_name="A N.Other",
                                                      transfer_amount="10000.00",
                                                      currency_code="USD",
                                                      reference_no="692194625798",
                                                      transfer_date=date.today(),
                                                      description="some description here")
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.send_money_services.requests.post')
def test_send_pesalink_to_mobile_number(mock_post):
    mock_response = {
        "transactionId": "10000345333355",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.send_pesalink_to_mobile_number(signature, destination_mobile_number="0722000000",
                                                       bank_code="01", country_code="KE",
                                                       source_name="John Doe",
                                                       source_account_number="0011547896523",
                                                       destination_name="A N.Other",
                                                       transfer_amount="10000.00",
                                                       currency_code="USD",
                                                       reference_no="692194625798",
                                                       transfer_date=date.today(),
                                                       description="some description here")
    assert response is not None
    assert response == mock_response
