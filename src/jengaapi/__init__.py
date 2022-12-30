import os

from .utils import get_project_root

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("JENGA_API_BASE_URL", "https://uat.finserve.africa/")
ENVIRONMENT = os.getenv("ENVIRONMENT")
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH", os.path.join(get_project_root(), "privatekey.pem"))
TESTING_PRIVATE_KEY_PATH = os.path.join(get_project_root(), "tests/testkey.pem")
