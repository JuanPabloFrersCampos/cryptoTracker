from celery import shared_task
from .external_crypto_price_fetcher import ExternalCryptoPriceFetcher
from .dao import Dao

# esta task debería ser scheduleada por código, no por bdd
@shared_task
def fetchCryptoPricesBackgroundTask():
    dao = Dao()
    external_crypto_price_fetcher = ExternalCryptoPriceFetcher()
    symbols = dao.get_all_symbols()
    for symbol in symbols:
        # FIXME: Temporal patch to fix tests's mocking in external API
        #external_crypto_price_fetche = external_crypto_price_fetche.getPrice(symbol = symbol)
        external_crypto_price_fetcher.fetchPrices(symbol=symbol.symbol)