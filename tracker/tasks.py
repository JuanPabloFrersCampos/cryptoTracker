from celery import shared_task
from .externalCryptoPriceFetcher import ExternalCryptoPriceFetcher
from .dao import Dao

@shared_task
def fetchCryptoPricesBackgroundTask():
    dao = Dao()
    symbols = dao.get_all_symbols()
    for symbol in symbols:
        externalCryptoPriceFetcher = ExternalCryptoPriceFetcher(symbol=symbol)
        externalCryptoPriceFetcher.fetchPrices()