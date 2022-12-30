from unittest import mock

from src.jengaapi.auth import JengaAPI

instance = JengaAPI(api_key="Basic XXXX", consumer_secret="consumer_secret",
                    merchant_code="8900124", base_url="https://uat.finserve.africa/")


@mock.patch('src.jengaapi.auth.requests.post')
def test_authorization_token(mock_post):
    mock_post.return_value.json.return_value = {
        "accessToken": "exxxxxxxx",
        "refreshToken": "Q/lKyyNKrtQP",
        "expiresIn": "2022-12-30T13:12:27Z",
        "issuedAt": "2022-12-30T12:57:27Z",
        "tokenType": "Bearer"
    }
    response = instance.authorization_token
    assert response is not None
    assert response == 'Bearer exxxxxxxx'


def test_signature_generation():
    response = instance.signature(('0011547896523', 'KE', '2018-08-09'))
    assert response is not None
