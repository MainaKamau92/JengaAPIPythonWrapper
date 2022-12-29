
# TODO: Remove once done testing
import os

from src.jengaapi.account_services import account_services
from src.jengaapi.auth import JengaAPI
from src.jengaapi.exceptions import generate_reference
from src.jengaapi.send_money_services import send_money_service
from datetime import datetime

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

payload = {
   "countryCode": "KE",
   "accountId": ACCOUNT_NUMBER,
   "date": "2022-12-30"
}
api = JengaAPI(API_KEY, CONSUMER_SECRET, MERCHANT_CODE, BASE_URL)
api_token = api.authorization_token
data = ("KE", ACCOUNT_NUMBER)
signature = api.signature(data)
res = account_services.account_inquiry_bank_accounts(signature, api_token, "KE", ACCOUNT_NUMBER)
print(res)