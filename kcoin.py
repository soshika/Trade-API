import os
from kucoin.client import Market
from kucoin.client import User
from kucoin.client import Trade
from dotenv import load_dotenv



#####################Global Variables ########################

load_dotenv()
base_url = 'https://api.kucoin.com'

#####################End of Global Variables #################


def get_historical_data(symbol):
    client = Market(url=base_url)
    markets = client.get_trade_histories(symbol)
    return markets

def get_servertime():
    client = Market(url=base_url)
    server_time = client.get_server_timestamp()
    from datetime import datetime
    ts = int(server_time/1000)

    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case
    return (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'), ts)

def get_accounts():
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    API_PASSPHRASE = os.getenv('API_PASSPHRASE')
    client = User(API_KEY, API_SECRET, API_PASSPHRASE, is_sandbox=True)
    accounts = client.get_account_list()
    return accounts

def buy_service(symbol, price, size, state='buy'):
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    API_PASSPHRASE = os.getenv('API_PASSPHRASE')
    client = Trade(API_KEY, API_SECRET, API_PASSPHRASE, is_sandbox=True)
    order_id = client.create_limit_order(symbol, state, size, price)
    return order_id

def cancel_order(order_id):
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    API_PASSPHRASE = os.getenv('API_PASSPHRASE')
    client = Trade(API_KEY, API_SECRET, API_PASSPHRASE, is_sandbox=True)
    return client.cancel_order(order_id)
    