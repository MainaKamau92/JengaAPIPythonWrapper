import os


def pytest_generate_tests(metafunc):
    os.environ['ENVIRONMENT'] = "testing"
