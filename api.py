import requests

from util import *

# if work,all network requests must go through proxies
DEBUG = True


class Api():
    _exchange_name = ""
    _baseurl = ''

    def __init__(self):
        self._baseurl = exchangeConfigJson[self._exchange_name]['baseUrl']

    # currency_pair对不同的交易所统一做处理，交易币在前，基准币在后
    def getCurrencyPair(self, src_currency, dst_currency):
        # 处理同一币种在不同交易所名字不一样的问题
        if "aliases" in exchangeConfigJson[self._exchange_name]:
            if src_currency in exchangeConfigJson[self._exchange_name]['aliases']:
                src_currency = exchangeConfigJson[self._exchange_name]['aliases'][src_currency]
            if dst_currency in exchangeConfigJson[self._exchange_name]['aliases']:
                dst_currency = exchangeConfigJson[self._exchange_name]['aliases'][dst_currency]

        currencyPairTemplate = exchangeConfigJson[self._exchange_name]['currencyPairTemplate']
        isUpper = exchangeConfigJson[self._exchange_name]['isUpper']
        if isUpper:
            src_currency = src_currency.upper()
            dst_currency = dst_currency.upper()
        return currencyPairTemplate.replace("#SRC", src_currency).replace("#DST", dst_currency)

    def buy(self, currency_pair):
        pass

    def sell(self, currency_pair):
        pass

    def getDepth(self, currency_pair):
        pass

    def getCurrentPrice(self, currency_pair, direction):
        pass

    def getExchangeName(self):
        return self._exchange_name


class HttpApi(Api):
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    _proxies = {}
    if DEBUG:
        _proxies = {
            'http': '127.0.0.1:1080',
            'https': '127.0.0.1:1080'
        }

    def _get(self, url, **kwargs):
        return requests.get(url, headers=self._headers, **kwargs)

    def _get_proxied(self, url, *args, **kwargs):
        return requests.get(url, headers=self._headers, proxies=self._proxies, *args, **kwargs)


class WebSocketApi(Api):
    pass


class CryptopiaApi(HttpApi):
    _exchange_name = 'cryptopia'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'Sell'
        elif 'sell' == direction:
            direction = 'Buy'
        result = self._get_proxied("https://www.cryptopia.co.nz/api" + "/GetMarketOrders" + "/" + currency_pair)
        result_json = result.json()
        price = result_json['Data'][direction][0]['Price']
        return float(price)


class GateioApi(HttpApi):
    _exchange_name = 'gateio'

    def getCurrentPrice(self, currency_pair, direction):
        index = 0
        if 'buy' == direction:
            direction = 'asks'
            index = -1
        elif 'sell' == direction:
            direction = 'bids'
        try:
            result = self._get_proxied(self._baseurl + "/orderBook/" + currency_pair)
            result_json = result.json()
            price = result_json[direction][index][0]
            return float(price)
        except Exception as e:
            print(str(e))


class HitbtcWebSocketApi(WebSocketApi):
    pass


class HitbtcApi(HttpApi):
    _exchange_name = 'hitbtc'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'asks'
        elif 'sell' == direction:
            direction = 'bids'
        result = self._get_proxied("http://api.hitbtc.com/api" + "/1/public/" + currency_pair + "/orderbook")
        result_json = result.json()
        price = result_json[direction][0][0]
        return float(price)


class BittrexApi(HttpApi):
    _exchange_name = 'bittrex'


class BinanceApi(HttpApi):
    _exchange_name = 'binance'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'asks'
        elif 'sell' == direction:
            direction = 'bids'
        params = {
            "symbol": currency_pair
        }
        try:
            result = self._get_proxied(self._baseurl + "/v1/depth", params)
            result_json = result.json()
            price = result_json[direction][0][0]
            return float(price)
        except Exception as e:
            print(str(e))


class BitfinexApi(HttpApi):
    _exchange_name = 'bitfinex'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'asks'
        elif 'sell' == direction:
            direction = 'bids'
        try:
            result = self._get_proxied(self._baseurl + "/book/" + currency_pair)
            result_json = result.json()
            price = result_json[direction][0]["price"]
            return float(price)
        except Exception as e:
            print(str(e))


class HuobiApi(HttpApi):
    _exchange_name = 'huobi'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'asks'
        elif 'sell' == direction:
            direction = 'bids'
        params = {
            "symbol": currency_pair,
            "type": "step0"
        }
        try:
            result = self._get_proxied(self._baseurl + "/market/depth", params)
            result_json = result.json()
            price = result_json["tick"][direction][0][0]
            return float(price)
        except Exception as e:
            print(str(e))


class OkexApi(HttpApi):
    _exchange_name = 'okex'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'asks'
        elif 'sell' == direction:
            direction = 'bids'
        params = {
            "symbol": currency_pair,
            "size": 10,
        }
        try:
            result = self._get_proxied(self._baseurl + "/v1/depth.do", params)
            result_json = result.json()
            index = 0
            if 'asks' == direction:
                index = -1
            price = result_json[direction][index][0]
            return float(price)
        except Exception as e:
            print(str(e))


class BigoneApi(HttpApi):
    _exchange_name = 'bigone'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'asks'
        elif 'sell' == direction:
            direction = 'bids'
        try:
            result = self._get_proxied(self._baseurl + "/markets/" + currency_pair + "/book")
            result_json = result.json()
            price = result_json['data'][direction][0]['price']
            return float(price)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    # cryptopiaApi = CryptopiaApi()
    # print(cryptopiaApi.getCurrentPrice("BTM_BTC", "sell"))
    # hitbtcApi = HitbtcApi()
    # print(hitbtcApi.getCurrentPrice("BTMETH", "sell"))
    # gateioApi = GateioApi()
    # print(gateioApi.getCurrentPrice("btm_eth", "sell"))
    # binanceApi = BinanceApi()
    # print(binanceApi.getCurrentPrice("btm", "eth"))
    # bitfinexApi = BitfinexApi()
    # print(bitfinexApi.getCurrencyPair("qash", "eth"))
    # huobiApi = HuobiApi()
    # print(huobiApi.getCurrentPrice("qasheth", "buy"))
    # print(binanceApi.getCurrentPrice("LRCETH", "buy"))
    # okexApi = OkexApi()
    # print(okexApi.getCurrentPrice("eth_btc", "buy"))
    bigoneApi = BigoneApi()
    print(bigoneApi.getCurrentPrice("ETH-BTC", "buy"))
