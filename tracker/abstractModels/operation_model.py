class OperationModel:
    def __init__(self, symbol, assetQuantity, price, isSell):
        self.__symbol = symbol
        self.assetQuantity = assetQuantity
        self.price = price
        self.isSell = isSell

    def getSymbol(self):
        return self.__symbol.symbol