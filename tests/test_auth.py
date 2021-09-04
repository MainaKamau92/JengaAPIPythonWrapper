from unittest import mock

from src.jengaapi.auth import JengaAPI

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
    gen_sig = b'L+u6uKCvPUjgyGlACfDCVWG35I94s55QLh3NoqqxQO'
    response = instance.signature(('0011547896523', 'KE', '2018-08-09'))
    assert gen_sig in response
