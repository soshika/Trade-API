#  MarketData
# from kucoin.client import Market
# from pprint import pprint


# client = Market(url='https://api.kucoin.com')

# markets = client.get_trade_histories('UOS-USDT')
# print(len(markets))
# # pprint(markets)


# api_key = '6362afa841a5330001d201e4'
# api_secret = '3dd0c2b1-ad0b-4acb-9a1e-9bd24feac8b7'
# api_passphrase = 'RogerWaters2014'

# from kucoin.client import User
# client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

# accounts = client.get_account_list()
# from pprint import pprint
# pprint(accounts)

# import utills.rest_responses as rest
# from http import HTTPStatus
# import datasource.redis_c as redis_client

# import json
# # r = rest.REST()
# # ret = r.Rest_Response("inserted", "successfully inserted",None, HTTPStatus.CREATED)
# # print(ret)

# r = redis_client.REDIS().r

# ans = r.set('foo1', json.dumps({'bar': "barrrrrrr"}))
# print(ans)

# res = r.get('foo1').decode('utf8')
# print(res)