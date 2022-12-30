import os

from src.jengaapi.account_services import account_services
from src.jengaapi.auth import JengaAPI
from datetime import datetime

from src.jengaapi.utils import generate_reference

API_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
MERCHANT_CODE = os.getenv("MERCHANT_CODE")
ACCOUNT_NAME = os.getenv("ACCOUNT_NAME")
ACCOUNT_NUMBER = os.getenv("ACCOUNT_NUMBER")
BASE_URL = os.getenv("JENGA_API_BASE_URL", "https://uat.finserve.africa/")
SOURCE_ACCOUNT_NUMBER = ACCOUNT_NUMBER
TRANSFER_AMOUNT = "100.00"
CURRENCY_CODE = "KES"
REFERENCE_NO = generate_reference()
DATE = datetime.now().date().strftime("%Y-%m-%d")
COUNTRY_CODE = "KE"

payload = {
    "source": {
        "countryCode": "KE",
        "name": ACCOUNT_NAME,
        "accountNumber": ACCOUNT_NUMBER,
        "currency": "KES"
    },
    "destination": {
        "type": "bank",
        "countryCode": "KE",
        "name": ACCOUNT_NAME,
        "bankCode": "70",
        "accountNumber": ACCOUNT_NUMBER
    },
    "transfer": {
        "type": "RTGS",
        "amount": TRANSFER_AMOUNT,
        "currencyCode": "KES",
        "reference": REFERENCE_NO,
        "date": DATE,
        "description": "Some remarks here"
    }
}
api = JengaAPI(API_KEY, CONSUMER_SECRET, MERCHANT_CODE, BASE_URL)
api_token = api.authorization_token
data = (COUNTRY_CODE, ACCOUNT_NUMBER)
signature = api.signature(data)
res = account_services.account_mini_statement(signature, api_token, COUNTRY_CODE, ACCOUNT_NUMBER)
print(res)
