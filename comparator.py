from api import *
from util import *
import threading
import time

exchangeConfigJson = getExchangeConfigJson()


def compare(src_exchange, dst_exchange, src_currency, dst_currency):
    src_exchange_api = eval(exchangeConfigJson[src_exchange]['className'])()
    dst_exchange_api = eval(exchangeConfigJson[dst_exchange]['className'])()
    src_currency_pair = src_exchange_api.getCurrencyPair(src_currency, dst_currency)
    dst_currency_pair = dst_exchange_api.getCurrencyPair(src_currency, dst_currency)
    try:
        ratio_src_dst = dst_exchange_api.getCurrentPrice(dst_currency_pair, "sell") / src_exchange_api.getCurrentPrice(
            src_currency_pair, "buy")
        ratio_dst_src = src_exchange_api.getCurrentPrice(src_currency_pair, "sell") / dst_exchange_api.getCurrentPrice(
            dst_currency_pair, "buy")
        ratio_src_dst_str = "%s:%s,%s buy,%s sell:%f" % (
            src_currency, dst_currency, src_exchange, dst_exchange, ratio_src_dst)
        ratio_dst_src_str = "%s:%s,%s buy,%s sell:%f" % (
            src_currency, dst_currency, dst_exchange, src_exchange, ratio_dst_src)
        print(ratio_src_dst_str)
        print(ratio_dst_src_str)
        if ratio_src_dst > 1.015:
            alert(ratio_src_dst_str)
        if ratio_dst_src > 1.015:
            alert(ratio_dst_src_str)
    except Exception as e:
        print(str(e))


def loop_compare(src_exchange, dst_exchange, src_currency, dst_currency, timeout=2):
    while True:
        compare(src_exchange, dst_exchange, src_currency, dst_currency)
        time.sleep(timeout)


def start_compare():
    try:
        f = open(".\\config\\comparator.conf")
        lines = f.readlines()
    finally:
        f.close()
    for line in lines:
        line = line.replace("\n", "")
        config = line.split(",")
        src_exchange, dst_exchange, src_currency, dst_currency = config[0], config[1], config[2], config[3]
        t = threading.Thread(target=loop_compare, args=(src_exchange, dst_exchange, src_currency, dst_currency))
        t.start()
        # compare(src_exchange, dst_exchange, src_currency, dst_currency)


if __name__ == '__main__':
    start_compare()





