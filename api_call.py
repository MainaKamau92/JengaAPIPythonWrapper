# TODO: Remove once done testing
import os
from datetime import datetime

from src.jengaapi.auth import JengaAPI
from src.jengaapi.mpgs_direct_integration import mpgs_direct_integration
from src.jengaapi.uncategorized_services import miscellaneous_services
from src.jengaapi.utils import generate_reference

API_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
MERCHANT_CODE = os.getenv("MERCHANT_CODE")
ACCOUNT_NAME = os.getenv("ACCOUNT_NAME")
ACCOUNT_NUMBER = os.getenv("ACCOUNT_NUMBER")
BASE_URL = os.getenv("JENGA_API_BASE_URL", "https://uat.finserve.africa/")
SOURCE_ACCOUNT_NUMBER = ACCOUNT_NUMBER
TRANSFER_AMOUNT = 1000.00
CURRENCY_CODE = "KES"
COUNTRY_CODE = "KE"
FOREIGN_CURRENCY = "USD"
REFERENCE_NO = generate_reference()
DATE = datetime.now().date().strftime("%Y-%m-%d")
DEST_ACC_NO = "0250163591202"
DOCUMENT_NUMBER = "29009055"
payload = {
    "transactionReference": "NCJASSOPK101004",
    "customer": {
        "email": "john@yopmail.com",
        "firstName": "John",
        "cardFirstName": "John",
        "cardLastName": "Doe",
        "lastName": "Smith",
        "mobilePhone": "0763000000"
    },
    "order": {
        "amount": 258.75,
        "currency": "KES",
        "description": "Card payment for order OR1649092214608",
        "subMerchant": {
            "address": {
                "city": "Kisumu",
                "company": "Kilimall",
                "postalZip": "01001",
                "stateProvince": "Kisumu",
                "street": "Kilimani"
            },
            "email": "john@yopmail.com",
            "tradingName": "Kilimall",
            "phone": "254763000000",
            "identifier": "2179103820"
        }
    },
    "sourceOfFunds": {
        "cardNumber": "22d5fd8f8df08ba34a1dcbf84011ae783c326e9fcefd08501e40722c7aeeb946abb6255714b7289eef562748920b873be2aHMpN/qcSMMeh12GL5pxWLo9Y7fDn2lqUou0ICcBs=",
        "cardSecurity": "1fd3b576cb487da80b30551c0e66ee2768a5cb5c99c121d91e4721947914c01ee919ab8943475ca5847bf796241da2448EILoGUe8QuoJsNg4Vp7JQ==",
        "cardExpiryYear": "34",
        "cardExpiryMonth": "10"
    },
    "transaction": {
        "source": "INTERNET",
        "sourceOwner": "FINSERVE"
    }
}
api = JengaAPI(API_KEY, CONSUMER_SECRET, MERCHANT_CODE, BASE_URL)
api_token = api.authorization_token
data = (COUNTRY_CODE, DOCUMENT_NUMBER)
signature = api.signature(data)
res = mpgs_direct_integration.mpgs_authorize_payment(None, api_token, **payload)
print(res)
