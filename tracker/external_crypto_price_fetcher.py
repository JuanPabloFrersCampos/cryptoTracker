import requests
from typing import LiteralString
from django.core.cache import cache

class ExternalCryptoPriceFetcher:

    #def __init__(self):
        #self.symbol = symbol
        #self.cache_key = f'crypto_cotizations_{self.symbol}'
        #self.cached_cotization = cache.get(self.cache_key)

    # FIXME: Temporal patch to fix tests's mocking in external API
    # I don't like at ALL passing symbol, instead of creating class's instance
    # and setting self.symbol, but this is a workaround to make tests work.
    def getPrice(self, symbol: LiteralString): 
        catchedCotization = cache.get(f'crypto_cotizations_{symbol}')
        if catchedCotization:
            print('Cache hit')
            return catchedCotization
        else:
            return self.fetchPrices(symbol)
            
    def fetchPrices(self, symbol: LiteralString):
        symbolPair = symbol + '-USDT'
        api_url = 'https://api.coinbase.com/v2/prices/{}/spot'.format(symbolPair)
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            price = float(response.json().get("data", {}).get("amount"))
            cache.set(f'crypto_cotizations_{symbol}', price, timeout=35)
            return price
        else:
            cache.set(f'crypto_cotizations_{symbol}', None, timeout=35) # Temporal para que no afecte NEXO
            print("Error:", response.status_code, response.text)

    # def getCryptoSymbols(self):
    #     api_url = 'https://api.api-ninjas.com/v1/cryptosymbols'.format(self.symbol)
    #     response = requests.get(api_url, headers={'X-Api-Key': 'Ea+4rJb8CUaOu7dov3pSQA==WG3PQAgoqGgMjJmr'})
    #     return response.json()