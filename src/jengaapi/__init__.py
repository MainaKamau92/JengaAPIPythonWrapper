import os

# from .auth import JengaAPI

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("JENGA_API_BASE_URL", "https://uat.finserve.africa/")
ENVIRONMENT = os.getenv("ENVIRONMENT")

MERCHANT_CODE = os.getenv("MERCHANT_CODE")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
# ACCOUNT_ID = os.getenv("ACCOUNT_ID")
# ACCOUNT_NO = os.getenv("ACCOUNT_NO")
# COUNTRY_CODE = os.getenv("COUNTRY_CODE")
# PARTNER_ID = os.getenv("PARTNER_ID")
# BILLER_CODE = os.getenv("BILLER_CODE")
# PAYER_NAME = os.getenv("PAYER_NAME")
# PAYER_ACCOUNT = os.getenv("PAYER_ACCOUNT")

# API = JengaAPI(API_KEY, CONSUMER_SECRET, MERCHANT_CODE, BASE_URL)
