from unittest import mock
from src.jengaapi.receive_money_queries_services import ReceiveMoneyQueriesService

rms_instance = ReceiveMoneyQueriesService()


@mock.patch('src.jengaapi.receive_money_queries_services.requests.get')
def test_get_all_eazzypay_merchants(mock_get):
    mock_response = {
        "merchants": [
            {
                "name": "Nakumatt",
                "tillnumber": "0766002221",
                "outlets": [
                    {
                        "name": "Nakumatt Presitige",
                        "tillnumber": "0766002201"
                    },
                    {
                        "name": "Nakumatt Junction",
                        "tillnumber": "0766014221"
                    }
                ]
            }
        ]
    }
    mock_get.return_value.json.return_value = mock_response
    response = rms_instance.get_all_eazzypay_merchants(1, 1)
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.receive_money_queries_services.requests.get')
def test_get_payment_status_eazzy_pay_push(mock_get):
    mock_response = {
        "transactionRef": "692194625798",
        "status": "0",
        "message": "Transaction approved successfully."
    }
    mock_get.return_value.json.return_value = mock_response
    response = rms_instance.get_payment_status_eazzy_pay_push('692194625798')
    assert response is not None
    assert response == mock_response


@mock.patch('src.jengaapi.receive_money_queries_services.requests.get')
def test_get_all_billers(mock_get):
    mock_response = {
        "billers": [
            {
                "name": "test biller",
                "code": "400000"
            },
            {
                "name": "JAMBO PAY TRUSTEE ACCOUNT",
                "code": "147147"
            },
            {
                "name": "I PAY",
                "code": "300014"
            },
            {
                "name": "ZUKU",
                "code": "320320"
            },
            {
                "name": "WINGS TO FLY",
                "code": "344344"
            }
        ]
    }
    mock_get.return_value.json.return_value = mock_response
    response = rms_instance.get_all_billers(5, 1)
    assert response is not None
    assert response == mock_response
