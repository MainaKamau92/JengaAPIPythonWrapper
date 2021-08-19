from unittest import mock

from src.jengaapi.send_money_queries_services import SendMoneyQueriesServices

instance = SendMoneyQueriesServices(token="Bearer xxxxx")


@mock.patch('src.jengaapi.send_money_queries_services.requests.post')
def test_account_inquiry(mock_post):
    mock_response = {
        "banks": [
            {
                "bankCode": "11",
                "bankName": "CO-OPERATIVE BANK",
                "customerName": "A N Other"
            }
        ]
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.account_inquiry(mobile_number="0763000000")
    assert response is not None
    assert response == mock_response

# Confirm response object first

# @mock.patch('src.jengaapi.send_money_queries_services.requests.post')
# def test_transaction_status(mock_post):
#     mock_response = {
#         "banks": [
#             {
#                 "bankCode": "11",
#                 "bankName": "CO-OPERATIVE BANK",
#                 "customerName": "A N Other"
#             }
#         ]
#     }
#     mock_post.return_value.json.return_value = mock_response
#     response = instance.account_inquiry(mobile_number="0763000000")
#     assert response is not None
#     assert response == mock_response
