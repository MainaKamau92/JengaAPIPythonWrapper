from unittest import mock
from src.jengaapi.configs.config import app_config
from src.jengaapi.services.receive_money_queries_services import ReceiveMoneyQueriesService


receive_money_queries_service = ReceiveMoneyQueriesService(config=app_config.get('testing'))
signature = 'e967CLKebZyLfa73'
api_token = 'Bearer e967CLKebZyLfa73'


@mock.patch('src.jengaapi.services.receive_money_queries_services.send_get_request')
def test_get_all_eazzy_pay_merchants(send_get_request_mock):
    response_payload = {
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
    send_get_request_mock.return_value = response_payload
    response = receive_money_queries_service.get_all_eazzy_pay_merchants(api_token, 1, 1)
    assert response == response_payload


@mock.patch('src.jengaapi.services.receive_money_queries_services.send_get_request')
def test_query_transaction_details(send_get_request_mock):
    response_payload = {
        "transactionRef": "692194625798",
        "status": "0",
        "message": "Transaction approved successfully."
    }
    send_get_request_mock.return_value = response_payload
    response = receive_money_queries_service.query_transaction_details(api_token, "692194625798")
    assert response == response_payload


@mock.patch('src.jengaapi.services.receive_money_queries_services.send_get_request')
def test_get_all_billers(send_get_request_mock):
    response_payload = {
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
    send_get_request_mock.return_value = response_payload
    response = receive_money_queries_service.get_all_billers(api_token, 1, 5, "utilities")
    assert response == response_payload
