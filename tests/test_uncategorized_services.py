from unittest import mock
from datetime import date

from src.jengaapi.uncategorized_services import UncategorizedServices

instance = UncategorizedServices(token="Bearer XXX",
                                 country_code="KE", currency_code="KES")


@mock.patch('src.jengaapi.uncategorized_services.requests.post')
def test_purchase_airtime(mock_post):
    mock_response = {
        "referenceNumber": "4568899373748",
        "status": "SUCCESS"
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.purchase_airtime(mobile_number="0722000000", airtime_amount="2000",
                                         telco="Equitel")
    assert response is not None
    assert response == mock_response


# awaiting response object
# @mock.patch('src.jengaapi.uncategorized_services.requests.post')
# def test_get_forex_rates(mock_post):
#     pass

@mock.patch('src.jengaapi.uncategorized_services.requests.post')
def test_id_search_and_verification(mock_post):
    mock_response = {
        "identity": {
            "customer": {
                "fullName": "John Doe ",
                "firstName": "John",
                "middlename": "",
                "lastName": "Doe",
                "ShortName": "John",
                "birthDate": "1900-01-01T00:00:00",
                "birthCityName": "",
                "deathDate": "",
                "gender": "",
                "faceImage": "/9j/4AAQSkZJRgABAAEAYABgA+H8qr6n4e1O71SGFbV/sEOF3O6/N/eb71d/FGkaBVXaq9KfRRRRRUMsKSIdyr0r/9k=",
                "occupation": "",
                "nationality": "Refugee"
            },
            "documentType": "ALIEN ID",
            "documentNumber": "654321",
            "documentSerialNumber": "100500425",
            "documentIssueDate": "2002-11-29T12:00:00",
            "documentExpirationDate": "2004-11-28T12:00:00",
            "IssuedBy": "REPUBLIC OF KENYA",
            "additionalIdentityDetails": [
                {
                    "documentNumber": "",
                    "documentType": "",
                    "issuedBy": ""
                }
            ],
            "address": {
                "provinceName": " ",
                "districtName": "",
                "locationName": "",
                "subLocationName": "",
                "villageName": ""
            }
        }
    }
    mock_post.return_value.json.return_value = mock_response
    response = instance.id_search_and_verification(document_type="ID", first_name="John",
                                                   last_name="Doe",
                                                   date_of_birth=date(1999, 1, 1).strftime("%Y-%m-%d"),
                                                   document_number="25632548")
    assert response is not None
    assert response == mock_response
