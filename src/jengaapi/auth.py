from base64 import b64encode

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from . import ENVIRONMENT, BASE_URL, PRIVATE_KEY_PATH, TESTING_PRIVATE_KEY_PATH, API_KEY
from .utils import send_post_request


class JengaAPI:
    def __init__(self, consumer_secret, merchant_code):
        self._merchant_code = merchant_code
        self._consumer_secret = consumer_secret
        self.private_key = PRIVATE_KEY_PATH if ENVIRONMENT != "testing" else TESTING_PRIVATE_KEY_PATH

    @property
    def authorization_token(self):
        url = f"{BASE_URL}authentication/api/v3/authenticate/merchant"
        payload = {
            "merchantCode": self._merchant_code,
            "consumerSecret": self._consumer_secret
        }
        headers = {
            "Content-Type": "application/json",
            "Api-Key": API_KEY
        }
        response = send_post_request(headers, payload, url)
        return "Bearer " + response.get("accessToken")

    def signature(self, request_hash_fields: tuple):
        message = "".join(request_hash_fields).encode(
            "utf-8")  # See separate instruction on how to create this concatenation
        digest = SHA256.new()
        digest.update(message)
        with open(self.private_key, "r") as my_file:
            private_key = RSA.importKey(my_file.read())
        signer = PKCS1_v1_5.new(private_key)
        sigBytes = signer.sign(digest)
        return b64encode(sigBytes)
