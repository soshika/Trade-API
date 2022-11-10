from kucoin.client import Client
from kucoin.client import Trade
from time import sleep
import uuid

queue = []
part_money = 0.0
static_total = 0.0
segment = 0
remind_part_money = {'status': False, 'index': 0}
timeframes = ['5min', '15min', '30min', '45min', '1hour', '2hour', '3hour', '4hour', '1day']

def personal_info():
    ret = {
        'api_key': '6362afa841a5330001d201e4',
        'api_secret': '3dd0c2b1-ad0b-4acb-9a1e-9bd24feac8b7',
        'api_passphrase': 'RogerWaters2014'
    }

    return ret

def get_time_frame():
    # by default we set the timeframe to 1min
    return '1hour'



def buy():
    pass

def sell():
    pass

def calculate_profit():
    pass


def process(symbol, timeframe, stop_profit, total):
    # klines = client.get_kline(symbol, timeframe)

    invest = calculate_price_to_invest(total)
    if invest[0] is None:
        print('you reach your limit :(')
        return None
    print('price to invest is : ', invest[0])
    
    pi = personal_info()
    m_client = Trade(pi['api_key'], pi['api_secret'], pi['api_passphrase'], is_sandbox=True)
    # cancel_order = m_client.cancel_order('6362b16936d21f0001bc4d51')
    ans = m_client.get_order_list()
    from pprint import pprint
    pprint(ans)
    # order_id = m_client.create_limit_order(symbol, 'buy', 1, 20000)
    order_id = uuid.uuid4()
    queue.append(order_id)

    print('order id is : ', order_id)
    return invest[1]
    

def calculate_price_to_invest(total):
    #TODO: its dynamic
    levels = [10.0, 20.0, 40.0, 50.0, 60.0, 100.0]

    if remind_part_money['status'] == False:
        remind_part_money['status'] = True
        percent = levels[0]

        global segment
        if segment == 0:
            return (None, None)
        global part_money
        global static_total

        part_money = percent * static_total / 100.0
        total -= part_money
        remind_part_money['index'] = 1
        segment -= 1

    else:
        percent = levels[remind_part_money['index']]
        remind_part_money['index'] += 1
        if remind_part_money['index'] == 5:
            #TODO: clean the quee or what?!
            remind_part_money['status'] = False
            remind_part_money['index'] = 0

    price = percent * part_money / 100.0
    part_money = part_money - price
    
    return (price, total)
    
    

if __name__ == '__main__':
    pi = personal_info()
    client = user.UserData(pi['api_key'], pi['api_secret'], pi['api_passphrase'])
    acc = user.create_account('trade', 'BTC')
    print(acc)
    #
    # # total investment money in usdt
    # total = float(input("Please Enter your total money in USDT: "))
    # static_total = total

    # # timeframe that robot runs ....
    # tf = input('Please Enter a timeframe: ')
    # if tf == '':
    #     tf = get_time_frame()

    # # symbol that we want to trade on
    # symbol = input("Please Enter a Symbol(BTC-USDT): ")
    # if symbol == '':
    #     symbol = 'CELR-USDT'
    
    # #stop-profit
    # stop_profit = float(input("Please Enter a Stopprofit: "))


    # #segment_count
    # segment = int(input("Please Enter Count of consecutive segments: "))
    # while True:
    #     sleep(1)
    #     total = process(symbol,tf, stop_profit, total)

    #     if total is None or total <= 0.0:
    #         print("Robot take a nap since you don't have any money :(")
    #         break
    