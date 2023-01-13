from jengaapi.configs.config import app_config
from jengaapi.services.authorization_service import AuthorizationService
from jengaapi.services.account_services import AccountServices
from jengaapi.services.send_money_services import SendMoneyService

#

# Create a config file and set the environment variables
uat_config = app_config.get('uat')

COUNTRY_CODE = 'KE'
ACCOUNT_NO = "1450160649886"
# Authorization Service
# fetch the authorization token
# Create an instance of the AuthorizationService class
auth = AuthorizationService(config=uat_config)
auth_token = auth.auth_token

# Account Service
# account = AccountServices(config=uat_config)
# Signature = (countryCode, accountId)
# signature = auth.signature((COUNTRY_CODE, ACCOUNT_NO))
# Get account balance
# account_balance = account.account_balance(signature=signature, api_token=auth_token, country_code=COUNTRY_CODE,
#                                           account_id=ACCOUNT_NO)
# print(account_balance)
# {'status': True, 'code': 0, 'message': 'success', 'data': {'balances': [{'amount': '485115080.54', 'type': 'Available'},
#                                                                         {'amount': '485115080.54', 'type': 'Current'}], 'currency': 'KES'}}
# Get account mini statement
# account_mini_statement = account.account_mini_statement(signature=signature, api_token=auth_token,
#                                                         country_code=COUNTRY_CODE, account_no=ACCOUNT_NO)
# print(account_mini_statement)
# {
#    "status":true,
#    "code":0,
#    "message":"success",
#    "data":{
#       "balance":484837600.0,
#       "currency":"KES",
#       "accountNumber":"1450160649886",
#       "transactions":[
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE CREDIT 673579650955356",
#             "chequeNumber":"None",
#             "type":"Credit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE DEBIT 673579650955356",
#             "chequeNumber":"None",
#             "type":"Debit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE CREDIT 673579628084879",
#             "chequeNumber":"None",
#             "type":"Credit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE DEBIT 673579628084879",
#             "chequeNumber":"None",
#             "type":"Debit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE CREDIT 673579623845546",
#             "chequeNumber":"None",
#             "type":"Credit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE DEBIT 673579623845546",
#             "chequeNumber":"None",
#             "type":"Debit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE CREDIT 673579539764121",
#             "chequeNumber":"None",
#             "type":"Credit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"JENGA CHARGE DEBIT 673579539764121",
#             "chequeNumber":"None",
#             "type":"Debit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"REV-(673540528125447)JENGA CHARGE CREDIT 673540527",
#             "chequeNumber":"None",
#             "type":"Credit"
#          },
#          {
#             "date":"2023-01-12T00:00:00.000",
#             "amount":"1",
#             "description":"REV-(673540528125447)JENGA CHARGE DEBIT 6735405275",
#             "chequeNumber":"None",
#             "type":"Debit"
#          }
#       ]
#    }
# }

# account inquiry bank accounts
# account_inquiry = account.account_inquiry_bank_accounts(signature=signature, api_token=auth_token,
#                                                         country_code=COUNTRY_CODE, account_no=ACCOUNT_NO)
# print(account_inquiry)
# {
#    "status":true,
#    "code":0,
#    "message":"success",
#    "data":{
#       "account":{
#          "branchCode":"145",
#          "number":"1450160649886",
#          "currency":"KES",
#          "status":"Active"
#       },
#       "customer":[
#          {
#             "name":"CATHERINE MURANDITSI MUKABWA",
#             "id":"54307789658",
#             "type":"Retail"
#          }
#       ]
#    }
# }
# ===================================================================================
# get opening and closing balance
# ep_signature = auth.signature((ACCOUNT_NO, COUNTRY_CODE, "2023-01-01"))
# payload = dict(
#     countryCode=COUNTRY_CODE,
#     accountId=ACCOUNT_NO,
#     date="2023-01-01",
# )
# opening_closing = account.opening_closing_account_balance(ep_signature, auth_token, **payload)
# print(opening_closing)
# {
#    "status":true,
#    "code":0,
#    "message":"success",
#    "data":{
#       "balances":[
#          {
#             "amount":"0",
#             "type":"Closing Balance"
#          },
#          {
#             "amount":"0",
#             "type":"Opening Balance"
#          }
#       ]
#    }
# }

