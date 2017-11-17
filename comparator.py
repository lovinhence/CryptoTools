from api import *

exchangeConfigJson = getExchangeConfigJson()

f = open(".\\config\\comparator.conf")
lines = f.readlines()
for line in lines:
    config = line.split(",")
    src_exchange, dst_exchange, src_currency, dst_currency = config[0], config[1], config[2], config[3]
    src_exchange_api = eval(exchangeConfigJson[src_exchange]['className'])()
    dst_exchange_api = eval(exchangeConfigJson[dst_exchange]['className'])()
    src_currency_pair = src_exchange_api.getCurrencyPair(src_currency, dst_currency)
    dst_currency_pair = dst_exchange_api.getCurrencyPair(src_currency, dst_currency)
    ratio_src_dst = dst_exchange_api.getCurrentPrice(dst_currency_pair, "sell") / src_exchange_api.getCurrentPrice(
        src_currency_pair, "buy")
    ratio_dst_src = src_exchange_api.getCurrentPrice(src_currency_pair, "sell") / dst_exchange_api.getCurrentPrice(
        dst_currency_pair, "buy")
    print(ratio_dst_src)
    print(ratio_src_dst)



