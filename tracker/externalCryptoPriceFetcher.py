import requests

class ExternalCryptoPriceFetcher:

    def __init__(self, symbol):
        self.symbol = symbol

    def getPrice(self):
        api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(self.symbol)
        response = requests.get(api_url, headers={'X-Api-Key': 'Ea+4rJb8CUaOu7dov3pSQA==WG3PQAgoqGgMjJmr'})
        if response.status_code == requests.codes.ok:
            return (response.json())["price"]
        else:
            print("Error:", response.status_code, response.text)