from .models import Operation, Crypto

class dao():
    def get_operations_by_symbol(symbolName):
        return Operation.objects.filter(symbol__symbol=symbolName)

    @staticmethod
    def get_all_symbols():
        return Crypto.objects.all()
    
    def get_all_operations_grouping_by_symbol():
        operationsBySimbol = []
        for symbol in dao.get_all_symbols():
            operationsBySimbol.append(dao.get_operations_by_symbol(symbol))
        return operationsBySimbol