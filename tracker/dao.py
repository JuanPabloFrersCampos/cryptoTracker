from .models import Operation, Crypto
from django.core.cache import cache
from django.db.models import QuerySet

class Dao():
    def get_operations_by_symbol(self, symbolName):
        return Operation.objects.filter(symbol__symbol=symbolName)

    def get_all_symbols(self):
        cryptoSymbols = cache.get('cryptoSymbols')
        if cryptoSymbols:
            return cryptoSymbols
        else:
            symbols = self.__fetch_all_symbols()
            cache.set('cryptoSymbols', symbols)
            return symbols
    
    def __fetch_all_symbols(self):
        return Crypto.objects.all()
    
    def get_all_operations_grouping_by_symbol(self):
        operationsBySimbol = []
        for symbol in self.get_all_symbols():
            operationsBySimbol.append(self.get_operations_by_symbol(symbol))
        return operationsBySimbol
    
    def get_user_portfolio(self) -> QuerySet:
        return Operation.objects.all() #esto devuelve todo, en el futuro cambiar