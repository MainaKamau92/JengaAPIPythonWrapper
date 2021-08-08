import os

from src.jengaapi.auth import JengaAPI

API_KEY = os.getenv("API_KEY")
UAT_BASE_URL = os.getenv("UAT_BASE_URL")
MERCHANT_CODE = os.getenv("MERCHANT_CODE")
PASSWORD = os.getenv("PASSWORD")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
ACCOUNT_NO = os.getenv("ACCOUNT_NO")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
PARTNER_ID = os.getenv("PARTNER_ID")

API = JengaAPI(API_KEY, PASSWORD, MERCHANT_CODE, UAT_BASE_URL)
