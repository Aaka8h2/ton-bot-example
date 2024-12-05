BOT_TOKEN = '7330552132:AAFVGZHa6NyMNcm2oQ6n8KvzK25bNmVQX5I'
DEPOSIT_ADDRESS = 'UQCYYrnKkXhhVjLBMUw5ZLxMiEporAtTdjqxLbLKqWNGagOE'
API_KEY = 'YOUR API KEY'
RUN_IN_MAINNET = True  # Switch True/False to change mainnet to testnet

if RUN_IN_MAINNET:
    API_BASE_URL = 'https://toncenter.com'
else:
    API_BASE_URL = 'https://testnet.toncenter.com'
