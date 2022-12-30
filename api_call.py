# TODO: Remove once done testing
import os

from src.jengaapi.account_services import account_services
from src.jengaapi.auth import JengaAPI
from src.jengaapi.exceptions import generate_reference
from src.jengaapi.send_money_imt_services import send_money_imt_service
from src.jengaapi.send_money_services import send_money_service
from datetime import datetime

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
    "source": {
        "countryCode": "KE",
        "name": "Merchant name",
        "accountNumber": ACCOUNT_NUMBER
    },
    "sender": {
        "name": "Sender Name",
        "documentType": "NationalId",
        "documentNumber": "12345",
        "countryCode": "KE",
        "mobileNumber": "0763000000",
        "email": "sender.name@example.com",
        "address": "Sender Address"
    },
    "destination": {
        "type": "mobile",
        "countryCode": "KE",
        "name": "A N.Other",
        "walletName": "Mpesa",
        "accountNumber": DEST_ACC_NO,
        "mobileNumber": "0763123456",
        "documentType": "NationalId",
        "documentNumber": "123456",
        "address": "Destination Address"
    },
    "transfer": {
        "type": "Pesalink",
        "amount": TRANSFER_AMOUNT,
        "currencyCode": CURRENCY_CODE,
        "date": DATE,
        "reference": REFERENCE_NO,
        "description": "some remarks here"
    }
}
api = JengaAPI(API_KEY, CONSUMER_SECRET, MERCHANT_CODE, BASE_URL)
api_token = api.authorization_token
data = (TRANSFER_AMOUNT, CURRENCY_CODE, REFERENCE_NO, "A N.Other", ACCOUNT_NUMBER)
signature = api.signature(data)
res = send_money_imt_service.send_pesa_link_to_mobile_number(signature, api_token, **payload)
print(res)
