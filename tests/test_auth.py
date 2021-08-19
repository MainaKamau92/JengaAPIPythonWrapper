from src.jengaapi import JengaAPI
from unittest import mock

instance = JengaAPI(api_key="Basic XXXX", password="password",
                    merchant_code="8900124", base_url="uat.jengahq.io")


@mock.patch('src.jengaapi.auth.requests.post')
def test_authorization_token(mock_post):
    mock_post.return_value.json.return_value = {
        "token_type": "bearer",
        "issued_at": "1443102144106",
        "expires_in": "3599",
        "access_token": "ceTo5RCpluTfGn9B3OZXnnQkDVKM"
    }
    response = instance.authorization_token
    assert response is not None
    assert response == 'Bearer ceTo5RCpluTfGn9B3OZXnnQkDVKM'


def test_signature_generation():
    gen_sig =  b'T4BE0MCqoh3B7rgbz+RP15t4syaUYeAkiMh6lp/XOsGpXBKi6fHWjQjs8RWHJUlCT3El59XEoutvSdhoH5Rd8WOmZEXKly8oHn78aIsh8v+sJ8uqsD5Smbyi3emP9nWx2iQTtD8kQ2q/BzaCj3ER5P3uB1nMD2F7WCe66ZKJ7Clk6+ryZUr1iwxoZsMULMWvJKP+s7MQyzvcJ5qbeGxrvtbrwipvRiovWF4OvGHTdvq2/sSH2Teju89k1K96erPprCe1NmyBkKMonUMCqm0gqwWpZlSf/NF3DzHQ/Rv/C03swMn6GG2ubu0OOVymeWsgMfmILkbzHtxpIztrMkTG7Q=='
    response = instance.signature(('0011547896523', 'KE', '2018-08-09'))
    assert response == gen_sig
