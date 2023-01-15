from unittest import mock

from src.jengaapi.configs.config import app_config
from src.jengaapi.services.authorization_service import AuthorizationService

authorization_services = AuthorizationService(config=app_config.get('testing'))


@mock.patch('src.jengaapi.services.authorization_service.send_post_request')
def test_authorization_token(send_post_request_mock):
    send_post_request_mock.return_value = {
        "accessToken": "exxxxxxxx",
        "refreshToken": "Q/lKyyNKrtQP",
        "expiresIn": "2022-12-30T13:12:27Z",
        "issuedAt": "2022-12-30T12:57:27Z",
        "tokenType": "Bearer"
    }
    response = authorization_services.auth_token
    assert response is not None
    assert response == 'Bearer exxxxxxxx'


def test_signature_generation():
    request_hash_fields = ('0011547896523', 'KE', '2018-08-09')
    response = authorization_services.signature(request_hash_fields)
    assert response is not None
