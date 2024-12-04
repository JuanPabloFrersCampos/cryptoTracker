from celery import shared_task
from .externalCryptoPriceFetcher import ExternalCryptoPriceFetcher
from .dao import dao

@shared_task
def fetchCryptoPricesBackgroundTask():
    print('BT')
    symbols = ['BTCUSDT', 'ETHUSDT']
    for symbol in symbols:
        externalCryptoPriceFetcher = ExternalCryptoPriceFetcher(symbol=symbol)
        externalCryptoPriceFetcher.fetchPrices()