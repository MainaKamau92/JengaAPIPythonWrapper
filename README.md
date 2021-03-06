[![Pytest CI](https://github.com/MainaKamau92/JengaAPIPythonWrapper/actions/workflows/pytest.yml/badge.svg)](https://github.com/MainaKamau92/JengaAPIPythonWrapper/actions/workflows/pytest.yml) [![codecov](https://codecov.io/gh/MainaKamau92/JengaAPIPythonWrapper/branch/main/graph/badge.svg?token=cm9MaLo7Fc)](https://codecov.io/gh/MainaKamau92/JengaAPIPythonWrapper) [![Maintainability](https://api.codeclimate.com/v1/badges/883850b3a746cbc8f080/maintainability)](https://codeclimate.com/github/MainaKamau92/JengaAPIPythonWrapper/maintainability)

## JengaAPIPythonWrapper

A simple python wrapper around the JengaAPI from Equity Bank

## Setup

Installation

```pip install python-jengaapi```

Before beginning add these two environment variables in your .env file:

- BASE_URL="https://yourbaseurl.io" # if non is provided it defaults to https://uat.jengahq.io/
- ENVIRONMENT="production"

## SendMoneyService

```pycon

# Initial Setup
>>> from jengaapi.auth import JengaAPI
>>> API = JengaAPI(api_key="Basic TFZXxx", password="EhPPgRx4ZpxDrrznGdm25d", merchant_code="8995674492", base_url="https://uat.jengahq.io/")
>>> token = API.authorization_token

>>> from jengaapi.send_money_services import SendMoneyService
>>> send_money = SendMoneyService(token=token)
```

#### Send within equity

```pycon
# Generate signature by calling API.signature and passing the relevant tuple (the contents of this tuple are relative based on the request)
# e.g to generate signature for 
## generate signature for sending money within equity 
>>> signature = API.signature((source_account_number, transfer_amount,currency_code, reference_no))
>>> send_money.send_within_equity(signature, country_code="KE", source_name="John Doe", source_account_number="0770194201783", destination_account_number="0340197385508",destination_name="Jane Doe", transfer_amount="2300.00", currency_code="KES", reference_no="202108211617", transfer_date=date.today(), description="Send Money")
{'transactionId': '202108211618', 'status': 'SUCCESS'}
```

#### Send to mobile wallets

```pycon
>>> signature = API.signature((source_account_number, transfer_amount, currency_code, reference_no))
>>> send_money.send_to_mobile_wallets(signature, wallet_name="Equitel", destination_mobile_number="0763659874", country_code="KE", source_name="John Doe", source_account_number="0770194201783", destination_account_number="0340197385508",destination_name="Jane Doe", transfer_amount="2300.00", currency_code="KES", reference_no="162955567473", transfer_date=date.today(), description="Send Money")
{'transactionId': '162955567473', 'status': 'SUCCESS'}
```

#### Send RTGS

```pycon
>>> signature = API.signature((reference_no, transfer_date.strftime("%Y-%m-%d"), source_account_number, destination_account_number, transfer_amount))
>>> send_money.send_rtgs(signature, destination_account_number="0340197385508", bank_code="01", country_code="KE", source_name="John Doe", source_account_number="0770194201783", destination_name="Jane Doe", transfer_amount="1500.00", currency_code="KES", reference_no="162955622013", transfer_date=date.today(), description="Send Money")
{'transactionId': '000002399997', 'status': 'SUCCESS'}
```

#### Send Swift

```pycon
>>> signature = API.signature((reference_no, transfer_date.strftime("%Y-%m-%d"), source_account_number, destination_account_number, transfer_amount))
>>> send_money.send_rtgs(signature, destination_account_number="0340197385508", bank_code="01", country_code="KE", source_name="John Doe", source_account_number="0770194201783", destination_name="Jane Doe", transfer_amount="1500.00", currency_code="KES", reference_no="162955622013", transfer_date=date.today(), description="Send Money")
{'transactionId': '000002399997', 'status': 'SUCCESS'}
```

## To All Users

> This is the very first release of the package and despite most of the functionality already tested during development, a few bugs are expected. Feel free to create an issue and tag me and i'll get on it ASAP