import requests

# if work,all network requests must go through proxies
DEBUG = True


class Api():
    _exchange_name = ""

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
            'http': '127.0.0.1:1080',
            'https': '127.0.0.1:1080'
        }

    def _get(self, url, **kwargs):
        return requests.get(url, headers=self._headers, **kwargs)

    def _get_proxied(self, url, **kwargs):
        return requests.get(url, headers=self._headers, proxies=self._proxies, **kwargs)


class WebSocketApi(Api):
    pass


class CryptopiaApi(HttpApi):
    __exchange_name = 'cryptopia'

    def getCurrentPrice(self, currency_pair, direction):
        if 'buy' == direction:
            direction = 'Sell'
        elif 'sell' == direction:
            direction = 'Buy'
        result = self._get_proxied("https://www.cryptopia.co.nz/api" + "/GetMarketOrders" + "/" + currency_pair)
        result_json = result.json()
        price = result_json['Data'][direction][0]['Price']
        return float(price)


# class GateioApi(HttpApi):


if __name__ == '__main__':
    cryptopiaApi = CryptopiaApi()
    print(cryptopiaApi.getCurrentPrice("BTM_BTC", "sell"))