# ===================================================================================
# get account statement
# payload = {
#     "countryCode": COUNTRY_CODE,
#     "accountNumber": ACCOUNT_NO,
#     "fromDate": "2023-01-01",
#     "toDate": "2023-01-12",
#     "limit": 3
# }
# ep_signature = auth.signature((ACCOUNT_NO, COUNTRY_CODE, "2023-01-12"))
# account_full_statement = account.account_full_statement(ep_signature, auth_token, **payload)
# print(account_full_statement)
# {
#    "status":true,
#    "code":0,
#    "message":"success",
#    "data":{
#       "balance":484837600.0,
#       "currency":"KES",
#       "accountNumber":"1450160649886",
#       "transactions":[
#          {
#             "reference":"673580938172816",
#             "date":"2023-01-12T00:00:00.000",
#             "amount":1,
#             "serial":"1",
#             "description":"JENGA CHARGE CREDIT 673580937935574",
#             "postedDateTime":"2023-01-13T06:35:41.000",
#             "type":"Credit",
#             "runningBalance":{
#                "amount":76638.3,
#                "currency":"KES"
#             },
#             "transactionId":"54199"
#          },
#          {
#             "reference":"673580938172816",
#             "date":"2023-01-12T00:00:00.000",
#             "amount":1,
#             "serial":"2",
#             "description":"JENGA CHARGE DEBIT 673580937935574",
#             "postedDateTime":"2023-01-13T06:35:40.000",
#             "type":"Debit",
#             "runningBalance":{
#                "amount":76637.3,
#                "currency":"KES"
#             },
#             "transactionId":"54199"
#          },
#          {
#             "reference":"673579796228455",
#             "date":"2023-01-12T00:00:00.000",
#             "amount":1,
#             "serial":"3",
#             "description":"JENGA CHARGE CREDIT 673579795981233",
#             "postedDateTime":"2023-01-13T06:16:38.000",
#             "type":"Credit",
#             "runningBalance":{
#                "amount":76638.3,
#                "currency":"KES"
#             },
#             "transactionId":"54198"
#          }
#       ]
#    }
# }

# ===================================================================================
# Send money service
send_money = SendMoneyService(config=uat_config)

# send money within equity
# payload = {
#     "source": {
#         "countryCode": COUNTRY_CODE,
#         "name": "CATHERINE MURANDITSI MUKABWA",
#         "accountNumber": ACCOUNT_NO
#     },
#     "destination": {
#         "type": "bank",
#         "countryCode": "KE",
#         "name": "Tom Doe",
#         "accountNumber": "0250163591202"
#     },
#     "transfer": {
#         "type": "InternalFundsTransfer",
#         "amount": "1000.00",
#         "currencyCode": "KES",
#         "reference": "692494625798",
#         "date": "2023-08-18",
#         "description": "some remarks here"
#     }
# }
# ep_signature = auth.signature((ACCOUNT_NO,"1000.00", "KES", "692494625798"))
# send_money_within_equity = send_money.send_within_equity(ep_signature, auth_token, **payload)
# print(send_money_within_equity)

# ===================================================================================
# send money to mobile wallets
payload = {
    "source": {
        "countryCode": "KE",
        "name": "CATHERINE MURANDITSI MUKABWA",
        "accountNumber": ACCOUNT_NO
    },
    "destination": {
        "type": "mobile",
        "countryCode": "KE",
        "name": "A N.Other",
        "mobileNumber": "0722123456",
        "walletName": "Mpesa"
    },
    "transfer": {
        "type": "MobileWallet",
        "amount": "1000",
        "currencyCode": "KES",
        "date": "2023-01-13",
        "description": "some remarks here"
    }
}
ep_signature = auth.signature(("1000", "KES", "692494625799", ACCOUNT_NO))
send_money_within_equity = send_money.send_to_mobile_wallets(ep_signature, auth_token, **payload)
print(send_money_within_equity)
