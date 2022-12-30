[![Pytest CI](https://github.com/MainaKamau92/JengaAPIPythonWrapper/actions/workflows/pytest.yml/badge.svg)](https://github.com/MainaKamau92/JengaAPIPythonWrapper/actions/workflows/pytest.yml) [![codecov](https://codecov.io/gh/MainaKamau92/JengaAPIPythonWrapper/branch/main/graph/badge.svg?token=cm9MaLo7Fc)](https://codecov.io/gh/MainaKamau92/JengaAPIPythonWrapper) [![Maintainability](https://api.codeclimate.com/v1/badges/883850b3a746cbc8f080/maintainability)](https://codeclimate.com/github/MainaKamau92/JengaAPIPythonWrapper/maintainability)

## JengaAPIPythonWrapper

A simple python wrapper around the JengaAPI from Equity Bank

## Setup

Installation

```
pip install python-jengaapi
```

A sample of the `.env` variables required include:
```
MERCHANT_CODE=1234567
CONSUMER_SECRET=XXXXXXXXXXXXX
API_KEY=123XXX222
ACCOUNT_NAME=John Doe
ACCOUNT_NUMBER=12345678
CURRENCY_CODE=KES
COUNTRY_CODE=KE
FOREIGN_CURRENCY_CODE=USD
PRIVATE_KEY_PATH=path_to_privatekey.pem
```

### ACCOUNT SERVICES
#### Account Balance
This web service enables an application or service retrieve the current and available balance of an account:
```pycon
# script.py
import os
from jengaapi.auth import JengaAPI
from jengaapi.account_services import account_services

# Get the environment variables
MERCHANT_CODE = os.getenv('MERCHANT_CODE')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
COUNTRY_CODE = os.getenv('COUNTRY_CODE')
ACCOUNT_NUMBER = os.getenv('ACCOUNT_NUMBER')

# Initialize the JengaAPI class
api = JengaAPI(CONSUMER_SECRET, MERCHANT_CODE)
api_token = api.authorization_token
signature_data = (COUNTRY_CODE, ACCOUNT_NUMBER)
signature = api.signature(signature_data)

response = account_services.account_balance(
    signature=signature,
    api_token=api_token,
    country_code=COUNTRY_CODE,
    account_id=ACCOUNT_NUMBER
)
print(response)
```
```shell
$ python script.py
{'status': True, 'code': 0, 'message': 'success', 'data': {'balances': [{'amount': '485657113.54', 'type': 'Available'}, {'amount': '485657113.54', 'type': 'Current'}], 'currency': 'KES'}}
```

#### Account MINI Statement
This service will return the last (10) ten transactions of a given account number.
It's a super efficient service compared to the fullstatement web service.
```pycon
signature_data = (COUNTRY_CODE, ACCOUNT_NUMBER)
signature = api.signature(signature_data)

response = account_services.account_mini_statement(
    signature=signature,
    api_token=api_token,
    country_code=COUNTRY_CODE,
    account_id=ACCOUNT_NUMBER
)
print(response)
```
```shell
$ python script.py
{'status': True, 'code': 0, 'message': 'success', 'data': {'balance': 485432544.0, 'currency': 'KES', 'accountNumber': '1450160649886', 'transactions': [{'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE CREDIT 672439264275530', 'chequeNumber': None, 'type': 'Credit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE DEBIT 672439264275530', 'chequeNumber': None, 'type': 'Debit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE CREDIT 672438677873258', 'chequeNumber': None, 'type': 'Credit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE DEBIT 672438677873258', 'chequeNumber': None, 'type': 'Debit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE CREDIT 672438010400777', 'chequeNumber': None, 'type': 'Credit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE DEBIT 672438010400777', 'chequeNumber': None, 'type': 'Debit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE CREDIT 672437798372104', 'chequeNumber': None, 'type': 'Credit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE DEBIT 672437798372104', 'chequeNumber': None, 'type': 'Debit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE CREDIT 672437574565510', 'chequeNumber': None, 'type': 'Credit'}, {'date': '2022-12-30T00:00:00.000', 'amount': '1', 'description': 'JENGA CHARGE DEBIT 672437574565510', 'chequeNumber': None, 'type': 'Debit'}]}}
```

### SEND MONEY SERVICES
#### RTGS 
```pycon
data = ("922651940124", "2022-12-30", ACCOUNT_NUMBER, "0250163591202", "1000.00")
signature = api.signature(data)
payload = {
    "source": {
        "countryCode": "KES",
        "name": "John Doe",
        "currency": "KES",
        "accountNumber": ACCOUNT_NUMBER
    },
    "destination": {
        "type": "bank",
        "countryCode": "KE",
        "name": "Tom Doe",
        "bankCode": "01",
        "accountNumber": "0250163591202"
    },
    "transfer": {
        "type": "RTGS",
        "amount": "1000.00",
        "currencyCode": "KES",
        "reference": "922651940124",
        "date": "2022-12-30",
        "description": "some remarks here"
    }
}
res = send_money_service.send_rtgs(signature, api_token, **payload)
print(res)
```
```shell
$ python script.py
{"transactionId": "000000403777", "status": "SUCCESS"}
```
