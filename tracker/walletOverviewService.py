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
            symbolMarketPrice = self.getSymbolMarketPrice(symbol)
            currentBalance = self.getCurrentBalance(amountOfHoldedCrypto, symbolMarketPrice, totalCost, totalProceeds)
            walletOverview[str(symbol)] = { # Hay forma de no castearlo?
                'holdings': amountOfHoldedCrypto,
                'symbolMarketPrice': round(symbolMarketPrice, 2),
                'totalCost': round(totalCost, 2),
                'holdingsValue': round(float(amountOfHoldedCrypto) * float(symbolMarketPrice), 2),
                'currentBalance': currentBalance
            }
        walletOverview['totalBalance'] = self.getTotalBalance(walletOverview)
        return walletOverview

    def getCryptoHoldings(self, operationsGroupedByCrypto):
        availableCrypto = 0
        for operation in operationsGroupedByCrypto:
            if operation.isSell:
                availableCrypto -= operation.cryptoQuantity
            else:
                availableCrypto += operation.cryptoQuantity
        return availableCrypto

    def getTotalCostAndProceeds(self, operationsGroupedByCrypto):
        totalCost = 0
        proceeds = 0
        holdings = 0
        for operation in operationsGroupedByCrypto:
            if operation.isSell:
                costPerUnit = totalCost / holdings if holdings > 0 else 0
                totalCost -= costPerUnit * operation.cryptoQuantity
                proceeds += operation.cryptoQuantity * operation.price
                holdings -= operation.cryptoQuantity
            else:
                totalCost += operation.cryptoQuantity * operation.price
                holdings += operation.cryptoQuantity
        return totalCost, proceeds

    def getSymbolMarketPrice(self, symbol):
        externalCryptoPriceFetcher = ExternalCryptoPriceFetcher(symbol = symbol)
        return externalCryptoPriceFetcher.getPrice()
    
    def getCurrentBalance(self, amountOfHoldedCrypto, symbolMarketPrice, totalCost, totalProceeds):
        if not symbolMarketPrice:
            return "Non available"
        currentValue = float(amountOfHoldedCrypto) * float(symbolMarketPrice)
        return round(currentValue + totalProceeds - totalCost, 2)
    
    def getTotalBalance(self, wallet):
        totalBalance = 0
        for cryptocurrency, details in wallet.items():
            if details.get('currentBalance') == "Non available":
                continue
            totalBalance += details.get('currentBalance')
        return round(totalBalance, 2)