import requests


class Api():
    _exchange_name = ""

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

    _proxies = {
        'http': '127.0.0.1:1080',
        'https': '127.0.0.1:1080'
    }

    def _get(self, url, **kwargs):
        return requests.get(url, headers=self._headers, **kwargs)

    def _get_proxied(self, url, **kwargs):
        return requests.get(url, headers=self._headers, proxies=self._proxies, **kwargs)


def WebSocketApi(Api):
    pass


class CryptopiaApi(HttpApi):
    __exchange_name = 'cryptopia'

    def getDepth(self, currency_pair):
        pass

