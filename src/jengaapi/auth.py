import os
from base64 import b64encode

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from . import ENVIRONMENT
from .exceptions import handle_response
from .utils import get_project_root


class JengaAPI:
    def __init__(self, api_key, consumer_secret, merchant_code, base_url,
                 path_to_private_key=os.path.join(get_project_root(), "privatekey.pem")):
        self.api_key = api_key
        self._merchant_code = merchant_code
        self._consumer_secret = consumer_secret
        self.base_url = base_url
        self.private_key = path_to_private_key if ENVIRONMENT != "testing" else os.path.join(get_project_root(),
                                                                                             "tests/testkey.pem")
        self.merchant_code = merchant_code

    @property
    def authorization_token(self):
        url = self.base_url + "authentication/api/v3/authenticate/merchant"
        payload = {
            "merchantCode": self._merchant_code,
            "consumerSecret": self._consumer_secret
        }
        headers = {
            "Content-Type": "application/json",
            "Api-Key": self.api_key
        }
        response = requests.post(url, json=payload, headers=headers)
        _response = handle_response(response)
        token = "Bearer " + _response.get("accessToken")
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
