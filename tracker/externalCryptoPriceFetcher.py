import requests
from django.core.cache import cache

class ExternalCryptoPriceFetcher:

    def __init__(self, symbol):
        self.symbol = symbol
        self.cache_key = f'crypto_cotizations_{self.symbol}'
        self.cached_cotization = cache.get(self.cache_key)

    def getPrice(self):
        if self.cached_cotization:
            return self.cached_cotization
        else:
            return self.fetchPrices()
            
    def fetchPrices(self):
        symbolPair = str(self.symbol) + '-USDT'
        api_url = 'https://api.coinbase.com/v2/prices/{}/spot'.format(symbolPair)
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            price = response.json().get("data", {}).get("amount")
            cache.set(self.cache_key, price, timeout=35)
            return price
        else:
            cache.set(self.cache_key, None, timeout=35) # Temporal para que no afecte NEXO
            print("Error:", response.status_code, response.text)

    # def getCryptoSymbols(self):
    #     api_url = 'https://api.api-ninjas.com/v1/cryptosymbols'.format(self.symbol)
    #     response = requests.get(api_url, headers={'X-Api-Key': 'Ea+4rJb8CUaOu7dov3pSQA==WG3PQAgoqGgMjJmr'})
    #     return response.json()