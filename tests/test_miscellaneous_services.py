from unittest import mock

from src.jengaapi.miscellaneous_services import miscellaneous_services

signature = 'e967CLKebZyLfa73'
api_token = 'Bearer e967CLKebZyLfa73'


@mock.patch('src.jengaapi.miscellaneous_services.send_post_request')
def test_purchase_airtime(send_post_request_mock):
    mock_response = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "referenceNumber": "292516007075",
            "status": "SUCCESS"
        }
    }
    payload = {
        "customer": {
            "countryCode": "KE",
            "mobileNumber": "0765555131"
        },
        "airtime": {
            "amount": "100",
            "reference": "692194625798",
            "telco": "Equitel"
        }
    }
    send_post_request_mock.return_value = mock_response
    response = miscellaneous_services.purchase_airtime(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.miscellaneous_services.send_post_request')
def test_get_forex_rates(send_post_request_mock):
    mock_response = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "convertedAmount": 424.668,
            "rate": 1.2345,
            "fromAmount": 344,
            "rateCode": "TTB"
        }
    }
    payload = {
        "countryCode": "KE",
        "currencyCode": "USD",
        "amount": 344,
        "toCurrency": "GBP"
    }
    send_post_request_mock.return_value = mock_response
    response = miscellaneous_services.get_forex_rates(signature, api_token, **payload)
    assert response == mock_response


@mock.patch('src.jengaapi.miscellaneous_services.send_post_request')
def test_kyc(send_post_request_mock):
    mock_response = {
        "status": True,
        "code": 0,
        "message": "success",
        "data": {
            "identity": {
                "customer": {
                    "firstName": "JOHN",
                    "lastName": "DOE",
                    "occupation": "",
                    "gender": "M",
                    "nationality": "Kenyan",
                    "deathDate": "",
                    "fullName": "JOHN JOHN DOE DOE",
                    "middlename": "JOHN DOE",
                    "ShortName": "JOHN",
                    "birthCityName": "",
                    "birthDate": "1985-06-20T12:00:00",
                    "faceImage": ""
                },
                "documentType": "NATIONAL ID",
                "documentNumber": "555555",
                "documentSerialNumber": "55555555555",
                "documentIssueDate": "2011-12-08T12:00:00",
                "documentExpirationDate": "",
                "IssuedBy": "REPUBLIC OF KENYA",
                "additionalIdentityDetails": [
                    {
                        "documentType": "",
                        "documentNumber": "",
                        "issuedBy": ""
                    }
                ],
                "address": {
                    "locationName": "",
                    "districtName": "",
                    "subLocationName": "",
                    "provinceName": "",
                    "villageName": ""
                }
            }
        }
    }
    payload = {
        "identity": {
            "documentType": "ALIENID",
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "1970-01-30",
            "documentNumber": "123456",
            "countryCode": "KE"
        }
    }
    send_post_request_mock.return_value = mock_response
    response = miscellaneous_services.kyc(signature, api_token, **payload)
    assert response == mock_response
