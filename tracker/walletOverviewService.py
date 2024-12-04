import decimal
from .externalCryptoPriceFetcher import ExternalCryptoPriceFetcher

class WalletOverviewService():
    def process(self, allOperations):
        walletOverview = {}
        for operationsGroupedByCrypto in allOperations:
            if not operationsGroupedByCrypto:
                continue
            symbol = operationsGroupedByCrypto[0].symbol
            amountOfHoldedCrypto = self.getCryptoHoldings(operationsGroupedByCrypto)
            totalCost, totalProceeds = self.getTotalCostAndProceeds(operationsGroupedByCrypto)
            actualMarketPrice = self.getActualMarketPrice(symbol)
            currentBalance = self.getCurrentBalance(amountOfHoldedCrypto, actualMarketPrice, totalCost, totalProceeds)
            walletOverview[symbol] = {
                'amountOfHoldedCrypto': amountOfHoldedCrypto,
                'totalCost': totalCost,
                'actualMarketPrice': actualMarketPrice,
                'currentBalance': currentBalance
            }
        walletOverview['totalBalance'] = self.getTotalBalance(walletOverview)
        return walletOverview

    def getCryptoHoldings(self, operationsGroupedByCrypto):
        availableCrypto = decimal.Decimal(0)
        for operation in operationsGroupedByCrypto:
            if operation.isSell:
                availableCrypto -= decimal.Decimal(operation.cryptoQuantity)
            else:
                availableCrypto += decimal.Decimal(operation.cryptoQuantity)
        return availableCrypto

    def getTotalCostAndProceeds(self, operationsGroupedByCrypto):
        totalCost = decimal.Decimal(0)
        proceeds = decimal.Decimal(0)
        holdings = decimal.Decimal(0)
        for operation in operationsGroupedByCrypto:
            if operation.isSell:
                costPerUnit = totalCost / holdings if holdings > 0 else decimal.Decimal(0)
                totalCost -= costPerUnit * decimal.Decimal(operation.cryptoQuantity)
                proceeds += decimal.Decimal(operation.cryptoQuantity) * decimal.Decimal(operation.price)
                holdings -= decimal.Decimal(operation.cryptoQuantity)
            else:
                totalCost += decimal.Decimal(operation.cryptoQuantity) * decimal.Decimal(operation.price)
                holdings += decimal.Decimal(operation.cryptoQuantity)
        return totalCost, proceeds

    def getActualMarketPrice(self, symbol):
        externalCryptoPriceFetcher = ExternalCryptoPriceFetcher(symbolPair=str(symbol) + 'USDT')
        return externalCryptoPriceFetcher.getPrice()
    
    def getCurrentBalance(self, amountOfHoldedCrypto, actualMarketPrice, totalCost, totalProceeds):
        if not actualMarketPrice:
            return "Non available"
        currentValue = decimal.Decimal(amountOfHoldedCrypto) * decimal.Decimal(actualMarketPrice)
        return round(currentValue + totalProceeds - totalCost, 2)
    
    def getTotalBalance(self, wallet):
        totalBalance = 0
        for cryptocurrency, details in wallet.items():
            if details.get('currentBalance') == "Non available":
                continue
            totalBalance += details.get('currentBalance')
        return totalBalance