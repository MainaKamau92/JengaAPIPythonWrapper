import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Config:
    API_KEY = os.getenv("API_KEY")
    BASE_URL = os.getenv("JENGA_API_BASE_URL")
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    MERCHANT_CODE = os.getenv("MERCHANT_CODE")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH")
    # PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH", os.path.join(BASE_DIR, "privatekey.pem"))


class ProductionConfig(Config):
    BASE_URL = "https://api.finserve.africa/"
    ENVIRONMENT = "production"


class UatConfig(Config):
    BASE_URL = "https://uat.finserve.africa/"
    ENVIRONMENT = "uat"


class TestingConfig(Config):
    BASE_URL = "https://uat.finserve.africa/"
    ENVIRONMENT = "testing"
    TESTING_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, "tests/testkey.pem")


app_config = {
    'production': ProductionConfig,
    'testing': TestingConfig,
    'uat': UatConfig,
}
