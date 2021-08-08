import os
from base64 import b64encode

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from src.jengaapi.exceptions import handle_response
from src.jengaapi.utils import get_project_root


class JengaAPI:
    def __init__(self, api_key, password, merchant_code, uat_url):
        self.api_key = api_key
        self._username = merchant_code
        self._password = password
        self.uat_url = uat_url
        self.private_key = os.path.join(get_project_root(), "privatekey.pem")
        self.merchant_code = merchant_code

    @property
    def authorization_token(self):
        url = self.uat_url + "/identity/v2/token"
        headers = {"Authorization": self.api_key}
        body = dict(username=self._username, password=self._password)
        response = requests.post(url, headers=headers, data=body)
        _response = handle_response(response)
        token = "Bearer " + _response.get("access_token")
        return token

    def signature(self, request_hash_fields: tuple):
        message = "".join(request_hash_fields).encode(
            "utf-8")  # See separate instruction on how to create this concatenation
        digest = SHA256.new()
        digest.update(message)
        with open(self.private_key, "r") as myfile:
            private_key = RSA.importKey(myfile.read())
        signer = PKCS1_v1_5.new(private_key)
        sigBytes = signer.sign(digest)
        return b64encode(sigBytes)
