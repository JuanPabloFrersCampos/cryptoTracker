import requests
from django.core.cache import cache

class ExternalCryptoPriceFetcher:

    def __init__(self, symbolPair):
        self.symbolPair = symbolPair
        self.cache_key = f'crypto_cotizations_{self.symbolPair}'
        self.cached_cotization = cache.get(self.cache_key)

    def getPrice(self):
        return self.cached_cotization
            
    def fetchPrices(self):
        api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(self.symbolPair)
        response = requests.get(api_url, headers={'X-Api-Key': 'Ea+4rJb8CUaOu7dov3pSQA==WG3PQAgoqGgMjJmr'})
        if response.status_code == requests.codes.ok:
            price = response.json().get("price")
            cache.set(self.cache_key, price, timeout=35)
        else:
            cache.set(self.cache_key, None, timeout=35) # Temporal para que no afecte NEXO
            print("Error:", response.status_code, response.text)

    # def getCryptoSymbols(self):
    #     api_url = 'https://api.api-ninjas.com/v1/cryptosymbols'.format(self.symbol)
    #     response = requests.get(api_url, headers={'X-Api-Key': 'Ea+4rJb8CUaOu7dov3pSQA==WG3PQAgoqGgMjJmr'})
    #     return response.json()