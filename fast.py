from typing import Union
from fastapi import FastAPI
import utills.rest_responses as rest
from http import HTTPStatus
import coloredlogs, logging
import kcoin


#####################Global Variables ########################

app = FastAPI()

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

#####################End of Global Variables #################


@app.get("/")
def read_root():
    logger.info("Enter to Root of API v1")

    r_json = {"Hello": "World"}
    r =  rest.REST()
    ret = r.Rest_Response("Welcome to API v1 Kucoin-Fastmovie", "", r_json, HTTPStatus.OK)

    logger.info("Close from Root of API v1")
    return ret

@app.get('/server-time')
def serverTime():
    server_time = kcoin.get_servertime()
    date_time = server_time[0]
    timestamp = server_time[1]

    r_json =  {'server-timestamp': timestamp, 'server-time': date_time}
    r =  rest.REST()
    ret = r.Rest_Response("Sent ServerTime successfully", "", r_json, HTTPStatus.OK)
    return ret
    

@app.get("/historical/{symbol}")
def get_historical_data(symbol: str, q: Union[str, None] = None):
    data = kcoin.get_historical_data(symbol)
    r_json = data
    r =  rest.REST()
    ret = r.Rest_Response("Historical DATA sent successfully", "", r_json, HTTPStatus.OK)
    return ret


@app.get('/portfo')
def get_accounts():
    r_json = kcoin.get_accounts()
    r =  rest.REST()
    ret = r.Rest_Response("Account information sent successfully", "", r_json, HTTPStatus.OK)
    return ret


@app.get('/order/buy/{symbol}/{price}/{size}')
def buy(symbol: str, price: str, size: str, q: Union[str,None] = None):
    r_json = kcoin.buy_service(symbol, price, size)
    r =  rest.REST()
    ret = r.Rest_Response("Buy operation is completed now.", "", r_json, HTTPStatus.OK)
    return ret


@app.get('/order/sell/{symbol}/{price}/{size}')
def sell(symbol: str, price: str, size: str, q: Union[str,None] = None):
    r_json = {'data': kcoin.buy_service(symbol, price, size, 'sell')}
    r =  rest.REST()
    ret = r.Rest_Response("Sell operation is completed now.", "", r_json, HTTPStatus.OK)
    return ret

@app.get('order/cancel/{order_id}')
def cancel(order_id: str, q: Union[str,None] = None):
    logger.info("Enter to Cancel-Order controller successfully")
    
    r_json = kcoin.cancel_order(order_id)
    r =  rest.REST()
    ret = r.Rest_Response("Buy operation is completed now.", "", r_json, HTTPStatus.OK)

    logger.info("Close from Cancel-Order controller successfully")
    return ret