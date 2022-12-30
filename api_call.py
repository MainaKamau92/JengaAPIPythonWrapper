# TODO: Remove once done testing
import os
from datetime import datetime

from src.jengaapi.auth import JengaAPI
from src.jengaapi.exceptions import generate_reference
from src.jengaapi.receive_money_services import receive_money_service
from src.jengaapi.send_money_imt_services import send_money_imt_service

API_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
MERCHANT_CODE = os.getenv("MERCHANT_CODE")
ACCOUNT_NAME = os.getenv("ACCOUNT_NAME")
ACCOUNT_NUMBER = os.getenv("ACCOUNT_NUMBER")
BASE_URL = os.getenv("JENGA_API_BASE_URL", "https://uat.finserve.africa/")
SOURCE_ACCOUNT_NUMBER = ACCOUNT_NUMBER
TRANSFER_AMOUNT = "1000.00"
CURRENCY_CODE = "KES"
COUNTRY_CODE = "KE"
FOREIGN_CURRENCY = "USD"
REFERENCE_NO = generate_reference()
DATE = datetime.now().date().strftime("%Y-%m-%d")
DEST_ACC_NO = "0250163591202"

payload = {
    "billerCode": "320320",
    "customerRefNumber": "111222",
    "amount": TRANSFER_AMOUNT,
    "amountCurrency": CURRENCY_CODE,
    "countryCode": COUNTRY_CODE,
}
api = JengaAPI(API_KEY, CONSUMER_SECRET, MERCHANT_CODE, BASE_URL)
api_token = api.authorization_token
data = ("0766000000", ACCOUNT_NUMBER, TRANSFER_AMOUNT, CURRENCY_CODE, REFERENCE_NO)
signature = api.signature(data)
res = receive_money_service.bill_validation(signature, api_token, **payload)
print(res)
