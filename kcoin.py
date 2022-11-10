from kucoin.client import Market
from kucoin.client import User
from kucoin.client import Trade

API_KEY = '6362afa841a5330001d201e4'
API_SECRET = '3dd0c2b1-ad0b-4acb-9a1e-9bd24feac8b7'
API_PASSPHRASE = 'RogerWaters2014'


def get_historical_data(symbol):
    client = Market(url='https://api.kucoin.com')
    markets = client.get_trade_histories(symbol)
    return markets

def get_servertime():
    client = Market(url='https://api.kucoin.com')
    server_time = client.get_server_timestamp()
    from datetime import datetime
    ts = int(server_time/1000)

    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case
    return (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'), ts)

def get_accounts():
    client = User(API_KEY, API_SECRET, API_PASSPHRASE, is_sandbox=True)
    accounts = client.get_account_list()
    return accounts

def buy_service(symbol, price, size, state='buy'):
    client = Trade(API_KEY, API_SECRET, API_PASSPHRASE, is_sandbox=True)
    order_id = client.create_limit_order(symbol, state, size, price)
    return order_id