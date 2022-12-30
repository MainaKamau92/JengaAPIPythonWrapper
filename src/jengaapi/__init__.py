import os

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("JENGA_API_BASE_URL", "https://uat.finserve.africa/")
ENVIRONMENT = os.getenv("ENVIRONMENT")

MERCHANT_CODE = os.getenv("MERCHANT_CODE")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")