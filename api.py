import requests

# if work,all network requests must go through proxies
DEBUG = True


class Api():
    _exchange_name = ""
    _baseurl = ''

    # currency_pair对不同的交易所统一做处理，交易币在前，基准币在后
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
            'http': '127.0.0.1:1081',
            'https': '127.0.0.1:1081'
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
    _baseurl = 'http://data.gate.io/api2/1'

    def getCurrentPrice(self, currency_pair, direction):
        index = 0
        if 'buy' == direction:
            direction = 'asks'
            index = -1
        elif 'sell' == direction:
            direction = 'bids'
        result = self._get_proxied(self._baseurl + "/orderBook/" + currency_pair)
        result_json = result.json()
        price = result_json[direction][index][0]
        return float(price)


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


class BitfinexApi(HttpApi):
    _exchange_name = 'bitfinex'


class BittrexApi(HttpApi):
    _exchange_name = 'bittrex'


class BinanceApi(HttpApi):
    _exchange_name = 'binance'
    _baseurl = "https://www.binance.com/api"

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'asks'
        elif 'sell' == direction:
            direction = 'bids'
        params = {
            "symbol": currency_pair
        }
        result = self._get_proxied(self._baseurl + "/v1/depth", params)
        result_json = result.json()
        price = result_json[direction][0][0]
        return float(price)


if __name__ == '__main__':
    # cryptopiaApi = CryptopiaApi()
    # print(cryptopiaApi.getCurrentPrice("BTM_BTC", "sell"))
    # hitbtcApi = HitbtcApi()
    # print(hitbtcApi.getCurrentPrice("BTMETH", "sell"))
    gateioApi = GateioApi()
    print(gateioApi.getCurrentPrice("lrc_eth", "sell"))
    # binanceApi = BinanceApi()
    # print(binanceApi.getCurrentPrice("LRCETH", "buy"))


